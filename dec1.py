def decorator(function):
    def wrapper(a,b):
        if isinstance(a,int)==True and isinstance(b,int)==True:
         
            if a<b:
                a,b=b,a
            function(a,b)
        
        elif isinstance(a,int)==False and isinstance(b,int)==False:
            print("i am in first elif")
            a=int(input('enter the a value it must be int only='))
            b=int(input('enter the b value it must be int only='))
            if a<b:
                a,b=b,a
            function(a,b)
        elif isinstance(a,int)==False:
            print("i am insecond elif")
            print("a must be int type ony")
            a=int(input("enter the a value="))
            if a<b:
                a,b=b,a
            function(a,b)
        elif isinstance(b,int)==False:
            print("i am third elif")
            print(b,"must be int ony")
            b=int(input("enter the a value="))
            if a<b:
                a,b=b,a
            function(a,b)
    return wrapper

@decorator
def div(a,b):
    c=a/b
    print("a=",a)
    print('b=',b)
    print(c)
div(2,6)
div("r",6)
div("10","6")