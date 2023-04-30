
def netapi32_DsAddressToSiteNames(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsAddressToSiteNames(
        LPCTSTR ComputerName,
        DWORD EntryCount,
        PSOCKET_ADDRESS SocketAddresses,
        LPTSTR** SiteNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerName", "EntryCount", "SocketAddresses", "SiteNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsAddressToSiteNamesA(jitter):
    netapi32_DsAddressToSiteNames(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsAddressToSiteNamesW(jitter):
    netapi32_DsAddressToSiteNames(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsAddressToSiteNamesEx(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsAddressToSiteNamesEx(
        LPCTSTR ComputerName,
        DWORD EntryCount,
        PSOCKET_ADDRESS SocketAddresses,
        LPTSTR** SiteNames,
        LPTSTR** SubnetNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerName", "EntryCount", "SocketAddresses", "SiteNames", "SubnetNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsAddressToSiteNamesExA(jitter):
    netapi32_DsAddressToSiteNamesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsAddressToSiteNamesExW(jitter):
    netapi32_DsAddressToSiteNamesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsDeregisterDnsHostRecords(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsDeregisterDnsHostRecords(
        LPTSTR ServerName,
        LPTSTR DnsDomainName,
        GUID* DomainGuid,
        GUID* DsaGuid,
        LPTSTR DnsHostName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "DnsDomainName", "DomainGuid", "DsaGuid", "DnsHostName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsDeregisterDnsHostRecordsA(jitter):
    netapi32_DsDeregisterDnsHostRecords(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsDeregisterDnsHostRecordsW(jitter):
    netapi32_DsDeregisterDnsHostRecords(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsEnumerateDomainTrusts(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsEnumerateDomainTrusts(
        LPTSTR ServerName,
        ULONG Flags,
        PDS_DOMAIN_TRUSTS* Domains,
        PULONG DomainCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Flags", "Domains", "DomainCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsEnumerateDomainTrustsA(jitter):
    netapi32_DsEnumerateDomainTrusts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsEnumerateDomainTrustsW(jitter):
    netapi32_DsEnumerateDomainTrusts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetDcCloseW(jitter):
    """
    void DsGetDcCloseW(
        HANDLE GetDcContextHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["GetDcContextHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcName(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDcName(
        LPCTSTR ComputerName,
        LPCTSTR DomainName,
        GUID* DomainGuid,
        LPCTSTR SiteName,
        [DsGetDcNameFlags] Flags,
        PDOMAIN_CONTROLLER_INFO* DomainControllerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerName", "DomainName", "DomainGuid", "SiteName", "Flags", "DomainControllerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcNameA(jitter):
    netapi32_DsGetDcName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetDcNameW(jitter):
    netapi32_DsGetDcName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetDcNext(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDcNext(
        HANDLE GetDcContextHandle,
        PULONG SockAddressCount,
        LPSOCKET_ADDRESS* SockAddresses,
        LPTSTR* DnsHostName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["GetDcContextHandle", "SockAddressCount", "SockAddresses", "DnsHostName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcNextA(jitter):
    netapi32_DsGetDcNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetDcNextW(jitter):
    netapi32_DsGetDcNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetDcOpen(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDcOpen(
        LPCTSTR DnsName,
        ULONG OptionFlags,
        LPCTSTR SiteName,
        GUID* DomainGuid,
        LPCTSTR DnsForestName,
        ULONG DcFlags,
        PHANDLE RetGetDcContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DnsName", "OptionFlags", "SiteName", "DomainGuid", "DnsForestName", "DcFlags", "RetGetDcContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcOpenA(jitter):
    netapi32_DsGetDcOpen(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetDcOpenW(jitter):
    netapi32_DsGetDcOpen(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetDcSiteCoverage(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDcSiteCoverage(
        LPCTSTR ServerName,
        PULONG EntryCount,
        LPTSTR** SiteNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "EntryCount", "SiteNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcSiteCoverageA(jitter):
    netapi32_DsGetDcSiteCoverage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetDcSiteCoverageW(jitter):
    netapi32_DsGetDcSiteCoverage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetForestTrustInformationW(jitter):
    """
    [ERROR_CODE] DsGetForestTrustInformationW(
        LPCWSTR ServerName,
        LPCWSTR TrustedDomainName,
        DWORD Flags,
        PLSA_FOREST_TRUST_INFORMATION* ForestTrustInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "TrustedDomainName", "Flags", "ForestTrustInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetSiteName(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetSiteName(
        LPCTSTR ComputerName,
        LPTSTR* SiteName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerName", "SiteName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetSiteNameA(jitter):
    netapi32_DsGetSiteName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetSiteNameW(jitter):
    netapi32_DsGetSiteName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsMergeForestTrustInformationW(jitter):
    """
    void DsMergeForestTrustInformationW(
        LPCWSTR DomainName,
        PLSA_FOREST_TRUST_INFORMATION NewForestTrustInfo,
        PLSA_FOREST_TRUST_INFORMATION OldForestTrustInfo,
        PLSA_FOREST_TRUST_INFORMATION* ForestTrustInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainName", "NewForestTrustInfo", "OldForestTrustInfo", "ForestTrustInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsRoleFreeMemory(jitter):
    """
    void DsRoleFreeMemory(
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsRoleGetPrimaryDomainInformation(jitter):
    """
    [ERROR_CODE] DsRoleGetPrimaryDomainInformation(
        LPCWSTR lpServer,
        DSROLE_PRIMARY_DOMAIN_INFO_LEVEL InfoLevel,
        PBYTE* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "InfoLevel", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsValidateSubnetName(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsValidateSubnetName(
        LPCTSTR SubnetName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubnetName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsValidateSubnetNameA(jitter):
    netapi32_DsValidateSubnetName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsValidateSubnetNameW(jitter):
    netapi32_DsValidateSubnetName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_NetAlertRaise(jitter):
    """
    NET_API_STATUS NetAlertRaise(
        LPCWSTR AlertEventName,
        LPVOID Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AlertEventName", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAlertRaiseEx(jitter):
    """
    NET_API_STATUS NetAlertRaiseEx(
        LPCWSTR AlertEventName,
        LPVOID VariableInfo,
        DWORD VariableInfoSize,
        LPCWSTR ServiceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AlertEventName", "VariableInfo", "VariableInfoSize", "ServiceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetapipBufferAllocate(jitter):
    """
    NET_API_STATUS NetapipBufferAllocate(
        DWORD ByteCount,
        LPVOID* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ByteCount", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetApiBufferAllocate(jitter):
    """
    NET_API_STATUS NetApiBufferAllocate(
        DWORD ByteCount,
        LPVOID* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ByteCount", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetApiBufferFree(jitter):
    """
    NET_API_STATUS NetApiBufferFree(
        LPVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetApiBufferReallocate(jitter):
    """
    NET_API_STATUS NetApiBufferReallocate(
        LPVOID OldBuffer,
        DWORD NewByteCount,
        LPVOID* NewBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OldBuffer", "NewByteCount", "NewBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetApiBufferSize(jitter):
    """
    NET_API_STATUS NetApiBufferSize(
        LPVOID Buffer,
        LPDWORD ByteCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "ByteCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAddAlternateComputerName(jitter):
    """
    NET_API_STATUS NetAddAlternateComputerName(
        LPCWSTR Server,
        LPCWSTR AlternateName,
        LPCWSTR DomainAccount,
        LPCWSTR DomainAccountPassword,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Server", "AlternateName", "DomainAccount", "DomainAccountPassword", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetEnumerateComputerNames(jitter):
    """
    NET_API_STATUS NetEnumerateComputerNames(
        LPCWSTR Server,
        NET_COMPUTER_NAME_TYPE NameType,
        ULONG Reserved,
        PDWORD EntryCount,
        LPWSTR** ComputerNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Server", "NameType", "Reserved", "EntryCount", "ComputerNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetJoinableOUs(jitter):
    """
    NET_API_STATUS NetGetJoinableOUs(
        LPCWSTR lpServer,
        LPCWSTR lpDomain,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        DWORD* OUCount,
        LPWSTR** OUs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpDomain", "lpAccount", "lpPassword", "OUCount", "OUs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetJoinInformation(jitter):
    """
    NET_API_STATUS NetGetJoinInformation(
        LPCWSTR lpServer,
        LPWSTR* lpNameBuffer,
        PNETSETUP_JOIN_STATUS BufferType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpNameBuffer", "BufferType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetJoinDomain(jitter):
    """
    NET_API_STATUS NetJoinDomain(
        LPCWSTR lpServer,
        LPCWSTR lpDomain,
        LPCWSTR lpAccountOU,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        DWORD fJoinOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpDomain", "lpAccountOU", "lpAccount", "lpPassword", "fJoinOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLogonSetServiceBits(jitter):
    """
    NET_API_STATUS NetLogonSetServiceBits(
        LPWSTR ServerName,
        DWORD ServiceBitsOfInterest,
        DWORD ServiceBits
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "ServiceBitsOfInterest", "ServiceBits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetProvisionComputerAccount(jitter):
    """
    NET_API_STATUS NetProvisionComputerAccount(
        LPCWSTR lpDomain,
        LPCWSTR lpMachineName,
        LPCWSTR lpMachineAccountOU,
        LPCWSTR lpDcName,
        [NETSETUP_PROVISION_OPTIONS] dwOptions,
        PBYTE pProvisionBinData,
        DWORD pdwProvisionBinDataSize,
        LPWSTR pProvisionTextData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpDomain", "lpMachineName", "lpMachineAccountOU", "lpDcName", "dwOptions", "pProvisionBinData", "pdwProvisionBinDataSize", "pProvisionTextData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRemoveAlternateComputerName(jitter):
    """
    NET_API_STATUS NetRemoveAlternateComputerName(
        LPCWSTR Server,
        LPCWSTR AlternateName,
        LPCWSTR DomainAccount,
        LPCWSTR DomainAccountPassword,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Server", "AlternateName", "DomainAccount", "DomainAccountPassword", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRenameMachineInDomain(jitter):
    """
    NET_API_STATUS NetRenameMachineInDomain(
        LPCWSTR lpServer,
        LPCWSTR lpNewMachineName,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        DWORD fRenameOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpNewMachineName", "lpAccount", "lpPassword", "fRenameOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRequestOfflineDomainJoin(jitter):
    """
    NET_API_STATUS NetRequestOfflineDomainJoin(
        BYTE* pProvisionBinData,
        DWORD cbProvisionBinDataSize,
        DWORD dwOptions,
        LPCWSTR lpWindowsPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProvisionBinData", "cbProvisionBinDataSize", "dwOptions", "lpWindowsPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetSetPrimaryComputerName(jitter):
    """
    NET_API_STATUS NetSetPrimaryComputerName(
        LPCWSTR Server,
        LPCWSTR PrimaryName,
        LPCWSTR DomainAccount,
        LPCWSTR DomainAccountPassword,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Server", "PrimaryName", "DomainAccount", "DomainAccountPassword", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUnjoinDomain(jitter):
    """
    NET_API_STATUS NetUnjoinDomain(
        LPCWSTR lpServer,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        DWORD fUnjoinOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpAccount", "lpPassword", "fUnjoinOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetValidateName(jitter):
    """
    NET_API_STATUS NetValidateName(
        LPCWSTR lpServer,
        LPCWSTR lpName,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        NETSETUP_NAME_TYPE NameType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpName", "lpAccount", "lpPassword", "NameType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetCreateProvisioningPackage(jitter):
    """
    NET_API_STATUS NetCreateProvisioningPackage(
        PNETSETUP_PROVISIONING_PARAMS pProvisioningParams,
        PBYTE* pPackageBinData,
        DWORD* pdwPackageBinDataSize,
        LPWSTR* pPackageTextData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProvisioningParams", "pPackageBinData", "pdwPackageBinDataSize", "pPackageTextData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRequestProvisioningPackageInstall(jitter):
    """
    NET_API_STATUS NetRequestProvisioningPackageInstall(
        BYTE* pPackageBinData,
        DWORD dwPackageBinDataSize,
        DWORD dwProvisionOptions,
        LPCWSTR lpWindowsPath,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPackageBinData", "dwPackageBinDataSize", "dwProvisionOptions", "lpWindowsPath", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetAnyDCName(jitter):
    """
    NET_API_STATUS NetGetAnyDCName(
        LPCWSTR servername,
        LPCWSTR domainname,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "domainname", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetDCName(jitter):
    """
    NET_API_STATUS NetGetDCName(
        LPCWSTR servername,
        LPCWSTR domainname,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "domainname", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetDisplayInformationIndex(jitter):
    """
    NET_API_STATUS NetGetDisplayInformationIndex(
        LPCWSTR ServerName,
        DWORD Level,
        LPCWSTR Prefix,
        LPDWORD Index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Level", "Prefix", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetQueryDisplayInformation(jitter):
    """
    NET_API_STATUS NetQueryDisplayInformation(
        LPCWSTR ServerName,
        DWORD Level,
        DWORD Index,
        DWORD EntriesRequested,
        DWORD PreferredMaximumLength,
        LPDWORD ReturnedEntryCount,
        PVOID* SortedBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Level", "Index", "EntriesRequested", "PreferredMaximumLength", "ReturnedEntryCount", "SortedBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupAdd(jitter):
    """
    NET_API_STATUS NetGroupAdd(
        LPCWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupAddUser(jitter):
    """
    NET_API_STATUS NetGroupAddUser(
        LPCWSTR servername,
        LPCWSTR GroupName,
        LPCWSTR username
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "GroupName", "username"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupDel(jitter):
    """
    NET_API_STATUS NetGroupDel(
        LPCWSTR servername,
        LPCWSTR groupname
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupDelUser(jitter):
    """
    NET_API_STATUS NetGroupDelUser(
        LPCWSTR servername,
        LPCWSTR GroupName,
        LPCWSTR Username
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "GroupName", "Username"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupEnum(jitter):
    """
    NET_API_STATUS NetGroupEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupGetInfo(jitter):
    """
    NET_API_STATUS NetGroupGetInfo(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupGetUsers(jitter):
    """
    NET_API_STATUS NetGroupGetUsers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR ResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "ResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupSetInfo(jitter):
    """
    NET_API_STATUS NetGroupSetInfo(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupSetUsers(jitter):
    """
    NET_API_STATUS NetGroupSetUsers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        DWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupAdd(jitter):
    """
    NET_API_STATUS NetLocalGroupAdd(
        LPCWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupAddMembers(jitter):
    """
    NET_API_STATUS NetLocalGroupAddMembers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        DWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupDel(jitter):
    """
    NET_API_STATUS NetLocalGroupDel(
        LPCWSTR servername,
        LPCWSTR groupname
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupDelMembers(jitter):
    """
    NET_API_STATUS NetLocalGroupDelMembers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        DWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupEnum(jitter):
    """
    NET_API_STATUS NetLocalGroupEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupGetInfo(jitter):
    """
    NET_API_STATUS NetLocalGroupGetInfo(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupGetMembers(jitter):
    """
    NET_API_STATUS NetLocalGroupGetMembers(
        LPCWSTR servername,
        LPCWSTR localgroupname,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "localgroupname", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupSetInfo(jitter):
    """
    NET_API_STATUS NetLocalGroupSetInfo(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupSetMembers(jitter):
    """
    NET_API_STATUS NetLocalGroupSetMembers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        DWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageBufferSend(jitter):
    """
    NET_API_STATUS NetMessageBufferSend(
        LPCWSTR servername,
        LPCWSTR msgname,
        LPCWSTR fromname,
        LPBYTE buf,
        DWORD buflen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "msgname", "fromname", "buf", "buflen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageNameAdd(jitter):
    """
    NET_API_STATUS NetMessageNameAdd(
        LPCWSTR servername,
        LPCWSTR msgname
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "msgname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageNameDel(jitter):
    """
    NET_API_STATUS NetMessageNameDel(
        LPCWSTR servername,
        LPCWSTR msgname
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "msgname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageNameEnum(jitter):
    """
    NET_API_STATUS NetMessageNameEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageNameGetInfo(jitter):
    """
    NET_API_STATUS NetMessageNameGetInfo(
        LPCWSTR servername,
        LPCWSTR msgname,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "msgname", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRemoteComputerSupports(jitter):
    """
    NET_API_STATUS NetRemoteComputerSupports(
        LPCWSTR UncServerName,
        DWORD OptionsWanted,
        LPDWORD OptionsSupported
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "OptionsWanted", "OptionsSupported"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRemoteTOD(jitter):
    """
    NET_API_STATUS NetRemoteTOD(
        LPCWSTR UncServerName,
        LPBYTE* BufferPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "BufferPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetScheduleJobAdd(jitter):
    """
    NET_API_STATUS NetScheduleJobAdd(
        LPCWSTR Servername,
        LPBYTE Buffer,
        LPDWORD JobId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Servername", "Buffer", "JobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetScheduleJobDel(jitter):
    """
    NET_API_STATUS NetScheduleJobDel(
        LPCWSTR Servername,
        DWORD MinJobId,
        DWORD MaxJobId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Servername", "MinJobId", "MaxJobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetScheduleJobEnum(jitter):
    """
    NET_API_STATUS NetScheduleJobEnum(
        LPCWSTR Servername,
        LPBYTE* PointerToBuffer,
        DWORD PreferredMaximumLength,
        LPDWORD EntriesRead,
        LPDWORD TotalEntries,
        LPDWORD ResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Servername", "PointerToBuffer", "PreferredMaximumLength", "EntriesRead", "TotalEntries", "ResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetScheduleJobGetInfo(jitter):
    """
    NET_API_STATUS NetScheduleJobGetInfo(
        LPCWSTR Servername,
        DWORD JobId,
        LPBYTE* PointerToBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Servername", "JobId", "PointerToBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerDiskEnum(jitter):
    """
    NET_API_STATUS NetServerDiskEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerEnum(jitter):
    """
    NET_API_STATUS NetServerEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        [ServerType] servertype,
        LPCWSTR domain,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "servertype", "domain", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerEnumEx(jitter):
    """
    NET_API_STATUS NetServerEnumEx(
        LPCWSTR ServerName,
        DWORD Level,
        LPBYTE* Bufptr,
        DWORD PrefMaxlen,
        LPDWORD EntriesRead,
        LPDWORD totalentries,
        [ServerType] servertype,
        LPCWSTR domain,
        LPCWSTR FirstNameToReturn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Level", "Bufptr", "PrefMaxlen", "EntriesRead", "totalentries", "servertype", "domain", "FirstNameToReturn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerGetInfo(jitter):
    """
    NET_API_STATUS NetServerGetInfo(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerSetInfo(jitter):
    """
    NET_API_STATUS NetServerSetInfo(
        LPWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD ParmError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "ParmError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerSetInfoCommandLine(jitter):
    """
    NET_API_STATUS NetServerSetInfoCommandLine(
        WORD argc,
        LMSTR [] argv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["argc", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerComputerNameAdd(jitter):
    """
    NET_API_STATUS NetServerComputerNameAdd(
        LPWSTR ServerName,
        LPWSTR EmulatedDomainName,
        LPWSTR EmulatedServerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "EmulatedDomainName", "EmulatedServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerComputerNameDel(jitter):
    """
    NET_API_STATUS NetServerComputerNameDel(
        LPWSTR ServerName,
        LPWSTR EmulatedServerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "EmulatedServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerTransportAdd(jitter):
    """
    NET_API_STATUS NetServerTransportAdd(
        LPWSTR servername,
        DWORD level,
        LPBYTE bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerTransportAddEx(jitter):
    """
    NET_API_STATUS NetServerTransportAddEx(
        LPWSTR servername,
        DWORD level,
        LPBYTE bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerTransportDel(jitter):
    """
    NET_API_STATUS NetServerTransportDel(
        LPWSTR servername,
        DWORD level,
        LPBYTE bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerTransportEnum(jitter):
    """
    NET_API_STATUS NetServerTransportEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaTransportEnum(jitter):
    """
    NET_API_STATUS NetWkstaTransportEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUseAdd(jitter):
    """
    NET_API_STATUS NetUseAdd(
        LMSTR UncServerName,
        DWORD Level,
        LPBYTE Buf,
        LPDWORD ParmError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "Level", "Buf", "ParmError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUseDel(jitter):
    """
    NET_API_STATUS NetUseDel(
        LMSTR UncServerName,
        LMSTR UseName,
        DWORD ForceCond
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "UseName", "ForceCond"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUseEnum(jitter):
    """
    NET_API_STATUS NetUseEnum(
        LMSTR UncServerName,
        DWORD Level,
        LPBYTE* BufPtr,
        DWORD PreferedMaximumSize,
        LPDWORD EntriesRead,
        LPDWORD TotalEntries,
        LPDWORD ResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "Level", "BufPtr", "PreferedMaximumSize", "EntriesRead", "TotalEntries", "ResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUseGetInfo(jitter):
    """
    NET_API_STATUS NetUseGetInfo(
        LMSTR UncServerName,
        LMSTR UseName,
        DWORD Level,
        LPBYTE* BufPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "UseName", "Level", "BufPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserAdd(jitter):
    """
    NET_API_STATUS NetUserAdd(
        LMSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserChangePassword(jitter):
    """
    NET_API_STATUS NetUserChangePassword(
        LPCWSTR domainname,
        LPCWSTR username,
        LPCWSTR oldpassword,
        LPCWSTR newpassword
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["domainname", "username", "oldpassword", "newpassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserDel(jitter):
    """
    NET_API_STATUS NetUserDel(
        LPCWSTR servername,
        LPCWSTR username
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserEnum(jitter):
    """
    NET_API_STATUS NetUserEnum(
        LPCWSTR servername,
        DWORD level,
        DWORD filter,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "filter", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserGetGroups(jitter):
    """
    NET_API_STATUS NetUserGetGroups(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserGetInfo(jitter):
    """
    NET_API_STATUS NetUserGetInfo(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserGetLocalGroups(jitter):
    """
    NET_API_STATUS NetUserGetLocalGroups(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        [NetUserGetLocalGroupsFlags] flags,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "flags", "bufptr", "prefmaxlen", "entriesread", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserSetGroups(jitter):
    """
    NET_API_STATUS NetUserSetGroups(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        LPBYTE buf,
        DWORD num_entries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "buf", "num_entries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserSetInfo(jitter):
    """
    NET_API_STATUS NetUserSetInfo(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserModalsGet(jitter):
    """
    NET_API_STATUS NetUserModalsGet(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserModalsSet(jitter):
    """
    NET_API_STATUS NetUserModalsSet(
        LPCWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetValidatePasswordPolicyFree(jitter):
    """
    NET_API_STATUS NetValidatePasswordPolicyFree(
        LPVOID* OutputArg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OutputArg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetValidatePasswordPolicy(jitter):
    """
    NET_API_STATUS NetValidatePasswordPolicy(
        LPCWSTR ServerName,
        LPVOID Qualifier,
        NET_VALIDATE_PASSWORD_TYPE ValidationType,
        LPVOID InputArg,
        LPVOID OutputArg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Qualifier", "ValidationType", "InputArg", "OutputArg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaGetInfo(jitter):
    """
    NET_API_STATUS NetWkstaGetInfo(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaSetInfo(jitter):
    """
    NET_API_STATUS NetWkstaSetInfo(
        LPWSTR servername,
        DWORD level,
        LPBYTE buffer,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buffer", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaUserEnum(jitter):
    """
    NET_API_STATUS NetWkstaUserEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaUserGetInfo(jitter):
    """
    NET_API_STATUS NetWkstaUserGetInfo(
        LPWSTR reserved,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaUserSetInfo(jitter):
    """
    NET_API_STATUS NetWkstaUserSetInfo(
        LPWSTR reserved,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAddServiceAccount(jitter):
    """
    NTSTATUS NetAddServiceAccount(
        LPWSTR ServerName,
        LPWSTR AccountName,
        LPWSTR Reserved,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "AccountName", "Reserved", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetEnumerateServiceAccounts(jitter):
    """
    NTSTATUS NetEnumerateServiceAccounts(
        LPWSTR ServerName,
        DWORD Flags,
        DWORD* AccountsCount,
        PZPWSTR* Accounts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Flags", "AccountsCount", "Accounts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetIsServiceAccount(jitter):
    """
    NTSTATUS NetIsServiceAccount(
        LPWSTR ServerName,
        LPWSTR AccountName,
        BOOL* IsService
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "AccountName", "IsService"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRemoveServiceAccount(jitter):
    """
    NTSTATUS NetRemoveServiceAccount(
        LPWSTR ServerName,
        LPWSTR AccountName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "AccountName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavAddConnection(jitter):
    """
    [ERROR_CODE] DavAddConnection(
        HANDLE* ConnectionHandle,
        LPCWSTR RemoteName,
        LPCWSTR UserName,
        LPCWSTR Password,
        PBYTE ClientCert,
        DWORD CertSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "RemoteName", "UserName", "Password", "ClientCert", "CertSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavDeleteConnection(jitter):
    """
    [ERROR_CODE] DavDeleteConnection(
        HANDLE ConnectionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavFlushFile(jitter):
    """
    [ERROR_CODE] DavFlushFile(
        HANDLE hFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavGetExtendedError(jitter):
    """
    [ERROR_CODE] DavGetExtendedError(
        HANDLE hFile,
        DWORD* ExtError,
        LPWSTR ExtErrorString,
        DWORD* cChSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "ExtError", "ExtErrorString", "cChSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavGetHTTPFromUNCPath(jitter):
    """
    [ERROR_CODE] DavGetHTTPFromUNCPath(
        LPCWSTR UncPath,
        LPWSTR HttpPath,
        LPDWORD lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncPath", "HttpPath", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavGetUNCFromHTTPPath(jitter):
    """
    [ERROR_CODE] DavGetUNCFromHTTPPath(
        LPCWSTR HttpPath,
        LPWSTR UncPath,
        LPDWORD lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HttpPath", "UncPath", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetFileClose(jitter):
    """
    NET_API_STATUS NetFileClose(
        LMSTR servername,
        DWORD fileid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "fileid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetFileEnum(jitter):
    """
    NET_API_STATUS NetFileEnum(
        LMSTR servername,
        LMSTR basepath,
        LMSTR username,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "basepath", "username", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetFileGetInfo(jitter):
    """
    NET_API_STATUS NetFileGetInfo(
        LMSTR servername,
        DWORD fileid,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "fileid", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetSessionDel(jitter):
    """
    NET_API_STATUS NetSessionDel(
        LPWSTR servername,
        LPWSTR UncClientName,
        LPWSTR username
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "UncClientName", "username"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetSessionEnum(jitter):
    """
    NET_API_STATUS NetSessionEnum(
        LPWSTR servername,
        LPWSTR UncClientName,
        LPWSTR username,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "UncClientName", "username", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetSessionGetInfo(jitter):
    """
    NET_API_STATUS NetSessionGetInfo(
        LPWSTR servername,
        LPWSTR UncClientName,
        LPWSTR username,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "UncClientName", "username", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetConnectionEnum(jitter):
    """
    NET_API_STATUS NetConnectionEnum(
        LMSTR servername,
        LMSTR qualifier,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "qualifier", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareAdd(jitter):
    """
    NET_API_STATUS NetShareAdd(
        LPWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareCheck(jitter):
    """
    NET_API_STATUS NetShareCheck(
        LPWSTR servername,
        LPWSTR device,
        LPDWORD type
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "device", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareDel(jitter):
    """
    NET_API_STATUS NetShareDel(
        LMSTR servername,
        LMSTR netname,
        DWORD reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "netname", "reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareDelSticky(jitter):
    """
    NET_API_STATUS NetShareDelSticky(
        LMSTR servername,
        LMSTR netname,
        DWORD reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "netname", "reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareDelEx(jitter):
    """
    NET_API_STATUS NetShareDelEx(
        LMSTR servername,
        DWORD level,
        LPBYTE buf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareEnum(jitter):
    """
    NET_API_STATUS NetShareEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareEnumSticky(jitter):
    """
    NET_API_STATUS NetShareEnumSticky(
        LMSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareGetInfo(jitter):
    """
    NET_API_STATUS NetShareGetInfo(
        LPWSTR servername,
        LPWSTR netname,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "netname", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareSetInfo(jitter):
    """
    NET_API_STATUS NetShareSetInfo(
        LPWSTR servername,
        LPWSTR netname,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "netname", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetStatisticsGet(jitter):
    """
    NET_API_STATUS NetStatisticsGet(
        LPWSTR server,
        LPWSTR service,
        DWORD level,
        DWORD options,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "service", "level", "options", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessAdd(jitter):
    """
    NET_API_STATUS NetAccessAdd(
        LPCWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessCheck(jitter):
    """
    NET_API_STATUS NetAccessCheck(
        LPCWSTR reserved,
        LPCWSTR userName,
        LPCWSTR resource,
        DWORD operation,
        LPDWORD result
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "userName", "resource", "operation", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessDel(jitter):
    """
    NET_API_STATUS NetAccessDel(
        LPCWSTR servername,
        LPCWSTR resource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "resource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessEnum(jitter):
    """
    NET_API_STATUS NetAccessEnum(
        LPCWSTR servername,
        LPCWSTR BasePath,
        DWORD Recursive,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "BasePath", "Recursive", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessGetInfo(jitter):
    """
    NET_API_STATUS NetAccessGetInfo(
        LPCWSTR servername,
        LPCWSTR resource,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "resource", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessGetUserPerms(jitter):
    """
    NET_API_STATUS NetAccessGetUserPerms(
        LPCWSTR servername,
        LPCWSTR UGname,
        LPCWSTR resource,
        LPDWORD Perms
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "UGname", "resource", "Perms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessSetInfo(jitter):
    """
    NET_API_STATUS NetAccessSetInfo(
        LPCWSTR servername,
        LPCWSTR resource,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "resource", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAuditClear(jitter):
    """
    NET_API_STATUS NetAuditClear(
        LPCWSTR server,
        LPCWSTR backupfile,
        LPCWSTR service
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "backupfile", "service"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAuditRead(jitter):
    """
    NET_API_STATUS NetAuditRead(
        LPCWSTR server,
        LPCWSTR service,
        LPHLOG auditloghandle,
        DWORD offset,
        LPDWORD reserved1,
        DWORD reserved2,
        DWORD offsetflag,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD bytesread,
        LPDWORD totalavailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "service", "auditloghandle", "offset", "reserved1", "reserved2", "offsetflag", "bufptr", "prefmaxlen", "bytesread", "totalavailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAuditWrite(jitter):
    """
    NET_API_STATUS NetAuditWrite(
        DWORD type,
        LPBYTE buf,
        DWORD numbytes,
        LPCWSTR service,
        LPBYTE reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["type", "buf", "numbytes", "service", "reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetConfigGet(jitter):
    """
    NET_API_STATUS NetConfigGet(
        LPCWSTR server,
        LPCWSTR component,
        LPCWSTR parameter,
        LPBYTE* bufptr,
        LPDWORD totalavailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "component", "parameter", "bufptr", "totalavailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetConfigGetAll(jitter):
    """
    NET_API_STATUS NetConfigGetAll(
        LPCWSTR server,
        LPCWSTR component,
        LPBYTE* bufptr,
        LPDWORD totalavailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "component", "bufptr", "totalavailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetConfigSet(jitter):
    """
    NET_API_STATUS NetConfigSet(
        LPCWSTR server,
        LPCWSTR reserved1,
        LPCWSTR component,
        DWORD level,
        DWORD reserved2,
        LPBYTE buf,
        DWORD reserved3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "reserved1", "component", "level", "reserved2", "buf", "reserved3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetErrorLogClear(jitter):
    """
    NET_API_STATUS NetErrorLogClear(
        LPCWSTR UncServerName,
        LPCWSTR BackupFile,
        LPBYTE Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "BackupFile", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetErrorLogRead(jitter):
    """
    NET_API_STATUS NetErrorLogRead(
        LPCWSTR UncServerName,
        LPWSTR Reserved1,
        LPHLOG ErrorLogHandle,
        DWORD Offset,
        LPDWORD Reserved2,
        DWORD Reserved3,
        DWORD OffsetFlag,
        LPBYTE* BufPtr,
        DWORD PrefMaxSize,
        LPDWORD BytesRead,
        LPDWORD TotalAvailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "Reserved1", "ErrorLogHandle", "Offset", "Reserved2", "Reserved3", "OffsetFlag", "BufPtr", "PrefMaxSize", "BytesRead", "TotalAvailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetErrorLogWrite(jitter):
    """
    NET_API_STATUS NetErrorLogWrite(
        LPBYTE Reserved1,
        DWORD Code,
        LPCWSTR Component,
        LPBYTE Buffer,
        DWORD NumBytes,
        LPBYTE MsgBuf,
        DWORD StrCount,
        LPBYTE Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Reserved1", "Code", "Component", "Buffer", "NumBytes", "MsgBuf", "StrCount", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupAddMember(jitter):
    """
    NET_API_STATUS NetLocalGroupAddMember(
        LPCWSTR servername,
        LPCWSTR groupname,
        PSID membersid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "membersid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupDelMember(jitter):
    """
    NET_API_STATUS NetLocalGroupDelMember(
        LPCWSTR servername,
        LPCWSTR groupname,
        PSID membersid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "membersid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServiceControl(jitter):
    """
    NET_API_STATUS NetServiceControl(
        LPCWSTR servername,
        LPCWSTR service,
        DWORD opcode,
        DWORD arg,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "service", "opcode", "arg", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServiceEnum(jitter):
    """
    NET_API_STATUS NetServiceEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServiceGetInfo(jitter):
    """
    NET_API_STATUS NetServiceGetInfo(
        LPCWSTR servername,
        LPCWSTR service,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "service", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServiceInstall(jitter):
    """
    NET_API_STATUS NetServiceInstall(
        LPCWSTR servername,
        LPCWSTR service,
        DWORD argc,
        LPCWSTR [] argv,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "service", "argc", "argv", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaTransportAdd(jitter):
    """
    NET_API_STATUS NetWkstaTransportAdd(
        LMSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaTransportDel(jitter):
    """
    NET_API_STATUS NetWkstaTransportDel(
        LMSTR servername,
        LMSTR transportname,
        DWORD ucond
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "transportname", "ucond"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAdd(jitter):
    """
    NET_API_STATUS NetDfsAdd(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR PathName,
        LPWSTR Comment,
        [DFS_FLAG] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "PathName", "Comment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAddFtRoot(jitter):
    """
    NET_API_STATUS NetDfsAddFtRoot(
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR FtDfsName,
        LPWSTR Comment,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "FtDfsName", "Comment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAddRootTarget(jitter):
    """
    NET_API_STATUS NetDfsAddRootTarget(
        LPWSTR pDfsPath,
        LPWSTR pTargetPath,
        ULONG MajorVersion,
        LPWSTR pComment,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDfsPath", "pTargetPath", "MajorVersion", "pComment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAddStdRoot(jitter):
    """
    NET_API_STATUS NetDfsAddStdRoot(
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR Comment,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "Comment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAddStdRootForced(jitter):
    """
    NET_API_STATUS NetDfsAddStdRootForced(
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR Comment,
        LPWSTR Store
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "Comment", "Store"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsEnum(jitter):
    """
    NET_API_STATUS NetDfsEnum(
        LPWSTR DfsName,
        DWORD Level,
        DWORD PrefMaxLen,
        LPBYTE* Buffer,
        LPDWORD EntriesRead,
        LPDWORD ResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsName", "Level", "PrefMaxLen", "Buffer", "EntriesRead", "ResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetClientInfo(jitter):
    """
    NET_API_STATUS NetDfsGetClientInfo(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName,
        DWORD Level,
        LPBYTE* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName", "Level", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetFtContainerSecurity(jitter):
    """
    NET_API_STATUS NetDfsGetFtContainerSecurity(
        LPWSTR DomainName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR* ppSecurityDescriptor,
        LPDWORD lpcbSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainName", "SecurityInformation", "ppSecurityDescriptor", "lpcbSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetInfo(jitter):
    """
    NET_API_STATUS NetDfsGetInfo(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName,
        DWORD Level,
        LPBYTE* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName", "Level", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetSecurity(jitter):
    """
    NET_API_STATUS NetDfsGetSecurity(
        LPWSTR DfsEntryPath,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR* ppSecurityDescriptor,
        LPDWORD lpcbSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "SecurityInformation", "ppSecurityDescriptor", "lpcbSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetStdContainerSecurity(jitter):
    """
    NET_API_STATUS NetDfsGetStdContainerSecurity(
        LPWSTR MachineName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR* ppSecurityDescriptor,
        LPDWORD lpcbSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MachineName", "SecurityInformation", "ppSecurityDescriptor", "lpcbSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetSupportedNamespaceVersion(jitter):
    """
    NET_API_STATUS NetDfsGetSupportedNamespaceVersion(
        DFS_NAMESPACE_VERSION_ORIGIN Origin,
        PWSTR pName,
        PDFS_SUPPORTED_NAMESPACE_VERSION_INFO* ppVersionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Origin", "pName", "ppVersionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsManagerInitialize(jitter):
    """
    NET_API_STATUS NetDfsManagerInitialize(
        LPWSTR ServerName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsMove(jitter):
    """
    NET_API_STATUS NetDfsMove(
        LPWSTR Path,
        LPWSTR NewPath,
        [DFS_MOVE_FLAG] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Path", "NewPath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemove(jitter):
    """
    NET_API_STATUS NetDfsRemove(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemoveFtRoot(jitter):
    """
    NET_API_STATUS NetDfsRemoveFtRoot(
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR FtDfsName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "FtDfsName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemoveFtRootForced(jitter):
    """
    NET_API_STATUS NetDfsRemoveFtRootForced(
        LPWSTR DomainName,
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR FtDfsName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainName", "ServerName", "RootShare", "FtDfsName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemoveRootTarget(jitter):
    """
    NET_API_STATUS NetDfsRemoveRootTarget(
        LPWSTR pDfsPath,
        LPWSTR pTargetPath,
        [DFS_REMOVE_FLAG] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDfsPath", "pTargetPath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemoveStdRoot(jitter):
    """
    NET_API_STATUS NetDfsRemoveStdRoot(
        LPWSTR ServerName,
        LPWSTR RootShare,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetClientInfo(jitter):
    """
    NET_API_STATUS NetDfsSetClientInfo(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName,
        DWORD Level,
        LPBYTE Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName", "Level", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetFtContainerSecurity(jitter):
    """
    NET_API_STATUS NetDfsSetFtContainerSecurity(
        LPWSTR DomainName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetInfo(jitter):
    """
    NET_API_STATUS NetDfsSetInfo(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName,
        DWORD Level,
        LPBYTE Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName", "Level", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetSecurity(jitter):
    """
    NET_API_STATUS NetDfsSetSecurity(
        LPWSTR DfsEntryPath,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetStdContainerSecurity(jitter):
    """
    NET_API_STATUS NetDfsSetStdContainerSecurity(
        LPWSTR MachineName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MachineName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerAliasAdd(jitter):
    """
    NET_API_STATUS NetServerAliasAdd(
        LMSTR servername,
        DWORD level,
        LPBYTE buf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerAliasDel(jitter):
    """
    NET_API_STATUS NetServerAliasDel(
        LMSTR servername,
        DWORD level,
        LPBYTE buf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerAliasEnum(jitter):
    """
    NET_API_STATUS NetServerAliasEnum(
        LMSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
