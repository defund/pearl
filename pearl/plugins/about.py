import asyncio

import hangups

class About:
	about = 'Pearl is a bot framework for Google Hangouts. You can view source code at https://github.com/defund/pearl. Thanks!'

	def __init__(self, pearl):
		self.pearl = pearl
		self.client = pearl.client

	@asyncio.coroutine
	def handle(self, args, event):
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
					hangups.ChatMessageSegment(self.about).serialize()
				],
			),
		)
		yield from self.client.send_chat_message(request)

def initialize(client):
	return About(client)