
def powrprof_CallNtPowerInformation(jitter):
    """"
    [PowrProf.dll] NTSTATUS CallNtPowerInformation(POWER_INFORMATION_LEVEL InformationLevel, PVOID lpInputBuffer, ULONG nInputBufferSize, PVOID lpOutputBuffer, ULONG nOutputBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InformationLevel", "lpInputBuffer", "nInputBufferSize", "lpOutputBuffer", "nOutputBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DevicePowerClose(jitter):
    """"
    [PowrProf.dll] BOOLEAN DevicePowerClose()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DevicePowerEnumDevices(jitter):
    """"
    [PowrProf.dll] BOOLEAN DevicePowerEnumDevices(ULONG QueryIndex, ULONG QueryInterpretationFlags, ULONG QueryFlags, PBYTE pReturnBuffer, PULONG pBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueryIndex", "QueryInterpretationFlags", "QueryFlags", "pReturnBuffer", "pBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DevicePowerOpen(jitter):
    """"
    [PowrProf.dll] BOOLEAN DevicePowerOpen(ULONG Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DevicePowerSetDeviceState(jitter):
    """"
    [PowrProf.dll] DWORD DevicePowerSetDeviceState(LPCWSTR DeviceDescription, [DEVICEPOWER_FLAGS] SetFlags, PCVOID SetData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceDescription", "SetFlags", "SetData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_GetCurrentPowerPolicies(jitter):
    """"
    [PowrProf.dll] BOOLEAN GetCurrentPowerPolicies(PGLOBAL_POWER_POLICY pGlobalPowerPolicy, PPOWER_POLICY pPowerPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGlobalPowerPolicy", "pPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerCanRestoreIndividualDefaultPowerScheme(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerCanRestoreIndividualDefaultPowerScheme(const GUID* SchemeGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerCreatePossibleSetting(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerCreatePossibleSetting(HKEY RootSystemPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, ULONG PossibleSettingIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootSystemPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerCreateSetting(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerCreateSetting(HKEY RootSystemPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootSystemPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerDeleteScheme(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerDeleteScheme(HKEY RootPowerKey, const GUID* SchemeGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerDeterminePlatformRole(jitter):
    """"
    [PowrProf.dll] POWER_PLATFORM_ROLE PowerDeterminePlatformRole()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerDuplicateScheme(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerDuplicateScheme(HKEY RootPowerKey, const GUID* SourceSchemeGuid, GUID** DestinationSchemeGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SourceSchemeGuid", "DestinationSchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerEnumerate(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerEnumerate(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, POWER_DATA_ACCESSOR AccessFlags, ULONG Index, UCHAR* Buffer, DWORD* BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "AccessFlags", "Index", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerImportPowerScheme(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerImportPowerScheme(HKEY RootPowerKey, LPCWSTR ImportFileNamePath, GUID** DestinationSchemeGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "ImportFileNamePath", "DestinationSchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerIsSettingRangeDefined(jitter):
    """"
    [PowrProf.dll] BOOLEAN PowerIsSettingRangeDefined(const GUID* SubKeyGuid, const GUID* SettingGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubKeyGuid", "SettingGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadACDefaultIndex(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadACDefaultIndex(HKEY RootPowerKey, const GUID* SchemePersonalityGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPDWORD AcDefaultIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemePersonalityGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "AcDefaultIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadACValue(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadACValue(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, [RegType-PULONG] Type, LPBYTE Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Type", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadACValueIndex(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadACValueIndex(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPDWORD AcValueIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "AcValueIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadDCDefaultIndex(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadDCDefaultIndex(HKEY RootPowerKey, const GUID* SchemePersonalityGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPDWORD DcDefaultIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemePersonalityGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DcDefaultIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadDCValue(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadDCValue(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, [RegType-PULONG] Type, PUCHAR Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Type", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadDCValueIndex(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadDCValueIndex(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPDWORD DcValueIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DcValueIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadDescription(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadDescription(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPWSTR Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadFriendlyName(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadFriendlyName(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPWSTR Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadIconResourceSpecifier(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadIconResourceSpecifier(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, PUCHAR Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadPossibleDescription(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadPossibleDescription(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, ULONG PossibleSettingIndex, PUCHAR Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadPossibleFriendlyName(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadPossibleFriendlyName(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, ULONG PossibleSettingIndex, PUCHAR Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadPossibleValue(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadPossibleValue(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, [RegType-PULONG] Type, ULONG PossibleSettingIndex, PUCHAR Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Type", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadSettingAttributes(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadSettingAttributes(const GUID* SubGroupGuid, const GUID* PowerSettingGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubGroupGuid", "PowerSettingGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadValueIncrement(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadValueIncrement(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPDWORD ValueIncrement)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueIncrement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadValueMax(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadValueMax(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPDWORD ValueMaximum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueMaximum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadValueMin(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadValueMin(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPDWORD ValueMinimum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueMinimum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReadValueUnitsSpecifier(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReadValueUnitsSpecifier(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, LPWSTR Buffer, LPDWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerRemovePowerSetting(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerRemovePowerSetting(const GUID* PowerSettingSubKeyGuid, const GUID* PowerSettingGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PowerSettingSubKeyGuid", "PowerSettingGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerReplaceDefaultPowerSchemes(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerReplaceDefaultPowerSchemes()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerRestoreDefaultPowerSchemes(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerRestoreDefaultPowerSchemes()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerRestoreIndividualDefaultPowerScheme(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerRestoreIndividualDefaultPowerScheme(const GUID* SchemeGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSetActiveScheme(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerSetActiveScheme(HKEY UserRootPowerKey, const GUID* SchemeGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UserRootPowerKey", "SchemeGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSettingAccessCheck(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerSettingAccessCheck(POWER_DATA_ACCESSOR AccessFlags, const GUID* PowerGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AccessFlags", "PowerGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSettingAccessCheckEx(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerSettingAccessCheckEx(POWER_DATA_ACCESSOR AccessFlags, const GUID* PowerGuid, REGSAM AccessType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["AccessFlags", "PowerGuid", "AccessType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSettingRegisterNotification(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerSettingRegisterNotification(LPCGUID SettingGuid, DWORD Flags, HANDLE Recipient, PHPOWERNOTIFY RegistrationHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SettingGuid", "Flags", "Recipient", "RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerSettingUnregisterNotification(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerSettingUnregisterNotification(HPOWERNOTIFY RegistrationHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteACDefaultIndex(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteACDefaultIndex(HKEY RootSystemPowerKey, const GUID* SchemePersonalityGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, DWORD DefaultAcIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootSystemPowerKey", "SchemePersonalityGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DefaultAcIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteACValueIndex(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteACValueIndex(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, DWORD AcValueIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "AcValueIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteDCDefaultIndex(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteDCDefaultIndex(HKEY RootSystemPowerKey, const GUID* SchemePersonalityGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, DWORD DefaultDcIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootSystemPowerKey", "SchemePersonalityGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DefaultDcIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteDCValueIndex(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteDCValueIndex(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, DWORD DcValueIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "DcValueIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteDescription(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteDescription(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, UCHAR* Buffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteFriendlyName(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteFriendlyName(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, UCHAR* Buffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteIconResourceSpecifier(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteIconResourceSpecifier(HKEY RootPowerKey, const GUID* SchemeGuid, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, UCHAR* Buffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SchemeGuid", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWritePossibleDescription(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWritePossibleDescription(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, ULONG PossibleSettingIndex, UCHAR* Buffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWritePossibleFriendlyName(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWritePossibleFriendlyName(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, ULONG PossibleSettingIndex, UCHAR* Buffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWritePossibleValue(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWritePossibleValue(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, ULONG Type, ULONG PossibleSettingIndex, UCHAR* Buffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Type", "PossibleSettingIndex", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteSettingAttributes(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteSettingAttributes(const GUID* SubGroupGuid, const GUID* PowerSettingGuid, DWORD Attributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SubGroupGuid", "PowerSettingGuid", "Attributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteValueIncrement(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteValueIncrement(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, DWORD ValueIncrement)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueIncrement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteValueMax(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteValueMax(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, DWORD ValueMaximum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueMaximum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteValueMin(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteValueMin(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, DWORD ValueMinimum)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "ValueMinimum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerWriteValueUnitsSpecifier(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerWriteValueUnitsSpecifier(HKEY RootPowerKey, const GUID* SubGroupOfPowerSettingsGuid, const GUID* PowerSettingGuid, UCHAR* Buffer, DWORD BufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RootPowerKey", "SubGroupOfPowerSettingsGuid", "PowerSettingGuid", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_CanUserWritePwrScheme(jitter):
    """"
    [PowrProf.dll] BOOLEAN CanUserWritePwrScheme()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_DeletePwrScheme(jitter):
    """"
    [PowrProf.dll] BOOLEAN DeletePwrScheme(UINT uiIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uiIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_EnumPwrSchemes(jitter):
    """"
    [PowrProf.dll] BOOLEAN EnumPwrSchemes(PWRSCHEMESENUMPROC lpfnPwrSchemesEnumProc, LPARAM lParam)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpfnPwrSchemesEnumProc", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_GetActivePwrScheme(jitter):
    """"
    [PowrProf.dll] BOOLEAN GetActivePwrScheme(PUINT puiID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["puiID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerGetActiveScheme(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerGetActiveScheme(HKEY UserRootPowerKey, GUID** ActivePolicyGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["UserRootPowerKey", "ActivePolicyGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_GetPwrDiskSpindownRange(jitter):
    """"
    [PowrProf.dll] BOOLEAN GetPwrDiskSpindownRange(PUINT RangeMax, PUINT RangeMin)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RangeMax", "RangeMin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_IsPwrHibernateAllowed(jitter):
    """"
    [PowrProf.dll] BOOLEAN IsPwrHibernateAllowed()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_GetPwrCapabilities(jitter):
    """"
    [PowrProf.dll] BOOLEAN GetPwrCapabilities(PSYSTEM_POWER_CAPABILITIES lpSystemPowerCapabilities)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSystemPowerCapabilities"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_IsPwrShutdownAllowed(jitter):
    """"
    [PowrProf.dll] BOOLEAN IsPwrShutdownAllowed()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_IsPwrSuspendAllowed(jitter):
    """"
    [PowrProf.dll] BOOLEAN IsPwrSuspendAllowed()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_ReadGlobalPwrPolicy(jitter):
    """"
    [PowrProf.dll] BOOLEAN ReadGlobalPwrPolicy(PGLOBAL_POWER_POLICY pGlobalPowerPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGlobalPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_ReadProcessorPwrScheme(jitter):
    """"
    [PowrProf.dll] BOOLEAN ReadProcessorPwrScheme(UINT uiID, PMACHINE_PROCESSOR_POWER_POLICY pMachineProcessorPowerPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uiID", "pMachineProcessorPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_ReadPwrScheme(jitter):
    """"
    [PowrProf.dll] BOOLEAN ReadPwrScheme(UINT uiID, PPOWER_POLICY pPowerPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uiID", "pPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_SetActivePwrScheme(jitter):
    """"
    [PowrProf.dll] BOOLEAN SetActivePwrScheme(UINT uiID, PGLOBAL_POWER_POLICY lpGlobalPowerPolicy, PPOWER_POLICY lpPowerPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["uiID", "lpGlobalPowerPolicy", "lpPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_SetSuspendState(jitter):
    """"
    [PowrProf.dll] BOOLEAN SetSuspendState(BOOLEAN Hibernate, BOOLEAN ForceCritical, BOOLEAN DisableWakeEvent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Hibernate", "ForceCritical", "DisableWakeEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_WriteGlobalPwrPolicy(jitter):
    """"
    [PowrProf.dll] BOOLEAN WriteGlobalPwrPolicy(PGLOBAL_POWER_POLICY pGlobalPowerPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pGlobalPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_WriteProcessorPwrScheme(jitter):
    """"
    [PowrProf.dll] BOOLEAN WriteProcessorPwrScheme(UINT ID, PMACHINE_PROCESSOR_POWER_POLICY pMachineProcessorPowerPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ID", "pMachineProcessorPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_WritePwrScheme(jitter):
    """"
    [PowrProf.dll] BOOLEAN WritePwrScheme(PUINT puiID, LPWSTR lpszName, LPWSTR lpszDescription, PPOWER_POLICY pPowerPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["puiID", "lpszName", "lpszDescription", "pPowerPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerDeterminePlatformRoleEx(jitter):
    """"
    [PowrProf.dll] POWER_PLATFORM_ROLE PowerDeterminePlatformRoleEx([POWER_PLATFORM_ROLE_VERSION] Version)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Version"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerRegisterSuspendResumeNotification(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerRegisterSuspendResumeNotification([POWER_NOTIFICATION_FLAGS] Flags, HANDLE Recipient, PHPOWERNOTIFY RegistrationHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Recipient", "RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def powrprof_PowerUnregisterSuspendResumeNotification(jitter):
    """"
    [PowrProf.dll] [ERROR_CODE] PowerUnregisterSuspendResumeNotification(HPOWERNOTIFY RegistrationHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["RegistrationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
