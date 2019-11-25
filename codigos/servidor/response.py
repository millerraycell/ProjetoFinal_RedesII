import requests
import json

arq = open("localizacao.txt","w")
r = requests.get('http://34.95.155.151/send.php')

valor = r.text.split()

for i in range(0,len(valor)):
    valor[i] = valor[i].replace('\'', '').replace('(','').replace(')','').replace('[','').replace(']','').replace(',','').replace('"','')

mat = []
while len(valor) != 0:
    mat.append(valor[:8])
    del valor[:8]

j = 0
for i in range(len(mat)):
    arq.write(("Numero do Animal: %s\n" % mat[i][j]))
    arq.write(("Local do Animal: %s\n" % mat[i][j+1]))
    arq.write(("Dia: %s\n" % (mat[i][j+4] + '/' + mat[i][j+3] + '/' + mat[i][j+2])))
    arq.write(("Hora: %s\n\n" % (mat[i][j+5] + ':' + mat[i][j+6] + ':' + mat[i][j+7])))