###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def activeds_ADsBuildEnumerator(jitter):
    """
    HRESULT ADsBuildEnumerator(
        IADsContainer* pADsContainer,
        IEnumVARIANT** ppEnumVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pADsContainer", "ppEnumVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsBuildVarArrayInt(jitter):
    """
    HRESULT ADsBuildVarArrayInt(
        LPDWORD lpdwObjectTypes,
        DWORD dwObjectTypes,
        VARIANT* pVar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwObjectTypes", "dwObjectTypes", "pVar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsBuildVarArrayStr(jitter):
    """
    HRESULT ADsBuildVarArrayStr(
        LPWSTR* lppPathNames,
        DWORD dwPathNames,
        VARIANT* pVar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppPathNames", "dwPathNames", "pVar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsEncodeBinaryData(jitter):
    """
    HRESULT ADsEncodeBinaryData(
        PBYTE pbSrcData,
        DWORD dwSrcLen,
        LPWSTR* ppszDestData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbSrcData", "dwSrcLen", "ppszDestData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsEnumerateNext(jitter):
    """
    HRESULT ADsEnumerateNext(
        IEnumVARIANT* pEnumVariant,
        ULONG cElements,
        VARIANT* pvar,
        ULONG* pcElementsFetched
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEnumVariant", "cElements", "pvar", "pcElementsFetched"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsFreeEnumerator(jitter):
    """
    HRESULT ADsFreeEnumerator(
        IEnumVARIANT* pEnumVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pEnumVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsGetLastError(jitter):
    """
    HRESULT ADsGetLastError(
        LPDWORD lpError,
        LPWSTR lpErrorBuf,
        DWORD dwErrorBufLen,
        LPWSTR lpNameBuf,
        DWORD dwNameBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpError", "lpErrorBuf", "dwErrorBufLen", "lpNameBuf", "dwNameBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsGetObject(jitter):
    """
    HRESULT ADsGetObject(
        LPWSTR lpszPathName,
        REFIID riid,
        VOID** ppObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPathName", "riid", "ppObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsOpenObject(jitter):
    """
    HRESULT ADsOpenObject(
        LPWSTR lpszPathName,
        LPWSTR lpszUserName,
        LPWSTR lpszPassword,
        DWORD dwReserved,
        REFIID riid,
        VOID** ppObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszPathName", "lpszUserName", "lpszPassword", "dwReserved", "riid", "ppObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ADsSetLastError(jitter):
    """
    VOID ADsSetLastError(
        DWORD dwErr,
        LPWSTR pszError,
        LPWSTR pszProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwErr", "pszError", "pszProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_AllocADsMem(jitter):
    """
    LPVOID AllocADsMem(
        DWORD cb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_AllocADsStr(jitter):
    """
    LPWSTR AllocADsStr(
        LPWSTR pStr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_FreeADsMem(jitter):
    """
    BOOL FreeADsMem(
        LPVOID pMem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_FreeADsStr(jitter):
    """
    BOOL FreeADsStr(
        LPWSTR pStr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ReallocADsMem(jitter):
    """
    LPVOID ReallocADsMem(
        LPVOID pOldMem,
        DWORD cbOld,
        DWORD cbNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOldMem", "cbOld", "cbNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def activeds_ReallocADsStr(jitter):
    """
    BOOL ReallocADsStr(
        LPWSTR* ppStr,
        LPWSTR pStr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppStr", "pStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
