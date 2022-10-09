#read from bridgeTxt and post into firebase.. along data send the time also....
import time
import requests

file1 = 'bridgeTxt.txt'
list1 = []
#url = https://console.firebase.google.com/project/sec-cam-upgraded/database/sec-cam-upgraded-default-rtdb/data/dataLine
url_db = 'https://sec-cam-upgraded-default-rtdb.firebaseio.com/.json'
while 1:
    time.sleep(1)
	
    with open(file1, 'r') as fh:
        list1 = fh.read().splitlines()
	
    data_line = list1[-1]
    data_line_post = {'data1':{'dataLine':data_line}}
    #print('fuck', data_line_post)
    try:
        pub_var = requests.patch(url=url_db, json=data_line_post, timeout=7)
    except Exception:
        continue
    #pub_var = requests.patch(url=url_db, json=data_line_post)
    stat_str = 'static'
    t_stat = round(time.time())
    if len(list1) > 10:
        with open(file1, 'w') as fh:
            fh.write(stat_str+'_'+str(t_stat))
	