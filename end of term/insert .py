import pymysql


def insert_user(user_name, age, gender, email, password):
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           passwd='', db='testdb', charset='utf8')

    cursoer = conn.cursor()

    sql = 'INSERT INTO users(user_name,age,gender,email, password) VALUES (%s,%s,%s,%s,%s)'
    cursoer.executemany(sql, [
        (user_name, age, gender, email, password)
    ])

    conn.commit()

    sql = 'SELECT * FROM `users`'

    print(cursoer.execute(sql))

    print(cursoer.fetchall())

    cursoer.close()
    conn.close()
