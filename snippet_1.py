from datetime import date

class GYMManager:

	def __init__(self):
		self.customers = []
		self.packages = []
		

	def add_package(self, package_name, package_amount):
		print('...Adding Package {} with Amount Rs. {}'.format(package_name, package_amount))
		d = {package_name:package_amount}
		self.packages.append(d)
		print('Package Added')
		


	def add_customers(self, customer_name, amount, package, start_date):
		print('...Adding Customer {} to Customer List'.format(customer_name))
		d = {'Name':customer_name, 'Package':package, 'Start_Date':start_date}
		if self.make_payment(customer_name, amount):
			curr_package = next(pack for pack in self.packages if package in pack)
			d['Paid_Amount'] = amount
			self.customers.append(d)
		print('Customer Successfully Added!!')


	def make_payment(self, customer_name, amount):
		print('Starting Payment...')
		print('Payment Successful!!')
		return True


	def get_customer_details(self, customer_name):
		customer = next(cust for cust in self.customers if cust['Name']==customer_name)
		print('Customer Name: {}'.format(customer['Name']))
		print('Customer Package: {}'.format(customer['Package']))
		print('Customer Paid Amount: {}'.format(customer['Paid_Amount']))
		print('Customer Start Date: {}'.format(customer['Start_Date']))
		print('Done....')



gym = GYMManager()

gym.add_package('yearly', 10000)
#...Adding Package yearly with Amount Rs. 10000
#Package Added


gym.add_customers('Mukesh', 5000, 'yearly', date.today())
#...Adding Customer Mukesh to Customer List
#Starting Payment...
#Payment Successful!!
#Customer Successfully Added!!


gym.get_customer_details('Mukesh')		
#Customer Name: Mukesh
#Customer Package: yearly
#Customer Paid Amount: 5000
#Customer Start Date: 2019-12-22
#Done....

