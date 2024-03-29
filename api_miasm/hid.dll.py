###### Enums ######
_HIDP_STATUS_ = {
    "HIDP_STATUS_SUCCESS": 0x00110000,
    "HIDP_STATUS_NULL": 0x80110001,
    "HIDP_STATUS_INVALID_PREPARSED_DATA": 0xc0110001,
    "HIDP_STATUS_INVALID_REPORT_TYPE": 0xc0110002,
    "HIDP_STATUS_INVALID_REPORT_LENGTH": 0xc0110003,
    "HIDP_STATUS_USAGE_NOT_FOUND": 0xc0110004,
    "HIDP_STATUS_VALUE_OUT_OF_RANGE": 0xc0110005,
    "HIDP_STATUS_BAD_LOG_PHY_VALUES": 0xc0110006,
    "HIDP_STATUS_BUFFER_TOO_SMALL": 0xc0110007,
    "HIDP_STATUS_INTERNAL_ERROR": 0xc0110008,
    "HIDP_STATUS_I8042_TRANS_UNKNOWN": 0xc0110009,
    "HIDP_STATUS_INCOMPATIBLE_REPORT_ID": 0xc011000a,
    "HIDP_STATUS_NOT_VALUE_ARRAY": 0xc011000b,
    "HIDP_STATUS_IS_VALUE_ARRAY": 0xc011000c,
    "HIDP_STATUS_DATA_INDEX_NOT_FOUND": 0xc011000d,
    "HIDP_STATUS_DATA_INDEX_OUT_OF_RANGE": 0xc011000e,
    "HIDP_STATUS_BUTTON_NOT_PRESSED": 0xc011000f,
    "HIDP_STATUS_REPORT_DOES_NOT_EXIST": 0xc0110010,
    "HIDP_STATUS_NOT_IMPLEMENTED": 0xc0110020,
}
_HIDP_STATUS__INV = {
    0x00110000: "HIDP_STATUS_SUCCESS",
    0x80110001: "HIDP_STATUS_NULL",
    0xc0110001: "HIDP_STATUS_INVALID_PREPARSED_DATA",
    0xc0110002: "HIDP_STATUS_INVALID_REPORT_TYPE",
    0xc0110003: "HIDP_STATUS_INVALID_REPORT_LENGTH",
    0xc0110004: "HIDP_STATUS_USAGE_NOT_FOUND",
    0xc0110005: "HIDP_STATUS_VALUE_OUT_OF_RANGE",
    0xc0110006: "HIDP_STATUS_BAD_LOG_PHY_VALUES",
    0xc0110007: "HIDP_STATUS_BUFFER_TOO_SMALL",
    0xc0110008: "HIDP_STATUS_INTERNAL_ERROR",
    0xc0110009: "HIDP_STATUS_I8042_TRANS_UNKNOWN",
    0xc011000a: "HIDP_STATUS_INCOMPATIBLE_REPORT_ID",
    0xc011000b: "HIDP_STATUS_NOT_VALUE_ARRAY",
    0xc011000c: "HIDP_STATUS_IS_VALUE_ARRAY",
    0xc011000d: "HIDP_STATUS_DATA_INDEX_NOT_FOUND",
    0xc011000e: "HIDP_STATUS_DATA_INDEX_OUT_OF_RANGE",
    0xc011000f: "HIDP_STATUS_BUTTON_NOT_PRESSED",
    0xc0110010: "HIDP_STATUS_REPORT_DOES_NOT_EXIST",
    0xc0110020: "HIDP_STATUS_NOT_IMPLEMENTED",
}
HIDP_REPORT_TYPE = {
    "HidP_Input": 0,
    "HidP_Output": 1,
    "HidP_Feature": 2,
}
HIDP_REPORT_TYPE_INV = {
    0: "HidP_Input",
    1: "HidP_Output",
    2: "HidP_Feature",
}
HIDP_KEYBOARD_DIRECTION = {
    "HidP_Keyboard_Break": 0,
    "HidP_Keyboard_Make": 1,
}
HIDP_KEYBOARD_DIRECTION_INV = {
    0: "HidP_Keyboard_Break",
    1: "HidP_Keyboard_Make",
}

