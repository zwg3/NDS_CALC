class NdsCalc:

    def get_nums_after_decimal(self, num):
        nums_after_decimal = str(num - int(num))[2:]
        return str(nums_after_decimal)

    def round_if_zero_after_decimal(self, num):
        nums_after_decimal = self.get_nums_after_decimal(num)
        if int(nums_after_decimal) == 0:
            num = int(num)
        return num

    def calc_prices(self, input_price_with_nds, t_proc_nds):
        nds_data = (1 + t_proc_nds / 100)
        corrected_price_without_nds = input_price_with_nds / nds_data
        nums_after_decimal = self.get_nums_after_decimal(corrected_price_without_nds)
        if int(nums_after_decimal[0]) >= 5 and len(nums_after_decimal) > 3:
            corrected_price_without_nds = round(corrected_price_without_nds, 1)
        else:
            corrected_price_without_nds = round(corrected_price_without_nds, 2)
        corrected_price_without_nds = self.round_if_zero_after_decimal(corrected_price_without_nds)
        corrected_price_with_nds = corrected_price_without_nds * nds_data
        nums_after_decimal = self.get_nums_after_decimal(corrected_price_with_nds)
        if int(nums_after_decimal[0]) >= 5 and len(nums_after_decimal) > 3:
            corrected_price_with_nds = round(corrected_price_with_nds, 1)
        else:
            corrected_price_with_nds = round(corrected_price_with_nds, 2)
        corrected_price_with_nds = self.round_if_zero_after_decimal(corrected_price_with_nds)
        return [corrected_price_with_nds, corrected_price_without_nds]

    def run_demo(self):
        while True:
            print("Демонстрация функции рассчёта НДС.\nДля выхода введите 'выйти'.\n")
            price = input("Введите цену с НДС: ")
            if price == 'выйти':
                break
            nds = input("Укажите ставку НДС (целым числом): ")
            if nds == 'выйти':
                break
            res = self.calc_prices(float(price), float(nds))
            print(f"Скорректированная цена с НДС: {res[0]}\n"
                  f"Скорректированная цена без НДС: {res[1]}\n")


if __name__ == "__main__":
    test = NdsCalc()
    test.run_demo()
