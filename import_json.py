import json

file=open('./Contacts.json', 'r')
data: list = json.load(file)

# new_contact = {
#     "name": "Jane Smith",
#     "email": "jane.smith@example.com",
#     "phone": "098-765-4321"
# }


# data.append(new_contact)

# file_out=open('./contacts.json', 'w',encoding='utf-8')
# json.dump(data, file_out)



def read_json(contact_file):
    with open(contact_file, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json(contact_file, data):
    with open(contact_file, 'w', encoding='utf-8') as file:
        json.dump(data, file)

def find_Contact(contact_file, name):
    contacts = read_json(contact_file)
    for contact in contacts:
        if contact['name'] == name:
            return contact
        else:
            return None

print(find_Contact('./contacts.json', 'Jane Smith'))
#write_json('./contacts.json','    [{"name": "Dark vador", "email": "facedebook.com", "phone": "098-765-4321"}]')
#read_json('./contacts.json')
