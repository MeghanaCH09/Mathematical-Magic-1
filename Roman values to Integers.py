def roman_value(r):
    roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    integerformat=0
    for i  in range(len(r)):
        if i+1<len(r) and roman[r[i]]<roman[r[i+1]]:
            integerformat=roman[r[i]]
        else:
            integerformat+=roman[r[i]]
    return integerformat

r=input("Enter a Roman Number: ")
print(f"The integer form of {r} is {roman_value(r)}")
