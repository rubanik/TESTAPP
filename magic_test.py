class MagicTest():

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return 'Hey you use the __str__ magic'


if __name__ == '__main__':

    magic = MagicTest()

    print(magic)