# about user updatedata
import userToken
import returnmsg
from psycopg2 import sql

def updatedata(cur, conn, json):
    #先解析json
    id = json['Id']
    token = json['Token']
    user_data = json['UserData']
    #参数完整性验证
    if all([id, token, user_data]) == False:
        return returnmsg.error('参数不完整')
    
    #user_data完整性验证
    try:
        avatar = user_data['Avatar']
        username = user_data['Username']
        sex = user_data['Sex']
        height = user_data['Height']
        weight = user_data['Weight']
        birth = user_data['Birth']
        city = user_data['City']
        skintype = user_data['SkinType']
        heatquantitydemand = user_data['HeatQuantityDemand']
        proteindemand = user_data['ProteinDemand']
        carbohydratesdemand = user_data['CarbohydratesDemand']
        fatdemand = user_data['FatDemand']
        vitaminademand = user_data['VitaminADemand']
        vitaminb1demand = user_data['VitaminB1Demand']
        vitaminb2demand = user_data['VitaminB2Demand']
        vitaminb6demand = user_data['VitaminB6Demand']
        vitaminb12demand = user_data['VitaminB12Demand']
        vitamincdemand = user_data['VitaminCDemand']
        vitaminddemand = user_data['VitaminDDemand']
        vitaminedemand = user_data['VitaminEDemand']
        vitaminkdemand = user_data['VitaminKDemand']
    except KeyError:
        return returnmsg.error('UserData参数不完整')
    
    #验证Token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #将数据更新到表里
    cur.execute(
        sql.SQL(
            'UPDATE userinfo '
            'SET {Avatar} = %s, '
            '{Username} = %s, '
            '{Sex} = %s, '
            '{Height} = %s, '
            '{Weight} = %s, '
            '{Birth} = %s, '
            '{City} = %s, '
            '{SkinType} = %s, '
            '{HeatQuantityDemand} = %s, '
            '{ProteinDemand} = %s, '
            '{CarbohydratesDemand} = %s, '
            '{FatDemand} = %s, '
            '{VitaminADemand} = %s, '
            '{VitaminB1Demand} = %s, '
            '{VitaminB2Demand} = %s, '
            '{VitaminB6Demand} = %s, '
            '{VitaminB12Demand} = %s, '
            '{VitaminCDemand} = %s, '
            '{VitaminDDemand} = %s, '
            '{VitaminEDemand} = %s, '
            '{VitaminKDemand} = %s '
            'WHERE {ID} = %s'
        ).format(
            Avatar=sql.Identifier("Avatar"),
            Username=sql.Identifier("Username"),
            Sex=sql.Identifier("Sex"),
            Height=sql.Identifier("Height"),
            Weight=sql.Identifier("Weight"),
            Birth=sql.Identifier("Birth"),
            City=sql.Identifier("City"),
            SkinType=sql.Identifier("SkinType"),
            HeatQuantityDemand=sql.Identifier("HeatQuantityDemand"),
            ProteinDemand=sql.Identifier("ProteinDemand"),
            CarbohydratesDemand=sql.Identifier("CarbohydratesDemand"),
            FatDemand=sql.Identifier("FatDemand"),
            VitaminADemand=sql.Identifier("VitaminADemand"),
            VitaminB1Demand=sql.Identifier("VitaminB1Demand"),
            VitaminB2Demand=sql.Identifier("VitaminB2Demand"),
            VitaminB6Demand=sql.Identifier("VitaminB6Demand"),
            VitaminB12Demand=sql.Identifier("VitaminB12Demand"),
            VitaminCDemand=sql.Identifier("VitaminCDemand"),
            VitaminDDemand=sql.Identifier("VitaminDDemand"),
            VitaminEDemand=sql.Identifier("VitaminEDemand"),
            VitaminKDemand=sql.Identifier("VitaminKDemand"),
            ID=sql.Identifier("ID")
        ),(avatar, username, sex, height, weight, birth, city, skintype, heatquantitydemand, proteindemand, carbohydratesdemand, fatdemand, vitaminademand, vitaminb1demand, vitaminb2demand, vitaminb6demand, vitaminb12demand, vitamincdemand, vitaminddemand, vitaminedemand, vitaminkdemand, id)
    )
    conn.commit()

    return returnmsg.success({})