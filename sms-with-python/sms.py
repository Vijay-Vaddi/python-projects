from twilio.rest import Client

account_sid = 'ACxxxxxxxxxxxxxx9f2be7e12cfbad9f17'
auth_token = 'dd3xxxxxxxxxxxxxxxxxc77762164ab65e7'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_ ='+447723463960',
    body='Hello',
    to='+447384351475'
)

print(message.sid)