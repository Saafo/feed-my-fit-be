# about postcomment
import userToken
import returnmsg

def postcomment(cur, conn, json):
    id = json['Id']
    token = json['Token']
    momentid = json['MomentID']
    text = json['Text']
    timestamp = json['Timestamp']
    #参数完整性验证
    if all([id, token, momentid, text, timestamp]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    #TODO 连接数据库，插入评论

    return returnmsg.success({"CommentID": commentid})