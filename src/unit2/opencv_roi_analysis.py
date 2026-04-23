import cv2
import numpy as np

height, width = 240, 320
x = np.linspace(0, 255, width, dtype=np.uint8)
gradient = np.tile(x, (height, 1))
image = cv2.merge([gradient, gradient, gradient])

cv2.rectangle(image, (100, 60), (220, 180), (0, 0, 255), 3)
roi = image[60:180, 100:220]
blurred_roi = cv2.GaussianBlur(roi, (15, 15), 0)
image[60:180, 100:220] = blurred_roi

mean_intensity = roi.mean()
cv2.imwrite("opencv_roi_blur.png", image)

print("Saved opencv_roi_blur.png")
print("ROI shape:", roi.shape)
print("Mean intensity inside ROI:", round(float(mean_intensity), 2))
