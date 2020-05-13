# about getmomentsid
import userToken
import returnmsg

def getmomentsid(mybase, args):
    id = args.get('id')
    token = args.get('token')
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    getall = args.get('getall')
    getid = args.get('getid')
    
    #TODO 根据getall的情况来获取数据
    #getall=false
    #if 用户不存在
        # return returnmsg.error('用户不存在')
    
    #getall=true

    return returnmsg.success(data)