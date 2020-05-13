# about postmoment
import userToken
import returnmsg

def postmoment(mybase, json):
    id = json['Id']
    token = json['Token']
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    text = json['Text']
    pic = json['Pic']
    timestamp = json['Timestamp']
    #TODO 数据库里新增一个moment

    return returnmsg.success({"MomentID": momentid})