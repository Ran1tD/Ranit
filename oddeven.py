class Numbers:
    def even():
        a=int(input("Enter starting point -> "))
        b=int(input("Enter ending point -> "))
        for x in range(a,b):
            if x%2==0:
                print(x,end=" ")
    def odd():
        x=int(input("Enter starting point -> "))
        y=int(input("Enter ending point -> "))
        for z in range(x,y):
            if z%2==1:
                print(z,end=" ")
print("\t\t------EVEN NUMBERS------")
Numbers.even()
print("\n")
print("\t\t------ODD NUMBERS------")
Numbers.odd()