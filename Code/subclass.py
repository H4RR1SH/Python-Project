import pickle

from main import AdAnalytic

class NativeAdAnalytic(AdAnalytic):
    def __init__(self, date, tag, sub_type, rating, cost, predicted_ctr):
        super().__init__(date, tag, sub_type, "Native", rating, cost, predicted_ctr)


class NonNativeAdAnalytic(AdAnalytic):
    def __init__(self, date, tag, sub_type, rating, cost, predicted_ctr):
        super().__init__(date, tag, sub_type, "non-Native", rating, cost, predicted_ctr)


class InApp(NativeAdAnalytic):
    def __init__(self, date, tag, rating, cost, predicted_ctr):
        super().__init__(date, tag, "InApp", rating, cost, predicted_ctr)


class Banner(NonNativeAdAnalytic):
    def __init__(self, date, tag, rating, cost, predicted_ctr):
        super().__init__(date, tag, "Banner", rating, cost, predicted_ctr)


class Interstitial(NonNativeAdAnalytic):
    def __init__(self, date, tag, rating, cost, predicted_ctr):
        super().__init__(date, tag, "Interstitial", rating, cost, predicted_ctr)



f = open('data.csv','w')
f.write("unique_id,date,tag,sub_type,type,rating,cost,predicted_ctr\n")

o = open('AdAnalyticpkl638200305.dat', 'rb')
objects = pickle.load(o)
for obj in objects:
    f.write(str(obj)+'\n')
o.close()
f.close()

