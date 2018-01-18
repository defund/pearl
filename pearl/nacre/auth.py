class Authenticator:

	def __init__(self, email, password):
		self.email = email
		self.password = password

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password