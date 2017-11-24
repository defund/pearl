import abc
import asyncio
import hangups

class Command:
	__metaclass__  = abc.ABCMeta

	@abc.abstractmethod
	def __init__(self, pearl):
		...

	@abc.abstractmethod
	def handle(self, args, event):
		...

	@asyncio.coroutine
	def send(self, message, eid):
		segment = hangups.ChatMessageSegment.from_str(message)
		request = hangups.hangouts_pb2.SendChatMessageRequest(
			request_header=self.client.get_request_header(),
			event_request_header=hangups.hangouts_pb2.EventRequestHeader(
				conversation_id=hangups.hangouts_pb2.ConversationId(
					id=eid
				),
				client_generated_id=self.client.get_client_generated_id(),
			),
			message_content=hangups.hangouts_pb2.MessageContent(
				segment=[seg.serialize() for seg in segment]
			)
		)
		yield from self.client.send_chat_message(request)

	@asyncio.coroutine
	def invite(self, accounts, eid):
		request = hangups.hangouts_pb2.AddUserRequest(
			request_header=self.client.get_request_header(),
			invitee_id=[hangups.hangouts_pb2.InviteeID(gaia_id=account['gaia_id']) for account in accounts],
			event_request_header=hangups.hangouts_pb2.EventRequestHeader(
				conversation_id=hangups.hangouts_pb2.ConversationId(
					id=eid
				),
				client_generated_id=self.client.get_client_generated_id(),
			),
		)
		yield from self.client.add_user(request)
