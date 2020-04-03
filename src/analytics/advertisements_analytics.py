from src.analytics.advertisements_calculation import AdvertisementsCalculation
from src.data.models.business.advertisement_resource import AdvertisementsMetrics, AdvertisementsAnalyticsResponse


class AdvertisementsAnalytics():
    def __init__(self, calculation: AdvertisementsCalculation):
        self._calculation = calculation

    def create_analytics(self, items):
        full_data = [item for item in items if item.originalPrice and item.boughtPrice and item.givenPrice]

        metrics = AdvertisementsMetrics(
            sumGivenPrice=self._calculation.sum_of_given_prices(full_data),
            sumBoughtPrice=self._calculation.sum_of_bought_prices(full_data),
            sumOriginalPrice=self._calculation.sum_of_original_prices(full_data),
            returnValueRatio=self._calculation.average_return_back_in_percent(full_data),
            lossValueRatio=self._calculation.average_loss_against_new_in_percent(full_data)
        )

        metrics_subset = None
        metrics_total = None
        if len(full_data) == len(items):
            metrics_total = metrics
        else:
            metrics_subset = metrics
            metrics_total = AdvertisementsMetrics(
                sumGivenPrice=self._calculation.sum_of_given_prices(items),
                sumBoughtPrice=self._calculation.sum_of_bought_prices(items,
                                                                      ratio=metrics_subset.returnValueRatio if  metrics_subset.returnValueRatio else 1),
                sumOriginalPrice=self._calculation.sum_of_original_prices(items,
                                                                          ratio=metrics_subset.lossValueRatio if metrics_subset.lossValueRatio else 1),
                returnValueRatio=metrics_subset.returnValueRatio,
                lossValueRatio=metrics_subset.lossValueRatio
            )

        response = AdvertisementsAnalyticsResponse(
            totalCount=len(items),
            usedForCalculation=len(full_data),
            totalSumGivenPrice=self._calculation.sum_of_given_prices(items),
            metricsOnSubset=metrics_subset,
            metricsOnTotal=metrics_total,
        )
        return response
