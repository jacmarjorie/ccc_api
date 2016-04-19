# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/framespace/framespace_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto.framespace import framespace_pb2 as proto_dot_framespace_dot_framespace__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/framespace/framespace_service.proto',
  package='framespace',
  syntax='proto3',
  serialized_pb=_b('\n)proto/framespace/framespace_service.proto\x12\nframespace\x1a!proto/framespace/framespace.proto\"I\n\x11SearchAxesRequest\x12\r\n\x05names\x18\x01 \x03(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"M\n\x12SearchAxesResponse\x12\x1e\n\x04\x61xes\x18\x01 \x03(\x0b\x32\x10.framespace.Axis\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x86\x01\n\x16SearchKeySpacesRequest\x12\x14\n\x0ckeyspace_ids\x18\x01 \x03(\x05\x12\r\n\x05names\x18\x02 \x03(\t\x12\x12\n\naxis_names\x18\x03 \x03(\t\x12\x0c\n\x04keys\x18\x04 \x03(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\"[\n\x17SearchKeySpacesResponse\x12\'\n\tkeyspaces\x18\x01 \x03(\x0b\x32\x14.framespace.KeySpace\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"J\n\x12SearchUnitsRequest\x12\r\n\x05names\x18\x01 \x03(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"O\n\x13SearchUnitsResponse\x12\x1f\n\x05units\x18\x01 \x03(\x0b\x32\x10.framespace.Unit\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x8e\x01\n\x17SearchDataFramesRequest\x12\x15\n\rdataframe_ids\x18\x01 \x03(\t\x12\x14\n\x0ckeyspace_ids\x18\x02 \x03(\x05\x12\x1f\n\x05units\x18\x03 \x03(\x0b\x32\x10.framespace.Unit\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\"^\n\x18SearchDataFramesResponse\x12)\n\ndataframes\x18\x01 \x03(\x0b\x32\x15.framespace.DataFrame\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x81\x01\n\x15SliceDataFrameRequest\x12\x14\n\x0c\x64\x61taframe_id\x18\x01 \x01(\t\x12(\n\tnew_major\x18\x02 \x01(\x0b\x32\x15.framespace.Dimension\x12(\n\tnew_minor\x18\x03 \x01(\x0b\x32\x15.framespace.Dimension2\xb7\x03\n\x11\x46rameSpaceService\x12K\n\nSearchAxes\x12\x1d.framespace.SearchAxesRequest\x1a\x1e.framespace.SearchAxesResponse\x12Z\n\x0fSearchKeySpaces\x12\".framespace.SearchKeySpacesRequest\x1a#.framespace.SearchKeySpacesResponse\x12N\n\x0bSearchUnits\x12\x1e.framespace.SearchUnitsRequest\x1a\x1f.framespace.SearchUnitsResponse\x12]\n\x10SearchDataFrames\x12#.framespace.SearchDataFramesRequest\x1a$.framespace.SearchDataFramesResponse\x12J\n\x0eSliceDataFrame\x12!.framespace.SliceDataFrameRequest\x1a\x15.framespace.DataFrameb\x06proto3')
  ,
  dependencies=[proto_dot_framespace_dot_framespace__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SEARCHAXESREQUEST = _descriptor.Descriptor(
  name='SearchAxesRequest',
  full_name='framespace.SearchAxesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='framespace.SearchAxesRequest.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='framespace.SearchAxesRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='framespace.SearchAxesRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=92,
  serialized_end=165,
)


_SEARCHAXESRESPONSE = _descriptor.Descriptor(
  name='SearchAxesResponse',
  full_name='framespace.SearchAxesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='axes', full_name='framespace.SearchAxesResponse.axes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='framespace.SearchAxesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=167,
  serialized_end=244,
)


_SEARCHKEYSPACESREQUEST = _descriptor.Descriptor(
  name='SearchKeySpacesRequest',
  full_name='framespace.SearchKeySpacesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyspace_ids', full_name='framespace.SearchKeySpacesRequest.keyspace_ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='framespace.SearchKeySpacesRequest.names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='axis_names', full_name='framespace.SearchKeySpacesRequest.axis_names', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keys', full_name='framespace.SearchKeySpacesRequest.keys', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='framespace.SearchKeySpacesRequest.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='framespace.SearchKeySpacesRequest.page_token', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=247,
  serialized_end=381,
)


_SEARCHKEYSPACESRESPONSE = _descriptor.Descriptor(
  name='SearchKeySpacesResponse',
  full_name='framespace.SearchKeySpacesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyspaces', full_name='framespace.SearchKeySpacesResponse.keyspaces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='framespace.SearchKeySpacesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=383,
  serialized_end=474,
)


_SEARCHUNITSREQUEST = _descriptor.Descriptor(
  name='SearchUnitsRequest',
  full_name='framespace.SearchUnitsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='framespace.SearchUnitsRequest.names', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='framespace.SearchUnitsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='framespace.SearchUnitsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=476,
  serialized_end=550,
)


_SEARCHUNITSRESPONSE = _descriptor.Descriptor(
  name='SearchUnitsResponse',
  full_name='framespace.SearchUnitsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='units', full_name='framespace.SearchUnitsResponse.units', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='framespace.SearchUnitsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=552,
  serialized_end=631,
)


_SEARCHDATAFRAMESREQUEST = _descriptor.Descriptor(
  name='SearchDataFramesRequest',
  full_name='framespace.SearchDataFramesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataframe_ids', full_name='framespace.SearchDataFramesRequest.dataframe_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyspace_ids', full_name='framespace.SearchDataFramesRequest.keyspace_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='units', full_name='framespace.SearchDataFramesRequest.units', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='framespace.SearchDataFramesRequest.page_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='framespace.SearchDataFramesRequest.page_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=634,
  serialized_end=776,
)


_SEARCHDATAFRAMESRESPONSE = _descriptor.Descriptor(
  name='SearchDataFramesResponse',
  full_name='framespace.SearchDataFramesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataframes', full_name='framespace.SearchDataFramesResponse.dataframes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='framespace.SearchDataFramesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=778,
  serialized_end=872,
)


_SLICEDATAFRAMEREQUEST = _descriptor.Descriptor(
  name='SliceDataFrameRequest',
  full_name='framespace.SliceDataFrameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataframe_id', full_name='framespace.SliceDataFrameRequest.dataframe_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_major', full_name='framespace.SliceDataFrameRequest.new_major', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_minor', full_name='framespace.SliceDataFrameRequest.new_minor', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=875,
  serialized_end=1004,
)

_SEARCHAXESRESPONSE.fields_by_name['axes'].message_type = proto_dot_framespace_dot_framespace__pb2._AXIS
_SEARCHKEYSPACESRESPONSE.fields_by_name['keyspaces'].message_type = proto_dot_framespace_dot_framespace__pb2._KEYSPACE
_SEARCHUNITSRESPONSE.fields_by_name['units'].message_type = proto_dot_framespace_dot_framespace__pb2._UNIT
_SEARCHDATAFRAMESREQUEST.fields_by_name['units'].message_type = proto_dot_framespace_dot_framespace__pb2._UNIT
_SEARCHDATAFRAMESRESPONSE.fields_by_name['dataframes'].message_type = proto_dot_framespace_dot_framespace__pb2._DATAFRAME
_SLICEDATAFRAMEREQUEST.fields_by_name['new_major'].message_type = proto_dot_framespace_dot_framespace__pb2._DIMENSION
_SLICEDATAFRAMEREQUEST.fields_by_name['new_minor'].message_type = proto_dot_framespace_dot_framespace__pb2._DIMENSION
DESCRIPTOR.message_types_by_name['SearchAxesRequest'] = _SEARCHAXESREQUEST
DESCRIPTOR.message_types_by_name['SearchAxesResponse'] = _SEARCHAXESRESPONSE
DESCRIPTOR.message_types_by_name['SearchKeySpacesRequest'] = _SEARCHKEYSPACESREQUEST
DESCRIPTOR.message_types_by_name['SearchKeySpacesResponse'] = _SEARCHKEYSPACESRESPONSE
DESCRIPTOR.message_types_by_name['SearchUnitsRequest'] = _SEARCHUNITSREQUEST
DESCRIPTOR.message_types_by_name['SearchUnitsResponse'] = _SEARCHUNITSRESPONSE
DESCRIPTOR.message_types_by_name['SearchDataFramesRequest'] = _SEARCHDATAFRAMESREQUEST
DESCRIPTOR.message_types_by_name['SearchDataFramesResponse'] = _SEARCHDATAFRAMESRESPONSE
DESCRIPTOR.message_types_by_name['SliceDataFrameRequest'] = _SLICEDATAFRAMEREQUEST

SearchAxesRequest = _reflection.GeneratedProtocolMessageType('SearchAxesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHAXESREQUEST,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchAxesRequest)
  ))
