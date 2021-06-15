#Dictionary 

x= {'morning':'wake','evening':'snack','noon':'lunch','night':'dinner'}
print(x)
#O/P{'morning': 'wake', 'evening': 'snack', 'noon': 'lunch', 'night': 'dinner'} 

for k,v in x.items():
    print(f'{k}:{v}')
#     morning:wake
# evening:snack
# noon:lunch
# night:dinner
for k in x.keys():
    print(k)
#all the keys
for v in x.values():
    print(v)
#all the values
print(x['morning'])  
#output wake
x['morning']='wakeup'
x['midnoon']='sleep2'
print('morning' in x)  
