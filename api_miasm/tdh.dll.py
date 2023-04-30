###### Enums ######
DECODING_SOURCE = {
    "DecodingSourceXMLFile": 0,
    "DecodingSourceWbem": 1,
    "DecodingSourceWPP": 2,
}
DECODING_SOURCE_INV = {
    0: "DecodingSourceXMLFile",
    1: "DecodingSourceWbem",
    2: "DecodingSourceWPP",
}
TDH_IN_TYPE = {
    "TDH_INTYPE_NULL": 0,
    "TDH_INTYPE_UNICODESTRING": 1,
    "TDH_INTYPE_ANSISTRING": 2,
    "TDH_INTYPE_INT8": 3,
    "TDH_INTYPE_UINT8": 4,
    "TDH_INTYPE_INT16": 5,
    "TDH_INTYPE_UINT16": 6,
    "TDH_INTYPE_INT32": 7,
    "TDH_INTYPE_UINT32": 8,
    "TDH_INTYPE_INT64": 9,
    "TDH_INTYPE_UINT64": 10,
    "TDH_INTYPE_FLOAT": 11,
    "TDH_INTYPE_DOUBLE": 12,
    "TDH_INTYPE_BOOLEAN": 13,
    "TDH_INTYPE_BINARY": 14,
    "TDH_INTYPE_GUID": 15,
    "TDH_INTYPE_POINTER": 16,
    "TDH_INTYPE_FILETIME": 17,
    "TDH_INTYPE_SYSTEMTIME": 18,
    "TDH_INTYPE_SID": 19,
    "TDH_INTYPE_HEXINT32": 20,
    "TDH_INTYPE_HEXINT64": 21,
    "TDH_INTYPE_COUNTEDSTRING": 300,
    "TDH_INTYPE_COUNTEDANSISTRING": 301,
    "TDH_INTYPE_REVERSEDCOUNTEDSTRING": 302,
    "TDH_INTYPE_REVERSEDCOUNTEDANSISTRING": 303,
    "TDH_INTYPE_NONNULLTERMINATEDSTRING": 304,
    "TDH_INTYPE_NONNULLTERMINATEDANSISTRING": 305,
    "TDH_INTYPE_UNICODECHAR": 306,
    "TDH_INTYPE_ANSICHAR": 307,
    "TDH_INTYPE_SIZET": 308,
    "TDH_INTYPE_HEXDUMP": 309,
    "TDH_INTYPE_WBEMSID": 310,
}
TDH_IN_TYPE_INV = {
    0: "TDH_INTYPE_NULL",
    1: "TDH_INTYPE_UNICODESTRING",
    2: "TDH_INTYPE_ANSISTRING",
    3: "TDH_INTYPE_INT8",
    4: "TDH_INTYPE_UINT8",
    5: "TDH_INTYPE_INT16",
    6: "TDH_INTYPE_UINT16",
    7: "TDH_INTYPE_INT32",
    8: "TDH_INTYPE_UINT32",
    9: "TDH_INTYPE_INT64",
    10: "TDH_INTYPE_UINT64",
    11: "TDH_INTYPE_FLOAT",
    12: "TDH_INTYPE_DOUBLE",
    13: "TDH_INTYPE_BOOLEAN",
    14: "TDH_INTYPE_BINARY",
    15: "TDH_INTYPE_GUID",
    16: "TDH_INTYPE_POINTER",
    17: "TDH_INTYPE_FILETIME",
    18: "TDH_INTYPE_SYSTEMTIME",
    19: "TDH_INTYPE_SID",
    20: "TDH_INTYPE_HEXINT32",
    21: "TDH_INTYPE_HEXINT64",
    300: "TDH_INTYPE_COUNTEDSTRING",
    301: "TDH_INTYPE_COUNTEDANSISTRING",
    302: "TDH_INTYPE_REVERSEDCOUNTEDSTRING",
    303: "TDH_INTYPE_REVERSEDCOUNTEDANSISTRING",
    304: "TDH_INTYPE_NONNULLTERMINATEDSTRING",
    305: "TDH_INTYPE_NONNULLTERMINATEDANSISTRING",
    306: "TDH_INTYPE_UNICODECHAR",
    307: "TDH_INTYPE_ANSICHAR",
    308: "TDH_INTYPE_SIZET",
    309: "TDH_INTYPE_HEXDUMP",
    310: "TDH_INTYPE_WBEMSID",
}
TDH_OUT_TYPE = {
    "TDH_OUTTYPE_NULL": 0,
    "TDH_OUTTYPE_STRING": 1,
    "TDH_OUTTYPE_DATETIME": 2,
    "TDH_OUTTYPE_BYTE": 3,
    "TDH_OUTTYPE_UNSIGNEDBYTE": 4,
    "TDH_OUTTYPE_SHORT": 5,
    "TDH_OUTTYPE_UNSIGNEDSHORT": 6,
    "TDH_OUTTYPE_INT": 7,
    "TDH_OUTTYPE_UNSIGNEDINT": 8,
    "TDH_OUTTYPE_LONG": 9,
    "TDH_OUTTYPE_UNSIGNEDLONG": 10,
    "TDH_OUTTYPE_FLOAT": 11,
    "TDH_OUTTYPE_DOUBLE": 12,
    "TDH_OUTTYPE_BOOLEAN": 13,
    "TDH_OUTTYPE_GUID": 14,
    "TDH_OUTTYPE_HEXBINARY": 15,
    "TDH_OUTTYPE_HEXINT8": 16,
    "TDH_OUTTYPE_HEXINT16": 17,
    "TDH_OUTTYPE_HEXINT32": 18,
    "TDH_OUTTYPE_HEXINT64": 19,
    "TDH_OUTTYPE_PID": 20,
    "TDH_OUTTYPE_TID": 21,
    "TDH_OUTTYPE_PORT": 22,
    "TDH_OUTTYPE_IPV4": 23,
    "TDH_OUTTYPE_IPV6": 24,
    "TDH_OUTTYPE_SOCKETADDRESS": 25,
    "TDH_OUTTYPE_CIMDATETIME": 26,
    "TDH_OUTTYPE_ETWTIME": 27,
    "TDH_OUTTYPE_XML": 28,
    "TDH_OUTTYPE_ERRORCODE": 29,
    "TDH_OUTTYPE_WIN32ERROR": 30,
    "TDH_OUTTYPE_NTSTATUS": 31,
    "TDH_OUTTYPE_HRESULT": 32,
    "TDH_OUTTYPE_CULTURE_INSENSITIVE_DATETIME": 33,
    "TDH_OUTTYPE_REDUCEDSTRING": 300,
    "TDH_OUTTYPE_NOPRINT": 301,
}
TDH_OUT_TYPE_INV = {
    0: "TDH_OUTTYPE_NULL",
    1: "TDH_OUTTYPE_STRING",
    2: "TDH_OUTTYPE_DATETIME",
    3: "TDH_OUTTYPE_BYTE",
    4: "TDH_OUTTYPE_UNSIGNEDBYTE",
    5: "TDH_OUTTYPE_SHORT",
    6: "TDH_OUTTYPE_UNSIGNEDSHORT",
    7: "TDH_OUTTYPE_INT",
    8: "TDH_OUTTYPE_UNSIGNEDINT",
    9: "TDH_OUTTYPE_LONG",
    10: "TDH_OUTTYPE_UNSIGNEDLONG",
    11: "TDH_OUTTYPE_FLOAT",
    12: "TDH_OUTTYPE_DOUBLE",
    13: "TDH_OUTTYPE_BOOLEAN",
    14: "TDH_OUTTYPE_GUID",
    15: "TDH_OUTTYPE_HEXBINARY",
    16: "TDH_OUTTYPE_HEXINT8",
    17: "TDH_OUTTYPE_HEXINT16",
    18: "TDH_OUTTYPE_HEXINT32",
    19: "TDH_OUTTYPE_HEXINT64",
    20: "TDH_OUTTYPE_PID",
    21: "TDH_OUTTYPE_TID",
    22: "TDH_OUTTYPE_PORT",
    23: "TDH_OUTTYPE_IPV4",
    24: "TDH_OUTTYPE_IPV6",
    25: "TDH_OUTTYPE_SOCKETADDRESS",
    26: "TDH_OUTTYPE_CIMDATETIME",
    27: "TDH_OUTTYPE_ETWTIME",
    28: "TDH_OUTTYPE_XML",
    29: "TDH_OUTTYPE_ERRORCODE",
    30: "TDH_OUTTYPE_WIN32ERROR",
    31: "TDH_OUTTYPE_NTSTATUS",
    32: "TDH_OUTTYPE_HRESULT",
    33: "TDH_OUTTYPE_CULTURE_INSENSITIVE_DATETIME",
    300: "TDH_OUTTYPE_REDUCEDSTRING",
    301: "TDH_OUTTYPE_NOPRINT",
}
MAP_VALUETYPE = {
    "EVENTMAP_ENTRY_VALUETYPE_ULONG": 0,
    "EVENTMAP_ENTRY_VALUETYPE_STRING": 1,
}
MAP_VALUETYPE_INV = {
    0: "EVENTMAP_ENTRY_VALUETYPE_ULONG",
    1: "EVENTMAP_ENTRY_VALUETYPE_STRING",
}
EVENT_FIELD_TYPE = {
    "EventKeywordInformation": 0,
    "EventLevelInformation": 1,
    "EventChannelInformation": 2,
    "EventTaskInformation": 3,
    "EventOpcodeInformation": 4,
}
EVENT_FIELD_TYPE_INV = {
    0: "EventKeywordInformation",
    1: "EventLevelInformation",
    2: "EventChannelInformation",
    3: "EventTaskInformation",
    4: "EventOpcodeInformation",
}
TDH_CONTEXT_TYPE = {
    "TDH_CONTEXT_WPP_TMFFILE": 0,
    "TDH_CONTEXT_WPP_TMFSEARCHPATH": 1,
    "TDH_CONTEXT_WPP_GMT": 2,
    "TDH_CONTEXT_POINTERSIZE": 3,
}
TDH_CONTEXT_TYPE_INV = {
    0: "TDH_CONTEXT_WPP_TMFFILE",
    1: "TDH_CONTEXT_WPP_TMFSEARCHPATH",
    2: "TDH_CONTEXT_WPP_GMT",
    3: "TDH_CONTEXT_POINTERSIZE",
}

