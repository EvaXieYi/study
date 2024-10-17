import mysql.connector
from mysql.connector import Error
 
def connect_to_mysql(**config):
    try:
        conn = mysql.connector.connect(**config)
        
        if conn.is_connected():
            print("连接成功！")
            # 这里可以添加你的代码来执行数据库操作
            cursor = conn.cursor()
            cursor.execute("select Host,user from mysql.user")
            #query = ("SELECT * FROM mysql.user")
            #cursor.execute(query)
            #for (column1, column2) in cursor:
               # print("{}, {}".format(column1, column2))
            abc=cursor.fetchall()
            print(abc)
            #for (column1, column2) in abc:
            #    print("{}, {}".format(column1, column2))
            cursor.close()
            conn.close()
    except Error as e:
        print("连接失败：", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
 
# 使用示例

connect_to_mysql(host='39.96.41.2',
database='python',
user='root',
password='15600227731Xy.')


a=[('abc','123213'),(123)]
print(a[0])

a={"我":"你","print":"1","1":"1","2":"2"}
del a["我"]
print(a)
a=['1','2','3','4','5']
print(a[0])