import asyncio

import hangups

class Hello:

	def __init__(self, client):
		self.client = client

	@asyncio.coroutine
	def handle(self, pearl, args, event):
		hello = 'Hello!'
		gaia_id = event.sender_id.gaia_id
		for user in pearl.users.get_all():
			if user.id_.gaia_id == gaia_id:
				hello = 'Hello ' + user.full_name.split()[0] + '!'
		
		request = hangups.hangouts_pb2.SendChatMessageRequest(
			request_header=self.client.get_request_header(),
			event_request_header=hangups.hangouts_pb2.EventRequestHeader(
				conversation_id=hangups.hangouts_pb2.ConversationId(
					id=event.conversation_id.id
				),
				client_generated_id=self.client.get_client_generated_id(),
			),
			message_content=hangups.hangouts_pb2.MessageContent(
				segment=[
					hangups.ChatMessageSegment(hello).serialize()
				],
			),
		)
		yield from self.client.send_chat_message(request)

def initialize(client):
	return Hello(client)