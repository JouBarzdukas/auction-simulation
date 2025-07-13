class BidderList:
    def __init__(self):
        self.bidders = []
        self.current_id_count = 0

    def add_n_bidders(self, n):
        for _ in range(n):
            self.add_extra_real_bidder()

    def add_extra_real_bidder(self):
        new_bidder = Bidder(self.current_id_count, distribution(100, 20).sample())
        self.bidders.append(new_bidder)
        self.current_id_count += 1

    ### CHANGE LATER
    def add_extra_fake_bidder(self):
        new_bidder = Bidder(self.current_id_count, distribution(100, 20).sample())
        self.bidders.append(new_bidder)
        self.current_id_count += 1

class Bidder:
    def __init__(self, id, value):
        self.id = id
        self.value = value


class distribution:
    def __init__(self, mean, stddev):
        self.mean = mean
        self.stddev = stddev

    def sample(self):
        import random
        return random.gauss(self.mean, self.stddev)
