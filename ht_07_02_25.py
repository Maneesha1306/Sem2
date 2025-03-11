def num_to_words(n):
    ones=["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens=["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen","Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens=["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    if n==0:
        return "Zero"
    elif n<10:
        return ones[n]
    elif n<20:
        return teens[n-10]
    elif n<100:
        return tens[n//10]+(" " +ones[n%10] if n%10!=0 else "")
    elif n<1000:
        return ones[n//100]+" Hundred"+(" " +num_to_words(n%100) if n%100!=0 else "")
    elif n < 1000000:
        return num_to_words(n//1000)+"Thousand"+(" "+num_to_words(n%1000) if n%1000!=0 else "")
    else:
        return "Number too large"
num=int(input("Enter a number: "))
print(num_to_words(num))

n=int(input("Enter a number: "))
count=0
for i in range(5,n+1,5):
    j=i
    while j%5==0:
        count+=1
        j//=5
print("Trailing zeros in", n,"factorial:",count)