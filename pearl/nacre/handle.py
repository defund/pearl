import re

import hangups

def isEventNotification(update):
	if update.event_notification:
		return True
	return False

def isMessageEvent(update):
	if isEventNotification(update):
		event = update.event_notification.event
		if event.event_type == hangups.hangouts_pb2.EVENT_TYPE_REGULAR_CHAT_MESSAGE:
			return True
	return False

def newConversationFilter(conversationIdList):
	return lambda event: hangups.ConversationEvent(event).conversation_id in conversationIdList

def newMessageFilter(regex):
	pattern = re.compile(regex)
	return lambda event: bool(pattern.match(hangups.ChatMessageEvent(event).text))

def newUserFilter(gaiaIdList):
	return lambda event: hangups.ConversationEvent(event).user_id.gaia_id in gaiaIdList
