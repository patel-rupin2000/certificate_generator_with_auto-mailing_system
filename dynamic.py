from tkinter import *
root=Tk()
root.title("Entry Boxes")
root.geometry("700x500")
my_entries=[]
my_e=[]
m_q=[]
from tkinter.filedialog import askopenfilename
import os
global arr
global arr_image
global fon
global base_destination
import pyrebase
import csv
import cv2 as cv
my_e=[]



def import_csv_data_1():


    csv_file_path = askopenfilename()
    print(csv_file_path)
    print("???????????????????????????????????????????????????????????????????")
    arr.set(csv_file_path)
    csv_text= Label(root, text=arr.get())
    csv_text.grid(row=9, column=0, pady=20)
    global my_e
    with open(arr.get())as file:
        data = csv.reader(file, delimiter=',')

        ncol = len(next(data))
        ncol=ncol-1
        print(ncol)

        file.seek(0)
    with open(arr.get(),"r")as file:
        reader = csv.reader(file, delimiter=',')
        data = list(reader)
        row_count = len(data)
        print(row_count)


        file.seek(0)
    for x in range(ncol+1):
        my = Entry(root)
        my.grid(row=10, column=x, pady=20, padx=5)
        my_e.append(my)

def image():
    image_path = askopenfilename()
    print(image_path)
    print("???????????????????????????????????????????????????????????????????")
    arr_image.set(image_path)
    csv = Label(root, text=arr_image.get())
    csv.grid(row=12, column=0, pady=20)










def generate():
    config = {
      <Firebase configuration>
    }
    firebase = pyrebase.initialize_app(config)
    storage = firebase.storage()
    def calc_start(center, a, size_of_font):
        length = len(a)
        center[0] = int(center[0] - size_of_font * (length / 2))
        return center
    print(arr.get())
    print(base_destination.get())
    for i in range(0,1):
        try:
            group=arr.get()
            print(group)
            print(':::::::::::::::::::::::::::::::::::::')
            with open(group)as file:
                data =csv.reader(file,delimiter=',')
                ncol = len(next(data))
                d = list(data)
                row_count = len(d)
                print(row_count)
                # Read first line and count columns
                file.seek(0)
                print((ncol))

                count=0
                l=[]
                f=[]


                for row in data:
                    count+=1
                    if(count==1):
                        continue
                    for i in range(0, ncol):
                        l.append(row[i])
            print(l)

            for j in range(0,len(l),ncol):
                f.append(l[j:ncol+j])

            print(f)
            q=[]
            for i in range(0,len(f)):


                q=f[i]
                print(q)
                for k in range(0,len(q),4):
                    print(q[k])
                    try:
                        destination = base_destination.get() + q[k] + '/'
                        if not os.path.exists(destination):
                            os.makedirs(destination)
                        img = cv.imread(arr_image.get())
                        m_q=[]
                        for en in my_e:
                            l_q = []
                            l_q = list(map(int, str(en.get()).split(',')))
                            m_q.append(l_q)

                        font = cv.FONT_HERSHEY_TRIPLEX

                        size_of_font = 40
                        for a in range(0,len(m_q)):
                            start_1 = calc_start(m_q[k+a], q[k+a], size_of_font)

                            cv.putText(img, q[k+a], tuple(start_1), font, 2, (0, 0, 0), 2, cv.LINE_AA)

                        cv.imwrite(destination + q[k] + '_' + q[k+1] + "_" + q[k+2] + '.jpg', img)
                        path = q[k] + " " + q[k + 1] + " " + q[k + 2] + '/' + '.jpg'
                        uniq_id=str(hash(path))
                        path_on_cloud = "certificates/" + q[k] + " " + q[k+1] + " " + q[k+2] + ".jpg"
                        path_local = destination + q[k] + '_' + q[k+1] + "_" + q[k+2] + '.jpg'
                        storage.child(path_on_cloud).put(path_local)
                        path_cloud = uniq_id + '/' + '.jpg'
                        storage.child(path_cloud).put(path_local)
                        #f_txt = open("Result.txt", "w")
                        with open('Result.txt', 'a') as the_file:
                            the_file.write(q[k]+" "+" sucessfull"+"  "+ uniq_id +'\n')





                        print(q[k]+" "+" sucessfull"+"  "+ uniq_id)
                    except:
                        print("Something went wrong")

        except:
            print("file is not proper format: {}".format(arr))








arr = StringVar()
arr_image=StringVar()

base_destination=Entry(root)
label = Label(text='Destination folder ', font=('calibre', 10, 'bold'))
label.grid(row=1,column=0,pady=20)
base_destination.grid(row=1,column=2,pady=20)
my_button=Button(root,text="import CSV!",command=import_csv_data_1,bg='#005DF9', fg='White')
my_button.grid(row=8,column=0,pady=20)
my_button=Button(root,text="import image!",command=image,bg='#005DF9', fg='White')
my_button.grid(row=11,column=0,pady=20)
my_button=Button(root,text="Generate!",command=generate,height=2, width=15, bg='#005DF9', fg='White')
my_button.grid(row=15,column=0,pady=20)



root.mainloop()