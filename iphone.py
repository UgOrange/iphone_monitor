import requests
import time
import json
#import Carbon.Snd
import os
import webbrowser
import datetime
#想要的机型
want=['MLT93CH/A','MLTC3CH/A','MLTD3CH/A','MLTE3CH/A','MLH83CH/A','MLH93CH/A','MLHA3CH/A','MLHC3CH/A','MLH43CH/A','MLH53CH/A','MLH63CH/A','MLH73CH/A','MLTF3CH/A','MLTG3CH/A','MLTH3CH/A','MLTJ3CH/A']
#不想去的店（我这里是三家天津的店）
unwant=["R579","R638","R637"]
headers = {
    'authority': 'www.apple.com.cn',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'sec-ch-ua-platform': '"macOS"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.apple.com.cn/shop/buy-iphone/iphone-13-pro/MLH83CH/A',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'dssid2=2a787326-d6c4-4b56-8aeb-7370a5e5167e; dssf=1; as_sfa=Mnxjbnxjbnx8emhfQ058Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; as_uct=0; geo=CN; at_check=true; as_pcts=3QwGdEMIOjKyfAaDuFVCzZQRevN6aKfi8TB5SMI2nW2kNoteAPztl1PhjFkCb-KoX_4h4sy6AnqqFzCnNUz5pZ-KldYg:hQ:dXp_UoKwjFsQ+aSre+:DBM; as_dc=nc; as_atb=1.0|MjAyMS0xMC0yNCAwNzoxMzowMA|49ab2291915cbf36cacfbdf89f033963bd9cc0db; s_vi=[CS]v1|30BB0956B2E18091-6000196AEE2FB3D5[CE]; mbox=session#ae644ae781f0480289e064c0b30548a5#1635129839|PC#ae644ae781f0480289e064c0b30548a5.32_0#1635129780; as_gloc=3f64c43efd446f555bd56a7f46a4aa5c745e5f0d58b61bc85d7c73ab20dd51da567f9a3b101d3663adc0df685fa58824c9383345599b25e7136f937b782787ee9a812db04f4a893d802505dda7ff85a3711425a231933b0106d14ce070277c55f3e6dddf37ea5715a19f29888dcefec1c839d2f3e80db512171c1baba4bb9bf8',
}

params = (
    ('mt', 'compact'),
    ('searchNearby', 'true'),
    ('store', 'R579'),
    ('product', 'MLH83CH/A'),
)
while True:
    response = requests.get('https://www.apple.com.cn/shop/pickup-message-recommendations', headers=headers, params=params)
	#print(response.text)
    obj=json.loads(response.text)
    if(len(obj['body']['PickupMessage']['recommendedProducts'])!=0):
        print(obj['body']['PickupMessage']['recommendedProducts'])
        for store in obj['body']['PickupMessage']['stores']:
            if(store['storeNumber'] in unwant):
                continue
            for key,value in store['partsAvailability'].items():
                if key in want:
                    print("https://www.apple.com.cn/shop/buy-iphone/iphone-13-pro/"+key)
                    duration = 1  # second
                    freq = 440  # Hz
                    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
                    webbrowser.open("https://www.apple.com.cn/shop/buy-iphone/iphone-13-pro/"+key,autoraise=False)
                    time.sleep(20)
                
        
    time2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(time2)
    print(obj['body']['PickupMessage']['recommendedProducts'])   
    time.sleep(1)


