# Name: Tyler Many
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one bagel: $2.25
#   Price for cream cheese: $1.25
#   Sales tax rate: 6%
import datetime

############## define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .06
PR_BAGEL = 2.25
PR_CREAMCH = 1.25

# define global variables
num_bagel = 0
num_creamch = 0
subtotal = 0
sales_tax = 0
total = 0

############## define program functions ################
def main():
    get_user_data()
    perform_calculations()
    display_results()

def get_user_data():
    global num_bagel, num_creamch
    num_bagels = int(input("Number of bagels: "))
    num_creamch = int(input("Number of cream cheese: "))

def perform_calculations():
    global cost_bagels, cost_creamch, subtotal, sales_tax, total
    cost_bagels = num_bagels * PR_BAGEL
    cost_creamch = num_creamch * PR_CREAMCH
    subtotal = cost_bagels + cost_creamch
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('------------------------------')
    print('BROWNSVILLE BAGEL COMPANY')
    print('Fresh-baked bagels every day')
    print('------------------------------')
    print('Bagels      $ ' + format(cost_bagels,'8,.2f')
    print('Bagels      $ ' + format(cost_creamch)      
    print('------------------------------')
    print('Subtotal    $ ' + format(subtotal))
    print('Sales Tax    $ ' + format(sales_tax))
    print('Total        $ ' + format(total))
    print('------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ############
main()
