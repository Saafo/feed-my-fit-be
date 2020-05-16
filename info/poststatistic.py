# about poststatistic
import userToken
import returnmsg
from psycopg2 import sql

def poststatistic(cur, conn, json):
    #先解析json
    try:
        id = json['Id']
        token = json['Token']
        user_statistic = json['UserStatistic']
    #参数完整性验证
    except KeyError:
        return returnmsg.error('参数不完整', 400)
    
    #验证Token是否合法
    if userToken.testToken(cur, id, token) == False:
        return returnmsg.tokeninvalid()
    
    #user_staticstic完整性验证
    try:
        date = user_statistic['Date']
        healthystate = user_statistic['HealthyState']
        healthyscore = user_statistic['HealthyScore']
        heatquantity = user_statistic['HeatQuantity']
        heatquantitydiff = user_statistic['HeatQuantityDiff']
        protein = user_statistic['Protein']
        proteindiff = user_statistic['ProteinDiff']
        carbohydrates = user_statistic['Carbohydrates']
        carbohydratesdiff = user_statistic['CarbohydratesDiff']
        fat = user_statistic['Fat']
        fatdiff = user_statistic['FatDiff']
        vitamina = user_statistic['VitaminA']
        vitaminadiff = user_statistic['VitaminADiff']
        vitaminb1 = user_statistic['VitaminB1']
        vitaminb1diff = user_statistic['VitaminB1Diff']
        vitaminb2 = user_statistic['VitaminB2']
        vitaminb2diff = user_statistic['VitaminB2Diff']
        vitaminb6 = user_statistic['VitaminB6']
        vitaminb6diff = user_statistic['VitaminB6Diff']
        vitaminb12 = user_statistic['VitaminB12']
        vitaminb12diff = user_statistic['VitaminB12Diff']
        vitaminc = user_statistic['VitaminC']
        vitamincdiff = user_statistic['VitaminCDiff']
        vitamind = user_statistic['VitaminD']
        vitaminddiff = user_statistic['VitaminDDiff']
        vitamine = user_statistic['VitaminE']
        vitaminediff = user_statistic['VitaminEDiff']
        vitamink = user_statistic['VitaminK']
        vitaminkdiff = user_statistic['VitaminKDiff']
    except KeyError:
        return returnmsg.error('UserStatistic参数不完整', 400)
    
    #将数据更新到表里
    #判断日期是否存在，存在则更新，不存在则新建
    cur.execute(
        sql.SQL(
            'SELECT {ID} FROM userdata '
            'WHERE {ID} = %s '
            'AND {Date} = %s'
        ).format(
            ID=sql.Identifier("ID"),
            Date=sql.Identifier("Date")
        ),(id, date)
    )
    #数据不存在
    if cur.fetchone() == None:
        cur.execute(
            sql.SQL(
                'INSERT INTO userdata '
                '({ID}, {Date}, {HealthyState}, {HealthyScore}, {HeatQuantity}, {HeatQuantityDiff}, {Protein}, {ProteinDiff}, {Carbohydrates}, {CarbohydratesDiff}, {Fat}, {FatDiff}, {VitaminA}, {VitaminADiff}, {VitaminB1}, {VitaminB1Diff}, {VitaminB2}, {VitaminB2Diff}, {VitaminB6}, {VitaminB6Diff}, {VitaminB12}, {VitaminB12Diff}, {VitaminC}, {VitaminCDiff}, {VitaminD}, {VitaminDDiff}, {VitaminE}, {VitaminEDiff}, {VitaminK}, {VitaminKDiff}) '
                'VALUES '
                '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            ).format(
                ID=sql.Identifier("ID"),
                Date=sql.Identifier("Date"),
                HealthyState=sql.Identifier("HealthyState"),
                HealthyScore=sql.Identifier("HealthyScore"),
                HeatQuantity=sql.Identifier("HeatQuantity"),
                HeatQuantityDiff=sql.Identifier("HeatQuantityDiff"),
                Protein=sql.Identifier("Protein"),
                ProteinDiff=sql.Identifier("ProteinDiff"),
                Carbohydrates=sql.Identifier("Carbohydrates"),
                CarbohydratesDiff=sql.Identifier("CarbohydratesDiff"),
                Fat=sql.Identifier("Fat"),
                FatDiff=sql.Identifier("FatDiff"),
                VitaminA=sql.Identifier("VitaminA"),
                VitaminADiff=sql.Identifier("VitaminADiff"),
                VitaminB1=sql.Identifier("VitaminB1"),
                VitaminB1Diff=sql.Identifier("VitaminB1Diff"),
                VitaminB2=sql.Identifier("VitaminB2"),
                VitaminB2Diff=sql.Identifier("VitaminB2Diff"),
                VitaminB6=sql.Identifier("VitaminB6"),
                VitaminB6Diff=sql.Identifier("VitaminB6Diff"),
                VitaminB12=sql.Identifier("VitaminB12"),
                VitaminB12Diff=sql.Identifier("VitaminB12Diff"),
                VitaminC=sql.Identifier("VitaminC"),
                VitaminCDiff=sql.Identifier("VitaminCDiff"),
                VitaminD=sql.Identifier("VitaminD"),
                VitaminDDiff=sql.Identifier("VitaminDDiff"),
                VitaminE=sql.Identifier("VitaminE"),
                VitaminEDiff=sql.Identifier("VitaminEDiff"),
                VitaminK=sql.Identifier("VitaminK"),
                VitaminKDiff=sql.Identifier("VitaminKDiff")
            ),(id, date, healthystate, healthyscore, heatquantity, heatquantitydiff, protein, proteindiff, carbohydrates, carbohydratesdiff, fat, fatdiff, vitamina, vitaminadiff, vitaminb1, vitaminb1diff, vitaminb2, vitaminb2diff, vitaminb6, vitaminb6diff, vitaminb12, vitaminb12diff, vitaminc, vitamincdiff, vitamind, vitaminddiff, vitamine, vitaminediff, vitamink, vitaminkdiff)
        )
    #数据存在，更新数据
    else:
        cur.execute(
            sql.SQL(
                'UPDATE userdata '
                'SET {HealthyState} = %s, '
                '{HealthyScore} = %s, '
                '{HeatQuantity} = %s, '
                '{HeatQuantityDiff} = %s, '
                '{Protein} = %s, '
                '{ProteinDiff} = %s, '
                '{Carbohydrates} = %s, '
                '{CarbohydratesDiff} = %s, '
                '{Fat} = %s, '
                '{FatDiff} = %s, '
                '{VitaminA} = %s, '
                '{VitaminADiff} = %s, '
                '{VitaminB1} = %s, '
                '{VitaminB1Diff} = %s, '
                '{VitaminB2} = %s, '
                '{VitaminB2Diff} = %s, '
                '{VitaminB6} = %s, '
                '{VitaminB6Diff} = %s, '
                '{VitaminB12} = %s, '
                '{VitaminB12Diff} = %s, '
                '{VitaminC} = %s, '
                '{VitaminCDiff} = %s, '
                '{VitaminD} = %s, '
                '{VitaminDDiff} = %s, '
                '{VitaminE} = %s, '
                '{VitaminEDiff} = %s, '
                '{VitaminK} = %s, '
                '{VitaminKDiff} = %s '
                'WHERE {ID} = %s '
                'AND {Date} = %s'
            ).format(
                HealthyState=sql.Identifier("HealthyState"),
                HealthyScore=sql.Identifier("HealthyScore"),
                HeatQuantity=sql.Identifier("HeatQuantity"),
                HeatQuantityDiff=sql.Identifier("HeatQuantityDiff"),
                Protein=sql.Identifier("Protein"),
                ProteinDiff=sql.Identifier("ProteinDiff"),
                Carbohydrates=sql.Identifier("Carbohydrates"),
                CarbohydratesDiff=sql.Identifier("CarbohydratesDiff"),
                Fat=sql.Identifier("Fat"),
                FatDiff=sql.Identifier("FatDiff"),
                VitaminA=sql.Identifier("VitaminA"),
                VitaminADiff=sql.Identifier("VitaminADiff"),
                VitaminB1=sql.Identifier("VitaminB1"),
                VitaminB1Diff=sql.Identifier("VitaminB1Diff"),
                VitaminB2=sql.Identifier("VitaminB2"),
                VitaminB2Diff=sql.Identifier("VitaminB2Diff"),
                VitaminB6=sql.Identifier("VitaminB6"),
                VitaminB6Diff=sql.Identifier("VitaminB6Diff"),
                VitaminB12=sql.Identifier("VitaminB12"),
                VitaminB12Diff=sql.Identifier("VitaminB12Diff"),
                VitaminC=sql.Identifier("VitaminC"),
                VitaminCDiff=sql.Identifier("VitaminCDiff"),
                VitaminD=sql.Identifier("VitaminD"),
                VitaminDDiff=sql.Identifier("VitaminDDiff"),
                VitaminE=sql.Identifier("VitaminE"),
                VitaminEDiff=sql.Identifier("VitaminEDiff"),
                VitaminK=sql.Identifier("VitaminK"),
                VitaminKDiff=sql.Identifier("VitaminKDiff"),
                ID=sql.Identifier("ID"),
                Date=sql.Identifier("Date")
            ),(healthystate, healthyscore, heatquantity, heatquantitydiff, protein, proteindiff, carbohydrates, carbohydratesdiff, fat, fatdiff, vitamina, vitaminadiff, vitaminb1, vitaminb1diff, vitaminb2, vitaminb2diff, vitaminb6, vitaminb6diff, vitaminb12, vitaminb12diff, vitaminc, vitamincdiff, vitamind, vitaminddiff, vitamine, vitaminediff, vitamink, vitaminkdiff, id, date)
        )
    conn.commit()
    return returnmsg.success({})