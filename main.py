import tkinter as tk
from tkinter import ttk
import sys
from memory_profiler import profile
from tkinter.filedialog import askopenfilename
LARGEFONT = ("Verdana", 35)
from email import encoders
import pyrebase
import PIL
import csv
import numpy as np
import os
import cv2 as cv
import smtplib
from email.mime.multipart import MIMEMultipart
from PIL import ImageTk, Image
from email.mime.base import MIMEBase
import tkinter
from tkinter import *
from PIL import Image, ImageTk,ImageDraw, ImageFilter
from tkinter.ttk import *
class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        root = Tk()
        main_frame=Frame(self)
        main_frame.pack(fill=BOTH,expand=1)
        my_canavas=Canvas(main_frame)
        my_canavas.pack(side=LEFT,fill=BOTH,expand=1)
        my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canavas.yview)
        my_scrollbar.pack(side=RIGHT,fill=Y)
        my_canavas.configure(yscrollcommand=my_scrollbar.set)
        my_canavas.bind('<Configure>',lambda e:my_canavas.configure(scrollregion=my_canavas.bbox("all")))

        def _on_mousewheel(event):
            my_canavas.yview_scroll(-1 * (event.delta / 120), "units")
        #my_canavas.bind_all('<MouseWheel>',_on_mousewheel)
        second_frame=Frame(my_canavas)
        my_canavas.create_window((0,0),window=second_frame,anchor="nw")















        # Create a photoimage object of the image in the path
        image1 = Image.open("gold1.png")
        image1 = image1.resize((600, 300), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(second_frame,image=test)
        label1.image = test

        # Position image
        label1.grid(row=0, column=1,padx=10,pady=10)

        # label of frame Layout 2
        #label = ttk.Label(self, text="Startpage", font=LARGEFONT)

        # putting the grid in its place by using
        # grid
        #label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(second_frame, text="Template-1",command=lambda: controller.show_frame(Page1))

        # putting the button in its place by
        # using grid
        button1.grid(row=1, column=1, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(second_frame, text="Template-2",command=lambda: controller.show_frame(Page2))
        button3=ttk.Button(second_frame,text="Import .CSV",command=lambda:os.system('dynamic.exe'))
        #button3.config(height = 200, width = 200)
        button4 = ttk.Button(second_frame, text="Image Coordinates Identifier", command=lambda: os.system('coordinate.exe'))
        image2 = Image.open("Sample1.png")
        image2 = image2.resize((600, 300), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(image2)

        label2 = tkinter.Label(second_frame,image=test)
        label2.image = test

        # Position image
        label2.grid(row=2, column=1,padx=10,pady=10)

        # putting the button in its place by
        # using grid
        button2.grid(row=3, column=1, padx=10, pady=10)
        button3.grid(row=1, column=50, padx=100, pady=10)
        button4.grid(row=2,column=50,padx=100,pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        import tkinter as ttk
        tk.Frame.__init__(self, parent)

        button7= ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button7.grid(row=7, column=1, padx=10, pady=10)
        root=Tk()

        # Program to make a simple
        # login screen


        config = {
          <firebase configuration>
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()





        # setting the windows size


        # here, image option is used to
        # set image on button

        # declaring string variable
        # for storing name and password
        name_var = ttk.StringVar()
        passw_var = ttk.StringVar()
        college_var = ttk.StringVar()
        event_var = ttk.StringVar()
        position_var = ttk.StringVar()
        email_var = ttk.StringVar()

        from tkinter.filedialog import askopenfilename
        # import pandas as pd

        def calc_start(center, arr, size_of_font):
            length = len(arr)
            center[0] = int(center[0] - size_of_font * (length / 2))
            return center

        def import_csv_data():
            global arr
            arr = ttk.StringVar()
            csv_file_path = askopenfilename()
            print(csv_file_path)
            print("???????????????????????????????????????????????????????????????????")
            arr.set(csv_file_path)
            base_destination = 'teams/'
            included_ext = ['csv']
            # arr = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_ext)]
            # no_of_files = len(arr)

            for i in range(0, 1):

                try:
                    group = csv_file_path
                    print(group)
                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

                    name = []
                    position = []
                    event = []
                    college = []
                    email_id = []
                    with open(group) as file:
                        data = csv.reader(file, delimiter=',')
                        count = 0
                        for row in data:
                            count += 1
                            if (count == 1):
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

                            if (position[i] == "First"):
                                img = cv.imread("gold.jpg")
                            elif (position[i] == "Second"):
                                img = cv.imread("silver.jpg")
                            else:
                                img = cv.imread("bronze.jpg")

                            center_1 = [1800, 1375]
                            center_2 = [1800, 1540]
                            center_3 = [1430, 1715]
                            center_4 = [2535, 1715]

                            font = cv.FONT_HERSHEY_TRIPLEX

                            size_of_font = 40

                            start_1 = calc_start(center_1, name[i], size_of_font)
                            start_2 = calc_start(center_2, college[i], size_of_font)
                            start_3 = calc_start(center_3, position[i], size_of_font)
                            start_4 = calc_start(center_4, event[i], size_of_font)

                            cv.putText(img, name[i], tuple(start_1), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, college[i], tuple(start_2), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, position[i], tuple(start_3), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, event[i], tuple(start_4), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, event[i], (1500, 500), font, 2, (0, 0, 0), 2)
                            cv.imwrite(destination + name[i] + '_' + event[i] + '.jpg', img)
                            path=name[i] + position[i] + event[i] +'/' + '.jpg'
                            uniq_id=str(hash(path))

                            path_on_cloud = "certificates/" + name[i] + ".jpg"
                            path_local = destination + name[i] + '_' + event[i] + '.jpg'
                            storage.child(path_on_cloud).put(path_local)
                            path_cloud = uniq_id + '/' + '.jpg'
                            storage.child(path_cloud).put(path_local)
                            from_addr = 'patel.rupin56@gmail.com'
                            to_addr = email_id
                            msg = MIMEMultipart()
                            msg['From'] = from_addr
                            msg['To'] = to_addr[i]
                            msg['subject'] = 'Your Certificate id is  '+uniq_id

                            filename = path_local
                            attachment = open(filename, 'rb')

                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload((attachment).read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', "attachment; filename= " + filename)

                            msg.attach(part)

                            email = 'patel.rupin56@gmail.com'
                            password = '+++++++++++++++'
                            recipients = 'patel.rupin56@gmail.com'

                            mail = smtplib.SMTP('smtp.gmail.com', 587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(email, password)
                            text = msg.as_string()
                            mail.sendmail(from_addr, to_addr[i], text)
                            mail.quit()
                            with open('Result Template-1 .txt', 'a') as the_file:
                                the_file.write(name[i] + " " + " sucessfull" + "  " + uniq_id + '\n')

                            print("{}/{}".format(i + 1, len(name)))
                        except:
                            print("Something went wrong")

                except:
                    print("file is not proper format: {}".format(arr))
            # df = pd.read_csv(csv_file_path)

        # defining a function that will
        # get the name and password and
        # print them on the screen
        def submit():
            name = name_var.get()
            college = college_var.get()
            position = position_var.get()
            event = event_var.get()
            email_id = email_var.get()

            def calc_start(center, a, size_of_font):
                length = len(a)
                center[0] = int(center[0] - size_of_font * (length / 2))
                return center

            print("The name is : " + name)
            print("The college is : " + college)
            print("The position is : " + position)
            print("The event is : " + event)
            print("The email id is : " + email_id)
            base_destination = 'teams/'
            included_ext = ['csv']
            # arr = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_ext)]
            # no_of_files = len(arr)

            for i in range(0, 1):

                try:

                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

                    for i in range(0, 1):
                        try:

                            destination = base_destination + college + '/' + event + '/'
                            if not os.path.exists(destination):
                                os.makedirs(destination)

                            if (position == "First"):
                                img = cv.imread("gold.jpg")
                            elif (position == "Second"):
                                img = cv.imread("silver.jpg")
                            else:
                                img = cv.imread("bronze.jpg")

                            center_1 = [1800, 1375]
                            center_2 = [1800, 1540]
                            center_3 = [1430, 1715]
                            center_4 = [2535, 1715]

                            font = cv.FONT_HERSHEY_TRIPLEX

                            size_of_font = 40

                            start_1 = calc_start(center_1, name, size_of_font)
                            start_2 = calc_start(center_2, college, size_of_font)
                            start_3 = calc_start(center_3, position, size_of_font)
                            start_4 = calc_start(center_4, event, size_of_font)

                            cv.putText(img, name, tuple(start_1), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, college, tuple(start_2), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, position, tuple(start_3), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, event, tuple(start_4), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, event, (1500, 500), font, 2, (0, 0, 0), 2)
                            cv.imwrite(destination + name + '_' + event + '.jpg', img)
                            path=name + position+ event + '/' + '.jpg'
                            uniq_id=str(hash(path))
                            path_on_cloud = "certificates/" + name + ".jpg"
                            path_local = destination + name + '_' + event + '.jpg'
                            storage.child(path_on_cloud).put(path_local)
                            path_cloud = uniq_id + '/' + '.jpg'
                            storage.child(path_cloud).put(path_local)
                            from_addr = 'patel.rupin56@gmail.com'
                            to_addr = email_id
                            msg = MIMEMultipart()
                            msg['From'] = from_addr
                            msg['To'] = to_addr
                            msg['subject'] = 'Your Certificate id is  '+uniq_id

                            filename = path_local
                            attachment = open(filename, 'rb')

                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload((attachment).read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', "attachment; filename= " + filename)

                            msg.attach(part)

                            email = 'patel.rupin56@gmail.com'
                            password = '+++++++++++++++'
                            recipients = 'patel.rupin56@gmail.com'

                            mail = smtplib.SMTP('smtp.gmail.com', 587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(email, password)
                            text = msg.as_string()
                            mail.sendmail(from_addr, to_addr, text)
                            mail.quit()
                            with open('Result Template-1 .txt', 'a') as the_file:
                                the_file.write(name + " " + " sucessfull" + "  " + uniq_id + '\n')

                            print(name)

                        except:
                            print("Something went wrong")

                except:
                    print("Error")
                

            name_var.set("")
            passw_var.set("")
            college_var.set("")
            event_var.set("")
            position_var.set("")
            email_var.set("")

        # creating a label for
        # name using widget Label
        name_label = ttk.Label(self, text='Username', font=('calibre', 10, 'bold'))

        # creating a entry for input
        # name using widget Entry
        name_entry = ttk.Entry(self, textvariable=name_var, font=('calibre', 10, 'normal'))

        # creating a label for password

        # creating a entry for password

        college_label = ttk.Label(self, text='College', font=('calibre', 10, 'bold'))
        college_entry = ttk.Entry(self, textvariable=college_var, font=('calibre', 10, 'normal'))
        position_label = ttk.Label(self, text='Position', font=('calibre', 10, 'bold'))
        position_entry = ttk.Entry(self, textvariable=position_var, font=('calibre', 10, 'normal'))
        event_label = ttk.Label(self, text='Event', font=('calibre', 10, 'bold'))
        event_entry = ttk.Entry(self, textvariable=event_var, font=('calibre', 10, 'normal'))
        email_label = ttk.Label(self, text='Email Id', font=('calibre', 10, 'bold'))
        email_entry = ttk.Entry(self, textvariable=email_var, font=('calibre', 10, 'normal'))

        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = ttk.Button(self, text='Submit', command=submit)
        bro = ttk.Button(self, text='Import .csv', command=import_csv_data)

        # placing the label and entry in
        # the required position using grid
        # method
        name_label.grid(row=0, column=0)
        name_entry.grid(row=0, column=1)
        college_label.grid(row=1, column=0)
        college_entry.grid(row=1, column=1)
        position_label.grid(row=2, column=0)
        position_entry.grid(row=2, column=1)
        event_label.grid(row=3, column=0)
        event_entry.grid(row=3, column=1)
        email_label.grid(row=4, column=0)
        email_entry.grid(row=4, column=1)

        sub_btn.grid(row=5, column=1)
        bro.grid(row=5, column=2)

        arr = ttk.StringVar()

        # performing an infinite loop
        # for the window to display



# third window frame page2
class Page2(tk.Frame):

    def __init__(self, parent, controller):

        import tkinter as ttk
        tk.Frame.__init__(self, parent)
        self.filename = ""


        # button to show frame 2 with text
        # layout2
        config = {
         <firebase configuration>
        }
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()

        # putting the button in its place by
        # using grid
        from tkinter import filedialog

        def openfile():




            self.filename = filedialog.askopenfilename(title="Select Signature")
            ttk.Label(self,text='Signature Path',font=('calibre',10,'bold')).grid(row=9,column=0)
            ttk.Label(self,text=self.filename, font=('calibre', 10, 'bold')).grid(row=9,column=1)
            print(self.filename)






        name_var = ttk.StringVar()
        duration_var = ttk.StringVar()
        company_var = ttk.StringVar()
        date_var=ttk.StringVar()
        email_var=StringVar()







        def submit():

            name = name_var.get()
            duration = duration_var.get()
            company = company_var.get()
            date=date_var.get()
            email_id = email_var.get()


            def calc_start(center, a, size_of_font):
                length = len(a)
                center[0] = int(center[0] - size_of_font * (length / 2))
                return center

            print("The name is : " + name)
            print("The duration is : " + duration)
            print("The company is : " + company)
            print("The date is : "+ date)
            print(self.filename)

            base_destination = 'company/'
            #included_ext = ['csv']
            # arr = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_ext)]
            # no_of_files = len(arr)
            im0=self.filename



            for i in range(0, 1):

                try:

                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

                    for i in range(0, 1):
                        try:

                            destination = base_destination + company + '/' + duration + '/'
                            if not os.path.exists(destination):
                                os.makedirs(destination)
                            im1 = Image.open('Sample.jpg')

                            im3 = Image.open(im0)
                            back_im = im1.copy()
                            back_im.paste(im3, (500, 1800),mask=im3)
                            back_im.save('company/_.jpg', quality=100)



                            img = cv.imread("company/_.jpg")




                            center_1 = [1800, 1045]
                            center_2 = [1780, 1225]
                            center_3 = [2010, 1495]
                            center_4=  [2650, 2080]


                            font = cv.FONT_HERSHEY_TRIPLEX

                            size_of_font = 40

                            start_1 = calc_start(center_1, name, size_of_font)
                            start_2 = calc_start(center_2, duration, size_of_font)
                            start_3 = calc_start(center_3, company, size_of_font)
                            start_4 = calc_start(center_4,date,size_of_font)




                            cv.putText(img, name, tuple(start_1), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, duration, tuple(start_2), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, company, tuple(start_3), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img,date,tuple(start_4),font, 2, (0, 0, 0), 2, cv.LINE_AA)






                            cv.imwrite(destination + name + '_' + company +"_"+duration+ '.jpg', img)
                            path=name +company+duration+ '/' + '.jpg'
                            uniq_id=str(hash(path))
                            path_on_cloud = "certificates/" + name +" " +company+" "+duration+ ".jpg"
                            path_local = destination + name + '_' + company +"_"+duration +'.jpg'
                            storage.child(path_on_cloud).put(path_local)
                            path_cloud = uniq_id+ '/' + '.jpg'
                            storage.child(path_cloud).put(path_local)
                            from_addr = 'patel.rupin56@gmail.com'
                            to_addr = email_id
                            msg = MIMEMultipart()
                            msg['From'] = from_addr
                            msg['To'] = to_addr
                            msg['subject'] = 'Your Certificate id is  ' + uniq_id

                            filename = path_local
                            attachment = open(filename, 'rb')

                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload((attachment).read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', "attachment; filename= " + filename)

                            msg.attach(part)

                            email = 'patel.rupin56@gmail.com'
                            password = '+++++++++++++++'
                            recipients = 'patel.rupin56@gmail.com'

                            mail = smtplib.SMTP('smtp.gmail.com', 587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(email, password)
                            text = msg.as_string()
                            mail.sendmail(from_addr, to_addr, text)
                            mail.quit()
                            with open('Result Template-2 .txt', 'a') as the_file:
                                the_file.write(name + " " + " sucessfull" + "  " + uniq_id + '\n')



                            print(name + "  " + uniq_id)


                        except:
                            print("Something went wrong")

                except:
                    print("Error")

            name_var.set("")
            duration_var.set("")
            company_var.set("")
            date_var.set("")
            email_var.set("")
        def import_csv_data_1():
            global arr
            arr = ttk.StringVar()
            csv_file_path = askopenfilename()
            print(csv_file_path)
            print("???????????????????????????????????????????????????????????????????")
            arr.set(csv_file_path)
            base_destination = 'company/'
            included_ext = ['csv']
            # arr = [fn for fn in os.listdir() if any(fn.endswith(ext) for ext in included_ext)]
            # no_of_files = len(arr)
            def calc_start(center, a, size_of_font):
                length = len(a)
                center[0] = int(center[0] - size_of_font * (length / 2))
                return center

            for i in range(0, 1):

                try:
                    group = csv_file_path
                    print(group)
                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

                    name = []
                    duration = []
                    company = []

                    date = []
                    email_id=[]
                    with open(group) as file:
                        data = csv.reader(file, delimiter=',')
                        count = 0
                        for row in data:
                            count += 1
                            if (count == 1):
                                continue
                            name.append(row[0])
                            duration.append(row[1])
                            company.append(row[2])
                            date.append(row[3])
                            email_id.append(row[4])

                    print(name[0])
                    print(company[0])
                    print(duration[0])
                    print(date[0])
                    print(email_id[0])
                    im0 = self.filename
                    print(self.filename)

                    for i in range(0, len(name)):
                        try:

                            destination = base_destination + company[i] + '/' + duration[i] + '/'
                            if not os.path.exists(destination):
                                os.makedirs(destination)
                            im1 = Image.open('Sample.jpg')

                            im3 = Image.open(im0)
                            back_im = im1.copy()
                            back_im.paste(im3, (500, 1800),mask=im3)
                            back_im.save('company/_.jpg', quality=100)



                            img = cv.imread("company/_.jpg")


                            center_1 = [1800, 1045]
                            center_2 = [1780, 1225]
                            center_3 = [2010, 1495]
                            center_4=  [2650, 2080]


                            font = cv.FONT_HERSHEY_TRIPLEX

                            size_of_font = 40

                            start_1 = calc_start(center_1, name, size_of_font)
                            start_2 = calc_start(center_2, duration, size_of_font)
                            start_3 = calc_start(center_3, company, size_of_font)
                            start_4 = calc_start(center_4,date,size_of_font)


                            cv.putText(img, name[i], tuple(start_1), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, duration[i], tuple(start_2), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img, company[i], tuple(start_3), font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.putText(img,date[i],tuple(start_4),font, 2, (0, 0, 0), 2, cv.LINE_AA)
                            cv.imwrite(destination + name[i] + '_' + company[i] +"_"+duration[i]+ '.jpg', img)
                            path=name[i] +" "+company[i]+" "+duration[i]+ '/' + '.jpg'
                            uniq_id=str(hash(path))
                            path_on_cloud = "certificates/" + name[i] +" " +company[i]+" "+duration[i]+ ".jpg"
                            path_local = destination + name[i] + '_' + company[i] +"_"+duration[i] +'.jpg'
                            storage.child(path_on_cloud).put(path_local)
                            path_cloud = uniq_id+ '/' + '.jpg'
                            storage.child(path_cloud).put(path_local)
                            from_addr = 'patel.rupin56@gmail.com'
                            to_addr = email_id
                            msg = MIMEMultipart()
                            msg['From'] = from_addr
                            msg['To'] = to_addr[i]
                            msg['subject'] = 'Your Certificate id is  '+uniq_id

                            filename = path_local
                            attachment = open(filename, 'rb')

                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload((attachment).read())
                            encoders.encode_base64(part)
                            part.add_header('Content-Disposition', "attachment; filename= " + filename)

                            msg.attach(part)

                            email = 'patel.rupin56@gmail.com'
                            password = '+++++++++++++'
                            recipients = 'patel.rupin56@gmail.com'

                            mail = smtplib.SMTP('smtp.gmail.com', 587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(email, password)
                            text = msg.as_string()
                            mail.sendmail(from_addr, to_addr[i], text)
                            mail.quit()
                            with open('Result Template-2 .txt', 'a') as the_file:
                                the_file.write(name[i] + " " + " sucessfull" + "  " + uniq_id + '\n')

                            print("{}/{}".format(i + 1, len(name)))
                        except:
                            print("Something went wrong")

                except:
                    print("file is not proper format: {}".format(arr))







        # creating a label for
        # name using widget Label
        name_label = ttk.Label(self, text='Name', font=('calibre', 10, 'bold'))

        # creating a entry for input
        # name using widget Entry
        name_entry = ttk.Entry(self, textvariable=name_var, font=('calibre', 10, 'normal'))

        # creating a label for password

        # creating a entry for password

        duration_label = ttk.Label(self, text='Duration', font=('calibre', 10, 'bold'))
        duration_entry = ttk.Entry(self, textvariable=duration_var, font=('calibre', 10, 'normal'))
        company_label = ttk.Label(self, text='Company', font=('calibre', 10, 'bold'))
        company_entry = ttk.Entry(self, textvariable=company_var, font=('calibre', 10, 'normal'))
        date_label=ttk.Label(self,text='Date',font=('calibre',10,'bold'))
        date_entry=ttk.Entry(self,textvariable=date_var, font=('calibre', 10, 'normal'))
        email_label = ttk.Label(self, text='Email Id', font=('calibre', 10, 'bold'))
        email_entry = ttk.Entry(self, textvariable=email_var, font=('calibre', 10, 'normal'))







        # creating a button using the widget
        # Button that will call the submit function
        sub_btn = ttk.Button(self, text='Submit', command=submit)
        signature = ttk.Button(self, text='signature', command=openfile)
        signature.grid(row=8, column=1, padx=10, pady=10)
        bro = ttk.Button(self, text='Browse excel', command=import_csv_data_1)


        # placing the label and entry in
        # the required position using grid
        # method
        name_label.grid(row=0, column=0)
        name_entry.grid(row=0, column=1)
        duration_label.grid(row=1, column=0)
        duration_entry.grid(row=1, column=1)
        company_label.grid(row=2, column=0)
        company_entry.grid(row=2, column=1)
        date_label.grid(row=3, column=0)
        date_entry.grid(row=3, column=1)
        email_label.grid(row=4, column=0)
        email_entry.grid(row=4, column=1)
        bro.grid(row=10,column=1, padx=10, pady=10)



        sub_btn.grid(row=5, column=1, padx=10, pady=10)



        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text="Startpage",
                             command=lambda: controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button2.grid(row=11, column=1, padx=10, pady=10)







        # performing an infinite loop
        # for the window to display

    # third window frame page2
# Driver Code
app = tkinterApp()
#app.geometry("700x500")
app.mainloop()