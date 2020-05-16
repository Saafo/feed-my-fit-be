# FeedMyFit 后台接口文档

若无特殊说明，请求和返回数据都是json

*   Domain: https://*

---

## 返回数据示例：

```jsonc
{
  "errorCode": 0,
  "errorMsg": "ok",
  "data":{}
}
```

## 错误代码

*   0 表示正常工作
*   -1 empty
*   -2 error
*   -3 token过期，重新登录
*   -4 非法url

返回数据在data里，也是一个json
以下**返回数据**的说明**只针对data内**的部分

---

## 用户部分

### 用户注册

HTTP Method: Get

Url:/user/register

Request:

```url
phonenum=12345678901&key=ed5ab7d5ac405659ed24e37bb89877c5
```

此处key由本地AES加密，秘钥私下给出。

Return:

```jsonc
{
  "Id": "xxxxxxxx",
  "Token": "xxxxxxxxxx",
  "Needinfo": "True" //没信息则True。有信息则False，不需要再填个人信息。
}
```

### 用户登录

HTTP Method: Get

Url:/user/login

Request:

```url
phonenum=12345678901&key=ed5ab7d5ac405659ed24e37bb89877c5
```

Return:

```jsonc
{
  "Id": "xxxxxxxx",
  "Token": "xxxxxxxxx",
  "Needinfo": "True" //可能上次注册流程没走完，则为False，需要继续填写信息
}
```

### Token更新，每次打开软件的时候进行

HTTP Method: Get

Url: /user/updatetoken

Request:

```url
id=xxxxxxx&token=xxxxxxx
```

Response:

```jsonc
{
  "Token": "zzzzzzzz" //新Token，用于替换旧Token
}
```

### 获取个人信息

HTTP Method: Get

Url:/user/getselfinfo

Request:

```url
id=xxxxxxx&token=xxxxxxx
```

Return:

```jsonc
{
  "PhoneNum": "12345678901",
  "Avatar": "xxxxxxxxxx", //七牛云url
  "Username": "Feed!",
  "Sex": "Male", //or Female or Secret
  "Height": "170.5",
  "Weight": "65.5",
  "Birth": "2000-01-01", //格式我还不敢完全确定，但差不多就是这样
  "City": "成都",
  "SkinType": "1",
  "HeatQuantityDemand": "100",
  "ProteinDemand": "100",
  "CarbohydratesDemand": "100", //糖类
  "FatDemand": "100",
  "VitaminADemand": "100",
  "VitaminB1Demand": "100",
  "VitaminB2Demand": "100",
  "VitaminB6Demand": "100",
  "VitaminB12Demand": "100",
  "VitaminCDemand": "100",
  "VitaminDDemand": "100",
  "VitaminEDemand": "100",
  "VitaminKDemand": "100",
  "Streak": 2
}
```

`*Demand`：需求量

### 获取用户公众信息

HTTP Method: Get

Url: /user/getpublicinfo

Request:

```url
id=xxxxxxx&token=xxxxxxx&getid=zzzzzz //Getid为需要获取的用户id
```

Response:

```jsonc
{
  "Id": "zzzzzz",
  "Avatar": "xxxxxxxxx", //七牛云url
  "Username": "Feed@",
  "Sex": "Male",
  "City": "成都",
  "Streak": 2
}
```

### 更新个人信息

HTTP Method: Post

Url:/user/updatedata

Request:

```jsonc
{
  "Id": "xxxxxxx",
  "Token": "xxxxxxxxxx",
  "UserData": {
    "Avatar": "1",
    "Username": "Feed!",
    "Sex": "Male",
    "Height": "170.5",
    "Weight": "65.5",
    "Birth": "2000-01-01",
    "City": "成都",
    "SkinType": "1",
    "HeatQuantityDemand": "100",
    "ProteinDemand": "100",
    "CarbohydratesDemand": "100", //糖类
    "FatDemand": "100",
    "VitaminADemand": "100",
    "VitaminB1Demand": "100",
    "VitaminB2Demand": "100",
    "VitaminB6Demand": "100",
    "VitaminB12Demand": "100",
    "VitaminCDemand": "100",
    "VitaminDDemand": "100",
    "VitaminEDemand": "100",
    "VitaminKDemand": "100",
    "Streak": 2
  }
}
```

Response:

```jsonc
//空data
```

### 获取历史数据

HTTP Method: Get

Url:/info/getstatistic

Request:

```url
id=xxxxxxxx&token=xxxxxxx&getall=true&date=none
//或者
id=xxxxxxxx&token=xxxxxxx&getall=false&date=20200401
```

Return:

