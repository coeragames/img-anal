from PIL import Image
from PIL import ImageFilter
import wget
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt 

url = -1
analyse = -1
analyse = url = input("Rentre le chemin l'image à analyser: ")

if url != "text" :
  wget.download(url, 'img')
  
  img_name = -1
  img_name = input(" Niquel ! Quel était le nom de l'image ? ") 

  if img_name != "text" :

    img_type = -1
    img_type = input("Parfait ! Dit moi ce que je dois faire avec " + img_name + ": ")

    if img_type == "find-eges" :
      image = Image.open("img/" + img_name) 
      image = image.filter(ImageFilter.FIND_EDGES)
      image = image.save("end/" + img_name)
      os.remove("img/" + img_name)
      print("C'est bon ! Ton image est stockée dans end/" + img_name)

    if img_type == "contour" :
      image = Image.open("img/" + img_name) 
      image = image.filter(ImageFilter.CONTOUR)
      image = image.save("end/" + img_name)
      os.remove("img/" + img_name)
      print("C'est bon ! Ton image est stockée dans end/" + img_name)

    if img_type == "blur" :
      image = Image.open("img/" + img_name) 
      image = image.filter(ImageFilter.BLUR)
      image = image.save("end/" + img_name)
      os.remove("img/" + img_name)
      print("C'est bon ! Ton image est stockée dans end/" + img_name)

    if img_type == "maxi-blur" :
      image = Image.open("img/" + img_name) 
      image = image.filter(ImageFilter.GaussianBlur(20))
      image = image.save("end/" + img_name)
      os.remove("img/" + img_name)
      print("C'est bon ! Ton image est stockée dans end/" + img_name)

    if img_type == "enhance-max" :
      image = Image.open("img/" + img_name) 
      image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
      image = image.save("end/" + img_name)
      os.remove("img/" + img_name)
      print("C'est bon ! Ton image est stockée dans end/" + img_name)

    if img_type == "enhance" :
      image = Image.open("img/" + img_name)      
      image = image.filter(ImageFilter.EDGE_ENHANCE)
      image = image.save("end/" + img_name)
      os.remove("img/" + img_name)
      print("C'est bon ! Ton image est stockée dans end/" + img_name)   

    if img_type == "blur-faces" :
      def plotImages(img): 
          plt.imshow(img, cmap="gray") 
          plt.axis('off') 
          plt.style.use('seaborn') 
          plt.show() 


      image = cv2.imread('img/' + img_name) 
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
      plotImages(image) 
      face_detect = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') 
      face_data = face_detect.detectMultiScale(image, 1.3, 5) 
      for (x, y, w, h) in face_data: 
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2) 
        roi = image[y:y+h, x:x+w]  
        roi = cv2.GaussianBlur(roi, (23, 23), 30) 
        image[y:y+roi.shape[0], x:x+roi.shape[1]] = roi 
      plotImages(image) 

     