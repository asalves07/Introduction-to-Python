def fizzbuzz(x):
    if(((x%5)==0) and ((x%3)==0)):
        return "FizzBuzz"
    else: 
        if((x%3)==0):
            return "Fizz"
        else:
            if((x%5)==0):
                return "Buzz"
            else:
                return x
