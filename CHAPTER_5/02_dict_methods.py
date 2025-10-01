d = {} # Empty dictionary

marks = {
  "Kushal":100,
  "Shubham":60,
  "Rohan":34,
  0: "kushal"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Kushal":99, "Renuka":100})
# print(marks)

print(marks.get("Kushal")) # Prints None
print(marks["Kushal"])  # Returns Error