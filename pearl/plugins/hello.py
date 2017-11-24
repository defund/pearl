import asyncio
import hangups

from command import Command

def sendMessage(self,event,message):
	asyncio.run_coroutine_threadsafe(self.send(message, event.conversation_id.id), self.pearl.loop)
	
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
				
		sendMessage(self,event,hello)

def initialize(pearl):
	return Hello(pearl)
