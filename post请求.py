

import json,urllib2
import sys
def printcn(b):         #配置中文输出函数
    sys_encoding = sys.getfilesystemencoding()
    print(b.decode('utf-8').encode(sys_encoding))

   
    reload(sys)

textmod={"queryString": "wlanuserip%3Dd593951046fdf2b7e01aebb894ccd20a%26wlanacname%3De1d02b0c3d387049f7ff525300161b78%26ssid%3D%26nasip%3D92eba309abd5bb83e049c2718596b443%26snmpagentip%3D%26mac%3D58ac09a68f99efb9499545f5eb8ec817%26t%3Dwireless-v2%26url%3D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30%26apmac%3D%26nasid%3De1d02b0c3d387049f7ff525300161b78%26vid%3D89813bf3840fac62%26port%3Db91a72e5d7a78ea8%26nasportid%3D5b9da5b08a53a540cb3c232440f12fc387f024c1e2af8c1c813c693e1f8aa2b8","userId": "s1518339693055","password":"111"}
textmod = json.dumps(textmod)
print(textmod)
header_dict = {'User-Agent': 'Mozilla/5.0',"Content-Type": "application/x-www-form-urlencoded",'Host':'10.100.200.3'}
url='http://10.100.200.3/eportal/InterFace.do?method=login'
req = urllib2.Request(url=url,data=textmod,headers=header_dict)
res = urllib2.urlopen(req)
res = res.read()
printcn(res)
