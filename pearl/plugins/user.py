import asyncio
import hangups
import re

from interactive import Interactive

class User(Interactive):

	usage = 'Methods:\n' + \
			'<b>list</b>: List users in chat\n' + \
			'<b>self</b>: View your profile\n' + \
			'<b>set</b>: Set your username'

	def __init__(self, pearl):
		self.pearl = pearl

		self.database = False
		self.methods = {
			'list': self.list_method,
			'self': self.self_method, 
			'set': self.set_method
		}

	def handle(self, args, event):
		if not self.database:
			self.users_ref = self.pearl.plugins['firebase'].db.collection('users')
			self.database = True

		if len(args) > 0 and args[0] in self.methods:
			try:
				self.methods[args[0]](args[1:], event)
			except:
				response = 'Sorry, Firebase threw an error. Please try again!'
				asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
				return
		else:
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), self.usage), self.pearl.loop)
			return

	def users(self):
		docs = self.users_ref.get()
		users = {}
		for doc in docs:
			users[doc.id] = doc.to_dict()
		return users

	def username(self, uid):
		users = self.users()
		for username in users:
			if 'uid' in users[username] and users[username]['uid'] == uid:
				return username
		return None

	def list_method(self, args, event):
		response = 'User List:'
		users = self.users()
		for username in sorted(users.keys()):
			if 'uid' in users[username]:
				name = self.user(raw=users[username]['uid']).full_name
				response += '\n<b>{}</b> ({})'.format(username, name)
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)


	def self_method(self, args, event):
		username = self.username(event.sender_id.gaia_id)
		if username:
			response = 'You are set to <b>{}</b>.'.format(username)
		else:
			response = 'You do not have a username. Create one by sending <i>user set username</i>'
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)

	def set_method(self, args, event):
		if len(args) == 0:
			response = 'Usage: user set username'
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		new = args[0].lower()
		old = self.username(event.sender_id.gaia_id)
		
		if len(new) < 3 or len(new) > 32:
			response = 'Username must be between 3 and 32 characters long.'
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		if not re.match('^\w+$', new):
			response = 'Username must only contain alphanumerics or underscores.'
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		if new == old:
			response = 'That\'s your current username, silly!'
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		if new in self.users():
			response = 'Sorry, <b>{}</b> is already taken.'.format(new)
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		if old:
			self.users_ref.document(old).delete()

		doc_ref = self.users_ref.document(new)
		doc_ref.set({
			'uid': event.sender_id.gaia_id
		})
		response = 'You are now set to <b>{}</b>!'.format(new)
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)

def initialize(pearl):
	return User(pearl)