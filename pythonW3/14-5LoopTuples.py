# Loop Tuples
t1 = ("um", "dois", "tres","quatro", "cinco")

print("iterate")
for item in t1:
    print("   " + 
          item)

# Loop Through the Index Numbers
print("index")
for i in range(len(t1)):
    print("   " + t1[i])

# Using a While Loop
print("While")
i=0
while i < len(t1):
    print("   " + t1[i])
    i+=1