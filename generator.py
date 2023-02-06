import random, string


ids = list(range(64))

def generate_message() -> dict:
    _id = random.choice(ids)

    _message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {'id': _id, 'message': _message}


if __name__ == '__main__':
    print(generate_message())