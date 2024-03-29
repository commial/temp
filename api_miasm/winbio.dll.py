###### Enums ######
WINBIO_POOL_TYPE = {
    "WINBIO_POOL_UNKNOWN": 0,
    "WINBIO_POOL_SYSTEM": 1,
    "WINBIO_POOL_PRIVATE": 2,
    "WINBIO_POOL_UNASSIGNED": 3,
}
WINBIO_POOL_TYPE_INV = {
    0: "WINBIO_POOL_UNKNOWN",
    1: "WINBIO_POOL_SYSTEM",
    2: "WINBIO_POOL_PRIVATE",
    3: "WINBIO_POOL_UNASSIGNED",
}
WINBIO_IDENTITY_TYPE = {
    "WINBIO_ID_TYPE_NULL": 0,
    "WINBIO_ID_TYPE_WILDCARD": 1,
    "WINBIO_ID_TYPE_GUID": 2,
    "WINBIO_ID_TYPE_SID": 3,
}
WINBIO_IDENTITY_TYPE_INV = {
    0: "WINBIO_ID_TYPE_NULL",
    1: "WINBIO_ID_TYPE_WILDCARD",
    2: "WINBIO_ID_TYPE_GUID",
    3: "WINBIO_ID_TYPE_SID",
}
WINBIO_PROPERTY_TYPE = {
    "WINBIO_PROPERTY_TYPE_SESSION": 1,
    "WINBIO_PROPERTY_TYPE_UNIT": 2,
    "WINBIO_PROPERTY_TYPE_TEMPLATE": 3,
}
WINBIO_PROPERTY_TYPE_INV = {
    1: "WINBIO_PROPERTY_TYPE_SESSION",
    2: "WINBIO_PROPERTY_TYPE_UNIT",
    3: "WINBIO_PROPERTY_TYPE_TEMPLATE",
}
WINBIO_CREDENTIAL_FORMAT = {
    "WINBIO_PASSWORD_GENERIC": 0x00000001,
    "WINBIO_PASSWORD_PACKED": 0x00000002,
}
WINBIO_CREDENTIAL_FORMAT_INV = {
    0x00000001: "WINBIO_PASSWORD_GENERIC",
    0x00000002: "WINBIO_PASSWORD_PACKED",
}
WINBIO_COMPONENT = {
    "WINBIO_COMPONENT_SENSOR": 1,
    "WINBIO_COMPONENT_ENGINE": 2,
    "WINBIO_COMPONENT_STORAGE": 3,
}
WINBIO_COMPONENT_INV = {
    1: "WINBIO_COMPONENT_SENSOR",
    2: "WINBIO_COMPONENT_ENGINE",
    3: "WINBIO_COMPONENT_STORAGE",
}
WINBIO_BIOMETRIC_SUBTYPE = {
    "WINBIO_SUBTYPE_NO_INFORMATION": 0x00,
    "WINBIO_SUBTYPE_ANY": 0xFF,
}
WINBIO_BIOMETRIC_SUBTYPE_INV = {
    0x00: "WINBIO_SUBTYPE_NO_INFORMATION",
    0xFF: "WINBIO_SUBTYPE_ANY",
}
WINBIO_REJECT_DETAIL = {
    "WINBIO_FP_TOO_HIGH": 1,
    "WINBIO_FP_TOO_LOW": 2,
    "WINBIO_FP_TOO_LEFT": 3,
    "WINBIO_FP_TOO_RIGHT": 4,
    "WINBIO_FP_TOO_FAST": 5,
    "WINBIO_FP_TOO_SLOW": 6,
    "WINBIO_FP_POOR_QUALITY": 7,
    "WINBIO_FP_TOO_SKEWED": 8,
    "WINBIO_FP_TOO_SHORT": 9,
    "WINBIO_FP_MERGE_FAILURE": 10,
}
WINBIO_REJECT_DETAIL_INV = {
    1: "WINBIO_FP_TOO_HIGH",
    2: "WINBIO_FP_TOO_LOW",
    3: "WINBIO_FP_TOO_LEFT",
    4: "WINBIO_FP_TOO_RIGHT",
    5: "WINBIO_FP_TOO_FAST",
    6: "WINBIO_FP_TOO_SLOW",
    7: "WINBIO_FP_POOR_QUALITY",
    8: "WINBIO_FP_TOO_SKEWED",
    9: "WINBIO_FP_TOO_SHORT",
    10: "WINBIO_FP_MERGE_FAILURE",
}
WINBIO_EVENT_TYPE = {
    "WINBIO_EVENT_ERROR": 0xFFFFFFFF,
    "WINBIO_EVENT_FP_UNCLAIMED": 0x00000001,
    "WINBIO_EVENT_FP_UNCLAIMED_IDENTIFY": 0x00000002,
}
WINBIO_EVENT_TYPE_INV = {
    0xFFFFFFFF: "WINBIO_EVENT_ERROR",
    0x00000001: "WINBIO_EVENT_FP_UNCLAIMED",
    0x00000002: "WINBIO_EVENT_FP_UNCLAIMED_IDENTIFY",
}
WINBIO_SETTING_SOURCE_TYPE = {
    "WINBIO_SETTING_SOURCE_INVALID": 0,
    "WINBIO_SETTING_SOURCE_DEFAULT": 1,
    "WINBIO_SETTING_SOURCE_POLICY": 2,
    "WINBIO_SETTING_SOURCE_LOCAL": 3,
}
WINBIO_SETTING_SOURCE_TYPE_INV = {
    0: "WINBIO_SETTING_SOURCE_INVALID",
    1: "WINBIO_SETTING_SOURCE_DEFAULT",
    2: "WINBIO_SETTING_SOURCE_POLICY",
    3: "WINBIO_SETTING_SOURCE_LOCAL",
}
WINBIO_PROPERTY_ID = {
    "WINBIO_PROPERTY_SAMPLE_HINT": 1,
}
WINBIO_PROPERTY_ID_INV = {
    1: "WINBIO_PROPERTY_SAMPLE_HINT",
}
WINBIO_CREDENTIAL_STATE = {
    "WINBIO_CREDENTIAL_NOT_SET": 0x00000001,
    "WINBIO_CREDENTIAL_SET": 0x00000002,
}
WINBIO_CREDENTIAL_STATE_INV = {
    0x00000001: "WINBIO_CREDENTIAL_NOT_SET",
    0x00000002: "WINBIO_CREDENTIAL_SET",
}
WINBIO_ASYNC_NOTIFICATION_METHOD = {
    "WINBIO_ASYNC_NOTIFY_NONE": 0,
    "WINBIO_ASYNC_NOTIFY_CALLBACK": 1,
    "WINBIO_ASYNC_NOTIFY_MESSAGE": 2,
}
WINBIO_ASYNC_NOTIFICATION_METHOD_INV = {
    0: "WINBIO_ASYNC_NOTIFY_NONE",
    1: "WINBIO_ASYNC_NOTIFY_CALLBACK",
    2: "WINBIO_ASYNC_NOTIFY_MESSAGE",
}

