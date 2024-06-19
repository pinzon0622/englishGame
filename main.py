import csv
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import time


#Clase 
class MCQ():
    def __init__(self, data):
        self.question = data[0]
        self.choice1 = data[1]
        self.choice2 = data[2]
        self.choice3 = data[3]
        self.choice4 = data[4]
        self.anwer = int(data[5])

        self.userAns = None

    def update(self,cursor,bboxs):
        for x, bbox in enumerate(bboxs):
            x1,y1,x2,y2 = bbox
            if x1<cursor[0]<x2 and y1<cursor[1]<y2:
                self.userAns = x+1
                cv2.rectangle(img, (x1,y1), (x2,y2), (255, 255, 255), cv2.FILLED) #Cambiar el color del rectangulo si esta seleccionado


#Inicializa la camara
cap = cv2.VideoCapture(0)
cap.set(3, 1288)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

#Importa las preguntas desde el archivo csv
pathCSV = "questionsData.csv"
with open(pathCSV, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[1:]


#Crea una lista de objetos de preguntas
mcqList = []
for q in dataAll:
    obj = MCQ(q)
    mcqList.append(obj)

print("Total de objetos MCQ creados:", len(mcqList))

#Inicializa las variables de las preguntas
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
        img, bbox =  cvzone.putTextRect(img, mcq.question, (250, 100),  
            scale=3, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 1, 1), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255) 
        )
        
        #Dibuja las opciones
        img, bbox1 = cvzone.putTextRect(img, mcq.choice1, [50, 250],
            scale=2, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 103, 103), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255)
        )
        img, bbox2 = cvzone.putTextRect(img, mcq.choice2, [50, 370],
            scale=2, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 103, 103), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255)
        )
        img, bbox3 = cvzone.putTextRect(img, mcq.choice3, [50, 490],
        scale=2, thickness=2, 
            colorT=(255, 255, 255), colorR=(255, 103, 103), 
            font=cv2.FONT_HERSHEY_PLAIN, 
            offset=20,  
            border=2, colorB=(255, 255, 255)
        )
        img, bbox4 = cvzone.putTextRect(img, mcq.choice4, [50, 610],
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
                mcq.update(cursor, [bbox1, bbox2, bbox3, bbox4])
                print(mcq.userAns)
                if mcq.userAns is not None:
                    time.sleep(0.3)
                    qNo += 1
    else:
        score = 0
        for mcq in mcqList:
            if mcq.userAns == mcq.anwer:
                score += 1
        score = round((score/qTotal)*100,2)
        img, _ = cvzone.putTextRect(img, "Quiz Completed", [250, 300], 2, 2, offset=50, border=5) #Mensaje de finalizacion
        img, _ = cvzone.putTextRect(img, f'Your Score is: {score}%', [700, 300], 2, 2, offset=50, border=5) #Mensaje de puntuacion
    #Dibuja la barra de progreso
    barValue = 150 + (1000 // qTotal) * qNo
    cv2.rectangle(img, (150, 650), (barValue, 700), (0, 255, 0), cv2.FILLED)
    cv2.rectangle(img, (150, 650), (1150, 700), (255, 0, 255), 5)
    img, _ = cvzone.putTextRect(img, f'{round((qNo/qTotal)*100)}%', [1180, 685], 2, 2, offset=16)


    cv2.imshow("Img", img)
    cv2.waitKey(1)
