import asyncio
from firebase_admin import firestore
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

		self.user_ref = None
		self.methods = {
			'list': self.list_method,
			'self': self.self_method, 
			'set': self.set_method
		}

	def handle(self, args, event):
		if len(args) > 0 and args[0] in self.methods:
			try:
				if not self.user_ref:
					self.user_ref = self.pearl.plugins['firebase'].db.collection('user')
					self.dbcall(event, lambda: self.user_ref.document('username').update({}, firestore.CreateIfMissingOption(True)))
				self.methods[args[0]](args[1:], event)
			except:
				return
		else:
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=self.event), self.usage), self.pearl.loop)
			return

	def dbcall(self, event, call, repeat=1):
		try:
			return call()
		except:
			if repeat:
				return self.dbcall(event, call, repeat=repeat-1)
			else:
				self.dbthrow(event)

	def dbthrow(self, event):
		response = 'Sorry, Firebase threw an error. Please try again!'
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
		raise Exception

	def users(self, event):
		username_ref = self.dbcall(event, lambda: self.user_ref.document('username'))
		return username_ref.get().to_dict()

	def usernames(self, event):
		users = self.users()
		return [users[uid] for uid in users]

	def uid(self, event, username):
		users = self.users(event)
		for uid in users:
			if users[uid] == username:
				return uid
		return None

	def username(self, event, uid):
		users = self.users(event)
		if uid in users:
			return users[uid]
		return None

	def list_method(self, args, event):
		users = self.users(event)
		entries = []
		for uid in users:
			entries.append([users[uid], self.user(raw=uid[1:]).full_name])
		response = 'User List:'
		for entry in sorted(entries):
			response += '\n<b>{}</b>: {}'.format(entry[0], entry[1])
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)


	def self_method(self, args, event):
		uid = 'u' + self.event.sender_id.gaia_id
		username = self.username(event, uid)
		if username:
			response = 'You are set to <b>{}</b>.'.format(username)
		else:
			response = 'You do not have a username. Create one with the <b>set</b> method.'
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)

	def set_method(self, args, event):
		if len(args) == 0:
			response = 'Usage: user set username'
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		usernames = self.usernames(event)
		uid = 'u' + event.sender_id.gaia_id
		new = args[0].lower()
		old = self.username(event, uid)
		
		if len(new) < 3 or len(new) > 12:
			response = 'Username must be between 3 and 12 characters long.'
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		if not re.match('^[a-zA-Z0-9]*$', new):
			response = 'Username must only contain alphanumeric characters.'
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		if new == old:
			response = 'That\'s your current username, silly!'
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		if new in usernames:
			response = 'Sorry, <b>{}</b> is already taken.'.format(new)
			asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)
			return

		self.dbcall(lambda: self.user_ref.document('username').update({
			uid: new
		}, firestore.CreateIfMissingOption(True)))
		response = 'You are now set to <b>{}</b>!'.format(new)
		asyncio.run_coroutine_threadsafe(self.send(self.conversation(event=event), response), self.pearl.loop)

def initialize(pearl):
	return User(pearl)