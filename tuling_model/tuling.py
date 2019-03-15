import requests
import traceback

apiKey = "af2979582c864c7ab7865ca721a6baed"
userid = "641084049"

#通过msg获取回复消息
def getMsg(msg):
    apiUrl = "http://www.tuling123.com/openapi/api"
    params = {
        "key": apiKey,#申请到的本接口专用的apiKey
        "info": msg, #要发送给机器人的内容，不要超过30个字符
        "userid": userid   #自定义唯一 userid（1-32位，字母与数字组成）,可以识别上下文，比如说我多次发送你好吗，机器人会回复"你好像个复读机呀"之类的信息
    }

    try:
        res = requests.post(apiUrl, data=params).json()
        print(res)
        return res.get('text')
    except Exception:
        #打印异常信息
        print("接口调用异常" + traceback.print_exc())
        return


#测试
getMsg("你好吗")
