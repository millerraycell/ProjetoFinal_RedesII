import cv2
import numpy as np
import os
import pyzbar.pyzbar as pyzbar
import psycopg2

conn = psycopg2.connect(host = 'localhost', database = 'banco', user = 'postgres', password='86554732')
cur = conn.cursor()

path = "imagens/"
dirs = os.listdir(path)

for files in dirs:
    img = cv2.imread("imagens/"+files)

    decodeObject = pyzbar.decode(img)

    for obj in decodeObject:
        resultado = str(obj.data)[2]
        texto = files.split()
        texto[2] = texto[2].replace(".png",'')
        cur.execute("UPDATE gado SET posicao = '(%s)', data = '(%s)', hora = '(%s)'::time WHERE id = (%d);" % (texto[0], texto[1], texto[2], int(resultado)))
        #cur.execute("SELECT * FROM gado;")
        conn.commit()
