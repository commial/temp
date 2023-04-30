
def dhcpsapi_DhcpAddFilterV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpAddFilterV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_FILTER_ADD_INFO* AddFilterInfo, BOOL ForceFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "AddFilterInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddServer(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpAddServer(DWORD Flags, LPVOID IdInfo, LPDHCP_SERVER_INFO NewServer, LPVOID CallbackFn, LPVOID CallbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "IdInfo", "NewServer", "CallbackFn", "CallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddSubnetElementV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpAddSubnetElementV5(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_ELEMENT_DATA_V5* AddElementInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "AddElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAuditLogGetParams(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpAuditLogGetParams(LPWSTR ServerIpAddress, DWORD Flags, LPWSTR* AuditLogDir, DWORD* DiskCheckInterval, DWORD* MaxLogFilesSize, DWORD* MinSpaceOnDisk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "AuditLogDir", "DiskCheckInterval", "MaxLogFilesSize", "MinSpaceOnDisk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAuditLogSetParams(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpAuditLogSetParams(LPWSTR ServerIpAddress, DWORD Flags, LPWSTR AuditLogDir, DWORD DiskCheckInterval, DWORD MaxLogFilesSize, DWORD MinSpaceOnDisk)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "AuditLogDir", "DiskCheckInterval", "MaxLogFilesSize", "MinSpaceOnDisk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClass(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateClass(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, LPDHCP_CLASS_INFO ClassInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClientInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateClientInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_CLIENT_INFO* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClientInfoV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateClientInfoV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_CLIENT_INFO_V4* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClientInfoVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateClientInfoVQ(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_CLIENT_INFO_VQ ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateOptionV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateOptionV5(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionId, LPWSTR ClassName, LPWSTR VendorName, LPDHCP_OPTION OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateSubnet(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateSubnet(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_INFO* SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateSubnetVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateSubnetVQ(WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_INFO_VQ* SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteClass(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteClass(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, LPWSTR ClassName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteClientInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteClientInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_SEARCH_INFO* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteFilterV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteFilterV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_ADDR_PATTERN* DeleteFilterInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "DeleteFilterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteServer(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteServer(DWORD Flags, LPVOID IdInfo, LPDHCP_SERVER_INFO NewServer, LPVOID CallbackFn, LPVOID CallbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "IdInfo", "NewServer", "CallbackFn", "CallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteSubnet(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteSubnet(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_FORCE_FLAG ForceFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteSuperScopeV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteSuperScopeV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST LPWSTR SuperScopeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SuperScopeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDsCleanup(jitter):
    """"
    [Dhcpsapi.dll] VOID DhcpDsCleanup()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDsInit(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDsInit()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumClasses(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumClasses(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLASS_INFO_ARRAY* ClassInfoArray, DWORD* nRead, DWORD* nTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ResumeHandle", "PreferredMaximum", "ClassInfoArray", "nRead", "nTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumFilterV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumFilterV4(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_ADDR_PATTERN ResumeHandle, DWORD PreferrredMaximum, DHCP_FILTER_LIST_TYPE ListType, LPDHCP_FILTER_ENUM_INFO* EnumFilterInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferrredMaximum", "ListType", "EnumFilterInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionsV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumOptionsV5(LPWSTR ServerIpAddress, DWORD Flags, LPWSTR ClassName, LPWSTR VendorName, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_OPTION_ARRAY* Options, DWORD* OptionsRead, DWORD* OptionsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ResumeHandle", "PreferredMaximum", "Options", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionValuesV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumOptionValuesV5(LPWSTR ServerIpAddress, DWORD Flags, LPWSTR ClassName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_OPTION_VALUE_ARRAY* OptionValues, DWORD* OptionsRead, DWORD* OptionsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ScopeInfo", "ResumeHandle", "PreferredMaximum", "OptionValues", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumServers(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumServers(DWORD Flags, LPVOID IdInfo, LPDHCP_SERVER_INFO_ARRAY* Servers, LPVOID CallbackFn, LPVOID CallbackData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "IdInfo", "Servers", "CallbackFn", "CallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClients(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetClients(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLIENT_INFO_ARRAY* ClientInfo, DWORD* ClientsRead, DWORD* ClientsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetClientsV5(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLIENT_INFO_ARRAY_V5* ClientInfo, DWORD* ClientsRead, DWORD* ClientsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetClientsVQ(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLIENT_INFO_ARRAY_VQ* ClientInfo, DWORD* ClientsRead, DWORD* ClientsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsFilterStatusInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetClientsFilterStatusInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLIENT_FILTER_STATUS_INFO_ARRAY* ClientInfo, DWORD* ClientsRead, DWORD* ClientsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetElementsV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetElementsV5(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_SUBNET_ELEMENT_TYPE EnumElementType, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_SUBNET_ELEMENT_INFO_ARRAY* EnumElementInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "EnumElementType", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnets(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnets(DHCP_CONST WCHAR* ServerIpAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_IP_ARRAY* EnumInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferredMaximum", "EnumInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetAllOptionValues(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetAllOptionValues(LPWSTR ServerIpAddress, DWORD Flags, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, LPDHCP_ALL_OPTION_VALUES* Values)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ScopeInfo", "Values"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClassInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetClassInfo(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, LPDHCP_CLASS_INFO PartialClassInfo, LPDHCP_CLASS_INFO* FilledClassInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "PartialClassInfo", "FilledClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetClientInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_SEARCH_INFO* SearchInfo, LPDHCP_CLIENT_INFO* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientInfoV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetClientInfoV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_SEARCH_INFO* SearchInfo, LPDHCP_CLIENT_INFO_V4* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientInfoVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetClientInfoVQ(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_SEARCH_INFO SearchInfo, LPDHCP_CLIENT_INFO_VQ ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetFilterV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetFilterV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_FILTER_GLOBAL_INFO* GlobalFilterInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "GlobalFilterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetMibInfoV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetMibInfoV5(WCHAR* ServerIpAddress, LPDHCP_MIB_INFO_V5* MibInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "MibInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionInfoV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetOptionInfoV5(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, LPWSTR ClassName, LPWSTR VendorName, LPDHCP_OPTION* OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionValue(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetOptionValue(DHCP_CONST WCHAR* ServerIpAddress, DHCP_OPTION_ID OptionID, DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo, LPDHCP_OPTION_VALUE* OptionValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionValueV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetOptionValueV5(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, LPWSTR ClassName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, LPDHCP_OPTION_VALUE* OptionValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetServerBindingInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetServerBindingInfo(DHCP_CONST WCHAR* ServerIpAddress, ULONG Flags, LPDHCP_BIND_ELEMENT_ARRAY* BindElementsInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "BindElementsInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSubnetDelayOffer(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetSubnetDelayOffer(LPWSTR ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, USHORT* TimeDelayInMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "TimeDelayInMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSubnetInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetSubnetInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, LPDHCP_SUBNET_INFO* SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSubnetInfoVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetSubnetInfoVQ(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, LPDHCP_SUBNET_INFO_VQ* SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSuperScopeInfoV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetSuperScopeInfoV4(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_SUPER_SCOPE_TABLE* SuperScopeTable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SuperScopeTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetVersion(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetVersion(LPWSTR ServerIpAddress, LPDWORD MajorVersion, LPDWORD MinorVersion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "MajorVersion", "MinorVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpModifyClass(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpModifyClass(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, LPDHCP_CLASS_INFO ClassInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveOptionV5(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, LPWSTR ClassName, LPWSTR VendorName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionValueV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveOptionValueV5(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, LPWSTR ClassName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "ScopeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveSubnetElementV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveSubnetElementV5(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_ELEMENT_DATA_V5* RemoveElementInfo, DHCP_FORCE_FLAG ForceFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "RemoveElementInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRpcFreeMemory(jitter):
    """"
    [Dhcpsapi.dll] VOID DhcpRpcFreeMemory(PVOID BufferPointer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferPointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerGetConfigVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerGetConfigVQ(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_SERVER_CONFIG_INFO_VQ* ConfigInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerQueryDnsRegCredentials(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerQueryDnsRegCredentials(LPWSTR ServerIpAddress, ULONG UnameSize, LPWSTR Uname, ULONG DomainSize, LPWSTR Domain)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "UnameSize", "Uname", "DomainSize", "Domain"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerRedoAuthorization(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerRedoAuthorization(LPWSTR ServerIpAddr, ULONG dwReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddr", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetConfigV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerSetConfigV4(DHCP_CONST WCHAR* ServerIpAddress, [DHCP_FIELDS_TO_SET] FieldsToSet, LPDHCP_SERVER_CONFIG_INFO_V4 ConfigInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "FieldsToSet", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetConfigVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerSetConfigVQ(DHCP_CONST WCHAR* ServerIpAddress, [DHCP_FIELDS_TO_SET] FieldsToSet, LPDHCP_SERVER_CONFIG_INFO_VQ ConfigInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "FieldsToSet", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetDnsRegCredentialsV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerSetDnsRegCredentialsV5(LPWSTR ServerIpAddress, LPWSTR Uname, LPWSTR Domain, LPWSTR Password)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Uname", "Domain", "Password"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetClientInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetClientInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_CLIENT_INFO* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetClientInfoV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetClientInfoV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_CLIENT_INFO_V4* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetClientInfoVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetClientInfoVQ(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_CLIENT_INFO_VQ ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetFilterV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetFilterV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_FILTER_GLOBAL_INFO* GlobalFilterInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "GlobalFilterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionInfoV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetOptionInfoV5(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, LPWSTR* ClassName, LPWSTR* VendorName, LPDHCP_OPTION OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValueV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetOptionValueV5(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionId, LPWSTR ClassName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, LPDHCP_OPTION_DATA OptionValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "ClassName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetServerBindingInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetServerBindingInfo(DHCP_CONST WCHAR* ServerIpAddress, ULONG Flags, LPDHCP_BIND_ELEMENT_ARRAY BindElementInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "BindElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSubnetDelayOffer(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetSubnetDelayOffer(LPWSTR ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, USHORT TimeDelayInMilliseconds)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "TimeDelayInMilliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSubnetInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetSubnetInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_INFO* SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSubnetInfoVQ(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetSubnetInfoVQ(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_INFO_VQ* SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSuperScopeV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetSuperScopeV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST LPWSTR SuperScopeName, DHCP_CONST BOOL ChangeExisting)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SuperScopeName", "ChangeExisting"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddSubnetElementV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpAddSubnetElementV6(LPWSTR ServerIpAddress, DHCP_IPV6_ADDRESS SubnetAddress, LPDHCP_SUBNET_ELEMENT_DATA_V6 AddElementInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "AddElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateClassV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateClassV6(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, LPDHCP_CLASS_INFO_V6 ClassInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateOptionV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateOptionV6(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionId, WCHAR* ClassName, WCHAR* VendorName, LPDHCP_OPTION OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateSubnetV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateSubnetV6(LPWSTR ServerIpAddress, DHCP_IPV6_ADDRESS SubnetAddress, LPDHCP_SUBNET_INFO_V6* SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteClassV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteClassV6(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, LPWSTR ClassName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteClientInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteClientInfoV6(LPWSTR ServerIpAddress, LPDHCP_SEARCH_INFO_V6 ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpDeleteSubnetV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpDeleteSubnetV6(LPWSTR ServerIpAddress, DHCP_IPV6_ADDRESS SubnetAddress, DHCP_FORCE_FLAG ForceFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumClassesV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumClassesV6(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLASS_INFO_ARRAY_V6* ClassInfoArray, DWORD* nRead, DWORD* nTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ResumeHandle", "PreferredMaximum", "ClassInfoArray", "nRead", "nTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionsV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumOptionsV6(LPWSTR ServerIpAddress, DWORD Flags, WCHAR* ClassName, WCHAR* VendorName, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_OPTION_ARRAY* Options, DWORD* OptionsRead, DWORD* OptionsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ResumeHandle", "PreferredMaximum", "Options", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionValuesV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumOptionValuesV6(LPWSTR ServerIpAddress, DWORD Flags, WCHAR* ClassName, WCHAR* VendorName, LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_OPTION_VALUE_ARRAY* OptionValues, DWORD* OptionsRead, DWORD* OptionsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ScopeInfo", "ResumeHandle", "PreferredMaximum", "OptionValues", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetsV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetsV6(LPWSTR ServerIpAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCPV6_IP_ARRAY* EnumInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferredMaximum", "EnumInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetClientsV6(LPWSTR ServerIpAddress, DHCP_IPV6_ADDRESS SubnetAddress, DHCP_RESUME_IPV6_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLIENT_INFO_ARRAY_V6* ClientInfo, DWORD* ClientsRead, DWORD* ClientsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetElementsV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetElementsV6(LPWSTR ServerIpAddress, DHCP_IPV6_ADDRESS SubnetAddress, DHCP_SUBNET_ELEMENT_TYPE_V6 EnumElementType, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V6* EnumElementInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "EnumElementType", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetAllOptionsV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetAllOptionsV6(LPWSTR ServerIpAddress, DWORD Flags, LPDHCP_ALL_OPTIONS* OptionStruct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetAllOptionValuesV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetAllOptionValuesV6(LPWSTR ServerIpAddress, DWORD Flags, LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo, LPDHCP_ALL_OPTION_VALUES* Values)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ScopeInfo", "Values"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetClientInfoV6(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_SEARCH_INFO_V6* SearchInfo, LPDHCP_CLIENT_INFO_V6* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetMibInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetMibInfoV6(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_MIB_INFO_V6* MibInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "MibInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetOptionInfoV6(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, WCHAR* ClassName, WCHAR* VendorName, LPDHCP_OPTION* OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionValueV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetOptionValueV6(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, WCHAR* ClassName, WCHAR* VendorName, LPDHCP_OPTION_SCOPE_INFO6* ScopeInfo, LPDHCP_OPTION_VALUE OptionValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetServerBindingInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetServerBindingInfoV6(DHCP_CONST WCHAR* ServerIpAddress, ULONG Flags, LPDHCPV6_BIND_ELEMENT_ARRAY* BindElementsInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "BindElementsInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetSubnetInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetSubnetInfoV6(LPWSTR ServerIpAddress, DHCP_IPV6_ADDRESS SubnetAddress, LPDHCP_SUBNET_INFO_V6* SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpModifyClassV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpModifyClassV6(LPWSTR ServerIpAddress, DWORD ReservedMustBeZero, LPDHCP_CLASS_INFO_V6 ClassInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ReservedMustBeZero", "ClassInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveOptionV6(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, WCHAR* ClassName, WCHAR* VendorName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionValueV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveOptionValueV6(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, WCHAR* ClassName, WCHAR* VendorName, LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "ScopeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveSubnetElementV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveSubnetElementV6(LPWSTR ServerIpAddress, DHCP_IPV6_ADDRESS SubnetAddress, LPDHCP_SUBNET_ELEMENT_DATA_V6 RemoveElementInfo, DHCP_FORCE_FLAG ForceFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "RemoveElementInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerGetConfigV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerGetConfigV6(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo, LPDHCP_SERVER_CONFIG_INFO_V6* ConfigInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeInfo", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetClientInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetClientInfoV6(LPWSTR ServerIpAddress, LPDHCP_CLIENT_INFO_V6 ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetOptionInfoV6(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, WCHAR* ClassName, WCHAR* VendorName, LPDHCP_OPTION OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "ClassName", "VendorName", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValueV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetOptionValueV6(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionId, WCHAR* ClassName, WCHAR* VendorName, LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo, LPDHCP_OPTION_DATA OptionValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "ClassName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetServerBindingInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetServerBindingInfoV6(DHCP_CONST WCHAR* ServerIpAddress, ULONG Flags, LPDHCPV6_BIND_ELEMENT_ARRAY BindElementsInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "BindElementsInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetConfigV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerSetConfigV6(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_OPTION_SCOPE_INFO6 ScopeInfo, [DHCP_FIELDS_TO_SET] FieldsToSet, LPDHCP_SERVER_CONFIG_INFO_V6 ConfigInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeInfo", "FieldsToSet", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetSubnetInfoV6(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetSubnetInfoV6(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IPV6_ADDRESS SubnetAddress, LPDHCP_SUBNET_INFO_V6 SubnetInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "SubnetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddSubnetElement(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpAddSubnetElement(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_ELEMENT_DATA* AddElementInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "AddElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpAddSubnetElementV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpAddSubnetElementV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_ELEMENT_DATA_V4* AddElementInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "AddElementInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpCreateOption(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpCreateOption(DHCP_CONST WCHAR* ServerIpAddress, DHCP_OPTION_ID OptionID, DHCP_CONST DHCP_OPTION* OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptions(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumOptions(DHCP_CONST WCHAR* ServerIpAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_OPTION_ARRAY* Options, DWORD* OptionsRead, DWORD* OptionsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferredMaximum", "Options", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumOptionValues(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumOptionValues(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_OPTION_VALUE_ARRAY* OptionValues, DWORD* OptionsRead, DWORD* OptionsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeInfo", "ResumeHandle", "PreferredMaximum", "OptionValues", "OptionsRead", "OptionsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetClientsV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetClientsV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLIENT_INFO_ARRAY_V4* ClientInfo, DWORD* ClientsRead, DWORD* ClientsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetElements(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetElements(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_SUBNET_ELEMENT_TYPE EnumElementType, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_SUBNET_ELEMENT_INFO_ARRAY* EnumElementInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "EnumElementType", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpEnumSubnetElementsV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpEnumSubnetElementsV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_SUBNET_ELEMENT_TYPE EnumElementType, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_SUBNET_ELEMENT_INFO_ARRAY_V4* EnumElementInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "EnumElementType", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetAllOptions(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetAllOptions(LPWSTR ServerIpAddress, DWORD Flags, LPDHCP_ALL_OPTIONS* OptionStruct)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionStruct"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetClientOptions(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetClientOptions(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS ClientIpAddress, DHCP_IP_MASK ClientSubnetMask, LPDHCP_OPTION_LIST* ClientOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientIpAddress", "ClientSubnetMask", "ClientOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetOptionInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetOptionInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_OPTION_ID OptionID, LPDHCP_OPTION* OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetServerSpecificStrings(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetServerSpecificStrings(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_SERVER_SPECIFIC_STRINGS* ServerSpecificStrings)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ServerSpecificStrings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpGetThreadOptions(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpGetThreadOptions(LPDWORD pFlags, LPVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprAddV4PolicyCondition(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpHlprAddV4PolicyCondition(LPDHCP_POLICY Policy, DWORD ParentExpr, DHCP_POL_ATTR_TYPE Type, DWORD OptionID, DWORD SubOptionID, LPWSTR VendorName, DHCP_POL_COMPARATOR Operator, LPBYTE Value, DWORD ValueLength, DWORD* ConditionIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Policy", "ParentExpr", "Type", "OptionID", "SubOptionID", "VendorName", "Operator", "Value", "ValueLength", "ConditionIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprAddV4PolicyExpr(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpHlprAddV4PolicyExpr(LPDHCP_POLICY Policy, DWORD ParentExpr, DHCP_POL_LOGIC_OPER Operator, DWORD* ExprIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Policy", "ParentExpr", "Operator", "ExprIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprAddV4PolicyRange(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpHlprAddV4PolicyRange(LPDHCP_POLICY Policy, LPDHCP_IP_RANGE Range)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Policy", "Range"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprCreateV4Policy(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpHlprCreateV4Policy(LPWSTR PolicyName, BOOL fGlobalPolicy, DHCP_IP_ADDRESS Subnet, DWORD ProcessingOrder, DHCP_POL_LOGIC_OPER RootOperator, LPWSTR Description, BOOL Enabled, LPDHCP_POLICY* Policy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyName", "fGlobalPolicy", "Subnet", "ProcessingOrder", "RootOperator", "Description", "Enabled", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprFreeV4Policy(jitter):
    """"
    [Dhcpsapi.dll] VOID DhcpHlprFreeV4Policy(LPDHCP_POLICY Policy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprIsV4PolicySingleUC(jitter):
    """"
    [Dhcpsapi.dll] BOOL DhcpHlprIsV4PolicySingleUC(LPDHCP_POLICY Policy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprIsV4PolicyValid(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpHlprIsV4PolicyValid(LPDHCP_POLICY pPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprIsV4PolicyWellFormed(jitter):
    """"
    [Dhcpsapi.dll] BOOL DhcpHlprIsV4PolicyWellFormed(LPDHCP_POLICY pPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprModifyV4PolicyExpr(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpHlprModifyV4PolicyExpr(LPDHCP_POLICY Policy, DHCP_POL_LOGIC_OPER Operator)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Policy", "Operator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpHlprResetV4PolicyExpr(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpHlprResetV4PolicyExpr(LPDHCP_POLICY Policy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOption(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveOption(DHCP_CONST WCHAR* ServerIpAddress, DHCP_OPTION_ID OptionID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveOptionValue(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveOptionValue(DHCP_CONST WCHAR* ServerIpAddress, DHCP_OPTION_ID OptionID, DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "ScopeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveSubnetElement(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveSubnetElement(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_ELEMENT_DATA* RemoveElementInfo, DHCP_FORCE_FLAG ForceFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "RemoveElementInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpRemoveSubnetElementV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpRemoveSubnetElementV4(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_CONST DHCP_SUBNET_ELEMENT_DATA_V4* RemoveElementInfo, DHCP_FORCE_FLAG ForceFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "RemoveElementInfo", "ForceFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpScanDatabase(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpScanDatabase(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DWORD FixFlag, LPDHCP_SCAN_LIST* ScanList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "FixFlag", "ScanList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerBackupDatabase(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerBackupDatabase(LPWSTR ServerIpAddress, LPWSTR Path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerGetConfig(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerGetConfig(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_SERVER_CONFIG_INFO* ConfigInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerGetConfigV4(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerGetConfigV4(DHCP_CONST WCHAR* ServerIpAddress, LPDHCP_SERVER_CONFIG_INFO_V4* ConfigInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerQueryAttribute(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerQueryAttribute(LPWSTR ServerIpAddr, ULONG dwReserved, DHCP_ATTRIB_ID DhcpAttribId, LPDHCP_ATTRIB* pDhcpAttrib)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddr", "dwReserved", "DhcpAttribId", "pDhcpAttrib"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerQueryAttributes(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerQueryAttributes(LPWSTR ServerIpAddr, ULONG dwReserved, ULONG dwAttribCount, DHCP_ATTRIB_ID [] pDhcpAttribs, LPDHCP_ATTRIB_ARRAY* pDhcpAttribArr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddr", "dwReserved", "dwAttribCount", "pDhcpAttribs", "pDhcpAttribArr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerRestoreDatabase(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerRestoreDatabase(LPWSTR ServerIpAddress, LPWSTR Path)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpServerSetConfig(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpServerSetConfig(DHCP_CONST WCHAR* ServerIpAddress, [DHCP_FIELDS_TO_SET] FieldsToSet, LPDHCP_SERVER_CONFIG_INFO ConfigInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "FieldsToSet", "ConfigInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetOptionInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_OPTION_ID OptionID, DHCP_CONST DHCP_OPTION* OptionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "OptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValue(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetOptionValue(DHCP_CONST WCHAR* ServerIpAddress, DHCP_OPTION_ID OptionID, DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo, DHCP_CONST DHCP_OPTION_DATA* OptionValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "OptionID", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValues(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetOptionValues(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_OPTION_SCOPE_INFO* ScopeInfo, DHCP_CONST DHCP_OPTION_VALUE_ARRAY* OptionValues)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeInfo", "OptionValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetOptionValuesV5(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetOptionValuesV5(LPWSTR ServerIpAddress, DWORD Flags, LPWSTR ClassName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, LPDHCP_OPTION_VALUE_ARRAY OptionValues)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ClassName", "VendorName", "ScopeInfo", "OptionValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpSetThreadOptions(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpSetThreadOptions(DWORD Flags, LPVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverAddScopeToRelationship(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverAddScopeToRelationship(LPWSTR ServerIpAddress, LPDHCP_FAILOVER_RELATIONSHIP pRelationship)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverCreateRelationship(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverCreateRelationship(LPWSTR ServerIpAddress, LPDHCP_FAILOVER_RELATIONSHIP pRelationship)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverDeleteRelationship(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverDeleteRelationship(LPWSTR ServerIpAddress, LPWSTR pRelationshipName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationshipName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverDeleteScopeFromRelationship(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverDeleteScopeFromRelationship(LPWSTR ServerIpAddress, LPDHCP_FAILOVER_RELATIONSHIP pRelationship)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverEnumRelationship(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverEnumRelationship(LPWSTR ServerIpAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD preferredMaximum, LPDHCP_FAILOVER_RELATIONSHIP_ARRAY* pRelationship, LPDWORD relationshipRead, LPDWORD relationshipTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "preferredMaximum", "pRelationship", "relationshipRead", "relationshipTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetAddressStatus(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverGetAddressStatus(LPWSTR ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, LPDWORD pStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "pStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetClientInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverGetClientInfo(LPWSTR ServerIpAddress, DHCP_CONST DHCP_SEARCH_INFO* SearchInfo, LPDHCPV4_FAILOVER_CLIENT_INFO* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetRelationship(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverGetRelationship(LPWSTR ServerIpAddress, LPWSTR pRelationshipName, LPDHCP_FAILOVER_RELATIONSHIP* pRelationship)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pRelationshipName", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetScopeRelationship(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverGetScopeRelationship(LPWSTR ServerIpAddress, DHCP_IP_ADDRESS scopeId, LPDHCP_FAILOVER_RELATIONSHIP* pRelationship)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "scopeId", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetScopeStatistics(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverGetScopeStatistics(LPWSTR ServerIpAddress, DHCP_IP_ADDRESS scopeId, LPDHCP_FAILOVER_STATISTICS* pStats)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "scopeId", "pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverGetSystemTime(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverGetSystemTime(LPWSTR ServerIpAddress, LPDWORD pTime)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverSetRelationship(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverSetRelationship(LPWSTR ServerIpAddress, DWORD flags, LPDHCP_FAILOVER_RELATIONSHIP pRelationship)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "flags", "pRelationship"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4FailoverTriggerAddrAllocation(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4FailoverTriggerAddrAllocation(LPWSTR ServerIpAddress, LPWSTR pFailRelName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pFailRelName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetFreeIPAddress(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4GetFreeIPAddress(LPWSTR ServerIpAddress, DHCP_IP_ADDRESS ScopeId, DHCP_IP_ADDRESS startIP, DHCP_IP_ADDRESS endIP, DWORD numFreeAddrReq, LPDHCP_IP_ARRAY* IPAddrList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeId", "startIP", "endIP", "numFreeAddrReq", "IPAddrList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4EnumSubnetClients(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4EnumSubnetClients(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_CLIENT_INFO_PB_ARRAY* ClientInfo, DWORD* ClientsRead, DWORD* ClientsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "ClientInfo", "ClientsRead", "ClientsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4EnumSubnetReservations(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4EnumSubnetReservations(DHCP_CONST WCHAR* ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, DHCP_RESUME_HANDLE* ResumeHandle, DWORD PreferredMaximum, LPDHCP_RESERVATION_INFO_ARRAY* EnumElementInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "ResumeHandle", "PreferredMaximum", "EnumElementInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4CreateClientInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4CreateClientInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST LPDHCP_CLIENT_INFO_PB ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetClientInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4GetClientInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST DHCP_SEARCH_INFO* SearchInfo, LPDHCP_CLIENT_INFO_PB* ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SearchInfo", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4RemoveOptionValue(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4RemoveOptionValue(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, LPWSTR PolicyName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "PolicyName", "VendorName", "ScopeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetAllOptionValues(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4GetAllOptionValues(LPWSTR ServerIpAddress, DWORD Flags, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, LPDHCP_ALL_OPTION_VALUES_PB* Values)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "ScopeInfo", "Values"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4SetOptionValues(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4SetOptionValues(LPWSTR ServerIpAddress, DWORD Flags, LPWSTR PolicyName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, LPDHCP_OPTION_VALUE_ARRAY OptionValues)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "PolicyName", "VendorName", "ScopeInfo", "OptionValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4SetOptionValue(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4SetOptionValue(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionId, LPWSTR PolicyName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, LPDHCP_OPTION_DATA OptionValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionId", "PolicyName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetOptionValue(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4GetOptionValue(LPWSTR ServerIpAddress, DWORD Flags, DHCP_OPTION_ID OptionID, LPWSTR PolicyName, LPWSTR VendorName, LPDHCP_OPTION_SCOPE_INFO ScopeInfo, LPDHCP_OPTION_VALUE* OptionValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "Flags", "OptionID", "PolicyName", "VendorName", "ScopeInfo", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4CreatePolicy(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4CreatePolicy(LPWSTR ServerIpAddress, LPDHCP_POLICY pPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "pPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4EnumPolicies(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4EnumPolicies(LPWSTR ServerIpAddress, LPDWORD ResumeHandle, DWORD PreferredMaximum, BOOL fGlobalPolicy, DHCP_IP_ADDRESS SubnetAddress, LPDHCP_POLICY_ARRAY* EnumInfo, DWORD* ElementsRead, DWORD* ElementsTotal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ResumeHandle", "PreferredMaximum", "fGlobalPolicy", "SubnetAddress", "EnumInfo", "ElementsRead", "ElementsTotal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4GetPolicy(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4GetPolicy(LPWSTR ServerIpAddress, BOOL fGlobalPolicy, DHCP_IP_ADDRESS SubnetAddress, LPWSTR PolicyName, LPDHCP_POLICY* Policy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fGlobalPolicy", "SubnetAddress", "PolicyName", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4SetPolicy(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4SetPolicy(LPWSTR ServerIpAddress, DWORD FieldsModified, BOOL fGlobalPolicy, DHCP_IP_ADDRESS SubnetAddress, LPWSTR PolicyName, LPDHCP_POLICY Policy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "FieldsModified", "fGlobalPolicy", "SubnetAddress", "PolicyName", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4DeletePolicy(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4DeletePolicy(LPWSTR ServerIpAddress, BOOL fGlobalPolicy, DHCP_IP_ADDRESS SubnetAddress, LPWSTR PolicyName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fGlobalPolicy", "SubnetAddress", "PolicyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4SetPolicyEnforcement(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4SetPolicyEnforcement(LPWSTR ServerIpAddress, BOOL fGlobalPolicy, DHCP_IP_ADDRESS SubnetAddress, BOOL Enable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fGlobalPolicy", "SubnetAddress", "Enable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4QueryPolicyEnforcement(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4QueryPolicyEnforcement(LPWSTR ServerIpAddress, BOOL fGlobalPolicy, DHCP_IP_ADDRESS SubnetAddress, BOOL* Enabled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fGlobalPolicy", "SubnetAddress", "Enabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4AddPolicyRange(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4AddPolicyRange(LPWSTR ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, LPWSTR PolicyName, LPDHCP_IP_RANGE Range)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "PolicyName", "Range"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV4RemovePolicyRange(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV4RemovePolicyRange(LPWSTR ServerIpAddress, DHCP_IP_ADDRESS SubnetAddress, LPWSTR PolicyName, LPDHCP_IP_RANGE Range)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "SubnetAddress", "PolicyName", "Range"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6CreateClientInfo(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV6CreateClientInfo(DHCP_CONST WCHAR* ServerIpAddress, DHCP_CONST LPDHCP_CLIENT_INFO_V6 ClientInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ClientInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6GetFreeIPAddress(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV6GetFreeIPAddress(LPWSTR ServerIpAddress, DHCP_IPV6_ADDRESS ScopeId, DHCP_IPV6_ADDRESS startIP, DHCP_IPV6_ADDRESS endIP, DWORD numFreeAddrReq, LPDHCPV6_IP_ARRAY* IPAddrList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "ScopeId", "startIP", "endIP", "numFreeAddrReq", "IPAddrList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6GetStatelessStatistics(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV6GetStatelessStatistics(LPWSTR ServerIpAddress, LPDHCPV6_STATELESS_STATS* StatelessStats)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "StatelessStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6GetStatelessStoreParams(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV6GetStatelessStoreParams(LPWSTR ServerIpAddress, BOOL fServerLevel, DHCP_IPV6_ADDRESS SubnetAddress, LPDHCPV6_STATELESS_PARAMS* Params)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fServerLevel", "SubnetAddress", "Params"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dhcpsapi_DhcpV6SetStatelessStoreParams(jitter):
    """"
    [Dhcpsapi.dll] [ERROR_CODE] DhcpV6SetStatelessStoreParams(LPWSTR ServerIpAddress, BOOL fServerLevel, DHCP_IPV6_ADDRESS SubnetAddress, DWORD FieldModified, LPDHCPV6_STATELESS_PARAMS Params)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ServerIpAddress", "fServerLevel", "SubnetAddress", "FieldModified", "Params"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
