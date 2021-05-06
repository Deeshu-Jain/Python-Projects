pi=3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
def number_dec():
    while True:
        try:
            n = int(input("Enter upto which decimal place you want Pi. (0-100): "))
            if n in range(1,101):
                return n
            else:
                print("Limit Exceed! Try Again")
        except:
            print("Invalid Output! Try Again")

print("FINDING PI TO THE Nth DIGIT..\n")
num=number_dec()
print("Pi to the {}th number of decimals is %.{}f".format(num, num) % (pi))