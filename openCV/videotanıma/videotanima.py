import cv2


cap = cv2.VideoCapture(0) #burada kendi kameranı şçiyorsun

#tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.legacy.TrackerCSRT_create()
succsess, img = cap.read()

bbox = cv2.selectROI("Bulundu",img,False)

tracker.init(img,bbox)

def drawBox(img,bbox):
    x = int(bbox[0])
    y = int(bbox[1])
    w = int(bbox[2])
    h = int(bbox[3])
    cv2.rectangle(img,(x,y),((x + w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"bulundu",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)




while True: # bu loopsda kendi videonu kare halşnde işliyorsun

    timer = cv2.getTickCount()
    succsess,img = cap.read()

    succsess,bbox = tracker.update(img)
    print(bbox)
    
    if succsess:
        drawBox(img,bbox)
    else:
            cv2.putText(img,"kayip oldu",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)


    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("trackinng",img) # burada gösterme işlemi zaten

    if cv2.waitKey(1) & 0xff == ord('q'): # çıkmak için q basmanız lazım 
        break
