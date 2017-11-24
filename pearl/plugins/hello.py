import asyncio
import hangups

from command import Command

class Hello(Command):

	def __init__(self, pearl):
		self.pearl = pearl
		self.client = pearl.client

	def handle(self, args, event):
		hello = 'Hello!'
		gaia_id = event.sender_id.gaia_id
		for user in self.pearl.users.get_all():
			if user.id_.gaia_id == gaia_id:
				hello = 'Hello ' + user.full_name.split()[0] + '!'
				
		asyncio.run_coroutine_threadsafe(self.send(hello, event.conversation_id.id), self.pearl.loop)

def initialize(client):
	return Hello(client)