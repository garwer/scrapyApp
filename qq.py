# -*- coding: utf-8 -*-
from qqbot import QQBotSlot as qqbotslot, RunBot
from qqbot import qqbotsched
import tuling_model.tuling as tuling
import mysql_model.mysqlUtil as mysqlUtil

@qqbotslot
def onQQMessage(bot, contact, member, content): #注意content和contact
    if content == '-hello':
        bot.SendTo(contact, '你好，我是QQ机器人')

    elif content == '在':
        bot.SendTo(contact, '我一直在呢，嘻嘻')

    #如果是好友发送-stop 则关闭机器人
    elif content == '-stop' and contact.ctype == 'buddy':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
    #如果类型为群 buddy/group/discuss ，代表 好友/群/讨论组 对象
    elif contact.ctype == 'group':
        #g1 = bot.List('group','茶景坊')
        g2 = bot.List('group', '上古IOD九大名剑')
        #如果为这个群 且不为自己发的消息
        #当本qq发消息时，qqbot也会收到一条同样的消息【可能是因为手机端pc端不影响】
        # bot.isMe判断是否为自己发的消息
        if not bot.isMe(contact, member) and g2 is not None:
            if '@ME' in content:
                bot.SendTo(contact, member.name + '，艾特我干神马呀？')
            if content.find("鸭子") != -1:
                bot.SendTo(contact, "嘎嘎嘎嘎嘎")
            if content.find("老福") != -1:
                bot.SendTo(contact, "呱呱呱")
            elif content.find("电影") != -1:
                type = 'now'; #默认新电影
                if(content.find("新") != -1):
                    type = "now"
                elif(content.find("将") != -1):
                    type = "will"
                elif(content.find("北美") != -1):
                    type = "usa"
                #以此类推...
                obj = mysqlUtil.DB()
                print(type)
                msg = obj.getTop10(type)
                print(str(msg))
                bot.SendTo(contact, str(msg))
            else:
                #pass
                res = tuling.getMsg(content)
                bot.SendTo(contact, res)


    #定时任务 11:55
    @qqbotsched(hour='11', minute='55')
    def mytask(bot):
        gl = bot.List('group', '上古IOD九大名剑')
        if gl is not None:
            for group in gl:
                bot.SendTo(group, '同志们：开饭啦啦啦啦啦啦！！！吃啥啊!!')


if __name__ == '__main__':
    RunBot()
