# about postmoment
import time
import userToken
import returnmsg
from psycopg2 import sql

def postmoment(cur, conn, json):
    id = json['Id']
    token = json['Token']
    text = json['Text']
    pic = json['Pic']
    #参数完整性验证
    if all([id, token, text, pic]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #获取时间
    #服务器为北京时间
    now = time.strftime("%Y-%m-%d %H:%M:%S+08", time.localtime())
    
    #数据库里新增一个moment
    cur.execute(
        sql.SQL(
            'INSERT INTO moments '
            '({ID}, {Time}, {Text}, {Pic}) '
            'VALUES '
            '(%s, %s, %s, %s) '
            'RETURNING {MomentID}'
        ).format(
            ID=sql.Identifier("ID"),
            Time=sql.Identifier("Time"),
            Text=sql.Identifier("Text"),
            Pic=sql.Identifier("Pic"),
            MomentID=sql.Identifier("MomentID")
        ),(id, now, text, pic)
    )
    conn.commit()
    momentid = cur.fetchone()[0]

    return returnmsg.success({"MomentID": momentid})