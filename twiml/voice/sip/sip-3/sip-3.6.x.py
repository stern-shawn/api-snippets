from twilio.twiml.voice_response import Dial, VoiceResponse, Sip

response = VoiceResponse()
dial = Dial()
dial.sip('sip:jack@example.com?x-mycustomheader=foo&x-myotherheader=bar')
response.append(dial)

print(response)
