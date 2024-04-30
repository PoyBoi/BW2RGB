import cv2
import numpy as np

def denoise_image(image_path, denoise_method="median", ksize=5, sigmaColor=75, sigmaSpace=75, h=10):
  img = cv2.imread(image_path)

  if img is None:
      print("Error reading image!")
      return None

  # Preprocessing (optional)
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # For some denoising methods
  img_float = img.astype(np.float32) / 255.0  # Normalization (optional)

  # Denoising based on chosen method
  if denoise_method == "median":
      denoised_img = cv2.medianBlur(gray_img if denoise_method in ["median"] else img, ksize=ksize)
  elif denoise_method == "bilateral":
      denoised_img = cv2.bilateralFiltering(img_float, d=9, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)
  elif denoise_method == "nlm":
      denoised_img = cv2.fastNlMeansDenoisingColored(img, None, h, 10, 7, 21)
  else:
      print(f"Invalid denoise_method: {denoise_method}. Using median blur instead.")
      denoised_img = cv2.medianBlur(gray_img, ksize=ksize)

  return denoised_img

# Example usage (replace with your image path and desired method/parameters)
denoised_image = denoise_image("path/to/your/image.jpg", denoise_method="bilateral", sigmaColor=50, sigmaSpace=50)