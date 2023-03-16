import json
import socket

file = "./TravelPlanSupport-win32-x64/resources/app/nativefier.json"

with open(file) as f:
    di = json.load(f)

print(di['targetUrl'])

ip = socket.gethostbyname(socket.gethostname())

targeturl = 'http://' + ip + ':3000/'
print(targeturl)
di['targetUrl'] = targeturl

with open(file, 'wt') as f:
    json.dump(di, f, indent=2, ensure_ascii=False)
