import time

timeArray = time.localtime(1613492734.5999568)  # 秒数
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
# 2000-1-1 0:0:0
#转换成时间数组
dt = '2000-1-1 0:0:0'
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(timeArray)

print (timestamp)
print(time.time())
args = {'name':'test'}
data_patch_name=args.get('name',None)
data_patch_psw=args.get('psw',None)
data_patch_sex=args.get('sex',None)
data_patch_rem = args.get('rem',None)
data_patch_photo=args.get('photo',None)
