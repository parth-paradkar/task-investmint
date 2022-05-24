from flask import Flask, request
import requests
import shutil
from PIL import Image


app = Flask(__name__)


@app.route("/api")
def handle():
    args = request.args

    url = args.get("url")
    height = int(args.get("height"))
    width = int(args.get("width"))

    response = requests.get(url, stream=True)
    with open('download.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    try:
        with Image.open("download.png") as img:
            img_resized = img.resize((width, height))
            img_resized.save("download_resized.png")

        return {"status": 200}

    except Exception as e:
        print(e)
        return {"status": 500}


app.run()
