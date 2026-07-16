# data types in python 
a = 1
b = 1
print(a+b) 
print(type(a)) # checking data type: integer
r=2
s=4
print(r+s)
print(type(r))

c = "1"
d = "1"
print(c+d)
print(type(c)) # checking data type: string
e="1"
f="1"
print(e+f)
print(type(f))

# basic data types in python: 
# 1. Numeric 
a1 = 1       #1a. integer 
a2 = 1.5     #1b. float
print(type(a2)) 
a3 = complex(3,5) #1c. complex  
print(type(a3))

r1=1
r2=1.4
print(type(r2))

r3= complex(4,5)
print(type(r3))

#2. Sequence 
b1 = "Madhav" #2a. string
b11 = '26'
print(type(b1))
b2 = [1,4,7,26,108,'Madhav'] #2b. list 
print(type(b2))
r1=[1,3,4,5,109,'rizwan']
print(type(r1))
b3 = (1,4,7,26,108,'Madhav') #2c. tuple 
print(type(b3))
r2=(1,2,34,54,'rizwan')
print(type(r2))

#3. Dictionary 
my_dictionary = {'name': 'Rishabh', 'age': 26, 'city': 'Prayagraj'}
print(type(my_dictionary))
dictionary={'name':'rizwan','age':26,'city':'nawabshah'}
print(type(dictionary))

#4. Sets 
my_sets = {1,4,7,26,108,'Madhav'} 
print(type(my_sets))
_set={1,3,4,5,3,5,'rizwan'}
print(type(_set))

# # #5. Boolean 
bool1 = True 
bool2 = False 
print(type(bool1))

# # #6. Binary 
# bytes, bytearray, memoryview 
byte1 = b"Madhav" 
print(type(byte1))
