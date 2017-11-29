import asyncio, bisect, importlib, json, os, re, sys

import hangups
import appdirs

import utils

class Pearl:

	def __init__(self):
		self.load_config()
		self.client = hangups.client.Client(self.login())
		self.load_commands()

	def login(self):
		dirs = appdirs.AppDirs('hangups', 'hangups')
		token = hangups.RefreshTokenCache(os.path.join(dirs.user_cache_dir, 'refresh_token.txt'))
		return hangups.get_auth(utils.Authenticator(self.auth['email'], self.auth['password']), token)

	def load_config(self):
		self.config = json.load(open('config.json'))
		self.auth = json.load(open(self.config['auth']))

	def load_commands(self):
		self.pattern = re.compile('^' + self.config['format'] + ' [a-zA-Z0-9_]')

		pluginlist = {'command': [], 'passive': [], 'utility': []}
		for plugin in self.config['plugins']:
			bisect.insort(pluginlist[self.config['plugins'][plugin]['type']], plugin)
		self.pluginlist = pluginlist

		plugins = {}
		for plugin in self.config['plugins']:
			path = os.path.join(os.getcwd(), self.config['plugins'][plugin]['path'])
			spec = importlib.util.spec_from_file_location(plugin, path)
			handler = importlib.util.module_from_spec(spec)
			spec.loader.exec_module(handler)
			plugins[plugin] = handler.initialize(self)
		self.plugins = plugins

	def run(self):
		self.client.on_connect.add_observer(self.initialize)
		self.client.on_state_update.add_observer(self.handle)
		self.loop = asyncio.get_event_loop()
		self.loop.run_until_complete(self.client.connect())

	@asyncio.coroutine
	def initialize(self):
		self.users, self.conversations = yield from hangups.build_user_conversation_list(self.client)

	@asyncio.coroutine
	def handle(self, update):
		event = update.event_notification.event
		if event.event_type == utils.EventType.EVENT_TYPE_REGULAR_CHAT_MESSAGE.value:
			message = hangups.ChatMessageEvent(event).text
			if self.pattern.match(message):
				self.execute(message, event)

	def execute(self, message, event):
		command = message.split()
		plugin = command[1]
		args = command[2:]
		if plugin in self.pluginlist['command']:
			self.plugins[plugin].handle(args, event)

Pearl().run()