import cv2 
import mediapipe as mp


webcam = cv2.VideoCapture(0)
reconhecimento = mp.solutions.face_detection
capturar_rostos = reconhecimento.FaceDetection()
desenhar = mp.solutions.drawing_utils

if webcam.isOpened() :
    validacao, frame = webcam.read()
    
    while True:
        validacao, frame = webcam.read()
       
        if not validacao:
            break
        lista_rostos = capturar_rostos.process(frame)
        if lista_rostos.detections:
            for rosto in lista_rostos.detections:
                desenhar.draw_detection(frame, rosto)
        
        cv2.imshow('reconhecimento facial', frame)
        key = cv2.waitKey(2)
        
        if key == 27:
            break

webcam.release()
        
