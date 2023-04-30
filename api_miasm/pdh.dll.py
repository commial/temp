PDH_STATUS = {
    "PDH_CSTATUS_NO_MACHINE": 0x800007D0,
    "PDH_CSTATUS_NO_INSTANCE": 0x800007D1,
    "PDH_MORE_DATA": 0x800007D2,
    "PDH_CSTATUS_ITEM_NOT_VALIDATED": 0x800007D3,
    "PDH_RETRY": 0x800007D4,
    "PDH_NO_DATA": 0x800007D5,
    "PDH_CALC_NEGATIVE_DENOMINATOR": 0x800007D6,
    "PDH_CALC_NEGATIVE_TIMEBASE": 0x800007D7,
    "PDH_CALC_NEGATIVE_VALUE": 0x800007D8,
    "PDH_DIALOG_CANCELLED": 0x800007D9,
    "PDH_END_OF_LOG_FILE": 0x800007DA,
    "PDH_ASYNC_QUERY_TIMEOUT": 0x800007DB,
    "PDH_CANNOT_SET_DEFAULT_REALTIME_DATASOURCE": 0x800007DC,
    "PDH_UNABLE_MAP_NAME_FILES": 0x80000BD5,
    "PDH_PLA_VALIDATION_WARNING": 0x80000BF3,
    "PDH_CSTATUS_NO_OBJECT": 0xC0000BB8,
    "PDH_CSTATUS_NO_COUNTER": 0xC0000BB9,
    "PDH_CSTATUS_INVALID_DATA": 0xC0000BBA,
    "PDH_MEMORY_ALLOCATION_FAILURE": 0xC0000BBB,
    "PDH_INVALID_HANDLE": 0xC0000BBC,
    "PDH_INVALID_ARGUMENT": 0xC0000BBD,
    "PDH_FUNCTION_NOT_FOUND": 0xC0000BBE,
    "PDH_CSTATUS_NO_COUNTERNAME": 0xC0000BBF,
    "PDH_CSTATUS_BAD_COUNTERNAME": 0xC0000BC0,
    "PDH_INVALID_BUFFER": 0xC0000BC1,
    "PDH_INSUFFICIENT_BUFFER": 0xC0000BC2,
    "PDH_CANNOT_CONNECT_MACHINE": 0xC0000BC3,
    "PDH_INVALID_PATH": 0xC0000BC4,
    "PDH_INVALID_INSTANCE": 0xC0000BC5,
    "PDH_INVALID_DATA": 0xC0000BC6,
    "PDH_NO_DIALOG_DATA": 0xC0000BC7,
    "PDH_CANNOT_READ_NAME_STRINGS": 0xC0000BC8,
    "PDH_LOG_FILE_CREATE_ERROR": 0xC0000BC9,
    "PDH_LOG_FILE_OPEN_ERROR": 0xC0000BCA,
    "PDH_LOG_TYPE_NOT_FOUND": 0xC0000BCB,
    "PDH_NO_MORE_DATA": 0xC0000BCC,
    "PDH_ENTRY_NOT_IN_LOG_FILE": 0xC0000BCD,
    "PDH_DATA_SOURCE_IS_LOG_FILE": 0xC0000BCE,
    "PDH_DATA_SOURCE_IS_REAL_TIME": 0xC0000BCF,
    "PDH_UNABLE_READ_LOG_HEADER": 0xC0000BD0,
    "PDH_FILE_NOT_FOUND": 0xC0000BD1,
    "PDH_FILE_ALREADY_EXISTS": 0xC0000BD2,
    "PDH_NOT_IMPLEMENTED": 0xC0000BD3,
    "PDH_STRING_NOT_FOUND": 0xC0000BD4,
    "PDH_UNKNOWN_LOG_FORMAT": 0xC0000BD6,
    "PDH_UNKNOWN_LOGSVC_COMMAND": 0xC0000BD7,
    "PDH_LOGSVC_QUERY_NOT_FOUND": 0xC0000BD8,
    "PDH_LOGSVC_NOT_OPENED": 0xC0000BD9,
    "PDH_WBEM_ERROR": 0xC0000BDA,
    "PDH_ACCESS_DENIED": 0xC0000BDB,
    "PDH_LOG_FILE_TOO_SMALL": 0xC0000BDC,
    "PDH_INVALID_DATASOURCE": 0xC0000BDD,
    "PDH_INVALID_SQLDB": 0xC0000BDE,
    "PDH_NO_COUNTERS": 0xC0000BDF,
    "PDH_SQL_ALLOC_FAILED": 0xC0000BE0,
    "PDH_SQL_ALLOCCON_FAILED": 0xC0000BE1,
    "PDH_SQL_EXEC_DIRECT_FAILED": 0xC0000BE2,
    "PDH_SQL_FETCH_FAILED": 0xC0000BE3,
    "PDH_SQL_ROWCOUNT_FAILED": 0xC0000BE4,
    "PDH_SQL_MORE_RESULTS_FAILED": 0xC0000BE5,
    "PDH_SQL_CONNECT_FAILED": 0xC0000BE6,
    "PDH_SQL_BIND_FAILED": 0xC0000BE7,
    "PDH_CANNOT_CONNECT_WMI_SERVER": 0xC0000BE8,
    "PDH_PLA_COLLECTION_ALREADY_RUNNING": 0xC0000BE9,
    "PDH_PLA_ERROR_SCHEDULE_OVERLAP": 0xC0000BEA,
    "PDH_PLA_COLLECTION_NOT_FOUND": 0xC0000BEB,
    "PDH_PLA_ERROR_SCHEDULE_ELAPSED": 0xC0000BEC,
    "PDH_PLA_ERROR_NOSTART": 0xC0000BED,
    "PDH_PLA_ERROR_ALREADY_EXISTS": 0xC0000BEE,
    "PDH_PLA_ERROR_TYPE_MISMATCH": 0xC0000BEF,
    "PDH_PLA_ERROR_FILEPATH": 0xC0000BF0,
    "PDH_PLA_SERVICE_ERROR": 0xC0000BF1,
    "PDH_PLA_VALIDATION_ERROR": 0xC0000BF2,
    "PDH_PLA_ERROR_NAME_TOO_LONG": 0xC0000BF4,
    "PDH_INVALID_SQL_LOG_FORMAT": 0xC0000BF5,
    "PDH_COUNTER_ALREADY_IN_QUERY": 0xC0000BF6,
    "PDH_BINARY_LOG_CORRUPT": 0xC0000BF7,
    "PDH_LOG_SAMPLE_TOO_SMALL": 0xC0000BF8,
    "PDH_OS_LATER_VERSION": 0xC0000BF9,
    "PDH_OS_EARLIER_VERSION": 0xC0000BFA,
    "PDH_INCORRECT_APPEND_TIME": 0xC0000BFB,
    "PDH_UNMATCHED_APPEND_COUNTER": 0xC0000BFC,
    "PDH_SQL_ALTER_DETAIL_FAILED": 0xC0000BFD,
    "PDH_QUERY_PERF_DATA_TIMEOUT": 0xC0000BFE,
}
PDH_STATUS_INV = {
    0x800007D0: "PDH_CSTATUS_NO_MACHINE",
    0x800007D1: "PDH_CSTATUS_NO_INSTANCE",
    0x800007D2: "PDH_MORE_DATA",
    0x800007D3: "PDH_CSTATUS_ITEM_NOT_VALIDATED",
    0x800007D4: "PDH_RETRY",
    0x800007D5: "PDH_NO_DATA",
    0x800007D6: "PDH_CALC_NEGATIVE_DENOMINATOR",
    0x800007D7: "PDH_CALC_NEGATIVE_TIMEBASE",
    0x800007D8: "PDH_CALC_NEGATIVE_VALUE",
    0x800007D9: "PDH_DIALOG_CANCELLED",
    0x800007DA: "PDH_END_OF_LOG_FILE",
    0x800007DB: "PDH_ASYNC_QUERY_TIMEOUT",
    0x800007DC: "PDH_CANNOT_SET_DEFAULT_REALTIME_DATASOURCE",
    0x80000BD5: "PDH_UNABLE_MAP_NAME_FILES",
    0x80000BF3: "PDH_PLA_VALIDATION_WARNING",
    0xC0000BB8: "PDH_CSTATUS_NO_OBJECT",
    0xC0000BB9: "PDH_CSTATUS_NO_COUNTER",
    0xC0000BBA: "PDH_CSTATUS_INVALID_DATA",
    0xC0000BBB: "PDH_MEMORY_ALLOCATION_FAILURE",
    0xC0000BBC: "PDH_INVALID_HANDLE",
    0xC0000BBD: "PDH_INVALID_ARGUMENT",
    0xC0000BBE: "PDH_FUNCTION_NOT_FOUND",
    0xC0000BBF: "PDH_CSTATUS_NO_COUNTERNAME",
    0xC0000BC0: "PDH_CSTATUS_BAD_COUNTERNAME",
    0xC0000BC1: "PDH_INVALID_BUFFER",
    0xC0000BC2: "PDH_INSUFFICIENT_BUFFER",
    0xC0000BC3: "PDH_CANNOT_CONNECT_MACHINE",
    0xC0000BC4: "PDH_INVALID_PATH",
    0xC0000BC5: "PDH_INVALID_INSTANCE",
    0xC0000BC6: "PDH_INVALID_DATA",
    0xC0000BC7: "PDH_NO_DIALOG_DATA",
    0xC0000BC8: "PDH_CANNOT_READ_NAME_STRINGS",
    0xC0000BC9: "PDH_LOG_FILE_CREATE_ERROR",
    0xC0000BCA: "PDH_LOG_FILE_OPEN_ERROR",
    0xC0000BCB: "PDH_LOG_TYPE_NOT_FOUND",
    0xC0000BCC: "PDH_NO_MORE_DATA",
    0xC0000BCD: "PDH_ENTRY_NOT_IN_LOG_FILE",
    0xC0000BCE: "PDH_DATA_SOURCE_IS_LOG_FILE",
    0xC0000BCF: "PDH_DATA_SOURCE_IS_REAL_TIME",
    0xC0000BD0: "PDH_UNABLE_READ_LOG_HEADER",
    0xC0000BD1: "PDH_FILE_NOT_FOUND",
    0xC0000BD2: "PDH_FILE_ALREADY_EXISTS",
    0xC0000BD3: "PDH_NOT_IMPLEMENTED",
    0xC0000BD4: "PDH_STRING_NOT_FOUND",
    0xC0000BD6: "PDH_UNKNOWN_LOG_FORMAT",
    0xC0000BD7: "PDH_UNKNOWN_LOGSVC_COMMAND",
    0xC0000BD8: "PDH_LOGSVC_QUERY_NOT_FOUND",
    0xC0000BD9: "PDH_LOGSVC_NOT_OPENED",
    0xC0000BDA: "PDH_WBEM_ERROR",
    0xC0000BDB: "PDH_ACCESS_DENIED",
    0xC0000BDC: "PDH_LOG_FILE_TOO_SMALL",
    0xC0000BDD: "PDH_INVALID_DATASOURCE",
    0xC0000BDE: "PDH_INVALID_SQLDB",
    0xC0000BDF: "PDH_NO_COUNTERS",
    0xC0000BE0: "PDH_SQL_ALLOC_FAILED",
    0xC0000BE1: "PDH_SQL_ALLOCCON_FAILED",
    0xC0000BE2: "PDH_SQL_EXEC_DIRECT_FAILED",
    0xC0000BE3: "PDH_SQL_FETCH_FAILED",
    0xC0000BE4: "PDH_SQL_ROWCOUNT_FAILED",
    0xC0000BE5: "PDH_SQL_MORE_RESULTS_FAILED",
    0xC0000BE6: "PDH_SQL_CONNECT_FAILED",
    0xC0000BE7: "PDH_SQL_BIND_FAILED",
    0xC0000BE8: "PDH_CANNOT_CONNECT_WMI_SERVER",
    0xC0000BE9: "PDH_PLA_COLLECTION_ALREADY_RUNNING",
    0xC0000BEA: "PDH_PLA_ERROR_SCHEDULE_OVERLAP",
    0xC0000BEB: "PDH_PLA_COLLECTION_NOT_FOUND",
    0xC0000BEC: "PDH_PLA_ERROR_SCHEDULE_ELAPSED",
    0xC0000BED: "PDH_PLA_ERROR_NOSTART",
    0xC0000BEE: "PDH_PLA_ERROR_ALREADY_EXISTS",
    0xC0000BEF: "PDH_PLA_ERROR_TYPE_MISMATCH",
    0xC0000BF0: "PDH_PLA_ERROR_FILEPATH",
    0xC0000BF1: "PDH_PLA_SERVICE_ERROR",
    0xC0000BF2: "PDH_PLA_VALIDATION_ERROR",
    0xC0000BF4: "PDH_PLA_ERROR_NAME_TOO_LONG",
    0xC0000BF5: "PDH_INVALID_SQL_LOG_FORMAT",
    0xC0000BF6: "PDH_COUNTER_ALREADY_IN_QUERY",
    0xC0000BF7: "PDH_BINARY_LOG_CORRUPT",
    0xC0000BF8: "PDH_LOG_SAMPLE_TOO_SMALL",
    0xC0000BF9: "PDH_OS_LATER_VERSION",
    0xC0000BFA: "PDH_OS_EARLIER_VERSION",
    0xC0000BFB: "PDH_INCORRECT_APPEND_TIME",
    0xC0000BFC: "PDH_UNMATCHED_APPEND_COUNTER",
    0xC0000BFD: "PDH_SQL_ALTER_DETAIL_FAILED",
    0xC0000BFE: "PDH_QUERY_PERF_DATA_TIMEOUT",
}
_PDH_CSTATUS_ = {
    "PDH_CSTATUS_VALID_DATA": 0x0,
    "PDH_CSTATUS_NEW_DATA": 0x1,
    "PDH_CSTATUS_NO_MACHINE": 0x800007D0,
    "PDH_CSTATUS_NO_INSTANCE": 0x800007D1,
    "PDH_CSTATUS_ITEM_NOT_VALIDATED": 0x800007D3,
    "PDH_CSTATUS_NO_OBJECT": 0xC0000BB8,
    "PDH_CSTATUS_NO_COUNTER": 0xC0000BB9,
    "PDH_CSTATUS_INVALID_DATA": 0xC0000BBA,
    "PDH_CSTATUS_NO_COUNTERNAME": 0xC0000BBF,
    "PDH_CSTATUS_BAD_COUNTERNAME": 0xC0000BC0,
}
_PDH_CSTATUS__INV = {
    0x0: "PDH_CSTATUS_VALID_DATA",
    0x1: "PDH_CSTATUS_NEW_DATA",
    0x800007D0: "PDH_CSTATUS_NO_MACHINE",
    0x800007D1: "PDH_CSTATUS_NO_INSTANCE",
    0x800007D3: "PDH_CSTATUS_ITEM_NOT_VALIDATED",
    0xC0000BB8: "PDH_CSTATUS_NO_OBJECT",
    0xC0000BB9: "PDH_CSTATUS_NO_COUNTER",
    0xC0000BBA: "PDH_CSTATUS_INVALID_DATA",
    0xC0000BBF: "PDH_CSTATUS_NO_COUNTERNAME",
    0xC0000BC0: "PDH_CSTATUS_BAD_COUNTERNAME",
}
_PDH_LOG_TYPE_ = {
    "PDH_LOG_TYPE_UNDEFINED": 0,
    "PDH_LOG_TYPE_CSV": 1,
    "PDH_LOG_TYPE_TSV": 2,
    "PDH_LOG_TYPE_TRACE_KERNEL": 4,
    "PDH_LOG_TYPE_TRACE_GENERIC": 5,
    "PDH_LOG_TYPE_PERFMON": 6,
    "PDH_LOG_TYPE_SQL": 7,
    "PDH_LOG_TYPE_BINARY": 8,
}
_PDH_LOG_TYPE__INV = {
    0: "PDH_LOG_TYPE_UNDEFINED",
    1: "PDH_LOG_TYPE_CSV",
    2: "PDH_LOG_TYPE_TSV",
    4: "PDH_LOG_TYPE_TRACE_KERNEL",
    5: "PDH_LOG_TYPE_TRACE_GENERIC",
    6: "PDH_LOG_TYPE_PERFMON",
    7: "PDH_LOG_TYPE_SQL",
    8: "PDH_LOG_TYPE_BINARY",
}
_PerfDetailLevel_ = {
    "PERF_DETAIL_NOVICE": 100,
    "PERF_DETAIL_ADVANCED": 200,
    "PERF_DETAIL_EXPERT": 300,
    "PERF_DETAIL_WIZARD": 400,
}
_PerfDetailLevel__INV = {
    100: "PERF_DETAIL_NOVICE",
    200: "PERF_DETAIL_ADVANCED",
    300: "PERF_DETAIL_EXPERT",
    400: "PERF_DETAIL_WIZARD",
}

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
