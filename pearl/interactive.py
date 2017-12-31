import abc
import asyncio
import hangups

class Interactive:
	__metaclass__  = abc.ABCMeta

	@abc.abstractmethod
	def __init__(self, pearl):
		...

	@abc.abstractmethod
	def handle(self, args, event):
		...

	@asyncio.coroutine
	def send(self, conversation, message, annotate=True):
		request = hangups.hangouts_pb2.SendChatMessageRequest(
			request_header=self.pearl.client.get_request_header(),
			event_request_header=conversation._get_event_request_header(),
			message_content=hangups.hangouts_pb2.MessageContent(
				segment=[seg.serialize() for seg in hangups.ChatMessageSegment.from_str(message)]
			),
			annotation=[hangups.hangouts_pb2.EventAnnotation(
				type=4
			)]
		)
		if not annotate:
			request.annotation[0].type = 0
		yield from self.pearl.client.send_chat_message(request)
		
	def conversation(self, raw=None, event=None):
		if raw:
			return self.pearl.conversations.get(raw)
		if event:
			return self.pearl.conversations.get(event.conversation_id.id)

	def user(self, raw=None, uid=None):
		if raw:
			return self.pearl.users.get_user(hangups.user.UserID(raw, raw))
		if uid:
			return self.pearl.users.get_user(hangups.user.UserID(uid.chat_id, uid.gaia_id))