from flask import Flask, request, jsonify
import json
import pandas as pd
import cv2
import numpy as np
import argparse
import time
import os
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route('/')
def count_oranges():
 #Open a simple image
 m=cv2.imread("C:/Users/User/Desktop/m.jpg")
 img_HSV = cv2.cvtColor( m, cv2.COLOR_BGR2HSV)
 #skin color range for hsv color space
 HSV_mask = cv2.inRange(img_HSV, (0, 80, 20), (25, 255, 255))
 target = cv2.bitwise_and(m,m, mask=HSV_mask)
 cv2.imwrite('segmented out region.jpg',target)
 bounding_boxes = []
 threshold = 75
 ar=[]
 imgwithbox = m.copy()
 for c in contours:
      area = cv2.contourArea(c)
      if area >threshold:
          [x,y,w,h]=cv2.boundingRect(c)
          bounding_boxes.append([x,y,w,h])
          print([x,y,w,h])
          area_rect=w*h
          print(area_rect)
          ar.append(area_rect)
          cv2.rectangle(imgwithbox,(x,y),(x+w,y+h),(0,255,0),2)
 print(len(bounding_boxes))
 print(ar)
 total_area=sum(ar)
 print(total_area)
 avg_rect= total_area/len(bounding_boxes)
 print(avg_rect)
 q=np.asarray(ar)
 number_of_oranges_list=[]
 print(q)
 no_of_oranges = q/avg_rect
 print(no_of_oranges)
 rounded_value=np.around(no_of_oranges,0)
 print(rounded_value)
 total_fruits=sum(rounded_value)
 print(total_fruits)
 number_of_oranges_list=[]
 print(no_of_oranges)
 for count in enumerate(no_of_oranges):
 #     print(index)
      if count[1]<0.3:
          no_of_oranges[count[0]]=0
      elif count[1]>0.3 and count[1]<1.5:
          no_of_oranges[count[0]]=1
      elif count[1]>1.5 and count[1]<2.5:
          no_of_oranges[count[0]]=2
      elif count[1]>2.5 and count[1]<3.5:
          no_of_oranges[count[0]]=3
 no_of_oranges    
 print(int(fruits))
 output = m.copy()
 #cv2.putText(output, "WELCOME TO PROJECT FRUIT", (10, 25),
 cv2.putText(output,f" Number  of  fruits : {fruits}", (10, 25),
           
     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
 cv2.imshow("Text", output)
app.run(port=600,debug=False)
