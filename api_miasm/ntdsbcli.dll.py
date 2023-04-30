###### Enums ######

###################

###### Types ######
HBC = LPVOID
HBC_PTR = Ptr("<I", HBC())
_NtdsBackupType_ = ULONG
_NtdsRestoreType_ = ULONG

###################

###### Functions ######

def ntdsbcli_DsBackupClose(jitter):
    """
    HRESULT DsBackupClose(
        HBC hbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupEnd(jitter):
    """
    HRESULT DsBackupEnd(
        HBC hbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupFree(jitter):
    """
    void DsBackupFree(
        PVOID pvBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupGetBackupLogs(jitter, get_str, set_str):
    """
    HRESULT DsBackupGetBackupLogs(
        HBC hbc,
        LPTSTR* pszBackupLogFiles,
        LPDWORD pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pszBackupLogFiles", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupGetBackupLogsA(jitter):
    ntdsbcli_DsBackupGetBackupLogs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsBackupGetBackupLogsW(jitter):
    ntdsbcli_DsBackupGetBackupLogs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsBackupGetDatabaseNames(jitter, get_str, set_str):
    """
    HRESULT DsBackupGetDatabaseNames(
        HBC hbc,
        LPTSTR* pszAttachmentInfo,
        LPDWORD pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pszAttachmentInfo", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupGetDatabaseNamesA(jitter):
    ntdsbcli_DsBackupGetDatabaseNames(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsBackupGetDatabaseNamesW(jitter):
    ntdsbcli_DsBackupGetDatabaseNames(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsBackupOpenFile(jitter, get_str, set_str):
    """
    HRESULT DsBackupOpenFile(
        HBC hbc,
        LPCTSTR szAttachmentName,
        DWORD cbReadHintSize,
        LARGE_INTEGER* pliFileSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "szAttachmentName", "cbReadHintSize", "pliFileSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupOpenFileA(jitter):
    ntdsbcli_DsBackupOpenFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsBackupOpenFileW(jitter):
    ntdsbcli_DsBackupOpenFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsBackupPrepare(jitter, get_str, set_str):
    """
    HRESULT DsBackupPrepare(
        LPCTSTR szBackupServer,
        ULONG grbit,
        [NtdsBackupType] btBackupType,
        PVOID* ppvExpiryToken,
        LPDWORD pcbExpiryTokenSize,
        HBC* phbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szBackupServer", "grbit", "btBackupType", "ppvExpiryToken", "pcbExpiryTokenSize", "phbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupPrepareA(jitter):
    ntdsbcli_DsBackupPrepare(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsBackupPrepareW(jitter):
    ntdsbcli_DsBackupPrepare(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsBackupRead(jitter):
    """
    HRESULT DsBackupRead(
        HBC hbc,
        PVOID pvBuffer,
        DWORD cbBuffer,
        PDWORD pcbRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pvBuffer", "cbBuffer", "pcbRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupTruncateLogs(jitter):
    """
    HRESULT DsBackupTruncateLogs(
        HBC hbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsIsNTDSOnline(jitter, get_str, set_str):
    """
    HRESULT DsIsNTDSOnline(
        LPCTSTR szServerName,
        BOOL* pfNTDSOnline
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szServerName", "pfNTDSOnline"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsIsNTDSOnlineA(jitter):
    ntdsbcli_DsIsNTDSOnline(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsIsNTDSOnlineW(jitter):
    ntdsbcli_DsIsNTDSOnline(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsRestoreEnd(jitter):
    """
    HRESULT DsRestoreEnd(
        HBC hbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestoreGetDatabaseLocations(jitter, get_str, set_str):
    """
    HRESULT DsRestoreGetDatabaseLocations(
        HBC hbc,
        LPWSTR* pszDatabaseLocationList,
        LPDWORD pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pszDatabaseLocationList", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestoreGetDatabaseLocationsA(jitter):
    ntdsbcli_DsRestoreGetDatabaseLocations(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsRestoreGetDatabaseLocationsW(jitter):
    ntdsbcli_DsRestoreGetDatabaseLocations(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsRestorePrepare(jitter, get_str, set_str):
    """
    HRESULT DsRestorePrepare(
        LPCWSTR szServerName,
        [NtdsRestoreType] rtFlag,
        PVOID pvExpiryToken,
        DWORD cbExpiryTokenSize,
        HBC* phbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szServerName", "rtFlag", "pvExpiryToken", "cbExpiryTokenSize", "phbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestorePrepareA(jitter):
    ntdsbcli_DsRestorePrepare(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsRestorePrepareW(jitter):
    ntdsbcli_DsRestorePrepare(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsRestoreRegister(jitter, get_str, set_str):
    """
    HRESULT DsRestoreRegister(
        HBC hbc,
        LPCTSTR szCheckPointFilePath,
        LPCTSTR szLogPath,
        LONG crstmap,
        LPCTSTR szBackupLogPath,
        ULONG genLow,
        ULONG genHigh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "szCheckPointFilePath", "szLogPath", "crstmap", "szBackupLogPath", "genLow", "genHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestoreRegisterA(jitter):
    ntdsbcli_DsRestoreRegister(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsRestoreRegisterW(jitter):
    ntdsbcli_DsRestoreRegister(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsRestoreRegisterComplete(jitter):
    """
    HRESULT DsRestoreRegisterComplete(
        HBC hbc,
        HRESULT hrRestoreState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "hrRestoreState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsSetAuthIdentity(jitter, get_str, set_str):
    """
    HRESULT DsSetAuthIdentity(
        LPCTSTR szUserName,
        LPCTSTR szDomainName,
        LPCTSTR szPassword
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szUserName", "szDomainName", "szPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsSetAuthIdentityA(jitter):
    ntdsbcli_DsSetAuthIdentity(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsSetAuthIdentityW(jitter):
    ntdsbcli_DsSetAuthIdentity(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsbcli_DsSetCurrentBackupLog(jitter, get_str, set_str):
    """
    HRESULT DsSetCurrentBackupLog(
        LPCWSTR szServerName,
        DWORD dwCurrentLog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szServerName", "dwCurrentLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsSetCurrentBackupLogA(jitter):
    ntdsbcli_DsSetCurrentBackupLog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsbcli_DsSetCurrentBackupLogW(jitter):
    ntdsbcli_DsSetCurrentBackupLog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
