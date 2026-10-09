class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

Contacts=[{"name": "John Doe", "email": "john.doe@example.com", "phone": "123-456-7890"},
         {"name": "Jane Smith", "email": "jane.smith@example.com", "phone": "098-765-4321"},
         {"name": "Alice Johnson", "email": "alice.johnson@example.com", "phone": "555-123-4567"}]
