import pymysql


def select_president():
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           passwd='', db='testdb', charset='utf8')

    cursoer = conn.cursor()

    sql = 'SELECT * FROM `users` WHERE  president_id = 1'

    cursoer.execute(sql)
    conn.commit()

    cursoer.close()
    conn.close()
    
    return cursoer.fetchall()

