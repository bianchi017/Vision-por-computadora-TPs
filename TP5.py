import cv2

drawing = False
ix, iy = -1, -1


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1)


img = cv2.imread('gamer.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'):
        cv2.imwrite('gamer_tp5.jpg', img)
        print('Imagen guardada como gamer_tp5.jpg')
        break
    elif k == ord('r'):
        img = cv2.imread('gamer.jpg', cv2.IMREAD_COLOR)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image', draw_rectangle)
        print('Restaurando imagen original')
    elif k == ord('q'):
        break
cv2.destroyAllWindows()
