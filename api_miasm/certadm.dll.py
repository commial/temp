###### Enums ######

###################

###### Types ######
HCSBC = LPVOID
HCSBC_PTR = Ptr("<I", HCSBC())

class CSEDB_RSTMAP(MemStruct):
    fields = [
        ("pwszDatabaseName", WCHAR_PTR()),
        ("pwszNewDatabaseName", WCHAR_PTR()),
    ]

CSEDB_RSTMAP___ = Ptr("<I", CSEDB_RSTMAP())

###################

###### Functions ######

def certadm_CertSrvBackupClose(jitter):
    """
    HRESULT CertSrvBackupClose(
        HCSBC hbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupEnd(jitter):
    """
    HRESULT CertSrvBackupEnd(
        HCSBC hbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupFree(jitter):
    """
    void CertSrvBackupFree(
        VOID* pv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupGetBackupLogsW(jitter):
    """
    HRESULT CertSrvBackupGetBackupLogsW(
        HCSBC hbc,
        WCHAR** ppwszzBackupLogFiles,
        DWORD* pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "ppwszzBackupLogFiles", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupGetDatabaseNamesW(jitter):
    """
    HRESULT CertSrvBackupGetDatabaseNamesW(
        HCSBC hbc,
        WCHAR** ppwszzAttachmentInformation,
        DWORD* pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "ppwszzAttachmentInformation", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupGetDynamicFileListW(jitter):
    """
    HRESULT CertSrvBackupGetDynamicFileListW(
        HCSBC hbc,
        WCHAR** ppwszzFileList,
        DWORD* pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "ppwszzFileList", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupOpenFileW(jitter):
    """
    HRESULT CertSrvBackupOpenFileW(
        HCSBC hbc,
        const WCHAR* pwszAttachmentName,
        DWORD cbReadHintSize,
        LARGE_INTEGER* pliFileSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pwszAttachmentName", "cbReadHintSize", "pliFileSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupPrepareW(jitter):
    """
    HRESULT CertSrvBackupPrepareW(
        const WCHAR* pwszServerName,
        ULONG grbitJet,
        ULONG dwBackupFlags,
        HCSBC* phbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "grbitJet", "dwBackupFlags", "phbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupRead(jitter):
    """
    HRESULT CertSrvBackupRead(
        HCSBC hbc,
        VOID* pvBuffer,
        DWORD cbBuffer,
        DWORD* pcbRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pvBuffer", "cbBuffer", "pcbRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvBackupTruncateLogs(jitter):
    """
    HRESULT CertSrvBackupTruncateLogs(
        HCSBC hbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvIsServerOnlineW(jitter):
    """
    HRESULT CertSrvIsServerOnlineW(
        const WCHAR* pwszServerName,
        BOOL* pfServerOnline
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "pfServerOnline"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreEnd(jitter):
    """
    HRESULT CertSrvRestoreEnd(
        HCSBC hbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreGetDatabaseLocationsW(jitter):
    """
    HRESULT CertSrvRestoreGetDatabaseLocationsW(
        HCSBC hbc,
        WCHAR** ppwszzDatabaseLocationList,
        DWORD* pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "ppwszzDatabaseLocationList", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestorePrepareW(jitter):
    """
    HRESULT CertSrvRestorePrepareW(
        const WCHAR* pwszServerName,
        ULONG dwRestoreFlags,
        HCSBC* phbc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "dwRestoreFlags", "phbc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreRegisterW(jitter):
    """
    HRESULT CertSrvRestoreRegisterW(
        HCSBC hbc,
        const WCHAR* pwszCheckPointFilePath,
        const WCHAR* pwszLogPath,
        CSEDB_RSTMAP [] rgrstmap,
        LONG crstmap,
        const WCHAR* pwszBackupLogPath,
        ULONG genLow,
        ULONG genHigh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pwszCheckPointFilePath", "pwszLogPath", "rgrstmap", "crstmap", "pwszBackupLogPath", "genLow", "genHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreRegisterComplete(jitter):
    """
    HRESULT CertSrvRestoreRegisterComplete(
        HCSBC hbc,
        HRESULT hrRestoreState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "hrRestoreState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvRestoreRegisterThroughFile(jitter):
    """
    HRESULT CertSrvRestoreRegisterThroughFile(
        HCSBC hbc,
        const WCHAR* pwszCheckPointFilePath,
        const WCHAR* pwszLogPath,
        CSEDB_RSTMAP [] rgrstmap,
        LONG crstmap,
        const WCHAR* pwszBackupLogPath,
        ULONG genLow,
        ULONG genHigh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hbc", "pwszCheckPointFilePath", "pwszLogPath", "rgrstmap", "crstmap", "pwszBackupLogPath", "genLow", "genHigh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def certadm_CertSrvServerControlW(jitter):
    """
    HRESULT CertSrvServerControlW(
        const WCHAR* pwszServerName,
        DWORD dwControlFlags,
        DWORD* pcbOut,
        BYTE** ppbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszServerName", "dwControlFlags", "pcbOut", "ppbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
