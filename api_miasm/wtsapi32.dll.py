
def wtsapi32_WTSCloseServer(jitter):
    """
    void WTSCloseServer(
        [WtsServerHandle] hServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSConnectSession(jitter, get_str, set_str):
    """
    BOOL WTSConnectSession(
        ULONG LogonId,
        ULONG TargetLogonId,
        PTSTR pPassword,
        BOOL bWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogonId", "TargetLogonId", "pPassword", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSConnectSessionA(jitter):
    wtsapi32_WTSConnectSession(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSConnectSessionW(jitter):
    wtsapi32_WTSConnectSession(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSCreateListener(jitter, get_str, set_str):
    """
    BOOL WTSCreateListener(
        [WtsServerHandle] hServer,
        PVOID pReserved,
        DWORD Reserved,
        LPTSTR pListenerName,
        PWTSLISTENERCONFIG pBuffer,
        DWORD flag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListenerName", "pBuffer", "flag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSCreateListenerA(jitter):
    wtsapi32_WTSCreateListener(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSCreateListenerW(jitter):
    wtsapi32_WTSCreateListener(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSDisconnectSession(jitter):
    """
    BOOL WTSDisconnectSession(
        [WtsServerHandle] hServer,
        DWORD SessionId,
        BOOL bWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnableChildSessions(jitter):
    """
    BOOL WTSEnableChildSessions(
        BOOL bEnable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateListeners(jitter, get_str, set_str):
    """
    BOOL WTSEnumerateListeners(
        [WtsServerHandle] hServer,
        PVOID pReserved,
        DWORD Reserved,
        PWTSLISTENERNAME pListeners,
        DWORD* pCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListeners", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateListenersA(jitter):
    wtsapi32_WTSEnumerateListeners(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSEnumerateListenersW(jitter):
    wtsapi32_WTSEnumerateListeners(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSEnumerateProcesses(jitter, get_str, set_str):
    """
    BOOL WTSEnumerateProcesses(
        [WtsServerHandle] hServer,
        DWORD Reserved,
        DWORD Version,
        PWTS_PROCESS_INFO* ppProcessInfo,
        DWORD* pCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "Reserved", "Version", "ppProcessInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateProcessesA(jitter):
    wtsapi32_WTSEnumerateProcesses(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSEnumerateProcessesW(jitter):
    wtsapi32_WTSEnumerateProcesses(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSEnumerateProcessesEx(jitter, get_str, set_str):
    """
    BOOL WTSEnumerateProcessesEx(
        [WtsServerHandle] hServer,
        DWORD* pLevel,
        DWORD SessionID,
        LPTSTR* ppProcessInfo,
        DWORD* pCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pLevel", "SessionID", "ppProcessInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateProcessesExA(jitter):
    wtsapi32_WTSEnumerateProcessesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSEnumerateProcessesExW(jitter):
    wtsapi32_WTSEnumerateProcessesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSEnumerateServers(jitter, get_str, set_str):
    """
    BOOL WTSEnumerateServers(
        LPTSTR pDomainName,
        DWORD Reserved,
        DWORD Version,
        PWTS_SERVER_INFO* ppServerInfo,
        DWORD* pCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDomainName", "Reserved", "Version", "ppServerInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateServersA(jitter):
    wtsapi32_WTSEnumerateServers(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSEnumerateServersW(jitter):
    wtsapi32_WTSEnumerateServers(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSEnumerateSessions(jitter, get_str, set_str):
    """
    BOOL WTSEnumerateSessions(
        [WtsServerHandle] hServer,
        DWORD Reserved,
        DWORD Version,
        PWTS_SESSION_INFO* ppSessionInfo,
        DWORD* pCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "Reserved", "Version", "ppSessionInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateSessionsA(jitter):
    wtsapi32_WTSEnumerateSessions(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSEnumerateSessionsW(jitter):
    wtsapi32_WTSEnumerateSessions(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSEnumerateSessionsEx(jitter, get_str, set_str):
    """
    BOOL WTSEnumerateSessionsEx(
        [WtsServerHandle] hServer,
        DWORD* pLevel,
        DWORD Filter,
        PWTS_SESSION_INFO_1* ppSessionInfo,
        DWORD* pCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pLevel", "Filter", "ppSessionInfo", "pCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSEnumerateSessionsExA(jitter):
    wtsapi32_WTSEnumerateSessionsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSEnumerateSessionsExW(jitter):
    wtsapi32_WTSEnumerateSessionsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSFreeMemory(jitter):
    """
    void WTSFreeMemory(
        PVOID pMemory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSFreeMemoryEx(jitter, get_str, set_str):
    """
    BOOL WTSFreeMemoryEx(
        WTS_TYPE_CLASS WTSTypeClass,
        PVOID pMemory,
        ULONG NumberOfEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["WTSTypeClass", "pMemory", "NumberOfEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSFreeMemoryExA(jitter):
    wtsapi32_WTSFreeMemoryEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSFreeMemoryExW(jitter):
    wtsapi32_WTSFreeMemoryEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSGetChildSessionId(jitter):
    """
    BOOL WTSGetChildSessionId(
        ULONG* pSessionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSGetListenerSecurity(jitter, get_str, set_str):
    """
    BOOL WTSGetListenerSecurity(
        [WtsServerHandle] hServer,
        PVOID pReserved,
        DWORD Reserved,
        LPTSTR pListenerName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor,
        DWORD nLength,
        LPDWORD lpnLengthNeeded
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListenerName", "SecurityInformation", "pSecurityDescriptor", "nLength", "lpnLengthNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSGetListenerSecurityA(jitter):
    wtsapi32_WTSGetListenerSecurity(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSGetListenerSecurityW(jitter):
    wtsapi32_WTSGetListenerSecurity(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSIsChildSessionsEnabled(jitter):
    """
    BOOL WTSIsChildSessionsEnabled(
        BOOL* pbEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSLogoffSession(jitter):
    """
    BOOL WTSLogoffSession(
        [WtsServerHandle] hServer,
        DWORD SessionId,
        BOOL bWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSOpenServer(jitter, get_str, set_str):
    """
    HANDLE WTSOpenServer(
        LPTSTR pServerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSOpenServerA(jitter):
    wtsapi32_WTSOpenServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSOpenServerW(jitter):
    wtsapi32_WTSOpenServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSOpenServerEx(jitter, get_str, set_str):
    """
    HANDLE WTSOpenServerEx(
        LPTSTR pServerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSOpenServerExA(jitter):
    wtsapi32_WTSOpenServerEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSOpenServerExW(jitter):
    wtsapi32_WTSOpenServerEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSQueryListenerConfig(jitter, get_str, set_str):
    """
    BOOL WTSQueryListenerConfig(
        [WtsServerHandle] hServer,
        PVOID pReserved,
        DWORD Reserved,
        LPTSTR pListenerName,
        PWTSLISTENERCONFIG pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListenerName", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSQueryListenerConfigA(jitter):
    wtsapi32_WTSQueryListenerConfig(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSQueryListenerConfigW(jitter):
    wtsapi32_WTSQueryListenerConfig(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSQuerySessionInformation(jitter, get_str, set_str):
    """
    BOOL WTSQuerySessionInformation(
        [WtsServerHandle] hServer,
        DWORD SessionId,
        WTS_INFO_CLASS WTSInfoClass,
        LPTSTR* ppBuffer,
        DWORD* pBytesReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "WTSInfoClass", "ppBuffer", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSQuerySessionInformationA(jitter):
    wtsapi32_WTSQuerySessionInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSQuerySessionInformationW(jitter):
    wtsapi32_WTSQuerySessionInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSQueryUserConfig(jitter, get_str, set_str):
    """
    BOOL WTSQueryUserConfig(
        LPTSTR pServerName,
        LPTSTR pUserName,
        WTS_CONFIG_CLASS WTSConfigClass,
        LPTSTR* ppBuffer,
        DWORD* pBytesReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pServerName", "pUserName", "WTSConfigClass", "ppBuffer", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSQueryUserConfigA(jitter):
    wtsapi32_WTSQueryUserConfig(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSQueryUserConfigW(jitter):
    wtsapi32_WTSQueryUserConfig(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSQueryUserToken(jitter):
    """
    BOOL WTSQueryUserToken(
        ULONG SessionId,
        PHANDLE phToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionId", "phToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSRegisterSessionNotification(jitter):
    """
    BOOL WTSRegisterSessionNotification(
        HWND hWnd,
        [ConsoleNotificationFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSRegisterSessionNotificationEx(jitter):
    """
    BOOL WTSRegisterSessionNotificationEx(
        [WtsServerHandle] hServer,
        HWND hWnd,
        [ConsoleNotificationFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "hWnd", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSendMessage(jitter, get_str, set_str):
    """
    BOOL WTSSendMessage(
        [WtsServerHandle] hServer,
        DWORD SessionId,
        LPTSTR pTitle,
        DWORD TitleLength,
        LPTSTR pMessage,
        DWORD MessageLength,
        DWORD Style,
        DWORD Timeout,
        DWORD* pResponse,
        BOOL bWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "pTitle", "TitleLength", "pMessage", "MessageLength", "Style", "Timeout", "pResponse", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSendMessageA(jitter):
    wtsapi32_WTSSendMessage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSSendMessageW(jitter):
    wtsapi32_WTSSendMessage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSSetListenerSecurity(jitter, get_str, set_str):
    """
    BOOL WTSSetListenerSecurity(
        [WtsServerHandle] hServer,
        PVOID pReserved,
        DWORD Reserved,
        LPTSTR pListenerName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "pReserved", "Reserved", "pListenerName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSetListenerSecurityA(jitter):
    wtsapi32_WTSSetListenerSecurity(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSSetListenerSecurityW(jitter):
    wtsapi32_WTSSetListenerSecurity(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSSetUserConfig(jitter, get_str, set_str):
    """
    BOOL WTSSetUserConfig(
        LPTSTR pServerName,
        LPTSTR pUserName,
        WTS_CONFIG_CLASS WTSConfigClass,
        LPTSTR pBuffer,
        DWORD DataLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pServerName", "pUserName", "WTSConfigClass", "pBuffer", "DataLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSetUserConfigA(jitter):
    wtsapi32_WTSSetUserConfig(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSSetUserConfigW(jitter):
    wtsapi32_WTSSetUserConfig(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSShutdownSystem(jitter):
    """
    BOOL WTSShutdownSystem(
        [WtsServerHandle] hServer,
        DWORD ShutdownFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "ShutdownFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSStartRemoteControlSession(jitter, get_str, set_str):
    """
    BOOL WTSStartRemoteControlSession(
        LPTSTR pTargetServerName,
        ULONG TargetLogonId,
        BYTE HotkeyVk,
        USHORT HotkeyModifiers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTargetServerName", "TargetLogonId", "HotkeyVk", "HotkeyModifiers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSStartRemoteControlSessionA(jitter):
    wtsapi32_WTSStartRemoteControlSession(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wtsapi32_WTSStartRemoteControlSessionW(jitter):
    wtsapi32_WTSStartRemoteControlSession(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wtsapi32_WTSStopRemoteControlSession(jitter):
    """
    BOOL WTSStopRemoteControlSession(
        ULONG LogonId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogonId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSTerminateProcess(jitter):
    """
    BOOL WTSTerminateProcess(
        [WtsServerHandle] hServer,
        DWORD ProcessId,
        DWORD ExitCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "ProcessId", "ExitCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSUnRegisterSessionNotification(jitter):
    """
    BOOL WTSUnRegisterSessionNotification(
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSUnRegisterSessionNotificationEx(jitter):
    """
    BOOL WTSUnRegisterSessionNotificationEx(
        [WtsServerHandle] hServer,
        HWND hWnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "hWnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelClose(jitter):
    """
    BOOL WTSVirtualChannelClose(
        HANDLE hChannelHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelOpen(jitter):
    """
    HANDLE WTSVirtualChannelOpen(
        [WtsServerHandle] hServer,
        DWORD SessionId,
        LPSTR pVirtualName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "SessionId", "pVirtualName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelOpenEx(jitter):
    """
    HANDLE WTSVirtualChannelOpenEx(
        DWORD SessionId,
        LPSTR pVirtualName,
        DWORD flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SessionId", "pVirtualName", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelPurgeInput(jitter):
    """
    BOOL WTSVirtualChannelPurgeInput(
        HANDLE hChannelHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelPurgeOutput(jitter):
    """
    BOOL WTSVirtualChannelPurgeOutput(
        HANDLE hChannelHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelQuery(jitter):
    """
    BOOL WTSVirtualChannelQuery(
        HANDLE hChannelHandle,
        WTS_VIRTUAL_CLASS WtsVirtualClass,
        PVOID* ppBuffer,
        DWORD* pBytesReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle", "WtsVirtualClass", "ppBuffer", "pBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelRead(jitter):
    """
    BOOL WTSVirtualChannelRead(
        HANDLE hChannelHandle,
        ULONG TimeOut,
        LPVOID Buffer,
        ULONG BufferSize,
        PULONG pBytesRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle", "TimeOut", "Buffer", "BufferSize", "pBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSVirtualChannelWrite(jitter):
    """
    BOOL WTSVirtualChannelWrite(
        HANDLE hChannelHandle,
        LPVOID Buffer,
        ULONG Length,
        PULONG pBytesWritten
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hChannelHandle", "Buffer", "Length", "pBytesWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSWaitSystemEvent(jitter):
    """
    BOOL WTSWaitSystemEvent(
        [WtsServerHandle] hServer,
        [WtsEventFlags] EventMask,
        [WtsEventFlags*] pEventFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hServer", "EventMask", "pEventFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wtsapi32_WTSSetRenderHint(jitter):
    """
    HRESULT WTSSetRenderHint(
        UINT64* pRenderHintID,
        HWND hwndOwner,
        DWORD renderHintType,
        DWORD cbHintDataLength,
        BYTE* pHintData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRenderHintID", "hwndOwner", "renderHintType", "cbHintDataLength", "pHintData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
