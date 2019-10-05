# gpa=0
# lowest_grade=0
# if gpa<= 0.85:
#     if lowest_grade>0.70:
#         print('well done')
#     else:
#         print('nothing')


# # using AND
# gpa=float(input('gpa?'))
# # one more way to convert
# lowest_grade = input('lg?')
# lowest_grade = float(lowest_grade)
# if gpa>=0.85 and lowest_grade>=0.70:
#     print('Well done')

# using boolean variable
gpa=float(input('gpa?'))
lowest_grade=float(input('lg?'))
if gpa>=0.85 and lowest_grade>=0.70:
    honour_roll= True
else:
    honour_roll= False
# somewhere later in code
if honour_roll:
    print('welldone')
else:
    print('NOTHING')

