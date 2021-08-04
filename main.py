"""
Week 3, Question 3 Homework
Your friend works for an antique book shop that sells books between
1800 and 1950 and wants to quickly categorise books by the century
and decade that they were written.
Write a program that takes a year (e.g. 1872) and
outputs the century and decade (e.g. "Eighteenth Century, Seventies")
"""

pub_date = int(input("In what year was the book published? "))

if pub_date >= 1800 and pub_date < 1900:
    print("This book was written in the Nineteenth Century.")

elif pub_date >= 1900 and pub_date < 1951:
    print("This book was written in the Twentieth Century.")

else:
    print("This book shouldn't be sold here.")

if str(pub_date)[2] == "0":
    print("In the Noughts.")

elif str(pub_date)[2] == "1":
    print("In the Tens.")

elif str(pub_date)[2] == "2":
    print("In the Twenties.")

elif str(pub_date)[2] == "3":
    print("In the Thirties.")

elif str(pub_date)[2] == "4":
    print("In the Forties.")

elif str(pub_date)[2] == "5":
    print("In the Fifties.")

elif str(pub_date)[2] == "6":
    print("In the Sixties.")

elif str(pub_date)[2] == "7":
    print("In the Seventies.")

elif str(pub_date)[2] == "8":
    print("In the Eighties.")

elif str(pub_date)[2] == "9":
    print("In the Nineties.")
