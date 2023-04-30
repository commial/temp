
def iscsidsc_AddISNSServer(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS AddISNSServer(PTCHAR Address)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiConnection(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS AddIScsiConnection(PISCSI_UNIQUE_SESSION_ID UniqueSessionId, PVOID Reserved, ULONG InitiatorPortNumber, PISCSI_TARGET_PORTAL TargetPortal, ISCSI_SECURITY_FLAGS SecurityFlags, PISCSI_LOGIN_OPTIONS LoginOptions, ULONG KeySize, PCHAR Key, PISCSI_UNIQUE_CONNECTION_ID ConnectionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Reserved", "InitiatorPortNumber", "TargetPortal", "SecurityFlags", "LoginOptions", "KeySize", "Key", "ConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiSendTargetPortal(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS AddIScsiSendTargetPortal(PTCHAR InitiatorName, ULONG InitiatorPortNumber, PISCSI_LOGIN_OPTIONS LoginOptions, ISCSI_SECURITY_FLAGS SecurityFlags, PISCSI_TARGET_PORTAL Portal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "InitiatorPortNumber", "LoginOptions", "SecurityFlags", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddIScsiStaticTarget(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS AddIScsiStaticTarget(PTCHAR TargetName, PTCHAR TargetAlias, ISCSI_TARGET_FLAGS TargetFlags, BOOLEAN Persist, PISCSI_TARGET_MAPPING Mappings, PISCSI_LOGIN_OPTIONS LoginOptions, PISCSI_TARGET_PORTAL_GROUP PortalGroup)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "TargetAlias", "TargetFlags", "Persist", "Mappings", "LoginOptions", "PortalGroup"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddPersistentIScsiDevice(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS AddPersistentIScsiDevice(PTCHAR VolumePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["VolumePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_AddRadiusServer(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS AddRadiusServer(PWCHAR Address)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ClearPersistentIScsiDevices(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ClearPersistentIScsiDevices()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetDevicesForIScsiSession(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS GetDevicesForIScsiSession(PISCSI_UNIQUE_SESSION_ID UniqueSessionId, ULONG* DeviceCount, PISCSI_DEVICE_ON_SESSION Devices)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "DeviceCount", "Devices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiIKEInfo(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS GetIScsiIKEInfo(PTCHAR InitiatorName, ULONG PortNumber, PULONG Reserved, PIKE_AUTHENTICATION_INFORMATION AuthInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "PortNumber", "Reserved", "AuthInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiInitiatorNodeName(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS GetIScsiInitiatorNodeName(PTCHAR InitiatorNodeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorNodeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiSessionList(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS GetIScsiSessionList(ULONG* BufferSize, ULONG* SessionCount, PISCSI_SESSION_INFO SessionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "SessionCount", "SessionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiTargetInformation(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS GetIScsiTargetInformation(PTCHAR TargetName, PTCHAR DiscoveryMechanism, TARGET_INFORMATION_CLASS InfoClass, PULONG BufferSize, PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "DiscoveryMechanism", "InfoClass", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_GetIScsiVersionInformation(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS GetIScsiVersionInformation(PISCSI_VERSION_INFO VersionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["VersionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_LoginIScsiTarget(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS LoginIScsiTarget(PTCHAR TargetName, BOOLEAN IsInformationalSession, PTCHAR InitiatorName, ULONG InitiatorPortNumber, PISCSI_TARGET_PORTAL TargetPortal, ISCSI_SECURITY_FLAGS SecurityFlags, PISCSI_TARGET_MAPPING Mappings, PISCSI_LOGIN_OPTIONS LoginOptions, ULONG KeySize, PCHAR Key, BOOLEAN IsPersistent, PISCSI_UNIQUE_SESSION_ID UniqueSessionId, PISCSI_UNIQUE_CONNECTION_ID UniqueConnectionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetName", "IsInformationalSession", "InitiatorName", "InitiatorPortNumber", "TargetPortal", "SecurityFlags", "Mappings", "LoginOptions", "KeySize", "Key", "IsPersistent", "UniqueSessionId", "UniqueConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_LogoutIScsiTarget(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS LogoutIScsiTarget(PISCSI_UNIQUE_SESSION_ID UniqueSessionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RefreshISNSServer(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RefreshISNSServer(PTCHAR Address)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RefreshIScsiSendTargetPortal(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RefreshIScsiSendTargetPortal(PTCHAR InitiatorInstance, ULONG InitiatorPortNumber, PISCSI_TARGET_PORTAL Portal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveISNSServer(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RemoveISNSServer(PTCHAR Address)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiConnection(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RemoveIScsiConnection(PISCSI_UNIQUE_SESSION_ID UniqueSessionId, PISCSI_UNIQUE_CONNECTION_ID UniqueConnectionId)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "UniqueConnectionId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiPersistentTarget(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RemoveIScsiPersistentTarget(PTCHAR InitiatorInstance, ULONG InitiatorPortNumber, PTCHAR TargetName, PISCSI_TARGET_PORTAL Portal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "TargetName", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiSendTargetPortal(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RemoveIScsiSendTargetPortal(PTCHAR InitiatorInstance, ULONG InitiatorPortNumber, PISCSI_TARGET_PORTAL Portal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorInstance", "InitiatorPortNumber", "Portal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveIScsiStaticTarget(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RemoveIScsiStaticTarget(PTCHAR TargetName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["TargetName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemovePersistentIScsiDevice(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RemovePersistentIScsiDevice(PTCHAR VolumePath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["VolumePath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_RemoveRadiusServer(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS RemoveRadiusServer(PTCHAR Address)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportActiveIScsiTargetMappings(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportActiveIScsiTargetMappings(PULONG BufferSize, PULONG MappingCount, PISCSI_TARGET_MAPPING Mappings)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "MappingCount", "Mappings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportISNSServerList(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportISNSServerList(PULONG BufferSizeInChar, PTCHAR Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiInitiatorList(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportIScsiInitiatorList(ULONG* BufferSize, PTCHAR Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiPersistentLogins(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportIScsiPersistentLogins(ULONG* Count, PPERSISTENT_ISCSI_LOGIN_INFO PersistentLoginInfo, PULONG BufferSizeInBytes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Count", "PersistentLoginInfo", "BufferSizeInBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiSendTargetPortals(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportIScsiSendTargetPortals(PULONG PortalCount, PISCSI_TARGET_PORTAL_INFO PortalInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PortalCount", "PortalInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiSendTargetPortalsEx(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportIScsiSendTargetPortalsEx(PULONG PortalCount, PULONG PortalInfoSize, PISCSI_TARGET_PORTAL_INFO_EX PortalInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PortalCount", "PortalInfoSize", "PortalInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiTargets(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportIScsiTargets(BOOLEAN ForceUpdate, PULONG BufferSize, PTCHAR Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ForceUpdate", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportIScsiTargetPortals(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportIScsiTargetPortals(PWCHAR InitiatorName, PWCHAR TargetName, PUSHORT TargetPortalTag, PULONG ElementCount, PISCSI_TARGET_PORTAL Portals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "TargetName", "TargetPortalTag", "ElementCount", "Portals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportPersistentIScsiDevices(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportPersistentIScsiDevices(PULONG BufferSizeInChar, PTCHAR Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_ReportRadiusServerList(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS ReportRadiusServerList(PULONG BufferSizeInChar, PTCHAR Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["BufferSizeInChar", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SendScsiInquiry(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SendScsiInquiry(PISCSI_UNIQUE_SESSION_ID* UniqueSessionId, ULONGLONG Lun, UCHAR EvpdCmddt, UCHAR PageCode, PUCHAR* ScsiStatus, PULONG* ReponseSize, PUCHAR ReponseBuffer, PULONG* SenseSize, PUCHAR SenseBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Lun", "EvpdCmddt", "PageCode", "ScsiStatus", "ReponseSize", "ReponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SendScsiReadCapacity(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SendScsiReadCapacity(PISCSI_UNIQUE_SESSION_ID UniqueSessionId, ULONGLONG Lun, PUCHAR* ScsiStatus, PULONG* ResponseSize, PUCHAR ResponseBuffer, PULONG* SenseSize, PUCHAR SenseBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "Lun", "ScsiStatus", "ResponseSize", "ResponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SendScsiReportLuns(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SendScsiReportLuns(PISCSI_UNIQUE_SESSION_ID UniqueSessionId, PUCHAR* ScsiStatus, PULONG* ResponseSize, PUCHAR ResponseBuffer, PULONG* SenseSize, PUCHAR SenseBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UniqueSessionId", "ScsiStatus", "ResponseSize", "ResponseBuffer", "SenseSize", "SenseBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiGroupPresharedKey(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SetIScsiGroupPresharedKey(ULONG KeyLength, PUCHAR Key, BOOLEAN Persist)
    """"
    ret_ad, args = jitter.func_args_stdcall(["KeyLength", "Key", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiIKEInfo(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SetIScsiIKEInfo(PTCHAR InitiatorName, ULONG PortNumber, PIKE_AUTHENTICATION_INFORMATION AuthInfo, BOOLEAN Persist)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "PortNumber", "AuthInfo", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorCHAPSharedSecret(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SetIScsiInitiatorCHAPSharedSecret(ULONG SharedSecretLength, PUCHAR SharedSecret)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SharedSecretLength", "SharedSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorRADIUSSharedSecret(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SetIScsiInitiatorRADIUSSharedSecret(ULONG SharedSecretLength, PUCHAR SharedSecret)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SharedSecretLength", "SharedSecret"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiInitiatorNodeName(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SetIScsiInitiatorNodeName(PTCHAR InitiatorNodeName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorNodeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetIScsiTunnelModeOuterAddress(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SetIScsiTunnelModeOuterAddress(PTCHAR InitiatorName, ULONG InitiatorPortNumber, PTCHAR DestinationAddress, PTCHAR OuterModeAddress, BOOLEAN Persist)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InitiatorName", "InitiatorPortNumber", "DestinationAddress", "OuterModeAddress", "Persist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iscsidsc_SetupPersistentIScsiDevices(jitter):
    """"
    [Iscsidsc.dll] ISDSC_STATUS SetupPersistentIScsiDevices()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
