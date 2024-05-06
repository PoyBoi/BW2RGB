from flask import Flask, request, jsonify
from main import localTest, imgClr, imgRes, imgUp, scrDet, scrRem
from pathlib import Path
import os
from PIL import Image
from io import BytesIO
import base64
import cv2

app = Flask(__name__)

@app.route('/main_run', methods=['POST'])
def main_run():
    # Get the name of the image

    # API call block ======================================================================
    image_name = request.json['image_name']
    mode = int(request.json['mode'])
    image = request.json['image']

    # Block to convert image's bytes to images ============================================
    loc = r"C:\Users\parvs\VSC Codes\Python-root\BW2RGB\images.temp_1.jpg"
    image_bytes = base64.b64decode(image)
    image = Image.open(BytesIO(image_bytes))
    # image.show()
    # loc: Name of the file that has been saved and has to be used, can be passed directly as a path
    image.save(loc)
    
    # Block to check for image existance ==================================================
    if mode == 1 or mode == 2:
        file_nam = str(image_name)

        folder_2 = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\mask\PSD"
        
        print(folder_2, file_nam)
        final_name = os.path.join(folder_2, file_nam)

        # Define the other folder
        other_folder = Path(folder_2)
        print(str(other_folder))

        if (other_folder / image_name).exists():
            print(f"{image_name} exists in {other_folder}")
        else:
            print(f"{image_name} does not exist in {other_folder}")

    # Call the appropriate function based on the mode =====================================
    if mode == 1:
        # Mask file name
        op = scrDet(final_name)
    elif mode == 2:
        # Mask loc, Img loc
        op = scrRem(final_name, loc)
    elif mode == 3:
        op = imgUp(loc)
    elif mode == 4:
        op = imgClr(loc)
    elif mode == 5:
        op = imgRes(loc)
    else:
        return jsonify({"Error": "Incorrect Method passed"})

    # print(op.dtype)
    # return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

    # Block that turns BGR to RGB =========================================================
    img_rgb = cv2.cvtColor(op, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    # img_pil.show()

    # Block that converts the image into Bytes ============================================
    byte_arr = BytesIO()
    img_pil.save(byte_arr, format='JPEG')
    img_byte_arr = byte_arr.getvalue()
    print(img_byte_arr)

    print("=======================================\nAlmost Done\n=======================================\n")

    img_str = base64.b64encode(img_byte_arr).decode()
    return jsonify({"image": img_str})

if __name__ == '__main__':
    app.run(debug=True)