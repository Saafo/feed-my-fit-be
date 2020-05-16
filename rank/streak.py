# about streak
import time
import userToken
import returnmsg
from psycopg2 import sql

def streak(cur, args):
    id = args.get('id')
    token = args.get('token')
    #参数完整性验证
    if all([id, token]) == False:
        return returnmsg.error('参数不完整', 400)
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #数据库部分
    cur.execute(
        sql.SQL(
            'SELECT {ID}, {Username}, {Avatar}, {Streak} '
            'FROM userinfo '
            'WHERE {City} = ( '
                'SELECT {City} FROM userinfo '
                'WHERE {ID} = %s) '
            'ORDER BY {Streak} DESC '
            'LIMIT 50'
        ).format(
            ID=sql.Identifier("ID"),
            Username=sql.Identifier("Username"),
            Avatar=sql.Identifier("Avatar"),
            Streak=sql.Identifier("Streak"),
            City=sql.Identifier("City")
        ),(id,)
    )
    rows = cur.fetchall()
    if len(rows) == 0:
        return returnmsg.empty("今日还没有排行榜数据")
    ids = []
    usernames = []
    avatars = []
    streak = []
    for row in rows:
        ids.append(row[0])
        usernames.append(row[1])
        avatars.append(row[2])
        streak.append(row[3])
    
    return returnmsg.success({
        "Ids": ids,
        "Usernames": usernames,
        "Avatars": avatars,
        "Streak": streak
    })