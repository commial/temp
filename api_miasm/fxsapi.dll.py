###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def fxsapi_FaxOpenPort(jitter):
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

def fxsapi_FaxGetConfiguration(jitter, get_str, set_str):
    """
    BOOL FaxGetConfiguration(
        HANDLE FaxHandle,
        PFAX_CONFIGURATION* FaxConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FaxConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxGetConfigurationA(jitter):
    fxsapi_FaxGetConfiguration(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxGetConfigurationW(jitter):
    fxsapi_FaxGetConfiguration(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxSetConfiguration(jitter, get_str, set_str):
    """
    BOOL FaxSetConfiguration(
        HANDLE FaxHandle,
        const FAX_CONFIGURATION* FaxConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FaxConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxSetConfigurationA(jitter):
    fxsapi_FaxSetConfiguration(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxSetConfigurationW(jitter):
    fxsapi_FaxSetConfiguration(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxSetGlobalRoutingInfo(jitter, get_str, set_str):
    """
    BOOL FaxSetGlobalRoutingInfo(
        HANDLE FaxHandle,
        const FAX_GLOBAL_ROUTING_INFO* RoutingInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "RoutingInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxSetGlobalRoutingInfoA(jitter):
    fxsapi_FaxSetGlobalRoutingInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxSetGlobalRoutingInfoW(jitter):
    fxsapi_FaxSetGlobalRoutingInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxSetLoggingCategories(jitter, get_str, set_str):
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

def fxsapi_FaxSetLoggingCategoriesA(jitter):
    fxsapi_FaxSetLoggingCategories(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxSetLoggingCategoriesW(jitter):
    fxsapi_FaxSetLoggingCategories(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxGetDeviceStatus(jitter, get_str, set_str):
    """
    BOOL FaxGetDeviceStatus(
        HANDLE FaxPortHandle,
        PFAX_DEVICE_STATUS* DeviceStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "DeviceStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxGetDeviceStatusA(jitter):
    fxsapi_FaxGetDeviceStatus(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxGetDeviceStatusW(jitter):
    fxsapi_FaxGetDeviceStatus(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxGetPort(jitter, get_str, set_str):
    """
    BOOL FaxGetPort(
        HANDLE FaxPortHandle,
        PFAX_PORT_INFO* PortInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "PortInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxGetPortA(jitter):
    fxsapi_FaxGetPort(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxGetPortW(jitter):
    fxsapi_FaxGetPort(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxSetPort(jitter, get_str, set_str):
    """
    BOOL FaxSetPort(
        HANDLE FaxPortHandle,
        const FAX_PORT_INFO* PortInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "PortInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxSetPortA(jitter):
    fxsapi_FaxSetPort(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxSetPortW(jitter):
    fxsapi_FaxSetPort(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxSendDocumentForBroadcast(jitter, get_str, set_str):
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

def fxsapi_FaxSendDocumentForBroadcastA(jitter):
    fxsapi_FaxSendDocumentForBroadcast(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxSendDocumentForBroadcastW(jitter):
    fxsapi_FaxSendDocumentForBroadcast(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxPrintCoverPage(jitter, get_str, set_str):
    """
    BOOL FaxPrintCoverPage(
        const FAX_CONTEXT_INFO* FaxContextInfo,
        const FAX_COVERPAGE_INFO* CoverPageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxContextInfo", "CoverPageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxPrintCoverPageA(jitter):
    fxsapi_FaxPrintCoverPage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxPrintCoverPageW(jitter):
    fxsapi_FaxPrintCoverPage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxStartPrintJob(jitter, get_str, set_str):
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

def fxsapi_FaxStartPrintJobA(jitter):
    fxsapi_FaxStartPrintJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxStartPrintJobW(jitter):
    fxsapi_FaxStartPrintJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxAbort(jitter):
    """
    BOOL FaxAbort(
        HANDLE FaxHandle,
        DWORD JobId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxEnumJobs(jitter, get_str, set_str):
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

def fxsapi_FaxEnumJobsA(jitter):
    fxsapi_FaxEnumJobs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxEnumJobsW(jitter):
    fxsapi_FaxEnumJobs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxGetJob(jitter, get_str, set_str):
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

def fxsapi_FaxGetJobA(jitter):
    fxsapi_FaxGetJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxGetJobW(jitter):
    fxsapi_FaxGetJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxSetJob(jitter, get_str, set_str):
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

def fxsapi_FaxSetJobA(jitter):
    fxsapi_FaxSetJob(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxSetJobW(jitter):
    fxsapi_FaxSetJob(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxAccessCheck(jitter):
    """
    BOOL FaxAccessCheck(
        HANDLE FaxHandle,
        DWORD AccessMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "AccessMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxCompleteJobParams(jitter, get_str, set_str):
    """
    BOOL FaxCompleteJobParams(
        PFAX_JOB_PARAM* JobParams,
        PFAX_COVERPAGE_INFO* CoverpageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["JobParams", "CoverpageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxCompleteJobParamsA(jitter):
    fxsapi_FaxCompleteJobParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxCompleteJobParamsW(jitter):
    fxsapi_FaxCompleteJobParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxFreeBuffer(jitter):
    """
    void FaxFreeBuffer(
        LPVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxRegisterRoutingExtensionW(jitter):
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

def fxsapi_FaxRegisterServiceProviderW(jitter):
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

def fxsapi_FaxClose(jitter):
    """
    BOOL FaxClose(
        HANDLE FaxHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxConnectFaxServer(jitter, get_str, set_str):
    """
    BOOL FaxConnectFaxServer(
        LPCTSTR MachineName,
        LPHANDLE FaxHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MachineName", "FaxHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fxsapi_FaxConnectFaxServerA(jitter):
    fxsapi_FaxConnectFaxServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxConnectFaxServerW(jitter):
    fxsapi_FaxConnectFaxServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxEnableRoutingMethod(jitter, get_str, set_str):
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

def fxsapi_FaxEnableRoutingMethodA(jitter):
    fxsapi_FaxEnableRoutingMethod(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxEnableRoutingMethodW(jitter):
    fxsapi_FaxEnableRoutingMethod(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxEnumGlobalRoutingInfo(jitter, get_str, set_str):
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

def fxsapi_FaxEnumGlobalRoutingInfoA(jitter):
    fxsapi_FaxEnumGlobalRoutingInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxEnumGlobalRoutingInfoW(jitter):
    fxsapi_FaxEnumGlobalRoutingInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxEnumPorts(jitter, get_str, set_str):
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

def fxsapi_FaxEnumPortsA(jitter):
    fxsapi_FaxEnumPorts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxEnumPortsW(jitter):
    fxsapi_FaxEnumPorts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxEnumRoutingMethods(jitter, get_str, set_str):
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

def fxsapi_FaxEnumRoutingMethodsA(jitter):
    fxsapi_FaxEnumRoutingMethods(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxEnumRoutingMethodsW(jitter):
    fxsapi_FaxEnumRoutingMethods(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxGetLoggingCategories(jitter, get_str, set_str):
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

def fxsapi_FaxGetLoggingCategoriesA(jitter):
    fxsapi_FaxGetLoggingCategories(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxGetLoggingCategoriesW(jitter):
    fxsapi_FaxGetLoggingCategories(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxGetPageData(jitter):
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

def fxsapi_FaxGetRoutingInfo(jitter, get_str, set_str):
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

def fxsapi_FaxGetRoutingInfoA(jitter):
    fxsapi_FaxGetRoutingInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxGetRoutingInfoW(jitter):
    fxsapi_FaxGetRoutingInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxInitializeEventQueue(jitter):
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

def fxsapi_FaxSendDocument(jitter, get_str, set_str):
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

def fxsapi_FaxSendDocumentA(jitter):
    fxsapi_FaxSendDocument(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxSendDocumentW(jitter):
    fxsapi_FaxSendDocument(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def fxsapi_FaxSetRoutingInfo(jitter, get_str, set_str):
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

def fxsapi_FaxSetRoutingInfoA(jitter):
    fxsapi_FaxSetRoutingInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def fxsapi_FaxSetRoutingInfoW(jitter):
    fxsapi_FaxSetRoutingInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
