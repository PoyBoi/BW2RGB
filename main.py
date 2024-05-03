import os
import cv2
from pathlib import Path
import subprocess
from scripts.colorizeCode import colorize
from scripts.denoiser import denoise_image

print("Init location")

loc = r"..\Bringing-Old-Photos-Back-to-Life\test_images\old_w_scratch\b.png"
loc = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\input\6045292_orig.png"
loc_gen = r"C:\Users\parvs\VSC Codes\Python-root\BW2RGB\saved_siggraph17.png"
folder_2 = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\mask"

'''
mode list:
1 - Scratch Detection
2 - Scratch Removal
3 - Image and Background upscaling
4 - Colorizing image + denoising
5 - Face Restoration
'''

mode_list = int(input())

img_read = cv2.imread(loc)
# cv2.imshow('image', img_read)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print("IMG size = ", img_read.shape)

image_path = Path(loc)
image_name = image_path.name
file_nam = print(str(image_name))

print(folder_2, file_nam)
final_name = os.path.join(folder_2, image_name)

# Define the other folder
other_folder = Path(folder_2)
print(str(other_folder))

# Check if the image exists in the other folder
if (other_folder / image_name).exists():
    print(f"{image_name} exists in {other_folder}")
else:
    print(f"{image_name} does not exist in {other_folder}")

# Scratch Detection
if mode_list == 1:
    img_read = cv2.imread(loc)
    cv2.imshow('image', img_read)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(final_name)
    img = cv2.imread(final_name)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Scratch Removal Using SD
elif mode_list == 2:
    img_read = cv2.imread(loc_gen)
    cv2.imshow('image', img_read)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Just for a dry run
    subprocess.run([
        "cd", r"C:\Users\parvs\VSC Codes\Python-root\AynAssg", "&&",
        "python", "main.py", "--b", 
        "--p", "clean picture, smooth picture, same color", 
        "--k", "{}".format(final_name), 
        "--f", loc_gen, 
        "--n", "An image without cracks and scratches with no gaps, white lines, scratches, folds, embelishment, dirty, gaps, bad photo", 
        "--l", "AynAssg\\models\\diffused\\realisticVisionV60B1", 
        # "-cfg", 7, 
        # "-steps", 50
    ], shell=True)

# Image and Background Upscaling
elif mode_list == 3:
    img_read = cv2.imread(loc_gen)
    cv2.imshow('image', img_read)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #  python main.py --u 4 -f "C:\Users\parvs\VSC Codes\Python-root\AynAssg\outputs\miscHosted\output_bg_20240406_045718.png"  
    subprocess.run([
        "cd", r"C:\Users\parvs\VSC Codes\Python-root\AynAssg", "&&",
        "python", "main.py", 
        "--u", "3", 
        # "--p", "clean picture, smooth picture, same color", 
        # "--k", "{}".format(str(folder_2 / image_name)), 
        "--f", loc_gen, 
        # "--n", "An image without cracks and scratches with no gaps, white lines, scratches, folds, embelishment, dirty, gaps, bad photo", 
        # "--l", "AynAssg\\models\\diffused\\realisticVisionV60B1", 
        # "-cfg", "7", 
        # "-steps", "50"

    ], shell=True)

# Denoising + Colorizing Image
elif mode_list == 4:
    img_read = cv2.imread(loc)
    cv2.imshow('image', img_read)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    den_img = denoise_image(loc, denoise_method="nlm", h=3)

    print("Denoising Image size = ", den_img[0].shape)

    ret_img = colorize(
        img_obj=den_img[0], 
        file_org=den_img[1],
        #r"C:\Users\parvs\VSC Codes\Python-root\Bringing-Old-Photos-Back-to-Life\test_images\old_w_scratch\b.png", 
        file_loc= None,
        is_img = True,
        method = 1,
        show_graph = True,
        save_image = True,
        use_gpu = True
    )

    print("Colorized Image size = ", ret_img[1].shape)

    for i in range(len(ret_img)):
        img_rgb = cv2.cvtColor(ret_img[i], cv2.COLOR_BGR2RGB)
        cv2.imshow("Image", img_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Face Restoration
elif mode_list == 5:
    img_read = cv2.imread(loc_gen)
    cv2.imshow('image', img_read)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    subprocess.run([
        "cd", r"C:\Users\parvs\VSC Codes\Python-root\AynAssg", "&&",
        "python", "main.py", 
        "--u", "1", 
        # "--p", "clean picture, smooth picture, same color", 
        # "--k", "{}".format(str(folder_2 / image_name)), 
        "--f", loc_gen, 
        # "--n", "An image without cracks and scratches with no gaps, white lines, scratches, folds, embelishment, dirty, gaps, bad photo", 
        # "--l", "AynAssg\\models\\diffused\\realisticVisionV60B1", 
        # "-cfg", "7", 
        # "-steps", "50"

    ], shell=True)

# cv2.imwrite("./test.png", (cv2.cvtColor(ret_img[1], cv2.COLOR_BGR2RGB)))

