import BidderList
import SimulateAuction

def main():
    auction = SimulateAuction.AuctionSimulation(5, 1)
    auction.print_auction_details()

if __name__ == "__main__":
    main()