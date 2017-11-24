import asyncio
import hangups

import random

from command import Command

class EightBall(Command):

	answers = [
		'It is certain',
		'It is decidedly so',
		'Without a doubt',
		'Yes definitely',
		'You may rely on it',
		'As I see it, yes',
		'Most likely',
		'Outlook good',
		'Yes',
		'Signs point to yes',
		'Reply hazy try again',
		'Ask again later',
		'Better not tell you now',
		'Cannot predict now',
		'Concentrate and ask again',
		'Don\'t count on it',
		'My reply is no',
		'My sources say no',
		'Outlook not so good',
		'Very doubtful'
	]

	def __init__(self, pearl):
		self.pearl = pearl
		self.client = pearl.client

	def handle(self, args, event):
		answer = random.choice(self.answers)
		asyncio.run_coroutine_threadsafe(self.send(answer, event.conversation_id.id), self.pearl.loop)

def initialize(pearl):
	return EightBall(pearl)