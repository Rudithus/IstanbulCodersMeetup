import addressbook_pb2
import sys

def ListPeople(address_book):
  for person in address_book.People:
    print("Person ID:", person.Id)
    print("  Name:", person.Name)

    for phone_number in person.Phones:
      if phone_number.Type == addressbook_pb2.MOBILE:
        print("  Mobile phone #:", end=" ")
      elif phone_number.Type == addressbook_pb2.HOME:
        print("  Home phone #:", end=" ")
      elif phone_number.Type == addressbook_pb2.WORK:
        print("  Work phone #:", end=" ")
      print(phone_number.Number)

address_book = addressbook_pb2.AddressBook()
with open("../Addressbook.dat", "rb") as f:
  address_book.ParseFromString(f.read())

ListPeople(address_book)