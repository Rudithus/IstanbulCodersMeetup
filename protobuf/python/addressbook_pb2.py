# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: addressbook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='addressbook.proto',
  package='IstanbulCoders.Meetup.Protobuf',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x61\x64\x64ressbook.proto\x12\x1eIstanbulCoders.Meetup.Protobuf\"_\n\x06Person\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12;\n\x06Phones\x18\x03 \x03(\x0b\x32+.IstanbulCoders.Meetup.Protobuf.PhoneNumber\"V\n\x0bPhoneNumber\x12\x0e\n\x06Number\x18\x01 \x01(\t\x12\x37\n\x04Type\x18\x02 \x01(\x0e\x32).IstanbulCoders.Meetup.Protobuf.PhoneType\"E\n\x0b\x41\x64\x64ressBook\x12\x36\n\x06People\x18\x01 \x03(\x0b\x32&.IstanbulCoders.Meetup.Protobuf.Person*+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\x62\x06proto3')
)

_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='IstanbulCoders.Meetup.Protobuf.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=309,
  serialized_end=352,
)
_sym_db.RegisterEnumDescriptor(_PHONETYPE)

PhoneType = enum_type_wrapper.EnumTypeWrapper(_PHONETYPE)
MOBILE = 0
HOME = 1
WORK = 2



_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='IstanbulCoders.Meetup.Protobuf.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='IstanbulCoders.Meetup.Protobuf.Person.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Name', full_name='IstanbulCoders.Meetup.Protobuf.Person.Name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Phones', full_name='IstanbulCoders.Meetup.Protobuf.Person.Phones', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=148,
)


_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='IstanbulCoders.Meetup.Protobuf.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Number', full_name='IstanbulCoders.Meetup.Protobuf.PhoneNumber.Number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='IstanbulCoders.Meetup.Protobuf.PhoneNumber.Type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=236,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='IstanbulCoders.Meetup.Protobuf.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='People', full_name='IstanbulCoders.Meetup.Protobuf.AddressBook.People', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=307,
)

_PERSON.fields_by_name['Phones'].message_type = _PHONENUMBER
_PHONENUMBER.fields_by_name['Type'].enum_type = _PHONETYPE
_ADDRESSBOOK.fields_by_name['People'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['PhoneNumber'] = _PHONENUMBER
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
DESCRIPTOR.enum_types_by_name['PhoneType'] = _PHONETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:IstanbulCoders.Meetup.Protobuf.Person)
  ))
_sym_db.RegisterMessage(Person)

PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
  DESCRIPTOR = _PHONENUMBER,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:IstanbulCoders.Meetup.Protobuf.PhoneNumber)
  ))
_sym_db.RegisterMessage(PhoneNumber)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESSBOOK,
  __module__ = 'addressbook_pb2'
  # @@protoc_insertion_point(class_scope:IstanbulCoders.Meetup.Protobuf.AddressBook)
  ))
_sym_db.RegisterMessage(AddressBook)


# @@protoc_insertion_point(module_scope)