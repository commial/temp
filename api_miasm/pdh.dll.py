
def pdh_PdhAddCounter(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhAddCounter(PDH_HQUERY hQuery, LPCTSTR szFullCounterPath, DWORD_PTR dwUserData, PDH_HCOUNTER* phCounter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "szFullCounterPath", "dwUserData", "phCounter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhAddEnglishCounter(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhAddEnglishCounter(PDH_HQUERY hQuery, LPCTSTR szFullCounterPath, DWORD_PTR dwUserData, PDH_HCOUNTER* phCounter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "szFullCounterPath", "dwUserData", "phCounter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhBindInputDataSource(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhBindInputDataSource(PDH_HLOG* phDataSource, LPCTSTR szLogFileNameList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phDataSource", "szLogFileNameList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhBrowseCounters(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhBrowseCounters(PPDH_BROWSE_DLG_CONFIG pBrowseDlgData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBrowseDlgData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhBrowseCountersH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhBrowseCountersH(PPDH_BROWSE_DLG_CONFIG pBrowseDlgData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBrowseDlgData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCalculateCounterFromRawValue(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhCalculateCounterFromRawValue(PDH_HCOUNTER hCounter, [PdhFormatFlags] dwFormat, PPDH_RAW_COUNTER rawValue1, PPDH_RAW_COUNTER rawValue2, PPDH_FMT_COUNTERVALUE fmtValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "dwFormat", "rawValue1", "rawValue2", "fmtValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCloseLog(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhCloseLog(PDH_HLOG hLog, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCloseQuery(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhCloseQuery(PDH_HQUERY hQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCollectQueryData(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhCollectQueryData(PDH_HQUERY hQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCollectQueryDataEx(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhCollectQueryDataEx(PDH_HQUERY hQuery, DWORD dwIntervalTime, HANDLE hNewDataEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "dwIntervalTime", "hNewDataEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhCollectQueryDataWithTime(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhCollectQueryDataWithTime(PDH_HQUERY hQuery, LONGLONG* pllTimeStamp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "pllTimeStamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhComputeCounterStatistics(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhComputeCounterStatistics(PDH_HCOUNTER hCounter, [PdhFormatFlags] dwFormat, DWORD dwFirstEntry, DWORD dwNumEntries, PPDH_RAW_COUNTER lpRawValueArray, PPDH_STATISTICS data)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "dwFormat", "dwFirstEntry", "dwNumEntries", "lpRawValueArray", "data"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhConnectMachine(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhConnectMachine(LPCTSTR szMachineName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szMachineName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumLogSetNames(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhEnumLogSetNames(LPCTSTR szDataSource, LPTSTR mszLogSetNameList, LPDWORD pcchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "mszLogSetNameList", "pcchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumMachines(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhEnumMachines(LPCTSTR szDataSource, LPTSTR mszMachineNameList, LPDWORD pcchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "mszMachineNameList", "pcchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumMachinesH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhEnumMachinesH(PDH_HLOG hDataSource, LPTSTR mszMachineNameList, LPDWORD pcchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "mszMachineNameList", "pcchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumObjectItems(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhEnumObjectItems(LPCTSTR szDataSource, LPCTSTR szMachineName, LPCTSTR szObjectName, LPTSTR mszCounterList, LPDWORD pcchCounterListLength, LPTSTR mszInstanceList, LPDWORD pcchInstanceListLength, [PerfDetailLevel] dwDetailLevel, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szMachineName", "szObjectName", "mszCounterList", "pcchCounterListLength", "mszInstanceList", "pcchInstanceListLength", "dwDetailLevel", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumObjectItemsH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhEnumObjectItemsH(PDH_HLOG hDataSource, LPCTSTR szMachineName, LPCTSTR szObjectName, LPTSTR mszCounterList, LPDWORD pcchCounterListLength, LPTSTR mszInstanceList, LPDWORD pcchInstanceListLength, [PerfDetailLevel] dwDetailLevel, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szMachineName", "szObjectName", "mszCounterList", "pcchCounterListLength", "mszInstanceList", "pcchInstanceListLength", "dwDetailLevel", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumObjects(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhEnumObjects(LPCTSTR szDataSource, LPCTSTR szMachineName, LPTSTR mszObjectList, LPDWORD pcchBufferLength, [PerfDetailLevel] dwDetailLevel, BOOL bRefresh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szMachineName", "mszObjectList", "pcchBufferLength", "dwDetailLevel", "bRefresh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhEnumObjectsH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhEnumObjectsH(PDH_HLOG hDataSource, LPCTSTR szMachineName, LPTSTR mszObjectList, LPDWORD pcchBufferLength, [PerfDetailLevel] dwDetailLevel, BOOL bRefresh)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szMachineName", "mszObjectList", "pcchBufferLength", "dwDetailLevel", "bRefresh"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhExpandCounterPath(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhExpandCounterPath(LPCTSTR szWildCardPath, LPTSTR mszExpandedPathList, LPDWORD pcchPathListLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szWildCardPath", "mszExpandedPathList", "pcchPathListLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhExpandWildCardPath(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhExpandWildCardPath(LPCTSTR szDataSource, LPCTSTR szWildCardPath, LPTSTR mszExpandedPathList, LPDWORD pcchPathListLength, [PdhExpandFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szWildCardPath", "mszExpandedPathList", "pcchPathListLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhExpandWildCardPathH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhExpandWildCardPathH(PDH_HLOG hDataSource, LPCTSTR szWildCardPath, LPTSTR mszExpandedPathList, LPDWORD pcchPathListLength, [PdhExpandFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szWildCardPath", "mszExpandedPathList", "pcchPathListLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhFormatFromRawValue(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhFormatFromRawValue(DWORD dwCounterType, [PdhFormatFlags] dwFormat, LONGLONG* pTimeBase, PPDH_RAW_COUNTER rawValue1, PPDH_RAW_COUNTER rawValue2, PPDH_FMT_COUNTERVALUE fmtValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwCounterType", "dwFormat", "pTimeBase", "rawValue1", "rawValue2", "fmtValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetCounterInfo(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetCounterInfo(PDH_HCOUNTER hCounter, BOOLEAN bRetrieveExplainText, LPDWORD pdwBufferSize, PPDH_COUNTER_INFO lpBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "bRetrieveExplainText", "pdwBufferSize", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetCounterTimeBase(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetCounterTimeBase(PDH_HCOUNTER hCounter, LONGLONG* pTimeBase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "pTimeBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDataSourceTimeRange(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetDataSourceTimeRange(LPCTSTR szDataSource, LPDWORD pdwNumEntries, PPDH_TIME_INFO pInfo, LPDWORD pdwBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "pdwNumEntries", "pInfo", "pdwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDataSourceTimeRangeH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetDataSourceTimeRangeH(PDH_HLOG hDataSource, LPDWORD pdwNumEntries, PPDH_TIME_INFO pInfo, LPDWORD pdwBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "pdwNumEntries", "pInfo", "pdwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfCounter(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetDefaultPerfCounter(LPCTSTR szDataSource, LPCTSTR szMachineName, LPCTSTR szObjectName, LPTSTR szDefaultCounterName, LPDWORD pcchBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szMachineName", "szObjectName", "szDefaultCounterName", "pcchBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfCounterH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetDefaultPerfCounterH(PDH_HLOG hDataSource, LPCTSTR szMachineName, LPCTSTR szObjectName, LPTSTR szDefaultCounterName, LPDWORD pcchBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szMachineName", "szObjectName", "szDefaultCounterName", "pcchBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfObject(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetDefaultPerfObject(LPCTSTR szDataSource, LPCTSTR szMachineName, LPTSTR szDefaultObjectName, LPDWORD pcchBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "szMachineName", "szDefaultObjectName", "pcchBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDefaultPerfObjectH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetDefaultPerfObjectH(PDH_HLOG hDataSource, LPCTSTR szMachineName, LPTSTR szDefaultObjectName, LPDWORD pcchBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szMachineName", "szDefaultObjectName", "pcchBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetDllVersion(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetDllVersion(LPDWORD lpdwVersion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpdwVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetFormattedCounterArray(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetFormattedCounterArray(PDH_HCOUNTER hCounter, [PdhFormatFlags] dwFormat, LPDWORD lpdwBufferSize, LPDWORD lpdwBufferCount, PPDH_FMT_COUNTERVALUE_ITEM ItemBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "dwFormat", "lpdwBufferSize", "lpdwBufferCount", "ItemBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetFormattedCounterValue(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetFormattedCounterValue(PDH_HCOUNTER hCounter, [PdhFormatFlags] dwFormat, LPDWORD lpdwType, PPDH_FMT_COUNTERVALUE pValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "dwFormat", "lpdwType", "pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetLogFileSize(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetLogFileSize(PDH_HLOG hLog, LONGLONG* llSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "llSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetRawCounterArray(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetRawCounterArray(PDH_HCOUNTER hCounter, LPDWORD lpdwBufferSize, LPDWORD lpdwItemCount, PPDH_RAW_COUNTER_ITEM ItemBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "lpdwBufferSize", "lpdwItemCount", "ItemBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhGetRawCounterValue(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhGetRawCounterValue(PDH_HCOUNTER hCounter, LPDWORD lpdwType, PPDH_RAW_COUNTER pValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "lpdwType", "pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhIsRealTimeQuery(jitter):
    """"
    [Pdh.dll] BOOL PdhIsRealTimeQuery(PDH_HQUERY hQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhLookupPerfIndexByName(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhLookupPerfIndexByName(LPCTSTR szMachineName, LPCTSTR szNameBuffer, LPDWORD pdwIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szMachineName", "szNameBuffer", "pdwIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhLookupPerfNameByIndex(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhLookupPerfNameByIndex(LPCTSTR szMachineName, DWORD dwNameIndex, LPTSTR szNameBuffer, LPDWORD pcchNameBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szMachineName", "dwNameIndex", "szNameBuffer", "pcchNameBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhMakeCounterPath(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhMakeCounterPath(PDH_COUNTER_PATH_ELEMENTS* pCounterPathElements, LPTSTR szFullPathBuffer, LPDWORD pcchBufferSize, [PdhPathFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCounterPathElements", "szFullPathBuffer", "pcchBufferSize", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhOpenLog(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhOpenLog(LPCTSTR szLogFileName, [PdhOpenLogFlags] dwAccessFlags, [PDH_LOG_TYPE*] lpdwLogType, PDH_HQUERY hQuery, DWORD dwMaxSize, LPCTSTR szUserCaption, PDH_HLOG* phLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szLogFileName", "dwAccessFlags", "lpdwLogType", "hQuery", "dwMaxSize", "szUserCaption", "phLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhOpenQuery(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhOpenQuery(LPCTSTR szDataSource, DWORD_PTR dwUserData, PDH_HQUERY* phQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szDataSource", "dwUserData", "phQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhOpenQueryH(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhOpenQueryH(PDH_HLOG hDataSource, DWORD_PTR dwUserData, PDH_HQUERY* phQuery)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "dwUserData", "phQuery"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhParseCounterPath(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhParseCounterPath(LPCTSTR szFullPathBuffer, PDH_COUNTER_PATH_ELEMENTS* pCounterPathElements, LPDWORD pdwBufferSize, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szFullPathBuffer", "pCounterPathElements", "pdwBufferSize", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhParseInstanceName(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhParseInstanceName(LPCTSTR szInstanceString, LPTSTR szInstanceName, LPDWORD pcchInstanceNameLength, LPTSTR szParentName, LPDWORD pcchParentNameLength, LPDWORD lpIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szInstanceString", "szInstanceName", "pcchInstanceNameLength", "szParentName", "pcchParentNameLength", "lpIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhReadRawLogRecord(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhReadRawLogRecord(PDH_HLOG hLog, FILETIME ftRecord, PPDH_RAW_LOG_RECORD pRawLogRecord, LPDWORD pdwBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "ftRecord", "pRawLogRecord", "pdwBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhRemoveCounter(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhRemoveCounter(PDH_HCOUNTER hCounter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhSelectDataSource(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhSelectDataSource(HWND hWndOwner, DWORD dwFlags, LPTSTR szDataSource, LPDWORD pcchBufferLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWndOwner", "dwFlags", "szDataSource", "pcchBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhSetCounterScaleFactor(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhSetCounterScaleFactor(PDH_HCOUNTER hCounter, LONG lFactor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCounter", "lFactor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhSetDefaultRealTimeDataSource(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhSetDefaultRealTimeDataSource(DWORD dwDataSourceId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwDataSourceId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhSetQueryTimeRange(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhSetQueryTimeRange(PDH_HQUERY hQuery, PPDH_TIME_INFO pInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hQuery", "pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhUpdateLog(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhUpdateLog(PDH_HLOG hLog, LPCTSTR szUserString)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "szUserString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhUpdateLogFileCatalog(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhUpdateLogFileCatalog(PDH_HLOG hLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhValidatePath(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhValidatePath(LPCTSTR szFullCounterPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["szFullCounterPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def pdh_PdhValidatePathEx(jitter):
    """"
    [Pdh.dll] PDH_STATUS PdhValidatePathEx(PDH_HLOG hDataSource, LPCTSTR szFullPathBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDataSource", "szFullPathBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
