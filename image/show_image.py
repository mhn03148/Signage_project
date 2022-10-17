import os
import cv2
import numpy as np

def show_image():
    path = "./images/"
    file_list = os.listdir(path)
    img_files = [path+file for file in file_list if file.endswith('s.png')]
    print(img_files)
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cnt = len(img_files)
    idx = 0
    while True:
        img = cv2.imread(img_files[idx])
        if img is None:
            print("img load error")
            break
        cv2.imshow('image', img)
        if cv2.waitKey(1000) >= 0:
            print("keyboard")
            break
        idx += 1
        if idx >= cnt:
            idx = 0
    cv2.destroyAllWindows()
    '''
    image = cv2.imread("images/1.png", cv2.IMREAD_UNCHANGED)
    if image is None:
        print("error")
    cv2.namedWindow("as", cv2.WINDOW_GUI_EXPANDED)
    cv2.imshow("as", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
