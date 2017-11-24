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
	def send(self, conversation, message, image=None):
		yield from conversation.send_message(hangups.ChatMessageSegment.from_str(message), image_file=image)

	def conversation(self, event=None):
		if event:
			return self.pearl.conversations.get(event.conversation_id.id)

	def user(self, uid=None):
		if uid:
			return self.pearl.users.get_user(hangups.user.UserID(uid.chat_id, uid.gaia_id))