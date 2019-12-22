from datetime import date


class GYMManager:

	def __init__(self):
		self.customers = CustomerListManager()
		self.packages = PackageListManager()
		self.customer_details = CustomerDetails()
		self.package_details = PackageDetails()
		self.payment = Payment()
	

class ListManager:
	def __init__(self, item_type):
		self.item_list = []
		self.item_type = item_type

	def add_to_list(self, item, payment=None):
		print('Adding Item {} to list'.format(self.item_type))



class CustomerListManager(ListManager):
	def __init__(self):
		super().__init__('Customers')

	def add_to_list(self, item, payment=None):
		print('Adding Customer {} '.format(item.name))
		payment.make_payment(item.paid_amount)
		self.item_list.append(item)
		print('Done..')


class PackageListManager(ListManager):
	def __init__(self):
		super().__init__('Packages')

	def add_to_list(self, item, payment=None):
		print('Adding Package.. {} with Fee {}'.format(item.name, item.fee))
		self.item_list.append(item)
		print('Done...')
	


class Package:
	def __init__(self, package_name, package_fee):
		self.name = package_name
		self.fee = package_fee



class Customer:
	def __init__(self, customer_name, package_name, paid_amount, start_date):
		self.name = customer_name
		self.package = package_name
		self.paid_amount = paid_amount
		self.start_date = start_date

		
class Details:
	def __init__(self, item_type):
		self.item_type = item_type

	def print_details(self):
		print('---------- Details for {} -----------'.format(self.item_type))


class CustomerDetails(Details):
	def __init__(self):
		super().__init__('customer')

	def print_details(self, customer):
		print('Customer Name: {}'.format(customer.name))
		print('Customer Package: {}'.format(customer.package))
		print('Customer Paid Amount: {}'.format(customer.paid_amount))
		print('Customer Start Date: {}'.format(customer.start_date))
		print('Done....')


class PackageDetails(Details):
	def __init__(self):
		super().__init__('package')

	def print_details(self, package):
		print('Package Name: {}'.format(package.name))
		print('Package Fee: {}'.format(package.fee))
		print('Done...')


class Payment:

	def make_payment(self, amount):
		print('Starting Payment...')
		print('Amount Paid {}'.format(amount))
		print('Payment Successful...')



gym = GYMManager()

gym.packages.add_to_list(Package('yearly', 10000))
#Adding Package.. yearly with Fee 10000
#Done...


gym.customers.add_to_list(Customer('Mukesh', 'yearly', 10000, date.today()), gym.payment)
#Adding Customer Mukesh 
#Starting Payment...
#Amount Paid 10000
#Payment Successful...
#Done..


gym.customer_details.print_details(gym.customers.item_list[0])
#Customer Name: Mukesh
#Customer Package: yearly
#Customer Paid Amount: 10000
#Customer Start Date: 2019-12-22
#Done....






