import cv2
import os
import numpy as np
import time

destino = '/media/miller/5A0CA98A0CA961AD/Users/mille/Documents/Faculdade/5 Semestre/Redes de Computadores II/ProjetoFinal_RedesII/codigos/cliente/imagens/'
#os.chdir(destino)

cap1 = cv2.VideoCapture(2)
cap2 = cv2.VideoCapture(4)
cap3 = cv2.VideoCapture(0)
cap4 = cv2.VideoCapture(6)
  
ret1, frame1 = cap1.read()
ret2, frame2 = cap2.read()
ret3, frame3 = cap3.read()
ret4, frame4 = cap4.read()

if ret1:
    dia = time.localtime()
    data = str(dia[0]) + '-' + str(dia[1]) + '-' + str(dia[2]) + ' ' + str(dia[3]) + ':' + str(dia[4]) + ':' + str(dia[5])
    
    filename = 'pasto1' + ' ' + data + '.png'
    cv2.imwrite((destino+filename),frame1)

if ret2:
    dia = time.localtime()
    data = str(dia[0]) + '-' + str(dia[1]) + '-' + str(dia[2]) + ' ' + str(dia[3]) + ':' + str(dia[4]) + ':' + str(dia[5])
    
    filename = 'pasto2' + ' ' + data + '.png'
    cv2.imwrite((destino+filename),frame2)

if ret3:
    dia = time.localtime()
    data = str(dia[0]) + '-' + str(dia[1]) + '-' + str(dia[2]) + ' ' + str(dia[3]) + ':' + str(dia[4]) + ':' + str(dia[5])
    
    filename = 'pasto3' + ' ' + data + '.png'
    cv2.imwrite((destino+filename),frame3)

if ret4:
    dia = time.localtime()
    data = str(dia[0]) + '-' + str(dia[1]) + '-' + str(dia[2]) + ' ' + str(dia[3]) + ':' + str(dia[4]) + ':' + str(dia[5])
    
    filename = 'bebedouro' + ' ' + data + '.png'
    cv2.imwrite((destino+filename),frame4)

cap1.release()
cap2.release()
cap3.release()
cap4.release()
cv2.destroyAllWindows()