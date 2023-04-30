###### Enums ######
NETISO_ERROR_TYPE = {
    "NETISO_ERROR_TYPE_NONE": 0x00,
    "NETISO_ERROR_TYPE_PRIVATE_NETWORK": 0x01,
    "NETISO_ERROR_TYPE_INTERNET_CLIENT": 0x02,
    "NETISO_ERROR_TYPE_INTERNET_CLIENT_SERVER": 0x03,
}
NETISO_ERROR_TYPE_INV = {
    0x00: "NETISO_ERROR_TYPE_NONE",
    0x01: "NETISO_ERROR_TYPE_PRIVATE_NETWORK",
    0x02: "NETISO_ERROR_TYPE_INTERNET_CLIENT",
    0x03: "NETISO_ERROR_TYPE_INTERNET_CLIENT_SERVER",
}

###################

###### Types ######
PAC_CHANGES_CALLBACK_FN = LPVOID
NETISO_ERROR_TYPE = UINT
NETISO_ERROR_TYPE_PTR = Ptr("<I", NETISO_ERROR_TYPE())

class INET_FIREWALL_AC_CAPABILITIES(MemStruct):
    fields = [
        ("count", DWORD()),
        ("capabilities", SID_AND_ATTRIBUTES_PTR()),
    ]


class INET_FIREWALL_AC_BINARIES(MemStruct):
    fields = [
        ("count", DWORD()),
        ("binaries", LPWSTR_PTR()),
    ]


class INET_FIREWALL_APP_CONTAINER(MemStruct):
    fields = [
        ("appContainerSid", SID_PTR()),
        ("userSid", SID_PTR()),
        ("appContainerName", LPWSTR()),
        ("displayName", LPWSTR()),
        ("description", LPWSTR()),
        ("capabilities", INET_FIREWALL_AC_CAPABILITIES()),
        ("binaries", INET_FIREWALL_AC_BINARIES()),
        ("workingDirectory", LPWSTR()),
        ("packageFullName", LPWSTR()),
    ]

PINET_FIREWALL_APP_CONTAINER = Ptr("<I", INET_FIREWALL_APP_CONTAINER())
PINET_FIREWALL_APP_CONTAINER_PTR = Ptr("<I", PINET_FIREWALL_APP_CONTAINER())

###################

###### Functions ######

def api-ms-win-net-isolation-l1_NetworkIsolationDiagnoseConnectFailureAndGetInfo(jitter):
    """
    [ERROR_CODE] NetworkIsolationDiagnoseConnectFailureAndGetInfo(
        LPCWSTR wszServerName,
        NETISO_ERROR_TYPE* netIsoError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wszServerName", "netIsoError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationEnumAppContainers(jitter):
    """
    [ERROR_CODE] NetworkIsolationEnumAppContainers(
        DWORD Flags,
        DWORD* pdwNumPublicAppCs,
        PINET_FIREWALL_APP_CONTAINER* ppPublicAppCs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "pdwNumPublicAppCs", "ppPublicAppCs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationEnumerateAppContainerRules(jitter):
    """
    HRESULT NetworkIsolationEnumerateAppContainerRules(
        IEnumVARIANT** newEnum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["newEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationFreeAppContainers(jitter):
    """
    [ERROR_CODE] NetworkIsolationFreeAppContainers(
        PINET_FIREWALL_APP_CONTAINER pPublicAppCs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPublicAppCs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationGetAppContainerConfig(jitter):
    """
    [ERROR_CODE] NetworkIsolationGetAppContainerConfig(
        DWORD* pdwNumPublicAppCs,
        PSID_AND_ATTRIBUTES* appContainerSids
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwNumPublicAppCs", "appContainerSids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationRegisterForAppContainerChanges(jitter):
    """
    [ERROR_CODE] NetworkIsolationRegisterForAppContainerChanges(
        DWORD flags,
        PAC_CHANGES_CALLBACK_FN callback,
        PVOID context,
        HANDLE* registrationObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "callback", "context", "registrationObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationSetAppContainerConfig(jitter):
    """
    [ERROR_CODE] NetworkIsolationSetAppContainerConfig(
        DWORD dwNumPublicAppCs,
        PSID_AND_ATTRIBUTES appContainerSids
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwNumPublicAppCs", "appContainerSids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationSetupAppContainerBinaries(jitter):
    """
    HRESULT NetworkIsolationSetupAppContainerBinaries(
        PSID applicationContainerSid,
        LPCWSTR packageFullName,
        LPCWSTR packageFolder,
        LPCWSTR displayName,
        BOOL bBinariesFullyComputed,
        LPCWSTR* binaries,
        DWORD binariesCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["applicationContainerSid", "packageFullName", "packageFolder", "displayName", "bBinariesFullyComputed", "binaries", "binariesCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationUnregisterForAppContainerChanges(jitter):
    """
    [ERROR_CODE] NetworkIsolationUnregisterForAppContainerChanges(
        HANDLE registrationObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["registrationObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
