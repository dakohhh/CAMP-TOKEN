import random



def generate_number(length):
    
    length = length - 1

    num = random.randint(10**(length - 1), 10**(length)-1)
    return (4 * (10**length)) + num







