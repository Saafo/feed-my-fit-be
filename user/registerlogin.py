# about user login
import userToken
import returnmsg
import aescrypt

def registerlogin(mybase, args):
    phone_num = args.get('phonenum')
    key = args.get('key')
    #参数完整性验证
    if all([phone_num, key]) == False:
        return returnmsg.error('参数不完整')
    
    #验证key
    if aescrypt.verify_key(phone_num, key) == False:
        return returnmsg.error('Key不合法')
    #生成随机token并写入数据库，从数据库返回id,将id和token一并return
    id, token = userToken.genToken(mybase, phone_num, None)
    data = {'Id': id, 'Token': token}
    return returnmsg.success(data)