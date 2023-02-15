from datetime import datetime

# timestamp = 1672358400000
# date_time = datetime.fromtimestamp(timestamp/1000)
# print(date_time)

import string
import random

def generate_password():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(6))
print(generate_password())