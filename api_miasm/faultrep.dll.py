
def faultrep_WerReportHang(jitter):
    """"
    [Faultrep.dll] HRESULT WerReportHang(HWND hwndHungWinow, PCWSTR wszHungApplicationName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndHungWinow", "wszHungApplicationName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def faultrep_AddERExcludedApplication(jitter):
    """"
    [Faultrep.dll] BOOL AddERExcludedApplication(LPCTSTR szApplication)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szApplication"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def faultrep_ReportFault(jitter):
    """"
    [Faultrep.dll] EFaultRepRetVal ReportFault(LPEXCEPTION_POINTERS pep, DWORD dwMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pep", "dwMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
