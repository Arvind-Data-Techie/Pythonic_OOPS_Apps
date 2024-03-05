class Paint:

    def __init__(self, buckets, color): # Or get house area and height
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19

class DiscountedPaint(Paint):

    def discounted_price(self,discount_percentage):
        original_price=super().total_price()
        print(original_price)
        return original_price*(100-discount_percentage)/100

paint=Paint(100,'white')
original_price=paint.total_price()
discount_percentage=20
discounted_price=DiscountedPaint(100,'white').discounted_price(discount_percentage)
print("original_price",original_price)
print("discounted_price",discounted_price)













