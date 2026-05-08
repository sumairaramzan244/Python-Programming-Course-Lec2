
# variables are used to store data in a program. They are like containers that hold values. In programming, we can assign values to variables and use them later in our code.

pakistan =1947 
india ="14 August"
print(pakistan)
print(india)

# get var in print statement so the computer will print the value of the variable instead of the variable name
print("Pakistan was created in the year",pakistan)

#  we can also print a statement with the variable value by using the + operator to concatenate the string and the variable value. However, we need to convert the variable value to a string using the str() function before concatenating it.
# and also  print a statement that is in the single  quotes and the variable value is in double quotes and it will work fine because the single quotes and double quotes are used to define string literals in Python, and they can be used interchangeably as long as they are properly closed.

print('Pakistan was established in the year ' + str(pakistan))

print("Pakistan was came on the map  in the year " + str(pakistan))

# if we have a number and a string with the same var name then  in print statement it will print the string value because it is the last value assigned to that var name

Ali= 109
Ali="Ali is a good student"
print(Ali)

# casting of variables means it will tell the computer to treat a variable as a different data type

year = int(2447)
month = str("June")
day = float(24.0)
print(year)
print(month)
print(day)


# find type of variables the type() function is used to find the type of variable like string, integer, float etc

print(type(pakistan))
print(type(india))

# case sensitive  language means that the language treats uppercase and lowercase letters as different. For example, in Python, "Pakistan" and "pakistan" are considered different variables because of the case sensitivity.

pakistan =1947 
Pakistan = "Islamic Republic of Pakistan"
print(Pakistan)




