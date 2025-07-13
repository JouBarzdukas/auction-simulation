import BidderList
import SimulateAuction

def main():
    expected_profit = 0
    amount_of_rounds = 1000000
    for _ in range(amount_of_rounds):
        auction = SimulateAuction.AuctionSimulation(1, 1.3)
        expected_profit += auction.profit_for_auctioneer()
    print("Average profit for auctioneer: ", expected_profit / amount_of_rounds)

if __name__ == "__main__":
    main()