```jsonc
{
  "2020-04-01": {
    "HealthyState": "健康",
    "HealthyScore": "97",
    "HeatQuantity": "100",
    "HeatQuantityDiff": "10",
    "Protein": "100",
    "ProteinDiff": "10",
    "Carbohydrates": "100",
    "CarbohydratesDiff": "10",
    "Fat": "100",
    "FatDiff": "10",
    "VitaminA": "100",
    "VitaminADiff": "10",
    "VitaminB1": "100",
    "VitaminB1Diff": "10",
    "VitaminB2": "100",
    "VitaminB2Diff": "10",
    "VitaminB6": "100",
    "VitaminB6Diff": "10",
    "VitaminB12": "100",
    "VitaminB12Diff": "10",
    "VitaminC": "100",
    "VitaminCDiff": "10",
    "VitaminD": "100",
    "VitaminDDiff": "10",
    "VitaminE": "100",
    "VitaminEDiff": "10",
    "VitaminK": "100",
    "VitaminKDiff": "10"
  }
}
```

**以上只是返回一天的数据，如果请求里`getall`是`true`的话，可能会返回多天的数据，`key`即是日期。

### 更新数据

HTTP Method: Post

Url:/info/poststatistic

Request:

```jsonc
{
  "Id": "xxxxxxx",
  "Token": "xxxxxxxxxx",
  "UserStatistic": {
    "Date": "2020-04-01",
    "HealthyState": "亚健康",
    "HealthyScore": "97",
    "HeatQuantity": "100",
    "HeatQuantityDiff": "10",
    "Protein": "100",
    "ProteinDiff": "10",
    "Carbohydrates": "100",
    "CarbohydratesDiff": "10",
    "Fat": "100",
    "FatDiff": "10",
    "VitaminA": "100",
    "VitaminADiff": "10",
    "VitaminB1": "100",
    "VitaminB1Diff": "10",
    "VitaminB2": "100",
    "VitaminB2Diff": "10",
    "VitaminB6": "100",
    "VitaminB6Diff": "10",
    "VitaminB12": "100",
    "VitaminB12Diff": "10",
    "VitaminC": "100",
    "VitaminCDiff": "10",
    "VitaminD": "100",
    "VitaminDDiff": "10",
    "VitaminE": "100",
    "VitaminEDiff": "10",
    "VitaminK": "100",
    "VitaminKDiff": "10"
  }
}
```

这里应该POST每天的累计量，服务器只做存储，不做累计工作。

Return:

```jsonc
//空data
```

---

## 朋友圈部分

### 获取`id为xxxx用户`或者`全体用户`的所有MomentsID

HTTP Method: Get

Url: /moments/getmomentsid

Request:

```url
id=xxxxxxxx&token=xxxxxxx&getall=true&getid=none
//或者
id=xxxxxxxx&token=xxxxxxx&getall=false&getid=xxxx
```

Response:

```jsonc
{
  "MomentsIds": ["id1xxxxx", "id2xxxxxxx", "id3xxxxxxx"]
} //按时间顺序从新到旧
```

### 获取单条动态内容

HTTP Method: Get

Url: /moments/getmoment

Request:

```url
id=xxxxxxx&token=xxxxxxx&momentid=id1xxxxxx //Id为本用户id
```

Response:

```jsonc
{
  "MomentID": "id1xxxxxx",
  "Id": "xxxxxxxx", //发这条moment用户的id
  "Time": "Fri, 15 May 2020 03:00:00 GMT",
  "Text": "dgsgsgsdgasf sdff faf fa 啦啦啦啦测试内容",
  "Pic": "xxxxxxxxxxxxxxx", //url
  "Thumbs": "233",
  "Username": "啦啦啦",
  "Avatar": "xxxxxxxxxx", //用户头像链接
  "Streak": 4, //该用户坚持天数
  "Comments": { //因为是json，所以可能乱序，但commentid有规律，越大越新
    "1232131": { //CommentID
      "Id": "xxxxxxxx", //发送该条评论的用户id
      "Username": "啦啦啦",
      "Text": "哈哈哈哈昂xswl",
		  "Time": "Fri, 15 May 2020 03:00:00 GMT"
    },
    "2342341": {
      "Id": "xxxxxxxx",
      "Username": "这TM是来捣乱的是吧",
      "Text": "233333333"
		  "Time": "Fri, 15 May 2020 03:00:00 GMT"
    }
  }
}
```

### 点赞

HTTP Method: Get
Url: /moments/thumbup

Request:

```url
id=xxxxxxx&token=xxxxxxx&momentid=id1xxxxxx
```

Response:

```jsonc
//无data
```

### 发Moments

HTTP Method: POST

Url: /moments/postmoment

Request:

```jsonc
{
  "Id": "xxxxxxxx",
  "Token": "xxxxxxx",
  "Text": "这是一条测试文案",
  "Pic": "xxxxxxxxxxxx", //七牛云返回的图片url链接
}
```

Response:

```jsonc
{
  "MomentID": "xxxxx"
}
```

### 评论

HTTP Method: Post

Url: /moments/postcomment

Request:

```jsonc
{
  "Id": "xxxxxxx",
  "Token": "xxxxxxxxx",
  "MomentID": "id1xxxxxx",
  "Text": "哈哈哈哈笑死我了",
}
```

Response:

```jsonc
{
  "CommentID": "cxxxxxxxxxx"
}
```



---

## 排行榜部分