###################

###### Types ######
TDH_HANDLE = HANDLE
PTDH_HANDLE = Ptr("<I", TDH_HANDLE())
PEVENT_HEADER_EXTENDED_DATA_ITEM = LPVOID

class TRACE_PROVIDER_INFO(MemStruct):
    fields = [
        ("ProviderGuid", GUID()),
        ("SchemaSource", ULONG()),
        ("ProviderNameOffset", ULONG()),
    ]

TRACE_PROVIDER_INFO__ANYSIZE_ARRAY_ = Array(TRACE_PROVIDER_INFO, 1)

class PROVIDER_ENUMERATION_INFO(MemStruct):
    fields = [
        ("NumberOfProviders", ULONG()),
        ("Reserved", ULONG()),
        ("TraceProviderInfoArray", TRACE_PROVIDER_INFO__ANYSIZE_ARRAY_()),
    ]

PPROVIDER_ENUMERATION_INFO = Ptr("<I", PROVIDER_ENUMERATION_INFO())
DECODING_SOURCE = UINT
TEMPLATE_FLAGS = UINT
TDH_IN_TYPE = USHORT
TDH_OUT_TYPE = USHORT
PROPERTY_FLAGS = UINT

class _EVENT_PROPERTY_INFO_u1_s1_(MemStruct):
    fields = [
        ("InType", TDH_IN_TYPE()),
        ("OutType", TDH_OUT_TYPE()),
        ("MapNameOffset", ULONG()),
    ]


