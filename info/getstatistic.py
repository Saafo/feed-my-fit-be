# about getstatistic
import userToken
import returnmsg

def getstatistic(mybase, args):
    id = args.get('id')
    token = args.get('token')
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    getall = args.get('getall')
    date = args.get('date')

    # TODO根据getall的情况来获取数据
    
    return returnmsg.success(data)