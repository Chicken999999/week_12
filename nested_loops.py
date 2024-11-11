# nested loops = A loop within another loop (outer, inner)
# outer:
#     inner:


rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):   
        print(symbol, end="-")   # puts them all in the same line with a seperator
    print() # seperates them into their own line when printed

