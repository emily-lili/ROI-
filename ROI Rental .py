#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ROI():
    def __init__(self, prop = 0, Income = 0, Expenses = 0, Investment = 0):
        self.prop = prop
        self.Income = Income
        self.Expenses = Expenses
        self.Investment = Investment
        
    def prop(self):
        return int(input("How much was the property originally? "))
    
    def Income(self):
        return int(input("How much is your monthly income? "))

    def Expenses(self):
        Monthly= int(input("How much are your monthly expenses? "))
        insurance = int(input("Enter property insurance: $"))
        hoa = int(input("What are the HOA fees? "))
        utilities = int(input("What are your utilities costs"))
        self.Expenses = Monthly + insurance + hoa + utilities
        print(f"Total Expenses: ${self.Expenses}")

    def Investment(self):
        return int(input("\nHow much have you spent on this property? "))

    def Cash(self):
        return (12 * (self.Income - self.Expenses))
    
    def math(self):
        print(f"\nYour yearly cash flow is: ${self.Cash()}\nYour total investment is: ${self.Investment}")
        roi = 100 * ((self.Cash()) / self.Investment)
        print(f"Your purchased the house for: ${self.prop}\nYour yearly ${self.Cash()}", 
        f"investment on your ${self.Investment} investment is {roi}%")


def main():
    Run = ROI()
    print(f"Hello and welcome to our ROI calculator!")
    start = input("\nPress 'Enter' to continue")
    if start == "":
            Run.prop()
            Run.Income()
            Run.Expenses()
            Run.Investment()
            Run.Cash()
        
    
main()


# In[ ]:




