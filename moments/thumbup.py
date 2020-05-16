# about thumbup
import userToken
import returnmsg
from psycopg2 import sql

def thumbup(cur, conn, args):
    id = args.get('id')
    token = args.get('token')
    momentid = args.get('momentid')
    #参数完整性验证
    if all([id, token, momentid]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()

    #数据库找到momentid, thumb+1
    cur.execute(
        sql.SQL(
            'SELECT {Thumbs} FROM moments '
            'WHERE {MomentID} = %s'
        ).format(
            Thumbs=sql.Identifier("Thumbs"),
            MomentID=sql.Identifier("MomentID")
        ),(momentid,)
    )
    row = cur.fetchone()
    if row == None:
        return returnmsg.error("点赞的动态不存在")
    thumbs = row[0]
    #点赞操作
    thumbs += 1 
    #写入数据库
    cur.execute(
        sql.SQL(
            'UPDATE moments '
            'SET {Thumbs} = %s '
            'WHERE {MomentID} = %s'
        ).format(
            Thumbs=sql.Identifier("Thumbs"),
            MomentID=sql.Identifier("MomentID")
        ),(thumbs, momentid)
    )
    conn.commit()

    return returnmsg.success({})