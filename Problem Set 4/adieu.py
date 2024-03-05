"""
In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs
control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with
one and, three names with two commas and one and, and
 names with
 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""
import sys
import inflect

p = inflect.engine()
given_names = []
# Check if input = ctrl-d else keep asking for input while saving each input into a list
while True:
    try:
        names = (input("Name: "))
        given_names.append(names)
    except EOFError:
        break
# Inflect method for joining words into a list and outputting how we want it
mylist = p.join(given_names)
print("Adieu, adieu, to ", mylist)
