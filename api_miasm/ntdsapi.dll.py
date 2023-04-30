_ScheduleType_ = {
    "SCHEDULE_INTERVAL": 0,
    "SCHEDULE_BANDWIDTH": 1,
    "SCHEDULE_PRIORITY": 2,
}
DS_REPSYNCALL_ERROR = {
    "DS_REPSYNCALL_WIN32_ERROR_CONTACTING_SERVER": 0,
    "DS_REPSYNCALL_WIN32_ERROR_REPLICATING": 1,
    "DS_REPSYNCALL_SERVER_UNREACHABLE": 2,
}
DS_NAME_FORMAT = {
    "DS_UNKNOWN_NAME": 0,
    "DS_FQDN_1779_NAME": 1,
    "DS_NT4_ACCOUNT_NAME": 2,
    "DS_DISPLAY_NAME": 3,
    "DS_DOMAIN_SIMPLE_NAME": 4,
    "DS_ENTERPRISE_SIMPLE_NAME": 5,
    "DS_UNIQUE_ID_NAME": 6,
    "DS_CANONICAL_NAME": 7,
    "DS_USER_PRINCIPAL_NAME": 8,
    "DS_CANONICAL_NAME_EX": 9,
    "DS_SERVICE_PRINCIPAL_NAME": 10,
    "DS_SID_OR_SID_HISTORY_NAME": 11,
    "DS_DNS_DOMAIN_NAME": 12,
}
DS_MANGLE_FOR = {
    "DS_MANGLE_UNKNOWN": 0,
    "DS_MANGLE_OBJECT_RDN_FOR_DELETION": 1,
    "DS_MANGLE_OBJECT_RDN_FOR_NAME_CONFLICT": 2,
}
DS_SPN_NAME_TYPE = {
    "DS_SPN_DNS_HOST": 0,
    "DS_SPN_DN_HOST": 1,
    "DS_SPN_NB_HOST": 2,
    "DS_SPN_DOMAIN": 3,
    "DS_SPN_NB_DOMAIN": 4,
    "DS_SPN_SERVICE": 5,
}
DS_KCC_TASKID = {
    "DS_KCC_TASKID_UPDATE_TOPOLOGY": 0,
}
DS_REPL_INFO_TYPE = {
    "DS_REPL_INFO_NEIGHBORS": 0,
    "DS_REPL_INFO_CURSORS_FOR_NC": 1,
    "DS_REPL_INFO_METADATA_FOR_OBJ": 2,
    "DS_REPL_INFO_KCC_DSA_CONNECT_FAILURES": 3,
    "DS_REPL_INFO_KCC_DSA_LINK_FAILURES": 4,
    "DS_REPL_INFO_PENDING_OPS": 5,
    "DS_REPL_INFO_METADATA_FOR_ATTR_VALUE": 6,
    "DS_REPL_INFO_CURSORS_2_FOR_NC": 7,
    "DS_REPL_INFO_CURSORS_3_FOR_NC": 8,
    "DS_REPL_INFO_METADATA_2_FOR_OBJ": 9,
    "DS_REPL_INFO_METADATA_2_FOR_ATTR_VALUE": 10,
}
DS_SPN_WRITE_OP = {
    "DS_SPN_ADD_SPN_OP": 0,
    "DS_SPN_REPLACE_SPN_OP": 1,
    "DS_SPN_DELETE_SPN_OP": 2,
}

