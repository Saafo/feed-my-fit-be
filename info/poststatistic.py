# about poststatistic
import userToken
import returnmsg

def poststatistic(mybase, json):
    #先解析json
    id = json['Id']
    token = json['Token']
    #验证Token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    user_statistic = json['UserStatistic']
    #TODO 将数据更新到表里
    #判断日期是否存在，存在则更新，不存在则新建

    return returnmsg.success({})