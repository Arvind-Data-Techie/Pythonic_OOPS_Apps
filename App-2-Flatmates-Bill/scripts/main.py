from flat import Bill,Flatmate
from bill_pdf import Pdfreport

import os

'''
Get the Bill Amount and period
'''

bill_amount=int(input('Enter the Bill Amount : '))
period=input('Enter the Month and Year : ')
the_bill=Bill(bill_amount,period)

'''
Get the Number of Days
'''

f1_no_of_days=int(input('Enter the Number of days Arvind has stayed: '))
f2_no_of_days=int(input('Enter the Number of days Harshni has stayed: '))


'''
Initialize Flatmates
'''

arvind=Flatmate("Arvind",f1_no_of_days)
harshni=Flatmate("Harshni",f2_no_of_days)

'''
Calculate  the amount
'''

arvind_amount=arvind.pay_bill(the_bill,harshni)
harshni_amount=harshni.pay_bill(the_bill,arvind)

'''
Build the Report 
'''

pdf_path = os.path.join(os.path.dirname(__file__), '..', 'files', 'bill_generator.pdf')

Pdfreport(pdf_path).generate_pdf(arvind,harshni,the_bill)