import time,sys
'''indent=0
indentIncreasing=True
try:
      while True:
            print('  '*indent,end='')
            print('********')
            time.sleep(0.1)
            if indentIncreasing:
                  indent=indent+1
                  if indent == 20:
                        indentIncreasing = False
            else:
                  indent=indent-1
                  if indent == 0:
                        indentIncreasing=True
except KeyboardInterrupt:
    sys.exit()

'''










index=0
indexname=True
try:
    while False:
      
        print('    '*index,end='')
        print('*******')
        time.sleep(0.1)
        if indexname:
              index=index+1
              if index == 20:
                    indexname=False
        else :
              index=index-1
              if index==0:
                    indexname = True
except KeyboardInterrupt:
      sys.exit()



























index=0
indexname=True
try:
     while False:
        print('  '*index,end="")
        print("########")
        time.sleep(0.1)
        if indexname:
            index=index+1
            if index==20:
                indexname=False
        else:
            index=index-1
            if index==0:
                 indexname=True



except KeyboardInterrupt:
       sys.exit()
print(time.time()) #从1970年1月1日到当前时间相隔多少秒
print(int(time.mktime(time.localtime()))) #将时间元组转化为时间戳 
print(time.localtime())#将本地时间转化为时间元组
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) #将本地时间元组转化为特定的日期格式
print(time.asctime(time.localtime())) #将本地时间转化为英文标识
print(time.strptime("2022-10-11 22:23:10","%Y-%m-%d %H:%M:%S"))  #时间元组

print(time.struct_time)
import datetime
#datetime.datetime类
# 分别返回年月日
# 2023
print(datetime.datetime.now().year)
# 1
print(datetime.datetime.now().month)
# 5
print(datetime.datetime.now().day)

# 借助date()函数将日期和时间设置成只展示日期
# 2023-01-05
print(datetime.datetime.now().date())
# 借助time()函数将日期和时间设置成只展示日期
# 21:00:51.695680
print(datetime.datetime.now().time())
# 借助strftime()函数自定义日期和时间
# 2023-01-05
print(datetime.datetime.now().strftime('%Y-%m-%d'))
# 借助strftime()函数自定义日期和时间
# 2023-01-05 21:00:51
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#常见场景
#时间格式转时间戳
# 昨天的时间戳 1672761600
print(int(time.mktime(time.strptime(str(datetime.date.today() - datetime.timedelta(days=1)), '%Y-%m-%d'))))

# 指定时间的时间戳  1672920000
print(int(time.mktime(datetime.datetime.strptime("2023/01/05 20:00", "%Y/%m/%d %H:%M").timetuple())))

# 转换函数
def string2timestamp(strValue):
    try:        
        d = datetime.datetime.strptime(strValue, "%Y-%m-%d %H:%M:%S.%f")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond))/1000000
        print(timeStamp)
        return timeStamp
    except ValueError as e:
        print(e)
        d = datetime.datetime.strptime(str2, "%Y-%m-%d %H:%M:%S")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        timeStamp = float(str(timeStamp) + str("%06d" % d.microsecond))/1000000
        print(timeStamp)
        return timeStamp

#时间戳转日期格式
# 将时间戳转化为时间元组 
# time.struct_time(tm_year=2023, tm_mon=1, tm_mday=5, tm_hour=20, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=5, tm_isdst=0)
print(time.localtime(1672920000))

# 转换函数
def timestamp2string(timeStamp):
    try:
        d = datetime.datetime.fromtimestamp(timeStamp)
        str1 = d.strftime("%Y%m%d%H%M")
        # 2015-08-28 16:43
        return str1
    except Exception as e:
        print(e)
        return ''
#时间偏移
from datetime import datetime, timedelta

date = datetime.today()

#往后推一天
print(date+timedelta(days=1))
#往后推60秒
print(date+timedelta(seconds=60))
#往前推一天
print(date-timedelta(days=1))
#往前推60秒
print(date-timedelta(seconds=60))
'''时间格式
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
