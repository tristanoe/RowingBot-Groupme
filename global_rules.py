import urllib.request, json

def run(data, bot_info, send):

    help_message = "//// Announcements ////\nSpring Break;\n    March 6th: 6-8am & 3-6pm\n    March 7-11th: 7:30-9:30am & 3-6pm\nMarch 18-19th; Ergathon\nMarch 21st; Elections after practice\n\n.flow -> Rowing info\n" + getTemp()

    message = data['text']

    if message == '.help':
        send(help_message, bot_info[0])
        return True

    if message == '.flow':

        send(getFlow(), bot_info[0])
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
        sentence_lfk = "Lawrence: "+ flow_lfk + " "
        # print(sentence_lfk)
    final = sentence_lfk + sentence_lcn
    return final
    # return flow_lcn, flow_lfk
    
 def getTemp():
    with urllib.request.urlopen("") as url:
        data_temp = json.loads(url.read().decode())
        temp_temp = data_temp["value"]["timeSeries"][0]["values"][0]["value"][0]["value"]
        return temp_temp
