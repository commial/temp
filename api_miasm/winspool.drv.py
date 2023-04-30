_DeviceCapability_ = {
    "DC_FIELDS": 1,
    "DC_PAPERS": 2,
    "DC_PAPERSIZE": 3,
    "DC_MINEXTENT": 4,
    "DC_MAXEXTENT": 5,
    "DC_BINS": 6,
    "DC_DUPLEX": 7,
    "DC_SIZE": 8,
    "DC_EXTRA": 9,
    "DC_VERSION": 10,
    "DC_DRIVER": 11,
    "DC_BINNAMES": 12,
    "DC_ENUMRESOLUTIONS": 13,
    "DC_FILEDEPENDENCIES": 14,
    "DC_TRUETYPE": 15,
    "DC_PAPERNAMES": 16,
    "DC_ORIENTATION": 17,
    "DC_COPIES": 18,
    "DC_BINADJUST": 19,
    "DC_EMF_COMPLIANT": 20,
    "DC_DATATYPE_PRODUCED": 21,
    "DC_COLLATE": 22,
    "DC_MANUFACTURER": 23,
    "DC_MODEL": 24,
    "DC_PERSONALITY": 25,
    "DC_PRINTRATE": 26,
    "DC_PRINTRATEUNIT": 27,
    "DC_PRINTERMEM": 28,
    "DC_MEDIAREADY": 29,
    "DC_STAPLE": 30,
    "DC_PRINTRATEPPM": 31,
    "DC_COLORDEVICE": 32,
    "DC_NUP": 33,
    "DC_MEDIATYPENAMES": 34,
    "DC_MEDIATYPES": 35,
}
_DeviceCapability__INV = {
    1: "DC_FIELDS",
    2: "DC_PAPERS",
    3: "DC_PAPERSIZE",
    4: "DC_MINEXTENT",
    5: "DC_MAXEXTENT",
    6: "DC_BINS",
    7: "DC_DUPLEX",
    8: "DC_SIZE",
    9: "DC_EXTRA",
    10: "DC_VERSION",
    11: "DC_DRIVER",
    12: "DC_BINNAMES",
    13: "DC_ENUMRESOLUTIONS",
    14: "DC_FILEDEPENDENCIES",
    15: "DC_TRUETYPE",
    16: "DC_PAPERNAMES",
    17: "DC_ORIENTATION",
    18: "DC_COPIES",
    19: "DC_BINADJUST",
    20: "DC_EMF_COMPLIANT",
    21: "DC_DATATYPE_PRODUCED",
    22: "DC_COLLATE",
    23: "DC_MANUFACTURER",
    24: "DC_MODEL",
    25: "DC_PERSONALITY",
    26: "DC_PRINTRATE",
    27: "DC_PRINTRATEUNIT",
    28: "DC_PRINTERMEM",
    29: "DC_MEDIAREADY",
    30: "DC_STAPLE",
    31: "DC_PRINTRATEPPM",
    32: "DC_COLORDEVICE",
    33: "DC_NUP",
    34: "DC_MEDIATYPENAMES",
    35: "DC_MEDIATYPES",
}
_JobControl_ = {
    "JOB_CONTROL_PAUSE": 1,
    "JOB_CONTROL_RESUME": 2,
    "JOB_CONTROL_CANCEL": 3,
    "JOB_CONTROL_RESTART": 4,
    "JOB_CONTROL_DELETE": 5,
    "JOB_CONTROL_SENT_TO_PRINTER": 6,
    "JOB_CONTROL_LAST_PAGE_EJECTED": 7,
    "JOB_CONTROL_RETAIN": 8,
    "JOB_CONTROL_RELEASE": 9,
}
_JobControl__INV = {
    1: "JOB_CONTROL_PAUSE",
    2: "JOB_CONTROL_RESUME",
    3: "JOB_CONTROL_CANCEL",
    4: "JOB_CONTROL_RESTART",
    5: "JOB_CONTROL_DELETE",
    6: "JOB_CONTROL_SENT_TO_PRINTER",
    7: "JOB_CONTROL_LAST_PAGE_EJECTED",
    8: "JOB_CONTROL_RETAIN",
    9: "JOB_CONTROL_RELEASE",
}
_PrinterControl_ = {
    "PRINTER_CONTROL_PAUSE": 1,
    "PRINTER_CONTROL_RESUME": 2,
    "PRINTER_CONTROL_PURGE": 3,
    "PRINTER_CONTROL_SET_STATUS": 4,
}
_PrinterControl__INV = {
    1: "PRINTER_CONTROL_PAUSE",
    2: "PRINTER_CONTROL_RESUME",
    3: "PRINTER_CONTROL_PURGE",
    4: "PRINTER_CONTROL_SET_STATUS",
}
EPrintXPSJobOperation = {
    "kJobProduction": 1,
    "kJobConsumption": 2,
}
EPrintXPSJobOperation_INV = {
    1: "kJobProduction",
    2: "kJobConsumption",
}
EPrintXPSJobProgress = {
    "kAddingDocumentSequence": 0,
    "kDocumentSequenceAdded": 1,
    "kAddingFixedDocument": 2,
    "kFixedDocumentAdded": 3,
    "kAddingFixedPage": 4,
    "kFixedPageAdded": 5,
    "kResourceAdded": 6,
    "kFontAdded": 7,
    "kImageAdded": 8,
    "kXpsDocumentCommitted": 9,
}
EPrintXPSJobProgress_INV = {
    0: "kAddingDocumentSequence",
    1: "kDocumentSequenceAdded",
    2: "kAddingFixedDocument",
    3: "kFixedDocumentAdded",
    4: "kAddingFixedPage",
    5: "kFixedPageAdded",
    6: "kResourceAdded",
    7: "kFontAdded",
    8: "kImageAdded",
    9: "kXpsDocumentCommitted",
}
PrintAsyncNotifyUserFilter = {
    "kPerUser": 0,
    "kAllUsers": 1,
}
PrintAsyncNotifyUserFilter_INV = {
    0: "kPerUser",
    1: "kAllUsers",
}
PrintAsyncNotifyConversationStyle = {
    "kBiDirectional": 0,
    "kUniDirectional": 1,
}
PrintAsyncNotifyConversationStyle_INV = {
    0: "kBiDirectional",
    1: "kUniDirectional",
}

