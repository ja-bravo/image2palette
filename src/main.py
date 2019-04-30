from tools.image import getWithPalette
from flask import Flask, render_template, request, Response
import json
import re
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)


@app.route('/')
def frontend():
    return render_template('index.html')


@app.route('/palette', methods=['POST'])
def get_palette():
    imageData = json.loads(request.get_data())['data']
    imageData = re.sub("data:image/\w*;base64,", '', imageData)
    baseImage = Image.open(BytesIO(base64.b64decode(imageData)))
    newImage, colours = getWithPalette(baseImage)

    buffered = BytesIO()
    newImage = newImage.convert('RGB')
    newImage.save(buffered, format="JPEG")

    resp = {'data': base64.b64encode(buffered.getvalue()).decode("utf-8"), 'colours': colours}
    return Response(json.dumps(resp), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