###################

###### Types ######
USAGE = USHORT
PUSAGE = Ptr("<I", USAGE())
PHIDP_INSERT_SCANCODES = Ptr("<I", LPVOID())
PHIDP_PREPARSED_DATA = LPVOID
PHIDP_PREPARSED_DATA_PTR = Ptr("<I", PHIDP_PREPARSED_DATA())
PDRIVER_OBJECT = LPVOID
ULONG__10_ = Array(ULONG, 10)
USHORT__5_ = Array(USHORT, 5)
USHORT__17_ = Array(USHORT, 17)
_HIDP_STATUS_ = UINT
HIDP_REPORT_TYPE = UINT
HIDP_KEYBOARD_DIRECTION = UINT

class HIDD_ATTRIBUTES(MemStruct):
    fields = [
        ("Size", ULONG()),
        ("VendorID", USHORT()),
        ("ProductID", USHORT()),
        ("VersionNumber", USHORT()),
    ]

PHIDD_ATTRIBUTES = Ptr("<I", HIDD_ATTRIBUTES())

class HIDP_LINK_COLLECTION_NODE(MemStruct):
    fields = [
        ("LinkUsage", USAGE()),
        ("LinkUsagePage", USAGE()),
        ("Parent", USHORT()),
        ("NumberOfChildren", USHORT()),
        ("NextSibling", USHORT()),
        ("FirstChild", USHORT()),
        ("Reserved", ULONG()),
        ("UserContext", PVOID()),
    ]

PHIDP_LINK_COLLECTION_NODE = Ptr("<I", HIDP_LINK_COLLECTION_NODE())

class USAGE_AND_PAGE(MemStruct):
    fields = [
        ("Usage", USAGE()),
        ("UsagePage", USAGE()),
    ]

PUSAGE_AND_PAGE = Ptr("<I", USAGE_AND_PAGE())

class HID_MINIDRIVER_REGISTRATION(MemStruct):
    fields = [
        ("Revision", ULONG()),
        ("DriverObject", PDRIVER_OBJECT()),
        ("RegistryPath", PUNICODE_STRING()),
        ("DeviceExtensionSize", ULONG()),
        ("DevicesArePolled", BOOLEAN()),
        ("Reserved", UCHAR__3_()),
    ]

PHID_MINIDRIVER_REGISTRATION = Ptr("<I", HID_MINIDRIVER_REGISTRATION())

class HIDP_UNKNOWN_TOKEN(MemStruct):
    fields = [
        ("Token", UCHAR()),
        ("Reserved", UCHAR__3_()),
        ("BitField", ULONG()),
    ]

PHIDP_UNKNOWN_TOKEN = Ptr("<I", HIDP_UNKNOWN_TOKEN())

class HIDP_EXTENDED_ATTRIBUTES(MemStruct):
    fields = [
        ("NumGlobalUnknowns", UCHAR()),
        ("Reserved", UCHAR__3_()),
        ("GlobalUnknowns", PHIDP_UNKNOWN_TOKEN()),
        ("Data", ULONG__1_()),
    ]

PHIDP_EXTENDED_ATTRIBUTES = Ptr("<I", HIDP_EXTENDED_ATTRIBUTES())
_HIDP_DATA_u_ = Union([
    ("RawValue", ULONG),
    ("On", BOOLEAN),
])

class HIDP_DATA(MemStruct):
    fields = [
        ("DataIndex", USHORT()),
        ("Reserved", USHORT()),
        (None, _HIDP_DATA_u_()),
    ]

PHIDP_DATA = Ptr("<I", HIDP_DATA())

