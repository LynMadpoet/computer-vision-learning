import os
import cv2

#read image
image_path1 = os.path.join('.', 'data','toto.jpg')
img1 = cv2.imread(image_path1)

if img1 is None:
    raise FileNotFoundError(f"Image does not exist:{image_path1}")

img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

# write image 
image_path2 = os.path.join('.', 'outputs','mariogray.png')
write_sucess = cv2.imwrite(image_path2,img_gray)

if not write_sucess:
    raise IOError(f"Image not savable",{image_path2})

cv2.imshow('Frame',img1)
cv2.waitKey(0)