def winspool_AddJob(jitter, get_str, set_str):
    """
    BOOL AddJob(
        HANDLE hPrinter,
        DWORD Level,
        LPBYTE pData,
        DWORD cbBuf,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pData", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddJobA(jitter):
    winspool_AddJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddJobW(jitter):
    winspool_AddJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddMonitor(jitter, get_str, set_str):
    """
    BOOL AddMonitor(
        LPTSTR pName,
        DWORD Level,
        LPBYTE pMonitors
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pMonitors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddMonitorA(jitter):
    winspool_AddMonitor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddMonitorW(jitter):
    winspool_AddMonitor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddPrinter(jitter, get_str, set_str):
    """
    HANDLE AddPrinter(
        LPTSTR* pName,
        DWORD Level,
        LPBYTE pPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterA(jitter):
    winspool_AddPrinter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddPrinterW(jitter):
    winspool_AddPrinter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddPrinterConnection(jitter, get_str, set_str):
    """
    BOOL AddPrinterConnection(
        LPTSTR pName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterConnectionA(jitter):
    winspool_AddPrinterConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddPrinterConnectionW(jitter):
    winspool_AddPrinterConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddPrinterConnection2(jitter, get_str, set_str):
    """
    BOOL AddPrinterConnection2(
        HWND hWnd,
        LPCTSTR pszName,
        DWORD dwLevel,
        PVOID pConnectionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pszName", "dwLevel", "pConnectionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterConnection2A(jitter):
    winspool_AddPrinterConnection2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddPrinterConnection2W(jitter):
    winspool_AddPrinterConnection2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddPrinterDriver(jitter, get_str, set_str):
    """
    BOOL AddPrinterDriver(
        LPTSTR pName,
        DWORD Level,
        LPBYTE pDriverInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pDriverInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterDriverA(jitter):
    winspool_AddPrinterDriver(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddPrinterDriverW(jitter):
    winspool_AddPrinterDriver(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddPrinterDriverEx(jitter, get_str, set_str):
    """
    BOOL AddPrinterDriverEx(
        LPTSTR pName,
        DWORD Level,
        LPBYTE pDriverInfo,
        DWORD dwFileCopyFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pDriverInfo", "dwFileCopyFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterDriverExA(jitter):
    winspool_AddPrinterDriverEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddPrinterDriverExW(jitter):
    winspool_AddPrinterDriverEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddPrintProcessor(jitter, get_str, set_str):
    """
    BOOL AddPrintProcessor(
        LPTSTR pName,
        LPTSTR pEnvironment,
        LPTSTR pPathName,
        LPTSTR pPrintProcessorName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pPathName", "pPrintProcessorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrintProcessorA(jitter):
    winspool_AddPrintProcessor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddPrintProcessorW(jitter):
    winspool_AddPrintProcessor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddPrintProvidor(jitter, get_str, set_str):
    """
    BOOL AddPrintProvidor(
        LPTSTR pName,
        DWORD Level,
        LPBYTE pProviderInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pProviderInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrintProvidorA(jitter):
    winspool_AddPrintProvidor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddPrintProvidorW(jitter):
    winspool_AddPrintProvidor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_ConfigurePort(jitter, get_str, set_str):
    """
    BOOL ConfigurePort(
        LPTSTR pName,
        HWND hWnd,
        LPTSTR pPortName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "hWnd", "pPortName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ConfigurePortA(jitter):
    winspool_ConfigurePort(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_ConfigurePortW(jitter):
    winspool_ConfigurePort(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeleteForm(jitter, get_str, set_str):
    """
    BOOL DeleteForm(
        HANDLE hPrinter,
        LPTSTR pFormName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pFormName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeleteFormA(jitter):
    winspool_DeleteForm(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeleteFormW(jitter):
    winspool_DeleteForm(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeleteMonitor(jitter, get_str, set_str):
    """
    BOOL DeleteMonitor(
        LPTSTR pName,
        LPTSTR pEnvironment,
        LPTSTR pMonitorName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pMonitorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeleteMonitorA(jitter):
    winspool_DeleteMonitor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeleteMonitorW(jitter):
    winspool_DeleteMonitor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePort(jitter, get_str, set_str):
    """
    BOOL DeletePort(
        LPTSTR pName,
        HWND hWnd,
        LPTSTR pPortName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "hWnd", "pPortName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePortA(jitter):
    winspool_DeletePort(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePortW(jitter):
    winspool_DeletePort(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrinterConnection(jitter, get_str, set_str):
    """
    BOOL DeletePrinterConnection(
        LPTSTR pName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterConnectionA(jitter):
    winspool_DeletePrinterConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrinterConnectionW(jitter):
    winspool_DeletePrinterConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrinterData(jitter, get_str, set_str):
    """
    [ERROR_CODE] DeletePrinterData(
        HANDLE hPrinter,
        LPTSTR pValueName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pValueName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDataA(jitter):
    winspool_DeletePrinterData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrinterDataW(jitter):
    winspool_DeletePrinterData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrinterDataEx(jitter, get_str, set_str):
    """
    [ERROR_CODE] DeletePrinterDataEx(
        HANDLE hPrinter,
        LPCTSTR pKeyName,
        LPCTSTR pValueName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pValueName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDataExA(jitter):
    winspool_DeletePrinterDataEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrinterDataExW(jitter):
    winspool_DeletePrinterDataEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrinterDriver(jitter, get_str, set_str):
    """
    BOOL DeletePrinterDriver(
        LPTSTR pName,
        LPTSTR pEnvironment,
        LPTSTR pDriverName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pDriverName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDriverA(jitter):
    winspool_DeletePrinterDriver(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrinterDriverW(jitter):
    winspool_DeletePrinterDriver(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrinterDriverEx(jitter, get_str, set_str):
    """
    BOOL DeletePrinterDriverEx(
        LPTSTR pName,
        LPTSTR pEnvironment,
        LPTSTR pDriverName,
        DWORD dwDeleteFlag,
        DWORD dwVersionFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pDriverName", "dwDeleteFlag", "dwVersionFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDriverExA(jitter):
    winspool_DeletePrinterDriverEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrinterDriverExW(jitter):
    winspool_DeletePrinterDriverEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrinterKey(jitter, get_str, set_str):
    """
    [ERROR_CODE] DeletePrinterKey(
        HANDLE hPrinter,
        LPCTSTR pKeyName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterKeyA(jitter):
    winspool_DeletePrinterKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrinterKeyW(jitter):
    winspool_DeletePrinterKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrintProcessor(jitter, get_str, set_str):
    """
    BOOL DeletePrintProcessor(
        LPTSTR pName,
        LPTSTR pEnvironment,
        LPTSTR pPrintProcessorName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pPrintProcessorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrintProcessorA(jitter):
    winspool_DeletePrintProcessor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrintProcessorW(jitter):
    winspool_DeletePrintProcessor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrintProvidor(jitter, get_str, set_str):
    """
    BOOL DeletePrintProvidor(
        LPTSTR pName,
        LPTSTR pEnvironment,
        LPTSTR pPrintProviderName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pPrintProviderName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrintProvidorA(jitter):
    winspool_DeletePrintProvidor(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrintProvidorW(jitter):
    winspool_DeletePrintProvidor(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumForms(jitter, get_str, set_str):
    """
    BOOL EnumForms(
        HANDLE hPrinter,
        DWORD Level,
        LPBYTE pForm,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pForm", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumFormsA(jitter):
    winspool_EnumForms(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumFormsW(jitter):
    winspool_EnumForms(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumJobs(jitter, get_str, set_str):
    """
    BOOL EnumJobs(
        HANDLE hPrinter,
        DWORD FirstJob,
        DWORD NoJobs,
        DWORD Level,
        LPBYTE pJob,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "FirstJob", "NoJobs", "Level", "pJob", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumJobsA(jitter):
    winspool_EnumJobs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumJobsW(jitter):
    winspool_EnumJobs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumMonitors(jitter, get_str, set_str):
    """
    BOOL EnumMonitors(
        LPTSTR pName,
        DWORD Level,
        LPBYTE pMonitors,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pMonitors", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumMonitorsA(jitter):
    winspool_EnumMonitors(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumMonitorsW(jitter):
    winspool_EnumMonitors(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumPorts(jitter, get_str, set_str):
    """
    BOOL EnumPorts(
        LPTSTR pName,
        DWORD Level,
        LPBYTE pPorts,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pPorts", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPortsA(jitter):
    winspool_EnumPorts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumPortsW(jitter):
    winspool_EnumPorts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumPrinterData(jitter, get_str, set_str):
    """
    [ERROR_CODE] EnumPrinterData(
        HANDLE hPrinter,
        DWORD dwIndex,
        LPTSTR pValueName,
        DWORD cbValueName,
        LPDWORD pcbValueName,
        LPDWORD pType,
        LPBYTE pData,
        DWORD cbData,
        LPDWORD pcbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "dwIndex", "pValueName", "cbValueName", "pcbValueName", "pType", "pData", "cbData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinterDataA(jitter):
    winspool_EnumPrinterData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumPrinterDataW(jitter):
    winspool_EnumPrinterData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumPrinterDataEx(jitter, get_str, set_str):
    """
    [ERROR_CODE] EnumPrinterDataEx(
        HANDLE hPrinter,
        LPCTSTR pKeyName,
        LPBYTE pEnumValues,
        DWORD cbEnumValues,
        LPDWORD pcbEnumValues,
        LPDWORD pnEnumValues
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pEnumValues", "cbEnumValues", "pcbEnumValues", "pnEnumValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinterDataExA(jitter):
    winspool_EnumPrinterDataEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumPrinterDataExW(jitter):
    winspool_EnumPrinterDataEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumPrinterDrivers(jitter, get_str, set_str):
    """
    BOOL EnumPrinterDrivers(
        LPTSTR pName,
        LPTSTR pEnvironment,
        DWORD Level,
        LPBYTE pDriverInfo,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "Level", "pDriverInfo", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinterDriversA(jitter):
    winspool_EnumPrinterDrivers(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumPrinterDriversW(jitter):
    winspool_EnumPrinterDrivers(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumPrinterKey(jitter, get_str, set_str):
    """
    [ERROR_CODE] EnumPrinterKey(
        HANDLE hPrinter,
        LPCTSTR pKeyName,
        LPTSTR pSubkey,
        DWORD cbSubkey,
        LPDWORD pcbSubkey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pSubkey", "cbSubkey", "pcbSubkey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinterKeyA(jitter):
    winspool_EnumPrinterKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumPrinterKeyW(jitter):
    winspool_EnumPrinterKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumPrinters(jitter, get_str, set_str):
    """
    BOOL EnumPrinters(
        [EnumPrintersFlags] Flags,
        LPTSTR Name,
        DWORD Level,
        LPBYTE pPrinterEnum,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Name", "Level", "pPrinterEnum", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrintersA(jitter):
    winspool_EnumPrinters(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumPrintersW(jitter):
    winspool_EnumPrinters(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumPrintProcessorDatatypes(jitter, get_str, set_str):
    """
    BOOL EnumPrintProcessorDatatypes(
        LPTSTR pName,
        LPTSTR pPrintProcessorName,
        DWORD Level,
        LPBYTE pDatatypes,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pPrintProcessorName", "Level", "pDatatypes", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrintProcessorDatatypesA(jitter):
    winspool_EnumPrintProcessorDatatypes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumPrintProcessorDatatypesW(jitter):
    winspool_EnumPrintProcessorDatatypes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EnumPrintProcessors(jitter, get_str, set_str):
    """
    BOOL EnumPrintProcessors(
        LPTSTR pName,
        LPTSTR pEnvironment,
        DWORD Level,
        LPBYTE pPrintProcessorInfo,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "Level", "pPrintProcessorInfo", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrintProcessorsA(jitter):
    winspool_EnumPrintProcessors(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_EnumPrintProcessorsW(jitter):
    winspool_EnumPrintProcessors(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_FlushPrinter(jitter):
    """
    BOOL FlushPrinter(
        HANDLE hPrinter,
        LPVOID pBuf,
        DWORD cbBuf,
        LPDWORD pcWritten,
        DWORD cSleep
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pBuf", "cbBuf", "pcWritten", "cSleep"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetForm(jitter, get_str, set_str):
    """
    BOOL GetForm(
        HANDLE hPrinter,
        LPTSTR pFormName,
        DWORD Level,
        LPBYTE pForm,
        DWORD cbBuf,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pFormName", "Level", "pForm", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetFormA(jitter):
    winspool_GetForm(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetFormW(jitter):
    winspool_GetForm(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetJob(jitter, get_str, set_str):
    """
    BOOL GetJob(
        HANDLE hPrinter,
        DWORD JobId,
        DWORD Level,
        LPBYTE pJob,
        DWORD cbBuf,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "JobId", "Level", "pJob", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetJobA(jitter):
    winspool_GetJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetJobW(jitter):
    winspool_GetJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetPrinter(jitter, get_str, set_str):
    """
    BOOL GetPrinter(
        HANDLE hPrinter,
        DWORD Level,
        LPBYTE pPrinter,
        DWORD cbBuf,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pPrinter", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterA(jitter):
    winspool_GetPrinter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetPrinterW(jitter):
    winspool_GetPrinter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetPrinterData(jitter, get_str, set_str):
    """
    [ERROR_CODE] GetPrinterData(
        HANDLE hPrinter,
        LPTSTR pValueName,
        [RegType*] pType,
        LPBYTE pData,
        DWORD nSize,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pValueName", "pType", "pData", "nSize", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDataA(jitter):
    winspool_GetPrinterData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetPrinterDataW(jitter):
    winspool_GetPrinterData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetPrinterDataEx(jitter, get_str, set_str):
    """
    [ERROR_CODE] GetPrinterDataEx(
        HANDLE hPrinter,
        LPCTSTR pKeyName,
        LPCTSTR pValueName,
        [RegType*] pType,
        LPBYTE pData,
        DWORD nSize,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pValueName", "pType", "pData", "nSize", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDataExA(jitter):
    winspool_GetPrinterDataEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetPrinterDataExW(jitter):
    winspool_GetPrinterDataEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetPrinterDriver(jitter, get_str, set_str):
    """
    BOOL GetPrinterDriver(
        HANDLE hPrinter,
        LPTSTR pEnvironment,
        DWORD Level,
        LPBYTE pDriverInfo,
        DWORD cbBuf,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pEnvironment", "Level", "pDriverInfo", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDriverA(jitter):
    winspool_GetPrinterDriver(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetPrinterDriverW(jitter):
    winspool_GetPrinterDriver(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetPrinterDriverDirectory(jitter, get_str, set_str):
    """
    BOOL GetPrinterDriverDirectory(
        LPTSTR pName,
        LPTSTR pEnvironment,
        DWORD Level,
        LPWSTR pDriverDirectory,
        DWORD cbBuf,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "Level", "pDriverDirectory", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDriverDirectoryA(jitter):
    winspool_GetPrinterDriverDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetPrinterDriverDirectoryW(jitter):
    winspool_GetPrinterDriverDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetPrintProcessorDirectory(jitter, get_str, set_str):
    """
    BOOL GetPrintProcessorDirectory(
        LPTSTR pName,
        LPTSTR pEnvironment,
        DWORD Level,
        LPBYTE pPrintProcessorInfo,
        DWORD cbBuf,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "Level", "pPrintProcessorInfo", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrintProcessorDirectoryA(jitter):
    winspool_GetPrintProcessorDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetPrintProcessorDirectoryW(jitter):
    winspool_GetPrintProcessorDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_OpenPrinter(jitter, get_str, set_str):
    """
    BOOL OpenPrinter(
        LPTSTR pPrinterName,
        LPHANDLE phPrinter,
        LPPRINTER_DEFAULTS pDefault
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPrinterName", "phPrinter", "pDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_OpenPrinterA(jitter):
    winspool_OpenPrinter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_OpenPrinterW(jitter):
    winspool_OpenPrinter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_ResetPrinter(jitter, get_str, set_str):
    """
    BOOL ResetPrinter(
        HANDLE hPrinter,
        LPPRINTER_DEFAULTS pDefault
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ResetPrinterA(jitter):
    winspool_ResetPrinter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_ResetPrinterW(jitter):
    winspool_ResetPrinter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_StartDocPrinter(jitter, get_str, set_str):
    """
    DWORD StartDocPrinter(
        HANDLE hPrinter,
        DWORD Level,
        LPBYTE pDocInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pDocInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_StartDocPrinterA(jitter):
    winspool_StartDocPrinter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_StartDocPrinterW(jitter):
    winspool_StartDocPrinter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_SetForm(jitter, get_str, set_str):
    """
    BOOL SetForm(
        HANDLE hPrinter,
        LPTSTR pFormName,
        DWORD Level,
        LPTSTR pForm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pFormName", "Level", "pForm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetFormA(jitter):
    winspool_SetForm(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_SetFormW(jitter):
    winspool_SetForm(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_SetJob(jitter, get_str, set_str):
    """
    BOOL SetJob(
        HANDLE hPrinter,
        DWORD JobId,
        DWORD Level,
        LPBYTE pJob,
        [JobControl] Command
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "JobId", "Level", "pJob", "Command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetJobA(jitter):
    winspool_SetJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_SetJobW(jitter):
    winspool_SetJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_SetPort(jitter, get_str, set_str):
    """
    BOOL SetPort(
        LPTSTR pName,
        LPTSTR pPortName,
        DWORD dwLevel,
        LPBYTE pPortInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pPortName", "dwLevel", "pPortInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetPortA(jitter):
    winspool_SetPort(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_SetPortW(jitter):
    winspool_SetPort(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_SetPrinter(jitter, get_str, set_str):
    """
    BOOL SetPrinter(
        HANDLE hPrinter,
        DWORD Level,
        LPBYTE pPrinter,
        [PrinterControl] Command
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pPrinter", "Command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetPrinterA(jitter):
    winspool_SetPrinter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_SetPrinterW(jitter):
    winspool_SetPrinter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_SetPrinterData(jitter, get_str, set_str):
    """
    [ERROR_CODE] SetPrinterData(
        HANDLE hPrinter,
        LPTSTR pValueName,
        [RegType] Type,
        LPBYTE pData,
        DWORD cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pValueName", "Type", "pData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetPrinterDataA(jitter):
    winspool_SetPrinterData(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_SetPrinterDataW(jitter):
    winspool_SetPrinterData(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_SetPrinterDataEx(jitter, get_str, set_str):
    """
    [ERROR_CODE] SetPrinterDataEx(
        HANDLE hPrinter,
        LPCTSTR pKeyName,
        LPCTSTR pValueName,
        [RegType] Type,
        LPBYTE pData,
        DWORD cbData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pValueName", "Type", "pData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetPrinterDataExA(jitter):
    winspool_SetPrinterDataEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_SetPrinterDataExW(jitter):
    winspool_SetPrinterDataEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeviceCapabilities(jitter, get_str, set_str):
    """
    DWORD DeviceCapabilities(
        LPCTSTR pDevice,
        LPCTSTR pPort,
        [DeviceCapability] fwCapability,
        LPTSTR pOutput,
        const DEVMODE* pDevMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDevice", "pPort", "fwCapability", "pOutput", "pDevMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeviceCapabilitiesA(jitter):
    winspool_DeviceCapabilities(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeviceCapabilitiesW(jitter):
    winspool_DeviceCapabilities(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_CorePrinterDriverInstalled(jitter, get_str, set_str):
    """
    HRESULT CorePrinterDriverInstalled(
        LPCTSTR pszServer,
        LPCTSTR pszEnvironment,
        GUID CoreDriverGUID,
        FILETIME ftDriverDate,
        DWORDLONG dwlDriverVersion,
        BOOL* pbDriverInstalled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszEnvironment", "CoreDriverGUID", "ftDriverDate", "dwlDriverVersion", "pbDriverInstalled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_CorePrinterDriverInstalledA(jitter):
    winspool_CorePrinterDriverInstalled(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_CorePrinterDriverInstalledW(jitter):
    winspool_CorePrinterDriverInstalled(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_DeletePrinterDriverPackage(jitter, get_str, set_str):
    """
    HRESULT DeletePrinterDriverPackage(
        LPCTSTR pszServer,
        LPCTSTR pszInfPath,
        LPCTSTR pszEnvironment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszInfPath", "pszEnvironment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDriverPackageA(jitter):
    winspool_DeletePrinterDriverPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DeletePrinterDriverPackageW(jitter):
    winspool_DeletePrinterDriverPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetCorePrinterDrivers(jitter, get_str, set_str):
    """
    HRESULT GetCorePrinterDrivers(
        LPCTSTR pszServer,
        LPCTSTR pszEnvironment,
        LPCTSTR pszzCoreDriverDependencies,
        DWORD cCorePrinterDrivers,
        PCORE_PRINTER_DRIVER pCorePrinterDrivers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszEnvironment", "pszzCoreDriverDependencies", "cCorePrinterDrivers", "pCorePrinterDrivers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetCorePrinterDriversA(jitter):
    winspool_GetCorePrinterDrivers(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetCorePrinterDriversW(jitter):
    winspool_GetCorePrinterDrivers(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetPrinterDriverPackagePath(jitter, get_str, set_str):
    """
    HRESULT GetPrinterDriverPackagePath(
        LPCTSTR pszServer,
        LPCTSTR pszEnvironment,
        LPCTSTR pszLanguage,
        LPCTSTR pszPackageID,
        LPTSTR pszDriverPackageCab,
        DWORD cchDriverPackageCab,
        LPDWORD pcchRequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszEnvironment", "pszLanguage", "pszPackageID", "pszDriverPackageCab", "cchDriverPackageCab", "pcchRequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDriverPackagePathA(jitter):
    winspool_GetPrinterDriverPackagePath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetPrinterDriverPackagePathW(jitter):
    winspool_GetPrinterDriverPackagePath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_InstallPrinterDriverFromPackage(jitter, get_str, set_str):
    """
    HRESULT InstallPrinterDriverFromPackage(
        LPCTSTR pszServer,
        LPCTSTR pszInfPath,
        LPCTSTR pszDriverName,
        LPCTSTR pszEnvironment,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszInfPath", "pszDriverName", "pszEnvironment", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_InstallPrinterDriverFromPackageA(jitter):
    winspool_InstallPrinterDriverFromPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_InstallPrinterDriverFromPackageW(jitter):
    winspool_InstallPrinterDriverFromPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_UploadPrinterDriverPackage(jitter, get_str, set_str):
    """
    HRESULT UploadPrinterDriverPackage(
        LPCTSTR pszServer,
        LPCTSTR pszInfPath,
        LPCTSTR pszEnvironment,
        DWORD dwFlags,
        HWND hwnd,
        LPTSTR pszDestInfPath,
        PULONG pcchDestInfPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszInfPath", "pszEnvironment", "dwFlags", "hwnd", "pszDestInfPath", "pcchDestInfPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_UploadPrinterDriverPackageA(jitter):
    winspool_UploadPrinterDriverPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_UploadPrinterDriverPackageW(jitter):
    winspool_UploadPrinterDriverPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AbortPrinter(jitter):
    """
    BOOL AbortPrinter(
        HANDLE hPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddForm(jitter, get_str, set_str):
    """
    BOOL AddForm(
        HANDLE hPrinter,
        DWORD Level,
        LPBYTE pForm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pForm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddFormA(jitter):
    winspool_AddForm(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddFormW(jitter):
    winspool_AddForm(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AddPort(jitter, get_str, set_str):
    """
    BOOL AddPort(
        LPTSTR pName,
        HWND hWnd,
        LPTSTR pMonitorName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "hWnd", "pMonitorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPortA(jitter):
    winspool_AddPort(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AddPortW(jitter):
    winspool_AddPort(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_AdvancedDocumentProperties(jitter, get_str, set_str):
    """
    LONG AdvancedDocumentProperties(
        HWND hWnd,
        HANDLE hPrinter,
        LPTSTR pDeviceName,
        PDEVMODE pDevModeOutput,
        PDEVMODE pDevModeInput
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hPrinter", "pDeviceName", "pDevModeOutput", "pDevModeInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AdvancedDocumentPropertiesA(jitter):
    winspool_AdvancedDocumentProperties(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_AdvancedDocumentPropertiesW(jitter):
    winspool_AdvancedDocumentProperties(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_ClosePrinter(jitter):
    """
    BOOL ClosePrinter(
        HANDLE hPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ConnectToPrinterDlg(jitter):
    """
    HANDLE ConnectToPrinterDlg(
        HWND hwnd,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_CreatePrintAsyncNotifyChannel(jitter):
    """
    HRESULT CreatePrintAsyncNotifyChannel(
        LPCWSTR pName,
        PrintAsyncNotificationType* pSchema,
        PrintAsyncNotifyUserFilter filter,
        PrintAsyncNotifyConversationStyle directionality,
        IPrintAsyncNotifyCallback* pCallback,
        IPrintAsyncNotifyChannel** ppChannel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pSchema", "filter", "directionality", "pCallback", "ppChannel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinter(jitter):
    """
    BOOL DeletePrinter(
        HANDLE hPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DocumentProperties(jitter, get_str, set_str):
    """
    LONG DocumentProperties(
        HWND hWnd,
        HANDLE hPrinter,
        LPTSTR pDeviceName,
        PDEVMODE pDevModeOutput,
        PDEVMODE pDevModeInput,
        [DocumentMode] fMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hPrinter", "pDeviceName", "pDevModeOutput", "pDevModeInput", "fMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DocumentPropertiesA(jitter):
    winspool_DocumentProperties(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_DocumentPropertiesW(jitter):
    winspool_DocumentProperties(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_EndDocPrinter(jitter):
    """
    BOOL EndDocPrinter(
        HANDLE hPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EndPagePrinter(jitter):
    """
    BOOL EndPagePrinter(
        HANDLE hPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FindClosePrinterChangeNotification(jitter):
    """
    BOOL FindClosePrinterChangeNotification(
        HANDLE hChange
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChange"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FindFirstPrinterChangeNotification(jitter):
    """
    HANDLE FindFirstPrinterChangeNotification(
        HANDLE hPrinter,
        [PrinterChangeFlags] fdwFilter,
        DWORD fdwOptions,
        PPRINTER_NOTIFY_OPTIONS pPrinterNotifyOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "fdwFilter", "fdwOptions", "pPrinterNotifyOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FindNextPrinterChangeNotification(jitter):
    """
    BOOL FindNextPrinterChangeNotification(
        HANDLE hChange,
        [PrinterChangeFlags*] pdwChange,
        PPRINTER_NOTIFY_OPTIONS pPrinterNotifyOptions,
        LPVOID* ppPrinterNotifyInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChange", "pdwChange", "pPrinterNotifyOptions", "ppPrinterNotifyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FreePrinterNotifyInfo(jitter):
    """
    BOOL FreePrinterNotifyInfo(
        PPRINTER_NOTIFY_INFO pPrinterNotifyInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPrinterNotifyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetDefaultPrinter(jitter, get_str, set_str):
    """
    BOOL GetDefaultPrinter(
        LPTSTR pszBuffer,
        LPDWORD pcchBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszBuffer", "pcchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetDefaultPrinterA(jitter):
    winspool_GetDefaultPrinter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetDefaultPrinterW(jitter):
    winspool_GetDefaultPrinter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_GetPrinterDriver2(jitter, get_str, set_str):
    """
    BOOL GetPrinterDriver2(
        HWND hWnd,
        HANDLE hPrinter,
        LPTSTR pEnvironment,
        DWORD Level,
        LPBYTE pDriverInfo,
        DWORD cbBuf,
        LPDWORD pcbNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hPrinter", "pEnvironment", "Level", "pDriverInfo", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDriver2A(jitter):
    winspool_GetPrinterDriver2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_GetPrinterDriver2W(jitter):
    winspool_GetPrinterDriver2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_OpenPrinter2(jitter, get_str, set_str):
    """
    BOOL OpenPrinter2(
        LPCTSTR pPrinterName,
        LPHANDLE phPrinter,
        LPPRINTER_DEFAULTS pDefault,
        PPRINTER_OPTIONS pOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPrinterName", "phPrinter", "pDefault", "pOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_OpenPrinter2A(jitter):
    winspool_OpenPrinter2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_OpenPrinter2W(jitter):
    winspool_OpenPrinter2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_PrinterProperties(jitter):
    """
    BOOL PrinterProperties(
        HWND hWnd,
        HANDLE hPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ReadPrinter(jitter):
    """
    BOOL ReadPrinter(
        HANDLE hPrinter,
        LPVOID pBuf,
        DWORD cbBuf,
        LPDWORD pNoBytesRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pBuf", "cbBuf", "pNoBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_RegisterForPrintAsyncNotifications(jitter):
    """
    HRESULT RegisterForPrintAsyncNotifications(
        LPCWSTR pName,
        PrintAsyncNotificationType* pSchema,
        PrintAsyncNotifyUserFilter filter,
        PrintAsyncNotifyConversationStyle directionality,
        IPrintAsyncNotifyCallback* pCallback,
        HANDLE* pRegistrationHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName", "pSchema", "filter", "directionality", "pCallback", "pRegistrationHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ReportJobProcessingProgress(jitter):
    """
    HRESULT ReportJobProcessingProgress(
        HANDLE printerHandle,
        ULONG jobId,
        EPrintXPSJobOperation jobOperation,
        EPrintXPSJobProgress jobProgress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["printerHandle", "jobId", "jobOperation", "jobProgress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ScheduleJob(jitter):
    """
    BOOL ScheduleJob(
        HANDLE hPrinter,
        DWORD dwJobID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "dwJobID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetDefaultPrinter(jitter, get_str, set_str):
    """
    BOOL SetDefaultPrinter(
        LPCTSTR pszPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetDefaultPrinterA(jitter):
    winspool_SetDefaultPrinter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winspool_SetDefaultPrinterW(jitter):
    winspool_SetDefaultPrinter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winspool_StartPagePrinter(jitter):
    """
    BOOL StartPagePrinter(
        HANDLE hPrinter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_UnRegisterForPrintAsyncNotifications(jitter):
    """
    HRESULT UnRegisterForPrintAsyncNotifications(
        HANDLE hRegistrationHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRegistrationHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_WritePrinter(jitter):
    """
    BOOL WritePrinter(
        HANDLE hPrinter,
        LPVOID pBuf,
        DWORD cbBuf,
        LPDWORD pcWritten
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pBuf", "cbBuf", "pcWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
