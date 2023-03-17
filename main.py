import cv2  # pip install opencv-python
import numpy as np  # pip install numpy

video = cv2.VideoCapture('2.mp4')
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
threshold = 20.

writer = cv2.VideoWriter('final1.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 25, (width, height))
ret, frame1 = video.read()
prev_frame = frame1
count = 0
a = 0
b = 0
c = 0

while True:
    ret, frame = video.read()

    if ret is True:
        if (((np.sum(np.absolute(frame - prev_frame)) / np.size(frame)) > threshold)):
            writer.write(frame)
            prev_frame = frame
            a += 1
        else:
            prev_frame = frame
            b += 1

        cv2.imshow('hizlandirilmis video', frame)
        c += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Toplam frame adedi: ", c)
print("Benzeri olmayan frame adedi: ", a)
print("Ortak frame adedi: ", b)

video.release()
writer.release()
cv2.destroyAllWindows()
