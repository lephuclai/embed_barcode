import cv2
import numpy as np

cap = cv2.VideoCapture('input.mp4')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('output.mp4', 0x7634706d, 24.0, (frame_width, frame_height))

i = 0
while(cap.isOpened()):
    barcode_img = cv2.imread('Barcode/Code/new_code' + str(i) + '.png')
    height, width, channel = barcode_img.shape
        
    offset = np.array((900, 1050))
    
    ret, frame = cap.read()
    
    frame[offset[0]:offset[0] + height, offset[1]:offset[1] + width] = barcode_img
    
    out.write(frame)
    
    cv2.imshow('Vid', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    i += 1

cap.release()
out.release()
cv2.destroyAllWindows()

    