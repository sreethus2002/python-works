weightin_kg=52
heightin_cm=165
heightin_m=heightin_cm/100
bmi=weightin_kg/heightin_m**2
print(bmi)

if(bmi<20):
    print("underweight")
elif(bmi>=20 and bmi<=24):
    print("normal")    
elif(bmi<=29 and bmi>=25):
    print("over weight")
else:
    print("obesity")
