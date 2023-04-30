
def ntdsapi_DsAddSidHistory(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsAddSidHistory(HANDLE hDS, DWORD Flags, LPCTSTR SrcDomain, LPCTSTR SrcPrincipal, LPCTSTR SrcDomainController, RPC_AUTH_IDENTITY_HANDLE SrcDomainCreds, LPCTSTR DstDomain, LPCTSTR DstPrincipal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "Flags", "SrcDomain", "SrcPrincipal", "SrcDomainController", "SrcDomainCreds", "DstDomain", "DstPrincipal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBind(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsBind(LPCTSTR DomainControllerName, LPCTSTR DnsDomainName, HANDLE* phDS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DomainControllerName", "DnsDomainName", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindingSetTimeout(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsBindingSetTimeout(HANDLE hDS, ULONG cTimeoutSecs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "cTimeoutSecs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindToISTG(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsBindToISTG(LPCTSTR SiteName, HANDLE* phDS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SiteName", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindWithCred(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsBindWithCred(LPCTSTR DomainControllerName, LPCTSTR DnsDomainName, RPC_AUTH_IDENTITY_HANDLE AuthIdentity, HANDLE* phDS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DomainControllerName", "DnsDomainName", "AuthIdentity", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindWithSpn(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsBindWithSpn(LPCTSTR DomainControllerName, LPCTSTR DnsDomainName, RPC_AUTH_IDENTITY_HANDLE AuthIdentity, LPCTSTR ServicePrincipalName, HANDLE* phDS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DomainControllerName", "DnsDomainName", "AuthIdentity", "ServicePrincipalName", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsBindWithSpnEx(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsBindWithSpnEx(LPCTSTR DomainControllerName, LPCTSTR DnsDomainName, RPC_AUTH_IDENTITY_HANDLE AuthIdentity, LPCTSTR ServicePrincipalName, DWORD BindFlags, HANDLE* phDS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DomainControllerName", "DnsDomainName", "AuthIdentity", "ServicePrincipalName", "BindFlags", "phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsClientMakeSpnForTargetServer(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsClientMakeSpnForTargetServer(LPCTSTR ServiceClass, LPCTSTR ServiceName, DWORD* pcSpnLength, LPTSTR pszSpn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServiceClass", "ServiceName", "pcSpnLength", "pszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsCrackNames(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsCrackNames(HANDLE hDS, DS_NAME_FLAGS flags, DS_NAME_FORMAT formatOffered, DS_NAME_FORMAT formatDesired, DWORD cNames, LPCTSTR* rpNames, PDS_NAME_RESULT* ppResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "flags", "formatOffered", "formatDesired", "cNames", "rpNames", "ppResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsCrackSpn(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsCrackSpn(LPCTSTR pszSPN, DWORD* pcServiceClass, LPTSTR ServiceClass, DWORD* pcServiceName, LPTSTR ServiceName, DWORD* pcInstanceName, LPTSTR InstanceName, USHORT* pInstancePort)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszSPN", "pcServiceClass", "ServiceClass", "pcServiceName", "ServiceName", "pcInstanceName", "InstanceName", "pInstancePort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsCrackUnquotedMangledRdn(jitter):
    """"
    [NtDsAPI.dll] BOOL DsCrackUnquotedMangledRdn(LPCTSTR pszRDN, DWORD cchRDN, GUID* pGuid, DS_MANGLE_FOR* peDsMangleFor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszRDN", "cchRDN", "pGuid", "peDsMangleFor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeDomainControllerInfo(jitter):
    """"
    [NtDsAPI.dll] void DsFreeDomainControllerInfo(DWORD InfoLevel, DWORD cInfo, VOID* pInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfoLevel", "cInfo", "pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeNameResult(jitter):
    """"
    [NtDsAPI.dll] void DsFreeNameResult(DS_NAME_RESULT* pResult)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreePasswordCredentials(jitter):
    """"
    [NtDsAPI.dll] void DsFreePasswordCredentials(RPC_AUTH_IDENTITY_HANDLE AuthIdentity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeSchemaGuidMap(jitter):
    """"
    [NtDsAPI.dll] void DsFreeSchemaGuidMap(PDS_SCHEMA_GUID_MAP pGuidMap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGuidMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsFreeSpnArray(jitter):
    """"
    [NtDsAPI.dll] void DsFreeSpnArray(DWORD cSpn, LPTSTR* rpszSpn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cSpn", "rpszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsGetDomainControllerInfo(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsGetDomainControllerInfo(HANDLE hDs, LPTSTR DomainName, DWORD InfoLevel, DWORD* pcOut, VOID** ppInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "DomainName", "InfoLevel", "pcOut", "ppInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsGetRdnW(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsGetRdnW(LPCWCH* ppDN, DWORD* pcDN, LPCWCH* ppKey, DWORD* pcKey, LPCWCH* ppVal, DWORD* pcVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ppDN", "pcDN", "ppKey", "pcKey", "ppVal", "pcVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsGetSpn(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsGetSpn(DS_SPN_NAME_TYPE ServiceType, LPCTSTR ServiceClass, LPCTSTR ServiceName, USHORT InstancePort, USHORT cInstanceNames, LPCTSTR* pInstanceNames, const USHORT* pInstancePorts, DWORD* pcSpn, LPTSTR** prpszSpn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServiceType", "ServiceClass", "ServiceName", "InstancePort", "cInstanceNames", "pInstanceNames", "pInstancePorts", "pcSpn", "prpszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsInheritSecurityIdentity(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsInheritSecurityIdentity(HANDLE hDS, DWORD Flags, LPCTSTR SrcPrincipal, LPCTSTR DstPrincipal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "Flags", "SrcPrincipal", "DstPrincipal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsIsMangledDn(jitter):
    """"
    [NtDsAPI.dll] BOOL DsIsMangledDn(LPCTSTR pszDn, DS_MANGLE_FOR eDsMangleFor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszDn", "eDsMangleFor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsIsMangledRdnValue(jitter):
    """"
    [NtDsAPI.dll] BOOL DsIsMangledRdnValue(LPCTSTR pszRdn, DWORD cRdn, DS_MANGLE_FOR eDsMangleForDesired)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszRdn", "cRdn", "eDsMangleForDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListDomainsInSite(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsListDomainsInSite(HANDLE hDs, LPTSTR site, PDS_NAME_RESULT* ppDomains)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "site", "ppDomains"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListInfoForServer(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsListInfoForServer(HANDLE hDs, LPTSTR server, PDS_NAME_RESULT* ppInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "server", "ppInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListRoles(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsListRoles(HANDLE hDs, PDS_NAME_RESULT* ppRoles)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "ppRoles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListServersForDomainInSite(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsListServersForDomainInSite(HANDLE hDs, LPTSTR domain, LPTSTR site, PDS_NAME_RESULT* ppServers)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "domain", "site", "ppServers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListServersInSite(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsListServersInSite(HANDLE hDs, LPTSTR site, PDS_NAME_RESULT* ppServers)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "site", "ppServers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsListSites(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsListSites(HANDLE hDs, PDS_NAME_RESULT* ppSites)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "ppSites"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsMakePasswordCredentials(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsMakePasswordCredentials(LPCTSTR User, LPCTSTR Domain, LPCTSTR Password, RPC_AUTH_IDENTITY_HANDLE* pAuthIdentity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["User", "Domain", "Password", "pAuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsMakeSpn(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsMakeSpn(LPCTSTR ServiceClass, LPCTSTR ServiceName, LPCTSTR InstanceName, USHORT InstancePort, LPCTSTR Referrer, DWORD* pcSpnLength, LPTSTR pszSpn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServiceClass", "ServiceName", "InstanceName", "InstancePort", "Referrer", "pcSpnLength", "pszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsMapSchemaGuids(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsMapSchemaGuids(HANDLE hDs, DWORD cGuids, GUID* rGuids, DS_SCHEMA_GUID_MAP** ppGuidMap)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "cGuids", "rGuids", "ppGuidMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsQuerySitesByCost(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsQuerySitesByCost(HANDLE hDS, LPTSTR pwszFromSite, LPTSTR* rgwszToSites, DWORD cToSites, DWORD dwFlags, PDS_SITE_COST_INFO* prgSiteInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "pwszFromSite", "rgwszToSites", "cToSites", "dwFlags", "prgSiteInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsQuerySitesFree(jitter):
    """"
    [NtDsAPI.dll] void DsQuerySitesFree(PDS_SITE_COST_INFO rgSiteInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["rgSiteInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsQuoteRdnValue(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsQuoteRdnValue(DWORD cUnquotedRdnValueLength, LPCTCH psUnquotedRdnValue, DWORD* pcQuotedRdnValueLength, LPTCH psQuotedRdnValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cUnquotedRdnValueLength", "psUnquotedRdnValue", "pcQuotedRdnValueLength", "psQuotedRdnValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsRemoveDsDomain(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsRemoveDsDomain(HANDLE hDs, LPTSTR DomainDN)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "DomainDN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsRemoveDsServer(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsRemoveDsServer(HANDLE hDs, LPTSTR ServerDN, LPTSTR DomainDN, BOOL* fLastDcInDomain, BOOL fCommit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDs", "ServerDN", "DomainDN", "fLastDcInDomain", "fCommit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaAdd(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaAdd(HANDLE hDS, LPCTSTR NameContext, LPCTSTR SourceDsaDn, LPCTSTR TransportDn, LPCTSTR SourceDsaAddress, const PSCHEDULE pSchedule, DWORD Options)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "SourceDsaDn", "TransportDn", "SourceDsaAddress", "pSchedule", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaConsistencyCheck(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaConsistencyCheck(HANDLE hDS, DS_KCC_TASKID TaskID, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "TaskID", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaDel(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaDel(HANDLE hDS, LPCTSTR NameContext, LPCTSTR DsaSrc, ULONG Options)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "DsaSrc", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaFreeInfo(jitter):
    """"
    [NtDsAPI.dll] void DsReplicaFreeInfo(DS_REPL_INFO_TYPE InfoType, VOID* pInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfoType", "pInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaGetInfoW(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaGetInfoW(HANDLE hDS, DS_REPL_INFO_TYPE InfoType, LPCWSTR pszObject, UUID* puuidForSourceDsaObjGuid, VOID** ppInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "InfoType", "pszObject", "puuidForSourceDsaObjGuid", "ppInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaGetInfo2W(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaGetInfo2W(HANDLE hDS, DS_REPL_INFO_TYPE InfoType, LPCWSTR pszObject, UUID* puuidForSourceDsaObjGuid, LPCWSTR pszAttributeName, LPCWSTR pszValue, DWORD dwFlags, DWORD dwEnumerationContext, VOID** ppInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "InfoType", "pszObject", "puuidForSourceDsaObjGuid", "pszAttributeName", "pszValue", "dwFlags", "dwEnumerationContext", "ppInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaModify(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaModify(HANDLE hDS, LPCTSTR NameContext, const UUID* pUuidSourceDsa, LPCTSTR TransportDn, LPCTSTR SourceDsaAddress, const PSCHEDULE pSchedule, DWORD ReplicaFlags, DWORD ModifyFields, DWORD Options)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "pUuidSourceDsa", "TransportDn", "SourceDsaAddress", "pSchedule", "ReplicaFlags", "ModifyFields", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaSync(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaSync(HANDLE hDS, LPCTSTR NameContext, const UUID* pUuidDsaSrc, ULONG Options)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "pUuidDsaSrc", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaSyncAll(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaSyncAll(HANDLE hDS, LPTSTR pszNameContext, ULONG ulFlags, LPVOID pCallbackData, PDS_REPSYNCALL_ERRINFO** pErrors)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "pszNameContext", "ulFlags", "pCallbackData", "pErrors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaUpdateRefs(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaUpdateRefs(HANDLE hDS, LPCTSTR NameContext, LPCTSTR DsaDest, const UUID* pUuidDsaDest, ULONG Options)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "DsaDest", "pUuidDsaDest", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsReplicaVerifyObjects(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsReplicaVerifyObjects(HANDLE hDS, LPCTSTR NameContext, const UUID* pUuidDsaSrc, ULONG ulOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "NameContext", "pUuidDsaSrc", "ulOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsServerRegisterSpn(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsServerRegisterSpn(DS_SPN_WRITE_OP Operation, LPCTSTR ServiceClass, LPCTSTR UserObjectDN)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Operation", "ServiceClass", "UserObjectDN"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsUnBind(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsUnBind(HANDLE* phDS)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phDS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsUnquoteRdnValue(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsUnquoteRdnValue(DWORD cQuotedRdnValueLength, LPCTCH psQuotedRdnValue, DWORD* pcUnquotedRdnValueLength, LPTCH psUnquotedRdnValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cQuotedRdnValueLength", "psQuotedRdnValue", "pcUnquotedRdnValueLength", "psUnquotedRdnValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdsapi_DsWriteAccountSpn(jitter):
    """"
    [NtDsAPI.dll] [ERROR_CODE] DsWriteAccountSpn(HANDLE hDS, DS_SPN_WRITE_OP Operation, LPCTSTR pszAccount, DWORD cSpn, LPCTSTR* rpszSpn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hDS", "Operation", "pszAccount", "cSpn", "rpszSpn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
