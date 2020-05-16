# about getmoment
import userToken
import returnmsg
from psycopg2 import sql

def getmoment(cur, args):
    id = args.get('id')
    token = args.get('token')
    momentid = args.get('momentid')
    #参数完整性验证
    if all([id, token, momentid]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #从数据库中获取momentid的数据
    cur.execute(
        sql.SQL(
            'SELECT m.{ID}, {MomentID}, {Time}, {Text}, {Pic}, '
            '{Thumbs}, {Username}, {Avatar}, {Streak} '
            'FROM moments as m, userinfo as i '
            'WHERE m.{ID} = i.{ID} and {MomentID} = %s'
        ).format(
            ID=sql.Identifier("ID"),
            MomentID=sql.Identifier("MomentID"),
            Time=sql.Identifier("Time"),
            Text=sql.Identifier("Text"),
            Pic=sql.Identifier("Pic"),
            Thumbs=sql.Identifier("Thumbs"),
            Username=sql.Identifier("Username"),
            Avatar=sql.Identifier("Avatar"),
            Streak=sql.Identifier("Streak")
        ),(momentid,)
    )
    info_row = cur.fetchone()
    if info_row == None:
        return returnmsg.empty("无动态数据")
    #查询评论数据
    cur.execute(
        sql.SQL(
            'SELECT {MomentID}, {CommentID}, c.{ID}, '
            '{Time}, {Text}, {Username} '
            'FROM comments as c, userinfo as i '
            'WHERE c.{ID} = i.{ID} and {MomentID} = %s'
        ).format(
            MomentID=sql.Identifier("MomentID"),
            CommentID=sql.Identifier("CommentID"),
            ID=sql.Identifier("ID"),
            Time=sql.Identifier("Time"),
            Text=sql.Identifier("Text"),
            Username=sql.Identifier("Username"),
        ),(momentid,)
    )
    comment_rows = cur.fetchall()
    #comments集
    comments = {}
    for row in comment_rows:
        comments.update(
            {
                row[1]: {
                "Id": row[2],
                "Username": row[5],
                "Text": row[4],
                "Time": row[3] #TODO 时间格式，时区转换
                }
            }
        )

    return returnmsg.success(
        {
            "MomentID": info_row[1],
            "Id": info_row[0],
            "Time": info_row[2], #TODO 时间格式转换
            "Text": info_row[3],
            "Pic": info_row[4],
            "Thumbs": info_row[5],
            "Username": info_row[6],
            "Avatar": info_row[7],
            "Streak": info_row[8],
            "Comments": comments
        }
    )