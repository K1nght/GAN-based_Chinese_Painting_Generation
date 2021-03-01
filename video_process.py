import numpy as np
import cv2

cap = cv2.VideoCapture('test.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
height = int(cap.get(4))
width = int(cap.get(3))
print(height,width)
fps = cap.get(5)
print(fps)
out = cv2.VideoWriter('testwrite.mp4', fourcc, fps, (width, height))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        cv2.imshow('frame', frame)
        ####################use transfer function to frame

        trans_frame = Function(frame)


        out.write(trans_frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
