DI_FUNCTION = {
    "DIF_SELECTDEVICE": 0x00000001,
    "DIF_INSTALLDEVICE": 0x00000002,
    "DIF_ASSIGNRESOURCES": 0x00000003,
    "DIF_PROPERTIES": 0x00000004,
    "DIF_REMOVE": 0x00000005,
    "DIF_FIRSTTIMESETUP": 0x00000006,
    "DIF_FOUNDDEVICE": 0x00000007,
    "DIF_SELECTCLASSDRIVERS": 0x00000008,
    "DIF_VALIDATECLASSDRIVERS": 0x00000009,
    "DIF_INSTALLCLASSDRIVERS": 0x0000000A,
    "DIF_CALCDISKSPACE": 0x0000000B,
    "DIF_DESTROYPRIVATEDATA": 0x0000000C,
    "DIF_VALIDATEDRIVER": 0x0000000D,
    "DIF_DETECT": 0x0000000F,
    "DIF_INSTALLWIZARD": 0x00000010,
    "DIF_DESTROYWIZARDDATA": 0x00000011,
    "DIF_PROPERTYCHANGE": 0x00000012,
    "DIF_ENABLECLASS": 0x00000013,
    "DIF_DETECTVERIFY": 0x00000014,
    "DIF_INSTALLDEVICEFILES": 0x00000015,
    "DIF_UNREMOVE": 0x00000016,
    "DIF_SELECTBESTCOMPATDRV": 0x00000017,
    "DIF_ALLOW_INSTALL": 0x00000018,
    "DIF_REGISTERDEVICE": 0x00000019,
    "DIF_NEWDEVICEWIZARD_PRESELECT": 0x0000001A,
    "DIF_NEWDEVICEWIZARD_SELECT": 0x0000001B,
    "DIF_NEWDEVICEWIZARD_PREANALYZE": 0x0000001C,
    "DIF_NEWDEVICEWIZARD_POSTANALYZE": 0x0000001D,
    "DIF_NEWDEVICEWIZARD_FINISHINSTALL": 0x0000001E,
    "DIF_UNUSED1": 0x0000001F,
    "DIF_INSTALLINTERFACES": 0x00000020,
    "DIF_DETECTCANCEL": 0x00000021,
    "DIF_REGISTER_COINSTALLERS": 0x00000022,
    "DIF_ADDPROPERTYPAGE_ADVANCED": 0x00000023,
    "DIF_ADDPROPERTYPAGE_BASIC": 0x00000024,
    "DIF_RESERVED1": 0x00000025,
    "DIF_TROUBLESHOOTER": 0x00000026,
    "DIF_POWERMESSAGEWAKE": 0x00000027,
    "DIF_ADDREMOTEPROPERTYPAGE_ADVANCED": 0x00000028,
    "DIF_UPDATEDRIVER_UI": 0x00000029,
    "DIF_FINISHINSTALL_ACTION": 0x0000002A,
    "DIF_RESERVED2": 0x00000030,
    "DIF_MOVEDEVICE": 0x0000000E,
}
_DiGetClassDevPropertySheetsType_ = {
    "DIGCDP_FLAG_BASIC": 0x00000001,
    "DIGCDP_FLAG_ADVANCED": 0x00000002,
    "DIGCDP_FLAG_REMOTE_BASIC": 0x00000003,
    "DIGCDP_FLAG_REMOTE_ADVANCED": 0x00000004,
}
_SetupDeviceRegistryProperty_ = {
    "SPDRP_DEVICEDESC": 0x00000000,
    "SPDRP_HARDWAREID": 0x00000001,
    "SPDRP_COMPATIBLEIDS": 0x00000002,
    "SPDRP_UNUSED0": 0x00000003,
    "SPDRP_SERVICE": 0x00000004,
    "SPDRP_UNUSED1": 0x00000005,
    "SPDRP_UNUSED2": 0x00000006,
    "SPDRP_CLASS": 0x00000007,
    "SPDRP_CLASSGUID": 0x00000008,
    "SPDRP_DRIVER": 0x00000009,
    "SPDRP_CONFIGFLAGS": 0x0000000A,
    "SPDRP_MFG": 0x0000000B,
    "SPDRP_FRIENDLYNAME": 0x0000000C,
    "SPDRP_LOCATION_INFORMATION": 0x0000000D,
    "SPDRP_PHYSICAL_DEVICE_OBJECT_NAME": 0x0000000E,
    "SPDRP_CAPABILITIES": 0x0000000F,
    "SPDRP_UI_NUMBER": 0x00000010,
    "SPDRP_UPPERFILTERS": 0x00000011,
    "SPDRP_LOWERFILTERS": 0x00000012,
    "SPDRP_BUSTYPEGUID": 0x00000013,
    "SPDRP_LEGACYBUSTYPE": 0x00000014,
    "SPDRP_BUSNUMBER": 0x00000015,
    "SPDRP_ENUMERATOR_NAME": 0x00000016,
    "SPDRP_SECURITY": 0x00000017,
    "SPDRP_SECURITY_SDS": 0x00000018,
    "SPDRP_DEVTYPE": 0x00000019,
    "SPDRP_EXCLUSIVE": 0x0000001A,
    "SPDRP_CHARACTERISTICS": 0x0000001B,
    "SPDRP_ADDRESS": 0x0000001C,
    "SPDRP_UI_NUMBER_DESC_FORMAT": 0X0000001D,
    "SPDRP_DEVICE_POWER_DATA": 0x0000001E,
    "SPDRP_REMOVAL_POLICY": 0x0000001F,
    "SPDRP_REMOVAL_POLICY_HW_DEFAULT": 0x00000020,
    "SPDRP_REMOVAL_POLICY_OVERRIDE": 0x00000021,
    "SPDRP_INSTALL_STATE": 0x00000022,
    "SPDRP_LOCATION_PATHS": 0x00000023,
}
LogSeverity = {
    "LogSevInformation": 0x00000000,
    "LogSevWarning": 0x00000001,
    "LogSevError": 0x00000002,
    "LogSevFatalError": 0x00000003,
    "LogSevMaximum": 0x00000004,
}
SetupFileLogInfo = {
    "SetupFileLogSourceFilename": 0,
    "SetupFileLogChecksum": 1,
    "SetupFileLogDiskTagfile": 2,
    "SetupFileLogDiskDescription": 3,
    "SetupFileLogOtherInfo": 4,
}