class HIDP_CAPS(MemStruct):
    fields = [
        ("Usage", USAGE()),
        ("UsagePage", USAGE()),
        ("InputReportByteLength", USHORT()),
        ("OutputReportByteLength", USHORT()),
        ("FeatureReportByteLength", USHORT()),
        ("Reserved", USHORT__17_()),
        ("NumberLinkCollectionNodes", USHORT()),
        ("NumberInputButtonCaps", USHORT()),
        ("NumberInputValueCaps", USHORT()),
        ("NumberInputDataIndices", USHORT()),
        ("NumberOutputButtonCaps", USHORT()),
        ("NumberOutputValueCaps", USHORT()),
        ("NumberOutputDataIndices", USHORT()),
        ("NumberFeatureButtonCaps", USHORT()),
        ("NumberFeatureValueCaps", USHORT()),
        ("NumberFeatureDataIndices", USHORT()),
    ]

PHIDP_CAPS = Ptr("<I", HIDP_CAPS())

class _HIDP_BUTTON_CAPS_s1_(MemStruct):
    fields = [
        ("UsageMin", USAGE()),
        ("UsageMax", USAGE()),
        ("StringMin", USHORT()),
        ("StringMax", USHORT()),
        ("DesignatorMin", USHORT()),
        ("DesignatorMax", USHORT()),
        ("DataIndexMin", USHORT()),
        ("DataIndexMax", USHORT()),
    ]


class _HIDP_BUTTON_CAPS_s2_(MemStruct):
    fields = [
        ("Usage", USAGE()),
        ("Reserved1", USAGE()),
        ("StringIndex", USHORT()),
        ("Reserved2", USHORT()),
        ("DesignatorIndex", USHORT()),
        ("Reserved3", USHORT()),
        ("DataIndex", USHORT()),
        ("Reserved4", USHORT()),
    ]

_HIDP_BUTTON_CAPS_u_ = Union([
    ("Range", _HIDP_BUTTON_CAPS_s1_),
    ("NotRange", _HIDP_BUTTON_CAPS_s2_),
])

class HIDP_BUTTON_CAPS(MemStruct):
    fields = [
        ("UsagePage", USAGE()),
        ("ReportID", UCHAR()),
        ("IsAlias", BOOLEAN()),
        ("BitField", USHORT()),
        ("LinkCollection", USHORT()),
        ("LinkUsage", USAGE()),
        ("LinkUsagePage", USAGE()),
        ("IsRange", BOOLEAN()),
        ("IsStringRange", BOOLEAN()),
        ("IsDesignatorRange", BOOLEAN()),
        ("IsAbsolute", BOOLEAN()),
        ("Reserved", ULONG__10_()),
        (None, _HIDP_BUTTON_CAPS_u_()),
    ]

PHIDP_BUTTON_CAPS = Ptr("<I", HIDP_BUTTON_CAPS())

class _HIDP_VALUE_CAPS_s1_(MemStruct):
    fields = [
        ("UsageMin", USAGE()),
        ("UsageMax", USAGE()),
        ("StringMin", USHORT()),
        ("StringMax", USHORT()),
        ("DesignatorMin", USHORT()),
        ("DesignatorMax", USHORT()),
        ("DataIndexMin", USHORT()),
        ("DataIndexMax", USHORT()),
    ]


class _HIDP_VALUE_CAPS_s2_(MemStruct):
    fields = [
        ("Usage", USAGE()),
        ("Reserved1", USAGE()),
        ("StringIndex", USHORT()),
        ("Reserved2", USHORT()),
        ("DesignatorIndex", USHORT()),
        ("Reserved3", USHORT()),
        ("DataIndex", USHORT()),
        ("Reserved4", USHORT()),
    ]

_HIDP_VALUE_CAPS_u_ = Union([
    ("Range", _HIDP_VALUE_CAPS_s1_),
    ("NotRange", _HIDP_VALUE_CAPS_s2_),
])