class _EVENT_PROPERTY_INFO_u1_s2_(MemStruct):
    fields = [
        ("StructStartIndex", USHORT()),
        ("NumOfStructMembers", USHORT()),
        ("padding", ULONG()),
    ]

_EVENT_PROPERTY_INFO_u1_ = Union([
    ("nonStructType", _EVENT_PROPERTY_INFO_u1_s1_),
    ("structType", _EVENT_PROPERTY_INFO_u1_s2_),
])
_EVENT_PROPERTY_INFO_u2_ = Union([
    ("count", USHORT),
    ("countPropertyIndex", USHORT),
])
_EVENT_PROPERTY_INFO_u3_ = Union([
    ("length", USHORT),
    ("lengthPropertyIndex", USHORT),
])

class EVENT_PROPERTY_INFO(MemStruct):
    fields = [
        ("Flags", PROPERTY_FLAGS()),
        ("NameOffset", ULONG()),
        (None, _EVENT_PROPERTY_INFO_u1_()),
        (None, _EVENT_PROPERTY_INFO_u2_()),
        (None, _EVENT_PROPERTY_INFO_u3_()),
        ("Reserved", ULONG()),
    ]

EVENT_PROPERTY_INFO__ANYSIZE_ARRAY_ = Array(EVENT_PROPERTY_INFO, 1)

