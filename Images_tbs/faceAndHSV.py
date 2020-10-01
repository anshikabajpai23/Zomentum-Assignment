# -*- coding: utf-8 -*-

import cv2
import numpy as np
from PIL import Image 
import requests
import xlrd 
import os
#dataset of which the details will be extracted.
loc = ("FEAR.xlsx")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 2) 
imageURL = list()
for i in range(1,sheet.nrows): 
    imageURL.append(sheet.cell_value(i, 2).rstrip(os.linesep))
    #print(sheet.cell_value(i, 2))
#this file contains all the algo required for face detection, CV2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceCount = list()
H = list()
S = list()
V = list()
url_of_image = list()
j = 0
for i in imageURL:
  try:
    url = str(i).rstrip(os.linesep)
    image = Image.open(requests.get(url, stream=True).raw)
    width, height = image.size

    pil_image = image.convert('RGB') 
    image = np.array(pil_image) 

    # Convert RGB to BGR 
    image = image[:, :, ::-1].copy() 
 
    # perform the actual resizing of the image and show it
    x = 400
    y = (int)(height/width) * 400
    #image = cv2.resize(image, (x, y), interpolation = cv2.INTER_AREA)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faceCount.append(len(faces))
    url_of_image.append(url)
    
    hsv = cv2.cvtColor(np.float32(image),cv2.COLOR_BGR2HSV)
    hue, sat, val = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]
    h = np.mean(hsv[:,:,0])
    s = np.mean(hsv[:,:,1])
    v = ((np.mean(val))*100)/255  
    H.append(h)
    S.append(s)
    V.append(v)
    #for BGR VALUES
    #r = np.mean(image[:,:,0])
    #g = np.mean(image[:,:,1])
    #b = np.mean(image[:,:,2])
    j = j+1
    print(j)
  except:
    pass
print(faceCount)

from pandas import DataFrame
df = DataFrame({'url':url_of_image,'faceCount': faceCount, 'H':H,'S':S,'V':V})
print(df)
df.to_excel('FEAR_output.xlsx', sheet_name='sheet1', index=False)
