import os
import cv2
from scripts.colorizeCode import colorize
from scripts.denoiser import denoise_image

print("Init location")

loc = r"C:\Users\parvs\VSC Codes\Python-root\Bringing-Old-Photos-Back-to-Life\test_images\old_w_scratch\b.png"
loc = r"C:\Users\parvs\Downloads\Test\Done\stage_1_restore_output\masks\input\scratch_removal_automatic_1.png"

img_read = cv2.imread(loc)
cv2.imshow('image', img_read)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("IMG size = ", img_read.shape)

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
    # cv2.imshow("Image", img_rgb)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()