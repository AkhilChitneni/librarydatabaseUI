import sqlite3

def connect():
    con = sqlite3.connect("oops.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS lib1(id INTEGER PRIMARY KEY,name text,sid text,bookname text,bookid text)")
    con.commit()
    con.close()

def insert(name,sid,book,book_id):
    con = sqlite3.connect("oops.db")
    cur=con.cursor()
    cur.execute("INSERT INTO lib1 values(NULL,?,?,?,?)",(name,sid,book,book_id))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("oops.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM lib1")
    l = cur.fetchall()
    con.close()
    return l

def search(name="",sid="",book="",book_id=""):
    con = sqlite3.connect("oops.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM lib1 WHERE name = ? OR sid = ? OR bookname = ? OR bookid = ?",(name,sid,book,book_id))
    l = cur.fetchall()
    con.close()
    return l

def delete(id):
    con = sqlite3.connect("oops.db")
    cur=con.cursor()
    cur.execute("DELETE FROM lib1 WHERE id = ?",(id,))
    con.commit()
    con.close()

def update(id,name,sid,book,book_id):
    con = sqlite3.connect("oops.db")
    cur=con.cursor()
    cur.execute("UPDATE lib1 set name=?,sid=?,bookname=?,bookid=? WHERE id = ?",(name,sid,book,book_id,id))
    con.commit()
    con.close()

connect()
