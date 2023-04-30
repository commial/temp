###### Enums ######

###################

###### Types ######
PFNDAVAUTHCALLBACK = LPVOID
OPAQUE_HANDLE = DWORD

###################

###### Functions ######

def davclnt_DavCancelConnectionsToServer(jitter):
    """
    [ERROR_CODE] DavCancelConnectionsToServer(
        LPWSTR lpName,
        BOOL fForce
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpName", "fForce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def davclnt_DavGetTheLockOwnerOfTheFile(jitter):
    """
    [ERROR_CODE] DavGetTheLockOwnerOfTheFile(
        LPCWSTR FileName,
        PWSTR LockOwnerName,
        PULONG LockOwnerNameLengthInBytes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "LockOwnerName", "LockOwnerNameLengthInBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def davclnt_DavInvalidateCache(jitter):
    """
    [ERROR_CODE] DavInvalidateCache(
        LPWSTR URLName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["URLName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def davclnt_DavRegisterAuthCallback(jitter):
    """
    OPAQUE_HANDLE DavRegisterAuthCallback(
        PFNDAVAUTHCALLBACK CallBack,
        ULONG Version
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CallBack", "Version"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def davclnt_DavUnregisterAuthCallback(jitter):
    """
    VOID DavUnregisterAuthCallback(
        OPAQUE_HANDLE hCallback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
