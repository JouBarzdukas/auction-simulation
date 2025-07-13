import BidderList


class AuctionSimulation:
    def __init__(self, amount_of_bidders, reserve_price):
        self.bidder_list = BidderList.BidderList(reserve_price)
        self.bidder_list.add_n_bidders(amount_of_bidders)
        self.highest_bidder_id = 0
        self.second_highest_bidder_id = 0
        self.highest_price = -1
        self.second_highest_price = -1
        self.get_highest_bidders()

    def get_highest_bidders(self):
        for bidder_id in self.bidder_list.bidders:
            bidder = self.bidder_list.get_bidder_by_id(bidder_id)
            if bidder.value > self.highest_price:
                self.second_highest_price = self.highest_price
                self.second_highest_bidder_id = self.highest_bidder_id
                self.highest_price = bidder.value
                self.highest_bidder_id = bidder.id
            elif bidder.value > self.second_highest_price:
                self.second_highest_price = bidder.value
                self.second_highest_bidder_id = bidder.id


    
    def print_auction_details(self):
        print(f"Auction Winner: {self.highest_bidder_id}, Won with bid: {self.highest_price}, At price: {self.second_highest_price}")
        print("Profit to be made: ", self.profit_to_be_made())
        print("----------")
        print("Bidders:")
        for bidder_id in self.bidder_list.bidders:
            bidder = self.bidder_list.get_bidder_by_id(bidder_id)
            print(f"Bidder ID: {bidder.id}, Value: {bidder.value}")
    
    def profit_for_auctioneer(self):
        return self.second_highest_price
    
    def profit_to_be_made(self):
        return self.highest_price - self.second_highest_price