# Book Class Project

This project demonstrates basic object-oriented programming (OOP) concepts in Python using a `Book` theme.

It includes:
- Class creation
- Constructors
- Attributes and methods
- Inheritance
- Polymorphism

## Classes

### 1. `Book` (Base Class)
Represents a general book with basic information.

**Attributes:**
- `title`: Title of the book
- `author`: Author of the book
- `genre`: Genre of the book

**Methods:**
- `describe()`: Prints a short description of the book
- `read()`: Generic read message

### 2. `EBook` (Subclass of Book)
Represents an electronic book with an additional file size.

**Extra Attribute:**
- `file_size`: Size in MB

**Overrides:**
- `read()`: Displays a message for reading an eBook

### 3. `AudioBook` (Subclass of Book)
Represents an audiobook with an additional duration.

**Extra Attribute:**
- `length`: Length of the audio in minutes

**Overrides:**
- `read()`: Displays a message for playing an audiobook

