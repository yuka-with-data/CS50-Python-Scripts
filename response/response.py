""" 
implement a program that prompts the user for an email address via input 
and then prints Valid or Invalid, respectively, 
if the input is a syntatically valid email address. 
You may not use re. 
And do not validate whether the email address’s domain name actually exists.

 """

from validator_collection import validators, checkers, errors

email_input = input("Your Email?: ")
if checkers.is_email(email_input):
    print("Valid")
else:
    print("Invalid")
