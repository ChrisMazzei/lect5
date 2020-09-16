from twilio.rest import Client
import os
# this is insecure!

twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(twilio_account_sid, twilio_auth_token)

message = client.messages \
                .create(
                        body="Newest Message",
                        from_='+16614855244',
                        to='+19738862754')
                        
print(message.sid)