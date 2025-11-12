# lib/control_flow.py

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature <= 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    is_fizz = num % 3 == 0
    is_buzz = num % 5 == 0

    if is_fizz and is_buzz:
        return "FizzBuzz"
    elif is_fizz:
        return "Fizz"
    elif is_buzz:
        return "Buzz"
    else:
        return num

import sys

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
