from PIL import Image
from PIL import ImageFilter

analyse = -1
analyse = input("Rentre le chemin l'image à analyser: ")

if analyse == "img/lenny.jpg" :

  lenny_type = -1
  lenny_type = input("Niquel ! Tu as choisi lenny.jpg. Dis moi ce que tu veux faire: ")

  if lenny_type == "find-eges" :
    image = Image.open("img/lenny.jpg") 
    image = image.filter(ImageFilter.FIND_EDGES)
    image = image.save("end/lenny.jpg")
    print("C'est bon")
  if lenny_type == "contour" :
    image = Image.open("img/lenny.jpg") 
    image = image.filter(ImageFilter.CONTOUR)
    image = image.save("end/lenny.jpg")
    print("C'est bon")
  if lenny_type == "blur" :
    image = Image.open("img/lenny.jpg") 
    image = image.filter(ImageFilter.BLUR)
    image = image.save("end/lenny.jpg")
    print("C'est bon")
  if lenny_type == "maxi-blur" :
    image = Image.open("img/lenny.jpg") 
    image = image.filter(ImageFilter.GaussianBlur(20))
    image = image.save("end/lenny.jpg")
    print("C'est bon")
  if lenny_type == "enhance-max" :
    image = Image.open("img/lenny.jpg") 
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image = image.save("end/lenny.jpg")
    print("C'est bon")
  if lenny_type == "enhance" :
    image = Image.open("img/lenny.jpg")      
    image = image.filter(ImageFilter.EDGE_ENHANCE)
    image = image.save("end/lenny.jpg")
    print("C'est bon")


if analyse == "img/cat.png" :

  cat_type = -1
  cat_type = input("Niquel ! Tu as choisi cat.png. Dis moi ce que tu veux faire: ")

  if cat_type == "find-edges" :
    image = Image.open("img/cat.png") 
    image = image.filter(ImageFilter.FIND_EDGES)
    image = image.save("end/cat.png")
    print("C'est bon")
  if cat_type == "contour" :
    image = Image.open("img/cat.png") 
    image = image.filter(ImageFilter.CONTOUR)
    image = image.save("end/cat.png")
    print("C'est bon")
  if cat_type == "blur" :
    image = Image.open("img/cat.png") 
    image = image.filter(ImageFilter.BLUR)
    image = image.save("end/cat.png")
    print("C'est bon")
  if cat_type == "maxi-blur" :
    image = Image.open("img/cat.png") 
    image = image.filter(ImageFilter.GaussianBlur(20))
    image = image.save("end/cat.png")
    print("C'est bon")
  if cat_type == "enhance-max" :
    image = Image.open("img/cat.png") 
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image = image.save("end/cat.png")
    print("C'est bon")
  if cat_type == "enhance" :
    image = Image.open("img/cat.png") 
    image = image.filter(ImageFilter.EDGE_ENHANCE)
    image = image.save("end/cat.png")
    print("C'est bon")


if analyse == "img/logo.png" :

  logo_type = -1
  logo_type = input("Niquel Tu as choisi logo.png. Dis moi ce que tu veux faire: ")

  if logo_type == "find-edges" :
    image = Image.open("img/logo.png") 
    image = image.filter(ImageFilter.FIND_EDGES)
    image = image.save("end/logo.png")
    print("C'est bon")
  if logo_type == "contour" :
    image = Image.open("img/logo.png") 
    image = image.filter(ImageFilter.CONTOUR)
    image = image.save("end/logo.png")
    print("C'est bon")
  if logo_type == "blur" :
    image = Image.open("img/logo.png") 
    image = image.filter(ImageFilter.BLUR)
    image = image.save("end/logo.png")
    print("C'est bon")
  if logo_type == "maxi-blur" :
    image = Image.open("img/logo.png") 
    image = image.filter(ImageFilter.GaussianBlur(20))
    image = image.save("end/logo.png")
    print("C'est bon")
  if logo_type == "enhance-max" :
    image = Image.open("img/logo.png") 
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    image = image.save("end/logo.png")
    print("C'est bon")
  if logo_type == "enhance" :
    image = Image.open("img/logo.png") 
    image = image.filter(ImageFilter.EDGE_ENHANCE)
    image = image.save("end/logo.png")
    print("C'est bon")

