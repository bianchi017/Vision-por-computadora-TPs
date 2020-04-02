import cv2
import numpy as np

imagen = cv2.imread('gamer.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Imagen original', imagen)


def transformaciónEuclidiana(img, angle, tx, ty):
    (h, w) = img.shape[: 2]
    center = None
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    imagenRotada = cv2.warpAffine(img, M, (w, h))

    (h, w) = (imagenRotada.shape[0], imagenRotada.shape[1])

    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])
    imagenFinal = cv2.warpAffine(imagenRotada, M, (w, h))

    cv2.imshow('Imagen trasladada y rotada (Transformacion Euclidiana)', imagenFinal)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('Imagen trasladada y rotada (Transformacion Euclidiana)')
    print('Ángulo:', angle, '°')
    print('Traslación en X:', tx)
    print('Traslación en Y:', ty)
    return imagenFinal


transformaciónEuclidiana(imagen, 90, 100, 150)
