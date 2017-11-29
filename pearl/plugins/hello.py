import asyncio
import hangups

from interactive import Interactive

class Hello(Interactive):

	def __init__(self, pearl):
		self.pearl = pearl

	def handle(self, args, event):
		hello = 'Hello!'
		name = self.user(uid=event.sender_id).first_name
		hello = 'Hello {}!'.format(name)
				
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), hello), self.pearl.loop)

def initialize(pearl):
	return Hello(pearl)