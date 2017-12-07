mkdir AddressBook.Client
mkdir AddressBook.Server
mkdir AddressBook.Core

dotnet new sln --name AddressBook

Set-Location AddressBook.Client
dotnet new console
Rename-Item Program.cs ClientProgram.cs
dotnet add package Grpc.Core

Set-Location ../AddressBook.Server
dotnet new console
Rename-Item Program.cs ServerProgram.cs
dotnet add package Grpc.Core

Set-Location ../AddressBook.Core
dotnet new classlib
Remove-Item Class1.cs
dotnet add package Grpc
dotnet add package Grpc.Core
dotnet add package Google.Protobuf

Set-Location ..

dotnet sln add AddressBook.Server/AddressBook.Server.csproj
dotnet sln add AddressBook.Client/AddressBook.Client.csproj
dotnet sln add AddressBook.Core/AddressBook.Core.csproj

dotnet add AddressBook.Server/AddressBook.Server.csproj reference AddressBook.Core/AddressBook.Core.csproj
dotnet add AddressBook.Client/AddressBook.Client.csproj reference AddressBook.Core/AddressBook.Core.csproj

protoc --proto_path=. --csharp_out .\AddressBook.Core\ --grpc_out .\AddressBook.Core\ .\addressbook.proto --plugin=protoc-gen-grpc=grpc_csharp_plugin.exe

dotnet build