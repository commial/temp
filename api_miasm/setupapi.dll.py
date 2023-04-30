
def setupapi_InstallHinfSection(jitter):
    """"
    [SetupAPI.dll] VOID InstallHinfSection(HWND hwnd, HINSTANCE ModuleHandle, PCTSTR CmdLineBuffer, INT nCmdShow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "ModuleHandle", "CmdLineBuffer", "nCmdShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAddInstallSectionToDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupAddInstallSectionToDiskSpaceList(HDSKSPC DiskSpace, HINF InfHandle, HINF LayoutInfHandle, PCTSTR SectionName, PVOID Reserved1, UINT Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "InfHandle", "LayoutInfHandle", "SectionName", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAddSectionToDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupAddSectionToDiskSpaceList(HDSKSPC DiskSpace, HINF InfHandle, HINF ListInfHandle, PCTSTR SectionName, UINT Operation, PVOID Reserved1, UINT Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "InfHandle", "ListInfHandle", "SectionName", "Operation", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAddToDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupAddToDiskSpaceList(HDSKSPC DiskSpace, PCTSTR TargetFilespec, LONGLONG FileSize, UINT Operation, PVOID Reserved1, UINT Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "TargetFilespec", "FileSize", "Operation", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAddToSourceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupAddToSourceList(DWORD Flags, PCTSTR Source)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupAdjustDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupAdjustDiskSpaceList(HDSKSPC DiskSpace, LPCTSTR DriveRoot, LONGLONG Amount, PVOID Reserved1, UINT Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "DriveRoot", "Amount", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupBackupError(jitter):
    """"
    [SetupAPI.dll] UINT SetupBackupError(HWND hwndParent, PCTSTR DialogTitle, PCTSTR SourceFile, PCTSTR TargetFile, UINT Win32ErrorCode, DWORD Style)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "SourceFile", "TargetFile", "Win32ErrorCode", "Style"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCancelTemporarySourceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupCancelTemporarySourceList()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCloseFileQueue(jitter):
    """"
    [SetupAPI.dll] BOOL SetupCloseFileQueue(HSPFILEQ QueueHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCloseInfFile(jitter):
    """"
    [SetupAPI.dll] VOID SetupCloseInfFile(HINF InfHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCommitFileQueue(jitter):
    """"
    [SetupAPI.dll] BOOL SetupCommitFileQueue(HWND Owner, HSPFILEQ QueueHandle, PSP_FILE_CALLBACK MsgHandler, PVOID Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Owner", "QueueHandle", "MsgHandler", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupConfigureWmiFromInfSection(jitter):
    """"
    [SetupAPI.dll] BOOL SetupConfigureWmiFromInfSection(HINF InfHandle, PCWSTR SectionName, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "SectionName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCopyError(jitter):
    """"
    [SetupAPI.dll] UINT SetupCopyError(HWND hwndParent, PCTSTR DialogTitle, PCTSTR DiskName, PCTSTR PathToSource, PCTSTR SourceFile, PCTSTR TargetPathFile, UINT Win32ErrorCode, DWORD Style, PTSTR PathBuffer, DWORD PathBufferSize, PDWORD PathRequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "DiskName", "PathToSource", "SourceFile", "TargetPathFile", "Win32ErrorCode", "Style", "PathBuffer", "PathBufferSize", "PathRequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCopyOEMInf(jitter):
    """"
    [SetupAPI.dll] BOOL SetupCopyOEMInf(PCTSTR SourceInfFileName, PCTSTR OEMSourceMediaLocation, DWORD OEMSourceMediaType, DWORD CopyStyle, PTSTR DestinationInfFileName, DWORD DestinationInfFileNameSize, PDWORD RequiredSize, PTSTR DestinationInfFileNameComponent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SourceInfFileName", "OEMSourceMediaLocation", "OEMSourceMediaType", "CopyStyle", "DestinationInfFileName", "DestinationInfFileNameSize", "RequiredSize", "DestinationInfFileNameComponent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCreateDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] HDSKSPC SetupCreateDiskSpaceList(PVOID Reserved1, DWORD Reserved2, [SPDSL_FLAGS] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Reserved1", "Reserved2", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDecompressOrCopyFile(jitter):
    """"
    [SetupAPI.dll] [ERROR_CODE] SetupDecompressOrCopyFile(PCTSTR SourceFileName, PCTSTR TargetFileName, PUINT CompressionType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SourceFileName", "TargetFileName", "CompressionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDefaultQueueCallback(jitter):
    """"
    [SetupAPI.dll] UINT SetupDefaultQueueCallback(PVOID Context, UINT Notification, UINT Param1, UINT Param2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "Notification", "Param1", "Param2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDeleteError(jitter):
    """"
    [SetupAPI.dll] UINT SetupDeleteError(HWND hwndParent, PCTSTR DialogTitle, PCTSTR File, UINT Win32ErrorCode, DWORD Style)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "File", "Win32ErrorCode", "Style"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDestroyDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDestroyDiskSpaceList(HDSKSPC DiskSpace)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDuplicateDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] HDSKSPC SetupDuplicateDiskSpaceList(HDSKSPC DiskSpace, PVOID Reserved1, DWORD Reserved2, UINT Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "Reserved1", "Reserved2", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupEnumInfSections(jitter):
    """"
    [SetupAPI.dll] BOOL SetupEnumInfSections(HINF InfHandle, UINT EnumerationIndex, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "EnumerationIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupFindFirstLine(jitter):
    """"
    [SetupAPI.dll] BOOL SetupFindFirstLine(HINF InfHandle, PCTSTR Section, PCTSTR Key, PINFCONTEXT Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Section", "Key", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupFindNextLine(jitter):
    """"
    [SetupAPI.dll] BOOL SetupFindNextLine(PINFCONTEXT ContextIn, PINFCONTEXT ContextOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextIn", "ContextOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupFindNextMatchLine(jitter):
    """"
    [SetupAPI.dll] BOOL SetupFindNextMatchLine(PINFCONTEXT ContextIn, PCTSTR Key, PINFCONTEXT ContextOut)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextIn", "Key", "ContextOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupFreeSourceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupFreeSourceList(PCTSTR** List, UINT Count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["List", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetBinaryField(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetBinaryField(PINFCONTEXT Context, DWORD FieldIndex, BYTE* ReturnBuffer, DWORD ReturnBufferSize, LPDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "FieldIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFieldCount(jitter):
    """"
    [SetupAPI.dll] DWORD SetupGetFieldCount(PINFCONTEXT Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFileCompressionInfo(jitter):
    """"
    [SetupAPI.dll] [ERROR_CODE] SetupGetFileCompressionInfo(PCTSTR SourceFileName, PTSTR* ActualSourceFileName, PDWORD SourceFileSize, PDWORD TargetFileSize, PUINT CompressionType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SourceFileName", "ActualSourceFileName", "SourceFileSize", "TargetFileSize", "CompressionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFileCompressionInfoEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetFileCompressionInfoEx(PCTSTR SourceFileName, PTSTR ActualSourceFileNameBuffer, DWORD ActualSourceFileNameLen, PDWORD RequiredBufferLen, PDWORD SourceFileSize, PDWORD TargetFileSize, PUINT CompressionType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["SourceFileName", "ActualSourceFileNameBuffer", "ActualSourceFileNameLen", "RequiredBufferLen", "SourceFileSize", "TargetFileSize", "CompressionType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFileQueueCount(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetFileQueueCount(HSPFILEQ FileQueue, UINT SubQueueFileOp, PUINT NumOperations)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "SubQueueFileOp", "NumOperations"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetFileQueueFlags(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetFileQueueFlags(HSPFILEQ FileQueue, PDWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfFileList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetInfFileList(PCTSTR DirectoryPath, [InfStyle] InfStyle, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DirectoryPath", "InfStyle", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfInformation(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetInfInformation(LPCVOID InfSpec, DWORD SearchControl, PSP_INF_INFORMATION ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfSpec", "SearchControl", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetIntField(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetIntField(PINFCONTEXT Context, DWORD FieldIndex, PINT IntegerValue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "FieldIndex", "IntegerValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetLineByIndex(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetLineByIndex(HINF InfHandle, PCTSTR Section, DWORD Index, PINFCONTEXT Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Section", "Index", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetLineCount(jitter):
    """"
    [SetupAPI.dll] LONG SetupGetLineCount(HINF InfHandle, PCTSTR Section)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Section"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetLineText(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetLineText(PINFCONTEXT Context, HINF InfHandle, PCTSTR Section, PCTSTR Key, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "InfHandle", "Section", "Key", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetMultiSzField(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetMultiSzField(PINFCONTEXT Context, DWORD FieldIndex, PTSTR ReturnBuffer, DWORD ReturnBufferSize, LPDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "FieldIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetSourceFileLocation(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetSourceFileLocation(HINF InfHandle, PINFCONTEXT InfContext, PCTSTR FileName, PUINT SourceId, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "FileName", "SourceId", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetSourceFileSize(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetSourceFileSize(HINF InfHandle, PINFCONTEXT InfContext, PCTSTR FileName, PCTSTR Section, PDWORD FileSize, UINT RoundingFactor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "FileName", "Section", "FileSize", "RoundingFactor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetSourceInfo(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetSourceInfo(HINF InfHandle, UINT SourceId, UINT InfoDesired, PTSTR ReturnBuffer, DWORD ReturnBufferSize, LPDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "SourceId", "InfoDesired", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetStringField(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetStringField(PINFCONTEXT Context, DWORD FieldIndex, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "FieldIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetTargetPath(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetTargetPath(HINF InfHandle, PINFCONTEXT InfContext, PCTSTR Section, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "Section", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInitDefaultQueueCallback(jitter):
    """"
    [SetupAPI.dll] PVOID SetupInitDefaultQueueCallback(HWND OwnerWindow)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OwnerWindow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInitDefaultQueueCallbackEx(jitter):
    """"
    [SetupAPI.dll] PVOID SetupInitDefaultQueueCallbackEx(HWND OwnerWindow, HWND AlternateProgressWindow, UINT ProgressMessage, DWORD Reserved1, PVOID Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["OwnerWindow", "AlternateProgressWindow", "ProgressMessage", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInitializeFileLog(jitter):
    """"
    [SetupAPI.dll] HSPFILELOG SetupInitializeFileLog(PCTSTR LogFileName, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogFileName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallFile(jitter):
    """"
    [SetupAPI.dll] BOOL SetupInstallFile(HINF InfHandle, PINFCONTEXT InfContext, PCTSTR SourceFile, PCTSTR SourcePathRoot, PCTSTR DestinationName, DWORD CopyStyle, PSP_FILE_CALLBACK CopyMsgHandler, PVOID Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "SourceFile", "SourcePathRoot", "DestinationName", "CopyStyle", "CopyMsgHandler", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallFileEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupInstallFileEx(HINF InfHandle, PINFCONTEXT InfContext, PCTSTR SourceFile, PCTSTR SourcePathRoot, PCTSTR DestinationName, DWORD CopyStyle, PSP_FILE_CALLBACK CopyMsgHandler, PVOID Context, PBOOL FileWasInUse)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfContext", "SourceFile", "SourcePathRoot", "DestinationName", "CopyStyle", "CopyMsgHandler", "Context", "FileWasInUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallFilesFromInfSection(jitter):
    """"
    [SetupAPI.dll] BOOL SetupInstallFilesFromInfSection(HINF InfHandle, HINF LayoutInfHandle, HSPFILEQ FileQueue, PCTSTR SectionName, PCTSTR SourceRootPath, UINT CopyFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "LayoutInfHandle", "FileQueue", "SectionName", "SourceRootPath", "CopyFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallFromInfSection(jitter):
    """"
    [SetupAPI.dll] BOOL SetupInstallFromInfSection(HWND Owner, HINF InfHandle, PCTSTR SectionName, [SPINST_FLAGS] Flags, HKEY RelativeKeyRoot, PCTSTR SourceRootPath, UINT CopyFlags, PSP_FILE_CALLBACK MsgHandler, PVOID Context, HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Owner", "InfHandle", "SectionName", "Flags", "RelativeKeyRoot", "SourceRootPath", "CopyFlags", "MsgHandler", "Context", "DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallServicesFromInfSection(jitter):
    """"
    [SetupAPI.dll] BOOL SetupInstallServicesFromInfSection(HINF InfHandle, PCTSTR SectionName, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "SectionName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupInstallServicesFromInfSectionEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupInstallServicesFromInfSectionEx(HINF InfHandle, PCTSTR SectionName, DWORD Flags, HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PVOID Reserved1, PVOID Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "SectionName", "Flags", "DeviceInfoSet", "DeviceInfoData", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupIterateCabinet(jitter):
    """"
    [SetupAPI.dll] BOOL SetupIterateCabinet(PCTSTR CabinetFile, DWORD Reserved, PSP_FILE_CALLBACK MsgHandler, PVOID Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CabinetFile", "Reserved", "MsgHandler", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupLogFile(jitter):
    """"
    [SetupAPI.dll] BOOL SetupLogFile(HSPFILELOG FileLogHandle, PCTSTR LogSectionName, PCTSTR SourceFileName, PCTSTR TargetFileName, DWORD Checksum, PCTSTR DiskTagfile, PCTSTR DiskDescription, PCTSTR OtherInfo, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileLogHandle", "LogSectionName", "SourceFileName", "TargetFileName", "Checksum", "DiskTagfile", "DiskDescription", "OtherInfo", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupLogError(jitter):
    """"
    [SetupAPI.dll] BOOL SetupLogError(PCTSTR MessageString, LogSeverity Severity)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MessageString", "Severity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenAppendInfFile(jitter):
    """"
    [SetupAPI.dll] BOOL SetupOpenAppendInfFile(PCTSTR FileName, HINF InfHandle, PUINT ErrorLine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "InfHandle", "ErrorLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenFileQueue(jitter):
    """"
    [SetupAPI.dll] HSPFILEQ SetupOpenFileQueue()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenInfFile(jitter):
    """"
    [SetupAPI.dll] HINF SetupOpenInfFile(PCTSTR FileName, PCTSTR InfClass, [InfStyle] InfStyle, PUINT ErrorLine)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "InfClass", "InfStyle", "ErrorLine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenLog(jitter):
    """"
    [SetupAPI.dll] BOOL SetupOpenLog(BOOL Erase)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Erase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupCloseLog(jitter):
    """"
    [SetupAPI.dll] VOID SetupCloseLog()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupOpenMasterInf(jitter):
    """"
    [SetupAPI.dll] HINF SetupOpenMasterInf()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupPromptForDisk(jitter):
    """"
    [SetupAPI.dll] UINT SetupPromptForDisk(HWND hwndParent, PCTSTR DialogTitle, PCTSTR DiskName, PCTSTR PathToSource, PCTSTR FileSought, PCTSTR TagFile, DWORD DiskPromptStyle, PTSTR PathBuffer, DWORD PathBufferSize, PDWORD PathRequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "DiskName", "PathToSource", "FileSought", "TagFile", "DiskPromptStyle", "PathBuffer", "PathBufferSize", "PathRequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupPromptReboot(jitter):
    """"
    [SetupAPI.dll] INT SetupPromptReboot(HSPFILEQ FileQueue, HWND Owner, BOOL ScanOnly)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "Owner", "ScanOnly"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryDrivesInDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueryDrivesInDiskSpaceList(HDSKSPC DiskSpace, PSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryFileLog(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueryFileLog(HSPFILELOG FileLogHandle, PCTSTR LogSectionName, PCTSTR TargetFileName, SetupFileLogInfo DesiredInfo, PTSTR DataOut, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileLogHandle", "LogSectionName", "TargetFileName", "DesiredInfo", "DataOut", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryInfFileInformation(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueryInfFileInformation(PSP_INF_INFORMATION InfInformation, UINT InfIndex, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfInformation", "InfIndex", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryInfOriginalFileInformation(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueryInfOriginalFileInformation(PSP_INF_INFORMATION InfInformation, UINT InfIndex, PSP_ALTPLATFORM_INFO AlternatePlatformInfo, PSP_ORIGINAL_FILE_INFO OriginalFileInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfInformation", "InfIndex", "AlternatePlatformInfo", "OriginalFileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueryInfVersionInformation(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueryInfVersionInformation(PSP_INF_INFORMATION InfInformation, UINT InfIndex, PCTSTR Key, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfInformation", "InfIndex", "Key", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQuerySourceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQuerySourceList(DWORD Flags, PCTSTR** List, PUINT Count)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "List", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQuerySpaceRequiredOnDrive(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQuerySpaceRequiredOnDrive(HDSKSPC DiskSpace, PCTSTR DriveSpec, LONGLONG* SpaceRequired, PVOID Reserved1, UINT Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "DriveSpec", "SpaceRequired", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueCopy(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueueCopy(HSPFILEQ QueueHandle, PCTSTR SourceRootPath, PCTSTR SourcePath, PCTSTR SourceFileName, PCTSTR SourceDescription, PCTSTR SourceTagFile, PCTSTR TargetDirectory, PCTSTR TargetFileName, DWORD CopyStyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "SourceRootPath", "SourcePath", "SourceFileName", "SourceDescription", "SourceTagFile", "TargetDirectory", "TargetFileName", "CopyStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueCopyIndirect(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueueCopyIndirect(PSP_FILE_COPY_PARAMS CopyParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["CopyParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueCopySection(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueueCopySection(HSPFILEQ QueueHandle, PCTSTR SourceRootPath, HINF InfHandle, HINF ListInfHandle, PCTSTR Section, DWORD CopyStyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "SourceRootPath", "InfHandle", "ListInfHandle", "Section", "CopyStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueDefaultCopy(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueueDefaultCopy(HSPFILEQ QueueHandle, HINF InfHandle, PCTSTR SourceRootPath, PCTSTR SourceFileName, PCTSTR TargetFileName, DWORD CopyStyle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "InfHandle", "SourceRootPath", "SourceFileName", "TargetFileName", "CopyStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueDelete(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueueDelete(HSPFILEQ QueueHandle, PCTSTR PathPart1, PCTSTR PathPart2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "PathPart1", "PathPart2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueDeleteSection(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueueDeleteSection(HSPFILEQ QueueHandle, HINF InfHandle, HINF ListInfHandle, PCTSTR Section)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "InfHandle", "ListInfHandle", "Section"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueRename(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueueRename(HSPFILEQ QueueHandle, PCTSTR SourcePath, PCTSTR SourceFileName, PCTSTR TargetPath, PCTSTR TargetFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "SourcePath", "SourceFileName", "TargetPath", "TargetFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupQueueRenameSection(jitter):
    """"
    [SetupAPI.dll] BOOL SetupQueueRenameSection(HSPFILEQ QueueHandle, HINF InfHandle, HINF ListInfHandle, PCTSTR Section)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "InfHandle", "ListInfHandle", "Section"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveFileLogEntry(jitter):
    """"
    [SetupAPI.dll] BOOL SetupRemoveFileLogEntry(HSPFILELOG FileLogHandle, PCTSTR LogSectionName, PCTSTR TargetFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileLogHandle", "LogSectionName", "TargetFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveFromDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupRemoveFromDiskSpaceList(HDSKSPC DiskSpace, PCTSTR TargetFilespec, UINT Operation, PVOID Reserved1, UINT Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "TargetFilespec", "Operation", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveFromSourceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupRemoveFromSourceList(DWORD Flags, PCTSTR Source)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveInstallSectionFromDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupRemoveInstallSectionFromDiskSpaceList(HDSKSPC DiskSpace, HINF InfHandle, HINF LayoutInfHandle, PCTSTR SectionName, PVOID Reserved1, UINT Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "InfHandle", "LayoutInfHandle", "SectionName", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRemoveSectionFromDiskSpaceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupRemoveSectionFromDiskSpaceList(HDSKSPC DiskSpace, HINF InfHandle, HINF ListInfHandle, PCTSTR SectionName, UINT Operation, PVOID Reserved1, UINT Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DiskSpace", "InfHandle", "ListInfHandle", "SectionName", "Operation", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupRenameError(jitter):
    """"
    [SetupAPI.dll] UINT SetupRenameError(HWND hwndParent, PCTSTR DialogTitle, PCTSTR SourceFile, PCTSTR TargetFile, UINT Win32ErrorCode, DWORD Style)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DialogTitle", "SourceFile", "TargetFile", "Win32ErrorCode", "Style"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupScanFileQueue(jitter):
    """"
    [SetupAPI.dll] BOOL SetupScanFileQueue(HSPFILEQ FileQueue, DWORD Flags, HWND Window, PSP_FILE_CALLBACK CallbackRoutine, PVOID CallbackContext, PDWORD Result)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "Flags", "Window", "CallbackRoutine", "CallbackContext", "Result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetDirectoryId(jitter):
    """"
    [SetupAPI.dll] BOOL SetupSetDirectoryId(HINF InfHandle, DWORD Id, PCTSTR Directory)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Id", "Directory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetDirectoryIdEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupSetDirectoryIdEx(HINF InfHandle, DWORD Id, PCTSTR Directory, DWORD Flags, DWORD Reserved1, PVOID Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "Id", "Directory", "Flags", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetFileQueueAlternatePlatform(jitter):
    """"
    [SetupAPI.dll] BOOL SetupSetFileQueueAlternatePlatform(HSPFILEQ QueueHandle, PSP_ALTPLATFORM_INFO AlternatePlatformInfo, PCWSTR AlternateDefaultCatalogFile)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "AlternatePlatformInfo", "AlternateDefaultCatalogFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetFileQueueFlags(jitter):
    """"
    [SetupAPI.dll] BOOL SetupSetFileQueueFlags(HSPFILEQ FileQueue, DWORD FlagMask, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileQueue", "FlagMask", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetPlatformPathOverride(jitter):
    """"
    [SetupAPI.dll] BOOL SetupSetPlatformPathOverride(PCTSTR Override)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Override"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetSourceList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupSetSourceList(DWORD Flags, PCTSTR* SourceList, UINT SourceCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "SourceList", "SourceCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupTermDefaultQueueCallback(jitter):
    """"
    [SetupAPI.dll] VOID SetupTermDefaultQueueCallback(PVOID Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupTerminateFileLog(jitter):
    """"
    [SetupAPI.dll] BOOL SetupTerminateFileLog(HSPFILELOG FileLogHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileLogHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupUninstallNewlyCopiedInfs(jitter):
    """"
    [SetupAPI.dll] BOOL SetupUninstallNewlyCopiedInfs(HSPFILEQ QueueHandle, DWORD Flags, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["QueueHandle", "Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupUninstallOEMInf(jitter):
    """"
    [SetupAPI.dll] BOOL SetupUninstallOEMInf(PCWSTR InfFileName, DWORD Flags, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfFileName", "Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupVerifyInfFile(jitter):
    """"
    [SetupAPI.dll] BOOL SetupVerifyInfFile(PCWSTR InfName, PSP_ALTPLATFORM_INFO AltPlatformInfo, PSP_INF_SIGNER_INFO InfFileName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfName", "AltPlatformInfo", "InfFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfDriverStoreLocation(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetInfDriverStoreLocation(PCTSTR FileName, PSP_ALTPLATFORM_INFO AlternatePlatformInfo, PCTSTR LocaleName, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["FileName", "AlternatePlatformInfo", "LocaleName", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetInfPublishedName(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetInfPublishedName(PCTSTR DriverStoreLocation, PTSTR ReturnBuffer, DWORD ReturnBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DriverStoreLocation", "ReturnBuffer", "ReturnBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetNonInteractiveMode(jitter):
    """"
    [SetupAPI.dll] BOOL SetupGetNonInteractiveMode()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetNonInteractiveMode(jitter):
    """"
    [SetupAPI.dll] BOOL SetupSetNonInteractiveMode(BOOL NonInteractiveFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NonInteractiveFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiAskForOEMDisk(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiAskForOEMDisk(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiBuildClassInfoList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiBuildClassInfoList([SetupDiBuildClassInfoListFlags] Flags, LPGUID ClassGuidList, DWORD ClassGuidListSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "ClassGuidList", "ClassGuidListSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiBuildClassInfoListEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiBuildClassInfoListEx([SetupDiBuildClassInfoListFlags] Flags, LPGUID ClassGuidList, DWORD ClassGuidListSize, PDWORD RequiredSize, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "ClassGuidList", "ClassGuidListSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiBuildDriverInfoList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiBuildDriverInfoList(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, [DiDriverType] DriverType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCallClassInstaller(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiCallClassInstaller(DI_FUNCTION InstallFunction, HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InstallFunction", "DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCancelDriverInfoSearch(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiCancelDriverInfoSearch(HDEVINFO DeviceInfoSet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiChangeState(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiChangeState(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassGuidsFromName(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiClassGuidsFromName(PCTSTR ClassName, LPGUID ClassGuidList, DWORD ClassGuidListSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassName", "ClassGuidList", "ClassGuidListSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassGuidsFromNameEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiClassGuidsFromNameEx(PCTSTR ClassName, LPGUID ClassGuidList, DWORD ClassGuidListSize, PDWORD RequiredSize, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassName", "ClassGuidList", "ClassGuidListSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassNameFromGuid(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiClassNameFromGuid(LPGUID ClassGuid, PTSTR ClassName, DWORD ClassNameSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ClassName", "ClassNameSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiClassNameFromGuidEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiClassNameFromGuidEx(LPGUID ClassGuid, PTSTR ClassName, DWORD ClassNameSize, PDWORD RequiredSize, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ClassName", "ClassNameSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInfo(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiCreateDeviceInfo(HDEVINFO DeviceInfoSet, PCTSTR DeviceName, LPGUID ClassGuid, PCTSTR DeviceDescription, HWND hwndParent, [SetupDiCreateDeviceInfoFlags] CreationFlags, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceName", "ClassGuid", "DeviceDescription", "hwndParent", "CreationFlags", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInfoList(jitter):
    """"
    [SetupAPI.dll] HDEVINFO SetupDiCreateDeviceInfoList(LPGUID ClassGuid, HWND hwndParent)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "hwndParent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInfoListEx(jitter):
    """"
    [SetupAPI.dll] HDEVINFO SetupDiCreateDeviceInfoListEx(LPGUID ClassGuid, HWND hwndParent, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "hwndParent", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInterface(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiCreateDeviceInterface(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, LPGUID InterfaceClassGuid, PCTSTR ReferenceString, DWORD CreationFlags, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "InterfaceClassGuid", "ReferenceString", "CreationFlags", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDeviceInterfaceRegKey(jitter):
    """"
    [SetupAPI.dll] HKEY SetupDiCreateDeviceInterfaceRegKey(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, DWORD Reserved, REGSAM samDesired, HINF InfHandle, PCTSTR InfSectionName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "Reserved", "samDesired", "InfHandle", "InfSectionName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiCreateDevRegKey(jitter):
    """"
    [SetupAPI.dll] HKEY SetupDiCreateDevRegKey(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, [DeviceInfoScope] Scope, DWORD HwProfile, [DeviceInfoKeyType] KeyType, HINF InfHandle, PCTSTR InfSectionName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Scope", "HwProfile", "KeyType", "InfHandle", "InfSectionName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDeleteDeviceInfo(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiDeleteDeviceInfo(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDeleteDeviceInterfaceData(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiDeleteDeviceInterfaceData(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDeleteDeviceInterfaceRegKey(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiDeleteDeviceInterfaceRegKey(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, DWORD Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDeleteDevRegKey(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiDeleteDevRegKey(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, [DeviceInfoScope] Scope, DWORD HwProfile, [DeviceInfoKeyType] KeyType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Scope", "HwProfile", "KeyType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDestroyClassImageList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiDestroyClassImageList(PSP_CLASSIMAGELIST_DATA ClassImageListData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassImageListData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDestroyDeviceInfoList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiDestroyDeviceInfoList(HDEVINFO DeviceInfoSet)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDestroyDriverInfoList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiDestroyDriverInfoList(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, [DiDriverType] DriverType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiDrawMiniIcon(jitter):
    """"
    [SetupAPI.dll] INT SetupDiDrawMiniIcon(HDC hdc, RECT rc, INT MiniIconIndex, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hdc", "rc", "MiniIconIndex", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiEnumDeviceInfo(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiEnumDeviceInfo(HDEVINFO DeviceInfoSet, DWORD MemberIndex, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "MemberIndex", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiEnumDeviceInterfaces(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiEnumDeviceInterfaces(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, LPGUID InterfaceClassGuid, DWORD MemberIndex, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "InterfaceClassGuid", "MemberIndex", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiEnumDriverInfo(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiEnumDriverInfo(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, [DiDriverType] DriverType, DWORD MemberIndex, PSP_DRVINFO_DATA DriverInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverType", "MemberIndex", "DriverInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiFinishInstallAction(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiFinishInstallAction(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetActualModelsSection(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetActualModelsSection(PINFCONTEXT Context, PSP_ALTPLATFORM_INFO AlternatePlatformInfo, PTSTR DecoratedModelsSection, DWORD DecoratedModelsSectionSize, PDWORD RequiredSize, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Context", "AlternatePlatformInfo", "DecoratedModelsSection", "DecoratedModelsSectionSize", "RequiredSize", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetActualSectionToInstall(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetActualSectionToInstall(HINF InfHandle, PCTSTR InfSectionName, PTSTR InfSectionWithExt, DWORD InfSectionWithExtSize, PDWORD RequiredSize, PTSTR* Extension)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfSectionName", "InfSectionWithExt", "InfSectionWithExtSize", "RequiredSize", "Extension"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetActualSectionToInstallEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetActualSectionToInstallEx(HINF InfHandle, PCTSTR InfSectionName, PSP_ALTPLATFORM_INFO AlternatePlatformInfo, PTSTR InfSectionWithExt, DWORD InfSectionWithExtSize, PDWORD RequiredSize, PTSTR* Extension, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfHandle", "InfSectionName", "AlternatePlatformInfo", "InfSectionWithExt", "InfSectionWithExtSize", "RequiredSize", "Extension", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassBitmapIndex(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassBitmapIndex(LPGUID ClassGuid, PINT MiniIconIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "MiniIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDescription(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassDescription(LPGUID ClassGuid, PTSTR ClassDescription, DWORD ClassDescriptionSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ClassDescription", "ClassDescriptionSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDescriptionEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassDescriptionEx(LPGUID ClassGuid, PTSTR ClassDescription, DWORD ClassDescriptionSize, PDWORD RequiredSize, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "ClassDescription", "ClassDescriptionSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDevPropertySheets(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassDevPropertySheets(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, LPPROPSHEETHEADER PropertySheetHeader, DWORD PropertySheetHeaderPageListSize, PDWORD RequiredSize, [DiGetClassDevPropertySheetsType] PropertySheetType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "PropertySheetHeader", "PropertySheetHeaderPageListSize", "RequiredSize", "PropertySheetType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDevs(jitter):
    """"
    [SetupAPI.dll] HDEVINFO SetupDiGetClassDevs(LPGUID ClassGuid, PCTSTR Enumerator, HWND hwndParent, [DeviceInfoGetFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Enumerator", "hwndParent", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassDevsEx(jitter):
    """"
    [SetupAPI.dll] HDEVINFO SetupDiGetClassDevsEx(LPGUID ClassGuid, PCTSTR Enumerator, HWND hwndParent, [DeviceInfoGetFlags] Flags, HDEVINFO DeviceInfoSet, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Enumerator", "hwndParent", "Flags", "DeviceInfoSet", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassImageIndex(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassImageIndex(PSP_CLASSIMAGELIST_DATA ClassImageListData, LPGUID ClassGuid, PINT ImageIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassImageListData", "ClassGuid", "ImageIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassImageList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassImageList(PSP_CLASSIMAGELIST_DATA ClassImageListData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassImageListData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassImageListEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassImageListEx(PSP_CLASSIMAGELIST_DATA ClassImageListData, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassImageListData", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassInstallParams(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassInstallParams(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_CLASSINSTALL_HEADER ClassInstallParams, DWORD ClassInstallParamsSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "ClassInstallParams", "ClassInstallParamsSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassPropertyW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassPropertyW(CONST GUID* ClassGuid, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, DWORD PropertyBufferSize, PDWORD RequiredSize, [DiClassPropertyFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassPropertyExW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassPropertyExW(CONST GUID* ClassGuid, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, DWORD PropertyBufferSize, PDWORD RequiredSize, [DiClassPropertyFlags] Flags, PCWSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "Flags", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassPropertyKeys(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassPropertyKeys(CONST GUID* ClassGuid, DEVPROPKEY* PropertyKeyArray, DWORD PropertyKeyCount, PDWORD RequiredPropertyKeyCount, [DiClassPropertyFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKeyArray", "PropertyKeyCount", "RequiredPropertyKeyCount", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassPropertyKeysExW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassPropertyKeysExW(CONST GUID* ClassGuid, DEVPROPKEY* PropertyKeyArray, DWORD PropertyKeyCount, PDWORD RequiredPropertyKeyCount, [DiClassPropertyFlags] Flags, PCWSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKeyArray", "PropertyKeyCount", "RequiredPropertyKeyCount", "Flags", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetClassRegistryProperty(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetClassRegistryProperty(LPGUID ClassGuid, DWORD Property, [RegType*] PropertyRegDataType, PBYTE PropertyBuffer, DWORD PropertyBufferSize, PDWORD RequiredSize, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Property", "PropertyRegDataType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetCustomDeviceProperty(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetCustomDeviceProperty(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PCTSTR CustomPropertyName, [GetCustomDevicePropertyFlags] Flags, [RegType*] PropertyRegDataType, PBYTE PropertyBuffer, DWORD PropertyBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "CustomPropertyName", "Flags", "PropertyRegDataType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInfoListClass(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceInfoListClass(HDEVINFO DeviceInfoSet, LPGUID ClassGuid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "ClassGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInfoListDetail(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceInfoListDetail(HDEVINFO DeviceInfoSet, PSP_DEVINFO_LIST_DETAIL_DATA DeviceInfoSetDetailData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoSetDetailData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInstallParams(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceInstallParams(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_DEVINSTALL_PARAMS DeviceInstallParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DeviceInstallParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInstanceId(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceInstanceId(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PTSTR DeviceInstanceId, DWORD DeviceInstanceIdSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DeviceInstanceId", "DeviceInstanceIdSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInterfaceAlias(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceInterfaceAlias(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, LPGUID AliasInterfaceClassGuid, PSP_DEVICE_INTERFACE_DATA AliasDeviceInterfaceData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "AliasInterfaceClassGuid", "AliasDeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInterfaceDetail(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceInterfaceDetail(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, PSP_DEVICE_INTERFACE_DETAIL_DATA DeviceInterfaceDetailData, DWORD DeviceInterfaceDetailDataSize, PDWORD RequiredSize, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "DeviceInterfaceDetailData", "DeviceInterfaceDetailDataSize", "RequiredSize", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInterfacePropertyW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceInterfacePropertyW(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, DWORD PropertyBufferSize, PDWORD RequiredSize, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceInterfacePropertyKeys(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceInterfacePropertyKeys(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, DEVPROPKEY* PropertyKeyArray, DWORD PropertyKeyCount, PDWORD RequiredPropertyKeyCount, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "PropertyKeyArray", "PropertyKeyCount", "RequiredPropertyKeyCount", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDevicePropertyW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDevicePropertyW(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE* PropertyType, PBYTE PropertyBuffer, DWORD PropertyBufferSize, PDWORD RequiredSize, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDevicePropertyKeys(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDevicePropertyKeys(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, DEVPROPKEY* PropertyKeyArray, DWORD PropertyKeyCount, PDWORD RequiredPropertyKeyCount, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "PropertyKeyArray", "PropertyKeyCount", "RequiredPropertyKeyCount", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDeviceRegistryProperty(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDeviceRegistryProperty(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, [SetupDeviceRegistryProperty] Property, [RegType*] PropertyRegDataType, PBYTE PropertyBuffer, DWORD PropertyBufferSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Property", "PropertyRegDataType", "PropertyBuffer", "PropertyBufferSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDriverInfoDetail(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDriverInfoDetail(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_DRVINFO_DATA DriverInfoData, PSP_DRVINFO_DETAIL_DATA DriverInfoDetailData, DWORD DriverInfoDetailDataSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData", "DriverInfoDetailData", "DriverInfoDetailDataSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetDriverInstallParams(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetDriverInstallParams(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_DRVINFO_DATA DriverInfoData, PSP_DRVINSTALL_PARAMS DriverInstallParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData", "DriverInstallParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetHwProfileFriendlyName(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetHwProfileFriendlyName(DWORD HwProfile, PTSTR FriendlyName, DWORD FriendlyNameSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HwProfile", "FriendlyName", "FriendlyNameSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetHwProfileFriendlyNameEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetHwProfileFriendlyNameEx(DWORD HwProfile, PTSTR FriendlyName, DWORD FriendlyNameSize, PDWORD RequiredSize, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HwProfile", "FriendlyName", "FriendlyNameSize", "RequiredSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetHwProfileList(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetHwProfileList(PDWORD HwProfileList, DWORD HwProfileListSize, PDWORD RequiredSize, PDWORD CurrentlyActiveIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HwProfileList", "HwProfileListSize", "RequiredSize", "CurrentlyActiveIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetHwProfileListEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetHwProfileListEx(PDWORD HwProfileList, DWORD HwProfileListSize, PDWORD RequiredSize, PDWORD CurrentlyActiveIndex, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HwProfileList", "HwProfileListSize", "RequiredSize", "CurrentlyActiveIndex", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetINFClass(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetINFClass(PCTSTR InfName, LPGUID ClassGuid, PTSTR ClassName, DWORD ClassNameSize, PDWORD RequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InfName", "ClassGuid", "ClassName", "ClassNameSize", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetSelectedDevice(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetSelectedDevice(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetSelectedDriver(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiGetSelectedDriver(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_DRVINFO_DATA DriverInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiGetWizardPage(jitter):
    """"
    [SetupAPI.dll] HPROPSHEETPAGE SetupDiGetWizardPage(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_INSTALLWIZARD_DATA InstallWizardData, DWORD PageType, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "InstallWizardData", "PageType", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallClass(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiInstallClass(HWND hwndParent, PCTSTR InfFileName, DWORD Flags, HSPFILEQ FileQueue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "InfFileName", "Flags", "FileQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallClassEx(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiInstallClassEx(HWND hwndParent, PCTSTR InfFileName, DWORD Flags, HSPFILEQ FileQueue, LPGUID InterfaceClassGuid, PVOID Reserved1, PVOID Reserved2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "InfFileName", "Flags", "FileQueue", "InterfaceClassGuid", "Reserved1", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallDevice(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiInstallDevice(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallDeviceInterfaces(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiInstallDeviceInterfaces(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiInstallDriverFiles(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiInstallDriverFiles(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiLoadClassIcon(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiLoadClassIcon(LPGUID ClassGuid, HICON* LargeIcon, LPINT MiniIconIndex)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "LargeIcon", "MiniIconIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiLoadDeviceIcon(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiLoadDeviceIcon(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, UINT cxIcon, UINT cyIcon, DWORD Flags, HICON* hIcon)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "cxIcon", "cyIcon", "Flags", "hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenClassRegKey(jitter):
    """"
    [SetupAPI.dll] HKEY SetupDiOpenClassRegKey(LPGUID ClassGuid, REGSAM samDesired)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "samDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenClassRegKeyEx(jitter):
    """"
    [SetupAPI.dll] HKEY SetupDiOpenClassRegKeyEx(LPGUID ClassGuid, REGSAM samDesired, DWORD Flags, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "samDesired", "Flags", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenDeviceInfo(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiOpenDeviceInfo(HDEVINFO DeviceInfoSet, PCTSTR DeviceInstanceId, HWND hwndParent, [OpenDeviceInfoFlags] OpenFlags, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInstanceId", "hwndParent", "OpenFlags", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenDeviceInterface(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiOpenDeviceInterface(HDEVINFO DeviceInfoSet, PCTSTR DevicePath, [OpenDeviceInterfaceFlags] OpenFlags, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DevicePath", "OpenFlags", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenDeviceInterfaceRegKey(jitter):
    """"
    [SetupAPI.dll] HKEY SetupDiOpenDeviceInterfaceRegKey(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, DWORD Reserved, REGSAM samDesired)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "Reserved", "samDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiOpenDevRegKey(jitter):
    """"
    [SetupAPI.dll] HKEY SetupDiOpenDevRegKey(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, [DeviceInfoScope] Scope, DWORD HwProfile, [DeviceInfoKeyType] KeyType, REGSAM samDesired)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Scope", "HwProfile", "KeyType", "samDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRegisterCoDeviceInstallers(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiRegisterCoDeviceInstallers(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRegisterDeviceInfo(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiRegisterDeviceInfo(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, DWORD Flags, PSP_DETSIG_CMPPROC CompareProc, PVOID CompareContext, PSP_DEVINFO_DATA DupDeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Flags", "CompareProc", "CompareContext", "DupDeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRemoveDevice(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiRemoveDevice(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRemoveDeviceInterface(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiRemoveDeviceInterface(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiRestartDevices(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiRestartDevices(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSelectBestCompatDrv(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSelectBestCompatDrv(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSelectDevice(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSelectDevice(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSelectOEMDrv(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSelectOEMDrv(HWND hwndParent, HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassInstallParams(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetClassInstallParams(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_CLASSINSTALL_HEADER ClassInstallParams, DWORD ClassInstallParamsSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "ClassInstallParams", "ClassInstallParamsSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassPropertyW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetClassPropertyW(CONST GUID* ClassGuid, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, DWORD PropertyBufferSize, [DiClassPropertyFlags] Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassPropertyExW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetClassPropertyExW(CONST GUID* ClassGuid, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, DWORD PropertyBufferSize, DWORD Flags, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetClassRegistryProperty(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetClassRegistryProperty(LPGUID ClassGuid, DWORD Property, CONST BYTE* PropertyBuffer, DWORD PropertyBufferSize, PCTSTR MachineName, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClassGuid", "Property", "PropertyBuffer", "PropertyBufferSize", "MachineName", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDeviceInstallParams(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetDeviceInstallParams(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_DEVINSTALL_PARAMS DeviceInstallParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DeviceInstallParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDeviceInterfaceDefault(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetDeviceInterfaceDefault(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, DWORD Flags, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "Flags", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDeviceInterfacePropertyW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetDeviceInterfacePropertyW(HDEVINFO DeviceInfoSet, PSP_DEVICE_INTERFACE_DATA DeviceInterfaceData, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, DWORD PropertyBufferSize, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInterfaceData", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDevicePropertyW(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetDevicePropertyW(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, CONST DEVPROPKEY* PropertyKey, DEVPROPTYPE PropertyType, CONST PBYTE PropertyBuffer, DWORD PropertyBufferSize, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "PropertyKey", "PropertyType", "PropertyBuffer", "PropertyBufferSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDeviceRegistryProperty(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetDeviceRegistryProperty(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, [SetupDeviceRegistryProperty] Property, CONST BYTE* PropertyBuffer, DWORD PropertyBufferSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "Property", "PropertyBuffer", "PropertyBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetDriverInstallParams(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetDriverInstallParams(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_DRVINFO_DATA DriverInfoData, PSP_DRVINSTALL_PARAMS DriverInstallParams)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData", "DriverInstallParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetSelectedDevice(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetSelectedDevice(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiSetSelectedDriver(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiSetSelectedDriver(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_DRVINFO_DATA DriverInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "DriverInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiUnremoveDevice(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiUnremoveDevice(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupDiMoveDuplicateDevice(jitter):
    """"
    [SetupAPI.dll] BOOL SetupDiMoveDuplicateDevice(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupGetThreadLogToken(jitter):
    """"
    [SetupAPI.dll] SP_LOG_TOKEN SetupGetThreadLogToken()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupSetThreadLogToken(jitter):
    """"
    [SetupAPI.dll] VOID SetupSetThreadLogToken(SP_LOG_TOKEN LogToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupWriteTextLog(jitter):
    """"
    [SetupAPI.dll] VOID SetupWriteTextLog(SP_LOG_TOKEN LogToken, DWORD Category, DWORD Flags, PCTSTR MessageStr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogToken", "Category", "Flags", "MessageStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupWriteTextLogError(jitter):
    """"
    [SetupAPI.dll] VOID SetupWriteTextLogError(SP_LOG_TOKEN LogToken, DWORD Category, DWORD LogFlags, DWORD Error, PCSTR MessageStr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogToken", "Category", "LogFlags", "Error", "MessageStr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def setupapi_SetupWriteTextLogInfLine(jitter):
    """"
    [SetupAPI.dll] VOID SetupWriteTextLogInfLine(SP_LOG_TOKEN LogToken, DWORD Flags, HINF InfHandle, PINFCONTEXT Context)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogToken", "Flags", "InfHandle", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
