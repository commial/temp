ADSTYPE = {
    "ADSTYPE_INVALID": 0,
    "ADSTYPE_DN_STRING": 1,
    "ADSTYPE_CASE_EXACT_STRING": 2,
    "ADSTYPE_CASE_IGNORE_STRING": 3,
    "ADSTYPE_PRINTABLE_STRING": 4,
    "ADSTYPE_NUMERIC_STRING": 5,
    "ADSTYPE_BOOLEAN": 6,
    "ADSTYPE_INTEGER": 7,
    "ADSTYPE_OCTET_STRING": 8,
    "ADSTYPE_UTC_TIME": 9,
    "ADSTYPE_LARGE_INTEGER": 10,
    "ADSTYPE_PROV_SPECIFIC": 11,
    "ADSTYPE_OBJECT_CLASS": 12,
    "ADSTYPE_CASEIGNORE_LIST": 13,
    "ADSTYPE_OCTET_LIST": 14,
    "ADSTYPE_PATH": 15,
    "ADSTYPE_POSTALADDRESS": 16,
    "ADSTYPE_TIMESTAMP": 17,
    "ADSTYPE_BACKLINK": 18,
    "ADSTYPE_TYPEDNAME": 19,
    "ADSTYPE_HOLD": 20,
    "ADSTYPE_NETADDRESS": 21,
    "ADSTYPE_REPLICAPOINTER": 22,
    "ADSTYPE_FAXNUMBER": 23,
    "ADSTYPE_EMAIL": 24,
    "ADSTYPE_NT_SECURITY_DESCRIPTOR": 25,
    "ADSTYPE_UNKNOWN": 26,
    "ADSTYPE_DN_WITH_BINARY": 27,
    "ADSTYPE_DN_WITH_STRING": 28,
}
ADSTYPE_INV = {
    0: "ADSTYPE_INVALID",
    1: "ADSTYPE_DN_STRING",
    2: "ADSTYPE_CASE_EXACT_STRING",
    3: "ADSTYPE_CASE_IGNORE_STRING",
    4: "ADSTYPE_PRINTABLE_STRING",
    5: "ADSTYPE_NUMERIC_STRING",
    6: "ADSTYPE_BOOLEAN",
    7: "ADSTYPE_INTEGER",
    8: "ADSTYPE_OCTET_STRING",
    9: "ADSTYPE_UTC_TIME",
    10: "ADSTYPE_LARGE_INTEGER",
    11: "ADSTYPE_PROV_SPECIFIC",
    12: "ADSTYPE_OBJECT_CLASS",
    13: "ADSTYPE_CASEIGNORE_LIST",
    14: "ADSTYPE_OCTET_LIST",
    15: "ADSTYPE_PATH",
    16: "ADSTYPE_POSTALADDRESS",
    17: "ADSTYPE_TIMESTAMP",
    18: "ADSTYPE_BACKLINK",
    19: "ADSTYPE_TYPEDNAME",
    20: "ADSTYPE_HOLD",
    21: "ADSTYPE_NETADDRESS",
    22: "ADSTYPE_REPLICAPOINTER",
    23: "ADSTYPE_FAXNUMBER",
    24: "ADSTYPE_EMAIL",
    25: "ADSTYPE_NT_SECURITY_DESCRIPTOR",
    26: "ADSTYPE_UNKNOWN",
    27: "ADSTYPE_DN_WITH_BINARY",
    28: "ADSTYPE_DN_WITH_STRING",
}

def dsprop_ADsPropCheckIfWritable(jitter):
    """
    BOOL ADsPropCheckIfWritable(
        const PWSTR pwzAttr,
        const PADS_ATTR_INFO pWritableAttrs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzAttr", "pWritableAttrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropCreateNotifyObj(jitter):
    """
    HRESULT ADsPropCreateNotifyObj(
        LPDATAOBJECT pAppThdDataObj,
        PWSTR pwzADsObjName,
        HWND* phNotifyObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppThdDataObj", "pwzADsObjName", "phNotifyObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropGetInitInfo(jitter):
    """
    BOOL ADsPropGetInitInfo(
        HWND hNotifyObject,
        PADSPROPINITPARAMS pInitParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "pInitParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSendErrorMessage(jitter):
    """
    BOOL ADsPropSendErrorMessage(
        HWND hNotifyObject,
        PADSPROPERROR pError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "pError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSetHwnd(jitter):
    """
    BOOL ADsPropSetHwnd(
        HWND hNotifyObject,
        HWND hPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSetHwndWithTitle(jitter):
    """
    BOOL ADsPropSetHwndWithTitle(
        HWND hNotifyObject,
        HWND hPage,
        PTSTR ptzTitle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage", "ptzTitle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropShowErrorDialog(jitter):
    """
    BOOL ADsPropShowErrorDialog(
        HWND hNotifyObject,
        HWND hPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
