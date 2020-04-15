import cv2
import numpy as np

i = 1
x1, y1 = 0, 0
x2, y2 = 0, 0
x3, y3 = 0, 0

print('Seleccione tres puntos de la imagen')
print('Puntos elegidos (x,y):')


def seleccionarPuntos(event, x, y, flags, params):
    global i, x1, y1, x2, y2, x3, y3
    if event == cv2.EVENT_LBUTTONDOWN:
        if i == 1:
            x1, y1 = x, y
            cv2.circle(imagen1, (x1, y1), 2, (0, 0, 255), -1)
            i += 1
            print('Punto 1:', x1, y1)
        elif i == 2:
            x2, y2 = x, y
            cv2.circle(imagen1, (x2, y2), 2, (0, 0, 255), -1)
            i += 1
            print('Punto 2:', x2, y2)
        elif i == 3:
            x3, y3 = x, y
            cv2.circle(imagen1, (x3, y3), 2, (0, 0, 255), -1)
            i += 1
            print('Punto 3:', x3, y3)


imagen1 = cv2.imread('gamer.jpg', cv2.IMREAD_COLOR)
imagen2 = cv2.imread("meme.jpg", cv2.IMREAD_COLOR)
cv2.namedWindow('Imagen original')
cv2.setMouseCallback('Imagen original', seleccionarPuntos)

while 1:
    cv2.imshow('Imagen original', imagen1)
    if i == 4:
        # src = coordenadas de los puntos en la imagen original.
        src = np.float32([[0, 0], [imagen2.shape[1], 0], [0, imagen2.shape[0]]])
        # dst = coordenadas de los puntos en la imagen final.
        dst = np.float32([[x1, y1], [x2, y2], [x3, y3]])
        # Obtención de matriz para transformación.
        matriz = cv2.getAffineTransform(src, dst)
        # Aplicar transformación afín.
        incrustada = cv2.warpAffine(imagen2, matriz, (imagen1.shape[1], imagen1.shape[0]))
        # Crear máscara e invertir.
        hsv = cv2.cvtColor(incrustada, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(hsv, 10, 255, cv2.THRESH_BINARY)
        maskInv = cv2.bitwise_not(mask)
        # Creación de la imagen final.
        imagenEnmascarada = cv2.bitwise_and(imagen1, imagen1, mask=maskInv)
        incrustarEnmascarada = cv2.bitwise_and(incrustada, incrustada, mask=mask)
        imagenFinal = cv2.add(imagenEnmascarada, incrustarEnmascarada)
        cv2.imshow('Imagen final', imagenFinal)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
