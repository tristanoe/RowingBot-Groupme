import urllib.request, json
from decimal import Decimal
#import clock
 

def run(data, bot_info, send):
    help_message = "\n\n.flow -> Rowing info\n.compass -> Compass"
    exec_message = "Exec Board 2020-2021\n------------------\nPresident: Chris Hardin\nVice President: Justin Spurling\nMens Captain: Grant Gollier\nWomens Captain: Carolyn Hassett\nCoxswain Captain: Brent Linneman*\nTresurer: Zach Hardin\nSecretary: Jack Campbell\nPR/Alumni Rep: Noah Johnson\nRecruitment Chair: Jimmy Dorlac\n\n"

    #image = data['image']
    message = data['text']

    if message == '.exec':
        send(exec_message, bot_info[0])
        return True
        
    if message == '.help':
        send(help_message, bot_info[0])
        return True
        
    if message == '.flow':
        send(getFlow() + getTemp(), bot_info[0]) # getTemp()2 was removed.
        return True

    if message == '.compass':
        send("http://snowfence.umn.edu/Images/Wind/wind_bln1.gif", bot_info[0])
        return True
 
    if message[:1] == '.':
        if data['name'] == 'Zach Hardin':
            send("Is Zach making up commands again? smh", bot_info[0])
            return True
        else:
            send("{} isn't a command, sorry {}".format(data['text'], data['name']), bot_info[0])
            return True
   # send(message[1:], bot_info[0])
   # send(message[:1], bot_info[0])
   # send(data['name'], bot_info[0])
   # return True

def getFlow():
   # global flow_lcn, flow_lfk
    with urllib.request.urlopen("https://waterservices.usgs.gov/nwis/iv/?&sites=06891000&parameterCd=00060&format=json") as url:
        data_lcn = json.loads(url.read().decode())
        flow_lcn = data_lcn["value"]["timeSeries"][0]["values"][0]["value"][0]["value"]
        sentence_lcn = "Lecompton: "+ flow_lcn
        # print(sentence_lcn)

    with urllib.request.urlopen( "https://waterservices.usgs.gov/nwis/iv/?&sites=06891080&parameterCd=00060&format=json") as url2:
        data_lfk = json.loads(url2.read().decode())
        flow_lfk = data_lfk["value"]["timeSeries"][0]["values"][0]["value"][0]["value"]
        sentence_lfk = "Lawrence: "+ flow_lfk + ", "
        # print(sentence_lfk)
    final = sentence_lfk + sentence_lcn+"\nAverage: "
    return final+str(int((int(flow_lcn) + int(flow_lfk))/2))
    # return flow_lcn, flow_lfk
    
def getTemp():
    with urllib.request.urlopen("https://waterservices.usgs.gov/nwis/iv/?&sites=06892350&parameterCd=00010&format=json") as url:
        data_temp = json.loads(url.read().decode())
        water_temp = data_temp["value"]["timeSeries"][0]["values"][1]["value"][0]["value"]
        Decimal_water = Decimal(water_temp)
        final_water = (Decimal_water * 9/5 ) + 32
        
    sentence_temp = "\nWater Temp: " + str(final_water) + " F"
    return sentence_temp
def getTemp2():
    with urllib.request.urlopen("https://openweathermap.org/data/2.5/weather?lat=38.9806&lon=-95.2429&appid=b6907d289e10d714a6e88b30761fae22&units=imperial") as url2:
        data_temp2 = json.loads(url2.read().decode())
        air_temp = str(data_temp2["main"]["temp"]) + " F"
        wind = str(data_temp2["wind"]["speed"]) + "mph"
        deg_wind = data_temp2["wind"]["deg"]
        
        if deg_wind < 11.25 or deg_wind > 248.75:
            direction = " N"
        elif deg_wind > 11.25 and deg_wind < 33.75:
            direction = " NNE"
        elif deg_wind > 33.75 and deg_wind < 56.25:
            direction = " NE"
        elif deg_wind > 56.25 and deg_wind < 78.75:
            direction = " ENE"
        elif deg_wind > 78.75 and deg_wind < 101.25:
            direction = " E"
        elif deg_wind > 101.25 and deg_wind < 123.75:
            direction = " ESE"
        elif deg_wind > 123.75 and deg_wind < 146.25:
            direction = " SE"
        elif deg_wind > 146.25 and deg_wind < 168.75:
            direction = " SSE"
        elif deg_wind > 168.75 and deg_wind < 191.25:
            direction = " S"
  
        elif deg_wind > 191.25 and deg_wind < 213.75:
            direction = " SSW"
        elif deg_wind > 213.75 and deg_wind < 236.25:
            direction = " SW"
        elif deg_wind > 236.25 and deg_wind < 258.75:
            direction = " WSW"
        elif deg_wind > 258.75 and deg_wind < 281.25:
            direction = " W"
        elif deg_wind > 281.25 and deg_wind < 303.75:
            direction = " WNW"
        elif deg_wind > 303.75 and deg_wind < 326.25:
            direction = " NW"
        elif deg_wind > 326.25 and deg_wind < 348.75:
            direction = " NNW"
        else:
            direction = str(deg_wind) + " degrees"

        
    sentence_wind = "\nAir Temp:      "+ air_temp + "\nWind Speed: " + wind + direction + " (" + str(deg_wind) + ")"
    return sentence_temp + sentence_wind
 
