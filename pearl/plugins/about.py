import asyncio
import hangups

from command import Command

def sendMessage(self,event,message):
	asyncio.run_coroutine_threadsafe(self.send(message, event.conversation_id.id), self.pearl.loop)

class About(Command):

	about = 'Pearl is a bot framework for Google Hangouts. You can view source code at https://github.com/defund/pearl. Thanks!'

	def __init__(self, pearl):
		self.pearl = pearl
		self.client = pearl.client

	def handle(self, args, event):
		sendMessage(self, event, self.about)

def initialize(pearl):
	return About(pearl)
