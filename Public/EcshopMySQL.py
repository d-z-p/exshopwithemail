import pymysql
from Config.EcshopConf import *


class mysql_operation:
    def __init__(self):

        self.db = pymysql.connect(host=sit_db_server,
                                  user=sit_db_user,
                                  passwd=sit_db_password,
                                  port=sit_db_port,
                                  database=sit_db_name)  # 连接数据库，输入 /IP/用户名/密码/数据库名/端口

        self.cur = self.db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor

    def mysql_select(self, user):  # 这个是用来断言的
        self.cur.execute("SELECT user_name FROM `ecs_users`")
        data = self.cur.fetchall()  # fetchall获取所有的数据，以游标方式获取
        for user_test in data:
            if user_test[0] == user:  # test10
                return True
        else:
            return False

    def mysql_inserinto(self):  # 删除以前注册的用户
        self.cur.execute("SELECT user_name FROM `ecs_users`")

        # 使用 fetchone() 方法获取单条数据.fetchall() 是获取全部数据的用户名，以元组存放数据
        data = self.cur.fetchall()
        for user_test in data:
            if user_test[0] == 'test10':
                self.cur.execute("delete FROM `ecs_users` where user_name = 'test10'")

    def mysql_close(self):
        # 关闭数据库连接
        self.db.close()
