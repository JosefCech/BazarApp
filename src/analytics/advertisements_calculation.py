from src.data.models.business.advertisement_resource import AdvertisementResource


class AdvertisementsCalculation():

    def sum_of_original_prices(self, items: list, ratio: int = 1):
        if not items:
            return 0
        return sum([x.originalPrice if x.originalPrice else x.givenPrice/ratio for x in items])

    def sum_of_bought_prices(self, items, ratio: int = 1):
        if not items:
            return 0
        return sum([x.boughtPrice if x.boughtPrice else x.givenPrice/ratio for x in items])

    def sum_of_given_prices(self, items):
        if not items:
            return 0
        return sum([x.givenPrice for x in items])

    def average_return_back_in_percent(self, items):
        if not items:
            return 0
        return sum([x.givenPrice / x.boughtPrice for x in items]) / len(items)

    def average_loss_against_new_in_percent(self, items):
        if not items:
            return 0
        return sum([x.givenPrice / x.originalPrice for x in items]) / len(items)
