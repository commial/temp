
def hid_HidD_FlushQueue(jitter):
    """
    [hid.dll] BOOLEAN HidD_FlushQueue(HANDLE HidDeviceObject)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_FreePreparsedData(jitter):
    """
    [hid.dll] BOOLEAN HidD_FreePreparsedData(PHIDP_PREPARSED_DATA PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetAttributes(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetAttributes(HANDLE HidDeviceObject, PHIDD_ATTRIBUTES Attributes)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Attributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetFeature(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetFeature(HANDLE HidDeviceObject, PVOID ReportBuffer, ULONG ReportBufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "ReportBuffer", "ReportBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetHidGuid(jitter):
    """
    [hid.dll] void HidD_GetHidGuid(LPGUID HidGuid)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetIndexedString(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetIndexedString(HANDLE HidDeviceObject, ULONG StringIndex, PVOID Buffer, ULONG BufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "StringIndex", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetInputReport(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetInputReport(HANDLE HidDeviceObject, PVOID ReportBuffer, ULONG ReportBufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "ReportBuffer", "ReportBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetManufacturerString(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetManufacturerString(HANDLE HidDeviceObject, PVOID Buffer, ULONG BufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetNumInputBuffers(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetNumInputBuffers(HANDLE HidDeviceObject, PULONG NumberBuffers)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "NumberBuffers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetPhysicalDescriptor(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetPhysicalDescriptor(HANDLE HidDeviceObject, PVOID Buffer, ULONG BufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetPreparsedData(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetPreparsedData(HANDLE HidDeviceObject, PHIDP_PREPARSED_DATA* PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetProductString(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetProductString(HANDLE HidDeviceObject, PVOID Buffer, ULONG BufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetSerialNumberString(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetSerialNumberString(HANDLE HidDeviceObject, PVOID Buffer, ULONG BufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_SetFeature(jitter):
    """
    [hid.dll] BOOLEAN HidD_SetFeature(HANDLE HidDeviceObject, PVOID ReportBuffer, ULONG ReportBufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "ReportBuffer", "ReportBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_SetNumInputBuffers(jitter):
    """
    [hid.dll] BOOLEAN HidD_SetNumInputBuffers(HANDLE HidDeviceObject, ULONG NumberBuffers)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "NumberBuffers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_SetOutputReport(jitter):
    """
    [hid.dll] BOOLEAN HidD_SetOutputReport(HANDLE HidDeviceObject, PVOID ReportBuffer, ULONG ReportBufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "ReportBuffer", "ReportBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetButtonCaps(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetButtonCaps(HIDP_REPORT_TYPE ReportType, PHIDP_BUTTON_CAPS ButtonCaps, PUSHORT ButtonCapsLength, PHIDP_PREPARSED_DATA PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "ButtonCaps", "ButtonCapsLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetCaps(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetCaps(PHIDP_PREPARSED_DATA PreparsedData, PHIDP_CAPS Capabilities)
    """
    ret_ad, args = jitter.func_args_stdcall(["PreparsedData", "Capabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetData(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetData(HIDP_REPORT_TYPE ReportType, PHIDP_DATA DataList, PULONG DataLength, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "DataList", "DataLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetExtendedAttributes(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetExtendedAttributes(HIDP_REPORT_TYPE ReportType, USHORT DataIndex, PHIDP_PREPARSED_DATA PreparsedData, PHIDP_EXTENDED_ATTRIBUTES Attributes, PULONG LengthAttributes)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "DataIndex", "PreparsedData", "Attributes", "LengthAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetLinkCollectionNodes(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetLinkCollectionNodes(PHIDP_LINK_COLLECTION_NODE LinkCollectionNodes, PULONG LinkCollectionNodesLength, PHIDP_PREPARSED_DATA PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["LinkCollectionNodes", "LinkCollectionNodesLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetScaledUsageValue(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetScaledUsageValue(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, USAGE Usage, PLONG UsageValue, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetSpecificButtonCaps(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetSpecificButtonCaps(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, USAGE Usage, PHIDP_BUTTON_CAPS ButtonCaps, PUSHORT ButtonCapsLength, PHIDP_PREPARSED_DATA PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "ButtonCaps", "ButtonCapsLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetSpecificValueCaps(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetSpecificValueCaps(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, USAGE Usage, PHIDP_VALUE_CAPS ValueCaps, PUSHORT ValueCapsLength, PHIDP_PREPARSED_DATA PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "ValueCaps", "ValueCapsLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetUsages(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetUsages(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, PUSAGE UsageList, PULONG UsageLength, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "UsageList", "UsageLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetUsagesEx(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetUsagesEx(HIDP_REPORT_TYPE ReportType, USHORT LinkCollection, PUSAGE_AND_PAGE ButtonList, ULONG* UsageLength, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "LinkCollection", "ButtonList", "UsageLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetUsageValue(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetUsageValue(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, USAGE Usage, PULONG UsageValue, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetUsageValueArray(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetUsageValueArray(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, USAGE Usage, PCHAR UsageValue, USHORT UsageValueByteLength, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "UsageValueByteLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_GetValueCaps(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_GetValueCaps(HIDP_REPORT_TYPE ReportType, PHIDP_VALUE_CAPS ValueCaps, PUSHORT ValueCapsLength, PHIDP_PREPARSED_DATA PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "ValueCaps", "ValueCapsLength", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_InitializeReportForID(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_InitializeReportForID(HIDP_REPORT_TYPE ReportType, UCHAR ReportID, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "ReportID", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_IsSameUsageAndPage(jitter):
    """
    [hid.dll] BOOLEAN HidP_IsSameUsageAndPage(USAGE_AND_PAGE u1, USAGE_AND_PAGE u2)
    """
    ret_ad, args = jitter.func_args_stdcall(["u1", "u2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_MaxDataListLength(jitter):
    """
    [hid.dll] ULONG HidP_MaxDataListLength(HIDP_REPORT_TYPE ReportType, PHIDP_PREPARSED_DATA PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_MaxUsageListLength(jitter):
    """
    [hid.dll] ULONG HidP_MaxUsageListLength(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, PHIDP_PREPARSED_DATA PreparsedData)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "PreparsedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetData(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_SetData(HIDP_REPORT_TYPE ReportType, PHIDP_DATA DataList, PULONG DataLength, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "DataList", "DataLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetScaledUsageValue(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_SetScaledUsageValue(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, USAGE Usage, LONG UsageValue, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetUsages(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_SetUsages(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, PUSAGE UsageList, PULONG UsageLength, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "UsageList", "UsageLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetUsageValue(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_SetUsageValue(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, USAGE Usage, ULONG UsageValue, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_SetUsageValueArray(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_SetUsageValueArray(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, USAGE Usage, PCHAR UsageValue, USHORT UsageValueByteLength, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "Usage", "UsageValue", "UsageValueByteLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_TranslateUsagesToI8042ScanCodes(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_TranslateUsagesToI8042ScanCodes(PUSAGE ChangedUsageList, ULONG UsageListLength, HIDP_KEYBOARD_DIRECTION KeyAction, PHIDP_KEYBOARD_MODIFIER_STATE ModifierState, PHIDP_INSERT_SCANCODES InsertCodesProcedure, PVOID InsertCodesContext)
    """
    ret_ad, args = jitter.func_args_stdcall(["ChangedUsageList", "UsageListLength", "KeyAction", "ModifierState", "InsertCodesProcedure", "InsertCodesContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_UnsetUsages(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_UnsetUsages(HIDP_REPORT_TYPE ReportType, USAGE UsagePage, USHORT LinkCollection, PUSAGE UsageList, PULONG UsageLength, PHIDP_PREPARSED_DATA PreparsedData, PCHAR Report, ULONG ReportLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["ReportType", "UsagePage", "LinkCollection", "UsageList", "UsageLength", "PreparsedData", "Report", "ReportLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidP_UsageListDifference(jitter):
    """
    [hid.dll] [HIDP_STATUS] HidP_UsageListDifference(PUSAGE PreviousUsageList, PUSAGE CurrentUsageList, PUSAGE BreakUsageList, PUSAGE MakeUsageList, ULONG UsageListLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["PreviousUsageList", "CurrentUsageList", "BreakUsageList", "MakeUsageList", "UsageListLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetConfiguration(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetConfiguration(HANDLE HidDeviceObject, PHIDD_CONFIGURATION Configuration, ULONG ConfigurationLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Configuration", "ConfigurationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_SetConfiguration(jitter):
    """
    [hid.dll] BOOLEAN HidD_SetConfiguration(HANDLE HidDeviceObject, PHIDD_CONFIGURATION Configuration, ULONG ConfigurationLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Configuration", "ConfigurationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_GetMsGenreDescriptor(jitter):
    """
    [hid.dll] BOOLEAN HidD_GetMsGenreDescriptor(HANDLE HidDeviceObject, PVOID Buffer, ULONG BufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["HidDeviceObject", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def hid_HidD_Hello(jitter):
    """
    [hid.dll] ULONG HidD_Hello(PCHAR Buffer, ULONG BufferLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
