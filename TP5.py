import cv2

ix, iy = -1, -1


def recortarRectangulo(event, x, y, flags, param):
    global ix, iy, recorte
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 1)
        recorte = img[iy:y, ix:x]


img = cv2.imread('gamer.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('Imagen')
cv2.setMouseCallback('Imagen', recortarRectangulo)

while 1:
    cv2.imshow('Imagen', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('g'):
        cv2.imwrite('gamer_tp5.jpg', recorte)
        print('Imagen guardada como gamer_tp5.jpg')
        break
    elif k == ord('r'):
        img = cv2.imread('gamer.jpg', cv2.IMREAD_COLOR)
        cv2.namedWindow('Imagen')
        print('Restaurando imagen original')
    elif k == ord('q'):
        break
cv2.destroyAllWindows()
