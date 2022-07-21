import cv2
import os
def func_face_checker(image_path):
    print(image_path)
    cascade_folder = "./polls/learned_file/haarcascade_frontalface_default.xml"
    os.path.isdir("./polls/")
    print(os.path.isfile(cascade_folder))

    face_cascade_path =  cascade_folder

    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    src = cv2.imread('./'+image_path)
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("./media/img/gray.png",src_gray)
    faces = face_cascade.detectMultiScale(src_gray)
    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = src[y: y + h, x: x + w]
        face_gray = src_gray[y: y + h, x: x + w]
    
    savename = 'face_checker.png'
    imgpath = "."+image_path
    dirname = os.path.dirname(imgpath)
    savename = dirname+"/"+savename

    print(savename)
    cv2.imwrite(savename, src)

    num = len(faces)
    print(num,faces)
    return num
