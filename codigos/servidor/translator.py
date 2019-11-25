import base64
import os
import cv2
import numpy as np
import os
import pyzbar.pyzbar as pyzbar
import psycopg2

conn = psycopg2.connect(host = 'localhost', database = 'banco', user = 'postgres', password='12345678')
cur = conn.cursor()

path = "imagens/"
dirs = os.listdir(path)

arquivo = eval(open("imagens.txt","r").read())
imagens = dict(arquivo)

keys = list(imagens.keys())

for i in range (0,len(keys)):
    name = 'imagens/' + keys[i]
    valor = bytes(imagens[keys[i]],"utf-8")
    with open(name,"wb") as fh:
        fh.write(base64.decodebytes(valor))

for files in dirs:
    img = cv2.imread("imagens/"+files)

    decodeObject = pyzbar.decode(img)

    for obj in decodeObject:
        resultado = str(obj.data)[2]
        texto = files.split()
        texto[2] = texto[2].replace(".png",'')
        cur.execute("UPDATE gado SET posicao = '(%s)', data = '(%s)', hora = '(%s)'::time WHERE id = (%d);" % (texto[0], texto[1], texto[2], int(resultado)))
        #cur.execute("SELECT * FROM gado;")


for files in dirs:
    os.remove("imagens/"+files)