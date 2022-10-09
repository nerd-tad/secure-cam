#reading from firebase
import requests
import pyttsx3
import time
engine_sound = pyttsx3.init()
c = 0
d = 0
url_db = 'https://sec-cam-upgraded-default-rtdb.firebaseio.com/.json'
while 1:
    try:
        data = requests.get(url_db+'?auth=mmQi618DeKAbrV995EwyfiwwefmlvGKCt9xHrnjw')
        data = data.json()['data1']
        #print(data)
        dataList = data['dataLine'].split('_')
        #print(dataList)
        detected_obj = dataList[0]
        t_published = int(dataList[-1])
        t_real = round(time.time())
        dell = t_real - t_published
    except Exception:
        ##MY CONNECTION IS FUCKED,, YOU ASSHOLE.....................
        data = 404
       
    #seperate label and time eg-dog9874758549.099865 is the data format..
    if data == 404: #and c == 0, like that you could simplify wisely the code.....
        #c = 0
        #print('Connection is terrible on this device!!!')
        if c == 0:
            engine_sound.say('the connection is terrible on monitoring device')
            engine_sound.runAndWait()
            c = c + 1
        else:
            continue
            
    else:    #else means no problem in monitoring device..............................it recieves data from the database............................
        if c > 0:   #this is the point where connection is re-established on monitoring device side after the lack of connection.....
            engine_sound.say('connection is re-established on monitering device!')
            time.sleep(1)
            c = 0

        if dell > 30 and d == 0:   #d is to identify the number of times that was identified , there is a problem in connection on secure cam....
            engine_sound.say('connection on secure camera is terrible!')
            engine_sound.runAndWait()
            d = d + 1
			
        if (detected_obj != 'static') and dell <= 25:#if (detected_obj != 'nothing' or detected_obj != 'static') and dell <= 25:
            if d > 0:
                engine_sound.say('connection is re-established on secure cam!')
                engine_sound.runAndWait()
            d = 0
            strr = 'Caution! '+str(detected_obj)+' was detected!.. I repeat, '+str(detected_obj)+' was detected '+str(dell)+' seconds ago!'
            print(strr)
            engine_sound.say(strr)
            engine_sound.runAndWait()
        elif (detected_obj == 'nothing' or detected_obj == 'static') and dell <= 25:
            if d > 0:
                engine_sound.say('connection is re-established on secure cam!')
                engine_sound.runAndWait()
                d = 0
            strr_nothing = 'Nothing was detected!'
            print(strr_nothing)
        elif dell > 30:
            strr_del = 'Connection is terrible on secure cam!'
            print(strr_del)