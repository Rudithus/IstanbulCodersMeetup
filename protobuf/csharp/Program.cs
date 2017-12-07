using System;
using System.Collections.Generic;
using System.IO;
using Google.Protobuf;
using IstanbulCoders.Meetup.Protobuf;
namespace csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            var phone1 = new PhoneNumber { Number = "123123123", Type = PhoneType.Work };
            var phone2 = new PhoneNumber { Number = "124151231", Type = PhoneType.Mobile };
            var person1 = new Person()
            {
                Id = 1,
                Name = "Name1",
                Phones = { new List<PhoneNumber> { phone1, phone2 } }
            };

            var phone3 = new PhoneNumber { Number = "90989098", Type = PhoneType.Home };
            var person2 = new Person()
            {
                Id = 2,
                Name = "Name2",
                Phones = { new List<PhoneNumber> { phone3 } }
            };

            var AddressBook = new AddressBook { People = { new List<Person> { person1, person2 } } };

            using (var file = File.Create("../Addressbook.dat"))
            {
                AddressBook.WriteTo(file);
            }
        }
    }
}
