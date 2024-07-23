# Update Tuples
# Change Tuple Values → Converta para list e depois converta de volta para tupla

tupla=("um", "dois", "tres")
lista=list(tupla)
lista[2] = "dez"
print(lista)
tupla=tuple(lista)
print(tupla, type(tupla))

# Add Items
# 1. Convert into a list
num=("um", "dois", "tres")
novo=list(num)
novo.append("quatro")
num=tuple(novo)
print(num, type(num))

# 2. Add tuple to a tuple
t1=("um","dois","tres")
t2=("quatro",)
t1+=t2
print(t1)

# Remove Items
t1List = list(t1)
t1List.remove("quatro")
t1=tuple(t1List)
print(t1, type(t1))

# del → delete the tuple completely
del t1
print(t1) # Error → name 't1' is not defined