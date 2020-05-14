# about user updatedata
import userToken
import returnmsg

def updatedata(cur, conn, json):
    #先解析json
    id = json['Id']
    token = json['Token']
    user_data = json['UserData']
    #参数完整性验证
    if all([id, token, user_data]) == False:
        return returnmsg.error('参数不完整')
    
    #验证Token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #TODO 将数据更新到表里

    return returnmsg.success({})