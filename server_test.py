from flask import Flask, request
from main import localTest, imgClr, imgRes, imgUp, scrDet, scrRem
from pathlib import Path
import os
from PIL import Image

app = Flask(__name__)

@app.route('/main_run', methods=['POST'])
def main_run():
    # Get the name of the image
    image_name = request.json['image_name']
    mode = int(request.json['mode'])
    image = request.json['image']

    # block to convert image's bytes to images
    
    # block to check for image existance
    file_nam = str(image_name)

    folder_2 = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\mask\PSD"
    
    print(folder_2, file_nam)
    final_name = os.path.join(folder_2, image_name)

    # Define the other folder
    other_folder = Path(folder_2)
    print(str(other_folder))

    if (other_folder / image_name).exists():
        print(f"{image_name} exists in {other_folder}")
    else:
        print(f"{image_name} does not exist in {other_folder}")

    # Call the appropriate function based on the mode
    if mode == 1:
        scrDet(image_path, final_name)
    elif mode == 2:
        scrRem(final_name, loc_gen)
    elif mode == 3:
        imgUp(loc_gen)
    elif mode == 4:
        imgClr(loc)
    elif mode == 5:
        imgRes(loc_gen)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(debug=True)