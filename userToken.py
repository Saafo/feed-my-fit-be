# This file is about token
import random
from psycopg2 import sql

# This function is generate a new token
def genToken(cur, conn, phone_num, id):
    # 生成Token
    randomList = list('abcdefghijklmnopqrstuvwxyz0123456789')
    token = ''
    needinfo = False #True为没信息，False为有信息
    for _ in range(32):
        token += random.choice(randomList)
    # 到数据库中更新Token，有则更新token，无则新建用户更新token
    #先判断是phone_num还是id
    if phone_num != None:
        cur.execute(
            sql.SQL( #使用sql模块来防止sql注入
                'SELECT {ID} FROM userinfo '
                'WHERE {PhoneNum}=%s'
            ).format(
                ID=sql.Identifier("ID"),
                PhoneNum=sql.Identifier("PhoneNum")
            ),(phone_num,)
        )
        rows = cur.fetchall()
        #如果用户不存在
        if len(rows) == 0:
            #新建用户
            cur.execute(
                sql.SQL(
                    'INSERT INTO userinfo '
                    '({Token}, {PhoneNum}) '
                    'VALUES '
                    '(%s, %s)'
                ).format(
                    Token=sql.Identifier("Token"),
                    PhoneNum=sql.Identifier("PhoneNum")
                ),(token, phone_num)
            )
            conn.commit()
            cur.execute(
                sql.SQL(
                    'SELECT {ID} FROM userinfo '
                    'WHERE {PhoneNum}=%s'
                ).format(
                    ID=sql.Identifier("ID"),
                    PhoneNum=sql.Identifier("PhoneNum")
                ),(phone_num,)
            )
            rows = cur.fetchall()
        #再怎么也有了吧，该干正事了哈
        if len(rows) == 1: #TODO这里有点隐患，以后再迭代吧
            id = rows[0][0]
            cur.execute(
                sql.SQL(
                    'UPDATE userinfo '
                    'SET {Token} = %s '
                    'WHERE {PhoneNum} = %s'
                ).format(
                    Token=sql.Identifier("Token"),
                    PhoneNum=sql.Identifier("PhoneNum"),
                ),(token, phone_num)
            )
            conn.commit()

    elif id != None:
        cur.execute(
            sql.SQL(
                'UPDATE userinfo '
                'SET {Token} = %s '
                'WHERE {ID} = %s'
            ).format(
                Token=sql.Identifier("Token"),
                ID=sql.Identifier("ID")
            ),(token, id)
        )
        conn.commit()
    #最后从表中取出数据
    cur.execute(
        sql.SQL(
            'SELECT {ID},{Token},{Height} FROM userinfo '
            'WHERE {ID}=%s'
        ).format(
            ID=sql.Identifier("ID"),
            Token=sql.Identifier("Token"),
            Height=sql.Identifier("Height")
        ),(id,)
    )
    rows = cur.fetchall()
    id = rows[0][0]
    token = rows[0][1]

    #验证是否填了信息
    if rows[0][2] == None:
        needinfo = True

    return id, token, needinfo

def testToken(cur, id, token):
    cur.execute(
        sql.SQL(
            'SELECT {Token} FROM userinfo '
            'WHERE {ID}=%s'
        ).format(
            Token=sql.Identifier("Token"),
            ID=sql.Identifier("ID")
        ),(id,)
    )
    rows = cur.fetchall()
    realtoken=rows[0][0]
    if realtoken == token:
        return True
    return False
