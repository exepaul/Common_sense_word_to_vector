from bs4 import BeautifulSoup
import requests as parser
import json




#getting the  equal distance word vectors from given word vector like:

#'               Phone' ==>

# {'data', 'dies', 'hangouts', 'number', 'services', 'etc',
#  'iphone', 'phone-', 'idevice', 'mode', 'messages', 'iphone/ipad',
#  'scanner', 'plan', 'handset', 'ipad', 'smartphone', 'landline', 'sensor',
# 'headset', 'calls', 'phone/ipad', 'feature', 'dumbphone', 'cause', 'lol',
# 'device', 'message', 'player', 'card', 'line', 's5', 'call', 'app', 'notifications',
# 'facetime', 'wi-fi', 'voicemail', 'hotspot', 'imessages', 'phone/computer', 'right',
# 'memo', 'id', 'bluetooth', 'anyways', 'dialer', 'haha', 'everyday', 'tooth', 'tablet',
# 'phone*.', 'ipod', 'touch', 'history', 'needs', 'vibrate', 'phone/tablet', 'cellphone',
# 'siri', 'imessage', 'network', 'phones', 'pebble', 'laptop', 'speaker', 'flip-phone',
# 'speakerphone', 'screen', 'computer', 'wifi', 'phone/laptop', 'voice', 'control', '&amp;',
# 'phone_', 'works', 'connection'}





def sense_2_vector_words_model(query):
    vectors_words = []
    for each_word in query:

        query_1 = '68747470733a2f2f6170692e6578706c6f73696f6e2e61692f73656e7365327665632f' + each_word.lower().encode('utf-8').hex()

        get_url = parser.get(bytearray.fromhex(query_1).decode())

        _parser = BeautifulSoup(get_url.text, "html.parser")
        json_format_vectors = json.loads(_parser.decode())
        for item in json_format_vectors['results']:
            vectors_words.append(item['head'])

    return list(set(vectors_words))


print(sense_2_vector_words_model(['sit']))
