#!/usr/bin/python3

def deposit():
    while True:
        amount = input("What would you like to be deposited $? ")
        if amount.is_digit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    return amount