using System;
using Grpc.Core;
using IstanbulCoders.Meetup.Grpc;
namespace AddressBook.Client
{
    class Program
    {
        static void Main(string[] args)
        {
            var channel = new Channel("127.0.0.1:5000", ChannelCredentials.Insecure);

            var client = new PhoneBookService.PhoneBookServiceClient(channel);
            var person = new Person { Id = 1, Name = "Batman" };
            var person2 = new Person { Id = 2, Name = "Person2" };

            var response = client.AddPerson(person);
            Console.WriteLine($"Person added :{response.Id}");
            var response2 = client.AddPerson(person2);
            Console.WriteLine($"Person added :{response2.Id}");

            var addressBook = client.GetPhoneBook(new Empty());

            foreach (var p in addressBook.People)
            {
                Console.WriteLine($"Id:{p.Id} Name:{p.Name}");
            }
        }
    }
}
