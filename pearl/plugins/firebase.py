import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Firebase:

	def __init__(self, pearl):
		self.pearl = pearl
		
		path = os.path.join(os.getcwd(), self.pearl.config['plugins']['firebase']['auth'])
		cred = credentials.Certificate(path)
		firebase_admin.initialize_app(cred)
		self.db = firestore.client()

def initialize(pearl):
	return Firebase(pearl)