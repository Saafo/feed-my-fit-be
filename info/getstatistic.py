# about getstatistic
import time
import userToken
import returnmsg
from psycopg2 import sql

def getstatistic(cur, args):
    id = args.get('id')
    token = args.get('token')
    getall = args.get('getall')
    date = args.get('date')
    #参数完整性验证
    if all([id, token, getall, date]) == False:
        return returnmsg.error('参数不完整', 400)
    
    #先验证token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()

    #根据getall的情况来获取数据
    if getall == "true":
        cur.execute(
            sql.SQL(
                'SELECT * FROM userdata '
                'WHERE {ID} = %s'
            ).format(
                ID=sql.Identifier("ID")
            ),(id,)
        )
    elif getall == "false":
        cur.execute(
            sql.SQL(
                'SELECT * FROM userdata '
                'WHERE {ID} = %s '
                'AND {Date} = %s'
            ).format(
                ID=sql.Identifier("ID"),
                Date=sql.Identifier("Date")
            ),(id, date)
        )
    else:
        return returnmsg.error("getall值异常", 400)

    rows = cur.fetchall()
    #如果是空数据
    if len(rows) == 0:
        return returnmsg.empty("无数据")
    
    data = {}
    for row in rows:
        data_day = {
            "HealthyState": row[2],
            "HealthyScore": row[3],
            "HeatQuantity": row[4],
            "HeatQuantityDiff": row[5],
            "Protein": row[6],
            "ProteinDiff": row[7],
            "Carbohydrates": row[8],
            "CarbohydratesDiff": row[9],
            "Fat": row[10],
            "FatDiff": row[11],
            "VitaminA": row[12],
            "VitaminADiff": row[13],
            "VitaminB1": row[14],
            "VitaminB1Diff": row[15],
            "VitaminB2": row[16],
            "VitaminB2Diff": row[17],
            "VitaminB6": row[18],
            "VitaminB6Diff": row[19],
            "VitaminB12": row[20],
            "VitaminB12Diff": row[21],
            "VitaminC": row[22],
            "VitaminCDiff": row[23],
            "VitaminD": row[24],
            "VitaminDDiff": row[25],
            "VitaminE": row[26],
            "VitaminEDiff": row[27],
            "VitaminK": row[28],
            "VitaminKDiff": row[29]
        }
        data.update({row[1].strftime("%Y-%m-%d"): data_day})
    
    return returnmsg.success(data)