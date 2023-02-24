import pandas as pd
import ExpenseCalculationObject as eco
import ReferenceObject as ro

'''variables used as parameters for the pandas dataframe'''
path = input("Enter Report Directory:")
iopath = path.translate({ord('"'): None})
#iopath = "C:\\Users\\jcjct\\Downloads\\Documents\\ManufacturingExpenseAutomation\\Ultra Fine Mfg Expense Tracker.xlsx"
clm_names = ['expense types', 'accounts']
clms = [0, 1]

'''creating dataframe from excel column'''
df = pd.read_excel(io=iopath, sheet_name=0, header=4, names=clm_names, index_col=0, usecols=clms, dtype=str)

'''converting pandas data frame into a list to be iterated through and modified'''
accnt_list_rough = list(df['accounts'])

'''removing blank cells from dataframe, blank cells are marked with "nan"'''
for i in accnt_list_rough:
	if type(i) != str:
		pop_index = accnt_list_rough.index(i)
		break

for x in range(pop_index, len(accnt_list_rough)):
	accnt_list_rough.pop(pop_index)

'''excel column as a list in python (with spaces removed) ready to be manipulated'''
accnt_list = accnt_list_rough
account_ref = ro.account
amount_ref = ro.amount

'''calls upon the power of the Expense Calculation Module to sort through the list and find the expense balance of each account'''
expense_col = [round(i, 0) for i in eco.Expense_Calc(accnt_list, account_ref, amount_ref).answer]

'''Out put the expense column into an excel spreadsheet'''
expense_frame = {'Accounts':accnt_list, 'Balance': expense_col}
ef = pd.DataFrame(expense_frame)
output_directory = r"C:\Users\jcjct\Downloads\Documents\Manufacturing-Expense-Automation\NewTracker.xlsx"
ef.to_excel(output_directory)