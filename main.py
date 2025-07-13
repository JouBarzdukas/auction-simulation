import BidderList

def main():
    bidder_list = BidderList.BidderList()
    bidder_list.add_n_bidders(5)

    for bidder in bidder_list.bidders:
        print(f"Bidder ID: {bidder.id}, Value: {bidder.value}")

if __name__ == "__main__":
    main()