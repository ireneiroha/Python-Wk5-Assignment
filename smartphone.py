# Define the Smartphone class
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        """
        Initialize a Smartphone object with brand, model, storage, and battery life.
        """
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def call(self, number):
        """
        Simulate making a call to the specified number.
        """
        print(f"Calling {number} from {self.brand} {self.model}...")

    def browse(self, website):
        """
        Simulate browsing a website.
        """
        print(f"Browsing {website} on {self.brand} {self.model}...")

    def __str__(self):
        """
        Return a string representation of the Smartphone object.
        """
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery_life} hours battery life."


# Define the GamingSmartphone class, inheriting from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        """
        Initialize a GamingSmartphone object with additional GPU attribute.
        """
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu

    def play_game(self, game):
        """
        Simulate playing a game on the gaming smartphone.
        """
        print(f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU.")

    def __str__(self):
        """
        Return a string representation of the GamingSmartphone object,
        including GPU information.
        """
        return super().__str__() + f" It also has a {self.gpu} GPU."


# Example Usage
# Create a generic smartphone object
phone = Smartphone("Apple", "iPhone 14", 128, 20)

# Create a gaming smartphone object
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, 30, "Adreno 730")

# Print details of the generic smartphone
print(phone)
phone.call("123-456-7890")
phone.browse("www.example.com")

# Print details of the gaming smartphone
print(gaming_phone)
gaming_phone.play_game("PUBG")