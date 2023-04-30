
def pdh_PdhAddCounter(jitter, get_str, set_str):
    """
    PDH_STATUS PdhAddCounter(
        PDH_HQUERY hQuery,
        LPCTSTR szFullCounterPath,
        DWORD_PTR dwUserData,
        PDH_HCOUNTER* phCounter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "szFullCounterPath", "dwUserData", "phCounter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhAddCounterA(jitter):
    pdh_PdhAddCounter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhAddCounterW(jitter):
    pdh_PdhAddCounter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhAddEnglishCounter(jitter, get_str, set_str):
    """
    PDH_STATUS PdhAddEnglishCounter(
        PDH_HQUERY hQuery,
        LPCTSTR szFullCounterPath,
        DWORD_PTR dwUserData,
        PDH_HCOUNTER* phCounter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "szFullCounterPath", "dwUserData", "phCounter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhAddEnglishCounterA(jitter):
    pdh_PdhAddEnglishCounter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhAddEnglishCounterW(jitter):
    pdh_PdhAddEnglishCounter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhBindInputDataSource(jitter, get_str, set_str):
    """
    PDH_STATUS PdhBindInputDataSource(
        PDH_HLOG* phDataSource,
        LPCTSTR szLogFileNameList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phDataSource", "szLogFileNameList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhBindInputDataSourceA(jitter):
    pdh_PdhBindInputDataSource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhBindInputDataSourceW(jitter):
    pdh_PdhBindInputDataSource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhBrowseCounters(jitter, get_str, set_str):
    """
    PDH_STATUS PdhBrowseCounters(
        PPDH_BROWSE_DLG_CONFIG pBrowseDlgData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBrowseDlgData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhBrowseCountersA(jitter):
    pdh_PdhBrowseCounters(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhBrowseCountersW(jitter):
    pdh_PdhBrowseCounters(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhBrowseCountersH(jitter, get_str, set_str):
    """
    PDH_STATUS PdhBrowseCountersH(
        PPDH_BROWSE_DLG_CONFIG pBrowseDlgData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBrowseDlgData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhBrowseCountersHA(jitter):
    pdh_PdhBrowseCountersH(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhBrowseCountersHW(jitter):
    pdh_PdhBrowseCountersH(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhCalculateCounterFromRawValue(jitter):
    """
    PDH_STATUS PdhCalculateCounterFromRawValue(
        PDH_HCOUNTER hCounter,
        [PdhFormatFlags] dwFormat,
        PPDH_RAW_COUNTER rawValue1,
        PPDH_RAW_COUNTER rawValue2,
        PPDH_FMT_COUNTERVALUE fmtValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "dwFormat", "rawValue1", "rawValue2", "fmtValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCloseLog(jitter):
    """
    PDH_STATUS PdhCloseLog(
        PDH_HLOG hLog,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCloseQuery(jitter):
    """
    PDH_STATUS PdhCloseQuery(
        PDH_HQUERY hQuery
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCollectQueryData(jitter):
    """
    PDH_STATUS PdhCollectQueryData(
        PDH_HQUERY hQuery
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCollectQueryDataEx(jitter):
    """
    PDH_STATUS PdhCollectQueryDataEx(
        PDH_HQUERY hQuery,
        DWORD dwIntervalTime,
        HANDLE hNewDataEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "dwIntervalTime", "hNewDataEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCollectQueryDataWithTime(jitter):
    """
    PDH_STATUS PdhCollectQueryDataWithTime(
        PDH_HQUERY hQuery,
        LONGLONG* pllTimeStamp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "pllTimeStamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhComputeCounterStatistics(jitter):
    """
    PDH_STATUS PdhComputeCounterStatistics(
        PDH_HCOUNTER hCounter,
        [PdhFormatFlags] dwFormat,
        DWORD dwFirstEntry,
        DWORD dwNumEntries,
        PPDH_RAW_COUNTER lpRawValueArray,
        PPDH_STATISTICS data
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "dwFormat", "dwFirstEntry", "dwNumEntries", "lpRawValueArray", "data"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhConnectMachine(jitter, get_str, set_str):
    """
    PDH_STATUS PdhConnectMachine(
        LPCTSTR szMachineName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szMachineName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhConnectMachineA(jitter):
    pdh_PdhConnectMachine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhConnectMachineW(jitter):
    pdh_PdhConnectMachine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhEnumLogSetNames(jitter, get_str, set_str):
    """
    PDH_STATUS PdhEnumLogSetNames(
        LPCTSTR szDataSource,
        LPTSTR mszLogSetNameList,
        LPDWORD pcchBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "mszLogSetNameList", "pcchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumLogSetNamesA(jitter):
    pdh_PdhEnumLogSetNames(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhEnumLogSetNamesW(jitter):
    pdh_PdhEnumLogSetNames(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhEnumMachines(jitter, get_str, set_str):
    """
    PDH_STATUS PdhEnumMachines(
        LPCTSTR szDataSource,
        LPTSTR mszMachineNameList,
        LPDWORD pcchBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "mszMachineNameList", "pcchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumMachinesA(jitter):
    pdh_PdhEnumMachines(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhEnumMachinesW(jitter):
    pdh_PdhEnumMachines(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhEnumMachinesH(jitter, get_str, set_str):
    """
    PDH_STATUS PdhEnumMachinesH(
        PDH_HLOG hDataSource,
        LPTSTR mszMachineNameList,
        LPDWORD pcchBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "mszMachineNameList", "pcchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumMachinesHA(jitter):
    pdh_PdhEnumMachinesH(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhEnumMachinesHW(jitter):
    pdh_PdhEnumMachinesH(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhEnumObjectItems(jitter, get_str, set_str):
    """
    PDH_STATUS PdhEnumObjectItems(
        LPCTSTR szDataSource,
        LPCTSTR szMachineName,
        LPCTSTR szObjectName,
        LPTSTR mszCounterList,
        LPDWORD pcchCounterListLength,
        LPTSTR mszInstanceList,
        LPDWORD pcchInstanceListLength,
        [PerfDetailLevel] dwDetailLevel,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szMachineName", "szObjectName", "mszCounterList", "pcchCounterListLength", "mszInstanceList", "pcchInstanceListLength", "dwDetailLevel", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumObjectItemsA(jitter):
    pdh_PdhEnumObjectItems(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhEnumObjectItemsW(jitter):
    pdh_PdhEnumObjectItems(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhEnumObjectItemsH(jitter, get_str, set_str):
    """
    PDH_STATUS PdhEnumObjectItemsH(
        PDH_HLOG hDataSource,
        LPCTSTR szMachineName,
        LPCTSTR szObjectName,
        LPTSTR mszCounterList,
        LPDWORD pcchCounterListLength,
        LPTSTR mszInstanceList,
        LPDWORD pcchInstanceListLength,
        [PerfDetailLevel] dwDetailLevel,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szMachineName", "szObjectName", "mszCounterList", "pcchCounterListLength", "mszInstanceList", "pcchInstanceListLength", "dwDetailLevel", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumObjectItemsHA(jitter):
    pdh_PdhEnumObjectItemsH(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhEnumObjectItemsHW(jitter):
    pdh_PdhEnumObjectItemsH(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhEnumObjects(jitter, get_str, set_str):
    """
    PDH_STATUS PdhEnumObjects(
        LPCTSTR szDataSource,
        LPCTSTR szMachineName,
        LPTSTR mszObjectList,
        LPDWORD pcchBufferLength,
        [PerfDetailLevel] dwDetailLevel,
        BOOL bRefresh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szMachineName", "mszObjectList", "pcchBufferLength", "dwDetailLevel", "bRefresh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumObjectsA(jitter):
    pdh_PdhEnumObjects(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhEnumObjectsW(jitter):
    pdh_PdhEnumObjects(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhEnumObjectsH(jitter, get_str, set_str):
    """
    PDH_STATUS PdhEnumObjectsH(
        PDH_HLOG hDataSource,
        LPCTSTR szMachineName,
        LPTSTR mszObjectList,
        LPDWORD pcchBufferLength,
        [PerfDetailLevel] dwDetailLevel,
        BOOL bRefresh
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szMachineName", "mszObjectList", "pcchBufferLength", "dwDetailLevel", "bRefresh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumObjectsHA(jitter):
    pdh_PdhEnumObjectsH(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhEnumObjectsHW(jitter):
    pdh_PdhEnumObjectsH(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhExpandCounterPath(jitter, get_str, set_str):
    """
    PDH_STATUS PdhExpandCounterPath(
        LPCTSTR szWildCardPath,
        LPTSTR mszExpandedPathList,
        LPDWORD pcchPathListLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szWildCardPath", "mszExpandedPathList", "pcchPathListLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhExpandCounterPathA(jitter):
    pdh_PdhExpandCounterPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhExpandCounterPathW(jitter):
    pdh_PdhExpandCounterPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhExpandWildCardPath(jitter, get_str, set_str):
    """
    PDH_STATUS PdhExpandWildCardPath(
        LPCTSTR szDataSource,
        LPCTSTR szWildCardPath,
        LPTSTR mszExpandedPathList,
        LPDWORD pcchPathListLength,
        [PdhExpandFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szWildCardPath", "mszExpandedPathList", "pcchPathListLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhExpandWildCardPathA(jitter):
    pdh_PdhExpandWildCardPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhExpandWildCardPathW(jitter):
    pdh_PdhExpandWildCardPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhExpandWildCardPathH(jitter, get_str, set_str):
    """
    PDH_STATUS PdhExpandWildCardPathH(
        PDH_HLOG hDataSource,
        LPCTSTR szWildCardPath,
        LPTSTR mszExpandedPathList,
        LPDWORD pcchPathListLength,
        [PdhExpandFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szWildCardPath", "mszExpandedPathList", "pcchPathListLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhExpandWildCardPathHA(jitter):
    pdh_PdhExpandWildCardPathH(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhExpandWildCardPathHW(jitter):
    pdh_PdhExpandWildCardPathH(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhFormatFromRawValue(jitter):
    """
    PDH_STATUS PdhFormatFromRawValue(
        DWORD dwCounterType,
        [PdhFormatFlags] dwFormat,
        LONGLONG* pTimeBase,
        PPDH_RAW_COUNTER rawValue1,
        PPDH_RAW_COUNTER rawValue2,
        PPDH_FMT_COUNTERVALUE fmtValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwCounterType", "dwFormat", "pTimeBase", "rawValue1", "rawValue2", "fmtValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetCounterInfo(jitter, get_str, set_str):
    """
    PDH_STATUS PdhGetCounterInfo(
        PDH_HCOUNTER hCounter,
        BOOLEAN bRetrieveExplainText,
        LPDWORD pdwBufferSize,
        PPDH_COUNTER_INFO lpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "bRetrieveExplainText", "pdwBufferSize", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetCounterInfoA(jitter):
    pdh_PdhGetCounterInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhGetCounterInfoW(jitter):
    pdh_PdhGetCounterInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhGetCounterTimeBase(jitter):
    """
    PDH_STATUS PdhGetCounterTimeBase(
        PDH_HCOUNTER hCounter,
        LONGLONG* pTimeBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "pTimeBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDataSourceTimeRange(jitter, get_str, set_str):
    """
    PDH_STATUS PdhGetDataSourceTimeRange(
        LPCTSTR szDataSource,
        LPDWORD pdwNumEntries,
        PPDH_TIME_INFO pInfo,
        LPDWORD pdwBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "pdwNumEntries", "pInfo", "pdwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDataSourceTimeRangeA(jitter):
    pdh_PdhGetDataSourceTimeRange(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhGetDataSourceTimeRangeW(jitter):
    pdh_PdhGetDataSourceTimeRange(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhGetDataSourceTimeRangeH(jitter):
    """
    PDH_STATUS PdhGetDataSourceTimeRangeH(
        PDH_HLOG hDataSource,
        LPDWORD pdwNumEntries,
        PPDH_TIME_INFO pInfo,
        LPDWORD pdwBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "pdwNumEntries", "pInfo", "pdwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfCounter(jitter, get_str, set_str):
    """
    PDH_STATUS PdhGetDefaultPerfCounter(
        LPCTSTR szDataSource,
        LPCTSTR szMachineName,
        LPCTSTR szObjectName,
        LPTSTR szDefaultCounterName,
        LPDWORD pcchBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szMachineName", "szObjectName", "szDefaultCounterName", "pcchBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfCounterA(jitter):
    pdh_PdhGetDefaultPerfCounter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhGetDefaultPerfCounterW(jitter):
    pdh_PdhGetDefaultPerfCounter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhGetDefaultPerfCounterH(jitter, get_str, set_str):
    """
    PDH_STATUS PdhGetDefaultPerfCounterH(
        PDH_HLOG hDataSource,
        LPCTSTR szMachineName,
        LPCTSTR szObjectName,
        LPTSTR szDefaultCounterName,
        LPDWORD pcchBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szMachineName", "szObjectName", "szDefaultCounterName", "pcchBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfCounterHA(jitter):
    pdh_PdhGetDefaultPerfCounterH(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhGetDefaultPerfCounterHW(jitter):
    pdh_PdhGetDefaultPerfCounterH(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhGetDefaultPerfObject(jitter, get_str, set_str):
    """
    PDH_STATUS PdhGetDefaultPerfObject(
        LPCTSTR szDataSource,
        LPCTSTR szMachineName,
        LPTSTR szDefaultObjectName,
        LPDWORD pcchBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szMachineName", "szDefaultObjectName", "pcchBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfObjectA(jitter):
    pdh_PdhGetDefaultPerfObject(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhGetDefaultPerfObjectW(jitter):
    pdh_PdhGetDefaultPerfObject(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhGetDefaultPerfObjectH(jitter, get_str, set_str):
    """
    PDH_STATUS PdhGetDefaultPerfObjectH(
        PDH_HLOG hDataSource,
        LPCTSTR szMachineName,
        LPTSTR szDefaultObjectName,
        LPDWORD pcchBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szMachineName", "szDefaultObjectName", "pcchBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfObjectHA(jitter):
    pdh_PdhGetDefaultPerfObjectH(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhGetDefaultPerfObjectHW(jitter):
    pdh_PdhGetDefaultPerfObjectH(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhGetDllVersion(jitter):
    """
    PDH_STATUS PdhGetDllVersion(
        LPDWORD lpdwVersion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdwVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetFormattedCounterArray(jitter, get_str, set_str):
    """
    PDH_STATUS PdhGetFormattedCounterArray(
        PDH_HCOUNTER hCounter,
        [PdhFormatFlags] dwFormat,
        LPDWORD lpdwBufferSize,
        LPDWORD lpdwBufferCount,
        PPDH_FMT_COUNTERVALUE_ITEM ItemBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "dwFormat", "lpdwBufferSize", "lpdwBufferCount", "ItemBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetFormattedCounterArrayA(jitter):
    pdh_PdhGetFormattedCounterArray(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhGetFormattedCounterArrayW(jitter):
    pdh_PdhGetFormattedCounterArray(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhGetFormattedCounterValue(jitter):
    """
    PDH_STATUS PdhGetFormattedCounterValue(
        PDH_HCOUNTER hCounter,
        [PdhFormatFlags] dwFormat,
        LPDWORD lpdwType,
        PPDH_FMT_COUNTERVALUE pValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "dwFormat", "lpdwType", "pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetLogFileSize(jitter):
    """
    PDH_STATUS PdhGetLogFileSize(
        PDH_HLOG hLog,
        LONGLONG* llSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "llSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetRawCounterArray(jitter, get_str, set_str):
    """
    PDH_STATUS PdhGetRawCounterArray(
        PDH_HCOUNTER hCounter,
        LPDWORD lpdwBufferSize,
        LPDWORD lpdwItemCount,
        PPDH_RAW_COUNTER_ITEM ItemBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "lpdwBufferSize", "lpdwItemCount", "ItemBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetRawCounterArrayA(jitter):
    pdh_PdhGetRawCounterArray(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhGetRawCounterArrayW(jitter):
    pdh_PdhGetRawCounterArray(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhGetRawCounterValue(jitter):
    """
    PDH_STATUS PdhGetRawCounterValue(
        PDH_HCOUNTER hCounter,
        LPDWORD lpdwType,
        PPDH_RAW_COUNTER pValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "lpdwType", "pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhIsRealTimeQuery(jitter):
    """
    BOOL PdhIsRealTimeQuery(
        PDH_HQUERY hQuery
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhLookupPerfIndexByName(jitter, get_str, set_str):
    """
    PDH_STATUS PdhLookupPerfIndexByName(
        LPCTSTR szMachineName,
        LPCTSTR szNameBuffer,
        LPDWORD pdwIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szMachineName", "szNameBuffer", "pdwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhLookupPerfIndexByNameA(jitter):
    pdh_PdhLookupPerfIndexByName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhLookupPerfIndexByNameW(jitter):
    pdh_PdhLookupPerfIndexByName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhLookupPerfNameByIndex(jitter, get_str, set_str):
    """
    PDH_STATUS PdhLookupPerfNameByIndex(
        LPCTSTR szMachineName,
        DWORD dwNameIndex,
        LPTSTR szNameBuffer,
        LPDWORD pcchNameBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szMachineName", "dwNameIndex", "szNameBuffer", "pcchNameBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhLookupPerfNameByIndexA(jitter):
    pdh_PdhLookupPerfNameByIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhLookupPerfNameByIndexW(jitter):
    pdh_PdhLookupPerfNameByIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhMakeCounterPath(jitter, get_str, set_str):
    """
    PDH_STATUS PdhMakeCounterPath(
        PDH_COUNTER_PATH_ELEMENTS* pCounterPathElements,
        LPTSTR szFullPathBuffer,
        LPDWORD pcchBufferSize,
        [PdhPathFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCounterPathElements", "szFullPathBuffer", "pcchBufferSize", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhMakeCounterPathA(jitter):
    pdh_PdhMakeCounterPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhMakeCounterPathW(jitter):
    pdh_PdhMakeCounterPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhOpenLog(jitter, get_str, set_str):
    """
    PDH_STATUS PdhOpenLog(
        LPCTSTR szLogFileName,
        [PdhOpenLogFlags] dwAccessFlags,
        [PDH_LOG_TYPE*] lpdwLogType,
        PDH_HQUERY hQuery,
        DWORD dwMaxSize,
        LPCTSTR szUserCaption,
        PDH_HLOG* phLog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szLogFileName", "dwAccessFlags", "lpdwLogType", "hQuery", "dwMaxSize", "szUserCaption", "phLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhOpenLogA(jitter):
    pdh_PdhOpenLog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhOpenLogW(jitter):
    pdh_PdhOpenLog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhOpenQuery(jitter, get_str, set_str):
    """
    PDH_STATUS PdhOpenQuery(
        LPCTSTR szDataSource,
        DWORD_PTR dwUserData,
        PDH_HQUERY* phQuery
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "dwUserData", "phQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhOpenQueryA(jitter):
    pdh_PdhOpenQuery(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhOpenQueryW(jitter):
    pdh_PdhOpenQuery(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhOpenQueryH(jitter):
    """
    PDH_STATUS PdhOpenQueryH(
        PDH_HLOG hDataSource,
        DWORD_PTR dwUserData,
        PDH_HQUERY* phQuery
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "dwUserData", "phQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhParseCounterPath(jitter, get_str, set_str):
    """
    PDH_STATUS PdhParseCounterPath(
        LPCTSTR szFullPathBuffer,
        PDH_COUNTER_PATH_ELEMENTS* pCounterPathElements,
        LPDWORD pdwBufferSize,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFullPathBuffer", "pCounterPathElements", "pdwBufferSize", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhParseCounterPathA(jitter):
    pdh_PdhParseCounterPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhParseCounterPathW(jitter):
    pdh_PdhParseCounterPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhParseInstanceName(jitter, get_str, set_str):
    """
    PDH_STATUS PdhParseInstanceName(
        LPCTSTR szInstanceString,
        LPTSTR szInstanceName,
        LPDWORD pcchInstanceNameLength,
        LPTSTR szParentName,
        LPDWORD pcchParentNameLength,
        LPDWORD lpIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szInstanceString", "szInstanceName", "pcchInstanceNameLength", "szParentName", "pcchParentNameLength", "lpIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhParseInstanceNameA(jitter):
    pdh_PdhParseInstanceName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhParseInstanceNameW(jitter):
    pdh_PdhParseInstanceName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhReadRawLogRecord(jitter):
    """
    PDH_STATUS PdhReadRawLogRecord(
        PDH_HLOG hLog,
        FILETIME ftRecord,
        PPDH_RAW_LOG_RECORD pRawLogRecord,
        LPDWORD pdwBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "ftRecord", "pRawLogRecord", "pdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhRemoveCounter(jitter):
    """
    PDH_STATUS PdhRemoveCounter(
        PDH_HCOUNTER hCounter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhSelectDataSource(jitter, get_str, set_str):
    """
    PDH_STATUS PdhSelectDataSource(
        HWND hWndOwner,
        DWORD dwFlags,
        LPTSTR szDataSource,
        LPDWORD pcchBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndOwner", "dwFlags", "szDataSource", "pcchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhSelectDataSourceA(jitter):
    pdh_PdhSelectDataSource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhSelectDataSourceW(jitter):
    pdh_PdhSelectDataSource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhSetCounterScaleFactor(jitter):
    """
    PDH_STATUS PdhSetCounterScaleFactor(
        PDH_HCOUNTER hCounter,
        LONG lFactor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "lFactor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhSetDefaultRealTimeDataSource(jitter):
    """
    PDH_STATUS PdhSetDefaultRealTimeDataSource(
        DWORD dwDataSourceId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDataSourceId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhSetQueryTimeRange(jitter):
    """
    PDH_STATUS PdhSetQueryTimeRange(
        PDH_HQUERY hQuery,
        PPDH_TIME_INFO pInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhUpdateLog(jitter, get_str, set_str):
    """
    PDH_STATUS PdhUpdateLog(
        PDH_HLOG hLog,
        LPCTSTR szUserString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "szUserString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhUpdateLogA(jitter):
    pdh_PdhUpdateLog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhUpdateLogW(jitter):
    pdh_PdhUpdateLog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhUpdateLogFileCatalog(jitter):
    """
    PDH_STATUS PdhUpdateLogFileCatalog(
        PDH_HLOG hLog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhValidatePath(jitter, get_str, set_str):
    """
    PDH_STATUS PdhValidatePath(
        LPCTSTR szFullCounterPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFullCounterPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhValidatePathA(jitter):
    pdh_PdhValidatePath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhValidatePathW(jitter):
    pdh_PdhValidatePath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def pdh_PdhValidatePathEx(jitter, get_str, set_str):
    """
    PDH_STATUS PdhValidatePathEx(
        PDH_HLOG hDataSource,
        LPCTSTR szFullPathBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szFullPathBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhValidatePathExA(jitter):
    pdh_PdhValidatePathEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def pdh_PdhValidatePathExW(jitter):
    pdh_PdhValidatePathEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
