import random
import uuid
from secrets import token_hex
from user.models import User






def generate_wallet_id()-> int:
    while True:
        num = random.randint(4000000000, 4999999999)

        if not User.objects.filter(wallet_id=num).exists():
            return num



def generate_verification_token() -> str:

    return str(uuid.uuid4())




