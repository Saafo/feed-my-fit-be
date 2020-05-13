# about postcomment
import userToken
import returnmsg

def postcomment(mybase, json):
    id = json['Id']
    token = json['Token']
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    momentid = json['MomentID']
    text = json['Text']
    timestamp = json['Timestamp']
    
    #TODO 连接数据库，插入评论

    return returnmsg.success({"CommentID": commentid})