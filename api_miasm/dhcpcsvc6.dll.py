
def dhcpcsvc6_Dhcpv6CApiCleanup(jitter):
    """"
    [Dhcpcsvc6.dll] VOID Dhcpv6CApiCleanup()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6CApiInitialize(jitter):
    """"
    [Dhcpcsvc6.dll] [ERROR_CODE] Dhcpv6CApiInitialize(LPDWORD Version)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Version"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6RequestParams(jitter):
    """"
    [Dhcpcsvc6.dll] [ERROR_CODE] Dhcpv6RequestParams(BOOL forceNewInform, LPVOID reserved, LPWSTR adapterName, LPDHCPV6CAPI_CLASSID classId, DHCPV6CAPI_PARAMS_ARRAY recdParams, LPBYTE buffer, LPDWORD pSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["forceNewInform", "reserved", "adapterName", "classId", "recdParams", "buffer", "pSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6ReleasePrefix(jitter):
    """"
    [Dhcpcsvc6.dll] [ERROR_CODE] Dhcpv6ReleasePrefix(LPWSTR adapterName, LPDHCPV6CAPI_CLASSID classId, LPDHCPV6PrefixLeaseInformation prefixleaseInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["adapterName", "classId", "prefixleaseInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6RenewPrefix(jitter):
    """"
    [Dhcpcsvc6.dll] [ERROR_CODE] Dhcpv6RenewPrefix(LPWSTR adapterName, LPDHCPV6CAPI_CLASSID classId, LPDHCPV6PrefixLeaseInformation prefixleaseInfo, DWORD pdwTimeToWait, DWORD bValidatePrefix)
    """"
    ret_ad, args = jitter.func_args_stdcall(["adapterName", "classId", "prefixleaseInfo", "pdwTimeToWait", "bValidatePrefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpcsvc6_Dhcpv6RequestPrefix(jitter):
    """"
    [Dhcpcsvc6.dll] [ERROR_CODE] Dhcpv6RequestPrefix(LPWSTR adapterName, LPDHCPV6CAPI_CLASSID classId, LPDHCPV6PrefixLeaseInformation prefixleaseInfo, DWORD pdwTimeToWait)
    """"
    ret_ad, args = jitter.func_args_stdcall(["adapterName", "classId", "prefixleaseInfo", "pdwTimeToWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
