from flask import Flask, request
from main import scratch_detection, scratch_removal, image_upscaling, denoise_colorize, face_restoration
from pathlib import Path
import os

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the name of the image
    image_name = None
    file_nam = str(image_name)

    folder_2 = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\mask"
    
    print(folder_2, file_nam)
    final_name = os.path.join(folder_2, image_name)

    # Define the other folder
    other_folder = Path(folder_2)
    print(str(other_folder))

    if (other_folder / image_name).exists():
        print(f"{image_name} exists in {other_folder}")
    else:
        print(f"{image_name} does not exist in {other_folder}")
    mode = int(request.json['mode'])

    # Get the image path from the request data
    image_path = request.json['image_path']

    # Call the appropriate function based on the mode
    if mode == 1:
        scratch_detection(image_path, final_name)
    elif mode == 2:
        scratch_removal(final_name, loc_gen)
    elif mode == 3:
        image_upscaling(loc_gen)
    elif mode == 4:
        denoise_colorize(loc)
    elif mode == 5:
        face_restoration(loc_gen)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(debug=True)