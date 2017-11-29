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