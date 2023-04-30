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
EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID = {
    "EcSubscriptionRunTimeStatusActive": 0,
    "EcSubscriptionRunTimeStatusLastError": 1,
    "EcSubscriptionRunTimeStatusLastErrorMessage": 2,
    "EcSubscriptionRunTimeStatusLastErrorTime": 3,
    "EcSubscriptionRunTimeStatusNextRetryTime": 4,
    "EcSubscriptionRunTimeStatusInfoIdEND": 5,
}

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
