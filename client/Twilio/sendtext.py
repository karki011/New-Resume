

from twilio.rest import TwilioRestClient

account_sid = "AC93a23d379cb93292e2f7134a84ce9023"
auth_token = "eab58c90109d55f7c049db5d4ef59919"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Subash Please?",
    to="+12564266622",
    from_="+12562035638")
print message.sid
