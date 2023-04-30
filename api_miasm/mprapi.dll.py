###### Enums ######

###################

###### Types ######
RAS_SERVER_HANDLE = HANDLE
MPR_SERVER_HANDLE = HANDLE
MPR_SERVER_HANDLE_PTR = Ptr("<I", MPR_SERVER_HANDLE())
MIB_SERVER_HANDLE = HANDLE
MIB_SERVER_HANDLE_PTR = Ptr("<I", MIB_SERVER_HANDLE())
WCHAR__MAX_INTERFACE_NAME_LEN_+_1_ = Array(WCHAR, 257)

class MPR_IPINIP_INTERFACE_0(MemStruct):
    fields = [
        ("wszFriendlyName", WCHAR__MAX_INTERFACE_NAME_LEN_+_1_()),
        ("Guid", GUID()),
    ]

PMPR_IPINIP_INTERFACE_0 = Ptr("<I", MPR_IPINIP_INTERFACE_0())

###################

###### Functions ######

def mprapi_MprAdminPortEnum(jitter):
    """
    [ERROR_CODE] MprAdminPortEnum(
        RAS_SERVER_HANDLE hRasServer,
        DWORD dwLevel,
        HANDLE hConnection,
        LPBYTE* lplpbBuffer,
        DWORD dwPrefMaxLen,
        LPDWORD lpdwEntriesRead,
        LPDWORD lpdwTotalEntries,
        LPDWORD lpdwResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasServer", "dwLevel", "hConnection", "lplpbBuffer", "dwPrefMaxLen", "lpdwEntriesRead", "lpdwTotalEntries", "lpdwResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminConnectionGetInfo(jitter):
    """
    [ERROR_CODE] MprAdminConnectionGetInfo(
        RAS_SERVER_HANDLE hRasServer,
        DWORD dwLevel,
        HANDLE hConnection,
        LPBYTE* lplpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasServer", "dwLevel", "hConnection", "lplpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminPortGetInfo(jitter):
    """
    [ERROR_CODE] MprAdminPortGetInfo(
        RAS_SERVER_HANDLE hRasServer,
        DWORD dwLevel,
        HANDLE hPort,
        LPBYTE* lplpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasServer", "dwLevel", "hPort", "lplpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminConnectionClearStats(jitter):
    """
    [ERROR_CODE] MprAdminConnectionClearStats(
        RAS_SERVER_HANDLE hRasServer,
        HANDLE hConnection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasServer", "hConnection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminPortClearStats(jitter):
    """
    [ERROR_CODE] MprAdminPortClearStats(
        RAS_SERVER_HANDLE hRasServer,
        HANDLE hPort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasServer", "hPort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminPortReset(jitter):
    """
    [ERROR_CODE] MprAdminPortReset(
        RAS_SERVER_HANDLE hRasServer,
        HANDLE hPort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasServer", "hPort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminPortDisconnect(jitter):
    """
    [ERROR_CODE] MprAdminPortDisconnect(
        RAS_SERVER_HANDLE hRasServer,
        HANDLE hPort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasServer", "hPort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminConnectionRemoveQuarantine(jitter):
    """
    [ERROR_CODE] MprAdminConnectionRemoveQuarantine(
        HANDLE hRasServer,
        HANDLE hRasConnection,
        BOOL fIsIpAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRasServer", "hRasConnection", "fIsIpAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminUserGetInfo(jitter):
    """
    [ERROR_CODE] MprAdminUserGetInfo(
        const WCHAR* lpszServer,
        const WCHAR* lpszUser,
        DWORD dwLevel,
        LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszServer", "lpszUser", "dwLevel", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminUserSetInfo(jitter):
    """
    [ERROR_CODE] MprAdminUserSetInfo(
        const WCHAR* lpszServer,
        const WCHAR* lpszUser,
        DWORD dwLevel,
        const LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszServer", "lpszUser", "dwLevel", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminSendUserMessage(jitter):
    """
    [ERROR_CODE] MprAdminSendUserMessage(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hConnection,
        LPWSTR lpwszMessage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hConnection", "lpwszMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminGetPDCServer(jitter):
    """
    [ERROR_CODE] MprAdminGetPDCServer(
        const WCHAR* lpszDomain,
        const WCHAR* lpszServer,
        LPWSTR lpszPDCServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpszDomain", "lpszServer", "lpszPDCServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminIsServiceRunning(jitter):
    """
    BOOL MprAdminIsServiceRunning(
        LPWSTR lpwsServerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwsServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminServerConnect(jitter):
    """
    [ERROR_CODE] MprAdminServerConnect(
        LPWSTR lpwsServerName,
        MPR_SERVER_HANDLE* phMprServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwsServerName", "phMprServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminServerDisconnect(jitter):
    """
    VOID MprAdminServerDisconnect(
        MPR_SERVER_HANDLE hMprServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminServerGetCredentials(jitter):
    """
    [ERROR_CODE] MprAdminServerGetCredentials(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwLevel,
        LPBYTE* lplpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwLevel", "lplpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminServerSetCredentials(jitter):
    """
    [ERROR_CODE] MprAdminServerSetCredentials(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwLevel,
        LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwLevel", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminBufferFree(jitter):
    """
    [ERROR_CODE] MprAdminBufferFree(
        LPVOID pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminGetErrorString(jitter):
    """
    [ERROR_CODE] MprAdminGetErrorString(
        DWORD dwError,
        LPWSTR* lpwsErrorString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwError", "lpwsErrorString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminServerGetInfo(jitter):
    """
    [ERROR_CODE] MprAdminServerGetInfo(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwLevel,
        LPBYTE* lplpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwLevel", "lplpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminServerSetInfo(jitter):
    """
    [ERROR_CODE] MprAdminServerSetInfo(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwLevel,
        LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwLevel", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminEstablishDomainRasServer(jitter):
    """
    [ERROR_CODE] MprAdminEstablishDomainRasServer(
        PWCHAR pszDomain,
        PWCHAR pszMachine,
        BOOL bEnable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDomain", "pszMachine", "bEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminIsDomainRasServer(jitter):
    """
    [ERROR_CODE] MprAdminIsDomainRasServer(
        PWCHAR pszDomain,
        PWCHAR pszMachine,
        PBOOL pbIsRasServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDomain", "pszMachine", "pbIsRasServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminTransportCreate(jitter):
    """
    [ERROR_CODE] MprAdminTransportCreate(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwTransportId,
        LPWSTR lpwsTransportName,
        LPBYTE pGlobalInfo,
        DWORD dwGlobalInfoSize,
        LPBYTE pClientInterfaceInfo,
        DWORD dwClientInterfaceInfoSize,
        LPWSTR lpwsDLLPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwTransportId", "lpwsTransportName", "pGlobalInfo", "dwGlobalInfoSize", "pClientInterfaceInfo", "dwClientInterfaceInfoSize", "lpwsDLLPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminTransportSetInfo(jitter):
    """
    [ERROR_CODE] MprAdminTransportSetInfo(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwTransportId,
        LPBYTE pGlobalInfo,
        DWORD dwGlobalInfoSize,
        LPBYTE pClientInterfaceInfo,
        DWORD dwClientInterfaceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwTransportId", "pGlobalInfo", "dwGlobalInfoSize", "pClientInterfaceInfo", "dwClientInterfaceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminTransportGetInfo(jitter):
    """
    [ERROR_CODE] MprAdminTransportGetInfo(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwTransportId,
        LPBYTE* ppGlobalInfo,
        LPDWORD lpdwGlobalInfoSize,
        LPBYTE* ppClientInterfaceInfo,
        LPDWORD lpdwClientInterfaceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwTransportId", "ppGlobalInfo", "lpdwGlobalInfoSize", "ppClientInterfaceInfo", "lpdwClientInterfaceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminDeviceEnum(jitter):
    """
    [ERROR_CODE] MprAdminDeviceEnum(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwLevel,
        LPBYTE* lplpbBuffer,
        LPDWORD lpdwTotalEntries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwLevel", "lplpbBuffer", "lpdwTotalEntries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceGetHandle(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceGetHandle(
        MPR_SERVER_HANDLE hMprServer,
        LPWSTR lpwsInterfaceName,
        HANDLE* phInterface,
        BOOL fIncludeClientInterfaces
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "lpwsInterfaceName", "phInterface", "fIncludeClientInterfaces"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceCreate(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceCreate(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwLevel,
        LPBYTE lpbBuffer,
        HANDLE* phInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwLevel", "lpbBuffer", "phInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceGetInfo(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceGetInfo(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwLevel,
        LPBYTE* lplpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwLevel", "lplpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceSetInfo(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceSetInfo(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwLevel,
        LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwLevel", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceDelete(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceDelete(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceDeviceGetInfo(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceDeviceGetInfo(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwIndex,
        DWORD dwLevel,
        LPBYTE* lplpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwIndex", "dwLevel", "lplpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceDeviceSetInfo(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceDeviceSetInfo(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwIndex,
        DWORD dwLevel,
        LPBYTE lplpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwIndex", "dwLevel", "lplpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceTransportRemove(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceTransportRemove(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwTransportId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwTransportId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceTransportAdd(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceTransportAdd(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwTransportId,
        LPBYTE pInterfaceInfo,
        DWORD dwInterfaceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwTransportId", "pInterfaceInfo", "dwInterfaceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceTransportGetInfo(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceTransportGetInfo(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwTransportId,
        LPBYTE* ppInterfaceInfo,
        LPDWORD lpdwpInterfaceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwTransportId", "ppInterfaceInfo", "lpdwpInterfaceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceTransportSetInfo(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceTransportSetInfo(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwTransportId,
        LPBYTE pInterfaceInfo,
        DWORD dwInterfaceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwTransportId", "pInterfaceInfo", "dwInterfaceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceEnum(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceEnum(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwLevel,
        LPBYTE* lplpbBuffer,
        DWORD dwPrefMaxLen,
        LPDWORD lpdwEntriesRead,
        LPDWORD lpdwTotalEntries,
        LPDWORD lpdwResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwLevel", "lplpbBuffer", "dwPrefMaxLen", "lpdwEntriesRead", "lpdwTotalEntries", "lpdwResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprSetupIpInIpInterfaceFriendlyNameEnum(jitter):
    """
    [ERROR_CODE] MprSetupIpInIpInterfaceFriendlyNameEnum(
        PWCHAR pwszMachineName,
        LPBYTE* lplpBuffer,
        LPDWORD lpdwEntriesRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszMachineName", "lplpBuffer", "lpdwEntriesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprSetupIpInIpInterfaceFriendlyNameFree(jitter):
    """
    [ERROR_CODE] MprSetupIpInIpInterfaceFriendlyNameFree(
        LPVOID lpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprSetupIpInIpInterfaceFriendlyNameCreate(jitter):
    """
    [ERROR_CODE] MprSetupIpInIpInterfaceFriendlyNameCreate(
        PWCHAR pwszMachineName,
        PMPR_IPINIP_INTERFACE_0 pNameInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszMachineName", "pNameInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprSetupIpInIpInterfaceFriendlyNameDelete(jitter):
    """
    [ERROR_CODE] MprSetupIpInIpInterfaceFriendlyNameDelete(
        PWCHAR pwszMachineName,
        GUID* pGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszMachineName", "pGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceSetCredentials(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceSetCredentials(
        LPWSTR lpwsServer,
        LPWSTR lpwsInterfaceName,
        LPWSTR lpwsUserName,
        LPWSTR lpwsDomainName,
        LPWSTR lpwsPassword
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwsServer", "lpwsInterfaceName", "lpwsUserName", "lpwsDomainName", "lpwsPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceGetCredentials(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceGetCredentials(
        LPWSTR lpwsServer,
        LPWSTR lpwsInterfaceName,
        LPWSTR lpwsUserName,
        LPWSTR lpwsPassword,
        LPWSTR lpwsDomainName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwsServer", "lpwsInterfaceName", "lpwsUserName", "lpwsPassword", "lpwsDomainName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceSetCredentialsEx(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceSetCredentialsEx(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwLevel,
        LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwLevel", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceGetCredentialsEx(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceGetCredentialsEx(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwLevel,
        LPBYTE* lplpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwLevel", "lplpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceConnect(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceConnect(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        HANDLE hEvent,
        BOOL fSynchronous
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "hEvent", "fSynchronous"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceDisconnect(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceDisconnect(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceUpdateRoutes(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceUpdateRoutes(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwProtocolId,
        HANDLE hEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwProtocolId", "hEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceQueryUpdateResult(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceQueryUpdateResult(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface,
        DWORD dwProtocolId,
        LPDWORD lpdwUpdateResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface", "dwProtocolId", "lpdwUpdateResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminInterfaceUpdatePhonebookInfo(jitter):
    """
    [ERROR_CODE] MprAdminInterfaceUpdatePhonebookInfo(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminRegisterConnectionNotification(jitter):
    """
    [ERROR_CODE] MprAdminRegisterConnectionNotification(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hEventNotification
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hEventNotification"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminDeregisterConnectionNotification(jitter):
    """
    [ERROR_CODE] MprAdminDeregisterConnectionNotification(
        MPR_SERVER_HANDLE hMprServer,
        HANDLE hEventNotification
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "hEventNotification"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBServerConnect(jitter):
    """
    [ERROR_CODE] MprAdminMIBServerConnect(
        LPWSTR lpwsServerName,
        MIB_SERVER_HANDLE* phMibServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwsServerName", "phMibServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBServerDisconnect(jitter):
    """
    VOID MprAdminMIBServerDisconnect(
        MIB_SERVER_HANDLE hMibServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMibServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBEntryCreate(jitter):
    """
    [ERROR_CODE] MprAdminMIBEntryCreate(
        MIB_SERVER_HANDLE hMibServer,
        DWORD dwPid,
        DWORD dwRoutingPid,
        LPVOID lpEntry,
        DWORD dwEntrySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMibServer", "dwPid", "dwRoutingPid", "lpEntry", "dwEntrySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBEntryDelete(jitter):
    """
    [ERROR_CODE] MprAdminMIBEntryDelete(
        MIB_SERVER_HANDLE hMibServer,
        DWORD dwProtocolId,
        DWORD dwRoutingPid,
        LPVOID lpEntry,
        DWORD dwEntrySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMibServer", "dwProtocolId", "dwRoutingPid", "lpEntry", "dwEntrySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBEntrySet(jitter):
    """
    [ERROR_CODE] MprAdminMIBEntrySet(
        MIB_SERVER_HANDLE hMibServer,
        DWORD dwProtocolId,
        DWORD dwRoutingPid,
        LPVOID lpEntry,
        DWORD dwEntrySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMibServer", "dwProtocolId", "dwRoutingPid", "lpEntry", "dwEntrySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBEntryGet(jitter):
    """
    [ERROR_CODE] MprAdminMIBEntryGet(
        MIB_SERVER_HANDLE hMibServer,
        DWORD dwProtocolId,
        DWORD dwRoutingPid,
        LPVOID lpInEntry,
        DWORD dwInEntrySize,
        LPVOID* lplpOutEntry,
        LPDWORD lpOutEntrySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMibServer", "dwProtocolId", "dwRoutingPid", "lpInEntry", "dwInEntrySize", "lplpOutEntry", "lpOutEntrySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBEntryGetFirst(jitter):
    """
    [ERROR_CODE] MprAdminMIBEntryGetFirst(
        MIB_SERVER_HANDLE hMibServer,
        DWORD dwProtocolId,
        DWORD dwRoutingPid,
        LPVOID lpInEntry,
        DWORD dwInEntrySize,
        LPVOID* lplpOutEntry,
        LPDWORD lpOutEntrySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMibServer", "dwProtocolId", "dwRoutingPid", "lpInEntry", "dwInEntrySize", "lplpOutEntry", "lpOutEntrySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBEntryGetNext(jitter):
    """
    [ERROR_CODE] MprAdminMIBEntryGetNext(
        MIB_SERVER_HANDLE hMibServer,
        DWORD dwProtocolId,
        DWORD dwRoutingPid,
        LPVOID lpInEntry,
        DWORD dwInEntrySize,
        LPVOID* lplpOutEntry,
        LPDWORD lpOutEntrySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMibServer", "dwProtocolId", "dwRoutingPid", "lpInEntry", "dwInEntrySize", "lplpOutEntry", "lpOutEntrySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBGetTrapInfo(jitter):
    """
    [ERROR_CODE] MprAdminMIBGetTrapInfo(
        MIB_SERVER_HANDLE hMibServer,
        DWORD dwProtocolId,
        DWORD dwRoutingPid,
        LPVOID lpInData,
        DWORD dwInDataSize,
        LPVOID* lplpOutData,
        LPDWORD lpOutDataSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMibServer", "dwProtocolId", "dwRoutingPid", "lpInData", "dwInDataSize", "lplpOutData", "lpOutDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBSetTrapInfo(jitter):
    """
    [ERROR_CODE] MprAdminMIBSetTrapInfo(
        DWORD dwProtocolId,
        DWORD dwRoutingPid,
        HANDLE hEvent,
        LPVOID lpInData,
        DWORD dwInDataSize,
        LPVOID* lplpOutData,
        LPDWORD lpOutDataSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwProtocolId", "dwRoutingPid", "hEvent", "lpInData", "dwInDataSize", "lplpOutData", "lpOutDataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprAdminMIBBufferFree(jitter):
    """
    [ERROR_CODE] MprAdminMIBBufferFree(
        LPVOID pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigServerInstall(jitter):
    """
    [ERROR_CODE] MprConfigServerInstall(
        DWORD dwLevel,
        PVOID pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwLevel", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigServerConnect(jitter):
    """
    [ERROR_CODE] MprConfigServerConnect(
        LPWSTR lpwsServerName,
        HANDLE* phMprConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpwsServerName", "phMprConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigServerDisconnect(jitter):
    """
    VOID MprConfigServerDisconnect(
        HANDLE hMprConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigServerRefresh(jitter):
    """
    [ERROR_CODE] MprConfigServerRefresh(
        HANDLE hMprConfig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigBufferFree(jitter):
    """
    [ERROR_CODE] MprConfigBufferFree(
        LPVOID pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigServerGetInfo(jitter):
    """
    [ERROR_CODE] MprConfigServerGetInfo(
        HANDLE hMprConfig,
        DWORD dwLevel,
        LPBYTE* lplpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "dwLevel", "lplpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigServerSetInfo(jitter):
    """
    [ERROR_CODE] MprConfigServerSetInfo(
        MPR_SERVER_HANDLE hMprServer,
        DWORD dwLevel,
        LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprServer", "dwLevel", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigServerBackup(jitter):
    """
    [ERROR_CODE] MprConfigServerBackup(
        HANDLE hMprConfig,
        LPWSTR lpwsPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "lpwsPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigServerRestore(jitter):
    """
    [ERROR_CODE] MprConfigServerRestore(
        HANDLE hMprConfig,
        LPWSTR lpwsPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "lpwsPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigTransportCreate(jitter):
    """
    [ERROR_CODE] MprConfigTransportCreate(
        HANDLE hMprConfig,
        DWORD dwTransportId,
        LPWSTR lpwsTransportName,
        LPBYTE pGlobalInfo,
        DWORD dwGlobalInfoSize,
        LPBYTE pClientInterfaceInfo,
        DWORD dwClientInterfaceInfoSize,
        LPWSTR lpwsDLLPath,
        HANDLE* phRouterTransport
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "dwTransportId", "lpwsTransportName", "pGlobalInfo", "dwGlobalInfoSize", "pClientInterfaceInfo", "dwClientInterfaceInfoSize", "lpwsDLLPath", "phRouterTransport"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigTransportDelete(jitter):
    """
    [ERROR_CODE] MprConfigTransportDelete(
        HANDLE hMprConfig,
        HANDLE hRouterTransport
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterTransport"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigTransportGetHandle(jitter):
    """
    [ERROR_CODE] MprConfigTransportGetHandle(
        HANDLE hMprConfig,
        DWORD dwTransportId,
        HANDLE* phRouterTransport
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "dwTransportId", "phRouterTransport"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigTransportSetInfo(jitter):
    """
    [ERROR_CODE] MprConfigTransportSetInfo(
        HANDLE hMprConfig,
        HANDLE hRouterTransport,
        LPBYTE pGlobalInfo,
        DWORD dwGlobalInfoSize,
        LPBYTE pClientInterfaceInfo,
        DWORD dwClientInterfaceInfoSize,
        LPWSTR lpwsDLLPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterTransport", "pGlobalInfo", "dwGlobalInfoSize", "pClientInterfaceInfo", "dwClientInterfaceInfoSize", "lpwsDLLPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigTransportGetInfo(jitter):
    """
    [ERROR_CODE] MprConfigTransportGetInfo(
        HANDLE hMprConfig,
        HANDLE hRouterTransport,
        LPBYTE* ppGlobalInfo,
        LPDWORD lpdwGlobalInfoSize,
        LPBYTE* ppClientInterfaceInfo,
        LPDWORD lpdwClientInterfaceInfoSize,
        LPWSTR* lplpwsDLLPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterTransport", "ppGlobalInfo", "lpdwGlobalInfoSize", "ppClientInterfaceInfo", "lpdwClientInterfaceInfoSize", "lplpwsDLLPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigTransportEnum(jitter):
    """
    [ERROR_CODE] MprConfigTransportEnum(
        HANDLE hMprConfig,
        DWORD dwLevel,
        LPBYTE* lplpBuffer,
        DWORD dwPrefMaxLen,
        LPDWORD lpdwEntriesRead,
        LPDWORD lpdwTotalEntries,
        LPDWORD lpdwResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "dwLevel", "lplpBuffer", "dwPrefMaxLen", "lpdwEntriesRead", "lpdwTotalEntries", "lpdwResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceCreate(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceCreate(
        HANDLE hMprConfig,
        DWORD dwLevel,
        LPBYTE lpbBuffer,
        HANDLE* phRouterInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "dwLevel", "lpbBuffer", "phRouterInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceDelete(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceDelete(
        HANDLE hMprConfig,
        HANDLE hRouterInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceGetHandle(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceGetHandle(
        HANDLE hMprConfig,
        LPWSTR lpwsInterfaceName,
        HANDLE* phRouterInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "lpwsInterfaceName", "phRouterInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceGetInfo(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceGetInfo(
        HANDLE hMprConfig,
        HANDLE hRouterInterface,
        DWORD dwLevel,
        LPBYTE* lplpBuffer,
        LPDWORD lpdwBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface", "dwLevel", "lplpBuffer", "lpdwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceSetInfo(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceSetInfo(
        HANDLE hMprConfig,
        HANDLE hRouterInterface,
        DWORD dwLevel,
        LPBYTE lpbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface", "dwLevel", "lpbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceEnum(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceEnum(
        HANDLE hMprConfig,
        DWORD dwLevel,
        LPBYTE* lplpBuffer,
        DWORD dwPrefMaxLen,
        LPDWORD lpdwEntriesRead,
        LPDWORD lpdwTotalEntries,
        LPDWORD lpdwResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "dwLevel", "lplpBuffer", "dwPrefMaxLen", "lpdwEntriesRead", "lpdwTotalEntries", "lpdwResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceTransportAdd(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceTransportAdd(
        HANDLE hMprConfig,
        HANDLE hRouterInterface,
        DWORD dwTransportId,
        LPWSTR lpwsTransportName,
        LPBYTE pInterfaceInfo,
        DWORD dwInterfaceInfoSize,
        HANDLE* phRouterIfTransport
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface", "dwTransportId", "lpwsTransportName", "pInterfaceInfo", "dwInterfaceInfoSize", "phRouterIfTransport"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceTransportRemove(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceTransportRemove(
        HANDLE hMprConfig,
        HANDLE hRouterInterface,
        HANDLE hRouterIfTransport
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface", "hRouterIfTransport"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceTransportGetHandle(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceTransportGetHandle(
        HANDLE hMprConfig,
        HANDLE hRouterInterface,
        DWORD dwTransportId,
        HANDLE* phRouterIfTransport
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface", "dwTransportId", "phRouterIfTransport"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceTransportGetInfo(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceTransportGetInfo(
        HANDLE hMprConfig,
        HANDLE hRouterInterface,
        HANDLE hRouterIfTransport,
        LPBYTE* ppInterfaceInfo,
        LPDWORD lpdwInterfaceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface", "hRouterIfTransport", "ppInterfaceInfo", "lpdwInterfaceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceTransportSetInfo(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceTransportSetInfo(
        HANDLE hMprConfig,
        HANDLE hRouterInterface,
        HANDLE hRouterIfTransport,
        LPBYTE pInterfaceInfo,
        DWORD dwInterfaceInfoSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface", "hRouterIfTransport", "pInterfaceInfo", "dwInterfaceInfoSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigInterfaceTransportEnum(jitter):
    """
    [ERROR_CODE] MprConfigInterfaceTransportEnum(
        HANDLE hMprConfig,
        HANDLE hRouterInterface,
        DWORD dwLevel,
        LPBYTE* lplpBuffer,
        DWORD dwPrefMaxLen,
        LPDWORD lpdwEntriesRead,
        LPDWORD lpdwTotalEntries,
        LPDWORD lpdwResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "hRouterInterface", "dwLevel", "lplpBuffer", "dwPrefMaxLen", "lpdwEntriesRead", "lpdwTotalEntries", "lpdwResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigGetFriendlyName(jitter):
    """
    [ERROR_CODE] MprConfigGetFriendlyName(
        HANDLE hMprConfig,
        PWCHAR pszGuidName,
        PWCHAR pszBuffer,
        DWORD dwBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "pszGuidName", "pszBuffer", "dwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigGetGuidName(jitter):
    """
    [ERROR_CODE] MprConfigGetGuidName(
        HANDLE hMprConfig,
        PWCHAR pszFriendlyName,
        PWCHAR pszBuffer,
        DWORD dwBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "pszFriendlyName", "pszBuffer", "dwBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigFilterGetInfo(jitter):
    """
    [ERROR_CODE] MprConfigFilterGetInfo(
        HANDLE hMprConfig,
        DWORD dwLevel,
        LPBYTE lpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "dwLevel", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprConfigFilterSetInfo(jitter):
    """
    [ERROR_CODE] MprConfigFilterSetInfo(
        HANDLE hMprConfig,
        DWORD dwLevel,
        LPBYTE lpBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMprConfig", "dwLevel", "lpBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoCreate(jitter):
    """
    [ERROR_CODE] MprInfoCreate(
        DWORD dwVersion,
        LPVOID* lplpNewHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwVersion", "lplpNewHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoDelete(jitter):
    """
    [ERROR_CODE] MprInfoDelete(
        LPVOID lpHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoRemoveAll(jitter):
    """
    [ERROR_CODE] MprInfoRemoveAll(
        LPVOID lpHeader,
        LPVOID* lplpNewHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHeader", "lplpNewHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoDuplicate(jitter):
    """
    [ERROR_CODE] MprInfoDuplicate(
        LPVOID lpHeader,
        LPVOID* lplpNewHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHeader", "lplpNewHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoBlockAdd(jitter):
    """
    [ERROR_CODE] MprInfoBlockAdd(
        LPVOID lpHeader,
        DWORD dwInfoType,
        DWORD dwItemSize,
        DWORD dwItemCount,
        LPBYTE lpItemData,
        LPVOID* lplpNewHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHeader", "dwInfoType", "dwItemSize", "dwItemCount", "lpItemData", "lplpNewHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoBlockRemove(jitter):
    """
    [ERROR_CODE] MprInfoBlockRemove(
        LPVOID lpHeader,
        DWORD dwInfoType,
        LPVOID* lplpNewHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHeader", "dwInfoType", "lplpNewHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoBlockSet(jitter):
    """
    [ERROR_CODE] MprInfoBlockSet(
        LPVOID lpHeader,
        DWORD dwInfoType,
        DWORD dwItemSize,
        DWORD dwItemCount,
        LPBYTE lpItemData,
        LPVOID* lplpNewHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHeader", "dwInfoType", "dwItemSize", "dwItemCount", "lpItemData", "lplpNewHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoBlockFind(jitter):
    """
    [ERROR_CODE] MprInfoBlockFind(
        LPVOID lpHeader,
        DWORD dwInfoType,
        LPDWORD lpdwItemSize,
        LPDWORD lpdwItemCount,
        LPBYTE* lplpItemData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHeader", "dwInfoType", "lpdwItemSize", "lpdwItemCount", "lplpItemData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mprapi_MprInfoBlockQuerySize(jitter):
    """
    DWORD MprInfoBlockQuerySize(
        LPVOID lpHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