class PROVIDER_FILTER_INFO(MemStruct):
    fields = [
        ("Id", UCHAR()),
        ("Version", UCHAR()),
        ("MessageOffset", ULONG()),
        ("Reserved", ULONG()),
        ("PropertyCount", ULONG()),
        ("EventPropertyInfoArray", EVENT_PROPERTY_INFO__ANYSIZE_ARRAY_()),
    ]

PPROVIDER_FILTER_INFO = Ptr("<I", PROVIDER_FILTER_INFO())
PPROVIDER_FILTER_INFO_PTR = Ptr("<I", PPROVIDER_FILTER_INFO())

class TRACE_EVENT_INFO(MemStruct):
    fields = [
        ("ProviderGuid", GUID()),
        ("EventGuid", GUID()),
        ("EventDescriptor", EVENT_DESCRIPTOR()),
        ("DecodingSource", DECODING_SOURCE()),
        ("ProviderNameOffset", ULONG()),
        ("LevelNameOffset", ULONG()),
        ("ChannelNameOffset", ULONG()),
        ("KeywordsNameOffset", ULONG()),
        ("TaskNameOffset", ULONG()),
        ("OpcodeNameOffset", ULONG()),
        ("EventMessageOffset", ULONG()),
        ("ProviderMessageOffset", ULONG()),
        ("BinaryXMLOffset", ULONG()),
        ("BinaryXMLSize", ULONG()),
        ("ActivityIDNameOffset", ULONG()),
        ("RelatedActivityIDNameOffset", ULONG()),
        ("PropertyCount", ULONG()),
        ("TopLevelPropertyCount", ULONG()),
        ("Flags", TEMPLATE_FLAGS()),
        ("EventPropertyInfoArray", EVENT_PROPERTY_INFO__ANYSIZE_ARRAY_()),
    ]

PTRACE_EVENT_INFO = Ptr("<I", TRACE_EVENT_INFO())
MAP_VALUETYPE = UINT
MAP_FLAGS = UINT
_EVENT_MAP_ENTRY_u_ = Union([
    ("Value", ULONG),
    ("InputOffset", ULONG),
])

class EVENT_MAP_ENTRY(MemStruct):
    fields = [
        ("OutputOffset", ULONG()),
        (None, _EVENT_MAP_ENTRY_u_()),
    ]

EVENT_MAP_ENTRY__ANYSIZE_ARRAY_ = Array(EVENT_MAP_ENTRY, 1)
_EVENT_MAP_INFO_u_ = Union([
    ("MapEntryValueType", MAP_VALUETYPE),
    ("FormatStringOffset", ULONG),
])

class EVENT_MAP_INFO(MemStruct):
    fields = [
        ("NameOffset", ULONG()),
        ("Flag", MAP_FLAGS()),
        ("EntryCount", ULONG()),
        (None, _EVENT_MAP_INFO_u_()),
        ("MapEntryArray", EVENT_MAP_ENTRY__ANYSIZE_ARRAY_()),
    ]

PEVENT_MAP_INFO = Ptr("<I", EVENT_MAP_INFO())
EVENT_FIELD_TYPE = UINT

