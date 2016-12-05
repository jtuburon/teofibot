import cv2 as cv;

def addSmiles(input_photo):
        smile = cv.imread("data/smile.png")
        smile_mat = cv.cv.fromarray(smile)

        image = cv.imread(input_photo)
        haar = cv.cv.Load('data/haarcascade_frontalface_default.xml')
        image_mat = cv.cv.fromarray(image)

        storage = cv.cv.CreateMemStorage()

        faces= cv.cv.HaarDetectObjects(image_mat, haar, storage, 1.2, 2, cv.cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
        
        if len(faces):
                for (x,y,w,h),n in faces:
                        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)

                        sub = cv.cv.GetSubRect(image_mat, (x,y,w,h))
                        # Creamos una matriz con el tamano del rectangulo detectado para hacer un resize del SMILE dentro de esta matriz                       
                        thumbnail = cv.cv.CreateMat(h, w, cv.CV_8UC3)
                        # Hacemos el resize

                        cv.cv.Resize(smile_mat, thumbnail)
                        # Copiamos la imagen del SMILE redimensiona     do a la region detectada
                        for i in range(h):
                                for j in range(w):
                                        sub[i,j]= thumbnail[i,j]
                outFile = "c_"+ input_photo+".jpg"
                cv.imwrite(outFile, image)
                return True, outFile
        else:
                return False, ""