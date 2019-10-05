country= input('which country u live in?')

tax=0
if country=='canada':
    province=input('which province u live in?')
    if province in('alberta','nunavat','quebec'):
      tax=0.05   
    elif province=='ontario':
      tax=0.10
    else:
      tax=0.25
else:
   tax=0
print(tax)
