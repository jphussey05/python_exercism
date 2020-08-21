
class Robot:
    def __init__(self):
        self.name = self.__generate_name()
        
    def __generate_name(self):
        from random import randint


        a = chr(randint(65, 90))
        b = chr(randint(65, 90))
        c = str(randint(0,999))

        return f"{a}{b}{c:>03}"

    def reset(self):
        prev_name = self.name

        while prev_name == self.name:
            self.name = self.__generate_name()
