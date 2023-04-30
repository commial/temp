
def api-ms-win-net-isolation-l1_NetworkIsolationDiagnoseConnectFailureAndGetInfo(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] [ERROR_CODE] NetworkIsolationDiagnoseConnectFailureAndGetInfo(LPCWSTR wszServerName, NETISO_ERROR_TYPE* netIsoError)
    """
    ret_ad, args = jitter.func_args_stdcall(["wszServerName", "netIsoError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationEnumAppContainers(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] [ERROR_CODE] NetworkIsolationEnumAppContainers(DWORD Flags, DWORD* pdwNumPublicAppCs, PINET_FIREWALL_APP_CONTAINER* ppPublicAppCs)
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "pdwNumPublicAppCs", "ppPublicAppCs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationEnumerateAppContainerRules(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] HRESULT NetworkIsolationEnumerateAppContainerRules(IEnumVARIANT** newEnum)
    """
    ret_ad, args = jitter.func_args_stdcall(["newEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationFreeAppContainers(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] [ERROR_CODE] NetworkIsolationFreeAppContainers(PINET_FIREWALL_APP_CONTAINER pPublicAppCs)
    """
    ret_ad, args = jitter.func_args_stdcall(["pPublicAppCs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationGetAppContainerConfig(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] [ERROR_CODE] NetworkIsolationGetAppContainerConfig(DWORD* pdwNumPublicAppCs, PSID_AND_ATTRIBUTES* appContainerSids)
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwNumPublicAppCs", "appContainerSids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationRegisterForAppContainerChanges(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] [ERROR_CODE] NetworkIsolationRegisterForAppContainerChanges(DWORD flags, PAC_CHANGES_CALLBACK_FN callback, PVOID context, HANDLE* registrationObject)
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "callback", "context", "registrationObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationSetAppContainerConfig(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] [ERROR_CODE] NetworkIsolationSetAppContainerConfig(DWORD dwNumPublicAppCs, PSID_AND_ATTRIBUTES appContainerSids)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwNumPublicAppCs", "appContainerSids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationSetupAppContainerBinaries(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] HRESULT NetworkIsolationSetupAppContainerBinaries(PSID applicationContainerSid, LPCWSTR packageFullName, LPCWSTR packageFolder, LPCWSTR displayName, BOOL bBinariesFullyComputed, LPCWSTR* binaries, DWORD binariesCount)
    """
    ret_ad, args = jitter.func_args_stdcall(["applicationContainerSid", "packageFullName", "packageFolder", "displayName", "bBinariesFullyComputed", "binaries", "binariesCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def api-ms-win-net-isolation-l1_NetworkIsolationUnregisterForAppContainerChanges(jitter):
    """
    [api-ms-win-net-isolation-l1.dll] [ERROR_CODE] NetworkIsolationUnregisterForAppContainerChanges(HANDLE registrationObject)
    """
    ret_ad, args = jitter.func_args_stdcall(["registrationObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
