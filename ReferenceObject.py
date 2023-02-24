import pandas as pd

'''helper function to remove all empty spaces (marked as 'nan') from lists'''
def process_list(rough_list):
	loop_length = (len(rough_list) - 1) / 2 + 1
	for i in range(1, int(loop_length)):
		rough_list.pop(i)
	return rough_list

'''variables used as parameters in read_excel function'''
path = input("Enter Reference Directory:")
iopath = path.translate({ord('"'): None})
#iopath = "C:\\Users\\jcjct\\Downloads\\Documents\\ManufacturingExpenseAutomation\\Ultra Fine June 2021 Manufacturing Expense Balances.xlsx"
'''imports excel data into python dataframe object'''
df = pd.read_excel(io=iopath, sheet_name=0, index_col=None, dtype=str)

'''rough draft of account and amount lists'''
ACCNT = list(df.iloc[:, len(df.columns) - 2])
AMT = list(df.iloc[:, len(df.columns) - 1])

'''if the frame starts in the first row, where the index should be, this block will check
	for that and move the numbers from the index to the account and amount lists'''
index_item = False
flag = False
for c in df.columns:
	if flag == False:
		if type(c) != str:
			account_ind_item = c
			flag = True
			index_item = True
	else:
		amount_ind_item = c

'''if the frame starts lower than the second row, the account and amount lists will have empty
	spaces, marked with "nan", at the start of them. This block goes through and removes all
	"nan" spaces'''
mark = True
while mark:
	if type(ACCNT[0]) == float:
		ACCNT.pop(0)
		AMT.pop(0)
	else:
		break

'''second draft of account and amount lists'''
ACCOUNT = ACCNT
AMOUNT = AMT

'''if the excel spreadsheet was exported from the bank statement, there will be an empty space
	in between each number in the account and amount lists. If the excel spreadhseet was
	copied and pasted from the bank statement, there won't be. If mode = export, then the odd
	indices in the lists will be removed. If mode = paste, no change will be made.'''
if type(ACCOUNT[1]) == float:
	mode = 'export'
else:
	mode = 'paste'

'''final draft of account and amount lists'''
if mode == 'export':
	account = [int(i) for i in process_list(ACCOUNT)]
	amount = [float(i) for i in process_list(AMOUNT)]
else:
	account = [int(i) for i in ACCOUNT]
	amount = [float(i) for i in AMOUNT]

if index_item == True:
	account.append(int(account_ind_item))
	amount.append(float(amount_ind_item))