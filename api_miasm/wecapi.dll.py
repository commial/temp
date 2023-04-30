###### Enums ######
EC_SUBSCRIPTION_PROPERTY_ID = {
    "EcSubscriptionEnabled": 0,
    "EcSubscriptionEventSources": 1,
    "EcSubscriptionEventSourceAddress": 2,
    "EcSubscriptionEventSourceEnabled": 3,
    "EcSubscriptionEventSourceUserName": 4,
    "EcSubscriptionEventSourcePassword": 5,
    "EcSubscriptionDescription": 6,
    "EcSubscriptionURI": 7,
    "EcSubscriptionConfigurationMode": 8,
    "EcSubscriptionExpires": 9,
    "EcSubscriptionQuery": 10,
    "EcSubscriptionTransportName": 11,
    "EcSubscriptionTransportPort": 12,
    "EcSubscriptionDeliveryMode": 13,
    "EcSubscriptionDeliveryMaxItems": 14,
    "EcSubscriptionDeliveryMaxLatencyTime": 15,
    "EcSubscriptionHeartbeatInterval": 16,
    "EcSubscriptionLocale": 17,
    "EcSubscriptionContentFormat": 18,
    "EcSubscriptionLogFile": 19,
    "EcSubscriptionPublisherName": 20,
    "EcSubscriptionCredentialsType": 21,
    "EcSubscriptionCommonUserName": 22,
    "EcSubscriptionCommonPassword": 23,
    "EcSubscriptionHostName": 24,
    "EcSubscriptionReadExistingEvents": 25,
    "EcSubscriptionDialect": 26,
}
EC_SUBSCRIPTION_PROPERTY_ID_INV = {
    0: "EcSubscriptionEnabled",
    1: "EcSubscriptionEventSources",
    2: "EcSubscriptionEventSourceAddress",
    3: "EcSubscriptionEventSourceEnabled",
    4: "EcSubscriptionEventSourceUserName",
    5: "EcSubscriptionEventSourcePassword",
    6: "EcSubscriptionDescription",
    7: "EcSubscriptionURI",
    8: "EcSubscriptionConfigurationMode",
    9: "EcSubscriptionExpires",
    10: "EcSubscriptionQuery",
    11: "EcSubscriptionTransportName",
    12: "EcSubscriptionTransportPort",
    13: "EcSubscriptionDeliveryMode",
    14: "EcSubscriptionDeliveryMaxItems",
    15: "EcSubscriptionDeliveryMaxLatencyTime",
    16: "EcSubscriptionHeartbeatInterval",
    17: "EcSubscriptionLocale",
    18: "EcSubscriptionContentFormat",
    19: "EcSubscriptionLogFile",
    20: "EcSubscriptionPublisherName",
    21: "EcSubscriptionCredentialsType",
    22: "EcSubscriptionCommonUserName",
    23: "EcSubscriptionCommonPassword",
    24: "EcSubscriptionHostName",
    25: "EcSubscriptionReadExistingEvents",
    26: "EcSubscriptionDialect",
}
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = {
    "EcSubscriptionRunTimeStatusActive": 0,
    "EcSubscriptionRunTimeStatusLastError": 1,
    "EcSubscriptionRunTimeStatusLastErrorMessage": 2,
    "EcSubscriptionRunTimeStatusLastErrorTime": 3,
    "EcSubscriptionRunTimeStatusNextRetryTime": 4,
    "EcSubscriptionRunTimeStatusInfoIdEND": 5,
}
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID_INV = {
    0: "EcSubscriptionRunTimeStatusActive",
    1: "EcSubscriptionRunTimeStatusLastError",
    2: "EcSubscriptionRunTimeStatusLastErrorMessage",
    3: "EcSubscriptionRunTimeStatusLastErrorTime",
    4: "EcSubscriptionRunTimeStatusNextRetryTime",
    5: "EcSubscriptionRunTimeStatusInfoIdEND",
}

###################

###### Types ######
EC_HANDLE = HANDLE
EC_OBJECT_ARRAY_PROPERTY_HANDLE = HANDLE
EC_SUBSCRIPTION_PROPERTY_ID = UINT
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = UINT
_EC_VARIANT_u_ = Union([
    ("BooleanVal", BOOL),
    ("UInt32Val", UINT32),
    ("DateTimeVal", ULONGLONG),
    ("StringVal", LPCWSTR),
    ("BinaryVal", PBYTE),
    ("BooleanArr", BOOL_PTR),
    ("Int32Arr", INT32_PTR),
    ("StringArr", LPWSTR_PTR),
    ("PropertyHandleVal", EC_OBJECT_ARRAY_PROPERTY_HANDLE),
])
EC_VARIANT_TYPE = DWORD

