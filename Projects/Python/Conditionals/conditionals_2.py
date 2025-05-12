age = int(input("How old are you?"))

if age < 18:
  print("You are under 18.")
elif age >= 18 and age < 65:
  print("You are an adult.")
else:
  print("You are a senior.")