class PROVIDER_FIELD_INFO(MemStruct):
    fields = [
        ("NameOffset", ULONG()),
        ("DescriptionOffset", ULONG()),
        ("Value", ULONGLONG()),
    ]

PROVIDER_FIELD_INFO__ANYSIZE_ARRAY_ = Array(PROVIDER_FIELD_INFO, 1)

class PROVIDER_FIELD_INFOARRAY(MemStruct):
    fields = [
        ("NumberOfElements", ULONG()),
        ("FieldType", EVENT_FIELD_TYPE()),
        ("FieldInfoArray", PROVIDER_FIELD_INFO__ANYSIZE_ARRAY_()),
    ]

PPROVIDER_FIELD_INFOARRAY = Ptr("<I", PROVIDER_FIELD_INFOARRAY())
TDH_CONTEXT_TYPE = UINT

class TDH_CONTEXT(MemStruct):
    fields = [
        ("ParameterValue", ULONGLONG()),
        ("ParameterType", TDH_CONTEXT_TYPE()),
        ("ParameterSize", ULONG()),
    ]

PTDH_CONTEXT = Ptr("<I", TDH_CONTEXT())

class PROPERTY_DATA_DESCRIPTOR(MemStruct):
    fields = [
        ("PropertyName", ULONGLONG()),
        ("ArrayIndex", ULONG()),
        ("Reserved", ULONG()),
    ]

PPROPERTY_DATA_DESCRIPTOR = Ptr("<I", PROPERTY_DATA_DESCRIPTOR())

class _EVENT_HEADER_u_s_(MemStruct):
    fields = [
        ("KernelTime", ULONG()),
        ("UserTime", ULONG()),
    ]

_EVENT_HEADER_u_ = Union([
    (None, _EVENT_HEADER_u_s_),
    ("ProcessorTime", ULONG64),
])
_EVENT_HEADER_FLAG_ = USHORT
_EVENT_HEADER_PROPERTY_ = USHORT

class EVENT_HEADER(MemStruct):
    fields = [
        ("Size", USHORT()),
        ("HeaderType", USHORT()),
        ("Flags", _EVENT_HEADER_FLAG_()),
        ("EventProperty", _EVENT_HEADER_PROPERTY_()),
        ("ThreadId", ULONG()),
        ("ProcessId", ULONG()),
        ("TimeStamp", LARGE_INTEGER()),
        ("ProviderId", GUID()),
        ("EventDescriptor", EVENT_DESCRIPTOR()),
        (None, _EVENT_HEADER_u_()),
        ("ActivityId", GUID()),
    ]


class EVENT_RECORD(MemStruct):
    fields = [
        ("EventHeader", EVENT_HEADER()),
        ("BufferContext", ETW_BUFFER_CONTEXT()),
        ("ExtendedDataCount", USHORT()),
        ("UserDataLength", USHORT()),
        ("ExtendedData", PEVENT_HEADER_EXTENDED_DATA_ITEM()),
        ("UserData", PVOID()),
        ("UserContext", PVOID()),
    ]

PEVENT_RECORD = Ptr("<I", EVENT_RECORD())

###################

###### Functions ######

