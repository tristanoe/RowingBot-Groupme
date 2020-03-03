import urllib.request, json

def run(data, bot_info, send):

    help_message = "Help:\n.help  -->  This screen\n.test  -->  Try it!\nOtherwise, repeats your message."

    message = data['text']

    if message == '.help':
        send(help_message, bot_info[0])
        return True

    if message == '.test':

        send(getFlow(), bot_info[0])
        return True

    send("Hi {}! You said: {}".format(data['name'], data['text']), bot_info[0])
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
        sentence_lfk = "Lawrence: "+ flow_lfk
        # print(sentence_lfk)
    final = sentence_lfk + sentence_lcn
    return final
    # return flow_lcn, flow_lfk
