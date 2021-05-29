# importing the module
import cv2
from tkinter.filedialog import askopenfilename
import PIL
from PIL import Image
global image_path

# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        img_1 = PIL.Image.open(image_path)
        print(x,y)

        # fetching the dimensions
        wid, hgt = img_1.size

        a=(wid/800) * x
        b=(hgt/500) * y
        # displaying the coordinates
        # on the Shell
        a1=int(a)
        b1=int(b)
        print(a1, ' ', b1)


        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(a1) + ',' +
                    str(b1), (x, y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)




# driver function
if __name__ == "__main__":
    image_path = askopenfilename()
    print(image_path)
    print("???????????????????????????????????????????????????????????????????")



    # reading the image
    img = cv2.imread(image_path, 1)
    img_1 = PIL.Image.open(image_path)

    # fetching the dimensions
    wid, hgt = img_1.size


    # displaying the dimensions
    print(str(wid) + "x" + str(hgt))


    img = cv2.resize(img, (800 , 500))

    cv2.imshow('image', img)

    # setting mouse hadler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