_sym_db.RegisterMessage(SearchAxesRequest)

SearchAxesResponse = _reflection.GeneratedProtocolMessageType('SearchAxesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHAXESRESPONSE,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchAxesResponse)
  ))
_sym_db.RegisterMessage(SearchAxesResponse)

SearchKeySpacesRequest = _reflection.GeneratedProtocolMessageType('SearchKeySpacesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHKEYSPACESREQUEST,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchKeySpacesRequest)
  ))
_sym_db.RegisterMessage(SearchKeySpacesRequest)

SearchKeySpacesResponse = _reflection.GeneratedProtocolMessageType('SearchKeySpacesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHKEYSPACESRESPONSE,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchKeySpacesResponse)
  ))
_sym_db.RegisterMessage(SearchKeySpacesResponse)

SearchUnitsRequest = _reflection.GeneratedProtocolMessageType('SearchUnitsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHUNITSREQUEST,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchUnitsRequest)
  ))
_sym_db.RegisterMessage(SearchUnitsRequest)

SearchUnitsResponse = _reflection.GeneratedProtocolMessageType('SearchUnitsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHUNITSRESPONSE,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchUnitsResponse)
  ))
_sym_db.RegisterMessage(SearchUnitsResponse)

SearchDataFramesRequest = _reflection.GeneratedProtocolMessageType('SearchDataFramesRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHDATAFRAMESREQUEST,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchDataFramesRequest)
  ))
