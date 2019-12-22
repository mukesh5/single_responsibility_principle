from datetime import date

class GYMManager:

	def __init__(self):
		self.customers = []
		self.packages = []
		self.payment = Payment()
	
	def add_package(self, package):
		print('Adding Package.. {} with Fee {}'.format(package.name, package.fee))
		self.packages.append(package)
		print('Done...')

	def add_customers(self, customer):
		print('Adding Customer {} '.format(customer.name))
		self.payment.make_payment(customer.paid_amount)
		self.customers.append(customer)
		print('Done..')




class Package:
	def __init__(self, package_name, package_fee):
		self.name = package_name
		self.fee = package_fee
	

	def print_package_details(self):
		print('Package Name: {}'.format(self.name))
		print('Package Fee: {}'.format(self.fee))
		print('Done...')



class Customer:
	def __init__(self, customer_name, package_name, paid_amount, start_date):
		self.name = customer_name
		self.package = package_name
		self.paid_amount = paid_amount
		self.start_date = start_date


	def get_customer_details(self):
		print('Customer Name: {}'.format(self.name))
		print('Customer Package: {}'.format(self.package))
		print('Customer Paid Amount: {}'.format(self.paid_amount))
		print('Customer Start Date: {}'.format(self.start_date))
		print('Done....')
		


class Payment:

	def make_payment(self, amount):
		print('Starting Payment...')
		print('Amount Paid {}'.format(amount))
		print('Payment Successful...')








