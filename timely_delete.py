import os
import datetime
now_time = datetime.datetime.now().strptime(datetime.datetime.now().strftime("%Y.%m.%d"),"%Y.%m.%d")
os.system("curl -XGET http://172.18.1.1:9200/_cat/indices > date.txt")

with open("date.txt","r") as f:
    for line in f.readlines():
        index = line.strip().split()[2]

        try:
            index_name = index.split("-")[0];
            if index_name != "wdcrawler":
                continue;
            index_strftime = datetime.datetime.strptime(index.split("-")[-1], "%Y.%m.%d")
            Ca = (now_time - index_strftime)
            if str(Ca).split()[0] == "0:00:00":
                continue
            elif int(str(Ca).split()[0]) >= 1:
                command = "curl -XDELETE http://172.18.1.1:9200/%s" % index
                print(command)
                os.system(command)
            else:
                print(index,"no del")
        except:
            pass
