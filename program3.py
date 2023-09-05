def ask_for_input():
    number_picked = input("Pick a number: ")
    return number_picked
    
def echo_user_input(x):
    print (x)
    
def add_two_numbers(x,y):
    z = int(x) + int(y)
    print(z)

def multiply_three_numbers(x,y,z):
    a = int(x) * int(y) * int(z)
    return(a)
    #Comment: It will also work if you use the command return(int(x) * int(y) * int(z))
            
a = ask_for_input()

echo_user_input(a)

a = ask_for_input()
b = ask_for_input()
add_two_numbers(a,b)
#Comment: Can also be done like this: add_two_numbers(ask_for_input(),ask_for_input())