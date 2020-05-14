# about postmoment
import userToken
import returnmsg

def postmoment(cur, conn, json):
    id = json['Id']
    token = json['Token']
    text = json['Text']
    pic = json['Pic']
    timestamp = json['Timestamp']
    #参数完整性验证
    if all([id, token, text, pic, timestamp]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #TODO 数据库里新增一个moment

    return returnmsg.success({"MomentID": momentid})