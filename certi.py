import PIL
import csv
import os
import cv2 as cv
import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.base import MIMEBase

from email import encoders
import pyrebase
config={
    "apiKey": "AIzaSyC6IPdVSz3s4umFwNAtgJnliIG6IV3FGW8",
    "authDomain": "cert-43ffe.firebaseapp.com",
    "databaseURL": "https://cert-43ffe.firebaseio.com",
    "projectId": "cert-43ffe",
    "storageBucket": "cert-43ffe.appspot.com",
    "messagingSenderId": "261377733062",
    "appId": "1:261377733062:web:669d4041a96a41d69742c7",
    "measurementId": "G-24C3942VV3"
}
firebase=pyrebase.initialize_app(config)
storage=firebase.storage()

def calc_start(center,arr,size_of_font):
    length = len(arr)
    center[0] = int(center[0] - size_of_font * (length/2))
    return center


base_destination = 'teams/'
included_ext = ['csv']
arr=[fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_ext)]
no_of_files = len(arr)

for i in range(no_of_files):
    
    try:
        group = arr[i]
        print(arr[i])


        name=[]
        position=[]
        event=[]
        college = []
        email_id=[]
        with open(group) as file:
            data=csv.reader(file, delimiter=',')
            count=0
            for row in data:
                count+=1
                if(count==1):
                    continue
                name.append(row[0])
                college.append(row[1])
                position.append(row[2])
                event.append(row[3])
                email_id.append(row[4])

                   
        print(name[0])
        print(college[0])
        print(position[0])
        print(event[0])



        for i in range(0, len(name)):
            try:

                destination = base_destination + college[i] + '/' + event[i] + '/'
                if not os.path.exists(destination):
                    os.makedirs(destination)


                if(position[i]=="First"):
                    img = cv.imread("gold.jpg")
                elif(position[i]=="Second"):
                    img = cv.imread("silver.jpg")
                else:
                    img = cv.imread("bronze.jpg")



                center_1 = [1800,1375]
                center_2 = [1800,1540]
                center_3 = [1430,1715]
                center_4 = [2535,1715]

                font = cv.FONT_HERSHEY_TRIPLEX

                size_of_font = 40 



                start_1 = calc_start(center_1,name[i],size_of_font)
                start_2 = calc_start(center_2,college[i],size_of_font)
                start_3 = calc_start(center_3,position[i],size_of_font)
                start_4 = calc_start(center_4,event[i],size_of_font)

                cv.putText(img,name[i],tuple(start_1), font, 2,(0,0,0),2,cv.LINE_AA)
                cv.putText(img,college[i],tuple(start_2), font, 2,(0,0,0),2,cv.LINE_AA)
                cv.putText(img,position[i],tuple(start_3), font, 2,(0,0,0),2,cv.LINE_AA)
                cv.putText(img,event[i],tuple(start_4), font, 2,(0,0,0),2,cv.LINE_AA)
                cv.putText(img,event[i], (1500, 500), font, 2, (0, 0, 0), 2)
                cv.imwrite(destination+name[i]+'_'+event[i]+'.jpg',img)
                path_on_cloud="certificates"+name[i]+".jpg"
                path_local=destination+name[i]+'_'+event[i]+'.jpg'
                storage.child(path_on_cloud).put(path_local)
                path_cloud=name[i]+'.jpg'
                storage.child(path_cloud).put(path_local)
                from_addr = 'patelrupin63@gmail.com'
                to_addr =email_id
                msg = MIMEMultipart()
                msg['From'] = from_addr
                msg['To'] =to_addr[i]
                msg['subject'] = 'just to check Hii This is Rupin '

                filename = path_local
                attachment = open(filename, 'rb')

                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + filename)

                msg.attach(part)

                email = 'patel.rupin56@gmail.com'
                password = 'patelrocks69'
                recipients = 'patel.rupin56@gmail.com'

                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login(email, password)
                text = msg.as_string()
                mail.sendmail(from_addr,to_addr[i],text)
                mail.quit()

                print("{}/{}".format(i+1,len(name)))
            except:
                print("Something went wrong")

    except:
        print("file is not proper format: {}".format(arr[i]))
        