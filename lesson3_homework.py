# 1: Amount of euro after commission
nis = float(input("Enter amount of nis:"))
rate = float(input("Enter rate of euro:"))
commission_percent = float(input("Enter commission percent:"))

euro_before_commission_percent = nis / rate
commission_amount = euro_before_commission_percent * (commission_percent / 100)
euro_after_commission = euro_before_commission_percent - commission_amount

print("Amount of euro after commission:", euro_after_commission, "nis")


# 2: output: My name is Alina
def f1():
    print("name", end=" ")

def f2():
    print("My", end=" ")

def f3():
    print("is", end=" ")

def f4():
    print("Alina")
# function call
f2()
f1()
f3()
f4()

# 3: output:
# to be
#      or not
#            to be?

def f1():
    print("be")

def f2():
    print("to", end=" ")

def f3():
    print("\tor", end=" ")

def f4():
    print("not")

def f5():
    print("\t\t", end="")

# function call
f2()
f1()
f3()
f4()
f5()
f2()
f1()
