import BidderList


class AuctionSimulation:
    def __init__(self, amount_of_bidders, reserve_price):
        self.bidder_list = BidderList.BidderList(reserve_price)
        self.bidder_list.add_n_bidders(amount_of_bidders)
        
    def get_revenue(self):
        highest_bid = 0
        second_highest_bid = 0
        for bidder in self.bidder_list.bidders:
            if bidder.value > highest_bid:
                second_highest_bid = highest_bid
                highest_bid = bidder.value
            elif bidder.value > second_highest_bid:
                second_highest_bid = bidder.value
        return highest_bid - second_highest_bid
    
    def print_auction_details(self):
        print("Total Revenue: ", self.get_revenue())
        for bidder in self.bidder_list.bidders:
            print(f"Bidder ID: {bidder.id}, Value: {bidder.value}")