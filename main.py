import io
import os
from flask import Flask, request, send_file
import qrcode

application = Flask(__name__)

def generate_qr(url):
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4)

    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    return img

@application.route("/")
def r_qrcode():

    url = request.args.get('url', default='https://www.google.com')

    img_buf = io.BytesIO()
    img = generate_qr(url)
    img.save(img_buf)
    img_buf.seek(0)
    return send_file(img_buf, mimetype='image/png')

# run the app.
if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
