###### Enums ######
EFaultRepRetVal = {
    "frrvOk": 0,
    "frrvOkManifest": 1,
    "frrvOkQueued": 2,
    "frrvErr": 3,
    "frrvErrNoDW": 4,
    "frrvErrTimeout": 5,
    "frrvLaunchDebugger": 6,
    "frrvOkHeadless": 7,
    "frrvErrAnotherInstance": 8,
}
EFaultRepRetVal_INV = {
    0: "frrvOk",
    1: "frrvOkManifest",
    2: "frrvOkQueued",
    3: "frrvErr",
    4: "frrvErrNoDW",
    5: "frrvErrTimeout",
    6: "frrvLaunchDebugger",
    7: "frrvOkHeadless",
    8: "frrvErrAnotherInstance",
}

###################

###### Types ######
EFaultRepRetVal = UINT

###################

###### Functions ######

def faultrep_WerReportHang(jitter):
    """
    HRESULT WerReportHang(
        HWND hwndHungWinow,
        PCWSTR wszHungApplicationName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndHungWinow", "wszHungApplicationName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def faultrep_AddERExcludedApplication(jitter, get_str, set_str):
    """
    BOOL AddERExcludedApplication(
        LPCTSTR szApplication
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szApplication"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def faultrep_AddERExcludedApplicationA(jitter):
    faultrep_AddERExcludedApplication(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def faultrep_AddERExcludedApplicationW(jitter):
    faultrep_AddERExcludedApplication(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def faultrep_ReportFault(jitter):
    """
    EFaultRepRetVal ReportFault(
        LPEXCEPTION_POINTERS pep,
        DWORD dwMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pep", "dwMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
