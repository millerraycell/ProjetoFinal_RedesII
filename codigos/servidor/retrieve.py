import json
import psycopg2

conn = psycopg2.connect(host = 'localhost', database = 'banco', user = 'postgres', password='86554732')
cur = conn.cursor()

arq = open("resultado.txt", "w")
cur.execute("SELECT * FROM gado ORDER BY id;")
resultado = str(cur.fetchall()).replace('datetime.time','').replace('datetime.date','')
dados = json.dumps(resultado)

arq.write(dados)

arq.close()
conn.close()