###################

###### Types ######
WINBIO_SESSION_HANDLE = ULONG
WINBIO_SESSION_HANDLE_PTR = Ptr("<I", WINBIO_SESSION_HANDLE())
WINBIO_UNIT_ID = ULONG
WINBIO_UNIT_ID_PTR = Ptr("<I", WINBIO_UNIT_ID())
PWINBIO_ENROLL_CAPTURE_CALLBACK = LPVOID
PWINBIO_IDENTIFY_CALLBACK = LPVOID
PWINBIO_LOCATE_SENSOR_CALLBACK = LPVOID
PWINBIO_EVENT_CALLBACK = LPVOID
PWINBIO_CAPTURE_CALLBACK = LPVOID
PWINBIO_VERIFY_CALLBACK = LPVOID
WINBIO_UUID = UUID
WINBIO_BIOMETRIC_SENSOR_SUBTYPE = ULONG
WINBIO_FRAMEWORK_HANDLE = WINBIO_SESSION_HANDLE
WINBIO_FRAMEWORK_HANDLE_PTR = Ptr("<I", WINBIO_FRAMEWORK_HANDLE())
WINBIO_FRAMEWORK_CHANGE_TYPE = ULONG
PWINBIO_ASYNC_COMPLETION_CALLBACK = LPVOID
WINBIO_STRING = Array(WCHAR, 256)
UCHAR__SECURITY_MAX_SID_SIZE_ = Array(UCHAR, 68)
WINBIO_BIOMETRIC_TYPE = ULONG
WINBIO_POOL_TYPE = ULONG

class WINBIO_VERSION(MemStruct):
    fields = [
        ("MajorVersion", DWORD()),
        ("MinorVersion", DWORD()),
    ]

