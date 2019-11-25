import psycopg2
conn = psycopg2.connect(host = 'localhost', database = 'banco', user = 'postgres', password='86554732')
cur = conn.cursor()
# cur.execute("CREATE TABLE gado (id INT PRIMARY KEY, posicao TEXT);")
# cur.execute("INSERT INTO gado (id) VALUES (1),(2),(3),(4),(5),(6);")
conn.commit()
conn.close()
