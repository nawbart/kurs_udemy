print("Wpisz słowo: ")
#slowo = str(input(" "))
slowo = "kolokwium"

print(slowo[:1]) #
print(slowo[:-1])


for index,litera in enumerate(slowo):
    print(slowo[:index+1])

for index,litera in enumerate(slowo):
    print(slowo[:-index-1])







