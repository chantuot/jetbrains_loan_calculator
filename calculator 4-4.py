import math
import argparse


def nominal_interest(apr):
    beg_int = float(apr) / 1200
    return beg_int

def differential_payment(loan_principal, loan_period, loan_interest):
    diff_payment_counter = 1
    diff_payment_total = 0
    while diff_payment_counter <= (loan_period):
        diff_payment = math.ceil((loan_principal / loan_period) + nominal_interest(loan_interest) * (loan_principal - ((loan_principal * (diff_payment_counter - 1)) / loan_period)))
        print('Month ' + str(diff_payment_counter) + ': payment is', diff_payment)
        diff_payment_counter += 1
        diff_payment_total += diff_payment
    print()
    print('Overpayment =', diff_payment_total - loan_principal)

def pay_off_time(loan_principal, loan_payment, loan_interest):
    interest = nominal_interest(loan_interest)
    payment_time = math.log(loan_payment / (loan_payment - interest * loan_principal),1 + interest)
    finish_years = round(payment_time) // 12
    print("Your annunity payment =", finish_years, "!")
    print('Overpayment =', (loan_payment * finish_years * 12) - loan_principal)

def monthly_payment(loan_principal, loan_period, loan_interest):
    interest = nominal_interest(loan_interest)
    annuity = loan_principal * ((interest * (1 +interest) ** loan_period)) / (((1 + interest) ** loan_period) -1)
    print("Your monthly payment = " + str(math.ceil(annuity)) + "!")

def principal_loan(loan_payment, loan_period, loan_interest):
    interest = nominal_interest(loan_interest)
    principal = loan_payment / ((interest * ((1 + interest) ** loan_period)) / (((1 + interest) ** loan_period) - 1))
    print ("Your loan principal = ", math.floor(principal), "!")
    print('Overpayment =', math.ceil(loan_payment * loan_period - principal))



parser = argparse.ArgumentParser(description='differentiated payment or annuity financial calculator')
parser.add_argument('--type', type=str, help='picks either diff(erentiated payment) or annuity', choices=['diff', 'annuity'], dest='type')
parser.add_argument('--principal', type=int, help='principal loan ammount', dest='principal')
parser.add_argument('--periods', type=int, help='payment time or periods', dest='periods')
parser.add_argument('--payment', type=int, help='payment amount', dest='payment')
parser.add_argument('--interest', type=float, help='interest rate as a whole integer i.e. 10 for 10%', dest='interest')

args = parser.parse_args()

if args.type == 'diff':
    if args.principal is None or args.periods is None or args.interest is None:
        print('Incorrect parameters')
    else:
        differential_payment(args.principal, args.periods, args.interest)
elif args.type == 'annuity':
    if args.principal == None:
        if args.payment is None or args.periods is None or args.interest is None:
            print("Incorrect parameters")
        else:
            principal_loan(args.payment, args.periods, args.interest)
    elif args.periods == None:
        if args.principal is None or args.payment is None or args.interest is None:
            print("Incorrect parameters")
        else:
            pay_off_time(args.principal, args.payment, args.interest)
    elif args.payment == None:
        if args.principal is None or args.periods is None or args.interest is None:
            print('Incorrect parameters')
        else:
            monthly_payment(args.principal, args.periods, args.interest)
else:
    print('Incorrect parameters')
