class Bidder:
    def __init__(self, id, value, bidder_type="real"):
        self.id = id
        self.value = value
        self.bidder_type = bidder_type 
        # Real OR "Auctioneer" for bidder_type