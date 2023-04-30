
def winfax_FaxOpenPort(jitter):
    """"
    [WinFax.dll] BOOL FaxOpenPort(HANDLE FaxHandle, DWORD DeviceId, DWORD Flags, LPHANDLE FaxPortHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "DeviceId", "Flags", "FaxPortHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetConfiguration(jitter):
    """"
    [WinFax.dll] BOOL FaxGetConfiguration(HANDLE FaxHandle, PFAX_CONFIGURATION* FaxConfig)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FaxConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetConfiguration(jitter):
    """"
    [WinFax.dll] BOOL FaxSetConfiguration(HANDLE FaxHandle, const FAX_CONFIGURATION* FaxConfig)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FaxConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetGlobalRoutingInfo(jitter):
    """"
    [WinFax.dll] BOOL FaxSetGlobalRoutingInfo(HANDLE FaxHandle, const FAX_GLOBAL_ROUTING_INFO* RoutingInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "RoutingInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetLoggingCategories(jitter):
    """"
    [WinFax.dll] BOOL FaxSetLoggingCategories(HANDLE FaxHandle, const FAX_LOG_CATEGORY* Categories, DWORD NumberCategories)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "Categories", "NumberCategories"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetDeviceStatus(jitter):
    """"
    [WinFax.dll] BOOL FaxGetDeviceStatus(HANDLE FaxPortHandle, PFAX_DEVICE_STATUS* DeviceStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "DeviceStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetPort(jitter):
    """"
    [WinFax.dll] BOOL FaxGetPort(HANDLE FaxPortHandle, PFAX_PORT_INFO* PortInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "PortInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetPort(jitter):
    """"
    [WinFax.dll] BOOL FaxSetPort(HANDLE FaxPortHandle, const FAX_PORT_INFO* PortInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "PortInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSendDocumentForBroadcast(jitter):
    """"
    [WinFax.dll] BOOL FaxSendDocumentForBroadcast(HANDLE FaxHandle, LPCTSTR FileName, LPDWORD FaxJobId, PFAX_RECIPIENT_CALLBACK FaxRecipientCallback, LPVOID Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FileName", "FaxJobId", "FaxRecipientCallback", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxPrintCoverPage(jitter):
    """"
    [WinFax.dll] BOOL FaxPrintCoverPage(const FAX_CONTEXT_INFO* FaxContextInfo, const FAX_COVERPAGE_INFO* CoverPageInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxContextInfo", "CoverPageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxStartPrintJob(jitter):
    """"
    [WinFax.dll] BOOL FaxStartPrintJob(LPCTSTR PrinterName, const FAX_PRINT_INFO* PrintInfo, LPDWORD FaxJobId, PFAX_CONTEXT_INFO FaxContextInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PrinterName", "PrintInfo", "FaxJobId", "FaxContextInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxAbort(jitter):
    """"
    [WinFax.dll] BOOL FaxAbort(HANDLE FaxHandle, DWORD JobId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumJobs(jitter):
    """"
    [WinFax.dll] BOOL FaxEnumJobs(HANDLE FaxHandle, PFAX_JOB_ENTRY* JobEntry, LPDWORD JobsReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobEntry", "JobsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetJob(jitter):
    """"
    [WinFax.dll] BOOL FaxGetJob(HANDLE FaxHandle, DWORD JobId, PFAX_JOB_ENTRY* JobEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId", "JobEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetJob(jitter):
    """"
    [WinFax.dll] BOOL FaxSetJob(HANDLE FaxHandle, DWORD JobId, DWORD Command, const FAX_JOB_ENTRY* JobEntry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId", "Command", "JobEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxAccessCheck(jitter):
    """"
    [WinFax.dll] BOOL FaxAccessCheck(HANDLE FaxHandle, DWORD AccessMask)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "AccessMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxCompleteJobParams(jitter):
    """"
    [WinFax.dll] BOOL FaxCompleteJobParams(PFAX_JOB_PARAM* JobParams, PFAX_COVERPAGE_INFO* CoverpageInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["JobParams", "CoverpageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxFreeBuffer(jitter):
    """"
    [WinFax.dll] void FaxFreeBuffer(LPVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxRegisterRoutingExtensionW(jitter):
    """"
    [WinFax.dll] BOOL FaxRegisterRoutingExtensionW(HANDLE FaxHandle, LPCWSTR ExtensionName, LPCWSTR FriendlyName, LPCWSTR ImageName, PFAX_ROUTING_INSTALLATION_CALLBACK CallBack, LPVOID Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "ExtensionName", "FriendlyName", "ImageName", "CallBack", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxRegisterServiceProviderW(jitter):
    """"
    [WinFax.dll] BOOL FaxRegisterServiceProviderW(LPCWSTR DeviceProvider, LPCWSTR FriendlyName, LPCWSTR ImageName, LPCWSTR TspName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceProvider", "FriendlyName", "ImageName", "TspName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxClose(jitter):
    """"
    [WinFax.dll] BOOL FaxClose(HANDLE FaxHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxConnectFaxServer(jitter):
    """"
    [WinFax.dll] BOOL FaxConnectFaxServer(LPCTSTR MachineName, LPHANDLE FaxHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MachineName", "FaxHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnableRoutingMethod(jitter):
    """"
    [WinFax.dll] BOOL FaxEnableRoutingMethod(HANDLE FaxPortHandle, LPCTSTR RoutingGuid, BOOL Enabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "RoutingGuid", "Enabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumGlobalRoutingInfo(jitter):
    """"
    [WinFax.dll] BOOL FaxEnumGlobalRoutingInfo(HANDLE FaxHandle, PFAX_GLOBAL_ROUTING_INFO* RoutingInfo, LPDWORD MethodsReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "RoutingInfo", "MethodsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumPorts(jitter):
    """"
    [WinFax.dll] BOOL FaxEnumPorts(HANDLE FaxHandle, PFAX_PORT_INFO* PortInfo, LPDWORD PortsReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "PortInfo", "PortsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxEnumRoutingMethods(jitter):
    """"
    [WinFax.dll] BOOL FaxEnumRoutingMethods(HANDLE FaxPortHandle, PFAX_ROUTING_METHOD* RoutingMethod, LPDWORD MethodsReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "RoutingMethod", "MethodsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetLoggingCategories(jitter):
    """"
    [WinFax.dll] BOOL FaxGetLoggingCategories(HANDLE FaxHandle, PFAX_LOG_CATEGORY* Categories, LPDWORD NumberCategories)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "Categories", "NumberCategories"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetPageData(jitter):
    """"
    [WinFax.dll] BOOL FaxGetPageData(HANDLE FaxHandle, DWORD JobId, LPBYTE* Buffer, LPDWORD BufferSize, LPDWORD ImageWidth, LPDWORD ImageHeight)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "JobId", "Buffer", "BufferSize", "ImageWidth", "ImageHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxGetRoutingInfo(jitter):
    """"
    [WinFax.dll] BOOL FaxGetRoutingInfo(HANDLE FaxPortHandle, LPCTSTR RoutingGuid, LPBYTE* RoutingInfoBuffer, LPDWORD RoutingInfoBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "RoutingGuid", "RoutingInfoBuffer", "RoutingInfoBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxInitializeEventQueue(jitter):
    """"
    [WinFax.dll] BOOL FaxInitializeEventQueue(HANDLE FaxHandle, HANDLE CompletionPort, ULONG_PTR CompletionKey, HWND hWnd, UINT MessageStart)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "CompletionPort", "CompletionKey", "hWnd", "MessageStart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSendDocument(jitter):
    """"
    [WinFax.dll] BOOL FaxSendDocument(HANDLE FaxHandle, LPCTSTR FileName, PFAX_JOB_PARAM JobParams, const FAX_COVERPAGE_INFO* CoverpageInfo, LPDWORD FaxJobId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxHandle", "FileName", "JobParams", "CoverpageInfo", "FaxJobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winfax_FaxSetRoutingInfo(jitter):
    """"
    [WinFax.dll] BOOL FaxSetRoutingInfo(HANDLE FaxPortHandle, LPCTSTR RoutingGuid, const BYTE* RoutingInfoBuffer, DWORD RoutingInfoBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FaxPortHandle", "RoutingGuid", "RoutingInfoBuffer", "RoutingInfoBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
