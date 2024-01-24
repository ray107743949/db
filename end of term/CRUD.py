import pymysql



def select_position(data):
    conn = pymysql.connect(host='127.0.0.1', user='root',
                         passwd='', db='testdb', charset='utf8')

    cursoer = conn.cursor()
    print(data)
    sql = 'SELECT id,name,gender,age,nation,county,Township FROM `users` WHERE  position_id = '+data+''

    cursoer.execute(sql)
    conn.commit()

    cursoer.close()
    conn.close()
        
    return cursoer.fetchall() 



def delete_user(user_name):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root',
                                passwd='', db='testdb', charset='utf8')

        cursoer = conn.cursor()

        sql = 'DELETE FROM `users` WHERE `id` = %s'
        cursoer.execute(sql, user_name)

        conn.commit()
        sql = 'SELECT * FROM `users`'

        print(cursoer.execute(sql))                                                            

        print(cursoer.fetchall())

        cursoer.close()
        conn.close()
        return "delete success"

    except:
        cursoer.close()
        conn.close()
        return "delete fail"
    

def insert_user(data):
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root',
                                passwd='', db='testdb', charset='utf8')

        cursoer = conn.cursor()
        sql = 'INSERT INTO users(id,name,gender,age,position_id,nation, county,township) VALUES (NULL,%s,%s,%s,%s,%s,%s,%s)'
        cursoer.execute(sql,(data))
        conn.commit()
        cursoer.close()
        conn.close()
        return "insert success"
    except:
        cursoer.close()
        conn.close()
        return "insert fail"
    

def update_user(data):

    conn = pymysql.connect(host='127.0.0.1', user='root',
                        passwd='', db='testdb', charset='utf8')

    cursoer = conn.cursor()

    sql = 'UPDATE `users` SET `id` = %s,`name`=%s,`gender`=%s,`position_id`=%s,`age`=%s,`nation`=%s,`county`=%s,`township`=%s WHERE id = %s'

    cursoer.execute(sql,data)
    conn.commit()
        
    cursoer.close()
    conn.close()
    return "update success", 200, '更動資料數：', cursoer.fetchall()


def select_id(data):
    conn = pymysql.connect(host='127.0.0.1', user='root',
                         passwd='', db='testdb', charset='utf8')

    cursoer = conn.cursor()
    sql = 'SELECT name,gender,position_id,age,nation,county,Township FROM `users` WHERE  id = '+data+''

    cursoer.execute(sql)
    conn.commit()

    cursoer.close()
    conn.close()
        
    return cursoer.fetchall() 