class EC_VARIANT(MemStruct):
    fields = [
        (None, _EC_VARIANT_u_()),
        ("Count", DWORD()),
        ("Type", EC_VARIANT_TYPE()),
    ]

PEC_VARIANT = Ptr("<I", EC_VARIANT())

###################

###### Functions ######

def wecapi_EcClose(jitter):
    """
    BOOL EcClose(
        EC_HANDLE Object
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcDeleteSubscription(jitter):
    """
    BOOL EcDeleteSubscription(
        LPCWSTR SubscriptionName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcEnumNextSubscription(jitter):
    """
    BOOL EcEnumNextSubscription(
        EC_HANDLE SubscriptionEnum,
        DWORD SubscriptionNameBufferSize,
        LPWSTR SubscriptionNameBuffer,
        PDWORD SubscriptionNameBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionEnum", "SubscriptionNameBufferSize", "SubscriptionNameBuffer", "SubscriptionNameBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcGetObjectArrayProperty(jitter):
    """
    BOOL EcGetObjectArrayProperty(
        EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray,
        EC_SUBSCRIPTION_PROPERTY_ID PropertyId,
        DWORD ArrayIndex,
        DWORD Flags,
        DWORD PropertyValueBufferSize,
        PEC_VARIANT PropertyValueBuffer,
        PDWORD PropertyValueBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "PropertyId", "ArrayIndex", "Flags", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcGetObjectArraySize(jitter):
    """
    BOOL EcGetObjectArraySize(
        EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray,
        PDWORD ObjectArraySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "ObjectArraySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcGetSubscriptionProperty(jitter):
    """
    BOOL EcGetSubscriptionProperty(
        EC_HANDLE Subscription,
        EC_SUBSCRIPTION_PROPERTY_ID PropertyId,
        DWORD Flags,
        DWORD PropertyValueBufferSize,
        PEC_VARIANT PropertyValueBuffer,
        PDWORD PropertyValueBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Subscription", "PropertyId", "Flags", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcGetSubscriptionRunTimeStatus(jitter):
    """
    BOOL EcGetSubscriptionRunTimeStatus(
        LPCWSTR SubscriptionName,
        EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID StatusInfoId,
        LPCWSTR EventSourceName,
        DWORD Flags,
        DWORD StatusValueBufferSize,
        PEC_VARIANT StatusValueBuffer,
        PDWORD StatusValueBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionName", "StatusInfoId", "EventSourceName", "Flags", "StatusValueBufferSize", "StatusValueBuffer", "StatusValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcInsertObjectArrayElement(jitter):
    """
    BOOL EcInsertObjectArrayElement(
        EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray,
        DWORD ArrayIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "ArrayIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcOpenSubscriptionEnum(jitter):
    """
    EC_HANDLE EcOpenSubscriptionEnum(
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcOpenSubscription(jitter):
    """
    EC_HANDLE EcOpenSubscription(
        LPCWSTR SubscriptionName,
        DWORD AccessMask,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionName", "AccessMask", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcSaveSubscription(jitter):
    """
    BOOL EcSaveSubscription(
        EC_HANDLE Subscription,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Subscription", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcSetObjectArrayProperty(jitter):
    """
    BOOL EcSetObjectArrayProperty(
        EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray,
        EC_SUBSCRIPTION_PROPERTY_ID PropertyId,
        DWORD ArrayIndex,
        DWORD Flags,
        PEC_VARIANT PropertyValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "PropertyId", "ArrayIndex", "Flags", "PropertyValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcSetSubscriptionProperty(jitter):
    """
    BOOL EcSetSubscriptionProperty(
        EC_HANDLE Subscription,
        EC_SUBSCRIPTION_PROPERTY_ID PropertyId,
        DWORD Flags,
        PEC_VARIANT PropertyValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Subscription", "PropertyId", "Flags", "PropertyValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcRemoveObjectArrayElement(jitter):
    """
    BOOL EcRemoveObjectArrayElement(
        EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray,
        DWORD ArrayIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "ArrayIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcRetrySubscription(jitter):
    """
    BOOL EcRetrySubscription(
        LPCWSTR SubscriptionName,
        LPCWSTR EventSourceName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionName", "EventSourceName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
