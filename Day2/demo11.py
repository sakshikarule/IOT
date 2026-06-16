#   for loop_var in collection:
#       statement(s)

#   for loop_var in collection:
#       statement(s)
#   else:
#       statement(s)
str1 ="sunbeam Infotech"

print("str1 = ", end="")
for ch in str1:
    print(ch, end="")
else:
    print("\nstring is finished")

count = 0
for ch in str1:
    count += 1
else:
    print(f"str Length = {count}")

print(f"len(str1) = {len(str1)}")                