# variables: piece of space where we can store information

# examples
age = 12
name = "fred"
temp = 48.0
is_ok = True
uh_oh = None #none

# variable types
print(type(age))
print(type(name))
print(type(temp))
print(type(is_ok))
print(type(uh_oh))

# casting: changing variable type
age = "12"
int(age)

#quite common statements kind of nested with each other
print(type(float(age)))

#can declare multiple variables at te same time
x, y, z = 12, "drum", 56.5
print(x, y, z)

#string variable
my_name = "fred"
my_age = 45

myfs = f"{}" # curly braces placeholder for variable 
# / scaping

print(my_name, "no", my_age, "ssd")
