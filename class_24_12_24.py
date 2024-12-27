def calculate_fare(miles,minutes,surge):
    try:
        if miles<=0 or minutes<=0:
            raise ValueError("Minutes or miles connot be 0 or negative")
        else:
            total= 2.50+(1.50*miles)+(0.25*minutes)
            total*=surge
            return total
    except ValueError as e:
        return e
    
M=float(input("Enter Miles:"))
m=float(input("Enter minutes:"))
s=float(input("Enter surge:"))
print(calculate_fare(M,m,s))