# about getmomentsid
import userToken
import returnmsg
from psycopg2 import sql

def getmomentsid(cur, args):
    id = args.get('id')
    token = args.get('token')
    getall = args.get('getall')
    getid = args.get('getid')
    #参数完整性验证
    if all([id, token, getall, getid]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #根据getall的情况来获取数据
    #选择单用户的所有moments
    if getall == "false":
        #先查询用户是否存在
        cur.execute(
            sql.SQL(
                'SELECT {ID} FROM userinfo '
                'WHERE {ID} = %s'
            ).format(
                ID=sql.Identifier("ID")
            ),(id,)
        )
        if len(cur.fetchone()) == 0:
            return returnmsg.error("此用户不存在")

        cur.execute(
            sql.SQL(
                'SELECT {MomentID} FROM moments '
                'WHERE {ID} = %s'
            ).format(
                MomentID=sql.Identifier("MomendID"),
                ID=sql.Identifier("ID")
            ),(id,)
        )
    
    #所有用户的moments
    elif getall == "true":
        cur.execute(
            sql.SQL(
                'SELECT {MomentID} FROM moments'
            ).format(
                MomentID=sql.Identifier("MomentID")
            )
        )

    else:
        return returnmsg.error("gerall值异常")

    rows = cur.fetchall()
    #没有动态
    if len(rows) == 0:
        return returnmsg.empty('无动态数据')

    momentsids = []
    for row in rows:
        momentsids.append(row[0])
    #反向，按时间顺序排列
    momentsids.reverse()

    return returnmsg.success({"MomentsIDs": momentsids})