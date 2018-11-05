import time
from datetime import datetime as dt

hosts_temp=r"C:\eclipse\website blocker\hosts\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
websites=["www.web.whatsapp.com","www.facebook.com","www.bpitindia.com"]

while True:
    if not dt(dt.now().year,dt.now().month,dt.now().day,9)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,17):
        print('Working Hours........')
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+""+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print('Fun Hours........')
    time.sleep(5)