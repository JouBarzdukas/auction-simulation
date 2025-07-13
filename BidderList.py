import Distribution
import Bidder
class BidderList:
    def __init__(self, reserve_price=None):
        self.bidders = []
        self.current_id_count = 0
        self.distribution = Distribution.Distribution("equal_revenue")
        if reserve_price is not None:
            self.add_reserve_price(reserve_price)

    def add_n_bidders(self, n):
        for _ in range(n):
            self.add_extra_real_bidder()

    def add_extra_real_bidder(self):
        new_bidder = Bidder.Bidder(self.current_id_count, self.distribution.sample())
        self.bidders.append(new_bidder)
        self.current_id_count += 1

    def add_extra_fake_bidder(self):
        new_bidder = Bidder.Bidder(self.current_id_count, self.distribution.sample())
        self.bidders.append(new_bidder)
        self.current_id_count += 1
    
    def add_reserve_price(self, reserve_price):
        new_bidder = Bidder.Bidder(-1, reserve_price)
        self.bidders.append(new_bidder)