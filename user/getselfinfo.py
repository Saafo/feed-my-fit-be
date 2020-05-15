# about user getselfinfo
import time
import userToken
import returnmsg
from psycopg2 import sql

def getselfinfo(cur, args):
    id = args.get('id')
    token = args.get('token')
    #参数完整性验证
    if all([id, token]) == False:
        return returnmsg.error('参数不完整')
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    cur.execute(
        sql.SQL(
            'SELECT * FROM userinfo '
            'WHERE {ID}=%s'
        ).format(
            ID=sql.Identifier("ID")
        ),(id,)
    )
    row = cur.fetchone()
    #组装数据
    data = {
        "PhoneNum": row[4],
        "Avatar": row[5], 
        "Username": row[6],
        "Sex": row[7], 
        "Height": row[8],
        "Weight": row[9],
        "Birth": row[10].strftime("%Y-%m-%d"), 
        "City": row[11],
        "SkinType": row[12],
        "HeatQuantityDemand": row[13],
        "ProteinDemand": row[14],
        "CarbohydratesDemand": row[15], 
        "FatDemand": row[16],
        "VitaminADemand": row[17],
        "VitaminB1Demand": row[18],
        "VitaminB2Demand": row[19],
        "VitaminB6Demand": row[20],
        "VitaminB12Demand": row[21],
        "VitaminCDemand": row[22],
        "VitaminDDemand": row[23],
        "VitaminEDemand": row[24],
        "VitaminKDemand": row[25],
        "Streak": row[26]
    }
    return returnmsg.success(data)