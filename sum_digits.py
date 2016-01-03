def digit_sum(n):
    arr = []
    arr1 = []
    count = 0 
    n = str(n) #converts input n into string
    arr.append(n) # appends string n into emptry array
    for x in arr[0]: #appends each letter of str n into arr1
        arr1.append(x)
    while count < len(arr1):  #loops through arr1 and converts each char into int
        arr1[count] = int(arr1[count])
        count+=1   # increments count
    return sum(arr1)  # returns sum of the digits of n
