
def iscsidsc_AddISNSServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddISNSServer(
        PTCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddISNSServerA(jitter):
    iscsidsc_AddISNSServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddISNSServerW(jitter):
    iscsidsc_AddISNSServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddIScsiConnection(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddIScsiConnection(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        PVOID Reserved,
        ULONG InitiatorPortNumber,
        PISCSI_TARGET_PORTAL TargetPortal,
        ISCSI_SECURITY_FLAGS SecurityFlags,
        PISCSI_LOGIN_OPTIONS LoginOptions,
        ULONG KeySize,
        PCHAR Key,
        PISCSI_UNIQUE_CONNECTION_ID ConnectionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Reserved", "InitiatorPortNumber", "TargetPortal", "SecurityFlags", "LoginOptions", "KeySize", "Key", "ConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiConnectionA(jitter):
    iscsidsc_AddIScsiConnection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddIScsiConnectionW(jitter):
    iscsidsc_AddIScsiConnection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddIScsiSendTargetPortal(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddIScsiSendTargetPortal(
        PTCHAR InitiatorName,
        ULONG InitiatorPortNumber,
        PISCSI_LOGIN_OPTIONS LoginOptions,
        ISCSI_SECURITY_FLAGS SecurityFlags,
        PISCSI_TARGET_PORTAL Portal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "InitiatorPortNumber", "LoginOptions", "SecurityFlags", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiSendTargetPortalA(jitter):
    iscsidsc_AddIScsiSendTargetPortal(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddIScsiSendTargetPortalW(jitter):
    iscsidsc_AddIScsiSendTargetPortal(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddIScsiStaticTarget(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddIScsiStaticTarget(
        PTCHAR TargetName,
        PTCHAR TargetAlias,
        ISCSI_TARGET_FLAGS TargetFlags,
        BOOLEAN Persist,
        PISCSI_TARGET_MAPPING Mappings,
        PISCSI_LOGIN_OPTIONS LoginOptions,
        PISCSI_TARGET_PORTAL_GROUP PortalGroup
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "TargetAlias", "TargetFlags", "Persist", "Mappings", "LoginOptions", "PortalGroup"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiStaticTargetA(jitter):
    iscsidsc_AddIScsiStaticTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddIScsiStaticTargetW(jitter):
    iscsidsc_AddIScsiStaticTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddPersistentIScsiDevice(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddPersistentIScsiDevice(
        PTCHAR VolumePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VolumePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddPersistentIScsiDeviceA(jitter):
    iscsidsc_AddPersistentIScsiDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddPersistentIScsiDeviceW(jitter):
    iscsidsc_AddPersistentIScsiDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_AddRadiusServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS AddRadiusServer(
        PWCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddRadiusServerA(jitter):
    iscsidsc_AddRadiusServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_AddRadiusServerW(jitter):
    iscsidsc_AddRadiusServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ClearPersistentIScsiDevices(jitter):
    """
    ISDSC_STATUS ClearPersistentIScsiDevices()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetDevicesForIScsiSession(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetDevicesForIScsiSession(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        ULONG* DeviceCount,
        PISCSI_DEVICE_ON_SESSION Devices
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "DeviceCount", "Devices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetDevicesForIScsiSessionA(jitter):
    iscsidsc_GetDevicesForIScsiSession(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetDevicesForIScsiSessionW(jitter):
    iscsidsc_GetDevicesForIScsiSession(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiIKEInfo(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetIScsiIKEInfo(
        PTCHAR InitiatorName,
        ULONG PortNumber,
        PULONG Reserved,
        PIKE_AUTHENTICATION_INFORMATION AuthInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "PortNumber", "Reserved", "AuthInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiIKEInfoA(jitter):
    iscsidsc_GetIScsiIKEInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetIScsiIKEInfoW(jitter):
    iscsidsc_GetIScsiIKEInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiInitiatorNodeName(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetIScsiInitiatorNodeName(
        PTCHAR InitiatorNodeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorNodeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiInitiatorNodeNameA(jitter):
    iscsidsc_GetIScsiInitiatorNodeName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetIScsiInitiatorNodeNameW(jitter):
    iscsidsc_GetIScsiInitiatorNodeName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiSessionList(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetIScsiSessionList(
        ULONG* BufferSize,
        ULONG* SessionCount,
        PISCSI_SESSION_INFO SessionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "SessionCount", "SessionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiSessionListA(jitter):
    iscsidsc_GetIScsiSessionList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetIScsiSessionListW(jitter):
    iscsidsc_GetIScsiSessionList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiTargetInformation(jitter, get_str, set_str):
    """
    ISDSC_STATUS GetIScsiTargetInformation(
        PTCHAR TargetName,
        PTCHAR DiscoveryMechanism,
        TARGET_INFORMATION_CLASS InfoClass,
        PULONG BufferSize,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "DiscoveryMechanism", "InfoClass", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiTargetInformationA(jitter):
    iscsidsc_GetIScsiTargetInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_GetIScsiTargetInformationW(jitter):
    iscsidsc_GetIScsiTargetInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_GetIScsiVersionInformation(jitter):
    """
    ISDSC_STATUS GetIScsiVersionInformation(
        PISCSI_VERSION_INFO VersionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VersionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_LoginIScsiTarget(jitter, get_str, set_str):
    """
    ISDSC_STATUS LoginIScsiTarget(
        PTCHAR TargetName,
        BOOLEAN IsInformationalSession,
        PTCHAR InitiatorName,
        ULONG InitiatorPortNumber,
        PISCSI_TARGET_PORTAL TargetPortal,
        ISCSI_SECURITY_FLAGS SecurityFlags,
        PISCSI_TARGET_MAPPING Mappings,
        PISCSI_LOGIN_OPTIONS LoginOptions,
        ULONG KeySize,
        PCHAR Key,
        BOOLEAN IsPersistent,
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        PISCSI_UNIQUE_CONNECTION_ID UniqueConnectionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "IsInformationalSession", "InitiatorName", "InitiatorPortNumber", "TargetPortal", "SecurityFlags", "Mappings", "LoginOptions", "KeySize", "Key", "IsPersistent", "UniqueSessionId", "UniqueConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_LoginIScsiTargetA(jitter):
    iscsidsc_LoginIScsiTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_LoginIScsiTargetW(jitter):
    iscsidsc_LoginIScsiTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_LogoutIScsiTarget(jitter):
    """
    ISDSC_STATUS LogoutIScsiTarget(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RefreshISNSServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS RefreshISNSServer(
        PTCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RefreshISNSServerA(jitter):
    iscsidsc_RefreshISNSServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RefreshISNSServerW(jitter):
    iscsidsc_RefreshISNSServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RefreshIScsiSendTargetPortal(jitter, get_str, set_str):
    """
    ISDSC_STATUS RefreshIScsiSendTargetPortal(
        PTCHAR InitiatorInstance,
        ULONG InitiatorPortNumber,
        PISCSI_TARGET_PORTAL Portal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RefreshIScsiSendTargetPortalA(jitter):
    iscsidsc_RefreshIScsiSendTargetPortal(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RefreshIScsiSendTargetPortalW(jitter):
    iscsidsc_RefreshIScsiSendTargetPortal(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveISNSServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveISNSServer(
        PTCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveISNSServerA(jitter):
    iscsidsc_RemoveISNSServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveISNSServerW(jitter):
    iscsidsc_RemoveISNSServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveIScsiConnection(jitter):
    """
    ISDSC_STATUS RemoveIScsiConnection(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        PISCSI_UNIQUE_CONNECTION_ID UniqueConnectionId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "UniqueConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiPersistentTarget(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveIScsiPersistentTarget(
        PTCHAR InitiatorInstance,
        ULONG InitiatorPortNumber,
        PTCHAR TargetName,
        PISCSI_TARGET_PORTAL Portal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "TargetName", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiPersistentTargetA(jitter):
    iscsidsc_RemoveIScsiPersistentTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveIScsiPersistentTargetW(jitter):
    iscsidsc_RemoveIScsiPersistentTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveIScsiSendTargetPortal(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveIScsiSendTargetPortal(
        PTCHAR InitiatorInstance,
        ULONG InitiatorPortNumber,
        PISCSI_TARGET_PORTAL Portal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiSendTargetPortalA(jitter):
    iscsidsc_RemoveIScsiSendTargetPortal(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveIScsiSendTargetPortalW(jitter):
    iscsidsc_RemoveIScsiSendTargetPortal(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveIScsiStaticTarget(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveIScsiStaticTarget(
        PTCHAR TargetName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiStaticTargetA(jitter):
    iscsidsc_RemoveIScsiStaticTarget(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveIScsiStaticTargetW(jitter):
    iscsidsc_RemoveIScsiStaticTarget(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemovePersistentIScsiDevice(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemovePersistentIScsiDevice(
        PTCHAR VolumePath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VolumePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemovePersistentIScsiDeviceA(jitter):
    iscsidsc_RemovePersistentIScsiDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemovePersistentIScsiDeviceW(jitter):
    iscsidsc_RemovePersistentIScsiDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_RemoveRadiusServer(jitter, get_str, set_str):
    """
    ISDSC_STATUS RemoveRadiusServer(
        PTCHAR Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveRadiusServerA(jitter):
    iscsidsc_RemoveRadiusServer(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_RemoveRadiusServerW(jitter):
    iscsidsc_RemoveRadiusServer(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportActiveIScsiTargetMappings(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportActiveIScsiTargetMappings(
        PULONG BufferSize,
        PULONG MappingCount,
        PISCSI_TARGET_MAPPING Mappings
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "MappingCount", "Mappings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportActiveIScsiTargetMappingsA(jitter):
    iscsidsc_ReportActiveIScsiTargetMappings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportActiveIScsiTargetMappingsW(jitter):
    iscsidsc_ReportActiveIScsiTargetMappings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportISNSServerList(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportISNSServerList(
        PULONG BufferSizeInChar,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportISNSServerListA(jitter):
    iscsidsc_ReportISNSServerList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportISNSServerListW(jitter):
    iscsidsc_ReportISNSServerList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiInitiatorList(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiInitiatorList(
        ULONG* BufferSize,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiInitiatorListA(jitter):
    iscsidsc_ReportIScsiInitiatorList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiInitiatorListW(jitter):
    iscsidsc_ReportIScsiInitiatorList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiPersistentLogins(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiPersistentLogins(
        ULONG* Count,
        PPERSISTENT_ISCSI_LOGIN_INFO PersistentLoginInfo,
        PULONG BufferSizeInBytes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Count", "PersistentLoginInfo", "BufferSizeInBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiPersistentLoginsA(jitter):
    iscsidsc_ReportIScsiPersistentLogins(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiPersistentLoginsW(jitter):
    iscsidsc_ReportIScsiPersistentLogins(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiSendTargetPortals(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiSendTargetPortals(
        PULONG PortalCount,
        PISCSI_TARGET_PORTAL_INFO PortalInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortalCount", "PortalInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiSendTargetPortalsA(jitter):
    iscsidsc_ReportIScsiSendTargetPortals(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiSendTargetPortalsW(jitter):
    iscsidsc_ReportIScsiSendTargetPortals(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiSendTargetPortalsEx(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiSendTargetPortalsEx(
        PULONG PortalCount,
        PULONG PortalInfoSize,
        PISCSI_TARGET_PORTAL_INFO_EX PortalInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortalCount", "PortalInfoSize", "PortalInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiSendTargetPortalsExA(jitter):
    iscsidsc_ReportIScsiSendTargetPortalsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiSendTargetPortalsExW(jitter):
    iscsidsc_ReportIScsiSendTargetPortalsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiTargets(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiTargets(
        BOOLEAN ForceUpdate,
        PULONG BufferSize,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ForceUpdate", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiTargetsA(jitter):
    iscsidsc_ReportIScsiTargets(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiTargetsW(jitter):
    iscsidsc_ReportIScsiTargets(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportIScsiTargetPortals(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportIScsiTargetPortals(
        PWCHAR InitiatorName,
        PWCHAR TargetName,
        PUSHORT TargetPortalTag,
        PULONG ElementCount,
        PISCSI_TARGET_PORTAL Portals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "TargetName", "TargetPortalTag", "ElementCount", "Portals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiTargetPortalsA(jitter):
    iscsidsc_ReportIScsiTargetPortals(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportIScsiTargetPortalsW(jitter):
    iscsidsc_ReportIScsiTargetPortals(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportPersistentIScsiDevices(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportPersistentIScsiDevices(
        PULONG BufferSizeInChar,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportPersistentIScsiDevicesA(jitter):
    iscsidsc_ReportPersistentIScsiDevices(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportPersistentIScsiDevicesW(jitter):
    iscsidsc_ReportPersistentIScsiDevices(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_ReportRadiusServerList(jitter, get_str, set_str):
    """
    ISDSC_STATUS ReportRadiusServerList(
        PULONG BufferSizeInChar,
        PTCHAR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportRadiusServerListA(jitter):
    iscsidsc_ReportRadiusServerList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_ReportRadiusServerListW(jitter):
    iscsidsc_ReportRadiusServerList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_SendScsiInquiry(jitter):
    """
    ISDSC_STATUS SendScsiInquiry(
        PISCSI_UNIQUE_SESSION_ID* UniqueSessionId,
        ULONGLONG Lun,
        UCHAR EvpdCmddt,
        UCHAR PageCode,
        PUCHAR* ScsiStatus,
        PULONG* ReponseSize,
        PUCHAR ReponseBuffer,
        PULONG* SenseSize,
        PUCHAR SenseBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Lun", "EvpdCmddt", "PageCode", "ScsiStatus", "ReponseSize", "ReponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SendScsiReadCapacity(jitter):
    """
    ISDSC_STATUS SendScsiReadCapacity(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        ULONGLONG Lun,
        PUCHAR* ScsiStatus,
        PULONG* ResponseSize,
        PUCHAR ResponseBuffer,
        PULONG* SenseSize,
        PUCHAR SenseBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Lun", "ScsiStatus", "ResponseSize", "ResponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SendScsiReportLuns(jitter):
    """
    ISDSC_STATUS SendScsiReportLuns(
        PISCSI_UNIQUE_SESSION_ID UniqueSessionId,
        PUCHAR* ScsiStatus,
        PULONG* ResponseSize,
        PUCHAR ResponseBuffer,
        PULONG* SenseSize,
        PUCHAR SenseBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "ScsiStatus", "ResponseSize", "ResponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiGroupPresharedKey(jitter):
    """
    ISDSC_STATUS SetIScsiGroupPresharedKey(
        ULONG KeyLength,
        PUCHAR Key,
        BOOLEAN Persist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyLength", "Key", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiIKEInfo(jitter, get_str, set_str):
    """
    ISDSC_STATUS SetIScsiIKEInfo(
        PTCHAR InitiatorName,
        ULONG PortNumber,
        PIKE_AUTHENTICATION_INFORMATION AuthInfo,
        BOOLEAN Persist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "PortNumber", "AuthInfo", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiIKEInfoA(jitter):
    iscsidsc_SetIScsiIKEInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_SetIScsiIKEInfoW(jitter):
    iscsidsc_SetIScsiIKEInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_SetIScsiInitiatorCHAPSharedSecret(jitter):
    """
    ISDSC_STATUS SetIScsiInitiatorCHAPSharedSecret(
        ULONG SharedSecretLength,
        PUCHAR SharedSecret
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SharedSecretLength", "SharedSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorRADIUSSharedSecret(jitter):
    """
    ISDSC_STATUS SetIScsiInitiatorRADIUSSharedSecret(
        ULONG SharedSecretLength,
        PUCHAR SharedSecret
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SharedSecretLength", "SharedSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorNodeName(jitter, get_str, set_str):
    """
    ISDSC_STATUS SetIScsiInitiatorNodeName(
        PTCHAR InitiatorNodeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorNodeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorNodeNameA(jitter):
    iscsidsc_SetIScsiInitiatorNodeName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_SetIScsiInitiatorNodeNameW(jitter):
    iscsidsc_SetIScsiInitiatorNodeName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_SetIScsiTunnelModeOuterAddress(jitter, get_str, set_str):
    """
    ISDSC_STATUS SetIScsiTunnelModeOuterAddress(
        PTCHAR InitiatorName,
        ULONG InitiatorPortNumber,
        PTCHAR DestinationAddress,
        PTCHAR OuterModeAddress,
        BOOLEAN Persist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "InitiatorPortNumber", "DestinationAddress", "OuterModeAddress", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiTunnelModeOuterAddressA(jitter):
    iscsidsc_SetIScsiTunnelModeOuterAddress(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def iscsidsc_SetIScsiTunnelModeOuterAddressW(jitter):
    iscsidsc_SetIScsiTunnelModeOuterAddress(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def iscsidsc_SetupPersistentIScsiDevices(jitter):
    """
    ISDSC_STATUS SetupPersistentIScsiDevices()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
