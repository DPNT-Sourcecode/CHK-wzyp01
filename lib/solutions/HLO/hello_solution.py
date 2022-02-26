

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if not isinstance(friend_name, str):
        raise TypeError("friend_name must be an integer")

    return "Hello, {}!".format(friend_name)

if __name__ == "__main__":
    print(hello("John"))
    print(hello(["john"]))


