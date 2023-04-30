
def rstrtmgr_RmAddFilter(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmAddFilter(DWORD dwSessionHandle, LPCWSTR strFilename, RM_UNIQUE_PROCESS* Application, LPCWSTR strShortServiceName, RM_FILTER_ACTION ActionType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "strFilename", "Application", "strShortServiceName", "ActionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmStartSession(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmStartSession(DWORD* pSessionHandle, DWORD dwSessionFlags, WCHAR [] strSessionKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSessionHandle", "dwSessionFlags", "strSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmJoinSession(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmJoinSession(DWORD* pSessionHandle, const WCHAR [] strSessionKey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSessionHandle", "strSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmEndSession(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmEndSession(DWORD dwSessionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmRegisterResources(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmRegisterResources(DWORD dwSessionHandle, UINT nFiles, LPCWSTR [] rgsFileNames, UINT nApplications, RM_UNIQUE_PROCESS [] rgApplications, UINT nServices, LPCWSTR [] rgsServiceNames)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "nFiles", "rgsFileNames", "nApplications", "rgApplications", "nServices", "rgsServiceNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmGetList(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmGetList(DWORD dwSessionHandle, UINT* pnProcInfoNeeded, UINT* pnProcInfo, RM_PROCESS_INFO [] rgAffectedApps, LPDWORD lpdwRebootReasons)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "pnProcInfoNeeded", "pnProcInfo", "rgAffectedApps", "lpdwRebootReasons"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmGetFilterList(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmGetFilterList(DWORD dwSessionHandle, PBYTE pbFilterBuf, DWORD cbFilterBuf, LPDWORD cbFilterBufNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "pbFilterBuf", "cbFilterBuf", "cbFilterBufNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmShutdown(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmShutdown(DWORD dwSessionHandle, ULONG lActionFlags, RM_WRITE_STATUS_CALLBACK fnStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "lActionFlags", "fnStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmRemoveFilter(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmRemoveFilter(DWORD dwSessionHandle, LPCWSTR strFilename, RM_UNIQUE_PROCESS* Application, LPCWSTR strShortServiceName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "strFilename", "Application", "strShortServiceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmRestart(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmRestart(DWORD dwSessionHandle, DWORD dwRestartFlags, RM_WRITE_STATUS_CALLBACK fnStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "dwRestartFlags", "fnStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmCancelCurrentTask(jitter):
    """"
    [Rstrtmgr.dll] [ERROR_CODE] RmCancelCurrentTask(DWORD dwSessionHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
