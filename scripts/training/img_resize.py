import os
import cv2

mask_path = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\mask\PSD"
img_path = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\input"

# Specify the directories where the resized images will be saved
resized_mask_path = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\Training\mask_resized"
resized_img_path = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\Training\input_resized"

# Create the directories if they don't exist
os.makedirs(resized_mask_path, exist_ok=True)
os.makedirs(resized_img_path, exist_ok=True)

# Get a list of all image files in the directories
mask_files = os.listdir(mask_path)
img_files = os.listdir(img_path)

# Resize all mask images
for file in mask_files:
    img = cv2.imread(os.path.join(mask_path, file))
    resized_img = cv2.resize(img, (768, 1024))
    cv2.imwrite(os.path.join(resized_mask_path, file), resized_img)

# Resize all input images
for file in img_files:
    img = cv2.imread(os.path.join(img_path, file))
    resized_img = cv2.resize(img, (768, 1024))
    cv2.imwrite(os.path.join(resized_img_path, file), resized_img)