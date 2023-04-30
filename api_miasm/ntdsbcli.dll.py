
def ntdsbcli_DsBackupClose(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsBackupClose(HBC hbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupEnd(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsBackupEnd(HBC hbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupFree(jitter):
    """"
    [Ntdsbcli.dll] void DsBackupFree(PVOID pvBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupGetBackupLogs(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsBackupGetBackupLogs(HBC hbc, LPTSTR* pszBackupLogFiles, LPDWORD pcbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pszBackupLogFiles", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupGetDatabaseNames(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsBackupGetDatabaseNames(HBC hbc, LPTSTR* pszAttachmentInfo, LPDWORD pcbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pszAttachmentInfo", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupOpenFile(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsBackupOpenFile(HBC hbc, LPCTSTR szAttachmentName, DWORD cbReadHintSize, LARGE_INTEGER* pliFileSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "szAttachmentName", "cbReadHintSize", "pliFileSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupPrepare(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsBackupPrepare(LPCTSTR szBackupServer, ULONG grbit, [NtdsBackupType] btBackupType, PVOID* ppvExpiryToken, LPDWORD pcbExpiryTokenSize, HBC* phbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szBackupServer", "grbit", "btBackupType", "ppvExpiryToken", "pcbExpiryTokenSize", "phbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupRead(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsBackupRead(HBC hbc, PVOID pvBuffer, DWORD cbBuffer, PDWORD pcbRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pvBuffer", "cbBuffer", "pcbRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsBackupTruncateLogs(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsBackupTruncateLogs(HBC hbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsIsNTDSOnline(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsIsNTDSOnline(LPCTSTR szServerName, BOOL* pfNTDSOnline)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szServerName", "pfNTDSOnline"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestoreEnd(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsRestoreEnd(HBC hbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestoreGetDatabaseLocations(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsRestoreGetDatabaseLocations(HBC hbc, LPWSTR* pszDatabaseLocationList, LPDWORD pcbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pszDatabaseLocationList", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestorePrepare(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsRestorePrepare(LPCWSTR szServerName, [NtdsRestoreType] rtFlag, PVOID pvExpiryToken, DWORD cbExpiryTokenSize, HBC* phbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szServerName", "rtFlag", "pvExpiryToken", "cbExpiryTokenSize", "phbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestoreRegister(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsRestoreRegister(HBC hbc, LPCTSTR szCheckPointFilePath, LPCTSTR szLogPath, LONG crstmap, LPCTSTR szBackupLogPath, ULONG genLow, ULONG genHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "szCheckPointFilePath", "szLogPath", "crstmap", "szBackupLogPath", "genLow", "genHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsRestoreRegisterComplete(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsRestoreRegisterComplete(HBC hbc, HRESULT hrRestoreState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "hrRestoreState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsSetAuthIdentity(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsSetAuthIdentity(LPCTSTR szUserName, LPCTSTR szDomainName, LPCTSTR szPassword)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szUserName", "szDomainName", "szPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsbcli_DsSetCurrentBackupLog(jitter):
    """"
    [Ntdsbcli.dll] HRESULT DsSetCurrentBackupLog(LPCWSTR szServerName, DWORD dwCurrentLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szServerName", "dwCurrentLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
