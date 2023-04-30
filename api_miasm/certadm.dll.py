
def certadm_CertSrvBackupClose(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupClose(HCSBC hbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupEnd(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupEnd(HCSBC hbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupFree(jitter):
    """"
    [Certadm.dll] void CertSrvBackupFree(VOID* pv)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupGetBackupLogsW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupGetBackupLogsW(HCSBC hbc, WCHAR** ppwszzBackupLogFiles, DWORD* pcbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "ppwszzBackupLogFiles", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupGetDatabaseNamesW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupGetDatabaseNamesW(HCSBC hbc, WCHAR** ppwszzAttachmentInformation, DWORD* pcbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "ppwszzAttachmentInformation", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupGetDynamicFileListW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupGetDynamicFileListW(HCSBC hbc, WCHAR** ppwszzFileList, DWORD* pcbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "ppwszzFileList", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupOpenFileW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupOpenFileW(HCSBC hbc, const WCHAR* pwszAttachmentName, DWORD cbReadHintSize, LARGE_INTEGER* pliFileSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pwszAttachmentName", "cbReadHintSize", "pliFileSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupPrepareW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupPrepareW(const WCHAR* pwszServerName, ULONG grbitJet, ULONG dwBackupFlags, HCSBC* phbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "grbitJet", "dwBackupFlags", "phbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupRead(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupRead(HCSBC hbc, VOID* pvBuffer, DWORD cbBuffer, DWORD* pcbRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pvBuffer", "cbBuffer", "pcbRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupTruncateLogs(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvBackupTruncateLogs(HCSBC hbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvIsServerOnlineW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvIsServerOnlineW(const WCHAR* pwszServerName, BOOL* pfServerOnline)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "pfServerOnline"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreEnd(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvRestoreEnd(HCSBC hbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreGetDatabaseLocationsW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvRestoreGetDatabaseLocationsW(HCSBC hbc, WCHAR** ppwszzDatabaseLocationList, DWORD* pcbSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "ppwszzDatabaseLocationList", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestorePrepareW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvRestorePrepareW(const WCHAR* pwszServerName, ULONG dwRestoreFlags, HCSBC* phbc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "dwRestoreFlags", "phbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreRegisterW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvRestoreRegisterW(HCSBC hbc, const WCHAR* pwszCheckPointFilePath, const WCHAR* pwszLogPath, CSEDB_RSTMAP [] rgrstmap, LONG crstmap, const WCHAR* pwszBackupLogPath, ULONG genLow, ULONG genHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pwszCheckPointFilePath", "pwszLogPath", "rgrstmap", "crstmap", "pwszBackupLogPath", "genLow", "genHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreRegisterComplete(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvRestoreRegisterComplete(HCSBC hbc, HRESULT hrRestoreState)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "hrRestoreState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreRegisterThroughFile(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvRestoreRegisterThroughFile(HCSBC hbc, const WCHAR* pwszCheckPointFilePath, const WCHAR* pwszLogPath, CSEDB_RSTMAP [] rgrstmap, LONG crstmap, const WCHAR* pwszBackupLogPath, ULONG genLow, ULONG genHigh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pwszCheckPointFilePath", "pwszLogPath", "rgrstmap", "crstmap", "pwszBackupLogPath", "genLow", "genHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvServerControlW(jitter):
    """"
    [Certadm.dll] HRESULT CertSrvServerControlW(const WCHAR* pwszServerName, DWORD dwControlFlags, DWORD* pcbOut, BYTE** ppbOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "dwControlFlags", "pcbOut", "ppbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
