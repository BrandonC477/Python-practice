import sys

celsius = None
if(len(sys.argv) < 2):
    print("Please provide a temperature in celsius")
    sys.exit()
else:
    celsius = float(sys.argv[1])

fahrenheit = celsius * 1.8 + 32

print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")