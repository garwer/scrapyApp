import pymysql as mysql
import config

class DB():
    def __init__(self):
        cfg = config.mysql
        print(cfg['charset'])
        conn = mysql.connect(host= cfg['host'],
                             port = cfg['port'],
                             user = cfg['user'],
                             passwd = cfg['passwd'],
                             db = cfg['db'],
                             charset = cfg['charset'])
        self.conn = conn
    def getCon(self):
        return self.conn

    def switchType(argument):
        switcher = {
            'now': "热映口碑榜",
            'top100': "TOP100榜",
            "cn": "国内票房榜",
            'usa': "北美票房榜",
            "will": "最受期待榜"
        }
        return switcher.get(argument, "nothing")

    #获取最近热门top10
    def getTop10(self, type):
        # 创建游标
        cursor = self.conn.cursor()
        rows = []
        # 执行sql 并返回受影响的行数
        switcher = {
            'now': "热映口碑榜",
            'top100': "TOP100榜",
            "cn": "国内票房榜",
            'usa': "北美票房榜",
            "will": "最受期待榜"
        }

        flag = switcher.get(type, "nothing")
        sql = 'select top, movie_title, movie_star,releasetime from maoyan_movie t where t.movie_type =  "'+flag+'" order by top'
        print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            title = str(row[0]) + ':' + str(row[1]) + ',' + str(row[2]) + ',' + str(row[3])
            rows.append(title)
        print(rows)
        self.conn.close()
        return rows


#DB().getTop10('top100');

