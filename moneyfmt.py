class MoneyFmt:
    def __init__(self, n):
        self.__n = n

    def update(self, new_n):
        self.__n = new_n

    def repr(self):
        return float(self.__n)

    def __str__(self):
        return '${:,.2f}'.format(self.__n)