
import pymysql

"""
打开数据库的连接
参数1：主机名
参数2：用户名
参数3：密码
参数4：数据库名称
参数5：字符编码

游标：Cursor Object，代表数据库中的游标，用于指示抓取数据操作的上下文，主要提供执行
     SQL语句，调用存储过程，获取查询结果的方法
callproc:调用存储过程，需要数据支持；
close():关闭当前游标
execute:执行数据库操作，SQL语句或者是数据库的命令

操作数据库流程：
1）建立connect
2）使用cursor获取游标
3）执行SQL语句，处理数据结果
4) 关闭cursor
5) 关闭connect

数据库连接中的方法：
callproc(procname,[,parameters]): 需要存储过程，需要数据库支持
close(): 关闭当前游标
execute(operation[,parameters]): 执行数据库操作，SQL语句或者数据库命令
executemany(operation,seq_of_params): 用于批量操作，如批量更新
fetchone(): 获取查询结果集中的下一条记录
fetchmany(size): 获取指定数量的记录
fetchall(): 获取结构集的所有记录
nextset(): 跳至下一个可用的结果集
"""

"""创建数据库连接"""
db = pymysql.connect("localhost", "root", "123456", "test")

"""使用cursor获取游标"""
cursor = db.cursor()

"""数据列表"""
"""往数据库添加数据"""
data = [("人生苦短用python", "PYTHON", "99.9", "2020-01-01"),
        ("人生苦短用JAVA", "JAVA", "89.9", "2020-02-02"),
        ("人生苦短用PHP", "PHP", "79.9", "2020-03-03"),
        ("人生苦短用JS", "JAVAScript", "69.9", "2020-05-05"),
        ("人生苦短用Ruby", "Ruby", "59.9", "2020-06-06")
        ]

try:
    # 打开数据库的连接
    cursor.executemany("insert into books(name,category,price,publish_time)Values(%s,%s,%s,%s)", data)
    # 提交数据
    db.commit()
except:
    # 发生错误时回调
    db.rollback()
    # 关闭数据库
    db.close()
