import base64

arquivo = eval(open("imagens.txt","r").read())
imagens = dict(arquivo)

keys = list(imagens.keys())

for i in range (0,len(keys)):
    name = 'imagens/' + keys[i]
    valor = bytes(imagens[keys[i]])
    with open(name,"wb") as fh:
        fh.write(base64.decodebytes(valor))