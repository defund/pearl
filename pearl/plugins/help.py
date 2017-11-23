import asyncio

import hangups

class Hello:

	def __init__(self, pearl):
		self.pearl = pearl
		self.client = pearl.client
		self.build()

	def build(self):
		usage_help = 'Usage: ' + self.pearl.config['format'] + ' command<br>Commands:'
		for plugin in self.pearl.config['plugins']:
			usage_help += '<br><b>' + plugin + '</b>: ' + self.pearl.config['plugins'][plugin]['help']
		self.usage_help = hangups.ChatMessageSegment.from_str(usage_help)

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
				segment=[seg.serialize() for seg in self.usage_help]
			),
		)
		yield from self.client.send_chat_message(request)

def initialize(client):
	return Hello(client)