_sym_db.RegisterMessage(SearchDataFramesRequest)

SearchDataFramesResponse = _reflection.GeneratedProtocolMessageType('SearchDataFramesResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHDATAFRAMESRESPONSE,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SearchDataFramesResponse)
  ))
_sym_db.RegisterMessage(SearchDataFramesResponse)

SliceDataFrameRequest = _reflection.GeneratedProtocolMessageType('SliceDataFrameRequest', (_message.Message,), dict(
  DESCRIPTOR = _SLICEDATAFRAMEREQUEST,
  __module__ = 'proto.framespace.framespace_service_pb2'
  # @@protoc_insertion_point(class_scope:framespace.SliceDataFrameRequest)
  ))
_sym_db.RegisterMessage(SliceDataFrameRequest)


import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

class BetaFrameSpaceServiceServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def SearchAxes(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SearchKeySpaces(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SearchUnits(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SearchDataFrames(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def SliceDataFrame(self, request, context):
    raise NotImplementedError()

class BetaFrameSpaceServiceStub(object):
  """The interface to which stubs will conform."""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def SearchAxes(self, request, timeout):
    raise NotImplementedError()
  SearchAxes.future = None
  @abc.abstractmethod
  def SearchKeySpaces(self, request, timeout):
    raise NotImplementedError()
  SearchKeySpaces.future = None
  @abc.abstractmethod
  def SearchUnits(self, request, timeout):
    raise NotImplementedError()
  SearchUnits.future = None
  @abc.abstractmethod
  def SearchDataFrames(self, request, timeout):
    raise NotImplementedError()
  SearchDataFrames.future = None
  @abc.abstractmethod
  def SliceDataFrame(self, request, timeout):
    raise NotImplementedError()
  SliceDataFrame.future = None

def beta_create_FrameSpaceService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_pb2
  request_deserializers = {
    ('framespace.FrameSpaceService', 'SearchAxes'): proto.framespace.framespace_service_pb2.SearchAxesRequest.FromString,
    ('framespace.FrameSpaceService', 'SearchDataFrames'): proto.framespace.framespace_service_pb2.SearchDataFramesRequest.FromString,
    ('framespace.FrameSpaceService', 'SearchKeySpaces'): proto.framespace.framespace_service_pb2.SearchKeySpacesRequest.FromString,
    ('framespace.FrameSpaceService', 'SearchUnits'): proto.framespace.framespace_service_pb2.SearchUnitsRequest.FromString,
    ('framespace.FrameSpaceService', 'SliceDataFrame'): proto.framespace.framespace_service_pb2.SliceDataFrameRequest.FromString,
  }
  response_serializers = {
    ('framespace.FrameSpaceService', 'SearchAxes'): proto.framespace.framespace_service_pb2.SearchAxesResponse.SerializeToString,
    ('framespace.FrameSpaceService', 'SearchDataFrames'): proto.framespace.framespace_service_pb2.SearchDataFramesResponse.SerializeToString,
    ('framespace.FrameSpaceService', 'SearchKeySpaces'): proto.framespace.framespace_service_pb2.SearchKeySpacesResponse.SerializeToString,
    ('framespace.FrameSpaceService', 'SearchUnits'): proto.framespace.framespace_service_pb2.SearchUnitsResponse.SerializeToString,
    ('framespace.FrameSpaceService', 'SliceDataFrame'): proto.framespace.framespace_pb2.DataFrame.SerializeToString,
  }
  method_implementations = {
    ('framespace.FrameSpaceService', 'SearchAxes'): face_utilities.unary_unary_inline(servicer.SearchAxes),
    ('framespace.FrameSpaceService', 'SearchDataFrames'): face_utilities.unary_unary_inline(servicer.SearchDataFrames),
    ('framespace.FrameSpaceService', 'SearchKeySpaces'): face_utilities.unary_unary_inline(servicer.SearchKeySpaces),
    ('framespace.FrameSpaceService', 'SearchUnits'): face_utilities.unary_unary_inline(servicer.SearchUnits),
    ('framespace.FrameSpaceService', 'SliceDataFrame'): face_utilities.unary_unary_inline(servicer.SliceDataFrame),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)

def beta_create_FrameSpaceService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_service_pb2
  import proto.framespace.framespace_pb2
  request_serializers = {
    ('framespace.FrameSpaceService', 'SearchAxes'): proto.framespace.framespace_service_pb2.SearchAxesRequest.SerializeToString,
    ('framespace.FrameSpaceService', 'SearchDataFrames'): proto.framespace.framespace_service_pb2.SearchDataFramesRequest.SerializeToString,
    ('framespace.FrameSpaceService', 'SearchKeySpaces'): proto.framespace.framespace_service_pb2.SearchKeySpacesRequest.SerializeToString,
    ('framespace.FrameSpaceService', 'SearchUnits'): proto.framespace.framespace_service_pb2.SearchUnitsRequest.SerializeToString,
    ('framespace.FrameSpaceService', 'SliceDataFrame'): proto.framespace.framespace_service_pb2.SliceDataFrameRequest.SerializeToString,
  }
  response_deserializers = {
    ('framespace.FrameSpaceService', 'SearchAxes'): proto.framespace.framespace_service_pb2.SearchAxesResponse.FromString,
    ('framespace.FrameSpaceService', 'SearchDataFrames'): proto.framespace.framespace_service_pb2.SearchDataFramesResponse.FromString,
    ('framespace.FrameSpaceService', 'SearchKeySpaces'): proto.framespace.framespace_service_pb2.SearchKeySpacesResponse.FromString,
    ('framespace.FrameSpaceService', 'SearchUnits'): proto.framespace.framespace_service_pb2.SearchUnitsResponse.FromString,
    ('framespace.FrameSpaceService', 'SliceDataFrame'): proto.framespace.framespace_pb2.DataFrame.FromString,
  }
  cardinalities = {
    'SearchAxes': cardinality.Cardinality.UNARY_UNARY,
    'SearchDataFrames': cardinality.Cardinality.UNARY_UNARY,
    'SearchKeySpaces': cardinality.Cardinality.UNARY_UNARY,
    'SearchUnits': cardinality.Cardinality.UNARY_UNARY,
    'SliceDataFrame': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'framespace.FrameSpaceService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
