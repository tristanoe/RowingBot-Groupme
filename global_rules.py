import urllib.request, json
from decimal import Decimal

 

def run(data, bot_info, send):
    help_message2 = "April 4th; Wichita: Duel\nApril 26th; Michigan: MACRA\nMay 3rd; Wichita: PACRA\nMay 22-24th; Georgia: ACRA\n\n.flow -> Rowing info"
    help_message = "Announcements\n------------------\nSpring Break;\n    March 6th: 6am & 3pm\n    March 7-11th: 7:30am & 3pm\n\nMarch 18-19th; Ergathon\nMarch 21st; Elections after practice\n\n" + help_message2

    
    message = data['text']

    if message == '.help':
        send(help_message, bot_info[0])
        return True

    if message == '.flow':

        send(getFlow()+getTemp(), bot_info[0])
        return True

    # send("Hi {}! You said: {}".format(data['name'], data['text']), bot_info[0])
    return True

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
    # return sentence_temp
            
    with urllib.request.urlopen("https://openweathermap.org/data/2.5/weather?lat=38.9806&lon=-95.2429&appid=b6907d289e10d714a6e88b30761fae22&units=imperial") as url2:
        data_temp2 = json.loads(url2.read().decode())
        air_temp = str(data_temp2["main"]["temp"]) + " F"
        wind = str(data_temp2["wind"]["speed"]) + " mph"
    sentence_wind = "\nAir Temp:      "+ air_temp + "\nWind Speed: " + wind
    return sentence_temp + sentence_wind
 
