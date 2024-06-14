import csv
import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone


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

print(len(mcqList))

#Inicializa las variables de las preguntas
qNo = 0
qTotal = len(dataAll)

#Inicializa el detector de manos
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    mcq = mcqList[1]

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
        if length < 60:
            mcq.update(cursor, [bbox1, bbox2, bbox3, bbox4])


    cv2.imshow("Img", img)
    cv2.waitKey(1)
