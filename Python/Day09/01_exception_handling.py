# Exception = An envent that interrupt flow of the program
#             (ZeroDivisonError, TypeError, ValueError)
#             1. try, 2. except, 3. finally

try:
    num = int(input("Enter a number: "))
    print(1 / num)

except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong!")
finally:
    print("Thank You!")