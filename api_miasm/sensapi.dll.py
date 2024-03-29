###### Enums ######

###################

###### Types ######

class QOCINFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("dwFlags", DWORD()),
        ("dwInSpeed", DWORD()),
        ("dwOutSpeed", DWORD()),
    ]

LPQOCINFO = Ptr("<I", QOCINFO())
_NetworkAliveFlags_ = DWORD
_NetworkAliveFlags_PTR_ = Ptr("<I", _NetworkAliveFlags_())

###################

###### Functions ######

def sensapi_IsDestinationReachable(jitter, get_str, set_str):
    """
    BOOL IsDestinationReachable(
        LPCSTR lpszDestination,
        LPQOCINFO lpQOCInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDestination", "lpQOCInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sensapi_IsDestinationReachableA(jitter):
    sensapi_IsDestinationReachable(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def sensapi_IsDestinationReachableW(jitter):
    sensapi_IsDestinationReachable(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def sensapi_IsNetworkAlive(jitter):
    """
    BOOL IsNetworkAlive(
        [NetworkAliveFlags*] lpdwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
