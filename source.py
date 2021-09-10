def game(number):
    first, second = int(str(number)[0]),int(str(number)[1])
    if(second>=first):
        return second - first
    else:
        return first - second
