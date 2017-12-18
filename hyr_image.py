import cv2
import numpy as np

#***************** Functions **************

#************** Start Programs ************
pdir = "../"
f = "B3_P5_T5_mesh3_011.tif"
#2048 x 2048; 16-bit; 8MB
fpath = pdir+f

img = cv2.imread(fpath,-1)
print(img.shape)   #check image type
maxI = np.amax(np.amax(img))
minI = np.amin(np.amin(img))
imgS = cv2.resize(img,(512,512))
imgS = cv2.convertScaleAbs(imgS, alpha=(255.0/65535.0))
print(np.amax(np.amax(imgS)))
print(np.amin(np.amin(imgS)))
cv2.imshow(f,imgS)
ret, imgS2 = cv2.threshold(imgS,177,255,cv2.THRESH_BINARY_INV)
#****** Trackbar **********
def nothing(x):
	pass
cv2.createTrackbar('Brightness',f,0,255,nothing)
cv2.createTrackbar('Contrast',f,0,30000,nothing)
switch = '0:OFF \n1:ON'
cv2.createTrackbar(switch,f,0,1,nothing)

while(1):
	cv2.imshow(f,imgS)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	brightness  = cv2.getTrackbarPos('Brightness',f)
	contrast = cv2.getTrackbarPos('Contrast',f)
	print(brightness, contrast)
	s = cv2.getTrackbarPos(switch,f)
	if s == 0:
		pass
	else:
		imgS2 = cv2.multiply(imgS,contrast/1000)
		final = cv2.add(imgS2,brightness)
		cv2.imshow("adjusted "+f,final)
		k = cv2.waitKey(1) & 0xFF
		if k== 27:
			break
cv2.waitKey()&0xFF
cv2.destroyAllWindows()
