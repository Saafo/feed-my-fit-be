# about postcomment
import time
import userToken
import returnmsg
from psycopg2 import sql

def postcomment(cur, conn, json):
    try:
        id = json['Id']
        token = json['Token']
        momentid = json['MomentID']
        text = json['Text']
    #参数完整性验证
    except KeyError:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()

    #获取时间
    #服务器为北京时间
    now = time.strftime("%Y-%m-%d %H:%M:%S+08", time.localtime())

    #先检查是否存在动态
    cur.execute(
        sql.SQL(
            'SELECT {MomentID} FROM moments '
            'WHERE {MomentID} = %s'
        ).format(
            MomentID=sql.Identifier("MomentID")
        ),(momentid,)
    )
    if cur.fetchone == None:
        return returnmsg.error("评论的动态不存在")

    #连接数据库，插入评论
    cur.execute(
        sql.SQL(
            'INSERT INTO comments '
            '({MomentID}, {ID}, {Time}, {Text}) '
            'VALUES '
            '(%s, %s, %s, %s) '
            'RETURNING {CommentID}'
        ).format(
            MomentID=sql.Identifier("MomentID"),
            ID=sql.Identifier("ID"),
            Time=sql.Identifier("Time"),
            Text=sql.Identifier("Text"),
            CommentID=sql.Identifier("CommentID")
        ),(momentid, id, now, text)
    )
    conn.commit()
    commentid = cur.fetchone()[0]

    return returnmsg.success({"CommentID": commentid})