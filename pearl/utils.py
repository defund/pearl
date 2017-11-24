import enum

class Authenticator(object):

	def __init__(self, email, password):
		self.email = email
		self.password = password

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

class EventType(enum.Enum):
	EVENT_TYPE_UNKNOWN = 0
	EVENT_TYPE_REGULAR_CHAT_MESSAGE = 1
	EVENT_TYPE_SMS = 2
	EVENT_TYPE_VOICEMAIL = 3
	EVENT_TYPE_ADD_USER = 4
	EVENT_TYPE_REMOVE_USER = 5
	EVENT_TYPE_CONVERSATION_RENAME = 6
	EVENT_TYPE_HANGOUT = 7
	EVENT_TYPE_PHONE_CALL = 8
	EVENT_TYPE_OTR_MODIFICATION = 9
	EVENT_TYPE_PLAN_MUTATION = 10
	EVENT_TYPE_MMS = 11
	EVENT_TYPE_DEPRECATED_12 = 12
	EVENT_TYPE_OBSERVED_EVENT = 13
	EVENT_TYPE_GROUP_LINK_SHARING_MODIFICATION = 14