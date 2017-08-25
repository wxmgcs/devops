import MySQLdb

host,user,pwd,db = 'localhost','root','ctu800617','ctu_devops'

def execute_non_sql(sql):
    conn = MySQLdb.connect(host,user,pwd,db)
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def execute_non_sql2(sql,db):
    conn = MySQLdb.connect(host,user,pwd,db)
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()


def execute_sql(sql):
    conn = MySQLdb.connect(host,user,pwd,db)
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    line =  None
    try:
        cur.execute(sql)
        line = cur.fetchall()
        print ("\n>>>".join([sql,line]))
    except:
        conn.rollback()
    conn.close()

    return line