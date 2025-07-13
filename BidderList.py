import Distribution
import Bidder
class BidderList:
    def __init__(self):
        self.bidders = []
        self.current_id_count = 0
        self.distribution = Distribution("equal_revenue")

    def add_n_bidders(self, n):
        for _ in range(n):
            self.add_extra_real_bidder()

    def add_extra_real_bidder(self):
        new_bidder = Bidder(self.current_id_count, self.istribution.sample())
        self.bidders.append(new_bidder)
        self.current_id_count += 1

    def add_extra_fake_bidder(self):
        new_bidder = Bidder(self.current_id_count, self.distribution.sample())
        self.bidders.append(new_bidder)
        self.current_id_count += 1