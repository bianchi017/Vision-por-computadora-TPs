import cv2

img = cv2.imread('hoja.png', 0)
thr = 200

for i, row in enumerate(img):
    for j, col in enumerate(row):
        if col >= thr:
            img[i, j] = 255
        else:
            img[i, j] = 0
cv2.imwrite('resultado.png', img)
cv2.imshow('Resultado', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
