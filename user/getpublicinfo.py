# about user getpublicinfo
import userToken
import returnmsg
from psycopg2 import sql

def getpublicinfo(cur, args):
    id = args.get('id')
    token = args.get('token')
    getid = args.get('getid')
    #参数完整性验证
    if all([id, token, getid]) == False:
        return returnmsg.error('参数不完整', 400)

    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()

    #连接数据库，获取信息
    cur.execute(
        sql.SQL(
            'SELECT * FROM userinfo '
            'WHERE {ID}=%s'
        ).format(
            ID=sql.Identifier("ID")
        ),(getid,)
    )
    row = cur.fetchone()
    #如果用户存在
    if row != None:
        data = {
            "Id": row[0],
            "Avatar": row[5],
            "Username": row[6],
            "Sex": row[7],
            "City": row[11],
            "Streak": row[26]
        }
        return returnmsg.success(data)

    #如果用户不存在
    return returnmsg.error('用户不存在', 400)