def tdh_TdhCloseDecodingHandle(jitter):
    """
    [ERROR_CODE_ULONG] TdhCloseDecodingHandle(
        TDH_HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhEnumerateProviderFieldInformation(jitter):
    """
    [ERROR_CODE_ULONG] TdhEnumerateProviderFieldInformation(
        LPGUID pGuid,
        EVENT_FIELD_TYPE EventFieldType,
        PPROVIDER_FIELD_INFOARRAY pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGuid", "EventFieldType", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhEnumerateProviderFilters(jitter):
    """
    [ERROR_CODE_ULONG] TdhEnumerateProviderFilters(
        LPGUID pGuid,
        ULONG TdhContextCount,
        PTDH_CONTEXT pTdhContext,
        ULONG* FilterCount,
        PPROVIDER_FILTER_INFO* pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGuid", "TdhContextCount", "pTdhContext", "FilterCount", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhEnumerateProviders(jitter):
    """
    [ERROR_CODE_ULONG] TdhEnumerateProviders(
        PPROVIDER_ENUMERATION_INFO pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhFormatProperty(jitter):
    """
    [ERROR_CODE_ULONG] TdhFormatProperty(
        PTRACE_EVENT_INFO EventInfo,
        PEVENT_MAP_INFO MapInfo,
        ULONG PointerSize,
        USHORT PropertyInType,
        USHORT PropertyOutType,
        USHORT PropertyLength,
        USHORT UserDataLength,
        PBYTE UserData,
        PULONG BufferSize,
        PWCHAR Buffer,
        PUSHORT UserDataConsumed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventInfo", "MapInfo", "PointerSize", "PropertyInType", "PropertyOutType", "PropertyLength", "UserDataLength", "UserData", "BufferSize", "Buffer", "UserDataConsumed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetDecodingParameter(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetDecodingParameter(
        TDH_HANDLE Handle,
        PTDH_CONTEXT TdhContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "TdhContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetEventInformation(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetEventInformation(
        PEVENT_RECORD pEvent,
        ULONG TdhContextCount,
        PTDH_CONTEXT pTdhContext,
        PTRACE_EVENT_INFO pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEvent", "TdhContextCount", "pTdhContext", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetEventMapInformation(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetEventMapInformation(
        PEVENT_RECORD pEvent,
        LPWSTR pMapName,
        PEVENT_MAP_INFO pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEvent", "pMapName", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetPropertySize(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetPropertySize(
        PEVENT_RECORD pEvent,
        ULONG TdhContextCount,
        PTDH_CONTEXT pTdhContext,
        ULONG PropertyDataCount,
        PPROPERTY_DATA_DESCRIPTOR pPropertyData,
        ULONG* pPropertySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEvent", "TdhContextCount", "pTdhContext", "PropertyDataCount", "pPropertyData", "pPropertySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetProperty(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetProperty(
        PEVENT_RECORD pEvent,
        ULONG TdhContextCount,
        PTDH_CONTEXT pTdhContext,
        ULONG PropertyDataCount,
        PPROPERTY_DATA_DESCRIPTOR pPropertyData,
        ULONG BufferSize,
        PBYTE pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEvent", "TdhContextCount", "pTdhContext", "PropertyDataCount", "pPropertyData", "BufferSize", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetWppMessage(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetWppMessage(
        TDH_HANDLE Handle,
        PEVENT_RECORD EventRecord,
        PULONG BufferSize,
        PBYTE Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "EventRecord", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhGetWppProperty(jitter):
    """
    [ERROR_CODE_ULONG] TdhGetWppProperty(
        TDH_HANDLE Handle,
        PEVENT_RECORD EventRecord,
        PWSTR PropertyName,
        PULONG BufferSize,
        PBYTE Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "EventRecord", "PropertyName", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhLoadManifest(jitter):
    """
    [ERROR_CODE_ULONG] TdhLoadManifest(
        PWSTR Manifest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Manifest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhLoadManifestFromBinary(jitter):
    """
    [ERROR_CODE_ULONG] TdhLoadManifestFromBinary(
        PWSTR BinaryPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BinaryPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhOpenDecodingHandle(jitter):
    """
    [ERROR_CODE_ULONG] TdhOpenDecodingHandle(
        PTDH_HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhQueryProviderFieldInformation(jitter):
    """
    [ERROR_CODE_ULONG] TdhQueryProviderFieldInformation(
        LPGUID pGuid,
        ULONGLONG EventFieldValue,
        EVENT_FIELD_TYPE EventFieldType,
        PPROVIDER_FIELD_INFOARRAY pBuffer,
        ULONG* pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGuid", "EventFieldValue", "EventFieldType", "pBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhSetDecodingParameter(jitter):
    """
    [ERROR_CODE_ULONG] TdhSetDecodingParameter(
        TDH_HANDLE Handle,
        PTDH_CONTEXT TdhContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "TdhContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def tdh_TdhUnloadManifest(jitter):
    """
    [ERROR_CODE_ULONG] TdhUnloadManifest(
        PWSTR Manifest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Manifest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