WINBIO_IDENTITY_TYPE = UINT

class _WINBIO_IDENTITY_u_s_(MemStruct):
    fields = [
        ("Size", ULONG()),
        ("Data", UCHAR__SECURITY_MAX_SID_SIZE_()),
    ]

_WINBIO_IDENTITY_u_ = Union([
    ("Null", ULONG),
    ("Wildcard", ULONG),
    ("TemplateGuid", GUID),
    ("AccountSid", _WINBIO_IDENTITY_u_s_),
])

class WINBIO_IDENTITY(MemStruct):
    fields = [
        ("Type", WINBIO_IDENTITY_TYPE()),
        ("Value", _WINBIO_IDENTITY_u_()),
    ]

WINBIO_IDENTITY_PTR = Ptr("<I", WINBIO_IDENTITY())
WINBIO_CAPABILITIES = ULONG

class WINBIO_UNIT_SCHEMA(MemStruct):
    fields = [
        ("UnitId", WINBIO_UNIT_ID()),
        ("PoolType", WINBIO_POOL_TYPE()),
        ("BiometricFactor", WINBIO_BIOMETRIC_TYPE()),
        ("SensorSubType", WINBIO_BIOMETRIC_SENSOR_SUBTYPE()),
        ("Capabilities", WINBIO_CAPABILITIES()),
        ("DeviceInstanceId", WINBIO_STRING()),
        ("Description", WINBIO_STRING()),
        ("Manufacturer", WINBIO_STRING()),
        ("Model", WINBIO_STRING()),
        ("SerialNumber", WINBIO_STRING()),
        ("FirmwareVersion", WINBIO_VERSION()),
    ]

WINBIO_UNIT_SCHEMA_PTR = Ptr("<I", WINBIO_UNIT_SCHEMA())
WINBIO_UNIT_SCHEMA_PTR_PTR = Ptr("<I", WINBIO_UNIT_SCHEMA_PTR())
_WINBIO_DATABASE_ATTRIBUTES_ = ULONG

class WINBIO_STORAGE_SCHEMA(MemStruct):
    fields = [
        ("BiometricFactor", WINBIO_BIOMETRIC_TYPE()),
        ("DatabaseId", WINBIO_UUID()),
        ("DataFormat", WINBIO_UUID()),
        ("Attributes", _WINBIO_DATABASE_ATTRIBUTES_()),
        ("FilePath", WINBIO_STRING()),
        ("ConnectionString", WINBIO_STRING()),
    ]

WINBIO_STORAGE_SCHEMA_PTR = Ptr("<I", WINBIO_STORAGE_SCHEMA())
WINBIO_STORAGE_SCHEMA_PTR_PTR = Ptr("<I", WINBIO_STORAGE_SCHEMA_PTR())

class WINBIO_BSP_SCHEMA(MemStruct):
    fields = [
        ("BiometricFactor", WINBIO_BIOMETRIC_TYPE()),
        ("BspId", WINBIO_UUID()),
        ("Description", WINBIO_STRING()),
        ("Vendor", WINBIO_STRING()),
        ("Version", WINBIO_VERSION()),
    ]

WINBIO_BSP_SCHEMA_PTR = Ptr("<I", WINBIO_BSP_SCHEMA())
WINBIO_BSP_SCHEMA_PTR_PTR = Ptr("<I", WINBIO_BSP_SCHEMA_PTR())

class WINBIO_BIR_DATA(MemStruct):
    fields = [
        ("Size", ULONG()),
        ("Offset", ULONG()),
    ]


class WINBIO_BIR(MemStruct):
    fields = [
        ("HeaderBlock", WINBIO_BIR_DATA()),
        ("StandardDataBlock", WINBIO_BIR_DATA()),
        ("VendorDataBlock", WINBIO_BIR_DATA()),
        ("SignatureBlock", WINBIO_BIR_DATA()),
    ]

