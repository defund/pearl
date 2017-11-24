import asyncio
import hangups

from command import Command

class Hello(Command):

	def __init__(self, pearl):
		self.pearl = pearl
		self.client = pearl.client
		self.build()

	def build(self):
		usage_help = 'Usage: ' + self.pearl.config['format'] + ' command<br>Commands:'
		for plugin in self.pearl.plugins:
			usage_help += '<br><b>' + plugin + '</b>: ' + self.pearl.config['plugins'][plugin]['help']
		self.usage_help = usage_help

	def handle(self, args, event):
		asyncio.run_coroutine_threadsafe(self.send(self.usage_help, event.conversation_id.id), self.pearl.loop)

def initialize(pearl):
	return Hello(pearl)