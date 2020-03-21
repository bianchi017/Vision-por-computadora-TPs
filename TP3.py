import cv2

cap = cv2.VideoCapture('zilean.mp4')
#Conseguir FPS del video original
fps = int(cap.get(cv2.CAP_PROP_FPS))
#Calcular el retraso entre cada fotograma
delay = int(1000 / fps)
print('FPS del video original:',fps)
print('Delay:',delay)
print('Presione Q para salir del video')
while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', gray)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
