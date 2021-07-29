from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey = 'N0EnM0X_OLiiyF6L4Y5eb5svTFCtCZkJvpayt28xSGrY'
url = 'https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/bb6adca0-43b2-4ed0-a4b5-b3be8ff5110e'
# Setup Service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)
# Perform conversion
with open('voice.mp3', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
    text = res['results'][0]['alternatives'][0]['transcript']

confidence = res['results'][0]['alternatives'][0]['confidence']

with open('output.txt', 'w') as out:
    out.writelines(text)