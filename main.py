class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

Contact1=Contact("John Doe", "john.doe@example.com", "123-456-7890")
print(Contact1)