import asyncio
import hangups

from interactive import Interactive

class About(Interactive):

	about = 'Pearl is a bot framework for Google Hangouts. You can view source code at https://github.com/defund/pearl. Thanks!'

	def __init__(self, pearl):
		self.pearl = pearl

	def handle(self, args, event):
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), self.about), self.pearl.loop)

def initialize(pearl):
	return About(pearl)