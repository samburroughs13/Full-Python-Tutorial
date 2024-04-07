weight = float(input("Weight: "))
units = input("Lbs or Kg: ")
if units.lower() == "lbs" or units.lower() == "pounds" or units.lower() == "lb" or units.lower() == "pound":
    print(f"You are {(weight / 2.205):,.1f} kg.")
elif units.lower() == "kg" or units.lower() == "kilograms" or units.lower() == "kilogram" or units.lower() == "kilo":
    print(f"You are {(weight * 2.205):,.1f} lbs.")