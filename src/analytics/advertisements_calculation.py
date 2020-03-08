from src.data.models.business.advertisement_resource import AdvertisementResource


class AdvertisementsCalculation():

    def sum_of_orginal_prices(self, items: list, ratio: int = 1):
        return sum([x.original_price if x.original_price else x.given_price/ratio for x in items])

    def sum_of_bought_prices(self, items, ratio: int = 1):
        return sum([x.bought_price if x.bought_price else x.given_price/ratio for x in items])

    def sum_of_given_prices(self, items):
        return sum([x.given_price for x in items])

    def average_return_back_in_percent(self, items):
        return sum([x.given_price / x.bought_price for x in items]) / len(items)

    def average_loss_against_new_in_percent(self, items):
        return sum([x.given_price / x.original_price for x in items]) / len(items)
