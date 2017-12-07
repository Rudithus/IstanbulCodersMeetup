using System.Threading.Tasks;
using System.Collections.Generic;
using IstanbulCoders.Meetup.Grpc;
using Grpc.Core;
public class AddressBookServerImpl : PhoneBookService.PhoneBookServiceBase
{
    public List<Person> People { get; set; }
    public AddressBookServerImpl()
    {
        People = new List<Person>();
    }
    public override Task<AddPersonReply> AddPerson(Person request, Grpc.Core.ServerCallContext context)
    {
        People.Add(request);
        return Task.FromResult(new AddPersonReply { Id = People.Count });
    }
    public override Task<AddressBook> GetPhoneBook(Empty request, Grpc.Core.ServerCallContext context)
    {
        return Task.FromResult(new IstanbulCoders.Meetup.Grpc.AddressBook { People = { People } });
    }
}
