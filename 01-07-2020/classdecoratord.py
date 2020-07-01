class Shop:
    total_sales = 0
    def __init__(self, anme, sales_number):
        self._name = anme
        self._sales_number = sales_number

    def insrease_sales(self, sales_number):
        self.sales_number +=1

        # Shop.total_sales += 1
        self.__class__.total_sales +=1

    # @staticmethod
    # def insrease_total_sales(sales_number):
    #     Shop.total_sales += 1

    @classmethod
    def insrease_total_sales(cls, sales_number):
        cls.total_sales += 1

shop1 =Shop('Silpo', 4000)
shop2 = Shop('ATB', 8000)

Shop.insrease_total_sales(340)