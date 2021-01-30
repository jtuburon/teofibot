import cv2 as cv;

def addSmiles(input_photo):
        smile_mat = cv.imread("resources/smileys/smile.png", cv.IMREAD_UNCHANGED)

        image_mat  = cv.imread(input_photo, cv.IMREAD_UNCHANGED)
        gray = cv.cvtColor(image_mat, cv.COLOR_BGR2GRAY)

        haar = cv.CascadeClassifier('resources/haar/haarcascade_frontalface_default.xml')
        
        
        faces = haar.detectMultiScale(gray, 1.3, 5)
        
        if len(faces):
                for (x,y,w,h) in faces:
                        sub = image_mat[y:y+h,x:x+w]
                        resized= cv.resize(smile_mat, (w,h) )
                        for i in range(h):
                            for j in range(w):
                                color1 = sub[i, j]
                                color2 = resized[i, j]
                                alpha = color2[3] / 255.0
                                new_color = [ (1 - alpha) * color1[0] + alpha * color2[0],
                                        (1 - alpha) * color1[1] + alpha * color2[1],
                                        (1 - alpha) * color1[2] + alpha * color2[2] ]
                                sub[i,j]= new_color
                outFile = "c_"+ input_photo+".jpg"
                cv.imwrite(outFile, image_mat)
                return True, outFile
        else:
                return False, ""