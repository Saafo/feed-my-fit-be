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
        return returnmsg.error('参数不完整', 400)
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()

    #数据库找到momentid, thumb+1
    cur.execute(
        sql.SQL(
            'UPDATE moments '
            'SET {Thumbs} = {Thumbs} + 1 '
            'WHERE {MomentID} = %s '
            'RETURNING {Thumbs}'
        ).format(
            Thumbs=sql.Identifier("Thumbs"),
            MomentID=sql.Identifier("MomentID")
        ),(momentid,)
    )
    conn.commit()
    row = cur.fetchone()
    if row == None:
        return returnmsg.error("点赞的动态不存在", 400)

    return returnmsg.success({"Thumbs": row[0]})