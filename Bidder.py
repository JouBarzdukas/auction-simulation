class Bidder:
    def __init__(self, id, value, bidder_type="real"):
        self.id = id
        self.value = value
        self.bidder_type = bidder_type
        self.revealed = False
        self.paid_fine = 0.0

    def decide_reveal(self, current_highest, fine):
        if self.bidder_type in {"real", "reserve"}:
            return True
        return self.value < current_highest
