import cv2
import numpy as np

drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(' image ')
cv2.setMouseCallback(' image ', draw_rectangle)

while 1:
    cv2.imshow(' image ', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'):
        cv2.imwrite('TP5.png', img)
        print('Imagen guardada como TP5.png')
        break
    elif k == ord('r'):
        img = np.zeros((512, 512, 3), np.uint8)
        cv2.namedWindow(' image ')
        cv2.setMouseCallback(' image ', draw_rectangle)
        print('Restaurando imagen original')
    elif k == ord('q'):
        break
cv2.destroyAllWindows()
