import datetime

class MagicTest():

    def __init__(self,name) -> None:
        self.log = 'log'
        self.name = name

    def __str__(self) -> str:
        return 'Hey, you use the __str__ magic'

    def __setattr__(self, name, value):
        print(f"{datetime.datetime.now()} : {name} was changed. The New name is {value}")

if __name__ == '__main__':
    magic = MagicTest('Ui')
    #print(magic)
    magic.name = 'Io'
    magic.name = 'Lui'
    