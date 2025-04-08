# Smartphone OOP Example

This project demonstrates the use of Object-Oriented Programming (OOP) concepts in Python by modeling a `Smartphone` class and a derived `GamingSmartphone` class.

## Project Structure

- **`smartphone.py`**: Contains the implementation of the `Smartphone` and `GamingSmartphone` classes, along with example usage.

## Classes

### `Smartphone`
Represents a generic smartphone with the following attributes and methods:
- **Attributes**:
  - `brand`: The brand of the smartphone (e.g., Apple, Samsung).
  - `model`: The model of the smartphone (e.g., iPhone 14).
  - `storage`: The storage capacity of the smartphone in GB.
  - `battery_life`: The battery life of the smartphone in hours.
- **Methods**:
  - `call(number)`: Simulates making a call to the specified number.
  - `browse(website)`: Simulates browsing a website.
  - `__str__()`: Returns a string representation of the smartphone.

### `GamingSmartphone`
A subclass of `Smartphone` that adds gaming-specific functionality:
- **Additional Attribute**:
  - `gpu`: The GPU of the gaming smartphone.
- **Additional Method**:
  - `play_game(game)`: Simulates playing a game on the smartphone.
- **Overridden Method**:
  - `__str__()`: Extends the string representation to include GPU information.

## Example Usage

The `smartphone.py` file includes example usage of the classes:

```python
# Creating a generic smartphone
phone = Smartphone("Apple", "iPhone 14", 128, 20)
print(phone)
phone.call("123-456-7890")
phone.browse("www.example.com")

# Creating a gaming smartphone
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, 30, "Adreno 730")
print(gaming_phone)
gaming_phone.play_game("PUBG")
