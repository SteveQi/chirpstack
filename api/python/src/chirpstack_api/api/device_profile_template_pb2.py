# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/api/device_profile_template.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.api import device_profile_pb2 as chirpstack__api_dot_api_dot_device__profile__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0chirpstack-api/api/device_profile_template.proto\x12\x03\x61pi\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\x1a\'chirpstack-api/api/device_profile.proto\"\xf6\x07\n\x15\x44\x65viceProfileTemplate\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06vendor\x18\x04 \x01(\t\x12\x10\n\x08\x66irmware\x18\x05 \x01(\t\x12\x1e\n\x06region\x18\x06 \x01(\x0e\x32\x0e.common.Region\x12\'\n\x0bmac_version\x18\x07 \x01(\x0e\x32\x12.common.MacVersion\x12\x36\n\x13reg_params_revision\x18\x08 \x01(\x0e\x32\x19.common.RegParamsRevision\x12\x18\n\x10\x61\x64r_algorithm_id\x18\t \x01(\t\x12\x30\n\x15payload_codec_runtime\x18\n \x01(\x0e\x32\x11.api.CodecRuntime\x12\x1c\n\x14payload_codec_script\x18\x0b \x01(\t\x12\x1f\n\x17\x66lush_queue_on_activate\x18\x0c \x01(\x08\x12\x17\n\x0fuplink_interval\x18\r \x01(\r\x12\"\n\x1a\x64\x65vice_status_req_interval\x18\x0e \x01(\r\x12\x15\n\rsupports_otaa\x18\x0f \x01(\x08\x12\x18\n\x10supports_class_b\x18\x10 \x01(\x08\x12\x18\n\x10supports_class_c\x18\x11 \x01(\x08\x12\x17\n\x0f\x63lass_b_timeout\x18\x12 \x01(\r\x12\x1e\n\x16\x63lass_b_ping_slot_nb_k\x18\x13 \x01(\r\x12\x1c\n\x14\x63lass_b_ping_slot_dr\x18\x14 \x01(\r\x12\x1e\n\x16\x63lass_b_ping_slot_freq\x18\x15 \x01(\r\x12\x17\n\x0f\x63lass_c_timeout\x18\x16 \x01(\r\x12\x15\n\rabp_rx1_delay\x18\x17 \x01(\r\x12\x19\n\x11\x61\x62p_rx1_dr_offset\x18\x18 \x01(\r\x12\x12\n\nabp_rx2_dr\x18\x19 \x01(\r\x12\x14\n\x0c\x61\x62p_rx2_freq\x18\x1a \x01(\r\x12\x32\n\x04tags\x18\x1b \x03(\x0b\x32$.api.DeviceProfileTemplate.TagsEntry\x12\x42\n\x0cmeasurements\x18\x1c \x03(\x0b\x32,.api.DeviceProfileTemplate.MeasurementsEntry\x12 \n\x18\x61uto_detect_measurements\x18\x1d \x01(\x08\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x45\n\x11MeasurementsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.api.Measurement:\x02\x38\x01\"\x87\x03\n\x1d\x44\x65viceProfileTemplateListItem\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0e\n\x06vendor\x18\x05 \x01(\t\x12\x10\n\x08\x66irmware\x18\x06 \x01(\t\x12\x1e\n\x06region\x18\x07 \x01(\x0e\x32\x0e.common.Region\x12\'\n\x0bmac_version\x18\x08 \x01(\x0e\x32\x12.common.MacVersion\x12\x36\n\x13reg_params_revision\x18\t \x01(\x0e\x32\x19.common.RegParamsRevision\x12\x15\n\rsupports_otaa\x18\n \x01(\x08\x12\x18\n\x10supports_class_b\x18\x0b \x01(\x08\x12\x18\n\x10supports_class_c\x18\x0c \x01(\x08\"a\n\"CreateDeviceProfileTemplateRequest\x12;\n\x17\x64\x65vice_profile_template\x18\x01 \x01(\x0b\x32\x1a.api.DeviceProfileTemplate\"-\n\x1fGetDeviceProfileTemplateRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xbf\x01\n GetDeviceProfileTemplateResponse\x12;\n\x17\x64\x65vice_profile_template\x18\x01 \x01(\x0b\x32\x1a.api.DeviceProfileTemplate\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"a\n\"UpdateDeviceProfileTemplateRequest\x12;\n\x17\x64\x65vice_profile_template\x18\x01 \x01(\x0b\x32\x1a.api.DeviceProfileTemplate\"0\n\"DeleteDeviceProfileTemplateRequest\x12\n\n\x02id\x18\x01 \x01(\t\"B\n!ListDeviceProfileTemplatesRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\"m\n\"ListDeviceProfileTemplatesResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\r\x12\x32\n\x06result\x18\x02 \x03(\x0b\x32\".api.DeviceProfileTemplateListItem2\x9d\x05\n\x1c\x44\x65viceProfileTemplateService\x12s\n\x06\x43reate\x12\'.api.CreateDeviceProfileTemplateRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"\"\x1d/api/device-profile-templates:\x01*\x12~\n\x03Get\x12$.api.GetDeviceProfileTemplateRequest\x1a%.api.GetDeviceProfileTemplateResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/api/device-profile-templates/{id}\x12\x90\x01\n\x06Update\x12\'.api.UpdateDeviceProfileTemplateRequest\x1a\x16.google.protobuf.Empty\"E\x82\xd3\xe4\x93\x02?\x1a:/api/device-profile-templates/{device_profile_template.id}:\x01*\x12u\n\x06\x44\x65lete\x12\'.api.DeleteDeviceProfileTemplateRequest\x1a\x16.google.protobuf.Empty\"*\x82\xd3\xe4\x93\x02$*\"/api/device-profile-templates/{id}\x12~\n\x04List\x12&.api.ListDeviceProfileTemplatesRequest\x1a\'.api.ListDeviceProfileTemplatesResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/api/device-profile-templatesBa\n\x11io.chirpstack.apiB\x1a\x44\x65viceProfileTemplateProtoP\x01Z.github.com/chirpstack/chirpstack/api/go/v4/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.api.device_profile_template_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021io.chirpstack.apiB\032DeviceProfileTemplateProtoP\001Z.github.com/chirpstack/chirpstack/api/go/v4/api'
  _DEVICEPROFILETEMPLATE_TAGSENTRY._options = None
  _DEVICEPROFILETEMPLATE_TAGSENTRY._serialized_options = b'8\001'
  _DEVICEPROFILETEMPLATE_MEASUREMENTSENTRY._options = None
  _DEVICEPROFILETEMPLATE_MEASUREMENTSENTRY._serialized_options = b'8\001'
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['Create']._options = None
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002\"\"\035/api/device-profile-templates:\001*'
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['Get']._options = None
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002$\022\"/api/device-profile-templates/{id}'
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['Update']._options = None
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002?\032:/api/device-profile-templates/{device_profile_template.id}:\001*'
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['Delete']._options = None
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002$*\"/api/device-profile-templates/{id}'
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['List']._options = None
  _DEVICEPROFILETEMPLATESERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\037\022\035/api/device-profile-templates'
  _DEVICEPROFILETEMPLATE._serialized_start=227
  _DEVICEPROFILETEMPLATE._serialized_end=1241
  _DEVICEPROFILETEMPLATE_TAGSENTRY._serialized_start=1127
  _DEVICEPROFILETEMPLATE_TAGSENTRY._serialized_end=1170
  _DEVICEPROFILETEMPLATE_MEASUREMENTSENTRY._serialized_start=1172
  _DEVICEPROFILETEMPLATE_MEASUREMENTSENTRY._serialized_end=1241
  _DEVICEPROFILETEMPLATELISTITEM._serialized_start=1244
  _DEVICEPROFILETEMPLATELISTITEM._serialized_end=1635
  _CREATEDEVICEPROFILETEMPLATEREQUEST._serialized_start=1637
  _CREATEDEVICEPROFILETEMPLATEREQUEST._serialized_end=1734
  _GETDEVICEPROFILETEMPLATEREQUEST._serialized_start=1736
  _GETDEVICEPROFILETEMPLATEREQUEST._serialized_end=1781
  _GETDEVICEPROFILETEMPLATERESPONSE._serialized_start=1784
  _GETDEVICEPROFILETEMPLATERESPONSE._serialized_end=1975
  _UPDATEDEVICEPROFILETEMPLATEREQUEST._serialized_start=1977
  _UPDATEDEVICEPROFILETEMPLATEREQUEST._serialized_end=2074
  _DELETEDEVICEPROFILETEMPLATEREQUEST._serialized_start=2076
  _DELETEDEVICEPROFILETEMPLATEREQUEST._serialized_end=2124
  _LISTDEVICEPROFILETEMPLATESREQUEST._serialized_start=2126
  _LISTDEVICEPROFILETEMPLATESREQUEST._serialized_end=2192
  _LISTDEVICEPROFILETEMPLATESRESPONSE._serialized_start=2194
  _LISTDEVICEPROFILETEMPLATESRESPONSE._serialized_end=2303
  _DEVICEPROFILETEMPLATESERVICE._serialized_start=2306
  _DEVICEPROFILETEMPLATESERVICE._serialized_end=2975
# @@protoc_insertion_point(module_scope)
