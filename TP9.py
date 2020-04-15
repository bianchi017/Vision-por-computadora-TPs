import cv2
import numpy as np

i = 1
x1, y1 = 0, 0
x2, y2 = 0, 0
x3, y3 = 0, 0
x4, y4 = 0, 0

print('Seleccione cuatro puntos de la imagen en sentido horario')
print('Puntos elegidos (x,y):')


def seleccionarPuntos(event, x, y, flags, params):
    global i, x1, y1, x2, y2, x3, y3, x4, y4
    if event == cv2.EVENT_LBUTTONDOWN:
        if i == 1:
            x1, y1 = x, y
            cv2.circle(imagen, (x1, y1), 2, (0, 0, 255), -1)
            i += 1
            print('Punto 1:', x1, y1)
        elif i == 2:
            x2, y2 = x, y
            cv2.circle(imagen, (x2, y2), 2, (0, 0, 255), -1)
            i += 1
            print('Punto 2:', x2, y2)
        elif i == 3:
            x3, y3 = x, y
            cv2.circle(imagen, (x3, y3), 2, (0, 0, 255), -1)
            i += 1
            print('Punto 3:', x3, y3)
        elif i == 4:
            x4, y4 = x, y
            cv2.circle(imagen, (x4, y4), 2, (0, 0, 255), -1)
            i += 1
            print('Punto 4:', x4, y4)


imagen = cv2.imread('gameboy.jpg', cv2.IMREAD_COLOR)
rows, cols, channel = imagen.shape
cv2.namedWindow('Imagen original')
cv2.setMouseCallback('Imagen original', seleccionarPuntos)

while 1:
    cv2.imshow('Imagen original', imagen)
    if i == 5:
        # src = Coordenadas de los puntos en la imagen original.
        src = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
        # dst = Coordenadas de los puntos en la imagen final.
        dst = np.float32([[0, 0], [300, 0], [300, 300], [0, 300]])
        # Obtención de matriz para transformación.
        matriz = cv2.getPerspectiveTransform(src, dst)
        # Resultado de la imagen transformada.
        imagenFinal = cv2.warpPerspective(imagen, matriz, (300, 300))
        cv2.imshow('Transformacion Perspectiva', imagenFinal)
        i = 1
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
