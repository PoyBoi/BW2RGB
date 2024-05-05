# What are deliverables:

1. [x] Remove scratches from images
   1. [x] Take images from the model and get their masks, see if they are any good and then fine tune them
   2. [x] Fine tune those masks via photoshop
   3. [x] Use data augmentation to get more pictures from the same dataset
      1. Turn it into a TIFF image if needed (IDTS)
   4. [x] Run a UNet on it
      1. [x] Check how well it works on images
2. [x] BW to RGB conversion
   1. [x] Denoise the image
   2. [x] Check the older repo for how colorization was done, apply it here, ezpz
   3. [x] Add denoising
   4. [ ] Add mask blurring and check the output quality
   5. [x] Save the steps saves of the images
3. use GFP GAN like in AYNASSG to upscale faces and background of image
   1. Optional: Make the face upscaling thing yourself
   2. [x] Make a CMD call to AYNASSG for this
4. Color correction / restoration of images 
5. Image Upscaling
6. Finishing it all up:
   1. [x] Deploy SD and masking from AynAssg for filling in the masked parts of the images
   2. Try deploying this on Modal
   3. [ ] Try to make a thing where it can change the BG of the image
7. [ ] Integrate AynAssg into the pipeline and in the docs as well
8. [x] Hide the usage of the mask straight up
9. [ ] For the flask app:
   1. [ ] Convert the image from and to bit stream INSIDE the server app (make the bits into an image, and then pass it into the function call)
      1. [x] Add the args into the func definitions
      2. [ ] Save the image as a temp so it can be passed around via location
   2. [ ] Use that to pass it into the functions
   3. [x] Turn all the elif's into methods
      1. [ ] use the above stated thing to fill into the app from main.py
   4. [x] See how to call those methods from inside the server app
   5. [ ] Need to clean up locations


# Misc:

1. Links:
   1. [Link to the MS OpenSource repo](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life)
   2. [Link to the vercel app deployment](https://restoring-images.vercel.app/)
   3. [Video for small dataset semantic segmentation and UNet](https://www.youtube.com/watch?v=-XeKG_T6tdc)

2. Contributions to the open-source project:
   1. Line 219 in align_warp_back_multiple_dlib.py
   ```
   mask = mask.astype(np.float64)
   mask *= 255.0
   mask = mask.astype(np.uint8)
   ```
   2. Upgrading the dependancies:
      1. Check the log screen for which ones to upgrade (mostly pillow files)
   3. Check in updates for the ```requirements.txt```
   4. Try to get the download links for all the things and setting them up (which I had to do)
   5. Upgrading the front end for users