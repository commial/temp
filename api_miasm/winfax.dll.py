
def winfax_FaxOpenPort(jitter):
    """
    BOOL FaxOpenPort(
        HANDLE FaxHandle,
        DWORD DeviceId,
        DWORD Flags,
        LPHANDLE FaxPortHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "DeviceId", "Flags", "FaxPortHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetConfiguration(jitter, get_str, set_str):
    """
    BOOL FaxGetConfiguration(
        HANDLE FaxHandle,
        PFAX_CONFIGURATION* FaxConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FaxConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetConfigurationA(jitter):
    winfax_FaxGetConfiguration(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxGetConfigurationW(jitter):
    winfax_FaxGetConfiguration(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxSetConfiguration(jitter, get_str, set_str):
    """
    BOOL FaxSetConfiguration(
        HANDLE FaxHandle,
        const FAX_CONFIGURATION* FaxConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FaxConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetConfigurationA(jitter):
    winfax_FaxSetConfiguration(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxSetConfigurationW(jitter):
    winfax_FaxSetConfiguration(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxSetGlobalRoutingInfo(jitter, get_str, set_str):
    """
    BOOL FaxSetGlobalRoutingInfo(
        HANDLE FaxHandle,
        const FAX_GLOBAL_ROUTING_INFO* RoutingInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "RoutingInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetGlobalRoutingInfoA(jitter):
    winfax_FaxSetGlobalRoutingInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxSetGlobalRoutingInfoW(jitter):
    winfax_FaxSetGlobalRoutingInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxSetLoggingCategories(jitter, get_str, set_str):
    """
    BOOL FaxSetLoggingCategories(
        HANDLE FaxHandle,
        const FAX_LOG_CATEGORY* Categories,
        DWORD NumberCategories
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "Categories", "NumberCategories"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetLoggingCategoriesA(jitter):
    winfax_FaxSetLoggingCategories(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxSetLoggingCategoriesW(jitter):
    winfax_FaxSetLoggingCategories(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxGetDeviceStatus(jitter, get_str, set_str):
    """
    BOOL FaxGetDeviceStatus(
        HANDLE FaxPortHandle,
        PFAX_DEVICE_STATUS* DeviceStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "DeviceStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetDeviceStatusA(jitter):
    winfax_FaxGetDeviceStatus(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxGetDeviceStatusW(jitter):
    winfax_FaxGetDeviceStatus(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxGetPort(jitter, get_str, set_str):
    """
    BOOL FaxGetPort(
        HANDLE FaxPortHandle,
        PFAX_PORT_INFO* PortInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "PortInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetPortA(jitter):
    winfax_FaxGetPort(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxGetPortW(jitter):
    winfax_FaxGetPort(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxSetPort(jitter, get_str, set_str):
    """
    BOOL FaxSetPort(
        HANDLE FaxPortHandle,
        const FAX_PORT_INFO* PortInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "PortInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetPortA(jitter):
    winfax_FaxSetPort(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxSetPortW(jitter):
    winfax_FaxSetPort(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxSendDocumentForBroadcast(jitter, get_str, set_str):
    """
    BOOL FaxSendDocumentForBroadcast(
        HANDLE FaxHandle,
        LPCTSTR FileName,
        LPDWORD FaxJobId,
        PFAX_RECIPIENT_CALLBACK FaxRecipientCallback,
        LPVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FileName", "FaxJobId", "FaxRecipientCallback", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSendDocumentForBroadcastA(jitter):
    winfax_FaxSendDocumentForBroadcast(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxSendDocumentForBroadcastW(jitter):
    winfax_FaxSendDocumentForBroadcast(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxPrintCoverPage(jitter, get_str, set_str):
    """
    BOOL FaxPrintCoverPage(
        const FAX_CONTEXT_INFO* FaxContextInfo,
        const FAX_COVERPAGE_INFO* CoverPageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxContextInfo", "CoverPageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxPrintCoverPageA(jitter):
    winfax_FaxPrintCoverPage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxPrintCoverPageW(jitter):
    winfax_FaxPrintCoverPage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxStartPrintJob(jitter, get_str, set_str):
    """
    BOOL FaxStartPrintJob(
        LPCTSTR PrinterName,
        const FAX_PRINT_INFO* PrintInfo,
        LPDWORD FaxJobId,
        PFAX_CONTEXT_INFO FaxContextInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrinterName", "PrintInfo", "FaxJobId", "FaxContextInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxStartPrintJobA(jitter):
    winfax_FaxStartPrintJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxStartPrintJobW(jitter):
    winfax_FaxStartPrintJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxAbort(jitter):
    """
    BOOL FaxAbort(
        HANDLE FaxHandle,
        DWORD JobId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumJobs(jitter, get_str, set_str):
    """
    BOOL FaxEnumJobs(
        HANDLE FaxHandle,
        PFAX_JOB_ENTRY* JobEntry,
        LPDWORD JobsReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobEntry", "JobsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumJobsA(jitter):
    winfax_FaxEnumJobs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxEnumJobsW(jitter):
    winfax_FaxEnumJobs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxGetJob(jitter, get_str, set_str):
    """
    BOOL FaxGetJob(
        HANDLE FaxHandle,
        DWORD JobId,
        PFAX_JOB_ENTRY* JobEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId", "JobEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetJobA(jitter):
    winfax_FaxGetJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxGetJobW(jitter):
    winfax_FaxGetJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxSetJob(jitter, get_str, set_str):
    """
    BOOL FaxSetJob(
        HANDLE FaxHandle,
        DWORD JobId,
        DWORD Command,
        const FAX_JOB_ENTRY* JobEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId", "Command", "JobEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetJobA(jitter):
    winfax_FaxSetJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxSetJobW(jitter):
    winfax_FaxSetJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxAccessCheck(jitter):
    """
    BOOL FaxAccessCheck(
        HANDLE FaxHandle,
        DWORD AccessMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "AccessMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxCompleteJobParams(jitter, get_str, set_str):
    """
    BOOL FaxCompleteJobParams(
        PFAX_JOB_PARAM* JobParams,
        PFAX_COVERPAGE_INFO* CoverpageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["JobParams", "CoverpageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxCompleteJobParamsA(jitter):
    winfax_FaxCompleteJobParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxCompleteJobParamsW(jitter):
    winfax_FaxCompleteJobParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxFreeBuffer(jitter):
    """
    void FaxFreeBuffer(
        LPVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxRegisterRoutingExtensionW(jitter):
    """
    BOOL FaxRegisterRoutingExtensionW(
        HANDLE FaxHandle,
        LPCWSTR ExtensionName,
        LPCWSTR FriendlyName,
        LPCWSTR ImageName,
        PFAX_ROUTING_INSTALLATION_CALLBACK CallBack,
        LPVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "ExtensionName", "FriendlyName", "ImageName", "CallBack", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxRegisterServiceProviderW(jitter):
    """
    BOOL FaxRegisterServiceProviderW(
        LPCWSTR DeviceProvider,
        LPCWSTR FriendlyName,
        LPCWSTR ImageName,
        LPCWSTR TspName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceProvider", "FriendlyName", "ImageName", "TspName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxClose(jitter):
    """
    BOOL FaxClose(
        HANDLE FaxHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxConnectFaxServer(jitter, get_str, set_str):
    """
    BOOL FaxConnectFaxServer(
        LPCTSTR MachineName,
        LPHANDLE FaxHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MachineName", "FaxHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxConnectFaxServerA(jitter):
    winfax_FaxConnectFaxServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxConnectFaxServerW(jitter):
    winfax_FaxConnectFaxServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxEnableRoutingMethod(jitter, get_str, set_str):
    """
    BOOL FaxEnableRoutingMethod(
        HANDLE FaxPortHandle,
        LPCTSTR RoutingGuid,
        BOOL Enabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "RoutingGuid", "Enabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnableRoutingMethodA(jitter):
    winfax_FaxEnableRoutingMethod(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxEnableRoutingMethodW(jitter):
    winfax_FaxEnableRoutingMethod(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxEnumGlobalRoutingInfo(jitter, get_str, set_str):
    """
    BOOL FaxEnumGlobalRoutingInfo(
        HANDLE FaxHandle,
        PFAX_GLOBAL_ROUTING_INFO* RoutingInfo,
        LPDWORD MethodsReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "RoutingInfo", "MethodsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumGlobalRoutingInfoA(jitter):
    winfax_FaxEnumGlobalRoutingInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxEnumGlobalRoutingInfoW(jitter):
    winfax_FaxEnumGlobalRoutingInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxEnumPorts(jitter, get_str, set_str):
    """
    BOOL FaxEnumPorts(
        HANDLE FaxHandle,
        PFAX_PORT_INFO* PortInfo,
        LPDWORD PortsReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "PortInfo", "PortsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumPortsA(jitter):
    winfax_FaxEnumPorts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxEnumPortsW(jitter):
    winfax_FaxEnumPorts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxEnumRoutingMethods(jitter, get_str, set_str):
    """
    BOOL FaxEnumRoutingMethods(
        HANDLE FaxPortHandle,
        PFAX_ROUTING_METHOD* RoutingMethod,
        LPDWORD MethodsReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "RoutingMethod", "MethodsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumRoutingMethodsA(jitter):
    winfax_FaxEnumRoutingMethods(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxEnumRoutingMethodsW(jitter):
    winfax_FaxEnumRoutingMethods(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxGetLoggingCategories(jitter, get_str, set_str):
    """
    BOOL FaxGetLoggingCategories(
        HANDLE FaxHandle,
        PFAX_LOG_CATEGORY* Categories,
        LPDWORD NumberCategories
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "Categories", "NumberCategories"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetLoggingCategoriesA(jitter):
    winfax_FaxGetLoggingCategories(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxGetLoggingCategoriesW(jitter):
    winfax_FaxGetLoggingCategories(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxGetPageData(jitter):
    """
    BOOL FaxGetPageData(
        HANDLE FaxHandle,
        DWORD JobId,
        LPBYTE* Buffer,
        LPDWORD BufferSize,
        LPDWORD ImageWidth,
        LPDWORD ImageHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId", "Buffer", "BufferSize", "ImageWidth", "ImageHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetRoutingInfo(jitter, get_str, set_str):
    """
    BOOL FaxGetRoutingInfo(
        HANDLE FaxPortHandle,
        LPCTSTR RoutingGuid,
        LPBYTE* RoutingInfoBuffer,
        LPDWORD RoutingInfoBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "RoutingGuid", "RoutingInfoBuffer", "RoutingInfoBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetRoutingInfoA(jitter):
    winfax_FaxGetRoutingInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxGetRoutingInfoW(jitter):
    winfax_FaxGetRoutingInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxInitializeEventQueue(jitter):
    """
    BOOL FaxInitializeEventQueue(
        HANDLE FaxHandle,
        HANDLE CompletionPort,
        ULONG_PTR CompletionKey,
        HWND hWnd,
        UINT MessageStart
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "CompletionPort", "CompletionKey", "hWnd", "MessageStart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSendDocument(jitter, get_str, set_str):
    """
    BOOL FaxSendDocument(
        HANDLE FaxHandle,
        LPCTSTR FileName,
        PFAX_JOB_PARAM JobParams,
        const FAX_COVERPAGE_INFO* CoverpageInfo,
        LPDWORD FaxJobId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FileName", "JobParams", "CoverpageInfo", "FaxJobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSendDocumentA(jitter):
    winfax_FaxSendDocument(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxSendDocumentW(jitter):
    winfax_FaxSendDocument(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def winfax_FaxSetRoutingInfo(jitter, get_str, set_str):
    """
    BOOL FaxSetRoutingInfo(
        HANDLE FaxPortHandle,
        LPCTSTR RoutingGuid,
        const BYTE* RoutingInfoBuffer,
        DWORD RoutingInfoBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "RoutingGuid", "RoutingInfoBuffer", "RoutingInfoBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetRoutingInfoA(jitter):
    winfax_FaxSetRoutingInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def winfax_FaxSetRoutingInfoW(jitter):
    winfax_FaxSetRoutingInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
