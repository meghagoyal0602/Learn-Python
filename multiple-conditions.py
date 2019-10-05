# province=input('what province do ulive in?')
# tax=0
# if province=='alberto'or province=='nunavat':
#     tax=0.05
# elif province=='ontario':
#     tax=0.15
# else:
#     tax=0.30
# print(tax)

# using if statment
province=input('what province do ulive in?')
tax=0
if province in('alberto','nunavat','quebec'):
    tax=0.05
elif province=='ontario':
    tax=0.15
else:
    tax=0.30
print(tax)
