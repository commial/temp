###### Enums ######
RM_FILTER_ACTION = {
    "RmInvalidFilterAction": 0,
    "RmNoRestart": 1,
    "RmNoShutdown": 2,
}
RM_FILTER_ACTION_INV = {
    0: "RmInvalidFilterAction",
    1: "RmNoRestart",
    2: "RmNoShutdown",
}
RM_APP_TYPE = {
    "RmUnknownApp": 0,
    "RmMainWindow": 1,
    "RmOtherWindow": 2,
    "RmService": 3,
    "RmExplorer": 4,
    "RmConsole": 5,
    "RmCritical": 1000,
}
RM_APP_TYPE_INV = {
    0: "RmUnknownApp",
    1: "RmMainWindow",
    2: "RmOtherWindow",
    3: "RmService",
    4: "RmExplorer",
    5: "RmConsole",
    1000: "RmCritical",
}

###################

###### Types ######
RM_WRITE_STATUS_CALLBACK = LPVOID
const_WCHAR___ = WCHAR___
WCHAR__CCH_RM_MAX_APP_NAME_+_1_ = Array(WCHAR, 256)
WCHAR__CCH_RM_MAX_SVC_NAME_+_1_ = Array(WCHAR, 64)

class RM_UNIQUE_PROCESS(MemStruct):
    fields = [
        ("dwProcessId", DWORD()),
        ("ProcessStartTime", FILETIME()),
    ]

RM_UNIQUE_PROCESS_PTR = Ptr("<I", RM_UNIQUE_PROCESS())
RM_UNIQUE_PROCESS___ = Ptr("<I", RM_UNIQUE_PROCESS())
RM_FILTER_ACTION = UINT
RM_APP_TYPE = UINT

class RM_PROCESS_INFO(MemStruct):
    fields = [
        ("Process", RM_UNIQUE_PROCESS()),
        ("strAppName", WCHAR__CCH_RM_MAX_APP_NAME_+_1_()),
        ("strServiceShortName", WCHAR__CCH_RM_MAX_SVC_NAME_+_1_()),
        ("ApplicationType", RM_APP_TYPE()),
        ("AppStatus", ULONG()),
        ("TSSessionId", DWORD()),
        ("bRestartable", BOOL()),
    ]

RM_PROCESS_INFO___ = Ptr("<I", RM_PROCESS_INFO())

###################

###### Functions ######

def rstrtmgr_RmAddFilter(jitter):
    """
    [ERROR_CODE] RmAddFilter(
        DWORD dwSessionHandle,
        LPCWSTR strFilename,
        RM_UNIQUE_PROCESS* Application,
        LPCWSTR strShortServiceName,
        RM_FILTER_ACTION ActionType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "strFilename", "Application", "strShortServiceName", "ActionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmStartSession(jitter):
    """
    [ERROR_CODE] RmStartSession(
        DWORD* pSessionHandle,
        DWORD dwSessionFlags,
        WCHAR [] strSessionKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSessionHandle", "dwSessionFlags", "strSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmJoinSession(jitter):
    """
    [ERROR_CODE] RmJoinSession(
        DWORD* pSessionHandle,
        const WCHAR [] strSessionKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSessionHandle", "strSessionKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmEndSession(jitter):
    """
    [ERROR_CODE] RmEndSession(
        DWORD dwSessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmRegisterResources(jitter):
    """
    [ERROR_CODE] RmRegisterResources(
        DWORD dwSessionHandle,
        UINT nFiles,
        LPCWSTR [] rgsFileNames,
        UINT nApplications,
        RM_UNIQUE_PROCESS [] rgApplications,
        UINT nServices,
        LPCWSTR [] rgsServiceNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "nFiles", "rgsFileNames", "nApplications", "rgApplications", "nServices", "rgsServiceNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmGetList(jitter):
    """
    [ERROR_CODE] RmGetList(
        DWORD dwSessionHandle,
        UINT* pnProcInfoNeeded,
        UINT* pnProcInfo,
        RM_PROCESS_INFO [] rgAffectedApps,
        LPDWORD lpdwRebootReasons
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "pnProcInfoNeeded", "pnProcInfo", "rgAffectedApps", "lpdwRebootReasons"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmGetFilterList(jitter):
    """
    [ERROR_CODE] RmGetFilterList(
        DWORD dwSessionHandle,
        PBYTE pbFilterBuf,
        DWORD cbFilterBuf,
        LPDWORD cbFilterBufNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "pbFilterBuf", "cbFilterBuf", "cbFilterBufNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmShutdown(jitter):
    """
    [ERROR_CODE] RmShutdown(
        DWORD dwSessionHandle,
        ULONG lActionFlags,
        RM_WRITE_STATUS_CALLBACK fnStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "lActionFlags", "fnStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmRemoveFilter(jitter):
    """
    [ERROR_CODE] RmRemoveFilter(
        DWORD dwSessionHandle,
        LPCWSTR strFilename,
        RM_UNIQUE_PROCESS* Application,
        LPCWSTR strShortServiceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "strFilename", "Application", "strShortServiceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmRestart(jitter):
    """
    [ERROR_CODE] RmRestart(
        DWORD dwSessionHandle,
        DWORD dwRestartFlags,
        RM_WRITE_STATUS_CALLBACK fnStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle", "dwRestartFlags", "fnStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rstrtmgr_RmCancelCurrentTask(jitter):
    """
    [ERROR_CODE] RmCancelCurrentTask(
        DWORD dwSessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
