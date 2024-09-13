import csv
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time
import numpy as np
import tkinter as tk
from tkinter import filedialog


# Clase para gestionar las preguntas y respuestas
class MCQ():
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.answer = int(data[5])
        self.userAns = None

    def update(self, cursor, bboxs):
        for x, bbox in enumerate(bboxs):
            x1, y1, x2, y2 = bbox
            if x1 < cursor[0] < x2 and y1 < cursor[1] < y2:
                self.userAns = x + 1
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), cv2.FILLED)

# Función para mostrar el menú de bienvenida
def show_welcome_menu():
    while True:
        img = cv2.imread('fondo-english.png')  # Puedes usar una imagen de fondo si lo prefieres
        if img is None:
            img = 255 * np.ones(shape=[720, 1280, 3], dtype=np.uint8)  # Imagen en blanco si no hay fondo
        else:
            # Redimensionar la imagen de fondo para que se ajuste a la resolución de la pantalla (1280x720)
            img = cv2.resize(img, (1280, 720))

        # Añadir texto de bienvenida
        img, _ = cvzone.putTextRect(img, "Welcome to camera english game!", [220, 170],
                                    scale=3, thickness=2, 
                                    colorT=(255, 255, 255), colorR=(255, 1, 1), 
                                    font=cv2.FONT_HERSHEY_PLAIN, 
                                    offset=20,  
                                    border=2, colorB=(255, 255, 255))
        img, _ = cvzone.putTextRect(img, "Press any key for select a csv file", [330, 580],
                                    scale=2, thickness=2, 
                                    colorT=(255, 255, 255), colorR=(255, 1, 1), 
                                    font=cv2.FONT_HERSHEY_PLAIN, 
                                    offset=20,  
                                    border=2, colorB=(255, 255, 255))

        cv2.imshow("Welcome Menu", img)
        key = cv2.waitKey(0)
        
        if key:  # Si se presiona cualquier tecla, continuar
            cv2.destroyWindow("Welcome Menu")
            break


# Lista con los nombres reales de los archivos
files = ["animalsData.csv", "colorsData.csv", "numbersData.csv", "questionsData.csv"]

# Lista con los nombres personalizados que se mostrarán
display_names = ["Animals Quiz", "Colors Quiz", "Numbers Quiz", "Texts Quiz"]

# Función para mostrar el menú de selección de archivo
def show_file_selection_menu():
    files = ['animalsData.csv', 'colorsData.csv', 'numbersData.csv', 'questionsData.csv']
    selected_file = None

    while True:
        img = cv2.imread('fondo-english-file.png')  # Puedes usar una imagen de fondo si lo prefieres
        if img is None:
            img = 255 * np.ones(shape=[720, 1280, 3], dtype=np.uint8)  # Imagen en blanco si no hay fondo
        else:
            # Redimensionar la imagen de fondo para que se ajuste a la resolución de la pantalla (1280x720)
            img = cv2.resize(img, (1280, 720))
            img, _ = cvzone.putTextRect(img, "Select a option of game", [350, 100], scale=3, thickness=2, 
                                    colorT=(255, 255, 255), colorR=(255, 1, 1), 
                                    font=cv2.FONT_HERSHEY_PLAIN, offset=20, border=2, colorB=(255, 255, 255))
        
        # Mostrar archivos disponibles
        for i, display_name in enumerate(display_names):
            img, _ = cvzone.putTextRect(img, f"{i+1}. {display_name}", [95 + (i * 300), 220], scale=1.5, thickness=2, 
                                colorT=(255, 255, 255), colorR=(255, 103, 103), 
                                font=cv2.FONT_HERSHEY_PLAIN, offset=20, border=2, colorB=(255, 255, 255))
        
        # Mostrar imagen en pantalla
        cv2.imshow("File Selection", img)

        key = cv2.waitKey(0)

        if key >= ord('1') and key < ord('1') + len(files):
            selected_file = files[key - ord('1')]
            break
        elif key == ord('q'):  # Si se presiona 'q', salir
            break
    
    cv2.destroyWindow("File Selection")
    return selected_file


