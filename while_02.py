# Simple Python program to print the simple number pattern  
# Here, we are declaring the integer variable to store the input rows  
rows = int(input("Enter the number of rows: "))    
# Here, we are declaring the for loop that is used to print the number of rows    
for i in range(rows+1):    
# Here, we are declaring the for loop that is used to print the value of i after each iteration    
    for j in range(i):    
        print(i, end=" ")       # Here, we are printing the number in some pattern    
    # Here, this print is used for new line after each row to display pattern correctly    
    print(" ")    