class HIDP_VALUE_CAPS(MemStruct):
    fields = [
        ("UsagePage", USAGE()),
        ("ReportID", UCHAR()),
        ("IsAlias", BOOLEAN()),
        ("BitField", USHORT()),
        ("LinkCollection", USHORT()),
        ("LinkUsage", USAGE()),
        ("LinkUsagePage", USAGE()),
        ("IsRange", BOOLEAN()),
        ("IsStringRange", BOOLEAN()),
        ("IsDesignatorRange", BOOLEAN()),
        ("IsAbsolute", BOOLEAN()),
        ("HasNull", BOOLEAN()),
        ("Reserved", UCHAR()),
        ("BitSize", USHORT()),
        ("ReportCount", USHORT()),
        ("Reserved2", USHORT__5_()),
        ("UnitsExp", ULONG()),
        ("Units", ULONG()),
        ("LogicalMin", LONG()),
        ("LogicalMax", LONG()),
        ("PhysicalMin", LONG()),
        ("PhysicalMax", LONG()),
        (None, _HIDP_VALUE_CAPS_u_()),
    ]

PHIDP_VALUE_CAPS = Ptr("<I", HIDP_VALUE_CAPS())

class HIDP_KEYBOARD_MODIFIER_STATE(MemStruct):
    fields = [
        ("ul", ULONG()),
    ]

PHIDP_KEYBOARD_MODIFIER_STATE = Ptr("<I", HIDP_KEYBOARD_MODIFIER_STATE())

class HIDD_CONFIGURATION(MemStruct):
    fields = [
        ("cookie", PVOID()),
        ("size", ULONG()),
        ("RingBufferSize", ULONG()),
    ]

PHIDD_CONFIGURATION = Ptr("<I", HIDD_CONFIGURATION())

###################

###### Functions ######

