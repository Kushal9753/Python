try:
    a = int(input("Hey, Enter a no. "))
    print(a)

except ValueError as v:
  print("heyyyy")
  print(v)
except Exception as e:
  print(e)

print("Thank you")