from twilio.rest import Client

account_sid="AC1e0f9caefbbxc11c3c4d69b68ec57c172"	# Account Serial ID
auth_token="1415629c1f4dx698beaa5466fb5b3993f"		# Authentication token
sender_no="+183160716123"				# Number provided by twilio
receiver_no="+909977287232"				# Number verified by twilio
msg="message sended by RaspberryPi"			# Message

client=Client(account_sid, auth_token)
client.messages.create(from_=sender_no, body=msg, to=receiver_no)
