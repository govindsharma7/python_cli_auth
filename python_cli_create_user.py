# Create New role base user

import sys
from getpass import getpass


class CreateUserPermission(object):
	"""docstring for CreateUserPermission"""

	def check_user_exist(self, name):
		'''
		Used to check user exist or not.
		'''
		if name in self.user_record:
			return self.user_record[name]
		print("Invalid user. Please select create user option to create new user.")
		option = self.print_option()
		return self.selected_option(option)

	def switch_user(self):
		'''
		For swtiching from one user to another
		'''
		name = input("Enter User Name : ")
		self.check_user_exist(name)
		option = self.print_option(name)
		return self.selected_option(option)

	def create_user(self):
		'''
		For creating new user
		'''
		name = input("Enter User Name : ")
		password = getpass("Enter password to login : ")
		self.user_record[name] = {
			'user_name': name,
			'password': password,
			'role': self.user_role['user']
		}
		option = self.print_option(name)
		return self.selected_option(option)

	def edit_role(self):
		'''
		For edit role to the user
		'''
		name = input("Enter User Name : ")
		self.check_user_exist(name)
		print('Please select recource and action from the list:')
		print("Recource :", self.resource)
		print("Acction Type :", self.action_type)
		print("Please give input :")
		user_resource = input("Select Resource : ")
		action = input("Select Action (Please enter only key):")
		if 'resource' in self.user_record[name]:
			if action not in self.action_type:
				print("Please input valid action type")
			self.user_record[name]['resource'].update({
				user_resource: action
			})
		else:
			self.user_record[name]['resource'] = {
				user_resource: action
			}
		print('Role assign to user', name)
		option = self.print_option()
		return self.selected_option(option)

	def selected_option(self, option):
		'''
		Select option function
		'''
		if int(option) == 1:
			return self.switch_user()
		elif int(option) == 2:
			return self.create_user()
		elif int(option) == 3:
			return self.edit_role()
		elif int(option) == 4:
			return
		else:
			print("Please select an valid option")
			self.print_option()
			return self.selected_option(option)

	def print_option(self, name=None):
		'''
		Common print options
		'''
		if name:
			print("hi! you are logged in as", name)
		print("press 1 for login as another user")
		print("press 2 for create user")
		print("press 3 for edit role")
		print("press 4 for exit")
		option = input("Select Option : ")
		return option

	def __init__(self):
		super(CreateUserPermission, self).__init__()

		# Some pre-define variable along with data
		self.user_role = {
			'admin': 1,
			'user': 2
		}

		self.action_type = {
			'full': ['read', 'write', 'delete'],
			'rw': ['read', 'write'],
			'wd': ['write', 'delete'],
			'rd': ['read', 'delete'],
			'r': ['read'],
			'w': ['write'],
			'd': ['delete']
		}

		# These are the sample resource
		self.resource = [
			'full',
			'see_profile',
			'create_user',
			'fetch_user',
			'send_sms',
			'email_notify'
		]

		self.user_record = {}

		# Creating admin user
		self.user_record['admin'] = {
			'user_name': 'admin',
			'password': 'password',
			'role': self.user_role['admin'],
			'resource': {
				self.resource[0]: self.action_type['full']
			}
		}
		option = self.print_option('admin')
		return self.selected_option(option)


CreateUserPermission()
