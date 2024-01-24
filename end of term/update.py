import MySQLdb


def update_user(user_name, age, gender, email, password):

    conn = MySQLdb.connect(host='127.0.0.1', user='root',
                           passwd='', db='testdb', charset='utf8')

    cursoer = conn.cursor()

    sql = 'UPDATE `users` SET `user_name`=%s,`age`=%s,`gender`=%s,`email`=%s,`password`=%s WHERE user_name = "%s"'

    cursoer.execute(sql, (user_name, age, gender, email, password, user_name))
    conn.commit()
    
    cursoer.close()
    conn.close()
    return "update success", 200, '更動資料數：', cursoer.fetchall()
