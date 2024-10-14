from main import AdAnalytic

class NativeAdAnalytic(AdAnalytic):
    def __init__(self, date, tag, sub_type, rating, cost, predicted_ctr):
        super().__init__(date, tag, sub_type, "Native", rating, cost, predicted_ctr)


class NonNativeAdAnalytic(AdAnalytic):
    def __init__(self, date, tag, sub_type, rating, cost, predicted_ctr):
        super().__init__(date, tag, sub_type, "Non-Native", rating, cost, predicted_ctr)


class InApp(NativeAdAnalytic):
    def __init__(self, date, tag, rating, cost, predicted_ctr):
        super().__init__(date, tag, "InApp", rating, cost, predicted_ctr)


class Banner(NonNativeAdAnalytic):
    def __init__(self, date, tag, rating, cost, predicted_ctr):
        super().__init__(date, tag, "Banner", rating, cost, predicted_ctr)


class Interstitial(NonNativeAdAnalytic):
    def __init__(self, date, tag, rating, cost, predicted_ctr):
        super().__init__(date, tag, "Interstitial", rating, cost, predicted_ctr)


banner_ad_analytic = Banner("2022-11-15", "tagA", 2, 641, 86.06)
print(banner_ad_analytic)
