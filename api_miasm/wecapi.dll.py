
def wecapi_EcClose(jitter):
    """
    [Wecapi.dll] BOOL EcClose(EC_HANDLE Object)
    """
    ret_ad, args = jitter.func_args_stdcall(["Object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcDeleteSubscription(jitter):
    """
    [Wecapi.dll] BOOL EcDeleteSubscription(LPCWSTR SubscriptionName, DWORD Flags)
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcEnumNextSubscription(jitter):
    """
    [Wecapi.dll] BOOL EcEnumNextSubscription(EC_HANDLE SubscriptionEnum, DWORD SubscriptionNameBufferSize, LPWSTR SubscriptionNameBuffer, PDWORD SubscriptionNameBufferUsed)
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionEnum", "SubscriptionNameBufferSize", "SubscriptionNameBuffer", "SubscriptionNameBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcGetObjectArrayProperty(jitter):
    """
    [Wecapi.dll] BOOL EcGetObjectArrayProperty(EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray, EC_SUBSCRIPTION_PROPERTY_ID PropertyId, DWORD ArrayIndex, DWORD Flags, DWORD PropertyValueBufferSize, PEC_VARIANT PropertyValueBuffer, PDWORD PropertyValueBufferUsed)
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "PropertyId", "ArrayIndex", "Flags", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcGetObjectArraySize(jitter):
    """
    [Wecapi.dll] BOOL EcGetObjectArraySize(EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray, PDWORD ObjectArraySize)
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "ObjectArraySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcGetSubscriptionProperty(jitter):
    """
    [Wecapi.dll] BOOL EcGetSubscriptionProperty(EC_HANDLE Subscription, EC_SUBSCRIPTION_PROPERTY_ID PropertyId, DWORD Flags, DWORD PropertyValueBufferSize, PEC_VARIANT PropertyValueBuffer, PDWORD PropertyValueBufferUsed)
    """
    ret_ad, args = jitter.func_args_stdcall(["Subscription", "PropertyId", "Flags", "PropertyValueBufferSize", "PropertyValueBuffer", "PropertyValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcGetSubscriptionRunTimeStatus(jitter):
    """
    [Wecapi.dll] BOOL EcGetSubscriptionRunTimeStatus(LPCWSTR SubscriptionName, EC_SUBSCRIPTION_RUNTIME_STATUS_INFO_ID StatusInfoId, LPCWSTR EventSourceName, DWORD Flags, DWORD StatusValueBufferSize, PEC_VARIANT StatusValueBuffer, PDWORD StatusValueBufferUsed)
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionName", "StatusInfoId", "EventSourceName", "Flags", "StatusValueBufferSize", "StatusValueBuffer", "StatusValueBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcInsertObjectArrayElement(jitter):
    """
    [Wecapi.dll] BOOL EcInsertObjectArrayElement(EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray, DWORD ArrayIndex)
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "ArrayIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcOpenSubscriptionEnum(jitter):
    """
    [Wecapi.dll] EC_HANDLE EcOpenSubscriptionEnum(DWORD Flags)
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcOpenSubscription(jitter):
    """
    [Wecapi.dll] EC_HANDLE EcOpenSubscription(LPCWSTR SubscriptionName, DWORD AccessMask, DWORD Flags)
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionName", "AccessMask", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcSaveSubscription(jitter):
    """
    [Wecapi.dll] BOOL EcSaveSubscription(EC_HANDLE Subscription, DWORD Flags)
    """
    ret_ad, args = jitter.func_args_stdcall(["Subscription", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcSetObjectArrayProperty(jitter):
    """
    [Wecapi.dll] BOOL EcSetObjectArrayProperty(EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray, EC_SUBSCRIPTION_PROPERTY_ID PropertyId, DWORD ArrayIndex, DWORD Flags, PEC_VARIANT PropertyValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "PropertyId", "ArrayIndex", "Flags", "PropertyValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcSetSubscriptionProperty(jitter):
    """
    [Wecapi.dll] BOOL EcSetSubscriptionProperty(EC_HANDLE Subscription, EC_SUBSCRIPTION_PROPERTY_ID PropertyId, DWORD Flags, PEC_VARIANT PropertyValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["Subscription", "PropertyId", "Flags", "PropertyValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcRemoveObjectArrayElement(jitter):
    """
    [Wecapi.dll] BOOL EcRemoveObjectArrayElement(EC_OBJECT_ARRAY_PROPERTY_HANDLE ObjectArray, DWORD ArrayIndex)
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectArray", "ArrayIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wecapi_EcRetrySubscription(jitter):
    """
    [Wecapi.dll] BOOL EcRetrySubscription(LPCWSTR SubscriptionName, LPCWSTR EventSourceName, DWORD Flags)
    """
    ret_ad, args = jitter.func_args_stdcall(["SubscriptionName", "EventSourceName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
