import hangups

class Hangouts:

	def __init__(self, client):
		self.client = client

	async def start(self):
		self.users, self.conversations = await hangups.build_user_conversation_list(self.client)

	async def send(self, message, conversation, annotate=True, raw=False):
		if annotate:
			annotationType = 4
		else:
			annotationType = 0

		if raw:
			segments = [hangups.ChatMessageSegment(message)]
		else:
			segments = hangups.ChatMessageSegment.from_str(message)

		request = hangups.hangouts_pb2.SendChatMessageRequest(
			request_header=self.client.get_request_header(),
			event_request_header=conversation._get_event_request_header(),
			message_content=hangups.hangouts_pb2.MessageContent(
				segment=[segment.serialize() for segment in segments]
			),
			annotation=[hangups.hangouts_pb2.EventAnnotation(
				type=annotationType
			)]
		)
		
		await self.client.send_chat_message(request)

	def getConversation(self, cid=None, event=None):
		if event:
			cid = event.conversation_id.id
		return self.conversations.get(cid)

	def getUser(self, uid=None, event=None):
		if event:
			uid = event.sender_id.gaia_id
		return self.users.get_user(hangups.user.UserID(uid, uid))
