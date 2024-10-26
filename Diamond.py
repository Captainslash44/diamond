rows = int(input("For rows: "))

spaces = rows - 1 #we are required to set a specific number of spaces
            # so that the diamond shape appears
for i in range(1, rows + 1): # the range starts at 1 because the number of stars depends on i
    print(spaces * " " + ((i * 2) - 1) * "*") #this is a formula to set the number of stars
    spaces -= 1 
    
    if i == rows: #once i reaches the maximum of our rows, we need to go backwards
        spaces = 1
        for i in range(rows - 1, 0, -1):
            print(spaces * " " + ((i * 2) - 1) * "*")
            spaces += 1