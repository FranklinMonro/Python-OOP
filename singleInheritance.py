class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contacDetails(self):
        print("To contact us, log on to ", self.contactWebsite)


class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print("This MacBook was manufacturered in the year {} by {}".format(self.yearOfManufacture, self.manufacturer))



product = MacBook()
product.contacDetails()
product.manufactureDetails()
