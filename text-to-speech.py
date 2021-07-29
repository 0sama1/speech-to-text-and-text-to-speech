
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'EtGPFm9rPIM8fdtWr12VOM7iXvVuCfy6WYFEUqvZ03r2'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/700ce724-fe09-4149-bf8d-deecdf9da1e4'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('./output.mp3', 'wb') as audio_file:
    res = tts.synthesize('!Hello, !hello, !test, !test.', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)