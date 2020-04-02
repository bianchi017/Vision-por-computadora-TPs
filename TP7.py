import cv2
import numpy as np

imagen = cv2.imread('gamer.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Imagen original', imagen)


def transformaciónEuclidiana(img, angle, tx, ty, s):
    (h, w) = img.shape[: 2]
    center = None
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, s)
    imagenRotadaEscalada = cv2.warpAffine(img, M, (w, h))

    (h, w) = (imagenRotadaEscalada.shape[0], imagenRotadaEscalada.shape[1])

    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])
    imagenFinal = cv2.warpAffine(imagenRotadaEscalada, M, (w, h))

    cv2.imshow('Imagen trasladada, rotada y escalada', imagenFinal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('Imagen trasladada, rotada y escalada ')
    print('Ángulo:', angle, '°')
    print('Traslación en X:', tx)
    print('Traslación en Y:', ty)
    print('Escala:', s)
    return imagenFinal


transformaciónEuclidiana(imagen, 180, 110, 180, 2)
