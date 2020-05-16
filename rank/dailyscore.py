# about dailyscore
import time
import userToken
import returnmsg
from psycopg2 import sql

def dailyscore(cur, args):
    id = args.get('id')
    token = args.get('token')
    #参数完整性验证
    if all([id, token]) == False:
        return returnmsg.error('参数不完整', 400)
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #获取日期
    #服务器是北京时间
    today = time.strftime("%Y-%m-%d", time.localtime())
    
    #数据库部分
    cur.execute(
        sql.SQL(
            'SELECT i.{ID}, {Username}, {Avatar}, {HealthyScore} '
            'FROM userinfo as i, userdata as d '
            'WHERE i.{ID} = d.{ID} '
            'AND {City} = ( '
                'SELECT {City} FROM userinfo '
                'WHERE {ID} = %s) '
            'AND {Date} = %s '
            'ORDER BY {HealthyScore} DESC '
            'LIMIT 50'
        ).format(
            ID=sql.Identifier("ID"),
            Username=sql.Identifier("Username"),
            Avatar=sql.Identifier("Avatar"),
            HealthyScore=sql.Identifier("HealthyScore"),
            City=sql.Identifier("City"),
            Date=sql.Identifier("Date")
        ),(id, today)
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        return returnmsg.empty("今日还没有排行榜数据")
    ids = []
    usernames = []
    avatars = []
    healthyscores = []
    for row in rows:
        ids.append(row[0])
        usernames.append(row[1])
        avatars.append(row[2])
        healthyscores.append(row[3])
    
    return returnmsg.success({
        "Ids": ids,
        "Usernames": usernames,
        "Avatars": avatars,
        "HealthyScores": healthyscores
    })