### 每日健康值排行榜

HTTP Method: GET

Url: /rank/dailyscore

Request:

```url
id=xxxxxxx&token=xxxxxxx
```

Response:

```jsonc
{
  "Ids": ["id1xxxxx", "id2xxxxxxx", "id3xxxxxxx"],
  "Usernames":["啦啦啦", "哈哈哈", "呱呱呱"],
  "Avatars": ["https://pixiv/114514", "1", "2"],
  "HealthyScores": [99, 98, 93]
} //从高到低排列,最多50个
```

### 连击排行榜

HTTP Method: GET

Url: /rank/streak

Request:

```url
id=xxxxxxx&token=xxxxxxx
```

Response:

```jsonc
{
  "Ids": ["id1xxxxx", "id2xxxxxxx", "id3xxxxxxx"],
  "Usernames":["啦啦啦", "哈哈哈", "呱呱呱"],
  "Avatars": ["https://pixiv/114514", "1", "2"],
  "Streak": [7, 3, 0]
} //从高到低排列,最多50个
```

---

## 数据库结构

### userinfo table

| Key                 | Type    | Length | more   |
| ------------------- | ------- | ------ | ------ |
| ID                  | Serial  |        | PK, NN |
| Token               | char    | 32     | NN     |
| AppleID             | varchar | 64     |        |
| WechatID            | varchar | 32     |        |
| PhoneNum            | varchar    | 16     | NN     |
| Avatar              | varchar | 128    |        |
| Username            | varchar | 20     |        |
| Sex                 | varchar    | 9      |        |
| Height              | varchar    | 5      |        |
| Weight              | varchar    | 5      |        |
| Birth               | date    |        |        |
| City                | varchar | 20     |        |
| SkinType            | varchar    | 5      |        |
| HeatQuantityDemand  | varchar    | 8      |        |
| ProteinDemand       | varchar    | 8      |        |
| CarbohydratesDemand | varchar    | 8      |        |
| FatDemand           | varchar    | 8      |        |
| VitaminADemand      | varchar    | 8      |        |
| VitaminB1Demand     | varchar    | 8      |        |
| VitaminB2Demand     | varchar    | 8      |        |
| VitaminB6Demand     | varchar    | 8      |        |
| VitaminB12Demand    | varchar    | 8      |        |
| VitaminCDemand      | varchar    | 8      |        |
| VitaminDDemand      | varchar    | 8      |        |
| VitaminEDemand      | varchar    | 8      |        |
| VitaminKDemand      | varchar    | 8      |        |
| Streak | integer |  | |



### userdata table

| key               | type   | length | more               |
| ----------------- | ------ | ------ | ------------------ |
| ID                | Serial |        | PK,FK              |
| Date              | date   |        | PK                 |
| HealthyState      | varchar   | 15     | 健康，肥胖，亚健康 |
| HealthyScore | int | 4 |  |
| HeatQuantity      | varchar  |  8     |                    |
| HeatQuantityDiff  | varchar  |  8     |                    |
| Protein           | varchar  |  8     |                    |
| ProteinDiff       | varchar  |  8     |                    |
| Carbohydrates     | varchar  |  8     | (糖类)             |
| CarbohydratesDiff | varchar  |  8     |                    |
| Fat               | varchar  |  8     |                    |
| FatDiff           | varchar  |  8     |                    |
| VitaminA          | varchar  |  8     |                    |
| VitaminADiff      | varchar  |  8     |                    |
| VitaminB1         | varchar  |  8     |                    |
| VitaminB1Diff     | varchar  |  8     |                    |
| VitaminB2         | varchar  |  8     |                    |
| VitaminB2Diff     | varchar  |  8     |                    |
| VitaminB6         | varchar  |  8     |                    |
| VitaminB6Diff     | varchar  |  8     |                    |
| VitaminB12        | varchar  |  8     |                    |
| VitaminB12Diff    | varchar  |  8     |                    |
| VitaminC          | varchar  |  8     |                    |
| VitaminCDiff      | varchar  |  8     |                    |
| VitaminD          | varchar  |  8     |                    |
| VitaminDDiff      | varchar  |  8     |                    |
| VitaminE          | varchar  |  8     |                    |
| VitaminEDiff      | varchar  |  8     |                    |
| VitaminK          | varchar  |  8     |                    |
| VitaminKDiff      | varchar  |  8     |                    |



### moments table

| key      | type      | length | more |
| -------- | --------- | ------ | ---- |
| ID       | Serial4   |        | FK   |
| MomentID | Serial8   |        | PK   |
| Time     | Timestamp |        |      |
| Text     | varchar   | 256    |      |
| Pic      | varchar   | 512    |      |
| Thumbs   | int       | 8      |      |



### comments table

| key       | type      | length | more |
| --------- | --------- | ------ | ---- |
| MomentID  | Serial8   |        | FK   |
| CommentID | Serial8   |        | PK   |
| ID        | Serial4   |        | FK   |
| Time      | Timestamp |        |      |
| Text      | varchar   | 256    |      |

