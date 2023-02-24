class Expense_Calc:
	def __init__(self, arr, account, amount):
		self.arr = arr
		self.account = account
		self.amount = amount
		self.type20_nums = [5260, 5340, 5490, 5848, 6000, 6010, 6040, 6045]

		self.summed_balances = []
		
		'''the init fucntion will take each account in the manufacturing reports (list "self.arr"),
		 find the correpsoning account list from the reference object (list "account"), and locate
		 the expense for that account (list "amount"). It will then add that amound to the expense
		 column that will be included on the output excel sheet.'''
		for x in self.arr:
			balances_to_sum = []
			draft_item = self.ultrafine_exception_handler(x)
			item = self.str_to_nbr_list(draft_item)
			print(item)
			for num in item:
				if num in self.type20_nums:
					mode = "exclude"
				else:
					mode = "include"
				balance_to_sum = self.reference_account_balance(num, self.account, self.amount, mode)
				balances_to_sum.append(balance_to_sum)
			summed_balance = sum(balances_to_sum)
			self.summed_balances.append(summed_balance)

		self.answer = self.summed_balances

	'''helper fuction: each account from list "self.arr" consist of a list of sub accounts in a
		string. This fucntion converts the string of numbers into a list of number for python
		to iterate through'''
	def str_to_nbr_list(self, array):
		num_list = [int(i) for i in array]
		return num_list

	'''helper function: given a number as well as the account and amount reference lists, it will
		find the given number in the account list and return the amount from the amount list
		that correpsonds to the account.'''
	def reference_account_balance(self, nbr, account, amount, mode):
		result = 0
		for c in account:
			if round(c) == nbr:
				sub = account.index(c)
				if account.index(c) != len(account) - 1:
					if round(account[sub + 1]) == nbr:
						if mode == "exclude":
							result = amount[sub]
						else:
							result = amount[sub] + amount[sub + 1]
					else:
						result = amount[sub]
				else:
					result = amount[sub]
				break
		return result


	def ultrafine_exception_handler(self, item):
		inspection = [str(i) for i in item.split()]
		for j in inspection:
			if "Excl." in j:
				inspection.remove(j)
		return inspection