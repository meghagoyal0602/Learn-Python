
# 1st method used dict
christopher={}
christopher['first']='christopher'
christopher['last']='harrison'
# 2nd method used dictionary
susan={'first':'Susan','last':'Ibach'}
print()
# print(christopher) using dict
# print(susan) using dict
people = [christopher,susan]  # using list
people.append({'first':"bill",'last':'gates'})
print(people)
presenters=people[0:2]
print(presenters)