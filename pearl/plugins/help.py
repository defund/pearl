import asyncio
import hangups

from interactive import Interactive

class Help(Interactive):

	def __init__(self, pearl):
		self.pearl = pearl
		self.build()

	def build(self):
		usage_help = 'Usage: ' + self.pearl.config['format'] + ' command<br>Commands:'
		for plugin in self.pearl.pluginlist['command']:
			usage_help += '<br><b>' + plugin + '</b>: ' + self.pearl.config['plugins'][plugin]['help']
		self.usage_help = usage_help

	def handle(self, args, event):
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), self.usage_help), self.pearl.loop)

def initialize(pearl):
	return Help(pearl)