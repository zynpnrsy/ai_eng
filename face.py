#this code is for face recognition and using opencv & haarscade.


import cv2 #opencv

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# this is use-ready library, we dont have to use any datasets etc.

cam = cv2.VideoCapture(0) # 0 for cp cam, 1 for usb cam

while True: 
    
    ret, frame = cam.read()
    if not ret :
        print("frame error, frame can not open") 
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # haarcascade works with gray 
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50,50))
    
    for (x,y,h,w) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255) , 2) # 0,0,255 is red
        
        cv2.imshow("zeynep's face detection trial 1" , frame) # visible as a title in the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit 
        break
    
    
cam.release()
cv2.destroyAllWindows()
    
    



