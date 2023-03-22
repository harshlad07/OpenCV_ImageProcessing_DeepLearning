import cv2
import numpy as np
import matplotlib as plt
import time

drawing = False
ix = -1
iy = -1

def read_image(image):
    img = cv2.imread(image)
    return img

def show_image(image):
    cv2.imshow(f'{image}', image)
    cv2.waitKey(0)

def draw(event, x, y, flags, paramq):
    # print("inside draw funtion")
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(image, (x,y), 50, (0,255,0), -1)
        # cv2.imshow('draw1', image)
        # print("letclaick")
        drawing = True
        ix = x
        iy = y
        # print(ix)
        # print(iy)

    elif event == cv2.EVENT_MOUSEMOVE:
        # print("mouse move")
        if drawing == True:
            # print("in drawing")
            # print(x)
            # print(y)
            # print('##############')
            # print(ix)
            # print(iy)

            cv2.rectangle(image, (ix,iy), (x,y), (0,255,0), thickness=0)
            # cv2.circle(image, (x,y), 100, (0,255,0), -1)
            cv2.imshow('draw1', image)

    elif event == cv2.EVENT_LBUTTONUP:
        # print("left up")
        drawing = False
        cv2.rectangle(image, (ix,iy),(x,y),(0,255,0), thickness=0)
        # cv2.circle(image, (x,y), 5, (0,255,0), -1)

    return image


image = np.zeros((300,300,3))

# image = read_image('rickmorty.jpg')
# image = cv2.resize(image, (640 , 480))
cv2.namedWindow(winname='draw')
cv2.setMouseCallback('draw', draw)
# print(image.shape)
# print(image.shape)

#Adding Text to image
# font = cv2.FONT_HERSHEY_COMPLEX
# text_image = cv2.putText(image, "LAD", (320,240), font, fontScale=5, color=(255,0,0), thickness=2)
# show_image(text_image)

while True:

    # image = cv2.setMouseCallback('draw', draw)
    # time.sleep(5)
    cv2.imshow('draw', image)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()