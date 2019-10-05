x=42
y=0

print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print('not allowed to divide by zero')
else:
    print('something went wrong')
# finally:
#     print('this is our clean up code')

print()
