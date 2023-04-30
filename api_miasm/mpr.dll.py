
def mpr_WNetSetLastError(jitter, get_str, set_str):
    """"
    [Mpr.dll] void WNetSetLastError(DWORD err, LPTSTR lpError, LPTSTR lpProvider)
    """"
    ret_ad, args = jitter.func_args_stdcall(["err", "lpError", "lpProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetSetLastErrorA(jitter):
    mpr_WNetSetLastError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetSetLastErrorW(jitter):
    mpr_WNetSetLastError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_MultinetGetConnectionPerformance(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] MultinetGetConnectionPerformance(LPNETRESOURCE lpNetResource, LPNETCONNECTINFOSTRUCT lpNetConnectInfoStruct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNetResource", "lpNetConnectInfoStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_MultinetGetConnectionPerformanceA(jitter):
    mpr_MultinetGetConnectionPerformance(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_MultinetGetConnectionPerformanceW(jitter):
    mpr_MultinetGetConnectionPerformance(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetAddConnection2(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetAddConnection2(LPNETRESOURCE lpNetResource, LPCTSTR lpPassword, LPCTSTR lpUsername, [ConnectFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNetResource", "lpPassword", "lpUsername", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetAddConnection2A(jitter):
    mpr_WNetAddConnection2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetAddConnection2W(jitter):
    mpr_WNetAddConnection2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetAddConnection3(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetAddConnection3(HWND hwndOwner, LPNETRESOURCE lpNetResource, LPTSTR lpPassword, LPTSTR lpUserName, [ConnectFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "lpNetResource", "lpPassword", "lpUserName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetAddConnection3A(jitter):
    mpr_WNetAddConnection3(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetAddConnection3W(jitter):
    mpr_WNetAddConnection3(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetCancelConnection(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetCancelConnection(LPCTSTR lpName, BOOL fForce)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "fForce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetCancelConnectionA(jitter):
    mpr_WNetCancelConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetCancelConnectionW(jitter):
    mpr_WNetCancelConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetCancelConnection2(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetCancelConnection2(LPCTSTR lpName, [ConnectFlags] dwFlags, BOOL fForce)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "dwFlags", "fForce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetCancelConnection2A(jitter):
    mpr_WNetCancelConnection2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetCancelConnection2W(jitter):
    mpr_WNetCancelConnection2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetCloseEnum(jitter):
    """"
    [Mpr.dll] [ERROR_CODE] WNetCloseEnum(HANDLE hEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetConnectionDialog(jitter):
    """"
    [Mpr.dll] [ERROR_CODE] WNetConnectionDialog(HWND hwnd, [RESOURCETYPE] dwType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetConnectionDialog1(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetConnectionDialog1(LPCONNECTDLGSTRUCT lpConnDlgStruct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpConnDlgStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetConnectionDialog1A(jitter):
    mpr_WNetConnectionDialog1(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetConnectionDialog1W(jitter):
    mpr_WNetConnectionDialog1(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetDisconnectDialog(jitter):
    """"
    [Mpr.dll] [ERROR_CODE] WNetDisconnectDialog(HWND hwnd, [RESOURCETYPE] dwType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetDisconnectDialog1(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetDisconnectDialog1(LPDISCDLGSTRUCT lpConnDlgStruct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpConnDlgStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetDisconnectDialog1A(jitter):
    mpr_WNetDisconnectDialog1(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetDisconnectDialog1W(jitter):
    mpr_WNetDisconnectDialog1(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetEnumResource(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetEnumResource(HANDLE hEnum, LPDWORD lpcCount, LPNETRESOURCE lpBuffer, LPDWORD lpBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hEnum", "lpcCount", "lpBuffer", "lpBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetEnumResourceA(jitter):
    mpr_WNetEnumResource(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetEnumResourceW(jitter):
    mpr_WNetEnumResource(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetGetConnection(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetGetConnection(LPCTSTR lpLocalName, LPTSTR lpRemoteName, LPDWORD lpnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocalName", "lpRemoteName", "lpnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetGetConnectionA(jitter):
    mpr_WNetGetConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetGetConnectionW(jitter):
    mpr_WNetGetConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetGetLastError(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetGetLastError(LPDWORD lpError, LPTSTR lpErrorBuf, DWORD nErrorBufSize, LPTSTR lpNameBuf, DWORD nNameBufSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpError", "lpErrorBuf", "nErrorBufSize", "lpNameBuf", "nNameBufSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetGetLastErrorA(jitter):
    mpr_WNetGetLastError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetGetLastErrorW(jitter):
    mpr_WNetGetLastError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetGetNetworkInformation(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetGetNetworkInformation(LPCTSTR lpProvider, LPNETINFOSTRUCT lpNetInfoStruct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpProvider", "lpNetInfoStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetGetNetworkInformationA(jitter):
    mpr_WNetGetNetworkInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetGetNetworkInformationW(jitter):
    mpr_WNetGetNetworkInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetGetProviderName(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetGetProviderName(DWORD dwNetType, LPTSTR lpProviderName, LPDWORD lpBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwNetType", "lpProviderName", "lpBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetGetProviderNameA(jitter):
    mpr_WNetGetProviderName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetGetProviderNameW(jitter):
    mpr_WNetGetProviderName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetGetResourceInformation(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetGetResourceInformation(LPNETRESOURCE lpNetResource, LPVOID lpBuffer, LPDWORD lpcbBuffer, LPTSTR* lplpSystem)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNetResource", "lpBuffer", "lpcbBuffer", "lplpSystem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetGetResourceInformationA(jitter):
    mpr_WNetGetResourceInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetGetResourceInformationW(jitter):
    mpr_WNetGetResourceInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetGetResourceParent(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetGetResourceParent(LPNETRESOURCE lpNetResource, LPNETRESOURCE lpBuffer, LPDWORD lpcbBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpNetResource", "lpBuffer", "lpcbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetGetResourceParentA(jitter):
    mpr_WNetGetResourceParent(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetGetResourceParentW(jitter):
    mpr_WNetGetResourceParent(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetGetUniversalName(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetGetUniversalName(LPCTSTR lpLocalPath, [UniversalInfoLevel] dwInfoLevel, LPVOID lpBuffer, LPDWORD lpBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpLocalPath", "dwInfoLevel", "lpBuffer", "lpBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetGetUniversalNameA(jitter):
    mpr_WNetGetUniversalName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetGetUniversalNameW(jitter):
    mpr_WNetGetUniversalName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetGetUser(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetGetUser(LPCTSTR lpName, LPTSTR lpUserName, LPDWORD lpnLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpName", "lpUserName", "lpnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetGetUserA(jitter):
    mpr_WNetGetUser(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetGetUserW(jitter):
    mpr_WNetGetUser(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetOpenEnum(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetOpenEnum([ResourceScope] dwScope, [RESOURCETYPE] dwType, [RESOURCEUSAGE] dwUsage, LPNETRESOURCE lpNetResource, LPHANDLE lphEnum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwScope", "dwType", "dwUsage", "lpNetResource", "lphEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetOpenEnumA(jitter):
    mpr_WNetOpenEnum(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetOpenEnumW(jitter):
    mpr_WNetOpenEnum(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetRestoreConnectionW(jitter):
    """"
    [Mpr.dll] [ERROR_CODE] WNetRestoreConnectionW(HWND hwndParent, LPCWSTR lpDevice, BOOL fUseUI)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "lpDevice", "fUseUI"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetUseConnection(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetUseConnection(HWND hwndOwner, LPNETRESOURCE lpNetResource, LPCTSTR lpPassword, LPCTSTR lpUserID, [ConnectFlags] dwFlags, LPTSTR lpAccessName, LPDWORD lpBufferSize, LPDWORD lpResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "lpNetResource", "lpPassword", "lpUserID", "dwFlags", "lpAccessName", "lpBufferSize", "lpResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetUseConnectionA(jitter):
    mpr_WNetUseConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetUseConnectionW(jitter):
    mpr_WNetUseConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mpr_WNetAddConnection(jitter, get_str, set_str):
    """"
    [Mpr.dll] [ERROR_CODE] WNetAddConnection(LPCTSTR lpRemoteName, LPCTSTR lpPassword, LPCTSTR lpLocalName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpRemoteName", "lpPassword", "lpLocalName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mpr_WNetAddConnectionA(jitter):
    mpr_WNetAddConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mpr_WNetAddConnectionW(jitter):
    mpr_WNetAddConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
