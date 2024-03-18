# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hypernets/dispatchers/process/grpc/proto/proc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hypernets/dispatchers/process/grpc/proto/proc.proto',
  package='hypernets.dispatchers.process.grpc.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3hypernets/dispatchers/process/grpc/proto/proc.proto\x12(hypernets.dispatchers.process.grpc.proto\"c\n\x0eProcessRequest\x12\x0f\n\x07program\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\x12\x0b\n\x03\x63wd\x18\x03 \x01(\t\x12\x13\n\x0b\x62uffer_size\x18\x04 \x01(\x05\x12\x10\n\x08\x65ncoding\x18\x05 \x01(\t\"T\n\x0f\x44ownloadRequest\x12\x0c\n\x04peer\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x13\n\x0b\x62uffer_size\x18\x03 \x01(\x05\x12\x10\n\x08\x65ncoding\x18\x04 \x01(\t\"\xae\x01\n\tDataChunk\x12J\n\x04kind\x18\x01 \x01(\x0e\x32<.hypernets.dispatchers.process.grpc.proto.DataChunk.DataKind\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"G\n\x08\x44\x61taKind\x12\x06\n\x02IN\x10\x00\x12\x07\n\x03OUT\x10\x01\x12\x07\n\x03\x45RR\x10\x02\x12\x08\n\x04\x44\x41TA\x10\n\x12\x07\n\x03\x45ND\x10\x63\x12\x0e\n\tEXCEPTION\x10\x90\x03\x32\x8b\x02\n\rProcessBroker\x12z\n\x03run\x12\x38.hypernets.dispatchers.process.grpc.proto.ProcessRequest\x1a\x33.hypernets.dispatchers.process.grpc.proto.DataChunk\"\x00(\x01\x30\x01\x12~\n\x08\x64ownload\x12\x39.hypernets.dispatchers.process.grpc.proto.DownloadRequest\x1a\x33.hypernets.dispatchers.process.grpc.proto.DataChunk\"\x00\x30\x01\x62\x06proto3')
)



_DATACHUNK_DATAKIND = _descriptor.EnumDescriptor(
  name='DataKind',
  full_name='hypernets.dispatchers.process.grpc.proto.DataChunk.DataKind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA', index=3, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=4, number=99,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCEPTION', index=5, number=400,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=388,
  serialized_end=459,
)
_sym_db.RegisterEnumDescriptor(_DATACHUNK_DATAKIND)


_PROCESSREQUEST = _descriptor.Descriptor(
  name='ProcessRequest',
  full_name='hypernets.dispatchers.process.grpc.proto.ProcessRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='program', full_name='hypernets.dispatchers.process.grpc.proto.ProcessRequest.program', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='hypernets.dispatchers.process.grpc.proto.ProcessRequest.args', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cwd', full_name='hypernets.dispatchers.process.grpc.proto.ProcessRequest.cwd', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buffer_size', full_name='hypernets.dispatchers.process.grpc.proto.ProcessRequest.buffer_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='hypernets.dispatchers.process.grpc.proto.ProcessRequest.encoding', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=196,
)


_DOWNLOADREQUEST = _descriptor.Descriptor(
  name='DownloadRequest',
  full_name='hypernets.dispatchers.process.grpc.proto.DownloadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='hypernets.dispatchers.process.grpc.proto.DownloadRequest.peer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='hypernets.dispatchers.process.grpc.proto.DownloadRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buffer_size', full_name='hypernets.dispatchers.process.grpc.proto.DownloadRequest.buffer_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='hypernets.dispatchers.process.grpc.proto.DownloadRequest.encoding', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=282,
)


_DATACHUNK = _descriptor.Descriptor(
  name='DataChunk',
  full_name='hypernets.dispatchers.process.grpc.proto.DataChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kind', full_name='hypernets.dispatchers.process.grpc.proto.DataChunk.kind', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='hypernets.dispatchers.process.grpc.proto.DataChunk.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATACHUNK_DATAKIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=285,
  serialized_end=459,
)

_DATACHUNK.fields_by_name['kind'].enum_type = _DATACHUNK_DATAKIND
_DATACHUNK_DATAKIND.containing_type = _DATACHUNK
DESCRIPTOR.message_types_by_name['ProcessRequest'] = _PROCESSREQUEST
DESCRIPTOR.message_types_by_name['DownloadRequest'] = _DOWNLOADREQUEST
DESCRIPTOR.message_types_by_name['DataChunk'] = _DATACHUNK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessRequest = _reflection.GeneratedProtocolMessageType('ProcessRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSREQUEST,
  '__module__' : 'hypernets.dispatchers.process.grpc.proto.proc_pb2'
  # @@protoc_insertion_point(class_scope:hypernets.dispatchers.process.grpc.proto.ProcessRequest)
  })
_sym_db.RegisterMessage(ProcessRequest)

DownloadRequest = _reflection.GeneratedProtocolMessageType('DownloadRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADREQUEST,
  '__module__' : 'hypernets.dispatchers.process.grpc.proto.proc_pb2'
  # @@protoc_insertion_point(class_scope:hypernets.dispatchers.process.grpc.proto.DownloadRequest)
  })
_sym_db.RegisterMessage(DownloadRequest)

DataChunk = _reflection.GeneratedProtocolMessageType('DataChunk', (_message.Message,), {
  'DESCRIPTOR' : _DATACHUNK,
  '__module__' : 'hypernets.dispatchers.process.grpc.proto.proc_pb2'
  # @@protoc_insertion_point(class_scope:hypernets.dispatchers.process.grpc.proto.DataChunk)
  })
_sym_db.RegisterMessage(DataChunk)



_PROCESSBROKER = _descriptor.ServiceDescriptor(
  name='ProcessBroker',
  full_name='hypernets.dispatchers.process.grpc.proto.ProcessBroker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=462,
  serialized_end=729,
  methods=[
  _descriptor.MethodDescriptor(
    name='run',
    full_name='hypernets.dispatchers.process.grpc.proto.ProcessBroker.run',
    index=0,
    containing_service=None,
    input_type=_PROCESSREQUEST,
    output_type=_DATACHUNK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='download',
    full_name='hypernets.dispatchers.process.grpc.proto.ProcessBroker.download',
    index=1,
    containing_service=None,
    input_type=_DOWNLOADREQUEST,
    output_type=_DATACHUNK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROCESSBROKER)

DESCRIPTOR.services_by_name['ProcessBroker'] = _PROCESSBROKER

# @@protoc_insertion_point(module_scope)
