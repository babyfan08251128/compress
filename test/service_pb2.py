# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x0e\x66iledecompress\"E\n\tMyRequest\x12\x1a\n\x12\x63ompress_file_path\x18\x01 \x01(\t\x12\x1c\n\x14\x64\x65\x63ompress_file_path\x18\x02 \x01(\t\"-\n\nMyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t2S\n\x0e\x46ileDecompress\x12\x41\n\x08MyMethod\x12\x19.filedecompress.MyRequest\x1a\x1a.filedecompress.MyResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_MYREQUEST']._serialized_start=33
  _globals['_MYREQUEST']._serialized_end=102
  _globals['_MYRESPONSE']._serialized_start=104
  _globals['_MYRESPONSE']._serialized_end=149
  _globals['_FILEDECOMPRESS']._serialized_start=151
  _globals['_FILEDECOMPRESS']._serialized_end=234
# @@protoc_insertion_point(module_scope)