def ntdsapi_DsAddSidHistory(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsAddSidHistory(
        HANDLE hDS,
        DWORD Flags,
        LPCTSTR SrcDomain,
        LPCTSTR SrcPrincipal,
        LPCTSTR SrcDomainController,
        RPC_AUTH_IDENTITY_HANDLE SrcDomainCreds,
        LPCTSTR DstDomain,
        LPCTSTR DstPrincipal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "Flags", "SrcDomain", "SrcPrincipal", "SrcDomainController", "SrcDomainCreds", "DstDomain", "DstPrincipal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsAddSidHistoryA(jitter):
    ntdsapi_DsAddSidHistory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsAddSidHistoryW(jitter):
    ntdsapi_DsAddSidHistory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsBind(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsBind(
        LPCTSTR DomainControllerName,
        LPCTSTR DnsDomainName,
        HANDLE* phDS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainControllerName", "DnsDomainName", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindA(jitter):
    ntdsapi_DsBind(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsBindW(jitter):
    ntdsapi_DsBind(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsBindingSetTimeout(jitter):
    """
    [ERROR_CODE] DsBindingSetTimeout(
        HANDLE hDS,
        ULONG cTimeoutSecs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "cTimeoutSecs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindToISTG(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsBindToISTG(
        LPCTSTR SiteName,
        HANDLE* phDS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SiteName", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindToISTGA(jitter):
    ntdsapi_DsBindToISTG(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsBindToISTGW(jitter):
    ntdsapi_DsBindToISTG(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsBindWithCred(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsBindWithCred(
        LPCTSTR DomainControllerName,
        LPCTSTR DnsDomainName,
        RPC_AUTH_IDENTITY_HANDLE AuthIdentity,
        HANDLE* phDS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainControllerName", "DnsDomainName", "AuthIdentity", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindWithCredA(jitter):
    ntdsapi_DsBindWithCred(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsBindWithCredW(jitter):
    ntdsapi_DsBindWithCred(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsBindWithSpn(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsBindWithSpn(
        LPCTSTR DomainControllerName,
        LPCTSTR DnsDomainName,
        RPC_AUTH_IDENTITY_HANDLE AuthIdentity,
        LPCTSTR ServicePrincipalName,
        HANDLE* phDS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainControllerName", "DnsDomainName", "AuthIdentity", "ServicePrincipalName", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindWithSpnA(jitter):
    ntdsapi_DsBindWithSpn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsBindWithSpnW(jitter):
    ntdsapi_DsBindWithSpn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsBindWithSpnEx(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsBindWithSpnEx(
        LPCTSTR DomainControllerName,
        LPCTSTR DnsDomainName,
        RPC_AUTH_IDENTITY_HANDLE AuthIdentity,
        LPCTSTR ServicePrincipalName,
        DWORD BindFlags,
        HANDLE* phDS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainControllerName", "DnsDomainName", "AuthIdentity", "ServicePrincipalName", "BindFlags", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindWithSpnExA(jitter):
    ntdsapi_DsBindWithSpnEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsBindWithSpnExW(jitter):
    ntdsapi_DsBindWithSpnEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsClientMakeSpnForTargetServer(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsClientMakeSpnForTargetServer(
        LPCTSTR ServiceClass,
        LPCTSTR ServiceName,
        DWORD* pcSpnLength,
        LPTSTR pszSpn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServiceClass", "ServiceName", "pcSpnLength", "pszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsClientMakeSpnForTargetServerA(jitter):
    ntdsapi_DsClientMakeSpnForTargetServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsClientMakeSpnForTargetServerW(jitter):
    ntdsapi_DsClientMakeSpnForTargetServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsCrackNames(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsCrackNames(
        HANDLE hDS,
        DS_NAME_FLAGS flags,
        DS_NAME_FORMAT formatOffered,
        DS_NAME_FORMAT formatDesired,
        DWORD cNames,
        LPCTSTR* rpNames,
        PDS_NAME_RESULT* ppResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "flags", "formatOffered", "formatDesired", "cNames", "rpNames", "ppResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsCrackNamesA(jitter):
    ntdsapi_DsCrackNames(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsCrackNamesW(jitter):
    ntdsapi_DsCrackNames(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsCrackSpn(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsCrackSpn(
        LPCTSTR pszSPN,
        DWORD* pcServiceClass,
        LPTSTR ServiceClass,
        DWORD* pcServiceName,
        LPTSTR ServiceName,
        DWORD* pcInstanceName,
        LPTSTR InstanceName,
        USHORT* pInstancePort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSPN", "pcServiceClass", "ServiceClass", "pcServiceName", "ServiceName", "pcInstanceName", "InstanceName", "pInstancePort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsCrackSpnA(jitter):
    ntdsapi_DsCrackSpn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsCrackSpnW(jitter):
    ntdsapi_DsCrackSpn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsCrackUnquotedMangledRdn(jitter, get_str, set_str):
    """
    BOOL DsCrackUnquotedMangledRdn(
        LPCTSTR pszRDN,
        DWORD cchRDN,
        GUID* pGuid,
        DS_MANGLE_FOR* peDsMangleFor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszRDN", "cchRDN", "pGuid", "peDsMangleFor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsCrackUnquotedMangledRdnA(jitter):
    ntdsapi_DsCrackUnquotedMangledRdn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsCrackUnquotedMangledRdnW(jitter):
    ntdsapi_DsCrackUnquotedMangledRdn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsFreeDomainControllerInfo(jitter, get_str, set_str):
    """
    void DsFreeDomainControllerInfo(
        DWORD InfoLevel,
        DWORD cInfo,
        VOID* pInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfoLevel", "cInfo", "pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeDomainControllerInfoA(jitter):
    ntdsapi_DsFreeDomainControllerInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsFreeDomainControllerInfoW(jitter):
    ntdsapi_DsFreeDomainControllerInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsFreeNameResult(jitter, get_str, set_str):
    """
    void DsFreeNameResult(
        DS_NAME_RESULT* pResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeNameResultA(jitter):
    ntdsapi_DsFreeNameResult(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsFreeNameResultW(jitter):
    ntdsapi_DsFreeNameResult(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsFreePasswordCredentials(jitter):
    """
    void DsFreePasswordCredentials(
        RPC_AUTH_IDENTITY_HANDLE AuthIdentity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeSchemaGuidMap(jitter, get_str, set_str):
    """
    void DsFreeSchemaGuidMap(
        PDS_SCHEMA_GUID_MAP pGuidMap
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGuidMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeSchemaGuidMapA(jitter):
    ntdsapi_DsFreeSchemaGuidMap(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsFreeSchemaGuidMapW(jitter):
    ntdsapi_DsFreeSchemaGuidMap(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsFreeSpnArray(jitter, get_str, set_str):
    """
    void DsFreeSpnArray(
        DWORD cSpn,
        LPTSTR* rpszSpn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cSpn", "rpszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeSpnArrayA(jitter):
    ntdsapi_DsFreeSpnArray(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsFreeSpnArrayW(jitter):
    ntdsapi_DsFreeSpnArray(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsGetDomainControllerInfo(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDomainControllerInfo(
        HANDLE hDs,
        LPTSTR DomainName,
        DWORD InfoLevel,
        DWORD* pcOut,
        VOID** ppInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "DomainName", "InfoLevel", "pcOut", "ppInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsGetDomainControllerInfoA(jitter):
    ntdsapi_DsGetDomainControllerInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsGetDomainControllerInfoW(jitter):
    ntdsapi_DsGetDomainControllerInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsGetRdnW(jitter):
    """
    [ERROR_CODE] DsGetRdnW(
        LPCWCH* ppDN,
        DWORD* pcDN,
        LPCWCH* ppKey,
        DWORD* pcKey,
        LPCWCH* ppVal,
        DWORD* pcVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppDN", "pcDN", "ppKey", "pcKey", "ppVal", "pcVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsGetSpn(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetSpn(
        DS_SPN_NAME_TYPE ServiceType,
        LPCTSTR ServiceClass,
        LPCTSTR ServiceName,
        USHORT InstancePort,
        USHORT cInstanceNames,
        LPCTSTR* pInstanceNames,
        const USHORT* pInstancePorts,
        DWORD* pcSpn,
        LPTSTR** prpszSpn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServiceType", "ServiceClass", "ServiceName", "InstancePort", "cInstanceNames", "pInstanceNames", "pInstancePorts", "pcSpn", "prpszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsGetSpnA(jitter):
    ntdsapi_DsGetSpn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsGetSpnW(jitter):
    ntdsapi_DsGetSpn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsInheritSecurityIdentity(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsInheritSecurityIdentity(
        HANDLE hDS,
        DWORD Flags,
        LPCTSTR SrcPrincipal,
        LPCTSTR DstPrincipal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "Flags", "SrcPrincipal", "DstPrincipal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsInheritSecurityIdentityA(jitter):
    ntdsapi_DsInheritSecurityIdentity(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsInheritSecurityIdentityW(jitter):
    ntdsapi_DsInheritSecurityIdentity(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsIsMangledDn(jitter, get_str, set_str):
    """
    BOOL DsIsMangledDn(
        LPCTSTR pszDn,
        DS_MANGLE_FOR eDsMangleFor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszDn", "eDsMangleFor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsIsMangledDnA(jitter):
    ntdsapi_DsIsMangledDn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsIsMangledDnW(jitter):
    ntdsapi_DsIsMangledDn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsIsMangledRdnValue(jitter, get_str, set_str):
    """
    BOOL DsIsMangledRdnValue(
        LPCTSTR pszRdn,
        DWORD cRdn,
        DS_MANGLE_FOR eDsMangleForDesired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszRdn", "cRdn", "eDsMangleForDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsIsMangledRdnValueA(jitter):
    ntdsapi_DsIsMangledRdnValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsIsMangledRdnValueW(jitter):
    ntdsapi_DsIsMangledRdnValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsListDomainsInSite(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsListDomainsInSite(
        HANDLE hDs,
        LPTSTR site,
        PDS_NAME_RESULT* ppDomains
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "site", "ppDomains"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListDomainsInSiteA(jitter):
    ntdsapi_DsListDomainsInSite(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsListDomainsInSiteW(jitter):
    ntdsapi_DsListDomainsInSite(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsListInfoForServer(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsListInfoForServer(
        HANDLE hDs,
        LPTSTR server,
        PDS_NAME_RESULT* ppInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "server", "ppInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListInfoForServerA(jitter):
    ntdsapi_DsListInfoForServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsListInfoForServerW(jitter):
    ntdsapi_DsListInfoForServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsListRoles(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsListRoles(
        HANDLE hDs,
        PDS_NAME_RESULT* ppRoles
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "ppRoles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListRolesA(jitter):
    ntdsapi_DsListRoles(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsListRolesW(jitter):
    ntdsapi_DsListRoles(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsListServersForDomainInSite(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsListServersForDomainInSite(
        HANDLE hDs,
        LPTSTR domain,
        LPTSTR site,
        PDS_NAME_RESULT* ppServers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "domain", "site", "ppServers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListServersForDomainInSiteA(jitter):
    ntdsapi_DsListServersForDomainInSite(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsListServersForDomainInSiteW(jitter):
    ntdsapi_DsListServersForDomainInSite(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsListServersInSite(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsListServersInSite(
        HANDLE hDs,
        LPTSTR site,
        PDS_NAME_RESULT* ppServers
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "site", "ppServers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListServersInSiteA(jitter):
    ntdsapi_DsListServersInSite(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsListServersInSiteW(jitter):
    ntdsapi_DsListServersInSite(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsListSites(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsListSites(
        HANDLE hDs,
        PDS_NAME_RESULT* ppSites
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "ppSites"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListSitesA(jitter):
    ntdsapi_DsListSites(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsListSitesW(jitter):
    ntdsapi_DsListSites(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsMakePasswordCredentials(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsMakePasswordCredentials(
        LPCTSTR User,
        LPCTSTR Domain,
        LPCTSTR Password,
        RPC_AUTH_IDENTITY_HANDLE* pAuthIdentity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["User", "Domain", "Password", "pAuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsMakePasswordCredentialsA(jitter):
    ntdsapi_DsMakePasswordCredentials(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsMakePasswordCredentialsW(jitter):
    ntdsapi_DsMakePasswordCredentials(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsMakeSpn(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsMakeSpn(
        LPCTSTR ServiceClass,
        LPCTSTR ServiceName,
        LPCTSTR InstanceName,
        USHORT InstancePort,
        LPCTSTR Referrer,
        DWORD* pcSpnLength,
        LPTSTR pszSpn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServiceClass", "ServiceName", "InstanceName", "InstancePort", "Referrer", "pcSpnLength", "pszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsMakeSpnA(jitter):
    ntdsapi_DsMakeSpn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsMakeSpnW(jitter):
    ntdsapi_DsMakeSpn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsMapSchemaGuids(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsMapSchemaGuids(
        HANDLE hDs,
        DWORD cGuids,
        GUID* rGuids,
        DS_SCHEMA_GUID_MAP** ppGuidMap
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "cGuids", "rGuids", "ppGuidMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsMapSchemaGuidsA(jitter):
    ntdsapi_DsMapSchemaGuids(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsMapSchemaGuidsW(jitter):
    ntdsapi_DsMapSchemaGuids(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsQuerySitesByCost(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsQuerySitesByCost(
        HANDLE hDS,
        LPTSTR pwszFromSite,
        LPTSTR* rgwszToSites,
        DWORD cToSites,
        DWORD dwFlags,
        PDS_SITE_COST_INFO* prgSiteInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "pwszFromSite", "rgwszToSites", "cToSites", "dwFlags", "prgSiteInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsQuerySitesByCostA(jitter):
    ntdsapi_DsQuerySitesByCost(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsQuerySitesByCostW(jitter):
    ntdsapi_DsQuerySitesByCost(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsQuerySitesFree(jitter):
    """
    void DsQuerySitesFree(
        PDS_SITE_COST_INFO rgSiteInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rgSiteInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsQuoteRdnValue(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsQuoteRdnValue(
        DWORD cUnquotedRdnValueLength,
        LPCTCH psUnquotedRdnValue,
        DWORD* pcQuotedRdnValueLength,
        LPTCH psQuotedRdnValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cUnquotedRdnValueLength", "psUnquotedRdnValue", "pcQuotedRdnValueLength", "psQuotedRdnValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsQuoteRdnValueA(jitter):
    ntdsapi_DsQuoteRdnValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsQuoteRdnValueW(jitter):
    ntdsapi_DsQuoteRdnValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsRemoveDsDomain(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsRemoveDsDomain(
        HANDLE hDs,
        LPTSTR DomainDN
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "DomainDN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsRemoveDsDomainA(jitter):
    ntdsapi_DsRemoveDsDomain(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsRemoveDsDomainW(jitter):
    ntdsapi_DsRemoveDsDomain(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsRemoveDsServer(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsRemoveDsServer(
        HANDLE hDs,
        LPTSTR ServerDN,
        LPTSTR DomainDN,
        BOOL* fLastDcInDomain,
        BOOL fCommit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDs", "ServerDN", "DomainDN", "fLastDcInDomain", "fCommit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsRemoveDsServerA(jitter):
    ntdsapi_DsRemoveDsServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsRemoveDsServerW(jitter):
    ntdsapi_DsRemoveDsServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsReplicaAdd(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsReplicaAdd(
        HANDLE hDS,
        LPCTSTR NameContext,
        LPCTSTR SourceDsaDn,
        LPCTSTR TransportDn,
        LPCTSTR SourceDsaAddress,
        const PSCHEDULE pSchedule,
        DWORD Options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "SourceDsaDn", "TransportDn", "SourceDsaAddress", "pSchedule", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaAddA(jitter):
    ntdsapi_DsReplicaAdd(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsReplicaAddW(jitter):
    ntdsapi_DsReplicaAdd(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsReplicaConsistencyCheck(jitter):
    """
    [ERROR_CODE] DsReplicaConsistencyCheck(
        HANDLE hDS,
        DS_KCC_TASKID TaskID,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "TaskID", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaDel(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsReplicaDel(
        HANDLE hDS,
        LPCTSTR NameContext,
        LPCTSTR DsaSrc,
        ULONG Options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "DsaSrc", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaDelA(jitter):
    ntdsapi_DsReplicaDel(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsReplicaDelW(jitter):
    ntdsapi_DsReplicaDel(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsReplicaFreeInfo(jitter):
    """
    void DsReplicaFreeInfo(
        DS_REPL_INFO_TYPE InfoType,
        VOID* pInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfoType", "pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaGetInfoW(jitter):
    """
    [ERROR_CODE] DsReplicaGetInfoW(
        HANDLE hDS,
        DS_REPL_INFO_TYPE InfoType,
        LPCWSTR pszObject,
        UUID* puuidForSourceDsaObjGuid,
        VOID** ppInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "InfoType", "pszObject", "puuidForSourceDsaObjGuid", "ppInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaGetInfo2W(jitter):
    """
    [ERROR_CODE] DsReplicaGetInfo2W(
        HANDLE hDS,
        DS_REPL_INFO_TYPE InfoType,
        LPCWSTR pszObject,
        UUID* puuidForSourceDsaObjGuid,
        LPCWSTR pszAttributeName,
        LPCWSTR pszValue,
        DWORD dwFlags,
        DWORD dwEnumerationContext,
        VOID** ppInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "InfoType", "pszObject", "puuidForSourceDsaObjGuid", "pszAttributeName", "pszValue", "dwFlags", "dwEnumerationContext", "ppInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaModify(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsReplicaModify(
        HANDLE hDS,
        LPCTSTR NameContext,
        const UUID* pUuidSourceDsa,
        LPCTSTR TransportDn,
        LPCTSTR SourceDsaAddress,
        const PSCHEDULE pSchedule,
        DWORD ReplicaFlags,
        DWORD ModifyFields,
        DWORD Options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "pUuidSourceDsa", "TransportDn", "SourceDsaAddress", "pSchedule", "ReplicaFlags", "ModifyFields", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaModifyA(jitter):
    ntdsapi_DsReplicaModify(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsReplicaModifyW(jitter):
    ntdsapi_DsReplicaModify(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsReplicaSync(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsReplicaSync(
        HANDLE hDS,
        LPCTSTR NameContext,
        const UUID* pUuidDsaSrc,
        ULONG Options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "pUuidDsaSrc", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaSyncA(jitter):
    ntdsapi_DsReplicaSync(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsReplicaSyncW(jitter):
    ntdsapi_DsReplicaSync(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsReplicaSyncAll(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsReplicaSyncAll(
        HANDLE hDS,
        LPTSTR pszNameContext,
        ULONG ulFlags,
        LPVOID pCallbackData,
        PDS_REPSYNCALL_ERRINFO** pErrors
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "pszNameContext", "ulFlags", "pCallbackData", "pErrors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaSyncAllA(jitter):
    ntdsapi_DsReplicaSyncAll(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsReplicaSyncAllW(jitter):
    ntdsapi_DsReplicaSyncAll(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsReplicaUpdateRefs(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsReplicaUpdateRefs(
        HANDLE hDS,
        LPCTSTR NameContext,
        LPCTSTR DsaDest,
        const UUID* pUuidDsaDest,
        ULONG Options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "DsaDest", "pUuidDsaDest", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaUpdateRefsA(jitter):
    ntdsapi_DsReplicaUpdateRefs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsReplicaUpdateRefsW(jitter):
    ntdsapi_DsReplicaUpdateRefs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsReplicaVerifyObjects(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsReplicaVerifyObjects(
        HANDLE hDS,
        LPCTSTR NameContext,
        const UUID* pUuidDsaSrc,
        ULONG ulOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "pUuidDsaSrc", "ulOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaVerifyObjectsA(jitter):
    ntdsapi_DsReplicaVerifyObjects(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsReplicaVerifyObjectsW(jitter):
    ntdsapi_DsReplicaVerifyObjects(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsServerRegisterSpn(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsServerRegisterSpn(
        DS_SPN_WRITE_OP Operation,
        LPCTSTR ServiceClass,
        LPCTSTR UserObjectDN
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Operation", "ServiceClass", "UserObjectDN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsServerRegisterSpnA(jitter):
    ntdsapi_DsServerRegisterSpn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsServerRegisterSpnW(jitter):
    ntdsapi_DsServerRegisterSpn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsUnBind(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsUnBind(
        HANDLE* phDS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsUnBindA(jitter):
    ntdsapi_DsUnBind(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsUnBindW(jitter):
    ntdsapi_DsUnBind(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsUnquoteRdnValue(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsUnquoteRdnValue(
        DWORD cQuotedRdnValueLength,
        LPCTCH psQuotedRdnValue,
        DWORD* pcUnquotedRdnValueLength,
        LPTCH psUnquotedRdnValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cQuotedRdnValueLength", "psQuotedRdnValue", "pcUnquotedRdnValueLength", "psUnquotedRdnValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsUnquoteRdnValueA(jitter):
    ntdsapi_DsUnquoteRdnValue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsUnquoteRdnValueW(jitter):
    ntdsapi_DsUnquoteRdnValue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdsapi_DsWriteAccountSpn(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsWriteAccountSpn(
        HANDLE hDS,
        DS_SPN_WRITE_OP Operation,
        LPCTSTR pszAccount,
        DWORD cSpn,
        LPCTSTR* rpszSpn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDS", "Operation", "pszAccount", "cSpn", "rpszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsWriteAccountSpnA(jitter):
    ntdsapi_DsWriteAccountSpn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdsapi_DsWriteAccountSpnW(jitter):
    ntdsapi_DsWriteAccountSpn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