PWINBIO_BIR = Ptr("<I", WINBIO_BIR())
PWINBIO_BIR_PTR = Ptr("<I", PWINBIO_BIR())
WINBIO_PROPERTY_TYPE = ULONG
WINBIO_CREDENTIAL_FORMAT = UINT
WINBIO_COMPONENT = ULONG
WINBIO_BIR_PURPOSE = UCHAR
WINBIO_BIR_DATA_FLAGS = UCHAR
WINBIO_BIOMETRIC_SUBTYPE = UCHAR
WINBIO_BIOMETRIC_SUBTYPE_PTR = Ptr("<I", WINBIO_BIOMETRIC_SUBTYPE())
WINBIO_BIOMETRIC_SUBTYPE_PTR_PTR = Ptr("<I", WINBIO_BIOMETRIC_SUBTYPE_PTR())
WINBIO_REJECT_DETAIL = ULONG
WINBIO_REJECT_DETAIL_PTR = Ptr("<I", WINBIO_REJECT_DETAIL())
WINBIO_EVENT_TYPE = ULONG
WINBIO_SESSION_FLAGS = ULONG
WINBIO_CREDENTIAL_TYPE = UINT
WINBIO_SETTING_SOURCE_TYPE = ULONG
PWINBIO_SETTING_SOURCE_TYPE = Ptr("<I", WINBIO_SETTING_SOURCE_TYPE())
WINBIO_PROPERTY_ID = ULONG
WINBIO_CREDENTIAL_STATE = UINT
WINBIO_CREDENTIAL_STATE_PTR = Ptr("<I", WINBIO_CREDENTIAL_STATE())
WINBIO_ASYNC_NOTIFICATION_METHOD = UINT

###################

###### Functions ######

