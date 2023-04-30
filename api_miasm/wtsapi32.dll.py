
def wtsapi32_WTSCloseServer(jitter):
    """"
    [WtsApi32.dll] void WTSCloseServer([WtsServerHandle] hServer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSConnectSession(jitter):
    """"
    [WtsApi32.dll] BOOL WTSConnectSession(ULONG LogonId, ULONG TargetLogonId, PTSTR pPassword, BOOL bWait)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogonId", "TargetLogonId", "pPassword", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSCreateListener(jitter):
    """"
    [WtsApi32.dll] BOOL WTSCreateListener([WtsServerHandle] hServer, PVOID pReserved, DWORD Reserved, LPTSTR pListenerName, PWTSLISTENERCONFIG pBuffer, DWORD flag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListenerName", "pBuffer", "flag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSDisconnectSession(jitter):
    """"
    [WtsApi32.dll] BOOL WTSDisconnectSession([WtsServerHandle] hServer, DWORD SessionId, BOOL bWait)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnableChildSessions(jitter):
    """"
    [WtsApi32.dll] BOOL WTSEnableChildSessions(BOOL bEnable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["bEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateListeners(jitter):
    """"
    [WtsApi32.dll] BOOL WTSEnumerateListeners([WtsServerHandle] hServer, PVOID pReserved, DWORD Reserved, PWTSLISTENERNAME pListeners, DWORD* pCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListeners", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateProcesses(jitter):
    """"
    [WtsApi32.dll] BOOL WTSEnumerateProcesses([WtsServerHandle] hServer, DWORD Reserved, DWORD Version, PWTS_PROCESS_INFO* ppProcessInfo, DWORD* pCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "Reserved", "Version", "ppProcessInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateProcessesEx(jitter):
    """"
    [WtsApi32.dll] BOOL WTSEnumerateProcessesEx([WtsServerHandle] hServer, DWORD* pLevel, DWORD SessionID, LPTSTR* ppProcessInfo, DWORD* pCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pLevel", "SessionID", "ppProcessInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateServers(jitter):
    """"
    [WtsApi32.dll] BOOL WTSEnumerateServers(LPTSTR pDomainName, DWORD Reserved, DWORD Version, PWTS_SERVER_INFO* ppServerInfo, DWORD* pCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDomainName", "Reserved", "Version", "ppServerInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateSessions(jitter):
    """"
    [WtsApi32.dll] BOOL WTSEnumerateSessions([WtsServerHandle] hServer, DWORD Reserved, DWORD Version, PWTS_SESSION_INFO* ppSessionInfo, DWORD* pCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "Reserved", "Version", "ppSessionInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateSessionsEx(jitter):
    """"
    [WtsApi32.dll] BOOL WTSEnumerateSessionsEx([WtsServerHandle] hServer, DWORD* pLevel, DWORD Filter, PWTS_SESSION_INFO_1* ppSessionInfo, DWORD* pCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pLevel", "Filter", "ppSessionInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSFreeMemory(jitter):
    """"
    [WtsApi32.dll] void WTSFreeMemory(PVOID pMemory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSFreeMemoryEx(jitter):
    """"
    [WtsApi32.dll] BOOL WTSFreeMemoryEx(WTS_TYPE_CLASS WTSTypeClass, PVOID pMemory, ULONG NumberOfEntries)
    """"
    ret_ad, args = jitter.func_args_stdcall(["WTSTypeClass", "pMemory", "NumberOfEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSGetChildSessionId(jitter):
    """"
    [WtsApi32.dll] BOOL WTSGetChildSessionId(ULONG* pSessionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSGetListenerSecurity(jitter):
    """"
    [WtsApi32.dll] BOOL WTSGetListenerSecurity([WtsServerHandle] hServer, PVOID pReserved, DWORD Reserved, LPTSTR pListenerName, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor, DWORD nLength, LPDWORD lpnLengthNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListenerName", "SecurityInformation", "pSecurityDescriptor", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSIsChildSessionsEnabled(jitter):
    """"
    [WtsApi32.dll] BOOL WTSIsChildSessionsEnabled(BOOL* pbEnabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSLogoffSession(jitter):
    """"
    [WtsApi32.dll] BOOL WTSLogoffSession([WtsServerHandle] hServer, DWORD SessionId, BOOL bWait)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSOpenServer(jitter):
    """"
    [WtsApi32.dll] HANDLE WTSOpenServer(LPTSTR pServerName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSOpenServerEx(jitter):
    """"
    [WtsApi32.dll] HANDLE WTSOpenServerEx(LPTSTR pServerName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSQueryListenerConfig(jitter):
    """"
    [WtsApi32.dll] BOOL WTSQueryListenerConfig([WtsServerHandle] hServer, PVOID pReserved, DWORD Reserved, LPTSTR pListenerName, PWTSLISTENERCONFIG pBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListenerName", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSQuerySessionInformation(jitter):
    """"
    [WtsApi32.dll] BOOL WTSQuerySessionInformation([WtsServerHandle] hServer, DWORD SessionId, WTS_INFO_CLASS WTSInfoClass, LPTSTR* ppBuffer, DWORD* pBytesReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "WTSInfoClass", "ppBuffer", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSQueryUserConfig(jitter):
    """"
    [WtsApi32.dll] BOOL WTSQueryUserConfig(LPTSTR pServerName, LPTSTR pUserName, WTS_CONFIG_CLASS WTSConfigClass, LPTSTR* ppBuffer, DWORD* pBytesReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pServerName", "pUserName", "WTSConfigClass", "ppBuffer", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSQueryUserToken(jitter):
    """"
    [WtsApi32.dll] BOOL WTSQueryUserToken(ULONG SessionId, PHANDLE phToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionId", "phToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSRegisterSessionNotification(jitter):
    """"
    [WtsApi32.dll] BOOL WTSRegisterSessionNotification(HWND hWnd, [ConsoleNotificationFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSRegisterSessionNotificationEx(jitter):
    """"
    [WtsApi32.dll] BOOL WTSRegisterSessionNotificationEx([WtsServerHandle] hServer, HWND hWnd, [ConsoleNotificationFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "hWnd", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSendMessage(jitter):
    """"
    [WtsApi32.dll] BOOL WTSSendMessage([WtsServerHandle] hServer, DWORD SessionId, LPTSTR pTitle, DWORD TitleLength, LPTSTR pMessage, DWORD MessageLength, DWORD Style, DWORD Timeout, DWORD* pResponse, BOOL bWait)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "pTitle", "TitleLength", "pMessage", "MessageLength", "Style", "Timeout", "pResponse", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSetListenerSecurity(jitter):
    """"
    [WtsApi32.dll] BOOL WTSSetListenerSecurity([WtsServerHandle] hServer, PVOID pReserved, DWORD Reserved, LPTSTR pListenerName, SECURITY_INFORMATION SecurityInformation, PSECURITY_DESCRIPTOR pSecurityDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListenerName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSetUserConfig(jitter):
    """"
    [WtsApi32.dll] BOOL WTSSetUserConfig(LPTSTR pServerName, LPTSTR pUserName, WTS_CONFIG_CLASS WTSConfigClass, LPTSTR pBuffer, DWORD DataLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pServerName", "pUserName", "WTSConfigClass", "pBuffer", "DataLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSShutdownSystem(jitter):
    """"
    [WtsApi32.dll] BOOL WTSShutdownSystem([WtsServerHandle] hServer, DWORD ShutdownFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "ShutdownFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSStartRemoteControlSession(jitter):
    """"
    [WtsApi32.dll] BOOL WTSStartRemoteControlSession(LPTSTR pTargetServerName, ULONG TargetLogonId, BYTE HotkeyVk, USHORT HotkeyModifiers)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pTargetServerName", "TargetLogonId", "HotkeyVk", "HotkeyModifiers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSStopRemoteControlSession(jitter):
    """"
    [WtsApi32.dll] BOOL WTSStopRemoteControlSession(ULONG LogonId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogonId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSTerminateProcess(jitter):
    """"
    [WtsApi32.dll] BOOL WTSTerminateProcess([WtsServerHandle] hServer, DWORD ProcessId, DWORD ExitCode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "ProcessId", "ExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSUnRegisterSessionNotification(jitter):
    """"
    [WtsApi32.dll] BOOL WTSUnRegisterSessionNotification(HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSUnRegisterSessionNotificationEx(jitter):
    """"
    [WtsApi32.dll] BOOL WTSUnRegisterSessionNotificationEx([WtsServerHandle] hServer, HWND hWnd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelClose(jitter):
    """"
    [WtsApi32.dll] BOOL WTSVirtualChannelClose(HANDLE hChannelHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelOpen(jitter):
    """"
    [WtsApi32.dll] HANDLE WTSVirtualChannelOpen([WtsServerHandle] hServer, DWORD SessionId, LPSTR pVirtualName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "pVirtualName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelOpenEx(jitter):
    """"
    [WtsApi32.dll] HANDLE WTSVirtualChannelOpenEx(DWORD SessionId, LPSTR pVirtualName, DWORD flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SessionId", "pVirtualName", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelPurgeInput(jitter):
    """"
    [WtsApi32.dll] BOOL WTSVirtualChannelPurgeInput(HANDLE hChannelHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelPurgeOutput(jitter):
    """"
    [WtsApi32.dll] BOOL WTSVirtualChannelPurgeOutput(HANDLE hChannelHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelQuery(jitter):
    """"
    [WtsApi32.dll] BOOL WTSVirtualChannelQuery(HANDLE hChannelHandle, WTS_VIRTUAL_CLASS WtsVirtualClass, PVOID* ppBuffer, DWORD* pBytesReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle", "WtsVirtualClass", "ppBuffer", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelRead(jitter):
    """"
    [WtsApi32.dll] BOOL WTSVirtualChannelRead(HANDLE hChannelHandle, ULONG TimeOut, LPVOID Buffer, ULONG BufferSize, PULONG pBytesRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle", "TimeOut", "Buffer", "BufferSize", "pBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelWrite(jitter):
    """"
    [WtsApi32.dll] BOOL WTSVirtualChannelWrite(HANDLE hChannelHandle, LPVOID Buffer, ULONG Length, PULONG pBytesWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle", "Buffer", "Length", "pBytesWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSWaitSystemEvent(jitter):
    """"
    [WtsApi32.dll] BOOL WTSWaitSystemEvent([WtsServerHandle] hServer, [WtsEventFlags] EventMask, [WtsEventFlags*] pEventFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hServer", "EventMask", "pEventFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSetRenderHint(jitter):
    """"
    [WtsApi32.dll] HRESULT WTSSetRenderHint(UINT64* pRenderHintID, HWND hwndOwner, DWORD renderHintType, DWORD cbHintDataLength, BYTE* pHintData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pRenderHintID", "hwndOwner", "renderHintType", "cbHintDataLength", "pHintData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
