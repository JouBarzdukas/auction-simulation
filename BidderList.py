import Distribution
import Bidder

class BidderList:
    def __init__(self, reserve_price=None):
        self.bidders = {}  # Mapping bidder id to bidder instance
        self.current_id_count = 0
        self.distribution = Distribution.Distribution("equal_revenue")
        if reserve_price is not None:
            self.add_reserve_price(reserve_price)
            self.has_reserve = True
        else:
            self.has_reserve = False

    def add_n_bidders(self, n):
        for _ in range(n):
            self.add_extra_real_bidder()

    def add_extra_real_bidder(self):
        new_bidder = Bidder.Bidder(self.current_id_count, self.distribution.sample())
        self.bidders[self.current_id_count] = new_bidder
        self.current_id_count += 1

    def add_extra_fake_bidder(self):
        new_bidder = Bidder.Bidder(self.current_id_count, self.distribution.sample())
        self.bidders[self.current_id_count] = new_bidder
        self.current_id_count += 1

    def add_reserve_price(self, reserve_price):
        new_bidder = Bidder.Bidder(-1, reserve_price)
        self.bidders[-1] = new_bidder

    def get_bidder_by_id(self, bidder_id):
        return self.bidders.get(bidder_id)