# Función para mostrar el mensaje final
def show_final_message(score):
    while True:


        # Selecciona la imagen de fondo según el puntaje
        if score <= 25:
            img = cv2.imread('score-25.png') 
            mensaje = "Keep trying, you can do it!"
            colorT = (255, 255, 255) 
            colorR = (0, 0, 255)  
        elif score <= 50:
            img = cv2.imread('score-50.png') 
            mensaje = "Good effort, keep it up!"
            colorT = (255, 255, 255)  
            colorR = (255, 255, 0)
        elif score <= 75:
            img = cv2.imread('score-75.png')  
            mensaje = "Great job, you're almost there!"
            colorT = (255, 255, 255) 
            colorR = (0, 255, 255) 
        else:
            img = cv2.imread('score-100.png')
            mensaje = "Amazing, keep shining!"
            colorT = (255, 255, 255)
            colorR = (255, 1, 1) 

        if img is None:
            img = 255 * np.ones(shape=[720, 1280, 3], dtype=np.uint8) 
        else:
            img = cv2.resize(img, (1280, 720)) 

        
        img, _ = cvzone.putTextRect(img, "Quiz Completed", [100, 150],
                                    scale=3, thickness=2, 
                                    colorT=(255, 255, 255), colorR=(255, 1, 1), 
                                    font=cv2.FONT_HERSHEY_PLAIN, 
                                    offset=20,  
                                    border=2, colorB=(255, 255, 255))
        img, _ = cvzone.putTextRect(img, f'Your Score is: {score}%', [350, 580],
                                    scale=3, thickness=2, 
                                    colorT=(255, 255, 255), colorR=(255, 1, 1), 
                                    font=cv2.FONT_HERSHEY_PLAIN, 
                                    offset=20,  
                                    border=2, colorB=(255, 255, 255)) 
        img, _ = cvzone.putTextRect(img, "Press 'q' to exit", [100, 250],
                                    scale=2, thickness=2, 
                                    colorT=(255, 255, 255), colorR=(255, 1, 1), 
                                    font=cv2.FONT_HERSHEY_PLAIN, 
                                    offset=20,  
                                    border=2, colorB=(255, 255, 255))
        img, _ = cvzone.putTextRect(img, mensaje, [250, 450],
                                    scale=2, thickness=2, 
                                    colorT=colorT, colorR=colorR, 
                                    font=cv2.FONT_HERSHEY_PLAIN, 
                                    offset=20,  
                                    border=2, colorB=(255, 255, 255))
        
        cv2.imshow("Final Message", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyWindow("Final Message")
            break


# Llamar al menú de bienvenida
show_welcome_menu()

# Llamar al menú de selección de archivos
archivo_csv = show_file_selection_menu()
if not archivo_csv:
    print("No se seleccionó ningún archivo. Saliendo...")
    exit()

print(f"Archivo CSV seleccionado: {archivo_csv}")

# Inicializa la cámara
cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

# Importa las preguntas desde el archivo CSV seleccionado
with open(archivo_csv, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]

# Crea una lista de objetos de preguntas
mcqList = []
for q in dataAll:
    obj = MCQ(q)
    mcqList.append(obj)

# Inicializa las variables de las preguntas
qNo = 0
qTotal = len(dataAll)
#Inicializa el detector de manos
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if qNo < qTotal:
        mcq = mcqList[qNo]
        

        #Dibuja la pregunta
        img, bbox =  cvzone.putTextRect(img, mcq.question, (150, 100),  
            scale=3, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 1, 1), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255) 
        )
        
        #Dibuja las opciones
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [50, 280],
            scale=2, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 103, 103), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255)
        )
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [50, 440],
            scale=2, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 103, 103), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255)
        )
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [400, 280],
        scale=2, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 103, 103), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255)
        )
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [400, 440],
            scale=2, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 103, 103), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255)
        )

        #Detecta si la mano esta en la pantalla
        if hands:
            lmList = hands[0]['lmList']
            cursor = lmList[8]

            length, info, img = detector.findDistance(lmList[8][0:2], lmList[12][0:2], img, color=(255, 1, 1),scale=10) #color: es el color que detecta la punta de los dedos

            #Detecta si el cursor esta en una opcion
            if length < 40:
                time.sleep(0.3)
                mcq.update(cursor, [bbox1, bbox2, bbox3, bbox4])
                #print(mcq.userAns)
                
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    qNo += 1
    else:
        score = 0
        for mcq in mcqList:
            if mcq.userAns == mcq.answer:
                score += 1
        score = round((score/qTotal)*100,2)

        cap.release()
        cv2.destroyAllWindows()

        # Llamar a la función de mensaje final
        show_final_message(score)
        break
        
    #Dibuja la barra de progreso
    barValue = 80 + (1000 // qTotal) * qNo
    cv2.rectangle(img, (80, 580), (barValue, 640), (0, 255, 0), cv2.FILLED)
    cv2.rectangle(img, (80, 580), (1080, 640), (255, 255, 255), 5)
    img, _ = cvzone.putTextRect(img, f'{round((qNo/qTotal)*100)}%', [1110, 625], 
                                colorT=(255, 255, 255), colorR=(255, 1, 1), 
                                offset=20,  
                                border=2, colorB=(255, 255, 255))


    # Muestra la ventana de juego
    cv2.imshow("Camera English Game", img)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()



