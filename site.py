from bottle import route, run, template, SimpleTemplate, static_file, response
from PIL import Image
import io

width_record = 0
height_record = 0
recourse_record = 0




@route('/img/<width>/<height>')
def img_gen(width, height):
    global recourse_record
    global width_record
    global height_record
    recourse_record += 1
    height = int(height)
    width = int(width)
    width_record += width
    height_record += height
    img = Image.new("RGB", (height, width), (0, 0, 0))
    ff = io.BytesIO()
    img.save(ff, 'jpeg')
    bytes_img = ff.getvalue()
    response.content_type = 'image/jpeg'
    response.content_length = len(bytes_img)
    return bytes_img


@route('/stats')
def get_statistic():
    result_wigth = 0
    result_height = 0
    if recourse_record != 0:
        result_wigth = width_record / recourse_record
        result_height = height_record / recourse_record

    return template(
        '<h1>колличество посещений - {{g_coll}}</h>'
        '<h2>средняя ширина - {{result_wigth }}</h>'
        '<h2>средняя высота - {{result_height }}</h>',
        g_coll=recourse_record,
        result_wigth=result_wigth,
        result_height=result_height
    )


run(host='localhost', port=8000)
