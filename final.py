import cv2

face_cascade = cv2.CascadeClassifier('Cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)                 #0 means default so make 1 when connecting to Pi

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        #roi_gray = gray[y:y+h, x:x+w] #[cord1-height, cord2-height] so starting y-coordi and ending y-coord
        roi_color = frame[y:y+h,x:x+w]
        img_item = 'image.png' 
        cv2.imwrite(img_item,roi_color)
        color = (0,0,500) #BGR 0-255
        stroke = 5
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y),(end_cord_x,end_cord_y),color,stroke)
    cv2.imshow('frame',frame)              #webcam displays person in frame
    if cv2.waitKey(1) & 0xFF == ord('q'):         #hitting q ends frame
        break

cap.release()
cv2.destroyAllWindows()

'''
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)
def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)
def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)
def make_120p():
    cap.set(3, 240)
    cap.set(4, 120)
def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
'''