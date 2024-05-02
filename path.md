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
   3. [ ] Add denoising
   4. [ ] Add mask blurring and check the output quality
3. use GFP GAN like in AYNASSG to upscale faces and background of image
   1. Optional: Make the face upscaling thing yourself
4. Color correction / restoration of images 
5. Image Upscaling
6. Finishing it all up:
   1. Deploy SD and masking from AynAssg for filling in the masked parts of the images
   2. Try deploying this on Modal
   3. Try to make a thing where it can change the BG of the image



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