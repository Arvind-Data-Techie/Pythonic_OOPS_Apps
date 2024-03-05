class Bill:
    """
    Object that contains data about the bill, which is total amount and the period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object to Hold Flatmates name, Number of days stayed and o calculate the bill amount.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay_bill(self, bill,flatmate2):

        flatmate_amount=bill.amount*(self.days_in_house/(self.days_in_house+flatmate2.days_in_house))
        return flatmate_amount