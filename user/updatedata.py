# about user updatedata
import userToken
import returnmsg

def updatedata(mybase, json):
    #先解析json
    id = json['Id']
    token = json['Token']
    #验证Token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    user_data = json['UserData']
    #TODO 将数据更新到表里

    return returnmsg.success({})