class OperatingSystem:
    multitasking = True
    name = "Mac OS"
class Apple:
    name = "Apple Inc."
    contactWebsite = "www.apple.com/contact"


class MacBook(Apple, OperatingSystem):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system. Visit {} for more details".format(self.contactWebsite))
            print("Name: ", self.name)

product = MacBook()
