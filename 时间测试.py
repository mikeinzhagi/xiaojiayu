import datetime
import time
# starttime = datetime.datetime.now()
# time.sleep(3)
# # long running
# endtime = datetime.datetime.now()
# times = (endtime - starttime).seconds
# print (times)

# 使用datetime.now()
now = datetime.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# second = now.second

# print("现在时间是", year, "年", month, "月", day,
#       "日", hour, "点", minute, "分", second, "秒",sep="")

print(now.strftime("今天是:%Y年%m月%d日 %H:%M:%S"))