def hid_HidD_FlushQueue(jitter):
    """
    BOOLEAN HidD_FlushQueue(
        HANDLE HidDeviceObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_FreePreparsedData(jitter):
    """
    BOOLEAN HidD_FreePreparsedData(
        PHIDP_PREPARSED_DATA PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetAttributes(jitter):
    """
    BOOLEAN HidD_GetAttributes(
        HANDLE HidDeviceObject,
        PHIDD_ATTRIBUTES Attributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Attributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetFeature(jitter):
    """
    BOOLEAN HidD_GetFeature(
        HANDLE HidDeviceObject,
        PVOID ReportBuffer,
        ULONG ReportBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "ReportBuffer", "ReportBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetHidGuid(jitter):
    """
    void HidD_GetHidGuid(
        LPGUID HidGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetIndexedString(jitter):
    """
    BOOLEAN HidD_GetIndexedString(
        HANDLE HidDeviceObject,
        ULONG StringIndex,
        PVOID Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "StringIndex", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetInputReport(jitter):
    """
    BOOLEAN HidD_GetInputReport(
        HANDLE HidDeviceObject,
        PVOID ReportBuffer,
        ULONG ReportBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "ReportBuffer", "ReportBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetManufacturerString(jitter):
    """
    BOOLEAN HidD_GetManufacturerString(
        HANDLE HidDeviceObject,
        PVOID Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetNumInputBuffers(jitter):
    """
    BOOLEAN HidD_GetNumInputBuffers(
        HANDLE HidDeviceObject,
        PULONG NumberBuffers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "NumberBuffers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetPhysicalDescriptor(jitter):
    """
    BOOLEAN HidD_GetPhysicalDescriptor(
        HANDLE HidDeviceObject,
        PVOID Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetPreparsedData(jitter):
    """
    BOOLEAN HidD_GetPreparsedData(
        HANDLE HidDeviceObject,
        PHIDP_PREPARSED_DATA* PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetProductString(jitter):
    """
    BOOLEAN HidD_GetProductString(
        HANDLE HidDeviceObject,
        PVOID Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetSerialNumberString(jitter):
    """
    BOOLEAN HidD_GetSerialNumberString(
        HANDLE HidDeviceObject,
        PVOID Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_SetFeature(jitter):
    """
    BOOLEAN HidD_SetFeature(
        HANDLE HidDeviceObject,
        PVOID ReportBuffer,
        ULONG ReportBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "ReportBuffer", "ReportBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_SetNumInputBuffers(jitter):
    """
    BOOLEAN HidD_SetNumInputBuffers(
        HANDLE HidDeviceObject,
        ULONG NumberBuffers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "NumberBuffers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_SetOutputReport(jitter):
    """
    BOOLEAN HidD_SetOutputReport(
        HANDLE HidDeviceObject,
        PVOID ReportBuffer,
        ULONG ReportBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "ReportBuffer", "ReportBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetButtonCaps(jitter):
    """
    [HIDP_STATUS] HidP_GetButtonCaps(
        HIDP_REPORT_TYPE ReportType,
        PHIDP_BUTTON_CAPS ButtonCaps,
        PUSHORT ButtonCapsLength,
        PHIDP_PREPARSED_DATA PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "ButtonCaps", "ButtonCapsLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetCaps(jitter):
    """
    [HIDP_STATUS] HidP_GetCaps(
        PHIDP_PREPARSED_DATA PreparsedData,
        PHIDP_CAPS Capabilities
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PreparsedData", "Capabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetData(jitter):
    """
    [HIDP_STATUS] HidP_GetData(
        HIDP_REPORT_TYPE ReportType,
        PHIDP_DATA DataList,
        PULONG DataLength,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "DataList", "DataLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetExtendedAttributes(jitter):
    """
    [HIDP_STATUS] HidP_GetExtendedAttributes(
        HIDP_REPORT_TYPE ReportType,
        USHORT DataIndex,
        PHIDP_PREPARSED_DATA PreparsedData,
        PHIDP_EXTENDED_ATTRIBUTES Attributes,
        PULONG LengthAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "DataIndex", "PreparsedData", "Attributes", "LengthAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetLinkCollectionNodes(jitter):
    """
    [HIDP_STATUS] HidP_GetLinkCollectionNodes(
        PHIDP_LINK_COLLECTION_NODE LinkCollectionNodes,
        PULONG LinkCollectionNodesLength,
        PHIDP_PREPARSED_DATA PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LinkCollectionNodes", "LinkCollectionNodesLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetScaledUsageValue(jitter):
    """
    [HIDP_STATUS] HidP_GetScaledUsageValue(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        USAGE Usage,
        PLONG UsageValue,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetSpecificButtonCaps(jitter):
    """
    [HIDP_STATUS] HidP_GetSpecificButtonCaps(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        USAGE Usage,
        PHIDP_BUTTON_CAPS ButtonCaps,
        PUSHORT ButtonCapsLength,
        PHIDP_PREPARSED_DATA PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "ButtonCaps", "ButtonCapsLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetSpecificValueCaps(jitter):
    """
    [HIDP_STATUS] HidP_GetSpecificValueCaps(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        USAGE Usage,
        PHIDP_VALUE_CAPS ValueCaps,
        PUSHORT ValueCapsLength,
        PHIDP_PREPARSED_DATA PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "ValueCaps", "ValueCapsLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetUsages(jitter):
    """
    [HIDP_STATUS] HidP_GetUsages(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        PUSAGE UsageList,
        PULONG UsageLength,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "UsageList", "UsageLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetUsagesEx(jitter):
    """
    [HIDP_STATUS] HidP_GetUsagesEx(
        HIDP_REPORT_TYPE ReportType,
        USHORT LinkCollection,
        PUSAGE_AND_PAGE ButtonList,
        ULONG* UsageLength,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "LinkCollection", "ButtonList", "UsageLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetUsageValue(jitter):
    """
    [HIDP_STATUS] HidP_GetUsageValue(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        USAGE Usage,
        PULONG UsageValue,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetUsageValueArray(jitter):
    """
    [HIDP_STATUS] HidP_GetUsageValueArray(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        USAGE Usage,
        PCHAR UsageValue,
        USHORT UsageValueByteLength,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "UsageValueByteLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetValueCaps(jitter):
    """
    [HIDP_STATUS] HidP_GetValueCaps(
        HIDP_REPORT_TYPE ReportType,
        PHIDP_VALUE_CAPS ValueCaps,
        PUSHORT ValueCapsLength,
        PHIDP_PREPARSED_DATA PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "ValueCaps", "ValueCapsLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_InitializeReportForID(jitter):
    """
    [HIDP_STATUS] HidP_InitializeReportForID(
        HIDP_REPORT_TYPE ReportType,
        UCHAR ReportID,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "ReportID", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_IsSameUsageAndPage(jitter):
    """
    BOOLEAN HidP_IsSameUsageAndPage(
        USAGE_AND_PAGE u1,
        USAGE_AND_PAGE u2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["u1", "u2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_MaxDataListLength(jitter):
    """
    ULONG HidP_MaxDataListLength(
        HIDP_REPORT_TYPE ReportType,
        PHIDP_PREPARSED_DATA PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_MaxUsageListLength(jitter):
    """
    ULONG HidP_MaxUsageListLength(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        PHIDP_PREPARSED_DATA PreparsedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetData(jitter):
    """
    [HIDP_STATUS] HidP_SetData(
        HIDP_REPORT_TYPE ReportType,
        PHIDP_DATA DataList,
        PULONG DataLength,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "DataList", "DataLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetScaledUsageValue(jitter):
    """
    [HIDP_STATUS] HidP_SetScaledUsageValue(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        USAGE Usage,
        LONG UsageValue,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetUsages(jitter):
    """
    [HIDP_STATUS] HidP_SetUsages(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        PUSAGE UsageList,
        PULONG UsageLength,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "UsageList", "UsageLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetUsageValue(jitter):
    """
    [HIDP_STATUS] HidP_SetUsageValue(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        USAGE Usage,
        ULONG UsageValue,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetUsageValueArray(jitter):
    """
    [HIDP_STATUS] HidP_SetUsageValueArray(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        USAGE Usage,
        PCHAR UsageValue,
        USHORT UsageValueByteLength,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "UsageValueByteLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_TranslateUsagesToI8042ScanCodes(jitter):
    """
    [HIDP_STATUS] HidP_TranslateUsagesToI8042ScanCodes(
        PUSAGE ChangedUsageList,
        ULONG UsageListLength,
        HIDP_KEYBOARD_DIRECTION KeyAction,
        PHIDP_KEYBOARD_MODIFIER_STATE ModifierState,
        PHIDP_INSERT_SCANCODES InsertCodesProcedure,
        PVOID InsertCodesContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ChangedUsageList", "UsageListLength", "KeyAction", "ModifierState", "InsertCodesProcedure", "InsertCodesContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_UnsetUsages(jitter):
    """
    [HIDP_STATUS] HidP_UnsetUsages(
        HIDP_REPORT_TYPE ReportType,
        USAGE UsagePage,
        USHORT LinkCollection,
        PUSAGE UsageList,
        PULONG UsageLength,
        PHIDP_PREPARSED_DATA PreparsedData,
        PCHAR Report,
        ULONG ReportLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "UsageList", "UsageLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_UsageListDifference(jitter):
    """
    [HIDP_STATUS] HidP_UsageListDifference(
        PUSAGE PreviousUsageList,
        PUSAGE CurrentUsageList,
        PUSAGE BreakUsageList,
        PUSAGE MakeUsageList,
        ULONG UsageListLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PreviousUsageList", "CurrentUsageList", "BreakUsageList", "MakeUsageList", "UsageListLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetConfiguration(jitter):
    """
    BOOLEAN HidD_GetConfiguration(
        HANDLE HidDeviceObject,
        PHIDD_CONFIGURATION Configuration,
        ULONG ConfigurationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Configuration", "ConfigurationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_SetConfiguration(jitter):
    """
    BOOLEAN HidD_SetConfiguration(
        HANDLE HidDeviceObject,
        PHIDD_CONFIGURATION Configuration,
        ULONG ConfigurationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Configuration", "ConfigurationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetMsGenreDescriptor(jitter):
    """
    BOOLEAN HidD_GetMsGenreDescriptor(
        HANDLE HidDeviceObject,
        PVOID Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_Hello(jitter):
    """
    ULONG HidD_Hello(
        PCHAR Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