def winbio_WinBioAcquireFocus(jitter):
    """
    HRESULT WinBioAcquireFocus()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncEnumBiometricUnits(jitter):
    """
    HRESULT WinBioAsyncEnumBiometricUnits(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle,
        WINBIO_BIOMETRIC_TYPE Factor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle", "Factor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncEnumDatabases(jitter):
    """
    HRESULT WinBioAsyncEnumDatabases(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle,
        WINBIO_BIOMETRIC_TYPE Factor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle", "Factor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncEnumServiceProviders(jitter):
    """
    HRESULT WinBioAsyncEnumServiceProviders(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle,
        WINBIO_BIOMETRIC_TYPE Factor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle", "Factor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncMonitorFrameworkChanges(jitter):
    """
    HRESULT WinBioAsyncMonitorFrameworkChanges(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle,
        WINBIO_FRAMEWORK_CHANGE_TYPE ChangeTypes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle", "ChangeTypes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncOpenFramework(jitter):
    """
    HRESULT WinBioAsyncOpenFramework(
        WINBIO_ASYNC_NOTIFICATION_METHOD NotificationMethod,
        HWND TargetWindow,
        UINT MessageCode,
        PWINBIO_ASYNC_COMPLETION_CALLBACK CallbackRoutine,
        PVOID UserData,
        BOOL AsynchronousOpen,
        WINBIO_FRAMEWORK_HANDLE* FrameworkHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NotificationMethod", "TargetWindow", "MessageCode", "CallbackRoutine", "UserData", "AsynchronousOpen", "FrameworkHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioAsyncOpenSession(jitter):
    """
    HRESULT WinBioAsyncOpenSession(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_POOL_TYPE PoolType,
        WINBIO_SESSION_FLAGS Flags,
        WINBIO_UNIT_ID* UnitArray,
        SIZE_T UnitCount,
        GUID* DatabaseId,
        WINBIO_ASYNC_NOTIFICATION_METHOD NotificationMethod,
        HWND TargetWindow,
        UINT MessageCode,
        PWINBIO_ASYNC_COMPLETION_CALLBACK CallbackRoutine,
        PVOID UserData,
        BOOL AsynchronousOpen,
        WINBIO_SESSION_HANDLE* SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "PoolType", "Flags", "UnitArray", "UnitCount", "DatabaseId", "NotificationMethod", "TargetWindow", "MessageCode", "CallbackRoutine", "UserData", "AsynchronousOpen", "SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCancel(jitter):
    """
    HRESULT WinBioCancel(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCaptureSample(jitter):
    """
    HRESULT WinBioCaptureSample(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_BIR_PURPOSE Purpose,
        WINBIO_BIR_DATA_FLAGS Flags,
        WINBIO_UNIT_ID* UnitId,
        PWINBIO_BIR* Sample,
        SIZE_T* SampleSize,
        WINBIO_REJECT_DETAIL* RejectDetail
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Purpose", "Flags", "UnitId", "Sample", "SampleSize", "RejectDetail"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCaptureSampleWithCallback(jitter):
    """
    HRESULT WinBioCaptureSampleWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_BIR_PURPOSE Purpose,
        WINBIO_BIR_DATA_FLAGS Flags,
        PWINBIO_CAPTURE_CALLBACK CaptureCallback,
        PVOID CaptureCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Purpose", "Flags", "CaptureCallback", "CaptureCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCloseFramework(jitter):
    """
    HRESULT WinBioCloseFramework(
        WINBIO_FRAMEWORK_HANDLE FrameworkHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FrameworkHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioCloseSession(jitter):
    """
    HRESULT WinBioCloseSession(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioControlUnit(jitter):
    """
    HRESULT WinBioControlUnit(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId,
        WINBIO_COMPONENT Component,
        ULONG ControlCode,
        PUCHAR SendBuffer,
        SIZE_T SendBufferSize,
        PUCHAR ReceiveBuffer,
        SIZE_T ReceiveBufferSize,
        SIZE_T* ReceiveDataSize,
        ULONG* OperationStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Component", "ControlCode", "SendBuffer", "SendBufferSize", "ReceiveBuffer", "ReceiveBufferSize", "ReceiveDataSize", "OperationStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioControlUnitPrivileged(jitter):
    """
    HRESULT WinBioControlUnitPrivileged(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId,
        WINBIO_COMPONENT Component,
        ULONG ControlCode,
        PUCHAR SendBuffer,
        SIZE_T SendBufferSize,
        PUCHAR ReceiveBuffer,
        SIZE_T ReceiveBufferSize,
        SIZE_T* ReceiveDataSize,
        ULONG* OperationStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Component", "ControlCode", "SendBuffer", "SendBufferSize", "ReceiveBuffer", "ReceiveBufferSize", "ReceiveDataSize", "OperationStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioDeleteTemplate(jitter):
    """
    HRESULT WinBioDeleteTemplate(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Identity", "SubFactor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollBegin(jitter):
    """
    HRESULT WinBioEnrollBegin(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor,
        WINBIO_UNIT_ID UnitId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "SubFactor", "UnitId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollCapture(jitter):
    """
    HRESULT WinBioEnrollCapture(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_REJECT_DETAIL* RejectDetail
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "RejectDetail"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollCaptureWithCallback(jitter):
    """
    HRESULT WinBioEnrollCaptureWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        PWINBIO_ENROLL_CAPTURE_CALLBACK EnrollCallback,
        PVOID EnrollCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "EnrollCallback", "EnrollCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollCommit(jitter):
    """
    HRESULT WinBioEnrollCommit(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_IDENTITY* Identity,
        BOOLEAN* IsNewTemplate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Identity", "IsNewTemplate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnrollDiscard(jitter):
    """
    HRESULT WinBioEnrollDiscard(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnumBiometricUnits(jitter):
    """
    HRESULT WinBioEnumBiometricUnits(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_UNIT_SCHEMA** UnitSchemaArray,
        SIZE_T* UnitCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "UnitSchemaArray", "UnitCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnumDatabases(jitter):
    """
    HRESULT WinBioEnumDatabases(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_STORAGE_SCHEMA** StorageSchemaArray,
        SIZE_T* StorageCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "StorageSchemaArray", "StorageCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnumEnrollments(jitter):
    """
    HRESULT WinBioEnumEnrollments(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE** SubFactorArray,
        SIZE_T* SubFactorCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Identity", "SubFactorArray", "SubFactorCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioEnumServiceProviders(jitter):
    """
    HRESULT WinBioEnumServiceProviders(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_BSP_SCHEMA** BspSchemaArray,
        SIZE_T* BspCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "BspSchemaArray", "BspCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioFree(jitter):
    """
    HRESULT WinBioFree(
        PVOID Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetCredentialState(jitter):
    """
    HRESULT WinBioGetCredentialState(
        WINBIO_IDENTITY Identity,
        WINBIO_CREDENTIAL_TYPE Type,
        WINBIO_CREDENTIAL_STATE* CredentialState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Identity", "Type", "CredentialState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetDomainLogonSetting(jitter):
    """
    HRESULT WinBioGetDomainLogonSetting(
        BOOLEAN* Value,
        PWINBIO_SETTING_SOURCE_TYPE Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetEnabledSetting(jitter):
    """
    HRESULT WinBioGetEnabledSetting(
        BOOLEAN* Value,
        PWINBIO_SETTING_SOURCE_TYPE Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetLogonSetting(jitter):
    """
    HRESULT WinBioGetLogonSetting(
        BOOLEAN* Value,
        PWINBIO_SETTING_SOURCE_TYPE Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioGetProperty(jitter):
    """
    HRESULT WinBioGetProperty(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_PROPERTY_TYPE PropertyType,
        WINBIO_PROPERTY_ID PropertyId,
        WINBIO_UNIT_ID UnitId,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor,
        PVOID* PropertyBuffer,
        SIZE_T* PropertyBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "PropertyType", "PropertyId", "UnitId", "Identity", "SubFactor", "PropertyBuffer", "PropertyBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioIdentify(jitter):
    """
    HRESULT WinBioIdentify(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID* UnitId,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE* SubFactor,
        WINBIO_REJECT_DETAIL* RejectDetail
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId", "Identity", "SubFactor", "RejectDetail"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioIdentifyWithCallback(jitter):
    """
    HRESULT WinBioIdentifyWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        PWINBIO_IDENTIFY_CALLBACK IdentifyCallback,
        PVOID IdentifyCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "IdentifyCallback", "IdentifyCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioLocateSensor(jitter):
    """
    HRESULT WinBioLocateSensor(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID* UnitId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioLocateSensorWithCallback(jitter):
    """
    HRESULT WinBioLocateSensorWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        PWINBIO_LOCATE_SENSOR_CALLBACK LocateCallback,
        PVOID LocateCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "LocateCallback", "LocateCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioLockUnit(jitter):
    """
    HRESULT WinBioLockUnit(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioLogonIdentifiedUser(jitter):
    """
    HRESULT WinBioLogonIdentifiedUser(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioOpenSession(jitter):
    """
    HRESULT WinBioOpenSession(
        WINBIO_BIOMETRIC_TYPE Factor,
        WINBIO_POOL_TYPE PoolType,
        WINBIO_SESSION_FLAGS Flags,
        WINBIO_UNIT_ID* UnitArray,
        SIZE_T UnitCount,
        GUID* DatabaseId,
        WINBIO_SESSION_HANDLE* SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Factor", "PoolType", "Flags", "UnitArray", "UnitCount", "DatabaseId", "SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioRegisterEventMonitor(jitter):
    """
    HRESULT WinBioRegisterEventMonitor(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_EVENT_TYPE EventMask,
        PWINBIO_EVENT_CALLBACK EventCallback,
        PVOID EventCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "EventMask", "EventCallback", "EventCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioReleaseFocus(jitter):
    """
    HRESULT WinBioReleaseFocus()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioRemoveAllCredentials(jitter):
    """
    HRESULT WinBioRemoveAllCredentials()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioRemoveAllDomainCredentials(jitter):
    """
    HRESULT WinBioRemoveAllDomainCredentials()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioRemoveCredential(jitter):
    """
    HRESULT WinBioRemoveCredential(
        WINBIO_IDENTITY Identity,
        WINBIO_CREDENTIAL_TYPE Type
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Identity", "Type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioSetCredential(jitter):
    """
    HRESULT WinBioSetCredential(
        WINBIO_CREDENTIAL_TYPE Type,
        PUCHAR Credential,
        SIZE_T CredentialSize,
        WINBIO_CREDENTIAL_FORMAT Format
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Type", "Credential", "CredentialSize", "Format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioUnlockUnit(jitter):
    """
    HRESULT WinBioUnlockUnit(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_UNIT_ID UnitId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "UnitId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioUnregisterEventMonitor(jitter):
    """
    HRESULT WinBioUnregisterEventMonitor(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioVerify(jitter):
    """
    HRESULT WinBioVerify(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor,
        WINBIO_UNIT_ID* UnitId,
        BOOLEAN* Match,
        WINBIO_REJECT_DETAIL* RejectDetail
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Identity", "SubFactor", "UnitId", "Match", "RejectDetail"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioVerifyWithCallback(jitter):
    """
    HRESULT WinBioVerifyWithCallback(
        WINBIO_SESSION_HANDLE SessionHandle,
        WINBIO_IDENTITY* Identity,
        WINBIO_BIOMETRIC_SUBTYPE SubFactor,
        PWINBIO_VERIFY_CALLBACK VerifyCallback,
        PVOID VerifyCallbackContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle", "Identity", "SubFactor", "VerifyCallback", "VerifyCallbackContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winbio_WinBioWait(jitter):
    """
    HRESULT WinBioWait(
        WINBIO_SESSION_HANDLE SessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
