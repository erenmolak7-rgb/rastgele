from flask import Flask,rewuest,jsonify
from flask_cors import CORS
import psycopg2,os

app=Flask(__name__)
CORS(app)

DATABASE_URL=os.getenv(
  DATABASE_URL os.getenv ("DATABASE URL","postgresql://eren:F5O6GvZJFCio1No2xxUtYaMWJGRULwrk@dpg-d6t8rafafjfc73fcq2dg-a.oregon-postgres.render.com/hello_cloud3_db_qkgm")
)

def connect_db():
  return psycopg2.connect(DATABASE_URL)
  
@app.route("/ziyaretciler",methods=["GET","POST"])
def ziyaretciler():
  conn=connect_db()
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler(id SERIAL PRIMARY KEY, isim TEXT)")

  if request.method=="POST":
    isim=request.json.get("isim")
    if isim:
      cur.excute("INSERT INTO ziyaretciler (isim) VALUES (%s)",(isim,))
      conn.commit()

cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")
isimler=[row[0]for row in cur.fetchall()]

cur.close()
conn.close()

return jsonify(isimler)

if__name__=="__main__":
app.run(host="0.0.0.0",port=5001)
