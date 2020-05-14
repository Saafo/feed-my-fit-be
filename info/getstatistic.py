# about getstatistic
import userToken
import returnmsg

def getstatistic(cur, args):
    id = args.get('id')
    token = args.get('token')
    getall = args.get('getall')
    date = args.get('date')
    #参数完整性验证
    if all([id, token, getall, date]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()

    # TODO根据getall的情况来获取数据
    
    return returnmsg.success(data)