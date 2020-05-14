# about user updatetoken
import userToken
import returnmsg

def updatetoken(mybase, args):
    id = args.get('id')
    token = args.get('token')
    #参数完整性验证
    if all([id, token]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(id, token) == False:
        return returnmsg.tokeninvalid()
    
    id, token = userToken.genToken(mybase, None, id)
    data = {'Token': token}
    return returnmsg.success(data)