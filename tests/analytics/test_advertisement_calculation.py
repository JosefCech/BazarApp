from src.analytics.advertisements_calculation import AdvertisementsCalculation
from src.data.models.business.advertisement_resource import create_dummy_advertisement_resource


def test_calculation_sum():
    origin_item = create_dummy_advertisement_resource()
    origin_item.givenPrice = 1
    list_items = [origin_item, origin_item, origin_item]

    calculation = AdvertisementsCalculation()
    assert calculation.sum_of_given_prices(list_items) == len(list_items)*origin_item.givenPrice
    assert calculation.sum_of_bought_prices(list_items) == len(list_items) * origin_item.boughtPrice
    assert calculation.sum_of_original_prices(list_items) == len(list_items) * origin_item.originalPrice

