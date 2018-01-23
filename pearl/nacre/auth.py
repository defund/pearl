import pyotp

class Authenticator:

	def __init__(self, email, password, secret):
		self.email = email
		self.password = password
		self.totp = pyotp.TOTP(secret)

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

	def get_verification_code(self):
		return self.totp.now()