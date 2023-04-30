
def iphlpapi_GetAdapterIndex(jitter):
    """
    [ERROR_CODE] GetAdapterIndex(
        LPWSTR AdapterName,
        PULONG IfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AdapterName", "IfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAdaptersAddresses(jitter):
    """
    [ERROR_CODE_ULONG] GetAdaptersAddresses(
        ADDRESS_FAMILY Family,
        [GetAdaptersAddressesFlags] Flags,
        PVOID Reserved,
        PIP_ADAPTER_ADDRESSES AdapterAddresses,
        PULONG SizePointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Flags", "Reserved", "AdapterAddresses", "SizePointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAdaptersInfo(jitter):
    """
    [ERROR_CODE] GetAdaptersInfo(
        PIP_ADAPTER_INFO pAdapterInfo,
        PULONG pOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAdapterInfo", "pOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetPerAdapterInfo(jitter):
    """
    [ERROR_CODE] GetPerAdapterInfo(
        ULONG IfIndex,
        PIP_PER_ADAPTER_INFO pPerAdapterInfo,
        PULONG pOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfIndex", "pPerAdapterInfo", "pOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUniDirectionalAdapterInfo(jitter):
    """
    [ERROR_CODE] GetUniDirectionalAdapterInfo(
        PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS pIPIfInfo,
        PULONG dwOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIPIfInfo", "dwOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateIpNetEntry(jitter):
    """
    [ERROR_CODE] CreateIpNetEntry(
        PMIB_IPNETROW pArpEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pArpEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateProxyArpEntry(jitter):
    """
    [ERROR_CODE] CreateProxyArpEntry(
        DWORD dwAddress,
        DWORD dwMask,
        DWORD dwIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwAddress", "dwMask", "dwIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIpNetEntry(jitter):
    """
    [ERROR_CODE] DeleteIpNetEntry(
        PMIB_IPNETROW pArpEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pArpEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteProxyArpEntry(jitter):
    """
    [ERROR_CODE] DeleteProxyArpEntry(
        DWORD dwAddress,
        DWORD dwMask,
        DWORD dwIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwAddress", "dwMask", "dwIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_FlushIpNetTable(jitter):
    """
    [ERROR_CODE] FlushIpNetTable(
        DWORD dwIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpNetTable(jitter):
    """
    [ERROR_CODE] GetIpNetTable(
        PMIB_IPNETTABLE pIpNetTable,
        PULONG pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpNetTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SendARP(jitter):
    """
    [ERROR_CODE] SendARP(
        IPAddr DestIP,
        IPAddr SrcIP,
        PULONG pMacAddr,
        PULONG PhyAddrLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestIP", "SrcIP", "pMacAddr", "PhyAddrLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpNetEntry(jitter):
    """
    [ERROR_CODE] SetIpNetEntry(
        PMIB_IPNETROW pArpEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pArpEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceAliasToLuid(jitter):
    """
    NETIO_STATUS ConvertInterfaceAliasToLuid(
        const WCHAR* InterfaceAlias,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceAlias", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceGuidToLuid(jitter):
    """
    NETIO_STATUS ConvertInterfaceGuidToLuid(
        const GUID* InterfaceGuid,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceGuid", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceIndexToLuid(jitter):
    """
    NETIO_STATUS ConvertInterfaceIndexToLuid(
        NET_IFINDEX InterfaceIndex,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceIndex", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToAlias(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToAlias(
        const NET_LUID* InterfaceLuid,
        PWSTR InterfaceAlias,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceAlias", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToGuid(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToGuid(
        const NET_LUID* InterfaceLuid,
        GUID* InterfaceGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToIndex(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToIndex(
        const NET_LUID* InterfaceLuid,
        PNET_IFINDEX InterfaceIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToNameA(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToNameA(
        const NET_LUID* InterfaceLuid,
        PSTR InterfaceName,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceName", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToNameW(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToNameW(
        const NET_LUID* InterfaceLuid,
        PWSTR InterfaceName,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceName", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceNameToLuidA(jitter):
    """
    NETIO_STATUS ConvertInterfaceNameToLuidA(
        const CHAR* InterfaceName,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceName", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceNameToLuidW(jitter):
    """
    NETIO_STATUS ConvertInterfaceNameToLuidW(
        const WCHAR* InterfaceName,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceName", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_if_indextoname(jitter):
    """
    PCHAR if_indextoname(
        NET_IFINDEX InterfaceIndex,
        PCHAR InterfaceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceIndex", "InterfaceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_if_nametoindex(jitter):
    """
    NET_IFINDEX if_nametoindex(
        PCSTR InterfaceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetFriendlyIfIndex(jitter):
    """
    [ERROR_CODE] GetFriendlyIfIndex(
        DWORD IfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfEntry(jitter):
    """
    [ERROR_CODE] GetIfEntry(
        PMIB_IFROW pIfRow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIfRow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfEntry2(jitter):
    """
    NETIOAPI_API GetIfEntry2(
        PMIB_IF_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfStackTable(jitter):
    """
    NETIOAPI_API GetIfStackTable(
        PMIB_IFSTACK_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfTable(jitter):
    """
    [ERROR_CODE] GetIfTable(
        PMIB_IFTABLE pIfTable,
        PULONG pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIfTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfTable2(jitter):
    """
    NETIOAPI_API GetIfTable2(
        PMIB_IF_TABLE2* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfTable2Ex(jitter):
    """
    NETIOAPI_API GetIfTable2Ex(
        MIB_IF_TABLE_LEVEL Level,
        PMIB_IF_TABLE2* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Level", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetInterfaceInfo(jitter):
    """
    [ERROR_CODE] GetInterfaceInfo(
        PIP_INTERFACE_INFO pIfTable,
        PULONG dwOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIfTable", "dwOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetInvertedIfStackTable(jitter):
    """
    NETIOAPI_API GetInvertedIfStackTable(
        PMIB_INVERTEDIFSTACK_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpInterfaceEntry(jitter):
    """
    NETIOAPI_API GetIpInterfaceEntry(
        PMIB_IPINTERFACE_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpInterfaceTable(jitter):
    """
    NETIOAPI_API GetIpInterfaceTable(
        ADDRESS_FAMILY Family,
        PMIB_IPINTERFACE_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetNumberOfInterfaces(jitter):
    """
    [ERROR_CODE] GetNumberOfInterfaces(
        PDWORD pdwNumIf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwNumIf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_InitializeIpInterfaceEntry(jitter):
    """
    VOID InitializeIpInterfaceEntry(
        PMIB_IPINTERFACE_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIfEntry(jitter):
    """
    [ERROR_CODE] SetIfEntry(
        PMIB_IFROW pIfRow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIfRow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpInterfaceEntry(jitter):
    """
    NETIOAPI_API SetIpInterfaceEntry(
        PMIB_IPINTERFACE_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIcmpStatistics(jitter):
    """
    [ERROR_CODE] GetIcmpStatistics(
        PMIB_ICMP pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpStatistics(jitter):
    """
    [ERROR_CODE] GetIpStatistics(
        PMIB_IPSTATS pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_Icmp6CreateFile(jitter):
    """
    [FILE_HANDLE] Icmp6CreateFile()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_Icmp6ParseReplies(jitter):
    """
    [ERROR_CODE] Icmp6ParseReplies(
        LPVOID ReplyBuffer,
        DWORD ReplySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReplyBuffer", "ReplySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_Icmp6SendEcho2(jitter):
    """
    [ERROR_CODE] Icmp6SendEcho2(
        HANDLE IcmpHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        struct sockaddr_in6* SourceAddress,
        struct sockaddr_in6* DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "Event", "ApcRoutine", "ApcContext", "SourceAddress", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpSendEcho2Ex(jitter):
    """
    [ERROR_CODE] IcmpSendEcho2Ex(
        HANDLE IcmpHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        IPAddr SourceAddress,
        IPAddr DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "Event", "ApcRoutine", "ApcContext", "SourceAddress", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpTTL(jitter):
    """
    [ERROR_CODE] SetIpTTL(
        UINT nTTL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nTTL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_AddIPAddress(jitter):
    """
    [ERROR_CODE] AddIPAddress(
        IPAddr Address,
        IPMask IpMask,
        DWORD IfIndex,
        PULONG NTEContext,
        PULONG NTEInstance
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address", "IpMask", "IfIndex", "NTEContext", "NTEInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateAnycastIpAddressEntry(jitter):
    """
    NETIOAPI_API CreateAnycastIpAddressEntry(
        const MIB_ANYCASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateUnicastIpAddressEntry(jitter):
    """
    NETIOAPI_API CreateUnicastIpAddressEntry(
        const MIB_UNICASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIPAddress(jitter):
    """
    [ERROR_CODE] DeleteIPAddress(
        ULONG NTEContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NTEContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteAnycastIpAddressEntry(jitter):
    """
    NETIOAPI_API DeleteAnycastIpAddressEntry(
        const MIB_ANYCASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteUnicastIpAddressEntry(jitter):
    """
    NETIOAPI_API DeleteUnicastIpAddressEntry(
        const MIB_UNICASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAnycastIpAddressEntry(jitter):
    """
    NETIOAPI_API GetAnycastIpAddressEntry(
        PMIB_ANYCASTIPADDRESS_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAnycastIpAddressTable(jitter):
    """
    NETIOAPI_API GetAnycastIpAddressTable(
        ADDRESS_FAMILY Family,
        PMIB_ANYCASTIPADDRESS_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpAddrTable(jitter):
    """
    [ERROR_CODE] GetIpAddrTable(
        PMIB_IPADDRTABLE pIpAddrTable,
        PULONG pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpAddrTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetMulticastIpAddressEntry(jitter):
    """
    NETIOAPI_API GetMulticastIpAddressEntry(
        PMIB_MULTICASTIPADDRESS_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetMulticastIpAddressTable(jitter):
    """
    NETIOAPI_API GetMulticastIpAddressTable(
        ADDRESS_FAMILY Family,
        PMIB_MULTICASTIPADDRESS_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUnicastIpAddressEntry(jitter):
    """
    NETIOAPI_API GetUnicastIpAddressEntry(
        PMIB_UNICASTIPADDRESS_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUnicastIpAddressTable(jitter):
    """
    NETIOAPI_API GetUnicastIpAddressTable(
        ADDRESS_FAMILY Family,
        PMIB_UNICASTIPADDRESS_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_InitializeUnicastIpAddressEntry(jitter):
    """
    VOID InitializeUnicastIpAddressEntry(
        PMIB_UNICASTIPADDRESS_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IpReleaseAddress(jitter):
    """
    [ERROR_CODE] IpReleaseAddress(
        PIP_ADAPTER_INDEX_MAP AdapterInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AdapterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IpRenewAddress(jitter):
    """
    [ERROR_CODE] IpRenewAddress(
        PIP_ADAPTER_INDEX_MAP AdapterInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AdapterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyStableUnicastIpAddressTable(jitter):
    """
    NETIOAPI_API NotifyStableUnicastIpAddressTable(
        ADDRESS_FAMILY Family,
        PMIB_UNICASTIPADDRESS_TABLE* Table,
        PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK CallerCallback,
        PVOID CallerContext,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table", "CallerCallback", "CallerContext", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetUnicastIpAddressEntry(jitter):
    """
    NETIOAPI_API SetUnicastIpAddressEntry(
        const MIB_UNICASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateIpNetEntry2(jitter):
    """
    NETIOAPI_API CreateIpNetEntry2(
        const MIB_IPNET_ROW2* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIpNetEntry2(jitter):
    """
    NETIOAPI_API DeleteIpNetEntry2(
        const MIB_IPNET_ROW2* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_FlushIpNetTable2(jitter):
    """
    NETIOAPI_API FlushIpNetTable2(
        ADDRESS_FAMILY Family,
        NET_IFINDEX InterfaceIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "InterfaceIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpNetEntry2(jitter):
    """
    NETIOAPI_API GetIpNetEntry2(
        PMIB_IPNET_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpNetTable2(jitter):
    """
    NETIOAPI_API GetIpNetTable2(
        ADDRESS_FAMILY Family,
        PMIB_IPNET_TABLE2* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ResolveIpNetEntry2(jitter):
    """
    NETIOAPI_API ResolveIpNetEntry2(
        PMIB_IPNET_ROW2 Row,
        const SOCKADDR_INET* SourceAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "SourceAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ResolveNeighbor(jitter):
    """
    [ERROR_CODE_ULONG] ResolveNeighbor(
        SOCKADDR* NetworkAddress,
        PVOID PhysicalAddress,
        PULONG PhysicalAddressLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NetworkAddress", "PhysicalAddress", "PhysicalAddressLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpNetEntry2(jitter):
    """
    NETIOAPI_API SetIpNetEntry2(
        PMIB_IPNET_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_FlushIpPathTable(jitter):
    """
    NETIOAPI_API FlushIpPathTable(
        ADDRESS_FAMILY Family
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpPathEntry(jitter):
    """
    NETIOAPI_API GetIpPathEntry(
        PMIB_IPPATH_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpPathTable(jitter):
    """
    NETIOAPI_API GetIpPathTable(
        ADDRESS_FAMILY Family,
        MIB_IPPATH_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateIpForwardEntry(jitter):
    """
    [ERROR_CODE] CreateIpForwardEntry(
        PMIB_IPFORWARDROW pRoute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRoute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateIpForwardEntry2(jitter):
    """
    NETIOAPI_API CreateIpForwardEntry2(
        const MIB_IPFORWARD_ROW2* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIpForwardEntry(jitter):
    """
    [ERROR_CODE] DeleteIpForwardEntry(
        PMIB_IPFORWARDROW pRoute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRoute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIpForwardEntry2(jitter):
    """
    NETIOAPI_API DeleteIpForwardEntry2(
        const MIB_IPFORWARD_ROW2* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_EnableRouter(jitter):
    """
    [ERROR_CODE] EnableRouter(
        HANDLE* pHandle,
        OVERLAPPED* pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pHandle", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetBestInterface(jitter):
    """
    [ERROR_CODE] GetBestInterface(
        IPAddr dwDestAddr,
        PDWORD pdwBestIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDestAddr", "pdwBestIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetBestInterfaceEx(jitter):
    """
    [ERROR_CODE] GetBestInterfaceEx(
        struct sockaddr* pDestAddr,
        PDWORD pdwBestIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDestAddr", "pdwBestIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetBestRoute(jitter):
    """
    [ERROR_CODE] GetBestRoute(
        DWORD dwDestAddr,
        DWORD dwSourceAddr,
        PMIB_IPFORWARDROW pBestRoute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDestAddr", "dwSourceAddr", "pBestRoute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetBestRoute2(jitter):
    """
    NETIOAPI_API GetBestRoute2(
        NET_LUID* InterfaceLuid,
        NET_IFINDEX InterfaceIndex,
        const SOCKADDR_INET* SourceAddress,
        const SOCKADDR_INET* DestinationAddress,
        ULONG AddressSortOptions,
        PMIB_IPFORWARD_ROW2 BestRoute,
        SOCKADDR_INET* BestSourceAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceIndex", "SourceAddress", "DestinationAddress", "AddressSortOptions", "BestRoute", "BestSourceAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpForwardEntry2(jitter):
    """
    NETIOAPI_API GetIpForwardEntry2(
        PMIB_IPFORWARD_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpForwardTable(jitter):
    """
    [ERROR_CODE] GetIpForwardTable(
        PMIB_IPFORWARDTABLE pIpForwardTable,
        PULONG pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpForwardTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpForwardTable2(jitter):
    """
    NETIOAPI_API GetIpForwardTable2(
        ADDRESS_FAMILY Family,
        PMIB_IPFORWARD_TABLE2* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetRTTAndHopCount(jitter):
    """
    BOOL GetRTTAndHopCount(
        IPAddr DestIpAddress,
        PULONG HopCount,
        ULONG MaxHops,
        PULONG RTT
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestIpAddress", "HopCount", "MaxHops", "RTT"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_InitializeIpForwardEntry(jitter):
    """
    VOID InitializeIpForwardEntry(
        PMIB_IPFORWARD_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpForwardEntry(jitter):
    """
    [ERROR_CODE] SetIpForwardEntry(
        PMIB_IPFORWARDROW pRoute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRoute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpForwardEntry2(jitter):
    """
    NETIOAPI_API SetIpForwardEntry2(
        const MIB_IPFORWARD_ROW2* Route
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Route"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpStatistics(jitter):
    """
    [ERROR_CODE] SetIpStatistics(
        PMIB_IPSTATS pIpStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpStatisticsEx(jitter):
    """
    [ERROR_CODE] SetIpStatisticsEx(
        PMIB_IPSTATS pIpStats,
        ULONG Family
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpStats", "Family"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_UnenableRouter(jitter):
    """
    [ERROR_CODE] UnenableRouter(
        OVERLAPPED* pOverlapped,
        LPDWORD lpdwEnableCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOverlapped", "lpdwEnableCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_FreeMibTable(jitter):
    """
    VOID FreeMibTable(
        PVOID Memory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Memory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertIpv4MaskToLength(jitter):
    """
    NETIO_STATUS ConvertIpv4MaskToLength(
        ULONG Mask,
        PUINT8 MaskLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Mask", "MaskLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertLengthToIpv4Mask(jitter):
    """
    NETIO_STATUS ConvertLengthToIpv4Mask(
        ULONG MaskLength,
        PULONG Mask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MaskLength", "Mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateSortedAddressPairs(jitter):
    """
    NETIOAPI_API CreateSortedAddressPairs(
        const PSOCKADDR_IN6 SourceAddressList,
        ULONG SourceAddressCount,
        const PSOCKADDR_IN6 DestinationAddressList,
        ULONG DestinationAddressCount,
        ULONG AddressSortOptions,
        PSOCKADDR_IN6_PAIR* SortedAddressPairList,
        ULONG* SortedAddressPairCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceAddressList", "SourceAddressCount", "DestinationAddressList", "DestinationAddressCount", "AddressSortOptions", "SortedAddressPairList", "SortedAddressPairCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ParseNetworkString(jitter):
    """
    [ERROR_CODE] ParseNetworkString(
        const WCHAR* NetworkString,
        DWORD Types,
        PNET_ADDRESS_INFO AddressInfo,
        USHORT* PortNumber,
        BYTE* PrefixLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NetworkString", "Types", "AddressInfo", "PortNumber", "PrefixLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetNetworkParams(jitter):
    """
    [ERROR_CODE] GetNetworkParams(
        PFIXED_INFO pFixedInfo,
        PULONG pOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFixedInfo", "pOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CancelMibChangeNotify2(jitter):
    """
    NETIOAPI_API CancelMibChangeNotify2(
        HANDLE NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyAddrChange(jitter):
    """
    [ERROR_CODE] NotifyAddrChange(
        PHANDLE Handle,
        LPOVERLAPPED overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyIpInterfaceChange(jitter):
    """
    NETIOAPI_API NotifyIpInterfaceChange(
        ADDRESS_FAMILY Family,
        PIPINTERFACE_CHANGE_CALLBACK Callback,
        PVOID CallerContext,
        BOOLEAN InitialNotification,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Callback", "CallerContext", "InitialNotification", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyRouteChange(jitter):
    """
    [ERROR_CODE] NotifyRouteChange(
        PHANDLE Handle,
        LPOVERLAPPED overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyRouteChange2(jitter):
    """
    NETIOAPI_API NotifyRouteChange2(
        ADDRESS_FAMILY Family,
        PIPFORWARD_CHANGE_CALLBACK Callback,
        PVOID CallerContext,
        BOOLEAN InitialNotification,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Callback", "CallerContext", "InitialNotification", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyUnicastIpAddressChange(jitter):
    """
    NETIOAPI_API NotifyUnicastIpAddressChange(
        ADDRESS_FAMILY Family,
        PUNICAST_IPADDRESS_CHANGE_CALLBACK Callback,
        PVOID CallerContext,
        BOOLEAN InitialNotification,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Callback", "CallerContext", "InitialNotification", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CancelSecurityHealthChangeNotify(jitter):
    """
    BOOL CancelSecurityHealthChangeNotify(
        LPOVERLAPPED notifyOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["notifyOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifySecurityHealthChange(jitter):
    """
    [ERROR_CODE] NotifySecurityHealthChange(
        PHANDLE pHandle,
        LPOVERLAPPED pOverLapped,
        PULONG SecurityHealthFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pHandle", "pOverLapped", "SecurityHealthFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTeredoPort(jitter):
    """
    NETIOAPI_API GetTeredoPort(
        USHORT* Port
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyTeredoPortChange(jitter):
    """
    NETIOAPI_API NotifyTeredoPortChange(
        PTEREDO_PORT_CHANGE_CALLBACK Callback,
        PVOID CallerContext,
        BOOLEAN InitialNotification,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Callback", "CallerContext", "InitialNotification", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetExtendedTcpTable(jitter):
    """
    [ERROR_CODE] GetExtendedTcpTable(
        PVOID pTcpTable,
        PDWORD pdwSize,
        BOOL bOrder,
        ADDRESS_FAMILY ulAf,
        TCP_TABLE_CLASS TableClass,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpTable", "pdwSize", "bOrder", "ulAf", "TableClass", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetExtendedUdpTable(jitter):
    """
    [ERROR_CODE] GetExtendedUdpTable(
        PVOID pUdpTable,
        PDWORD pdwSize,
        BOOL bOrder,
        ADDRESS_FAMILY ulAf,
        UDP_TABLE_CLASS TableClass,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUdpTable", "pdwSize", "bOrder", "ulAf", "TableClass", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetOwnerModuleFromTcp6Entry(jitter):
    """
    [ERROR_CODE] GetOwnerModuleFromTcp6Entry(
        PMIB_TCP6ROW_OWNER_MODULE pTcpEntry,
        TCPIP_OWNER_MODULE_INFO_CLASS Class,
        PVOID Buffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpEntry", "Class", "Buffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetOwnerModuleFromTcpEntry(jitter):
    """
    [ERROR_CODE] GetOwnerModuleFromTcpEntry(
        PMIB_TCPROW_OWNER_MODULE pTcpEntry,
        TCPIP_OWNER_MODULE_INFO_CLASS Class,
        PVOID Buffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpEntry", "Class", "Buffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetOwnerModuleFromUdp6Entry(jitter):
    """
    [ERROR_CODE] GetOwnerModuleFromUdp6Entry(
        PMIB_UDP6ROW_OWNER_MODULE pUdpEntry,
        TCPIP_OWNER_MODULE_INFO_CLASS Class,
        PVOID Buffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUdpEntry", "Class", "Buffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetOwnerModuleFromUdpEntry(jitter):
    """
    [ERROR_CODE] GetOwnerModuleFromUdpEntry(
        PMIB_UDPROW_OWNER_MODULE pUdpEntry,
        TCPIP_OWNER_MODULE_INFO_CLASS Class,
        PVOID Buffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUdpEntry", "Class", "Buffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetPerTcp6ConnectionEStats(jitter):
    """
    [ERROR_CODE_ULONG] GetPerTcp6ConnectionEStats(
        PMIB_TCP6ROW Row,
        TCP_ESTATS_TYPE EstatsType,
        PUCHAR Rw,
        ULONG RwVersion,
        ULONG RwSize,
        PUCHAR Ros,
        ULONG RosVersion,
        ULONG RosSize,
        PUCHAR Rod,
        ULONG RodVersion,
        ULONG RodSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "EstatsType", "Rw", "RwVersion", "RwSize", "Ros", "RosVersion", "RosSize", "Rod", "RodVersion", "RodSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetPerTcpConnectionEStats(jitter):
    """
    [ERROR_CODE_ULONG] GetPerTcpConnectionEStats(
        PMIB_TCPROW Row,
        TCP_ESTATS_TYPE EstatsType,
        PUCHAR Rw,
        ULONG RwVersion,
        ULONG RwSize,
        PUCHAR Ros,
        ULONG RosVersion,
        ULONG RosSize,
        PUCHAR Rod,
        ULONG RodVersion,
        ULONG RodSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "EstatsType", "Rw", "RwVersion", "RwSize", "Ros", "RosVersion", "RosSize", "Rod", "RodVersion", "RodSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcpStatistics(jitter):
    """
    [ERROR_CODE] GetTcpStatistics(
        PMIB_TCPSTATS pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcpStatisticsEx(jitter):
    """
    [ERROR_CODE] GetTcpStatisticsEx(
        PMIB_TCPSTATS pStats,
        ADDRESS_FAMILY dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcp6Table(jitter):
    """
    [ERROR_CODE_ULONG] GetTcp6Table(
        PMIB_TCP6TABLE TcpTable,
        PULONG SizePointer,
        BOOL Order
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TcpTable", "SizePointer", "Order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcp6Table2(jitter):
    """
    [ERROR_CODE_ULONG] GetTcp6Table2(
        PMIB_TCP6TABLE2 TcpTable,
        PULONG SizePointer,
        BOOL Order
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TcpTable", "SizePointer", "Order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcpTable(jitter):
    """
    [ERROR_CODE] GetTcpTable(
        PMIB_TCPTABLE pTcpTable,
        PDWORD pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcpTable2(jitter):
    """
    [ERROR_CODE_ULONG] GetTcpTable2(
        PMIB_TCPTABLE2 TcpTable,
        PULONG SizePointer,
        BOOL Order
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TcpTable", "SizePointer", "Order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetPerTcp6ConnectionEStats(jitter):
    """
    [ERROR_CODE_ULONG] SetPerTcp6ConnectionEStats(
        PMIB_TCP6ROW Row,
        TCP_ESTATS_TYPE EstatsType,
        PUCHAR Rw,
        ULONG RwVersion,
        ULONG RwSize,
        ULONG Offset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "EstatsType", "Rw", "RwVersion", "RwSize", "Offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetPerTcpConnectionEStats(jitter):
    """
    [ERROR_CODE_ULONG] SetPerTcpConnectionEStats(
        PMIB_TCP6ROW Row,
        TCP_ESTATS_TYPE EstatsType,
        PUCHAR Rw,
        ULONG RwVersion,
        ULONG RwSize,
        ULONG Offset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "EstatsType", "Rw", "RwVersion", "RwSize", "Offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetTcpEntry(jitter):
    """
    [ERROR_CODE] SetTcpEntry(
        PMIB_TCPROW pTcpRow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpRow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUdp6Table(jitter):
    """
    [ERROR_CODE_ULONG] GetUdp6Table(
        PMIB_UDP6TABLE Udp6Table,
        PULONG SizePointer,
        BOOL Order
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Udp6Table", "SizePointer", "Order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUdpStatistics(jitter):
    """
    [ERROR_CODE] GetUdpStatistics(
        PMIB_UDPSTATS pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUdpStatisticsEx(jitter):
    """
    [ERROR_CODE] GetUdpStatisticsEx(
        PMIB_UDPSTATS pStats,
        ADDRESS_FAMILY dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUdpTable(jitter):
    """
    [ERROR_CODE] GetUdpTable(
        PMIB_UDPTABLE pUdpTable,
        PDWORD pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUdpTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_AllocateAndGetTcpExTableFromStack(jitter):
    """
    [ERROR_CODE] AllocateAndGetTcpExTableFromStack(
        PVOID* ppTcpTable,
        BOOL bOrder,
        HANDLE hHeap,
        DWORD dwFlags,
        ADDRESS_FAMILY dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppTcpTable", "bOrder", "hHeap", "dwFlags", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_AllocateAndGetUdpExTableFromStack(jitter):
    """
    [ERROR_CODE] AllocateAndGetUdpExTableFromStack(
        PVOID* ppUDPTable,
        BOOL bOrder,
        HANDLE hHeap,
        DWORD dwFlags,
        ADDRESS_FAMILY dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppUDPTable", "bOrder", "hHeap", "dwFlags", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpCloseHandle(jitter):
    """
    BOOL IcmpCloseHandle(
        HANDLE IcmpHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpCreateFile(jitter):
    """
    [FILE_HANDLE] IcmpCreateFile()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpParseReplies(jitter):
    """
    DWORD IcmpParseReplies(
        LPVOID ReplyBuffer,
        DWORD ReplySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReplyBuffer", "ReplySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpSendEcho(jitter):
    """
    [ERROR_CODE] IcmpSendEcho(
        HANDLE IcmpHandle,
        IPAddr DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpSendEcho2(jitter):
    """
    [ERROR_CODE] IcmpSendEcho2(
        HANDLE IcmpHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        IPAddr DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "Event", "ApcRoutine", "ApcContext", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpNetworkConnectionBandwidthEstimates(jitter):
    """
    NETIOAPI_API GetIpNetworkConnectionBandwidthEstimates(
        NET_IFINDEX InterfaceIndex,
        ADDRESS_FAMILY AddressFamily,
        PMIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES BandwidthEstimates
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceIndex", "AddressFamily", "BandwidthEstimates"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CancelIPChangeNotify(jitter):
    """
    BOOL CancelIPChangeNotify(
        LPOVERLAPPED notifyOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["notifyOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreatePersistentTcpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] CreatePersistentTcpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts,
        PULONG64 Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreatePersistentUdpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] CreatePersistentUdpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts,
        PULONG64 Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeletePersistentTcpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] DeletePersistentTcpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeletePersistentUdpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] DeletePersistentUdpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DisableMediaSense(jitter):
    """
    [ERROR_CODE] DisableMediaSense(
        HANDLE* pHandle,
        OVERLAPPED* pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pHandle", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAdapterOrderMap(jitter):
    """
    PIP_ADAPTER_ORDER_MAP GetAdapterOrderMap()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIcmpStatisticsEx(jitter):
    """
    [ERROR_CODE] GetIcmpStatisticsEx(
        PMIB_ICMP_EX pStats,
        DWORD dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpErrorString(jitter):
    """
    [ERROR_CODE] GetIpErrorString(
        IP_STATUS ErrorCode,
        PWCHAR Buffer,
        PDWORD Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ErrorCode", "Buffer", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpStatisticsEx(jitter):
    """
    [ERROR_CODE] GetIpStatisticsEx(
        PMIB_IPSTATS pStats,
        DWORD dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_LookupPersistentTcpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] LookupPersistentTcpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts,
        PULONG64 Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_LookupPersistentUdpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] LookupPersistentUdpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts,
        PULONG64 Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NhpAllocateAndGetInterfaceInfoFromStack(jitter):
    """
    [ERROR_CODE] NhpAllocateAndGetInterfaceInfoFromStack(
        IP_INTERFACE_NAME_INFO** ppTable,
        PDWORD pdwCount,
        BOOL bOrder,
        HANDLE hHeap,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppTable", "pdwCount", "bOrder", "hHeap", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_RestoreMediaSense(jitter):
    """
    [ERROR_CODE] RestoreMediaSense(
        OVERLAPPED* pOverlapped,
        LPDWORD lpdwEnableCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOverlapped", "lpdwEnableCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