def setupapi_InstallHinfSection(jitter, get_str, set_str):
    """
    VOID InstallHinfSection(
        HWND hwnd,
        HINSTANCE ModuleHandle,
        PCTSTR CmdLineBuffer,
        INT nCmdShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "ModuleHandle", "CmdLineBuffer", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_InstallHinfSectionA(jitter):
    setupapi_InstallHinfSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_InstallHinfSectionW(jitter):
    setupapi_InstallHinfSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupAddInstallSectionToDiskSpaceList(jitter, get_str, set_str):
    """
    BOOL SetupAddInstallSectionToDiskSpaceList(
        HDSKSPC DiskSpace,
        HINF InfHandle,
        HINF LayoutInfHandle,
        PCTSTR SectionName,
        PVOID Reserved1,
        UINT Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "InfHandle", "LayoutInfHandle", "SectionName", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAddInstallSectionToDiskSpaceListA(jitter):
    setupapi_SetupAddInstallSectionToDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupAddInstallSectionToDiskSpaceListW(jitter):
    setupapi_SetupAddInstallSectionToDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupAddSectionToDiskSpaceList(jitter, get_str, set_str):
    """
    BOOL SetupAddSectionToDiskSpaceList(
        HDSKSPC DiskSpace,
        HINF InfHandle,
        HINF ListInfHandle,
        PCTSTR SectionName,
        UINT Operation,
        PVOID Reserved1,
        UINT Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "InfHandle", "ListInfHandle", "SectionName", "Operation", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAddSectionToDiskSpaceListA(jitter):
    setupapi_SetupAddSectionToDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupAddSectionToDiskSpaceListW(jitter):
    setupapi_SetupAddSectionToDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupAddToDiskSpaceList(jitter, get_str, set_str):
    """
    BOOL SetupAddToDiskSpaceList(
        HDSKSPC DiskSpace,
        PCTSTR TargetFilespec,
        LONGLONG FileSize,
        UINT Operation,
        PVOID Reserved1,
        UINT Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "TargetFilespec", "FileSize", "Operation", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAddToDiskSpaceListA(jitter):
    setupapi_SetupAddToDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupAddToDiskSpaceListW(jitter):
    setupapi_SetupAddToDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupAddToSourceList(jitter, get_str, set_str):
    """
    BOOL SetupAddToSourceList(
        DWORD Flags,
        PCTSTR Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAddToSourceListA(jitter):
    setupapi_SetupAddToSourceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupAddToSourceListW(jitter):
    setupapi_SetupAddToSourceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupAdjustDiskSpaceList(jitter, get_str, set_str):
    """
    BOOL SetupAdjustDiskSpaceList(
        HDSKSPC DiskSpace,
        LPCTSTR DriveRoot,
        LONGLONG Amount,
        PVOID Reserved1,
        UINT Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "DriveRoot", "Amount", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAdjustDiskSpaceListA(jitter):
    setupapi_SetupAdjustDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupAdjustDiskSpaceListW(jitter):
    setupapi_SetupAdjustDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupBackupError(jitter, get_str, set_str):
    """
    UINT SetupBackupError(
        HWND hwndParent,
        PCTSTR DialogTitle,
        PCTSTR SourceFile,
        PCTSTR TargetFile,
        UINT Win32ErrorCode,
        DWORD Style
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "SourceFile", "TargetFile", "Win32ErrorCode", "Style"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupBackupErrorA(jitter):
    setupapi_SetupBackupError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupBackupErrorW(jitter):
    setupapi_SetupBackupError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupCancelTemporarySourceList(jitter):
    """
    BOOL SetupCancelTemporarySourceList()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCloseFileQueue(jitter):
    """
    BOOL SetupCloseFileQueue(
        HSPFILEQ QueueHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCloseInfFile(jitter):
    """
    VOID SetupCloseInfFile(
        HINF InfHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCommitFileQueue(jitter, get_str, set_str):
    """
    BOOL SetupCommitFileQueue(
        HWND Owner,
        HSPFILEQ QueueHandle,
        PSP_FILE_CALLBACK MsgHandler,
        PVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Owner", "QueueHandle", "MsgHandler", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCommitFileQueueA(jitter):
    setupapi_SetupCommitFileQueue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupCommitFileQueueW(jitter):
    setupapi_SetupCommitFileQueue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupConfigureWmiFromInfSection(jitter, get_str, set_str):
    """
    BOOL SetupConfigureWmiFromInfSection(
        HINF InfHandle,
        PCWSTR SectionName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "SectionName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupConfigureWmiFromInfSectionA(jitter):
    setupapi_SetupConfigureWmiFromInfSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupConfigureWmiFromInfSectionW(jitter):
    setupapi_SetupConfigureWmiFromInfSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupCopyError(jitter, get_str, set_str):
    """
    UINT SetupCopyError(
        HWND hwndParent,
        PCTSTR DialogTitle,
        PCTSTR DiskName,
        PCTSTR PathToSource,
        PCTSTR SourceFile,
        PCTSTR TargetPathFile,
        UINT Win32ErrorCode,
        DWORD Style,
        PTSTR PathBuffer,
        DWORD PathBufferSize,
        PDWORD PathRequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "DiskName", "PathToSource", "SourceFile", "TargetPathFile", "Win32ErrorCode", "Style", "PathBuffer", "PathBufferSize", "PathRequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCopyErrorA(jitter):
    setupapi_SetupCopyError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupCopyErrorW(jitter):
    setupapi_SetupCopyError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupCopyOEMInf(jitter, get_str, set_str):
    """
    BOOL SetupCopyOEMInf(
        PCTSTR SourceInfFileName,
        PCTSTR OEMSourceMediaLocation,
        DWORD OEMSourceMediaType,
        DWORD CopyStyle,
        PTSTR DestinationInfFileName,
        DWORD DestinationInfFileNameSize,
        PDWORD RequiredSize,
        PTSTR DestinationInfFileNameComponent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceInfFileName", "OEMSourceMediaLocation", "OEMSourceMediaType", "CopyStyle", "DestinationInfFileName", "DestinationInfFileNameSize", "RequiredSize", "DestinationInfFileNameComponent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCopyOEMInfA(jitter):
    setupapi_SetupCopyOEMInf(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupCopyOEMInfW(jitter):
    setupapi_SetupCopyOEMInf(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupCreateDiskSpaceList(jitter, get_str, set_str):
    """
    HDSKSPC SetupCreateDiskSpaceList(
        PVOID Reserved1,
        DWORD Reserved2,
        [SPDSL_FLAGS] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Reserved1", "Reserved2", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCreateDiskSpaceListA(jitter):
    setupapi_SetupCreateDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupCreateDiskSpaceListW(jitter):
    setupapi_SetupCreateDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDecompressOrCopyFile(jitter, get_str, set_str):
    """
    [ERROR_CODE] SetupDecompressOrCopyFile(
        PCTSTR SourceFileName,
        PCTSTR TargetFileName,
        PUINT CompressionType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceFileName", "TargetFileName", "CompressionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDecompressOrCopyFileA(jitter):
    setupapi_SetupDecompressOrCopyFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDecompressOrCopyFileW(jitter):
    setupapi_SetupDecompressOrCopyFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDefaultQueueCallback(jitter, get_str, set_str):
    """
    UINT SetupDefaultQueueCallback(
        PVOID Context,
        UINT Notification,
        UINT Param1,
        UINT Param2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "Notification", "Param1", "Param2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDefaultQueueCallbackA(jitter):
    setupapi_SetupDefaultQueueCallback(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDefaultQueueCallbackW(jitter):
    setupapi_SetupDefaultQueueCallback(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDeleteError(jitter, get_str, set_str):
    """
    UINT SetupDeleteError(
        HWND hwndParent,
        PCTSTR DialogTitle,
        PCTSTR File,
        UINT Win32ErrorCode,
        DWORD Style
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "File", "Win32ErrorCode", "Style"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDeleteErrorA(jitter):
    setupapi_SetupDeleteError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDeleteErrorW(jitter):
    setupapi_SetupDeleteError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDestroyDiskSpaceList(jitter):
    """
    BOOL SetupDestroyDiskSpaceList(
        HDSKSPC DiskSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDuplicateDiskSpaceList(jitter, get_str, set_str):
    """
    HDSKSPC SetupDuplicateDiskSpaceList(
        HDSKSPC DiskSpace,
        PVOID Reserved1,
        DWORD Reserved2,
        UINT Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "Reserved1", "Reserved2", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDuplicateDiskSpaceListA(jitter):
    setupapi_SetupDuplicateDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDuplicateDiskSpaceListW(jitter):
    setupapi_SetupDuplicateDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupEnumInfSections(jitter, get_str, set_str):
    """
    BOOL SetupEnumInfSections(
        HINF InfHandle,
        UINT EnumerationIndex,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "EnumerationIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupEnumInfSectionsA(jitter):
    setupapi_SetupEnumInfSections(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupEnumInfSectionsW(jitter):
    setupapi_SetupEnumInfSections(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupFindFirstLine(jitter, get_str, set_str):
    """
    BOOL SetupFindFirstLine(
        HINF InfHandle,
        PCTSTR Section,
        PCTSTR Key,
        PINFCONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Section", "Key", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupFindFirstLineA(jitter):
    setupapi_SetupFindFirstLine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupFindFirstLineW(jitter):
    setupapi_SetupFindFirstLine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupFindNextLine(jitter):
    """
    BOOL SetupFindNextLine(
        PINFCONTEXT ContextIn,
        PINFCONTEXT ContextOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextIn", "ContextOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupFindNextMatchLine(jitter, get_str, set_str):
    """
    BOOL SetupFindNextMatchLine(
        PINFCONTEXT ContextIn,
        PCTSTR Key,
        PINFCONTEXT ContextOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextIn", "Key", "ContextOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupFindNextMatchLineA(jitter):
    setupapi_SetupFindNextMatchLine(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupFindNextMatchLineW(jitter):
    setupapi_SetupFindNextMatchLine(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupFreeSourceList(jitter, get_str, set_str):
    """
    BOOL SetupFreeSourceList(
        PCTSTR** List,
        UINT Count
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["List", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupFreeSourceListA(jitter):
    setupapi_SetupFreeSourceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupFreeSourceListW(jitter):
    setupapi_SetupFreeSourceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetBinaryField(jitter):
    """
    BOOL SetupGetBinaryField(
        PINFCONTEXT Context,
        DWORD FieldIndex,
        BYTE* ReturnBuffer,
        DWORD ReturnBufferSize,
        LPDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "FieldIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFieldCount(jitter):
    """
    DWORD SetupGetFieldCount(
        PINFCONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFileCompressionInfo(jitter, get_str, set_str):
    """
    [ERROR_CODE] SetupGetFileCompressionInfo(
        PCTSTR SourceFileName,
        PTSTR* ActualSourceFileName,
        PDWORD SourceFileSize,
        PDWORD TargetFileSize,
        PUINT CompressionType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceFileName", "ActualSourceFileName", "SourceFileSize", "TargetFileSize", "CompressionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFileCompressionInfoA(jitter):
    setupapi_SetupGetFileCompressionInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetFileCompressionInfoW(jitter):
    setupapi_SetupGetFileCompressionInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetFileCompressionInfoEx(jitter, get_str, set_str):
    """
    BOOL SetupGetFileCompressionInfoEx(
        PCTSTR SourceFileName,
        PTSTR ActualSourceFileNameBuffer,
        DWORD ActualSourceFileNameLen,
        PDWORD RequiredBufferLen,
        PDWORD SourceFileSize,
        PDWORD TargetFileSize,
        PUINT CompressionType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceFileName", "ActualSourceFileNameBuffer", "ActualSourceFileNameLen", "RequiredBufferLen", "SourceFileSize", "TargetFileSize", "CompressionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFileCompressionInfoExA(jitter):
    setupapi_SetupGetFileCompressionInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetFileCompressionInfoExW(jitter):
    setupapi_SetupGetFileCompressionInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetFileQueueCount(jitter):
    """
    BOOL SetupGetFileQueueCount(
        HSPFILEQ FileQueue,
        UINT SubQueueFileOp,
        PUINT NumOperations
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "SubQueueFileOp", "NumOperations"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFileQueueFlags(jitter):
    """
    BOOL SetupGetFileQueueFlags(
        HSPFILEQ FileQueue,
        PDWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfFileList(jitter, get_str, set_str):
    """
    BOOL SetupGetInfFileList(
        PCTSTR DirectoryPath,
        [InfStyle] InfStyle,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DirectoryPath", "InfStyle", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfFileListA(jitter):
    setupapi_SetupGetInfFileList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetInfFileListW(jitter):
    setupapi_SetupGetInfFileList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetInfInformation(jitter, get_str, set_str):
    """
    BOOL SetupGetInfInformation(
        LPCVOID InfSpec,
        DWORD SearchControl,
        PSP_INF_INFORMATION ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfSpec", "SearchControl", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfInformationA(jitter):
    setupapi_SetupGetInfInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetInfInformationW(jitter):
    setupapi_SetupGetInfInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetIntField(jitter):
    """
    BOOL SetupGetIntField(
        PINFCONTEXT Context,
        DWORD FieldIndex,
        PINT IntegerValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "FieldIndex", "IntegerValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetLineByIndex(jitter, get_str, set_str):
    """
    BOOL SetupGetLineByIndex(
        HINF InfHandle,
        PCTSTR Section,
        DWORD Index,
        PINFCONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Section", "Index", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetLineByIndexA(jitter):
    setupapi_SetupGetLineByIndex(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetLineByIndexW(jitter):
    setupapi_SetupGetLineByIndex(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetLineCount(jitter, get_str, set_str):
    """
    LONG SetupGetLineCount(
        HINF InfHandle,
        PCTSTR Section
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Section"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetLineCountA(jitter):
    setupapi_SetupGetLineCount(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetLineCountW(jitter):
    setupapi_SetupGetLineCount(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetLineText(jitter, get_str, set_str):
    """
    BOOL SetupGetLineText(
        PINFCONTEXT Context,
        HINF InfHandle,
        PCTSTR Section,
        PCTSTR Key,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "InfHandle", "Section", "Key", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetLineTextA(jitter):
    setupapi_SetupGetLineText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetLineTextW(jitter):
    setupapi_SetupGetLineText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetMultiSzField(jitter, get_str, set_str):
    """
    BOOL SetupGetMultiSzField(
        PINFCONTEXT Context,
        DWORD FieldIndex,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        LPDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "FieldIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetMultiSzFieldA(jitter):
    setupapi_SetupGetMultiSzField(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetMultiSzFieldW(jitter):
    setupapi_SetupGetMultiSzField(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetSourceFileLocation(jitter, get_str, set_str):
    """
    BOOL SetupGetSourceFileLocation(
        HINF InfHandle,
        PINFCONTEXT InfContext,
        PCTSTR FileName,
        PUINT SourceId,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "FileName", "SourceId", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetSourceFileLocationA(jitter):
    setupapi_SetupGetSourceFileLocation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetSourceFileLocationW(jitter):
    setupapi_SetupGetSourceFileLocation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetSourceFileSize(jitter, get_str, set_str):
    """
    BOOL SetupGetSourceFileSize(
        HINF InfHandle,
        PINFCONTEXT InfContext,
        PCTSTR FileName,
        PCTSTR Section,
        PDWORD FileSize,
        UINT RoundingFactor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "FileName", "Section", "FileSize", "RoundingFactor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetSourceFileSizeA(jitter):
    setupapi_SetupGetSourceFileSize(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetSourceFileSizeW(jitter):
    setupapi_SetupGetSourceFileSize(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetSourceInfo(jitter, get_str, set_str):
    """
    BOOL SetupGetSourceInfo(
        HINF InfHandle,
        UINT SourceId,
        UINT InfoDesired,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        LPDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "SourceId", "InfoDesired", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetSourceInfoA(jitter):
    setupapi_SetupGetSourceInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetSourceInfoW(jitter):
    setupapi_SetupGetSourceInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetStringField(jitter, get_str, set_str):
    """
    BOOL SetupGetStringField(
        PINFCONTEXT Context,
        DWORD FieldIndex,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "FieldIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetStringFieldA(jitter):
    setupapi_SetupGetStringField(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetStringFieldW(jitter):
    setupapi_SetupGetStringField(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetTargetPath(jitter, get_str, set_str):
    """
    BOOL SetupGetTargetPath(
        HINF InfHandle,
        PINFCONTEXT InfContext,
        PCTSTR Section,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "Section", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetTargetPathA(jitter):
    setupapi_SetupGetTargetPath(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetTargetPathW(jitter):
    setupapi_SetupGetTargetPath(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupInitDefaultQueueCallback(jitter):
    """
    PVOID SetupInitDefaultQueueCallback(
        HWND OwnerWindow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OwnerWindow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInitDefaultQueueCallbackEx(jitter):
    """
    PVOID SetupInitDefaultQueueCallbackEx(
        HWND OwnerWindow,
        HWND AlternateProgressWindow,
        UINT ProgressMessage,
        DWORD Reserved1,
        PVOID Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OwnerWindow", "AlternateProgressWindow", "ProgressMessage", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInitializeFileLog(jitter, get_str, set_str):
    """
    HSPFILELOG SetupInitializeFileLog(
        PCTSTR LogFileName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogFileName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInitializeFileLogA(jitter):
    setupapi_SetupInitializeFileLog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupInitializeFileLogW(jitter):
    setupapi_SetupInitializeFileLog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupInstallFile(jitter, get_str, set_str):
    """
    BOOL SetupInstallFile(
        HINF InfHandle,
        PINFCONTEXT InfContext,
        PCTSTR SourceFile,
        PCTSTR SourcePathRoot,
        PCTSTR DestinationName,
        DWORD CopyStyle,
        PSP_FILE_CALLBACK CopyMsgHandler,
        PVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "SourceFile", "SourcePathRoot", "DestinationName", "CopyStyle", "CopyMsgHandler", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallFileA(jitter):
    setupapi_SetupInstallFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupInstallFileW(jitter):
    setupapi_SetupInstallFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupInstallFileEx(jitter, get_str, set_str):
    """
    BOOL SetupInstallFileEx(
        HINF InfHandle,
        PINFCONTEXT InfContext,
        PCTSTR SourceFile,
        PCTSTR SourcePathRoot,
        PCTSTR DestinationName,
        DWORD CopyStyle,
        PSP_FILE_CALLBACK CopyMsgHandler,
        PVOID Context,
        PBOOL FileWasInUse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "SourceFile", "SourcePathRoot", "DestinationName", "CopyStyle", "CopyMsgHandler", "Context", "FileWasInUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallFileExA(jitter):
    setupapi_SetupInstallFileEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupInstallFileExW(jitter):
    setupapi_SetupInstallFileEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupInstallFilesFromInfSection(jitter, get_str, set_str):
    """
    BOOL SetupInstallFilesFromInfSection(
        HINF InfHandle,
        HINF LayoutInfHandle,
        HSPFILEQ FileQueue,
        PCTSTR SectionName,
        PCTSTR SourceRootPath,
        UINT CopyFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "LayoutInfHandle", "FileQueue", "SectionName", "SourceRootPath", "CopyFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallFilesFromInfSectionA(jitter):
    setupapi_SetupInstallFilesFromInfSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupInstallFilesFromInfSectionW(jitter):
    setupapi_SetupInstallFilesFromInfSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupInstallFromInfSection(jitter, get_str, set_str):
    """
    BOOL SetupInstallFromInfSection(
        HWND Owner,
        HINF InfHandle,
        PCTSTR SectionName,
        [SPINST_FLAGS] Flags,
        HKEY RelativeKeyRoot,
        PCTSTR SourceRootPath,
        UINT CopyFlags,
        PSP_FILE_CALLBACK MsgHandler,
        PVOID Context,
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Owner", "InfHandle", "SectionName", "Flags", "RelativeKeyRoot", "SourceRootPath", "CopyFlags", "MsgHandler", "Context", "DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallFromInfSectionA(jitter):
    setupapi_SetupInstallFromInfSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupInstallFromInfSectionW(jitter):
    setupapi_SetupInstallFromInfSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupInstallServicesFromInfSection(jitter, get_str, set_str):
    """
    BOOL SetupInstallServicesFromInfSection(
        HINF InfHandle,
        PCTSTR SectionName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "SectionName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallServicesFromInfSectionA(jitter):
    setupapi_SetupInstallServicesFromInfSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupInstallServicesFromInfSectionW(jitter):
    setupapi_SetupInstallServicesFromInfSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupInstallServicesFromInfSectionEx(jitter, get_str, set_str):
    """
    BOOL SetupInstallServicesFromInfSectionEx(
        HINF InfHandle,
        PCTSTR SectionName,
        DWORD Flags,
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PVOID Reserved1,
        PVOID Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "SectionName", "Flags", "DeviceInfoSet", "DeviceInfoData", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallServicesFromInfSectionExA(jitter):
    setupapi_SetupInstallServicesFromInfSectionEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupInstallServicesFromInfSectionExW(jitter):
    setupapi_SetupInstallServicesFromInfSectionEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupIterateCabinet(jitter, get_str, set_str):
    """
    BOOL SetupIterateCabinet(
        PCTSTR CabinetFile,
        DWORD Reserved,
        PSP_FILE_CALLBACK MsgHandler,
        PVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CabinetFile", "Reserved", "MsgHandler", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupIterateCabinetA(jitter):
    setupapi_SetupIterateCabinet(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupIterateCabinetW(jitter):
    setupapi_SetupIterateCabinet(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupLogFile(jitter, get_str, set_str):
    """
    BOOL SetupLogFile(
        HSPFILELOG FileLogHandle,
        PCTSTR LogSectionName,
        PCTSTR SourceFileName,
        PCTSTR TargetFileName,
        DWORD Checksum,
        PCTSTR DiskTagfile,
        PCTSTR DiskDescription,
        PCTSTR OtherInfo,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileLogHandle", "LogSectionName", "SourceFileName", "TargetFileName", "Checksum", "DiskTagfile", "DiskDescription", "OtherInfo", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupLogFileA(jitter):
    setupapi_SetupLogFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupLogFileW(jitter):
    setupapi_SetupLogFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupLogError(jitter, get_str, set_str):
    """
    BOOL SetupLogError(
        PCTSTR MessageString,
        LogSeverity Severity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MessageString", "Severity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupLogErrorA(jitter):
    setupapi_SetupLogError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupLogErrorW(jitter):
    setupapi_SetupLogError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupOpenAppendInfFile(jitter, get_str, set_str):
    """
    BOOL SetupOpenAppendInfFile(
        PCTSTR FileName,
        HINF InfHandle,
        PUINT ErrorLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "InfHandle", "ErrorLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenAppendInfFileA(jitter):
    setupapi_SetupOpenAppendInfFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupOpenAppendInfFileW(jitter):
    setupapi_SetupOpenAppendInfFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupOpenFileQueue(jitter):
    """
    HSPFILEQ SetupOpenFileQueue()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenInfFile(jitter, get_str, set_str):
    """
    HINF SetupOpenInfFile(
        PCTSTR FileName,
        PCTSTR InfClass,
        [InfStyle] InfStyle,
        PUINT ErrorLine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "InfClass", "InfStyle", "ErrorLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenInfFileA(jitter):
    setupapi_SetupOpenInfFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupOpenInfFileW(jitter):
    setupapi_SetupOpenInfFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupOpenLog(jitter):
    """
    BOOL SetupOpenLog(
        BOOL Erase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Erase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCloseLog(jitter):
    """
    VOID SetupCloseLog()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenMasterInf(jitter):
    """
    HINF SetupOpenMasterInf()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupPromptForDisk(jitter, get_str, set_str):
    """
    UINT SetupPromptForDisk(
        HWND hwndParent,
        PCTSTR DialogTitle,
        PCTSTR DiskName,
        PCTSTR PathToSource,
        PCTSTR FileSought,
        PCTSTR TagFile,
        DWORD DiskPromptStyle,
        PTSTR PathBuffer,
        DWORD PathBufferSize,
        PDWORD PathRequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "DiskName", "PathToSource", "FileSought", "TagFile", "DiskPromptStyle", "PathBuffer", "PathBufferSize", "PathRequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupPromptForDiskA(jitter):
    setupapi_SetupPromptForDisk(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupPromptForDiskW(jitter):
    setupapi_SetupPromptForDisk(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupPromptReboot(jitter):
    """
    INT SetupPromptReboot(
        HSPFILEQ FileQueue,
        HWND Owner,
        BOOL ScanOnly
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "Owner", "ScanOnly"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryDrivesInDiskSpaceList(jitter, get_str, set_str):
    """
    BOOL SetupQueryDrivesInDiskSpaceList(
        HDSKSPC DiskSpace,
        PSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryDrivesInDiskSpaceListA(jitter):
    setupapi_SetupQueryDrivesInDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueryDrivesInDiskSpaceListW(jitter):
    setupapi_SetupQueryDrivesInDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueryFileLog(jitter, get_str, set_str):
    """
    BOOL SetupQueryFileLog(
        HSPFILELOG FileLogHandle,
        PCTSTR LogSectionName,
        PCTSTR TargetFileName,
        SetupFileLogInfo DesiredInfo,
        PTSTR DataOut,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileLogHandle", "LogSectionName", "TargetFileName", "DesiredInfo", "DataOut", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryFileLogA(jitter):
    setupapi_SetupQueryFileLog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueryFileLogW(jitter):
    setupapi_SetupQueryFileLog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueryInfFileInformation(jitter, get_str, set_str):
    """
    BOOL SetupQueryInfFileInformation(
        PSP_INF_INFORMATION InfInformation,
        UINT InfIndex,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfInformation", "InfIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryInfFileInformationA(jitter):
    setupapi_SetupQueryInfFileInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueryInfFileInformationW(jitter):
    setupapi_SetupQueryInfFileInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueryInfOriginalFileInformation(jitter, get_str, set_str):
    """
    BOOL SetupQueryInfOriginalFileInformation(
        PSP_INF_INFORMATION InfInformation,
        UINT InfIndex,
        PSP_ALTPLATFORM_INFO AlternatePlatformInfo,
        PSP_ORIGINAL_FILE_INFO OriginalFileInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfInformation", "InfIndex", "AlternatePlatformInfo", "OriginalFileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryInfOriginalFileInformationA(jitter):
    setupapi_SetupQueryInfOriginalFileInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueryInfOriginalFileInformationW(jitter):
    setupapi_SetupQueryInfOriginalFileInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueryInfVersionInformation(jitter, get_str, set_str):
    """
    BOOL SetupQueryInfVersionInformation(
        PSP_INF_INFORMATION InfInformation,
        UINT InfIndex,
        PCTSTR Key,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfInformation", "InfIndex", "Key", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryInfVersionInformationA(jitter):
    setupapi_SetupQueryInfVersionInformation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueryInfVersionInformationW(jitter):
    setupapi_SetupQueryInfVersionInformation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQuerySourceList(jitter, get_str, set_str):
    """
    BOOL SetupQuerySourceList(
        DWORD Flags,
        PCTSTR** List,
        PUINT Count
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "List", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQuerySourceListA(jitter):
    setupapi_SetupQuerySourceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQuerySourceListW(jitter):
    setupapi_SetupQuerySourceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQuerySpaceRequiredOnDrive(jitter, get_str, set_str):
    """
    BOOL SetupQuerySpaceRequiredOnDrive(
        HDSKSPC DiskSpace,
        PCTSTR DriveSpec,
        LONGLONG* SpaceRequired,
        PVOID Reserved1,
        UINT Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "DriveSpec", "SpaceRequired", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQuerySpaceRequiredOnDriveA(jitter):
    setupapi_SetupQuerySpaceRequiredOnDrive(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQuerySpaceRequiredOnDriveW(jitter):
    setupapi_SetupQuerySpaceRequiredOnDrive(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueueCopy(jitter, get_str, set_str):
    """
    BOOL SetupQueueCopy(
        HSPFILEQ QueueHandle,
        PCTSTR SourceRootPath,
        PCTSTR SourcePath,
        PCTSTR SourceFileName,
        PCTSTR SourceDescription,
        PCTSTR SourceTagFile,
        PCTSTR TargetDirectory,
        PCTSTR TargetFileName,
        DWORD CopyStyle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "SourceRootPath", "SourcePath", "SourceFileName", "SourceDescription", "SourceTagFile", "TargetDirectory", "TargetFileName", "CopyStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueCopyA(jitter):
    setupapi_SetupQueueCopy(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueueCopyW(jitter):
    setupapi_SetupQueueCopy(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueueCopyIndirect(jitter, get_str, set_str):
    """
    BOOL SetupQueueCopyIndirect(
        PSP_FILE_COPY_PARAMS CopyParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CopyParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueCopyIndirectA(jitter):
    setupapi_SetupQueueCopyIndirect(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueueCopyIndirectW(jitter):
    setupapi_SetupQueueCopyIndirect(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueueCopySection(jitter, get_str, set_str):
    """
    BOOL SetupQueueCopySection(
        HSPFILEQ QueueHandle,
        PCTSTR SourceRootPath,
        HINF InfHandle,
        HINF ListInfHandle,
        PCTSTR Section,
        DWORD CopyStyle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "SourceRootPath", "InfHandle", "ListInfHandle", "Section", "CopyStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueCopySectionA(jitter):
    setupapi_SetupQueueCopySection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueueCopySectionW(jitter):
    setupapi_SetupQueueCopySection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueueDefaultCopy(jitter, get_str, set_str):
    """
    BOOL SetupQueueDefaultCopy(
        HSPFILEQ QueueHandle,
        HINF InfHandle,
        PCTSTR SourceRootPath,
        PCTSTR SourceFileName,
        PCTSTR TargetFileName,
        DWORD CopyStyle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "InfHandle", "SourceRootPath", "SourceFileName", "TargetFileName", "CopyStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueDefaultCopyA(jitter):
    setupapi_SetupQueueDefaultCopy(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueueDefaultCopyW(jitter):
    setupapi_SetupQueueDefaultCopy(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueueDelete(jitter, get_str, set_str):
    """
    BOOL SetupQueueDelete(
        HSPFILEQ QueueHandle,
        PCTSTR PathPart1,
        PCTSTR PathPart2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "PathPart1", "PathPart2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueDeleteA(jitter):
    setupapi_SetupQueueDelete(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueueDeleteW(jitter):
    setupapi_SetupQueueDelete(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueueDeleteSection(jitter, get_str, set_str):
    """
    BOOL SetupQueueDeleteSection(
        HSPFILEQ QueueHandle,
        HINF InfHandle,
        HINF ListInfHandle,
        PCTSTR Section
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "InfHandle", "ListInfHandle", "Section"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueDeleteSectionA(jitter):
    setupapi_SetupQueueDeleteSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueueDeleteSectionW(jitter):
    setupapi_SetupQueueDeleteSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueueRename(jitter, get_str, set_str):
    """
    BOOL SetupQueueRename(
        HSPFILEQ QueueHandle,
        PCTSTR SourcePath,
        PCTSTR SourceFileName,
        PCTSTR TargetPath,
        PCTSTR TargetFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "SourcePath", "SourceFileName", "TargetPath", "TargetFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueRenameA(jitter):
    setupapi_SetupQueueRename(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueueRenameW(jitter):
    setupapi_SetupQueueRename(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupQueueRenameSection(jitter, get_str, set_str):
    """
    BOOL SetupQueueRenameSection(
        HSPFILEQ QueueHandle,
        HINF InfHandle,
        HINF ListInfHandle,
        PCTSTR Section
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "InfHandle", "ListInfHandle", "Section"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueRenameSectionA(jitter):
    setupapi_SetupQueueRenameSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupQueueRenameSectionW(jitter):
    setupapi_SetupQueueRenameSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupRemoveFileLogEntry(jitter, get_str, set_str):
    """
    BOOL SetupRemoveFileLogEntry(
        HSPFILELOG FileLogHandle,
        PCTSTR LogSectionName,
        PCTSTR TargetFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileLogHandle", "LogSectionName", "TargetFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveFileLogEntryA(jitter):
    setupapi_SetupRemoveFileLogEntry(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupRemoveFileLogEntryW(jitter):
    setupapi_SetupRemoveFileLogEntry(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupRemoveFromDiskSpaceList(jitter, get_str, set_str):
    """
    BOOL SetupRemoveFromDiskSpaceList(
        HDSKSPC DiskSpace,
        PCTSTR TargetFilespec,
        UINT Operation,
        PVOID Reserved1,
        UINT Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "TargetFilespec", "Operation", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveFromDiskSpaceListA(jitter):
    setupapi_SetupRemoveFromDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupRemoveFromDiskSpaceListW(jitter):
    setupapi_SetupRemoveFromDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupRemoveFromSourceList(jitter, get_str, set_str):
    """
    BOOL SetupRemoveFromSourceList(
        DWORD Flags,
        PCTSTR Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveFromSourceListA(jitter):
    setupapi_SetupRemoveFromSourceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupRemoveFromSourceListW(jitter):
    setupapi_SetupRemoveFromSourceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupRemoveInstallSectionFromDiskSpaceList(jitter, get_str, set_str):
    """
    BOOL SetupRemoveInstallSectionFromDiskSpaceList(
        HDSKSPC DiskSpace,
        HINF InfHandle,
        HINF LayoutInfHandle,
        PCTSTR SectionName,
        PVOID Reserved1,
        UINT Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "InfHandle", "LayoutInfHandle", "SectionName", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveInstallSectionFromDiskSpaceListA(jitter):
    setupapi_SetupRemoveInstallSectionFromDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupRemoveInstallSectionFromDiskSpaceListW(jitter):
    setupapi_SetupRemoveInstallSectionFromDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupRemoveSectionFromDiskSpaceList(jitter, get_str, set_str):
    """
    BOOL SetupRemoveSectionFromDiskSpaceList(
        HDSKSPC DiskSpace,
        HINF InfHandle,
        HINF ListInfHandle,
        PCTSTR SectionName,
        UINT Operation,
        PVOID Reserved1,
        UINT Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "InfHandle", "ListInfHandle", "SectionName", "Operation", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveSectionFromDiskSpaceListA(jitter):
    setupapi_SetupRemoveSectionFromDiskSpaceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupRemoveSectionFromDiskSpaceListW(jitter):
    setupapi_SetupRemoveSectionFromDiskSpaceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupRenameError(jitter, get_str, set_str):
    """
    UINT SetupRenameError(
        HWND hwndParent,
        PCTSTR DialogTitle,
        PCTSTR SourceFile,
        PCTSTR TargetFile,
        UINT Win32ErrorCode,
        DWORD Style
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "SourceFile", "TargetFile", "Win32ErrorCode", "Style"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRenameErrorA(jitter):
    setupapi_SetupRenameError(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupRenameErrorW(jitter):
    setupapi_SetupRenameError(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupScanFileQueue(jitter, get_str, set_str):
    """
    BOOL SetupScanFileQueue(
        HSPFILEQ FileQueue,
        DWORD Flags,
        HWND Window,
        PSP_FILE_CALLBACK CallbackRoutine,
        PVOID CallbackContext,
        PDWORD Result
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "Flags", "Window", "CallbackRoutine", "CallbackContext", "Result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupScanFileQueueA(jitter):
    setupapi_SetupScanFileQueue(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupScanFileQueueW(jitter):
    setupapi_SetupScanFileQueue(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupSetDirectoryId(jitter, get_str, set_str):
    """
    BOOL SetupSetDirectoryId(
        HINF InfHandle,
        DWORD Id,
        PCTSTR Directory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Id", "Directory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetDirectoryIdA(jitter):
    setupapi_SetupSetDirectoryId(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupSetDirectoryIdW(jitter):
    setupapi_SetupSetDirectoryId(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupSetDirectoryIdEx(jitter, get_str, set_str):
    """
    BOOL SetupSetDirectoryIdEx(
        HINF InfHandle,
        DWORD Id,
        PCTSTR Directory,
        DWORD Flags,
        DWORD Reserved1,
        PVOID Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Id", "Directory", "Flags", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetDirectoryIdExA(jitter):
    setupapi_SetupSetDirectoryIdEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupSetDirectoryIdExW(jitter):
    setupapi_SetupSetDirectoryIdEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupSetFileQueueAlternatePlatform(jitter, get_str, set_str):
    """
    BOOL SetupSetFileQueueAlternatePlatform(
        HSPFILEQ QueueHandle,
        PSP_ALTPLATFORM_INFO AlternatePlatformInfo,
        PCWSTR AlternateDefaultCatalogFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "AlternatePlatformInfo", "AlternateDefaultCatalogFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetFileQueueAlternatePlatformA(jitter):
    setupapi_SetupSetFileQueueAlternatePlatform(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupSetFileQueueAlternatePlatformW(jitter):
    setupapi_SetupSetFileQueueAlternatePlatform(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupSetFileQueueFlags(jitter):
    """
    BOOL SetupSetFileQueueFlags(
        HSPFILEQ FileQueue,
        DWORD FlagMask,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "FlagMask", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetPlatformPathOverride(jitter, get_str, set_str):
    """
    BOOL SetupSetPlatformPathOverride(
        PCTSTR Override
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Override"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetPlatformPathOverrideA(jitter):
    setupapi_SetupSetPlatformPathOverride(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupSetPlatformPathOverrideW(jitter):
    setupapi_SetupSetPlatformPathOverride(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupSetSourceList(jitter, get_str, set_str):
    """
    BOOL SetupSetSourceList(
        DWORD Flags,
        PCTSTR* SourceList,
        UINT SourceCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "SourceList", "SourceCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetSourceListA(jitter):
    setupapi_SetupSetSourceList(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupSetSourceListW(jitter):
    setupapi_SetupSetSourceList(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupTermDefaultQueueCallback(jitter):
    """
    VOID SetupTermDefaultQueueCallback(
        PVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupTerminateFileLog(jitter):
    """
    BOOL SetupTerminateFileLog(
        HSPFILELOG FileLogHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileLogHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupUninstallNewlyCopiedInfs(jitter):
    """
    BOOL SetupUninstallNewlyCopiedInfs(
        HSPFILEQ QueueHandle,
        DWORD Flags,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupUninstallOEMInf(jitter, get_str, set_str):
    """
    BOOL SetupUninstallOEMInf(
        PCWSTR InfFileName,
        DWORD Flags,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfFileName", "Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupUninstallOEMInfA(jitter):
    setupapi_SetupUninstallOEMInf(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupUninstallOEMInfW(jitter):
    setupapi_SetupUninstallOEMInf(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupVerifyInfFile(jitter, get_str, set_str):
    """
    BOOL SetupVerifyInfFile(
        PCWSTR InfName,
        PSP_ALTPLATFORM_INFO AltPlatformInfo,
        PSP_INF_SIGNER_INFO InfFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfName", "AltPlatformInfo", "InfFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupVerifyInfFileA(jitter):
    setupapi_SetupVerifyInfFile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupVerifyInfFileW(jitter):
    setupapi_SetupVerifyInfFile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetInfDriverStoreLocation(jitter, get_str, set_str):
    """
    BOOL SetupGetInfDriverStoreLocation(
        PCTSTR FileName,
        PSP_ALTPLATFORM_INFO AlternatePlatformInfo,
        PCTSTR LocaleName,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "AlternatePlatformInfo", "LocaleName", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfDriverStoreLocationA(jitter):
    setupapi_SetupGetInfDriverStoreLocation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetInfDriverStoreLocationW(jitter):
    setupapi_SetupGetInfDriverStoreLocation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetInfPublishedName(jitter, get_str, set_str):
    """
    BOOL SetupGetInfPublishedName(
        PCTSTR DriverStoreLocation,
        PTSTR ReturnBuffer,
        DWORD ReturnBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DriverStoreLocation", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfPublishedNameA(jitter):
    setupapi_SetupGetInfPublishedName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupGetInfPublishedNameW(jitter):
    setupapi_SetupGetInfPublishedName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupGetNonInteractiveMode(jitter):
    """
    BOOL SetupGetNonInteractiveMode()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetNonInteractiveMode(jitter):
    """
    BOOL SetupSetNonInteractiveMode(
        BOOL NonInteractiveFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NonInteractiveFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiAskForOEMDisk(jitter):
    """
    BOOL SetupDiAskForOEMDisk(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiBuildClassInfoList(jitter):
    """
    BOOL SetupDiBuildClassInfoList(
        [SetupDiBuildClassInfoListFlags] Flags,
        LPGUID ClassGuidList,
        DWORD ClassGuidListSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "ClassGuidList", "ClassGuidListSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiBuildClassInfoListEx(jitter, get_str, set_str):
    """
    BOOL SetupDiBuildClassInfoListEx(
        [SetupDiBuildClassInfoListFlags] Flags,
        LPGUID ClassGuidList,
        DWORD ClassGuidListSize,
        PDWORD RequiredSize,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "ClassGuidList", "ClassGuidListSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiBuildClassInfoListExA(jitter):
    setupapi_SetupDiBuildClassInfoListEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiBuildClassInfoListExW(jitter):
    setupapi_SetupDiBuildClassInfoListEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiBuildDriverInfoList(jitter):
    """
    BOOL SetupDiBuildDriverInfoList(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        [DiDriverType] DriverType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCallClassInstaller(jitter):
    """
    BOOL SetupDiCallClassInstaller(
        DI_FUNCTION InstallFunction,
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InstallFunction", "DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCancelDriverInfoSearch(jitter):
    """
    BOOL SetupDiCancelDriverInfoSearch(
        HDEVINFO DeviceInfoSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiChangeState(jitter):
    """
    BOOL SetupDiChangeState(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassGuidsFromName(jitter, get_str, set_str):
    """
    BOOL SetupDiClassGuidsFromName(
        PCTSTR ClassName,
        LPGUID ClassGuidList,
        DWORD ClassGuidListSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassName", "ClassGuidList", "ClassGuidListSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassGuidsFromNameA(jitter):
    setupapi_SetupDiClassGuidsFromName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiClassGuidsFromNameW(jitter):
    setupapi_SetupDiClassGuidsFromName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiClassGuidsFromNameEx(jitter, get_str, set_str):
    """
    BOOL SetupDiClassGuidsFromNameEx(
        PCTSTR ClassName,
        LPGUID ClassGuidList,
        DWORD ClassGuidListSize,
        PDWORD RequiredSize,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassName", "ClassGuidList", "ClassGuidListSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassGuidsFromNameExA(jitter):
    setupapi_SetupDiClassGuidsFromNameEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiClassGuidsFromNameExW(jitter):
    setupapi_SetupDiClassGuidsFromNameEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiClassNameFromGuid(jitter, get_str, set_str):
    """
    BOOL SetupDiClassNameFromGuid(
        LPGUID ClassGuid,
        PTSTR ClassName,
        DWORD ClassNameSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ClassName", "ClassNameSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassNameFromGuidA(jitter):
    setupapi_SetupDiClassNameFromGuid(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiClassNameFromGuidW(jitter):
    setupapi_SetupDiClassNameFromGuid(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiClassNameFromGuidEx(jitter, get_str, set_str):
    """
    BOOL SetupDiClassNameFromGuidEx(
        LPGUID ClassGuid,
        PTSTR ClassName,
        DWORD ClassNameSize,
        PDWORD RequiredSize,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ClassName", "ClassNameSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassNameFromGuidExA(jitter):
    setupapi_SetupDiClassNameFromGuidEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiClassNameFromGuidExW(jitter):
    setupapi_SetupDiClassNameFromGuidEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiCreateDeviceInfo(jitter, get_str, set_str):
    """
    BOOL SetupDiCreateDeviceInfo(
        HDEVINFO DeviceInfoSet,
        PCTSTR DeviceName,
        LPGUID ClassGuid,
        PCTSTR DeviceDescription,
        HWND hwndParent,
        [SetupDiCreateDeviceInfoFlags] CreationFlags,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceName", "ClassGuid", "DeviceDescription", "hwndParent", "CreationFlags", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInfoA(jitter):
    setupapi_SetupDiCreateDeviceInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiCreateDeviceInfoW(jitter):
    setupapi_SetupDiCreateDeviceInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiCreateDeviceInfoList(jitter):
    """
    HDEVINFO SetupDiCreateDeviceInfoList(
        LPGUID ClassGuid,
        HWND hwndParent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInfoListEx(jitter, get_str, set_str):
    """
    HDEVINFO SetupDiCreateDeviceInfoListEx(
        LPGUID ClassGuid,
        HWND hwndParent,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "hwndParent", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInfoListExA(jitter):
    setupapi_SetupDiCreateDeviceInfoListEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiCreateDeviceInfoListExW(jitter):
    setupapi_SetupDiCreateDeviceInfoListEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiCreateDeviceInterface(jitter, get_str, set_str):
    """
    BOOL SetupDiCreateDeviceInterface(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        LPGUID InterfaceClassGuid,
        PCTSTR ReferenceString,
        DWORD CreationFlags,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "InterfaceClassGuid", "ReferenceString", "CreationFlags", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInterfaceA(jitter):
    setupapi_SetupDiCreateDeviceInterface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiCreateDeviceInterfaceW(jitter):
    setupapi_SetupDiCreateDeviceInterface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiCreateDeviceInterfaceRegKey(jitter, get_str, set_str):
    """
    HKEY SetupDiCreateDeviceInterfaceRegKey(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        DWORD Reserved,
        REGSAM samDesired,
        HINF InfHandle,
        PCTSTR InfSectionName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "Reserved", "samDesired", "InfHandle", "InfSectionName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInterfaceRegKeyA(jitter):
    setupapi_SetupDiCreateDeviceInterfaceRegKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiCreateDeviceInterfaceRegKeyW(jitter):
    setupapi_SetupDiCreateDeviceInterfaceRegKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiCreateDevRegKey(jitter, get_str, set_str):
    """
    HKEY SetupDiCreateDevRegKey(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        [DeviceInfoScope] Scope,
        DWORD HwProfile,
        [DeviceInfoKeyType] KeyType,
        HINF InfHandle,
        PCTSTR InfSectionName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Scope", "HwProfile", "KeyType", "InfHandle", "InfSectionName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDevRegKeyA(jitter):
    setupapi_SetupDiCreateDevRegKey(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiCreateDevRegKeyW(jitter):
    setupapi_SetupDiCreateDevRegKey(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiDeleteDeviceInfo(jitter):
    """
    BOOL SetupDiDeleteDeviceInfo(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDeleteDeviceInterfaceData(jitter):
    """
    BOOL SetupDiDeleteDeviceInterfaceData(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDeleteDeviceInterfaceRegKey(jitter):
    """
    BOOL SetupDiDeleteDeviceInterfaceRegKey(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        DWORD Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDeleteDevRegKey(jitter):
    """
    BOOL SetupDiDeleteDevRegKey(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        [DeviceInfoScope] Scope,
        DWORD HwProfile,
        [DeviceInfoKeyType] KeyType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Scope", "HwProfile", "KeyType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDestroyClassImageList(jitter):
    """
    BOOL SetupDiDestroyClassImageList(
        PSP_CLASSIMAGELIST_DATA ClassImageListData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassImageListData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDestroyDeviceInfoList(jitter):
    """
    BOOL SetupDiDestroyDeviceInfoList(
        HDEVINFO DeviceInfoSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDestroyDriverInfoList(jitter):
    """
    BOOL SetupDiDestroyDriverInfoList(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        [DiDriverType] DriverType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDrawMiniIcon(jitter):
    """
    INT SetupDiDrawMiniIcon(
        HDC hdc,
        RECT rc,
        INT MiniIconIndex,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "rc", "MiniIconIndex", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiEnumDeviceInfo(jitter):
    """
    BOOL SetupDiEnumDeviceInfo(
        HDEVINFO DeviceInfoSet,
        DWORD MemberIndex,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "MemberIndex", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiEnumDeviceInterfaces(jitter):
    """
    BOOL SetupDiEnumDeviceInterfaces(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        LPGUID InterfaceClassGuid,
        DWORD MemberIndex,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "InterfaceClassGuid", "MemberIndex", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiEnumDriverInfo(jitter, get_str, set_str):
    """
    BOOL SetupDiEnumDriverInfo(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        [DiDriverType] DriverType,
        DWORD MemberIndex,
        PSP_DRVINFO_DATA DriverInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverType", "MemberIndex", "DriverInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiEnumDriverInfoA(jitter):
    setupapi_SetupDiEnumDriverInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiEnumDriverInfoW(jitter):
    setupapi_SetupDiEnumDriverInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiFinishInstallAction(jitter):
    """
    BOOL SetupDiFinishInstallAction(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetActualModelsSection(jitter, get_str, set_str):
    """
    BOOL SetupDiGetActualModelsSection(
        PINFCONTEXT Context,
        PSP_ALTPLATFORM_INFO AlternatePlatformInfo,
        PTSTR DecoratedModelsSection,
        DWORD DecoratedModelsSectionSize,
        PDWORD RequiredSize,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "AlternatePlatformInfo", "DecoratedModelsSection", "DecoratedModelsSectionSize", "RequiredSize", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetActualModelsSectionA(jitter):
    setupapi_SetupDiGetActualModelsSection(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetActualModelsSectionW(jitter):
    setupapi_SetupDiGetActualModelsSection(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetActualSectionToInstall(jitter, get_str, set_str):
    """
    BOOL SetupDiGetActualSectionToInstall(
        HINF InfHandle,
        PCTSTR InfSectionName,
        PTSTR InfSectionWithExt,
        DWORD InfSectionWithExtSize,
        PDWORD RequiredSize,
        PTSTR* Extension
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfSectionName", "InfSectionWithExt", "InfSectionWithExtSize", "RequiredSize", "Extension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetActualSectionToInstallA(jitter):
    setupapi_SetupDiGetActualSectionToInstall(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetActualSectionToInstallW(jitter):
    setupapi_SetupDiGetActualSectionToInstall(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetActualSectionToInstallEx(jitter, get_str, set_str):
    """
    BOOL SetupDiGetActualSectionToInstallEx(
        HINF InfHandle,
        PCTSTR InfSectionName,
        PSP_ALTPLATFORM_INFO AlternatePlatformInfo,
        PTSTR InfSectionWithExt,
        DWORD InfSectionWithExtSize,
        PDWORD RequiredSize,
        PTSTR* Extension,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfSectionName", "AlternatePlatformInfo", "InfSectionWithExt", "InfSectionWithExtSize", "RequiredSize", "Extension", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetActualSectionToInstallExA(jitter):
    setupapi_SetupDiGetActualSectionToInstallEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetActualSectionToInstallExW(jitter):
    setupapi_SetupDiGetActualSectionToInstallEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetClassBitmapIndex(jitter):
    """
    BOOL SetupDiGetClassBitmapIndex(
        LPGUID ClassGuid,
        PINT MiniIconIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "MiniIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDescription(jitter, get_str, set_str):
    """
    BOOL SetupDiGetClassDescription(
        LPGUID ClassGuid,
        PTSTR ClassDescription,
        DWORD ClassDescriptionSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ClassDescription", "ClassDescriptionSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDescriptionA(jitter):
    setupapi_SetupDiGetClassDescription(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetClassDescriptionW(jitter):
    setupapi_SetupDiGetClassDescription(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetClassDescriptionEx(jitter, get_str, set_str):
    """
    BOOL SetupDiGetClassDescriptionEx(
        LPGUID ClassGuid,
        PTSTR ClassDescription,
        DWORD ClassDescriptionSize,
        PDWORD RequiredSize,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ClassDescription", "ClassDescriptionSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDescriptionExA(jitter):
    setupapi_SetupDiGetClassDescriptionEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetClassDescriptionExW(jitter):
    setupapi_SetupDiGetClassDescriptionEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetClassDevPropertySheets(jitter, get_str, set_str):
    """
    BOOL SetupDiGetClassDevPropertySheets(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        LPPROPSHEETHEADER PropertySheetHeader,
        DWORD PropertySheetHeaderPageListSize,
        PDWORD RequiredSize,
        [DiGetClassDevPropertySheetsType] PropertySheetType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "PropertySheetHeader", "PropertySheetHeaderPageListSize", "RequiredSize", "PropertySheetType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDevPropertySheetsA(jitter):
    setupapi_SetupDiGetClassDevPropertySheets(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetClassDevPropertySheetsW(jitter):
    setupapi_SetupDiGetClassDevPropertySheets(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetClassDevs(jitter, get_str, set_str):
    """
    HDEVINFO SetupDiGetClassDevs(
        LPGUID ClassGuid,
        PCTSTR Enumerator,
        HWND hwndParent,
        [DeviceInfoGetFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Enumerator", "hwndParent", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDevsA(jitter):
    setupapi_SetupDiGetClassDevs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetClassDevsW(jitter):
    setupapi_SetupDiGetClassDevs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetClassDevsEx(jitter, get_str, set_str):
    """
    HDEVINFO SetupDiGetClassDevsEx(
        LPGUID ClassGuid,
        PCTSTR Enumerator,
        HWND hwndParent,
        [DeviceInfoGetFlags] Flags,
        HDEVINFO DeviceInfoSet,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Enumerator", "hwndParent", "Flags", "DeviceInfoSet", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDevsExA(jitter):
    setupapi_SetupDiGetClassDevsEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetClassDevsExW(jitter):
    setupapi_SetupDiGetClassDevsEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetClassImageIndex(jitter):
    """
    BOOL SetupDiGetClassImageIndex(
        PSP_CLASSIMAGELIST_DATA ClassImageListData,
        LPGUID ClassGuid,
        PINT ImageIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassImageListData", "ClassGuid", "ImageIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassImageList(jitter):
    """
    BOOL SetupDiGetClassImageList(
        PSP_CLASSIMAGELIST_DATA ClassImageListData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassImageListData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassImageListEx(jitter, get_str, set_str):
    """
    BOOL SetupDiGetClassImageListEx(
        PSP_CLASSIMAGELIST_DATA ClassImageListData,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassImageListData", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassImageListExA(jitter):
    setupapi_SetupDiGetClassImageListEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetClassImageListExW(jitter):
    setupapi_SetupDiGetClassImageListEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetClassInstallParams(jitter, get_str, set_str):
    """
    BOOL SetupDiGetClassInstallParams(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_CLASSINSTALL_HEADER ClassInstallParams,
        DWORD ClassInstallParamsSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "ClassInstallParams", "ClassInstallParamsSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassInstallParamsA(jitter):
    setupapi_SetupDiGetClassInstallParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetClassInstallParamsW(jitter):
    setupapi_SetupDiGetClassInstallParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetClassPropertyW(jitter):
    """
    BOOL SetupDiGetClassPropertyW(
        CONST GUID* ClassGuid,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        PDWORD RequiredSize,
        [DiClassPropertyFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassPropertyExW(jitter):
    """
    BOOL SetupDiGetClassPropertyExW(
        CONST GUID* ClassGuid,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        PDWORD RequiredSize,
        [DiClassPropertyFlags] Flags,
        PCWSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "Flags", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassPropertyKeys(jitter):
    """
    BOOL SetupDiGetClassPropertyKeys(
        CONST GUID* ClassGuid,
        DEVPROPKEY* PropertyKeyArray,
        DWORD PropertyKeyCount,
        PDWORD RequiredPropertyKeyCount,
        [DiClassPropertyFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKeyArray", "PropertyKeyCount", "RequiredPropertyKeyCount", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassPropertyKeysExW(jitter):
    """
    BOOL SetupDiGetClassPropertyKeysExW(
        CONST GUID* ClassGuid,
        DEVPROPKEY* PropertyKeyArray,
        DWORD PropertyKeyCount,
        PDWORD RequiredPropertyKeyCount,
        [DiClassPropertyFlags] Flags,
        PCWSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKeyArray", "PropertyKeyCount", "RequiredPropertyKeyCount", "Flags", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassRegistryProperty(jitter, get_str, set_str):
    """
    BOOL SetupDiGetClassRegistryProperty(
        LPGUID ClassGuid,
        DWORD Property,
        [RegType*] PropertyRegDataType,
        PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        PDWORD RequiredSize,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Property", "PropertyRegDataType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassRegistryPropertyA(jitter):
    setupapi_SetupDiGetClassRegistryProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetClassRegistryPropertyW(jitter):
    setupapi_SetupDiGetClassRegistryProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetCustomDeviceProperty(jitter, get_str, set_str):
    """
    BOOL SetupDiGetCustomDeviceProperty(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PCTSTR CustomPropertyName,
        [GetCustomDevicePropertyFlags] Flags,
        [RegType*] PropertyRegDataType,
        PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "CustomPropertyName", "Flags", "PropertyRegDataType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetCustomDevicePropertyA(jitter):
    setupapi_SetupDiGetCustomDeviceProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetCustomDevicePropertyW(jitter):
    setupapi_SetupDiGetCustomDeviceProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetDeviceInfoListClass(jitter):
    """
    BOOL SetupDiGetDeviceInfoListClass(
        HDEVINFO DeviceInfoSet,
        LPGUID ClassGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "ClassGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInfoListDetail(jitter, get_str, set_str):
    """
    BOOL SetupDiGetDeviceInfoListDetail(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_LIST_DETAIL_DATA DeviceInfoSetDetailData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoSetDetailData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInfoListDetailA(jitter):
    setupapi_SetupDiGetDeviceInfoListDetail(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetDeviceInfoListDetailW(jitter):
    setupapi_SetupDiGetDeviceInfoListDetail(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetDeviceInstallParams(jitter, get_str, set_str):
    """
    BOOL SetupDiGetDeviceInstallParams(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_DEVINSTALL_PARAMS DeviceInstallParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DeviceInstallParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInstallParamsA(jitter):
    setupapi_SetupDiGetDeviceInstallParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetDeviceInstallParamsW(jitter):
    setupapi_SetupDiGetDeviceInstallParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetDeviceInstanceId(jitter, get_str, set_str):
    """
    BOOL SetupDiGetDeviceInstanceId(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PTSTR DeviceInstanceId,
        DWORD DeviceInstanceIdSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DeviceInstanceId", "DeviceInstanceIdSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInstanceIdA(jitter):
    setupapi_SetupDiGetDeviceInstanceId(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetDeviceInstanceIdW(jitter):
    setupapi_SetupDiGetDeviceInstanceId(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetDeviceInterfaceAlias(jitter):
    """
    BOOL SetupDiGetDeviceInterfaceAlias(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        LPGUID AliasInterfaceClassGuid,
        PSP_DEVICE_INTERFACE_DATA AliasDeviceInterfaceData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "AliasInterfaceClassGuid", "AliasDeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInterfaceDetail(jitter, get_str, set_str):
    """
    BOOL SetupDiGetDeviceInterfaceDetail(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        PSP_DEVICE_INTERFACE_DETAIL_DATA DeviceInterfaceDetailData,
        DWORD DeviceInterfaceDetailDataSize,
        PDWORD RequiredSize,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "DeviceInterfaceDetailData", "DeviceInterfaceDetailDataSize", "RequiredSize", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInterfaceDetailA(jitter):
    setupapi_SetupDiGetDeviceInterfaceDetail(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetDeviceInterfaceDetailW(jitter):
    setupapi_SetupDiGetDeviceInterfaceDetail(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetDeviceInterfacePropertyW(jitter):
    """
    BOOL SetupDiGetDeviceInterfacePropertyW(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        PDWORD RequiredSize,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInterfacePropertyKeys(jitter):
    """
    BOOL SetupDiGetDeviceInterfacePropertyKeys(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        DEVPROPKEY* PropertyKeyArray,
        DWORD PropertyKeyCount,
        PDWORD RequiredPropertyKeyCount,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "PropertyKeyArray", "PropertyKeyCount", "RequiredPropertyKeyCount", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDevicePropertyW(jitter):
    """
    BOOL SetupDiGetDevicePropertyW(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE* PropertyType,
        PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        PDWORD RequiredSize,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDevicePropertyKeys(jitter):
    """
    BOOL SetupDiGetDevicePropertyKeys(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        DEVPROPKEY* PropertyKeyArray,
        DWORD PropertyKeyCount,
        PDWORD RequiredPropertyKeyCount,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "PropertyKeyArray", "PropertyKeyCount", "RequiredPropertyKeyCount", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceRegistryProperty(jitter, get_str, set_str):
    """
    BOOL SetupDiGetDeviceRegistryProperty(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        [SetupDeviceRegistryProperty] Property,
        [RegType*] PropertyRegDataType,
        PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Property", "PropertyRegDataType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceRegistryPropertyA(jitter):
    setupapi_SetupDiGetDeviceRegistryProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetDeviceRegistryPropertyW(jitter):
    setupapi_SetupDiGetDeviceRegistryProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetDriverInfoDetail(jitter, get_str, set_str):
    """
    BOOL SetupDiGetDriverInfoDetail(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_DRVINFO_DATA DriverInfoData,
        PSP_DRVINFO_DETAIL_DATA DriverInfoDetailData,
        DWORD DriverInfoDetailDataSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData", "DriverInfoDetailData", "DriverInfoDetailDataSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDriverInfoDetailA(jitter):
    setupapi_SetupDiGetDriverInfoDetail(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetDriverInfoDetailW(jitter):
    setupapi_SetupDiGetDriverInfoDetail(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetDriverInstallParams(jitter, get_str, set_str):
    """
    BOOL SetupDiGetDriverInstallParams(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_DRVINFO_DATA DriverInfoData,
        PSP_DRVINSTALL_PARAMS DriverInstallParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData", "DriverInstallParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDriverInstallParamsA(jitter):
    setupapi_SetupDiGetDriverInstallParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetDriverInstallParamsW(jitter):
    setupapi_SetupDiGetDriverInstallParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetHwProfileFriendlyName(jitter, get_str, set_str):
    """
    BOOL SetupDiGetHwProfileFriendlyName(
        DWORD HwProfile,
        PTSTR FriendlyName,
        DWORD FriendlyNameSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HwProfile", "FriendlyName", "FriendlyNameSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetHwProfileFriendlyNameA(jitter):
    setupapi_SetupDiGetHwProfileFriendlyName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetHwProfileFriendlyNameW(jitter):
    setupapi_SetupDiGetHwProfileFriendlyName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetHwProfileFriendlyNameEx(jitter, get_str, set_str):
    """
    BOOL SetupDiGetHwProfileFriendlyNameEx(
        DWORD HwProfile,
        PTSTR FriendlyName,
        DWORD FriendlyNameSize,
        PDWORD RequiredSize,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HwProfile", "FriendlyName", "FriendlyNameSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetHwProfileFriendlyNameExA(jitter):
    setupapi_SetupDiGetHwProfileFriendlyNameEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetHwProfileFriendlyNameExW(jitter):
    setupapi_SetupDiGetHwProfileFriendlyNameEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetHwProfileList(jitter):
    """
    BOOL SetupDiGetHwProfileList(
        PDWORD HwProfileList,
        DWORD HwProfileListSize,
        PDWORD RequiredSize,
        PDWORD CurrentlyActiveIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HwProfileList", "HwProfileListSize", "RequiredSize", "CurrentlyActiveIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetHwProfileListEx(jitter, get_str, set_str):
    """
    BOOL SetupDiGetHwProfileListEx(
        PDWORD HwProfileList,
        DWORD HwProfileListSize,
        PDWORD RequiredSize,
        PDWORD CurrentlyActiveIndex,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HwProfileList", "HwProfileListSize", "RequiredSize", "CurrentlyActiveIndex", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetHwProfileListExA(jitter):
    setupapi_SetupDiGetHwProfileListEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetHwProfileListExW(jitter):
    setupapi_SetupDiGetHwProfileListEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetINFClass(jitter, get_str, set_str):
    """
    BOOL SetupDiGetINFClass(
        PCTSTR InfName,
        LPGUID ClassGuid,
        PTSTR ClassName,
        DWORD ClassNameSize,
        PDWORD RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InfName", "ClassGuid", "ClassName", "ClassNameSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetINFClassA(jitter):
    setupapi_SetupDiGetINFClass(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetINFClassW(jitter):
    setupapi_SetupDiGetINFClass(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetSelectedDevice(jitter):
    """
    BOOL SetupDiGetSelectedDevice(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetSelectedDriver(jitter, get_str, set_str):
    """
    BOOL SetupDiGetSelectedDriver(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_DRVINFO_DATA DriverInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetSelectedDriverA(jitter):
    setupapi_SetupDiGetSelectedDriver(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiGetSelectedDriverW(jitter):
    setupapi_SetupDiGetSelectedDriver(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiGetWizardPage(jitter):
    """
    HPROPSHEETPAGE SetupDiGetWizardPage(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_INSTALLWIZARD_DATA InstallWizardData,
        DWORD PageType,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "InstallWizardData", "PageType", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallClass(jitter, get_str, set_str):
    """
    BOOL SetupDiInstallClass(
        HWND hwndParent,
        PCTSTR InfFileName,
        DWORD Flags,
        HSPFILEQ FileQueue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "InfFileName", "Flags", "FileQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallClassA(jitter):
    setupapi_SetupDiInstallClass(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiInstallClassW(jitter):
    setupapi_SetupDiInstallClass(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiInstallClassEx(jitter, get_str, set_str):
    """
    BOOL SetupDiInstallClassEx(
        HWND hwndParent,
        PCTSTR InfFileName,
        DWORD Flags,
        HSPFILEQ FileQueue,
        LPGUID InterfaceClassGuid,
        PVOID Reserved1,
        PVOID Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "InfFileName", "Flags", "FileQueue", "InterfaceClassGuid", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallClassExA(jitter):
    setupapi_SetupDiInstallClassEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiInstallClassExW(jitter):
    setupapi_SetupDiInstallClassEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiInstallDevice(jitter):
    """
    BOOL SetupDiInstallDevice(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallDeviceInterfaces(jitter):
    """
    BOOL SetupDiInstallDeviceInterfaces(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallDriverFiles(jitter):
    """
    BOOL SetupDiInstallDriverFiles(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiLoadClassIcon(jitter):
    """
    BOOL SetupDiLoadClassIcon(
        LPGUID ClassGuid,
        HICON* LargeIcon,
        LPINT MiniIconIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "LargeIcon", "MiniIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiLoadDeviceIcon(jitter):
    """
    BOOL SetupDiLoadDeviceIcon(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        UINT cxIcon,
        UINT cyIcon,
        DWORD Flags,
        HICON* hIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "cxIcon", "cyIcon", "Flags", "hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenClassRegKey(jitter):
    """
    HKEY SetupDiOpenClassRegKey(
        LPGUID ClassGuid,
        REGSAM samDesired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "samDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenClassRegKeyEx(jitter, get_str, set_str):
    """
    HKEY SetupDiOpenClassRegKeyEx(
        LPGUID ClassGuid,
        REGSAM samDesired,
        DWORD Flags,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "samDesired", "Flags", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenClassRegKeyExA(jitter):
    setupapi_SetupDiOpenClassRegKeyEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiOpenClassRegKeyExW(jitter):
    setupapi_SetupDiOpenClassRegKeyEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiOpenDeviceInfo(jitter, get_str, set_str):
    """
    BOOL SetupDiOpenDeviceInfo(
        HDEVINFO DeviceInfoSet,
        PCTSTR DeviceInstanceId,
        HWND hwndParent,
        [OpenDeviceInfoFlags] OpenFlags,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInstanceId", "hwndParent", "OpenFlags", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenDeviceInfoA(jitter):
    setupapi_SetupDiOpenDeviceInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiOpenDeviceInfoW(jitter):
    setupapi_SetupDiOpenDeviceInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiOpenDeviceInterface(jitter, get_str, set_str):
    """
    BOOL SetupDiOpenDeviceInterface(
        HDEVINFO DeviceInfoSet,
        PCTSTR DevicePath,
        [OpenDeviceInterfaceFlags] OpenFlags,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DevicePath", "OpenFlags", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenDeviceInterfaceA(jitter):
    setupapi_SetupDiOpenDeviceInterface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiOpenDeviceInterfaceW(jitter):
    setupapi_SetupDiOpenDeviceInterface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiOpenDeviceInterfaceRegKey(jitter):
    """
    HKEY SetupDiOpenDeviceInterfaceRegKey(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        DWORD Reserved,
        REGSAM samDesired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "Reserved", "samDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenDevRegKey(jitter):
    """
    HKEY SetupDiOpenDevRegKey(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        [DeviceInfoScope] Scope,
        DWORD HwProfile,
        [DeviceInfoKeyType] KeyType,
        REGSAM samDesired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Scope", "HwProfile", "KeyType", "samDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRegisterCoDeviceInstallers(jitter):
    """
    BOOL SetupDiRegisterCoDeviceInstallers(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRegisterDeviceInfo(jitter):
    """
    BOOL SetupDiRegisterDeviceInfo(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        DWORD Flags,
        PSP_DETSIG_CMPPROC CompareProc,
        PVOID CompareContext,
        PSP_DEVINFO_DATA DupDeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Flags", "CompareProc", "CompareContext", "DupDeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRemoveDevice(jitter):
    """
    BOOL SetupDiRemoveDevice(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRemoveDeviceInterface(jitter):
    """
    BOOL SetupDiRemoveDeviceInterface(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRestartDevices(jitter):
    """
    BOOL SetupDiRestartDevices(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSelectBestCompatDrv(jitter):
    """
    BOOL SetupDiSelectBestCompatDrv(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSelectDevice(jitter):
    """
    BOOL SetupDiSelectDevice(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSelectOEMDrv(jitter):
    """
    BOOL SetupDiSelectOEMDrv(
        HWND hwndParent,
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassInstallParams(jitter, get_str, set_str):
    """
    BOOL SetupDiSetClassInstallParams(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_CLASSINSTALL_HEADER ClassInstallParams,
        DWORD ClassInstallParamsSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "ClassInstallParams", "ClassInstallParamsSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassInstallParamsA(jitter):
    setupapi_SetupDiSetClassInstallParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiSetClassInstallParamsW(jitter):
    setupapi_SetupDiSetClassInstallParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiSetClassPropertyW(jitter):
    """
    BOOL SetupDiSetClassPropertyW(
        CONST GUID* ClassGuid,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        [DiClassPropertyFlags] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassPropertyExW(jitter):
    """
    BOOL SetupDiSetClassPropertyExW(
        CONST GUID* ClassGuid,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        DWORD Flags,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassRegistryProperty(jitter, get_str, set_str):
    """
    BOOL SetupDiSetClassRegistryProperty(
        LPGUID ClassGuid,
        DWORD Property,
        CONST BYTE* PropertyBuffer,
        DWORD PropertyBufferSize,
        PCTSTR MachineName,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Property", "PropertyBuffer", "PropertyBufferSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassRegistryPropertyA(jitter):
    setupapi_SetupDiSetClassRegistryProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiSetClassRegistryPropertyW(jitter):
    setupapi_SetupDiSetClassRegistryProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiSetDeviceInstallParams(jitter, get_str, set_str):
    """
    BOOL SetupDiSetDeviceInstallParams(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_DEVINSTALL_PARAMS DeviceInstallParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DeviceInstallParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDeviceInstallParamsA(jitter):
    setupapi_SetupDiSetDeviceInstallParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiSetDeviceInstallParamsW(jitter):
    setupapi_SetupDiSetDeviceInstallParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiSetDeviceInterfaceDefault(jitter):
    """
    BOOL SetupDiSetDeviceInterfaceDefault(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        DWORD Flags,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDeviceInterfacePropertyW(jitter):
    """
    BOOL SetupDiSetDeviceInterfacePropertyW(
        HDEVINFO DeviceInfoSet,
        PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDevicePropertyW(jitter):
    """
    BOOL SetupDiSetDevicePropertyW(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        CONST DEVPROPKEY* PropertyKey,
        DEVPROPTYPE PropertyType,
        CONST PBYTE PropertyBuffer,
        DWORD PropertyBufferSize,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDeviceRegistryProperty(jitter, get_str, set_str):
    """
    BOOL SetupDiSetDeviceRegistryProperty(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        [SetupDeviceRegistryProperty] Property,
        CONST BYTE* PropertyBuffer,
        DWORD PropertyBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Property", "PropertyBuffer", "PropertyBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDeviceRegistryPropertyA(jitter):
    setupapi_SetupDiSetDeviceRegistryProperty(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiSetDeviceRegistryPropertyW(jitter):
    setupapi_SetupDiSetDeviceRegistryProperty(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiSetDriverInstallParams(jitter, get_str, set_str):
    """
    BOOL SetupDiSetDriverInstallParams(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_DRVINFO_DATA DriverInfoData,
        PSP_DRVINSTALL_PARAMS DriverInstallParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData", "DriverInstallParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDriverInstallParamsA(jitter):
    setupapi_SetupDiSetDriverInstallParams(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiSetDriverInstallParamsW(jitter):
    setupapi_SetupDiSetDriverInstallParams(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiSetSelectedDevice(jitter):
    """
    BOOL SetupDiSetSelectedDevice(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetSelectedDriver(jitter, get_str, set_str):
    """
    BOOL SetupDiSetSelectedDriver(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData,
        PSP_DRVINFO_DATA DriverInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetSelectedDriverA(jitter):
    setupapi_SetupDiSetSelectedDriver(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def setupapi_SetupDiSetSelectedDriverW(jitter):
    setupapi_SetupDiSetSelectedDriver(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def setupapi_SetupDiUnremoveDevice(jitter):
    """
    BOOL SetupDiUnremoveDevice(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiMoveDuplicateDevice(jitter):
    """
    BOOL SetupDiMoveDuplicateDevice(
        HDEVINFO DeviceInfoSet,
        PSP_DEVINFO_DATA DeviceInfoData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetThreadLogToken(jitter):
    """
    SP_LOG_TOKEN SetupGetThreadLogToken()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetThreadLogToken(jitter):
    """
    VOID SetupSetThreadLogToken(
        SP_LOG_TOKEN LogToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupWriteTextLog(jitter):
    """
    VOID SetupWriteTextLog(
        SP_LOG_TOKEN LogToken,
        DWORD Category,
        DWORD Flags,
        PCTSTR MessageStr,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogToken", "Category", "Flags", "MessageStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupWriteTextLogError(jitter):
    """
    VOID SetupWriteTextLogError(
        SP_LOG_TOKEN LogToken,
        DWORD Category,
        DWORD LogFlags,
        DWORD Error,
        PCSTR MessageStr,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogToken", "Category", "LogFlags", "Error", "MessageStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupWriteTextLogInfLine(jitter):
    """
    VOID SetupWriteTextLogInfLine(
        SP_LOG_TOKEN LogToken,
        DWORD Flags,
        HINF InfHandle,
        PINFCONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogToken", "Flags", "InfHandle", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
