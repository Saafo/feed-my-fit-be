# This file is about token
import random

# This function is generate a new token
def genToken(mybase, phone_num, id):
    # 生成Token
    randomList = list('abcdefghijklmnopqrstuvwxyz0123456789')
    token = ''
    for _ in range(32):
        token += random.choice(randomList)
    #TODO 到数据库中更新Token，有则更新token，无则新建用户更新token
    #先判断是phone_num还是id
    id = ''

    return id, token

def testToken(mybase, id, token):
    #TODO 到数据库中验证token是否合法，返回True or False
    pass

if __name__ == "__main__":
    genToken()