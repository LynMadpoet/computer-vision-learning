from pathlib import Path
import cv2

#read image
lesson_folder = Path(__file__).resolve().parent
image_path1 = lesson_folder/"data"/"toto.jpg"
img1 = cv2.imread(str(image_path1))

if img1 is None:
    raise FileNotFoundError(f"Image does not exist:{image_path1}")

img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

# write image 
image_path2 = lesson_folder/"outputs"/"totogray.jpg"
write_sucess = cv2.imwrite(image_path2,img_gray)

if not write_sucess:
    raise IOError(f"Image not savable",{image_path2})

cv2.imshow('Frame',img_gray)
cv2.waitKey(0)