POWER_PLATFORM_ROLE = {
    "PlatformRoleUnspecified": 0,
    "PlatformRoleDesktop": 1,
    "PlatformRoleMobile": 2,
    "PlatformRoleWorkstation": 3,
    "PlatformRoleEnterpriseServer": 4,
    "PlatformRoleSOHOServer": 5,
    "PlatformRoleAppliancePC": 6,
    "PlatformRolePerformanceServer": 7,
    "PlatformRoleSlate": 8,
}
_POWER_PLATFORM_ROLE_VERSION_ = {
    "POWER_PLATFORM_ROLE_V1": 0x00000001,
    "POWER_PLATFORM_ROLE_V2": 0x00000002,
}

def powrprof_CallNtPowerInformation(jitter):
    """
    NTSTATUS CallNtPowerInformation(
        POWER_INFORMATION_LEVEL InformationLevel,
        PVOID lpInputBuffer,
        ULONG nInputBufferSize,
        PVOID lpOutputBuffer,
        ULONG nOutputBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InformationLevel", "lpInputBuffer", "nInputBufferSize", "lpOutputBuffer", "nOutputBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DevicePowerClose(jitter):
    """
    BOOLEAN DevicePowerClose()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DevicePowerEnumDevices(jitter):
    """
    BOOLEAN DevicePowerEnumDevices(
        ULONG QueryIndex,
        ULONG QueryInterpretationFlags,
        ULONG QueryFlags,
        PBYTE pReturnBuffer,
        PULONG pBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueryIndex", "QueryInterpretationFlags", "QueryFlags", "pReturnBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DevicePowerOpen(jitter):
    """
    BOOLEAN DevicePowerOpen(
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DevicePowerSetDeviceState(jitter):
    """
    DWORD DevicePowerSetDeviceState(
        LPCWSTR DeviceDescription,
        [DEVICEPOWER_FLAGS] SetFlags,
        PCVOID SetData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceDescription", "SetFlags", "SetData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_GetCurrentPowerPolicies(jitter):
    """
    BOOLEAN GetCurrentPowerPolicies(
        PGLOBAL_POWER_POLICY pGlobalPowerPolicy,
        PPOWER_POLICY pPowerPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGlobalPowerPolicy", "pPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerCanRestoreIndividualDefaultPowerScheme(jitter):
    """
    [ERROR_CODE] PowerCanRestoreIndividualDefaultPowerScheme(
        const GUID* SchemeGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerCreatePossibleSetting(jitter):
    """
    [ERROR_CODE] PowerCreatePossibleSetting(
        HKEY RootSystemPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        ULONG PossibleSettingIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootSystemPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerCreateSetting(jitter):
    """
    [ERROR_CODE] PowerCreateSetting(
        HKEY RootSystemPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootSystemPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerDeleteScheme(jitter):
    """
    [ERROR_CODE] PowerDeleteScheme(
        HKEY RootPowerKey,
        const GUID* SchemeGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerDeterminePlatformRole(jitter):
    """
    POWER_PLATFORM_ROLE PowerDeterminePlatformRole()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerDuplicateScheme(jitter):
    """
    [ERROR_CODE] PowerDuplicateScheme(
        HKEY RootPowerKey,
        const GUID* SourceSchemeGuid,
        GUID** DestinationSchemeGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SourceSchemeGuid", "DestinationSchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerEnumerate(jitter):
    """
    [ERROR_CODE] PowerEnumerate(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        POWER_DATA_ACCESSOR AccessFlags,
        ULONG Index,
        UCHAR* Buffer,
        DWORD* BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "AccessFlags", "Index", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerImportPowerScheme(jitter):
    """
    [ERROR_CODE] PowerImportPowerScheme(
        HKEY RootPowerKey,
        LPCWSTR ImportFileNamePath,
        GUID** DestinationSchemeGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "ImportFileNamePath", "DestinationSchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerIsSettingRangeDefined(jitter):
    """
    BOOLEAN PowerIsSettingRangeDefined(
        const GUID* SubKeyGuid,
        const GUID* SettingGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubKeyGuid", "SettingGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadACDefaultIndex(jitter):
    """
    [ERROR_CODE] PowerReadACDefaultIndex(
        HKEY RootPowerKey,
        const GUID* SchemePersonalityGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPDWORD AcDefaultIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemePersonalityGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "AcDefaultIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadACValue(jitter):
    """
    [ERROR_CODE] PowerReadACValue(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        [RegType-PULONG] Type,
        LPBYTE Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Type", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadACValueIndex(jitter):
    """
    [ERROR_CODE] PowerReadACValueIndex(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPDWORD AcValueIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "AcValueIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadDCDefaultIndex(jitter):
    """
    [ERROR_CODE] PowerReadDCDefaultIndex(
        HKEY RootPowerKey,
        const GUID* SchemePersonalityGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPDWORD DcDefaultIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemePersonalityGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DcDefaultIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadDCValue(jitter):
    """
    [ERROR_CODE] PowerReadDCValue(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        [RegType-PULONG] Type,
        PUCHAR Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Type", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadDCValueIndex(jitter):
    """
    [ERROR_CODE] PowerReadDCValueIndex(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPDWORD DcValueIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DcValueIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadDescription(jitter):
    """
    [ERROR_CODE] PowerReadDescription(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPWSTR Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadFriendlyName(jitter):
    """
    [ERROR_CODE] PowerReadFriendlyName(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPWSTR Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadIconResourceSpecifier(jitter):
    """
    [ERROR_CODE] PowerReadIconResourceSpecifier(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        PUCHAR Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadPossibleDescription(jitter):
    """
    [ERROR_CODE] PowerReadPossibleDescription(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        ULONG PossibleSettingIndex,
        PUCHAR Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadPossibleFriendlyName(jitter):
    """
    [ERROR_CODE] PowerReadPossibleFriendlyName(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        ULONG PossibleSettingIndex,
        PUCHAR Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadPossibleValue(jitter):
    """
    [ERROR_CODE] PowerReadPossibleValue(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        [RegType-PULONG] Type,
        ULONG PossibleSettingIndex,
        PUCHAR Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Type", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadSettingAttributes(jitter):
    """
    [ERROR_CODE] PowerReadSettingAttributes(
        const GUID* SubGroupGuid,
        const GUID* PowerSettingGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubGroupGuid", "PowerSettingGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadValueIncrement(jitter):
    """
    [ERROR_CODE] PowerReadValueIncrement(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPDWORD ValueIncrement
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueIncrement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadValueMax(jitter):
    """
    [ERROR_CODE] PowerReadValueMax(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPDWORD ValueMaximum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueMaximum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadValueMin(jitter):
    """
    [ERROR_CODE] PowerReadValueMin(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPDWORD ValueMinimum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueMinimum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadValueUnitsSpecifier(jitter):
    """
    [ERROR_CODE] PowerReadValueUnitsSpecifier(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        LPWSTR Buffer,
        LPDWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerRemovePowerSetting(jitter):
    """
    [ERROR_CODE] PowerRemovePowerSetting(
        const GUID* PowerSettingSubKeyGuid,
        const GUID* PowerSettingGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PowerSettingSubKeyGuid", "PowerSettingGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReplaceDefaultPowerSchemes(jitter):
    """
    [ERROR_CODE] PowerReplaceDefaultPowerSchemes()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerRestoreDefaultPowerSchemes(jitter):
    """
    [ERROR_CODE] PowerRestoreDefaultPowerSchemes()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerRestoreIndividualDefaultPowerScheme(jitter):
    """
    [ERROR_CODE] PowerRestoreIndividualDefaultPowerScheme(
        const GUID* SchemeGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSetActiveScheme(jitter):
    """
    [ERROR_CODE] PowerSetActiveScheme(
        HKEY UserRootPowerKey,
        const GUID* SchemeGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UserRootPowerKey", "SchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSettingAccessCheck(jitter):
    """
    [ERROR_CODE] PowerSettingAccessCheck(
        POWER_DATA_ACCESSOR AccessFlags,
        const GUID* PowerGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AccessFlags", "PowerGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSettingAccessCheckEx(jitter):
    """
    [ERROR_CODE] PowerSettingAccessCheckEx(
        POWER_DATA_ACCESSOR AccessFlags,
        const GUID* PowerGuid,
        REGSAM AccessType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AccessFlags", "PowerGuid", "AccessType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSettingRegisterNotification(jitter):
    """
    [ERROR_CODE] PowerSettingRegisterNotification(
        LPCGUID SettingGuid,
        DWORD Flags,
        HANDLE Recipient,
        PHPOWERNOTIFY RegistrationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SettingGuid", "Flags", "Recipient", "RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSettingUnregisterNotification(jitter):
    """
    [ERROR_CODE] PowerSettingUnregisterNotification(
        HPOWERNOTIFY RegistrationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteACDefaultIndex(jitter):
    """
    [ERROR_CODE] PowerWriteACDefaultIndex(
        HKEY RootSystemPowerKey,
        const GUID* SchemePersonalityGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        DWORD DefaultAcIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootSystemPowerKey", "SchemePersonalityGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DefaultAcIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteACValueIndex(jitter):
    """
    [ERROR_CODE] PowerWriteACValueIndex(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        DWORD AcValueIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "AcValueIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteDCDefaultIndex(jitter):
    """
    [ERROR_CODE] PowerWriteDCDefaultIndex(
        HKEY RootSystemPowerKey,
        const GUID* SchemePersonalityGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        DWORD DefaultDcIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootSystemPowerKey", "SchemePersonalityGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DefaultDcIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteDCValueIndex(jitter):
    """
    [ERROR_CODE] PowerWriteDCValueIndex(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        DWORD DcValueIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DcValueIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteDescription(jitter):
    """
    [ERROR_CODE] PowerWriteDescription(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        UCHAR* Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteFriendlyName(jitter):
    """
    [ERROR_CODE] PowerWriteFriendlyName(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        UCHAR* Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteIconResourceSpecifier(jitter):
    """
    [ERROR_CODE] PowerWriteIconResourceSpecifier(
        HKEY RootPowerKey,
        const GUID* SchemeGuid,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        UCHAR* Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWritePossibleDescription(jitter):
    """
    [ERROR_CODE] PowerWritePossibleDescription(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        ULONG PossibleSettingIndex,
        UCHAR* Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWritePossibleFriendlyName(jitter):
    """
    [ERROR_CODE] PowerWritePossibleFriendlyName(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        ULONG PossibleSettingIndex,
        UCHAR* Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWritePossibleValue(jitter):
    """
    [ERROR_CODE] PowerWritePossibleValue(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        ULONG Type,
        ULONG PossibleSettingIndex,
        UCHAR* Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Type", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteSettingAttributes(jitter):
    """
    [ERROR_CODE] PowerWriteSettingAttributes(
        const GUID* SubGroupGuid,
        const GUID* PowerSettingGuid,
        DWORD Attributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubGroupGuid", "PowerSettingGuid", "Attributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteValueIncrement(jitter):
    """
    [ERROR_CODE] PowerWriteValueIncrement(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        DWORD ValueIncrement
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueIncrement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteValueMax(jitter):
    """
    [ERROR_CODE] PowerWriteValueMax(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        DWORD ValueMaximum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueMaximum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteValueMin(jitter):
    """
    [ERROR_CODE] PowerWriteValueMin(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        DWORD ValueMinimum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueMinimum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteValueUnitsSpecifier(jitter):
    """
    [ERROR_CODE] PowerWriteValueUnitsSpecifier(
        HKEY RootPowerKey,
        const GUID* SubGroupOfPowerSettingsGuid,
        const GUID* PowerSettingGuid,
        UCHAR* Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_CanUserWritePwrScheme(jitter):
    """
    BOOLEAN CanUserWritePwrScheme()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DeletePwrScheme(jitter):
    """
    BOOLEAN DeletePwrScheme(
        UINT uiIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_EnumPwrSchemes(jitter):
    """
    BOOLEAN EnumPwrSchemes(
        PWRSCHEMESENUMPROC lpfnPwrSchemesEnumProc,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpfnPwrSchemesEnumProc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_GetActivePwrScheme(jitter):
    """
    BOOLEAN GetActivePwrScheme(
        PUINT puiID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["puiID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerGetActiveScheme(jitter):
    """
    [ERROR_CODE] PowerGetActiveScheme(
        HKEY UserRootPowerKey,
        GUID** ActivePolicyGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UserRootPowerKey", "ActivePolicyGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_GetPwrDiskSpindownRange(jitter):
    """
    BOOLEAN GetPwrDiskSpindownRange(
        PUINT RangeMax,
        PUINT RangeMin
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RangeMax", "RangeMin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_IsPwrHibernateAllowed(jitter):
    """
    BOOLEAN IsPwrHibernateAllowed()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_GetPwrCapabilities(jitter):
    """
    BOOLEAN GetPwrCapabilities(
        PSYSTEM_POWER_CAPABILITIES lpSystemPowerCapabilities
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSystemPowerCapabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_IsPwrShutdownAllowed(jitter):
    """
    BOOLEAN IsPwrShutdownAllowed()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_IsPwrSuspendAllowed(jitter):
    """
    BOOLEAN IsPwrSuspendAllowed()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_ReadGlobalPwrPolicy(jitter):
    """
    BOOLEAN ReadGlobalPwrPolicy(
        PGLOBAL_POWER_POLICY pGlobalPowerPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGlobalPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_ReadProcessorPwrScheme(jitter):
    """
    BOOLEAN ReadProcessorPwrScheme(
        UINT uiID,
        PMACHINE_PROCESSOR_POWER_POLICY pMachineProcessorPowerPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiID", "pMachineProcessorPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_ReadPwrScheme(jitter):
    """
    BOOLEAN ReadPwrScheme(
        UINT uiID,
        PPOWER_POLICY pPowerPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiID", "pPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_SetActivePwrScheme(jitter):
    """
    BOOLEAN SetActivePwrScheme(
        UINT uiID,
        PGLOBAL_POWER_POLICY lpGlobalPowerPolicy,
        PPOWER_POLICY lpPowerPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiID", "lpGlobalPowerPolicy", "lpPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_SetSuspendState(jitter):
    """
    BOOLEAN SetSuspendState(
        BOOLEAN Hibernate,
        BOOLEAN ForceCritical,
        BOOLEAN DisableWakeEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Hibernate", "ForceCritical", "DisableWakeEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_WriteGlobalPwrPolicy(jitter):
    """
    BOOLEAN WriteGlobalPwrPolicy(
        PGLOBAL_POWER_POLICY pGlobalPowerPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pGlobalPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_WriteProcessorPwrScheme(jitter):
    """
    BOOLEAN WriteProcessorPwrScheme(
        UINT ID,
        PMACHINE_PROCESSOR_POWER_POLICY pMachineProcessorPowerPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ID", "pMachineProcessorPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_WritePwrScheme(jitter):
    """
    BOOLEAN WritePwrScheme(
        PUINT puiID,
        LPWSTR lpszName,
        LPWSTR lpszDescription,
        PPOWER_POLICY pPowerPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["puiID", "lpszName", "lpszDescription", "pPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerDeterminePlatformRoleEx(jitter):
    """
    POWER_PLATFORM_ROLE PowerDeterminePlatformRoleEx(
        [POWER_PLATFORM_ROLE_VERSION] Version
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Version"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerRegisterSuspendResumeNotification(jitter):
    """
    [ERROR_CODE] PowerRegisterSuspendResumeNotification(
        [POWER_NOTIFICATION_FLAGS] Flags,
        HANDLE Recipient,
        PHPOWERNOTIFY RegistrationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Recipient", "RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerUnregisterSuspendResumeNotification(jitter):
    """
    [ERROR_CODE] PowerUnregisterSuspendResumeNotification(
        HPOWERNOTIFY RegistrationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
