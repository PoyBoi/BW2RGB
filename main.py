import os, io, cv2, subprocess
from pathlib import Path
from PIL import Image
import subprocess
from scripts.colorizeCode import colorize
from scripts.denoiser import denoise_image

# print("Init location")

loc = r"..\Bringing-Old-Photos-Back-to-Life\test_images\old_w_scratch\b.png"
loc = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\input\6045292_orig.png"
loc_gen = r"C:\Users\parvs\VSC Codes\Python-root\BW2RGB\saved_siggraph17.png"
folder_2 = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\mask\PSD"
op_folder = r"C:\Users\parvs\VSC Codes\Python-root\AynAssg\outputs"
up_folder = r"C:\Users\parvs\VSC Codes\Python-root\AynAssg\results\restored_imgs"


'''
mode list:
1 - Scratch Detection
2 - Scratch Removal
3 - Image and Background upscaling
4 - Colorizing image + denoising
5 - Face Restoration

Note:
final_name is the other name for the name of the final location where the mask is stored, we get this from:
    loc:            We scrape the name of the image from this
    os.path.join:   We use this to compound the name of the file that we got, check for it's existance locally, and then we look in the masks folder for it's exist

IMP:
Might want to import this to the flask app, but instead just taking the image name, raise flag for "check local"
'''

def localTest(mode:int, final_name:str):
    # mode_list = int(input())
    image_path = Path(loc)
    image_name = image_path.name
    file_nam = print(str(image_name))

    print(folder_2, file_nam)
    final_name = os.path.join(folder_2, image_name)

    # Define the other folder
    other_folder = Path(folder_2)
    print(str(other_folder))

    if (other_folder / image_name).exists():
        print(f"{image_name} exists in {other_folder}")
    else:
        print(f"{image_name} does not exist in {other_folder}")

# Scratch Detection
# if mode_list == 1:
def scrDet(final_name):
    # img_read = cv2.imread(loc)
    # cv2.imshow('image', img_read)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    print(final_name)
    img = cv2.imread(final_name)
    # print("IMG size = ", img_read.shape)
    # cv2.imshow('Image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return img

# Scratch Removal Using SD
# elif mode_list == 2:
def scrRem(final_name, loc_gen):
    # img_read = cv2.imread(loc_gen)
    # print("IMG size = ", img_read.shape)
    # cv2.imshow('image', img_read)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    completed_process = subprocess.run([
        "cd", r"C:\Users\parvs\VSC Codes\Python-root\AynAssg", "&&",
        "python", "main.py", "--b", 
        "--p", "clean picture, smooth picture, same color", 
        "--k", "{}".format(final_name), 
        "--f", loc_gen, 
        "--n", "An image without cracks and scratches with no gaps, white lines, scratches, folds, embelishment, dirty, gaps, bad photo", 
        "--l", "AynAssg\\models\\diffused\\realisticVisionV60B1", 
        "-cfg", "7", 
        "-steps", "50",
        "-method", "1"
    ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    output = completed_process.stdout
    # error_output = completed_process.stderr

    final_output = os.path.join(op_folder,output.split("brk")[1])
    # print(final_output)
    img_read = cv2.imread(final_output)

    # print(img_read.dtype)

    return img_read

# Image and Background Upscaling
# elif mode_list == 3:
def imgUp(loc_gen):
    # img_read = cv2.imread(loc_gen)
    # print("IMG size = ", img_read.shape)
    # cv2.imshow('image', img_read)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    completed_process = subprocess.run([
        "cd", r"C:\Users\parvs\VSC Codes\Python-root\AynAssg", "&&",
        "python", "main.py", 
        "--u", "2", 
        "--f", loc_gen, 

    ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    output = completed_process.stdout

    final_output = os.path.join(up_folder,output.split("brk")[1])
    # print(final_output)
    img_read = cv2.imread(final_output)

    # print(img_read.dtype)

    return img_read

# Denoising + Colorizing Image
# elif mode_list == 4:
def imgClr(loc):
    # img_read = cv2.imread(loc)
    # print("IMG size = ", img_read.shape)
    # cv2.imshow('image', img_read)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    den_img = denoise_image(loc, denoise_method="nlm", h=3)

    # print("Denoising Image size = ", den_img[0].shape)

    ret_img = colorize(
        img_obj=den_img[0], 
        file_org=den_img[1],
        file_loc= None,
        is_img = True,
        method = 1,
        show_graph = False,
        save_image = False,
        use_gpu = True
    )

    # print("Colorized Image size = ", ret_img[1].shape)

    for i in range(len(ret_img)):
        img_rgb = cv2.cvtColor(ret_img[i], cv2.COLOR_BGR2RGB)
        # cv2.imshow("Image", img_rgb)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        # This was an attempt to save the images, but for some reason they are black, and I only need SIGGRAPH, so decided to not go forward with it
        # output_dir = r"C:\Users\parvs\VSC Codes\Python-root\BW2RGB\images\test"
        # cv2.imwrite(os.path.join(output_dir, f'output_image_{i}.jpg'), img_rgb)

    return img_rgb

# Face Restoration
# elif mode_list == 5:
def imgRes(loc_gen):
    # img_read = cv2.imread(loc_gen)
    # print("IMG size = ", img_read.shape)
    # cv2.imshow('image', img_read)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    completed_process = subprocess.run([
        "cd", r"C:\Users\parvs\VSC Codes\Python-root\AynAssg", "&&",
        "python", "main.py", 
        "--u", "1", 
        "--f", loc_gen, 

    ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    output = completed_process.stdout
    # error_output = completed_process.stderr

    final_output = os.path.join(up_folder,output.split("brk")[1])
    
    print(final_output)
    img_read = cv2.imread(final_output)

    print(img_read.dtype)

    return img_read


#__main__
# op = scrDet(r"C:\Users\parvs\VSC Codes\Python-root\BW2RGB\saved_siggraph17.png")
# op = scrRem(r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\mask\PSD\scratch_removal_automatic_1.png", r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\input\scratch_removal_automatic_1.png")
# op = imgUp(r"C:\Users\parvs\VSC Codes\Python-root\BW2RGB\saved_siggraph17.png")
# op = imgClr(r"C:\Users\parvs\VSC Codes\Python-root\BW2RGB\saved_siggraph17.png")
# op = imgRes(r"C:\Users\parvs\VSC Codes\Python-root\BW2RGB\saved_siggraph17.png")
# op.show()
# print(op)


# print("BREAK")
# im = cv2.imshow("img", op)
# cv2.waitKey(0)
# cv2.destroyAllWindows()