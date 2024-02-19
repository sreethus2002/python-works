lst=[2,3,4,5]
squares=[num**2 for num in lst]
print(squares)

#cube

cube=[num**3 for num in lst]
print(cube)

#add two numbers

add_two=[num+2 for num in lst]
print(add_two)



#print even numbers

evens=[num for num in lst if num %2==0]
print(evens)

#print odd numbers


odds=[num for num in lst if num %2!=0]
print(odds)

#print leep yr

#1800 to 2024



years=[ y for y in range(1800,2024)]
print(years)

#centuary  yr

centuary_years=[y for y in years if y%100==0]
print(centuary_years)

leap_years=[y for y in years if (y%100==0 and y%400==0) or(y%100!=0 and y%4==0)]
print(leap_years)