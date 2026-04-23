import cv2
import numpy as np

canvas = np.zeros((300, 400, 3), dtype=np.uint8)
canvas[:] = (30, 30, 30)

cv2.rectangle(canvas, (40, 40), (180, 180), (0, 180, 255), thickness=-1)
cv2.circle(canvas, (280, 120), 50, (255, 120, 0), thickness=-1)
cv2.putText(canvas, "CV", (140, 260), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 80, 160)

cv2.imwrite("opencv_generated_scene.png", canvas)
cv2.imwrite("opencv_generated_edges.png", edges)

print("Saved opencv_generated_scene.png and opencv_generated_edges.png")
print("Canvas shape:", canvas.shape)
print("Edge pixels:", int((edges > 0).sum()))
