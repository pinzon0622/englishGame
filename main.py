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
    hand, img = detector.findHands(img, flipType=False)

    mcq = mcqList[0]

    #Dibuja la pregunta
    img, cvzone.putTextRect(img, mcq.question, [100, 100], 2, 2, offset=20, border=2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
