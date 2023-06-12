#Ex1: create dict
student_name = { 'sham': 10, 'nil': 30, 'veer': 40, 'ram': 50}

#for loop for getting first key
for new_s, new_val in student_name.items():
#print first key
	print(new_val)
#after getting first key break loop

#Ex2
dict1={'USD':'Dollar','EUR':'Euro', 'GBP':'Pound', 'INR':'Rupee'}
#Soln 1
print(list(dict1.keys())[list(dict1.values()).index("Pound")])
print(list(dict1.values())[list(dict1.keys()).index("GBP")])
print(list(dict1.values())[0])#Dollar
#Soln 2
def return_key(val):
    for key, value in dict1.items():
        if value ==val:
            return key
return_key('Dollar')
print(return_key("Dollar"))
#soln 3
def get_value():
    for i in list(dict1.keys)[i]:
        if 