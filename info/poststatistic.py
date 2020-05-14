# about poststatistic
import userToken
import returnmsg

def poststatistic(cur, conn, json):
    #先解析json
    id = json['Id']
    token = json['Token']
    user_statistic = json['UserStatistic']
    #参数完整性验证
    if all([id, token, user_statistic]) == False:
        return returnmsg.error('参数不完整')
    
    #验证Token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #TODO 将数据更新到表里
    #判断日期是否存在，存在则更新，不存在则新建

    return returnmsg.success({})