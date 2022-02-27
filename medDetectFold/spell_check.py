import cv2
import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt
import os
import pickle as pkl
import pytesseract 
from spellchecker import SpellChecker
import re 


main_text=[]


large = cv2.imread('5.png')
rgb = cv2.pyrDown(large)
rgb_orig = rgb.copy()
small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

cv2.imshow("black",small)
cv2.waitKey(0)

# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
kernel = np.ones((5, 5), np.uint8)
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
font = cv2.FONT_HERSHEY_COMPLEX
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

# using RETR_EXTERNAL instead of RETR_CCOMP
contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(contours[0])


mask = np.zeros(bw.shape, dtype=np.uint8)

for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)

    if r > 0.45 and w > 8 and h > 8:
        cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)
        detected_img = rgb_orig[y:y+h, x:x+w]
        pkl.dump(detected_img, open(f"{idx}_detect", "wb" )) 


# for p in box:
#   pt = (p[0],p[1])
#   print(pt)
#   cv2.circle(rgb,pt,5,(200,0,0),2)

rc= cv2.minAreaRect(contours[5])  
box = cv2.boxPoints(rc)

cv2.imshow('rect',rgb)
cv2.waitKey(0)




for i in range(1,len(contours)):
    try:
    	path = '/Users/maheshjain/Desktop/Brain/Saved/'
    	one_detect = pkl.load(open( f'{i}_detect', "rb" ))
    	cv2.imwrite(os.path.join(path , f'{i}_detect.jpg'),one_detect)
    	cv2.imshow('test',one_detect)
    	img_cv = cv2.imread(os.path.join(path , f'{i}_detect.jpg'))
    	img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    	grayImage = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    	text_final = pytesseract.image_to_string(grayImage)
    	text_final = re.sub(r'[^\w\s]','',text_final)
    	text_final = text_final.replace('_', '')
    	text_final=text_final.split()
    	main_text.append(text_final)
    	i= i+1
    	cv2.waitKey(1)


        

    except:
        pass

output = []



def reemovNestings(main_text):
    for i in main_text:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)
  
reemovNestings(main_text)



spell = SpellChecker()
spell.word_frequency.load_words(['remdesivir', 'mgvial', 'lyophilized','mg','ml','heaven'])
misspelled = spell.unknown(output)
print(misspelled)
print(output)









