import cv2

img0 = cv2.imread('Resources/logo.png')
img1 = cv2.imread('Resources/painting.png')
h_wm, w_wm, _ =img0.shape
cv2.imshow("watermark",img0)
cv2.waitKey(0)

#_ when value is not needed, here its channels
h_img, w_img,_ = img1.shape
print(h_img,w_img)

#top left point
center_y = int(h_img/2)
center_x = int(w_img/2)
top_y = center_y - int(h_wm/2)
left_x = center_x -int(w_wm/2)

#select ROI region of interest
#need the right bottom point

bottom_y = top_y + h_wm
right_x = left_x + w_wm

#extract the area btw these 2 points from original image
#preprocess roi
roi = img1[top_y:bottom_y, left_x:right_x]


#link the 2 images - roi and logo, give the logo opacity using add weighted
#roi,1 because 100%same and img0 0.5
result = cv2.addWeighted(roi,1,img0,0.5,0)
img1[top_y:bottom_y, left_x:right_x] = result

cv2.imshow("document",img1)
cv2.waitKey(0)
