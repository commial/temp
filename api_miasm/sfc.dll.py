
def sfc_SfcIsFileProtected(jitter):
    """
    [sfc.dll] BOOL SfcIsFileProtected(HANDLE RpcHandle, LPCWSTR ProtFileName)
    """
    ret_ad, args = jitter.func_args_stdcall(["RpcHandle", "ProtFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfcIsKeyProtected(jitter):
    """
    [sfc.dll] BOOL SfcIsKeyProtected(HKEY hKey, LPCWSTR lpSubKey, REGSAM samDesired)
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "samDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfcGetNextProtectedFile(jitter):
    """
    [sfc.dll] BOOL SfcGetNextProtectedFile(HANDLE RpcHandle, PPROTECTED_FILE_DATA ProtFileData)
    """
    ret_ad, args = jitter.func_args_stdcall(["RpcHandle", "ProtFileData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfcTerminateWatcherThread(jitter):
    """
    [sfc.dll] [ERROR_CODE] SfcTerminateWatcherThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfcFileException(jitter):
    """
    [sfc.dll] [ERROR_CODE] SfcFileException(DWORD dwUnknown0, LPCSTR lpwszFile, DWORD dwUnknown1)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwUnknown0", "lpwszFile", "dwUnknown1"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfpVerifyFile(jitter):
    """
    [sfc.dll] BOOL SfpVerifyFile(LPCSTR lpszFileName, LPSTR lpszError, DWORD dwErrSize)
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "lpszError", "dwErrSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SRRemoveRestorePoint(jitter):
    """
    [sfc.dll] [ERROR_CODE] SRRemoveRestorePoint(DWORD dwRPNum)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwRPNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SRSetRestorePointA(jitter):
    """
    [sfc.dll] BOOL SRSetRestorePointA(PRESTOREPOINTINFOA pRestorePtSpec, PSTATEMGRSTATUS pSMgrStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SRSetRestorePointW(jitter):
    """
    [sfc.dll] BOOL SRSetRestorePointW(PRESTOREPOINTINFOW pRestorePtSpec, PSTATEMGRSTATUS pSMgrStatus)
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
