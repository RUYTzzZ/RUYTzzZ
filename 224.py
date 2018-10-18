import requests




payload = {'cache':'0','Host':'mob.huanghuai.edu.cn','Connection':'Keep-Alive'}
res = requests.get("http://mob.huanghuai.edu.cn/huanghuai/libraryAppointmentOrder_getAppoint?cardnum=YKT1534130211",params=payload)
print(res.content)
