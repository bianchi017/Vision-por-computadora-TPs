import cv2
import numpy as np

imagen = cv2.imread('monedas-naipes.jpg', cv2.IMREAD_COLOR)
# Convertir la imagen en escala de grises
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
# Convertir la imagen en binaria
canny = cv2.Canny(gray, 10, 150)
# Aplicar dilatación y erosión a la imagen para mayor precisión al detectar vértices
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
# Detectar los contornos de los objetos en la imagen
cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # en OpenCV 4
# c (contorno a analizar), epsilon (precisión de aproximación)
for c in cnts:
    # Establecer un porcentaje de aproximación
    epsilon = 0.01 * cv2.arcLength(c, True)  # True (curva cerrada) o False (curva no cerrada)
    approx = cv2.approxPolyDP(c, epsilon, True)
    x, y, w, h = cv2.boundingRect(approx)
    # Averiguar la cantidad de vértices detectados del objeto
    if len(approx) == 4:
        aspectRatio = float(w) / h

        if aspectRatio == 1:
            cv2.putText(imagen, 'Cuadrado', (x + 20, y - 20), 1, 1, (0, 0, 0), 1)
            cv2.putText(imagen, "(ancho: " + str(w) + ", alto: " + str(h) + ")", (x - 40, y - 5), 1, 1, (0, 0, 0), 1)
            cv2.drawContours(imagen, [approx], 0, (0, 0, 0), 2)
            print('Cuadrado: ancho,alto =', w, h, 'píxeles')
        else:
            cv2.putText(imagen, 'Rectangulo', (x + 70, y - 20), 1, 1, (0, 0, 0), 1)
            cv2.putText(imagen, "(ancho: " + str(w) + ", alto: " + str(h) + ")", (x + 20, y - 5), 1, 1, (0, 0, 0), 1)
            cv2.drawContours(imagen, [approx], 0, (0, 0, 0), 2)
            print('Rectángulo: ancho,alto =', w, h, 'píxeles')

    if len(approx) > 10:
        area = cv2.contourArea(c)
        radio = np.sqrt(area / np.pi)
        cv2.putText(imagen, 'Circulo', (x + 15, y - 20), 1, 1, (0, 0, 0), 1)
        cv2.putText(imagen, "(radio: " + str(int(round(radio))) + ")", (x - 1, y - 5), 1, 1, (0, 0, 0), 1)
        cv2.drawContours(imagen, [approx], 0, (0, 0, 0), 2)
        print('Círculo: radio =', int(round(radio)), 'píxeles')

# Mostrar el resultado
while 1:
    cv2.imshow('Resultado', imagen)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:
        break
cv2.destroyAllWindows()
