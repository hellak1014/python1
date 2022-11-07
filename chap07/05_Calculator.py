class Calculator:
    text_list = []

    @staticmethod
    def plus(x1, x2):
        return x1 + x2

    @staticmethod
    def minus(x1, x2):
        return x1 - x2

    @staticmethod
    def multiply(x1, x2):
        return x1 * x2

    @staticmethod
    def divide(x1, x2):
        return x1 / x2

if __name__ == '__main__':
    print('{0} + {1} = {2}' .format(7, 4, Calculator.plus(7, 4)))
    print('{0} - {1} = {2}'.format(7, 4, Calculator.minus(7, 4)))
    print('{0} * {1} = {2}'.format(7, 4, Calculator.multiply(7, 4)))
    print('{0} / {1} = {2}'.format(7, 4, Calculator.divide(7, 4)))