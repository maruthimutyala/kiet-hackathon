# import library
import math, random


# function to generate OTP
def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = "6301577323"
    OTP = ""

    # length of password can be changed
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


# Driver code
if _name_ == "_main_":
    print("OTP of 4 digits:", generateOTP())

# import library
import math, random


# function to generate OTP
def generateOTP():
    # Declare a string variable
    # which stores all string
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6):
        OTP += string[math.floor(random.random() * length)]

    return OTP


# Driver code
if _name_ == "_main_":
    print("OTP of length 6:", generateOTP())

# Importing random to generate
# random string sequence
import random

# Importing string library function
import string


def rand_pass(size):
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                           string.ascii_lowercase +
                                           string.digits)
                             for n in range(size)])

    return generate_pass


# Driver Code
password = rand_pass(10)
print(password)