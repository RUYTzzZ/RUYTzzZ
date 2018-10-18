import urllib
import urllib2
xh=1534130229   
message ='GET http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_historyList?cardnum=YKT'+str(xh)+'&page=1&pageSize=15 HTTP/1.1\r\ncache: 0\r\nHost: mob.huanghuai.edu.cn\r\n\r\n'

url = message

req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res

