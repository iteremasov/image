from bottle import route, run, template, SimpleTemplate, static_file, response
from PIL import Image
import io


@route('/img/<width>/<height>')
def img_gen(width, height):
    height = int(height)
    width = int(width)
    img = Image.new("RGB", (height, width), (0, 0, 0))
    ff = io.BytesIO()
    img.save(ff, 'jpeg')
    bytes_img = ff.getvalue()
    response.content_type = 'image/jpeg'
    response.content_length = len(bytes_img)
    return bytes_img



@route('/statistic')
def get_statistic(request):

    return

run(host='localhost', port=8000)
