using System;
using Grpc.Core;
using IstanbulCoders.Meetup.Grpc;

namespace AddressBook.Server
{
    class Program
    {
        static void Main(string[] args)
        {
            var server = new Grpc.Core.Server()
            {
                Services = { PhoneBookService.BindService(new AddressBookServerImpl()) },
                Ports = { new ServerPort("127.0.0.1", 5000, ServerCredentials.Insecure) }
            };
            server.Start();
            Console.WriteLine($"Listening port 5000");
            Console.ReadKey();
        }
    }
}
