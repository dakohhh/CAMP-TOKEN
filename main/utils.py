import random
from .models import CustomUser




def generate_wallet_id(length):

    while True:
    
        length = length - 1

        num = random.randint(10**(length - 1), 10**(length)-1)

        
        num = (4 * (10**length)) + num


        if not CustomUser.objects.filter(wallet_id=num).exists():

            return num







