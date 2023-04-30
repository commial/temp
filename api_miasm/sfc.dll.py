###### Enums ######

###################

###### Types ######

class PROTECTED_FILE_DATA(MemStruct):
    fields = [
        ("FileName", WCHAR__MAX_PATH_()),
        ("FileNumber", DWORD()),
    ]

PPROTECTED_FILE_DATA = Ptr("<I", PROTECTED_FILE_DATA())

###################

###### Functions ######

def sfc_SfcIsFileProtected(jitter):
    """
    BOOL SfcIsFileProtected(
        HANDLE RpcHandle,
        LPCWSTR ProtFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RpcHandle", "ProtFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfcIsKeyProtected(jitter):
    """
    BOOL SfcIsKeyProtected(
        HKEY hKey,
        LPCWSTR lpSubKey,
        REGSAM samDesired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hKey", "lpSubKey", "samDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfcGetNextProtectedFile(jitter):
    """
    BOOL SfcGetNextProtectedFile(
        HANDLE RpcHandle,
        PPROTECTED_FILE_DATA ProtFileData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RpcHandle", "ProtFileData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfcTerminateWatcherThread(jitter):
    """
    [ERROR_CODE] SfcTerminateWatcherThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfcFileException(jitter):
    """
    [ERROR_CODE] SfcFileException(
        DWORD dwUnknown0,
        LPCSTR lpwszFile,
        DWORD dwUnknown1
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwUnknown0", "lpwszFile", "dwUnknown1"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SfpVerifyFile(jitter):
    """
    BOOL SfpVerifyFile(
        LPCSTR lpszFileName,
        LPSTR lpszError,
        DWORD dwErrSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszFileName", "lpszError", "dwErrSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SRRemoveRestorePoint(jitter):
    """
    [ERROR_CODE] SRRemoveRestorePoint(
        DWORD dwRPNum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwRPNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SRSetRestorePointA(jitter):
    """
    BOOL SRSetRestorePointA(
        PRESTOREPOINTINFOA pRestorePtSpec,
        PSTATEMGRSTATUS pSMgrStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sfc_SRSetRestorePointW(jitter):
    """
    BOOL SRSetRestorePointW(
        PRESTOREPOINTINFOW pRestorePtSpec,
        PSTATEMGRSTATUS pSMgrStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRestorePtSpec", "pSMgrStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
