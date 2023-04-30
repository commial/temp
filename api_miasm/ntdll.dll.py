KPROFILE_SOURCE = {
    "ProfileTime": 0,
    "ProfileAlignmentFixup": 1,
    "ProfileTotalIssues": 2,
    "ProfilePipelineDry": 3,
    "ProfileLoadInstructions": 4,
    "ProfilePipelineFrozen": 5,
    "ProfileBranchInstructions": 6,
    "ProfileTotalNonissues": 7,
    "ProfileDcacheMisses": 8,
    "ProfileIcacheMisses": 9,
    "ProfileCacheMisses": 10,
    "ProfileBranchMispredictions": 11,
    "ProfileStoreInstructions": 12,
    "ProfileFpInstructions": 13,
    "ProfileIntegerInstructions": 14,
    "Profile2Issue": 15,
    "Profile3Issue": 16,
    "Profile4Issue": 17,
    "ProfileSpecialInstructions": 18,
    "ProfileTotalCycles": 19,
    "ProfileIcacheIssues": 20,
    "ProfileDcacheAccesses": 21,
    "ProfileMemoryBarrierCycles": 22,
    "ProfileLoadLinkedIssues": 23,
}
KPROFILE_SOURCE_INV = {
    0: "ProfileTime",
    1: "ProfileAlignmentFixup",
    2: "ProfileTotalIssues",
    3: "ProfilePipelineDry",
    4: "ProfileLoadInstructions",
    5: "ProfilePipelineFrozen",
    6: "ProfileBranchInstructions",
    7: "ProfileTotalNonissues",
    8: "ProfileDcacheMisses",
    9: "ProfileIcacheMisses",
    10: "ProfileCacheMisses",
    11: "ProfileBranchMispredictions",
    12: "ProfileStoreInstructions",
    13: "ProfileFpInstructions",
    14: "ProfileIntegerInstructions",
    15: "Profile2Issue",
    16: "Profile3Issue",
    17: "Profile4Issue",
    18: "ProfileSpecialInstructions",
    19: "ProfileTotalCycles",
    20: "ProfileIcacheIssues",
    21: "ProfileDcacheAccesses",
    22: "ProfileMemoryBarrierCycles",
    23: "ProfileLoadLinkedIssues",
}
_RTL_USER_PROCESS_PARAMETERS_FLAGS_ = {
    "RTL_USER_PROCESS_PARAMETERS_NORMALIZED": 0x01,
    "RTL_USER_PROCESS_PARAMETERS_PROFILE_USER": 0x02,
    "RTL_USER_PROCESS_PARAMETERS_PROFILE_SERVER": 0x04,
    "RTL_USER_PROCESS_PARAMETERS_PROFILE_KERNEL": 0x08,
    "RTL_USER_PROCESS_PARAMETERS_UNKNOWN": 0x10,
    "RTL_USER_PROCESS_PARAMETERS_RESERVE_1MB": 0x20,
    "RTL_USER_PROCESS_PARAMETERS_DISABLE_HEAP_CHECKS": 0x100,
    "RTL_USER_PROCESS_PARAMETERS_PROCESS_OR_1": 0x200,
    "RTL_USER_PROCESS_PARAMETERS_PROCESS_OR_2": 0x400,
    "RTL_USER_PROCESS_PARAMETERS_PRIVATE_DLL_PATH": 0x1000,
    "RTL_USER_PROCESS_PARAMETERS_LOCAL_DLL_PATH": 0x2000,
    "RTL_USER_PROCESS_PARAMETERS_NX": 0x20000,
}
_RTL_USER_PROCESS_PARAMETERS_FLAGS__INV = {
    0x01: "RTL_USER_PROCESS_PARAMETERS_NORMALIZED",
    0x02: "RTL_USER_PROCESS_PARAMETERS_PROFILE_USER",
    0x04: "RTL_USER_PROCESS_PARAMETERS_PROFILE_SERVER",
    0x08: "RTL_USER_PROCESS_PARAMETERS_PROFILE_KERNEL",
    0x10: "RTL_USER_PROCESS_PARAMETERS_UNKNOWN",
    0x20: "RTL_USER_PROCESS_PARAMETERS_RESERVE_1MB",
    0x100: "RTL_USER_PROCESS_PARAMETERS_DISABLE_HEAP_CHECKS",
    0x200: "RTL_USER_PROCESS_PARAMETERS_PROCESS_OR_1",
    0x400: "RTL_USER_PROCESS_PARAMETERS_PROCESS_OR_2",
    0x1000: "RTL_USER_PROCESS_PARAMETERS_PRIVATE_DLL_PATH",
    0x2000: "RTL_USER_PROCESS_PARAMETERS_LOCAL_DLL_PATH",
    0x20000: "RTL_USER_PROCESS_PARAMETERS_NX",
}
RTL_PATH_TYPE = {
    "RtlPathTypeUnknown": 0,
    "RtlPathTypeUncAbsolute": 1,
    "RtlPathTypeDriveAbsolute": 2,
    "RtlPathTypeDriveRelative": 3,
    "RtlPathTypeRooted": 4,
    "RtlPathTypeRelative": 5,
    "RtlPathTypeLocalDevice": 6,
    "RtlPathTypeRootLocalDevice": 7,
}
RTL_PATH_TYPE_INV = {
    0: "RtlPathTypeUnknown",
    1: "RtlPathTypeUncAbsolute",
    2: "RtlPathTypeDriveAbsolute",
    3: "RtlPathTypeDriveRelative",
    4: "RtlPathTypeRooted",
    5: "RtlPathTypeRelative",
    6: "RtlPathTypeLocalDevice",
    7: "RtlPathTypeRootLocalDevice",
}
TABLE_SEARCH_RESULT = {
    "TableEmptyTree": 0,
    "TableFoundNode": 1,
    "TableInsertAsLeft": 2,
    "TableInsertAsRight": 3,
}
TABLE_SEARCH_RESULT_INV = {
    0: "TableEmptyTree",
    1: "TableFoundNode",
    2: "TableInsertAsLeft",
    3: "TableInsertAsRight",
}
NT_PRODUCT_TYPE = {
    "NtProductWinNt": 1,
    "NtProductLanManNt": 2,
    "NtProductServer": 3,
}
NT_PRODUCT_TYPE_INV = {
    1: "NtProductWinNt",
    2: "NtProductLanManNt",
    3: "NtProductServer",
}
KEY_INFORMATION_CLASS = {
    "KeyBasicInformation": 0,
    "KeyNodeInformation": 1,
    "KeyFullInformation": 2,
    "KeyNameInformation": 3,
    "KeyCachedInformation": 4,
    "KeyFlagsInformation": 5,
    "KeyVirtualizationInformation": 6,
    "KeyHandleTagsInformation": 7,
}
KEY_INFORMATION_CLASS_INV = {
    0: "KeyBasicInformation",
    1: "KeyNodeInformation",
    2: "KeyFullInformation",
    3: "KeyNameInformation",
    4: "KeyCachedInformation",
    5: "KeyFlagsInformation",
    6: "KeyVirtualizationInformation",
    7: "KeyHandleTagsInformation",
}
KEY_VALUE_INFORMATION_CLASS = {
    "KeyValueBasicInformation": 0,
    "KeyValueFullInformation": 1,
    "KeyValuePartialInformation": 2,
    "KeyValueFullInformationAlign64": 3,
    "KeyValuePartialInformationAlign64": 4,
}
KEY_VALUE_INFORMATION_CLASS_INV = {
    0: "KeyValueBasicInformation",
    1: "KeyValueFullInformation",
    2: "KeyValuePartialInformation",
    3: "KeyValueFullInformationAlign64",
    4: "KeyValuePartialInformationAlign64",
}
PLUGPLAY_CONTROL_CLASS = {
    "PlugPlayControlEnumerateDevice": 0,
    "PlugPlayControlRegisterNewDevice": 1,
    "PlugPlayControlDeregisterDevice": 2,
    "PlugPlayControlInitializeDevice": 3,
    "PlugPlayControlStartDevice": 4,
    "PlugPlayControlUnlockDevice": 5,
    "PlugPlayControlQueryAndRemoveDevice": 6,
    "PlugPlayControlUserResponse": 7,
    "PlugPlayControlGenerateLegacyDevice": 8,
    "PlugPlayControlGetInterfaceDeviceList": 9,
    "PlugPlayControlProperty": 10,
    "PlugPlayControlDeviceClassAssociation": 11,
    "PlugPlayControlGetRelatedDevice": 12,
    "PlugPlayControlGetInterfaceDeviceAlias": 13,
    "PlugPlayControlDeviceStatus": 14,
    "PlugPlayControlGetDeviceDepth": 15,
    "PlugPlayControlQueryDeviceRelations": 16,
    "PlugPlayControlTargetDeviceRelation": 17,
    "PlugPlayControlQueryConflictList": 18,
    "PlugPlayControlRetrieveDock": 19,
    "PlugPlayControlResetDevice": 20,
    "PlugPlayControlHaltDevice": 21,
    "PlugPlayControlGetBlockedDriverList": 22,
}
PLUGPLAY_CONTROL_CLASS_INV = {
    0: "PlugPlayControlEnumerateDevice",
    1: "PlugPlayControlRegisterNewDevice",
    2: "PlugPlayControlDeregisterDevice",
    3: "PlugPlayControlInitializeDevice",
    4: "PlugPlayControlStartDevice",
    5: "PlugPlayControlUnlockDevice",
    6: "PlugPlayControlQueryAndRemoveDevice",
    7: "PlugPlayControlUserResponse",
    8: "PlugPlayControlGenerateLegacyDevice",
    9: "PlugPlayControlGetInterfaceDeviceList",
    10: "PlugPlayControlProperty",
    11: "PlugPlayControlDeviceClassAssociation",
    12: "PlugPlayControlGetRelatedDevice",
    13: "PlugPlayControlGetInterfaceDeviceAlias",
    14: "PlugPlayControlDeviceStatus",
    15: "PlugPlayControlGetDeviceDepth",
    16: "PlugPlayControlQueryDeviceRelations",
    17: "PlugPlayControlTargetDeviceRelation",
    18: "PlugPlayControlQueryConflictList",
    19: "PlugPlayControlRetrieveDock",
    20: "PlugPlayControlResetDevice",
    21: "PlugPlayControlHaltDevice",
    22: "PlugPlayControlGetBlockedDriverList",
}
KEY_SET_INFORMATION_CLASS = {
    "KeyWriteTimeInformation": 0,
    "KeyWow64FlagsInformation": 1,
    "KeyControlFlagsInformation": 2,
    "KeySetVirtualizationInformation": 3,
    "KeySetDebugInformation": 4,
    "KeySetHandleTagsInformation": 5,
}
KEY_SET_INFORMATION_CLASS_INV = {
    0: "KeyWriteTimeInformation",
    1: "KeyWow64FlagsInformation",
    2: "KeyControlFlagsInformation",
    3: "KeySetVirtualizationInformation",
    4: "KeySetDebugInformation",
    5: "KeySetHandleTagsInformation",
}
DEBUGOBJECTINFOCLASS = {
    "DebugObjectUnusedInformation": 0,
    "DebugObjectKillProcessOnExitInformation": 1,
}
DEBUGOBJECTINFOCLASS_INV = {
    0: "DebugObjectUnusedInformation",
    1: "DebugObjectKillProcessOnExitInformation",
}
TIMER_TYPE = {
    "NotificationTimer": 0,
    "SynchronizationTimer": 1,
}
TIMER_TYPE_INV = {
    0: "NotificationTimer",
    1: "SynchronizationTimer",
}
EVENT_INFORMATION_CLASS = {
    "EventBasicInformation": 0,
}
EVENT_INFORMATION_CLASS_INV = {
    0: "EventBasicInformation",
}
ATOM_INFORMATION_CLASS = {
    "AtomBasicInformation": 0,
    "AtomTableInformation": 1,
}
ATOM_INFORMATION_CLASS_INV = {
    0: "AtomBasicInformation",
    1: "AtomTableInformation",
}
MUTANT_INFORMATION_CLASS = {
    "MutantBasicInformation": 0,
    "MutantOwnerInformation": 1,
}
MUTANT_INFORMATION_CLASS_INV = {
    0: "MutantBasicInformation",
    1: "MutantOwnerInformation",
}
SEMAPHORE_INFORMATION_CLASS = {
    "SemaphoreBasicInformation": 0,
}
SEMAPHORE_INFORMATION_CLASS_INV = {
    0: "SemaphoreBasicInformation",
}
TIMER_INFORMATION_CLASS = {
    "TimerBasicInformation": 0,
}
TIMER_INFORMATION_CLASS_INV = {
    0: "TimerBasicInformation",
}
SHUTDOWN_ACTION = {
    "ShutdownNoReboot": 0,
    "ShutdownReboot": 1,
    "ShutdownPowerOff": 2,
}
SHUTDOWN_ACTION_INV = {
    0: "ShutdownNoReboot",
    1: "ShutdownReboot",
    2: "ShutdownPowerOff",
}
FILE_INFORMATION_CLASS = {
    "FileDirectoryInformation": 1,
    "FileFullDirectoryInformation": 2,
    "FileBothDirectoryInformation": 3,
    "FileBasicInformation": 4,
    "FileStandardInformation": 5,
    "FileInternalInformation": 6,
    "FileEaInformation": 7,
    "FileAccessInformation": 8,
    "FileNameInformation": 9,
    "FileRenameInformation": 10,
    "FileLinkInformation": 11,
    "FileNamesInformation": 12,
    "FileDispositionInformation": 13,
    "FilePositionInformation": 14,
    "FileFullEaInformation": 15,
    "FileModeInformation": 16,
    "FileAlignmentInformation": 17,
    "FileAllInformation": 18,
    "FileAllocationInformation": 19,
    "FileEndOfFileInformation": 20,
    "FileAlternateNameInformation": 21,
    "FileStreamInformation": 22,
    "FilePipeInformation": 23,
    "FilePipeLocalInformation": 24,
    "FilePipeRemoteInformation": 25,
    "FileMailslotQueryInformation": 26,
    "FileMailslotSetInformation": 27,
    "FileCompressionInformation": 28,
    "FileObjectIdInformation": 29,
    "FileCompletionInformation": 30,
    "FileMoveClusterInformation": 31,
    "FileQuotaInformation": 32,
    "FileReparsePointInformation": 33,
    "FileNetworkOpenInformation": 34,
    "FileAttributeTagInformation": 35,
    "FileTrackingInformation": 36,
    "FileIdBothDirectoryInformation": 37,
    "FileIdFullDirectoryInformation": 38,
    "FileValidDataLengthInformation": 39,
    "FileShortNameInformation": 40,
    "FileIoCompletionNotificationInformation": 41,
    "FileIoStatusBlockRangeInformation": 42,
    "FileIoPriorityHintInformation": 43,
    "FileSfioReserveInformation": 44,
    "FileSfioVolumeInformation": 45,
    "FileHardLinkInformation": 46,
    "FileProcessIdsUsingFileInformation": 47,
    "FileNormalizedNameInformation": 48,
    "FileNetworkPhysicalNameInformation": 49,
    "FileIdGlobalTxDirectoryInformation": 50,
    "FileIsRemoteDeviceInformation": 51,
    "FileAttributeCacheInformation": 52,
    "FileNumaNodeInformation": 53,
    "FileStandardLinkInformation": 54,
    "FileRemoteProtocolInformation": 55,
    "FileRenameInformationBypassAccessCheck": 56,
    "FileLinkInformationBypassAccessCheck": 57,
    "FileIntegrityStreamInformation": 58,
    "FileVolumeNameInformation": 59,
}
FILE_INFORMATION_CLASS_INV = {
    1: "FileDirectoryInformation",
    2: "FileFullDirectoryInformation",
    3: "FileBothDirectoryInformation",
    4: "FileBasicInformation",
    5: "FileStandardInformation",
    6: "FileInternalInformation",
    7: "FileEaInformation",
    8: "FileAccessInformation",
    9: "FileNameInformation",
    10: "FileRenameInformation",
    11: "FileLinkInformation",
    12: "FileNamesInformation",
    13: "FileDispositionInformation",
    14: "FilePositionInformation",
    15: "FileFullEaInformation",
    16: "FileModeInformation",
    17: "FileAlignmentInformation",
    18: "FileAllInformation",
    19: "FileAllocationInformation",
    20: "FileEndOfFileInformation",
    21: "FileAlternateNameInformation",
    22: "FileStreamInformation",
    23: "FilePipeInformation",
    24: "FilePipeLocalInformation",
    25: "FilePipeRemoteInformation",
    26: "FileMailslotQueryInformation",
    27: "FileMailslotSetInformation",
    28: "FileCompressionInformation",
    29: "FileObjectIdInformation",
    30: "FileCompletionInformation",
    31: "FileMoveClusterInformation",
    32: "FileQuotaInformation",
    33: "FileReparsePointInformation",
    34: "FileNetworkOpenInformation",
    35: "FileAttributeTagInformation",
    36: "FileTrackingInformation",
    37: "FileIdBothDirectoryInformation",
    38: "FileIdFullDirectoryInformation",
    39: "FileValidDataLengthInformation",
    40: "FileShortNameInformation",
    41: "FileIoCompletionNotificationInformation",
    42: "FileIoStatusBlockRangeInformation",
    43: "FileIoPriorityHintInformation",
    44: "FileSfioReserveInformation",
    45: "FileSfioVolumeInformation",
    46: "FileHardLinkInformation",
    47: "FileProcessIdsUsingFileInformation",
    48: "FileNormalizedNameInformation",
    49: "FileNetworkPhysicalNameInformation",
    50: "FileIdGlobalTxDirectoryInformation",
    51: "FileIsRemoteDeviceInformation",
    52: "FileAttributeCacheInformation",
    53: "FileNumaNodeInformation",
    54: "FileStandardLinkInformation",
    55: "FileRemoteProtocolInformation",
    56: "FileRenameInformationBypassAccessCheck",
    57: "FileLinkInformationBypassAccessCheck",
    58: "FileIntegrityStreamInformation",
    59: "FileVolumeNameInformation",
}
IO_COMPLETION_INFORMATION_CLASS = {
    "IoCompletionBasicInformation": 0,
}
IO_COMPLETION_INFORMATION_CLASS_INV = {
    0: "IoCompletionBasicInformation",
}
FS_INFORMATION_CLASS = {
    "FileFsVolumeInformation": 1,
    "FileFsLabelInformation": 2,
    "FileFsSizeInformation": 3,
    "FileFsDeviceInformation": 4,
    "FileFsAttributeInformation": 5,
    "FileFsControlInformation": 6,
    "FileFsFullSizeInformation": 7,
    "FileFsObjectIdInformation": 8,
    "FileFsDriverPathInformation": 9,
    "FileFsVolumeFlagsInformation": 10,
    "FileFsSectorSizeInformation": 11,
}
FS_INFORMATION_CLASS_INV = {
    1: "FileFsVolumeInformation",
    2: "FileFsLabelInformation",
    3: "FileFsSizeInformation",
    4: "FileFsDeviceInformation",
    5: "FileFsAttributeInformation",
    6: "FileFsControlInformation",
    7: "FileFsFullSizeInformation",
    8: "FileFsObjectIdInformation",
    9: "FileFsDriverPathInformation",
    10: "FileFsVolumeFlagsInformation",
    11: "FileFsSectorSizeInformation",
}
SYSDBG_COMMAND = {
    "SysDbgQueryModuleInformation": 0,
    "SysDbgQueryTraceInformation": 1,
    "SysDbgSetTracepoint": 2,
    "SysDbgSetSpecialCall": 3,
    "SysDbgClearSpecialCalls": 4,
    "SysDbgQuerySpecialCalls": 5,
    "SysDbgBreakPoint": 6,
    "SysDbgQueryVersion": 7,
    "SysDbgReadVirtual": 8,
    "SysDbgWriteVirtual": 9,
    "SysDbgReadPhysical": 10,
    "SysDbgWritePhysical": 11,
    "SysDbgReadControlSpace": 12,
    "SysDbgWriteControlSpace": 13,
    "SysDbgReadIoSpace": 14,
    "SysDbgWriteIoSpace": 15,
    "SysDbgReadMsr": 16,
    "SysDbgWriteMsr": 17,
    "SysDbgReadBusData": 18,
    "SysDbgWriteBusData": 19,
    "SysDbgCheckLowMemory": 20,
    "SysDbgEnableKernelDebugger": 21,
    "SysDbgDisableKernelDebugger": 22,
    "SysDbgGetAutoKdEnable": 23,
    "SysDbgSetAutoKdEnable": 24,
    "SysDbgGetPrintBufferSize": 25,
    "SysDbgSetPrintBufferSize": 26,
    "SysDbgGetKdUmExceptionEnable": 27,
    "SysDbgSetKdUmExceptionEnable": 28,
    "SysDbgGetTriageDump": 29,
    "SysDbgGetKdBlockEnable": 30,
    "SysDbgSetKdBlockEnable": 31,
    "SysDbgRegisterForUmBreakInfo": 32,
    "SysDbgGetUmBreakPid": 33,
    "SysDbgClearUmBreakPid": 34,
    "SysDbgGetUmAttachPid": 35,
    "SysDbgClearUmAttachPid": 36,
}
SYSDBG_COMMAND_INV = {
    0: "SysDbgQueryModuleInformation",
    1: "SysDbgQueryTraceInformation",
    2: "SysDbgSetTracepoint",
    3: "SysDbgSetSpecialCall",
    4: "SysDbgClearSpecialCalls",
    5: "SysDbgQuerySpecialCalls",
    6: "SysDbgBreakPoint",
    7: "SysDbgQueryVersion",
    8: "SysDbgReadVirtual",
    9: "SysDbgWriteVirtual",
    10: "SysDbgReadPhysical",
    11: "SysDbgWritePhysical",
    12: "SysDbgReadControlSpace",
    13: "SysDbgWriteControlSpace",
    14: "SysDbgReadIoSpace",
    15: "SysDbgWriteIoSpace",
    16: "SysDbgReadMsr",
    17: "SysDbgWriteMsr",
    18: "SysDbgReadBusData",
    19: "SysDbgWriteBusData",
    20: "SysDbgCheckLowMemory",
    21: "SysDbgEnableKernelDebugger",
    22: "SysDbgDisableKernelDebugger",
    23: "SysDbgGetAutoKdEnable",
    24: "SysDbgSetAutoKdEnable",
    25: "SysDbgGetPrintBufferSize",
    26: "SysDbgSetPrintBufferSize",
    27: "SysDbgGetKdUmExceptionEnable",
    28: "SysDbgSetKdUmExceptionEnable",
    29: "SysDbgGetTriageDump",
    30: "SysDbgGetKdBlockEnable",
    31: "SysDbgSetKdBlockEnable",
    32: "SysDbgRegisterForUmBreakInfo",
    33: "SysDbgGetUmBreakPid",
    34: "SysDbgClearUmBreakPid",
    35: "SysDbgGetUmAttachPid",
    36: "SysDbgClearUmAttachPid",
}
PORT_INFORMATION_CLASS = {
    "PortBasicInformation": 0,
    "PortDumpInformation": 1,
}
PORT_INFORMATION_CLASS_INV = {
    0: "PortBasicInformation",
    1: "PortDumpInformation",
}
SECTION_INHERIT = {
    "ViewShare": 1,
    "ViewUnmap": 2,
}
SECTION_INHERIT_INV = {
    1: "ViewShare",
    2: "ViewUnmap",
}
SECTION_INFORMATION_CLASS = {
    "SectionBasicInformation": 0,
    "SectionImageInformation": 1,
    "SectionRelocationInformation": 2,
}
SECTION_INFORMATION_CLASS_INV = {
    0: "SectionBasicInformation",
    1: "SectionImageInformation",
    2: "SectionRelocationInformation",
}
MEMORY_INFORMATION_CLASS = {
    "MemoryBasicInformation": 0,
    "MemoryWorkingSetInformation": 1,
    "MemoryMappedFilenameInformation": 2,
    "MemoryRegionInformation": 3,
    "MemoryWorkingSetExInformation": 4,
}
MEMORY_INFORMATION_CLASS_INV = {
    0: "MemoryBasicInformation",
    1: "MemoryWorkingSetInformation",
    2: "MemoryMappedFilenameInformation",
    3: "MemoryRegionInformation",
    4: "MemoryWorkingSetExInformation",
}
OBJECT_INFORMATION_CLASS = {
    "ObjectBasicInformation": 0,
    "ObjectNameInformation": 1,
    "ObjectTypeInformation": 2,
    "ObjectAllTypesInformation": 3,
    "ObjectHandleFlagInformation": 4,
    "ObjectSessionInformation": 5,
}
OBJECT_INFORMATION_CLASS_INV = {
    0: "ObjectBasicInformation",
    1: "ObjectNameInformation",
    2: "ObjectTypeInformation",
    3: "ObjectAllTypesInformation",
    4: "ObjectHandleFlagInformation",
    5: "ObjectSessionInformation",
}
WAIT_TYPE = {
    "WaitAll": 0,
    "WaitAny": 1,
}
WAIT_TYPE_INV = {
    0: "WaitAll",
    1: "WaitAny",
}
APPHELPCACHESERVICECLASS = {
    "ApphelpCacheServiceLookup": 0,
    "ApphelpCacheServiceRemove": 1,
    "ApphelpCacheServiceUpdate": 2,
    "ApphelpCacheServiceFlush": 3,
    "ApphelpCacheServiceDump": 4,
}
APPHELPCACHESERVICECLASS_INV = {
    0: "ApphelpCacheServiceLookup",
    1: "ApphelpCacheServiceRemove",
    2: "ApphelpCacheServiceUpdate",
    3: "ApphelpCacheServiceFlush",
    4: "ApphelpCacheServiceDump",
}
SYSTEM_INFORMATION_CLASS = {
    "SystemBasicInformation": 0,
    "SystemProcessorInformation": 1,
    "SystemPerformanceInformation": 2,
    "SystemTimeOfDayInformation": 3,
    "SystemPathInformation": 4,
    "SystemProcessInformation": 5,
    "SystemCallCountInformation": 6,
    "SystemDeviceInformation": 7,
    "SystemProcessorPerformanceInformation": 8,
    "SystemFlagsInformation": 9,
    "SystemCallTimeInformation": 10,
    "SystemModuleInformation": 11,
    "SystemLocksInformation": 12,
    "SystemStackTraceInformation": 13,
    "SystemPagedPoolInformation": 14,
    "SystemNonPagedPoolInformation": 15,
    "SystemHandleInformation": 16,
    "SystemObjectInformation": 17,
    "SystemPageFileInformation": 18,
    "SystemVdmInstemulInformation": 19,
    "SystemVdmBopInformation": 20,
    "SystemFileCacheInformation": 21,
    "SystemPoolTagInformation": 22,
    "SystemInterruptInformation": 23,
    "SystemDpcBehaviorInformation": 24,
    "SystemFullMemoryInformation": 25,
    "SystemLoadGdiDriverInformation": 26,
    "SystemUnloadGdiDriverInformation": 27,
    "SystemTimeAdjustmentInformation": 28,
    "SystemSummaryMemoryInformation": 29,
    "SystemMirrorMemoryInformation": 30,
    "SystemPerformanceTraceInformation": 31,
    "SystemObsolete0": 32,
    "SystemExceptionInformation": 33,
    "SystemCrashDumpStateInformation": 34,
    "SystemKernelDebuggerInformation": 35,
    "SystemContextSwitchInformation": 36,
    "SystemRegistryQuotaInformation": 37,
    "SystemExtendServiceTableInformation": 38,
    "SystemPrioritySeperation": 39,
    "SystemVerifierAddDriverInformation": 40,
    "SystemVerifierRemoveDriverInformation": 41,
    "SystemProcessorIdleInformation": 42,
    "SystemLegacyDriverInformation": 43,
    "SystemCurrentTimeZoneInformation": 44,
    "SystemLookasideInformation": 45,
    "SystemTimeSlipNotification": 46,
    "SystemSessionCreate": 47,
    "SystemSessionDetach": 48,
    "SystemSessionInformation": 49,
    "SystemRangeStartInformation": 50,
    "SystemVerifierInformation": 51,
    "SystemVerifierThunkExtend": 52,
    "SystemSessionProcessInformation": 53,
    "SystemLoadGdiDriverInSystemSpace": 54,
    "SystemNumaProcessorMap": 55,
    "SystemPrefetcherInformation": 56,
    "SystemExtendedProcessInformation": 57,
    "SystemRecommendedSharedDataAlignment": 58,
    "SystemComPlusPackage": 59,
    "SystemNumaAvailableMemory": 60,
    "SystemProcessorPowerInformation": 61,
    "SystemEmulationBasicInformation": 62,
    "SystemEmulationProcessorInformation": 63,
    "SystemExtendedHandleInformation": 64,
    "SystemLostDelayedWriteInformation": 65,
    "SystemBigPoolInformation": 66,
    "SystemSessionPoolTagInformation": 67,
    "SystemSessionMappedViewInformation": 68,
    "SystemHotpatchInformation": 69,
    "SystemObjectSecurityMode": 70,
    "SystemWatchdogTimerHandler": 71,
    "SystemWatchdogTimerInformation": 72,
    "SystemLogicalProcessorInformation": 73,
    "SystemWow64SharedInformationObsolete": 74,
    "SystemRegisterFirmwareTableInformationHandler": 75,
    "SystemFirmwareTableInformation": 76,
    "SystemModuleInformationEx": 77,
    "SystemVerifierTriageInformation": 78,
    "SystemSuperfetchInformation": 79,
    "SystemMemoryListInformation": 80,
    "SystemFileCacheInformationEx": 81,
    "SystemThreadPriorityClientIdInformation": 82,
    "SystemProcessorIdleCycleTimeInformation": 83,
    "SystemVerifierCancellationInformation": 84,
    "SystemProcessorPowerInformationEx": 85,
    "SystemRefTraceInformation": 86,
    "SystemSpecialPoolInformation": 87,
    "SystemProcessIdInformation": 88,
    "SystemErrorPortInformation": 89,
    "SystemBootEnvironmentInformation": 90,
    "SystemHypervisorInformation": 91,
    "SystemVerifierInformationEx": 92,
    "SystemTimeZoneInformation": 93,
    "SystemImageFileExecutionOptionsInformation": 94,
    "SystemCoverageInformation": 95,
    "SystemPrefetchPatchInformation": 96,
    "SystemVerifierFaultsInformation": 97,
    "SystemSystemPartitionInformation": 98,
    "SystemSystemDiskInformation": 99,
    "SystemProcessorPerformanceDistribution": 100,
    "SystemNumaProximityNodeInformation": 101,
    "SystemDynamicTimeZoneInformation": 102,
    "SystemCodeIntegrityInformation": 103,
    "SystemProcessorMicrocodeUpdateInformation": 104,
    "SystemProcessorBrandString": 105,
    "SystemVirtualAddressInformation": 106,
    "SystemLogicalProcessorAndGroupInformation": 107,
    "SystemProcessorCycleTimeInformation": 108,
    "SystemStoreInformation": 109,
    "SystemRegistryAppendString": 110,
    "SystemAitSamplingValue": 111,
    "SystemVhdBootInformation": 112,
    "SystemCpuQuotaInformation": 113,
    "SystemNativeBasicInformation": 114,
    "SystemErrorPortTimeouts": 115,
    "SystemLowPriorityIoInformation": 116,
    "SystemBootEntropyInformation": 117,
    "SystemVerifierCountersInformation": 118,
    "SystemPagedPoolInformationEx": 119,
    "SystemSystemPtesInformationEx": 120,
    "SystemNodeDistanceInformation": 121,
    "SystemAcpiAuditInformation": 122,
    "SystemBasicPerformanceInformation": 123,
    "SystemQueryPerformanceCounterInformation": 124,
    "SystemSessionBigPoolInformation": 125,
    "SystemBootGraphicsInformation": 126,
    "SystemScrubPhysicalMemoryInformation": 127,
    "SystemBadPageInformation": 128,
    "SystemProcessorProfileControlArea": 129,
    "SystemCombinePhysicalMemoryInformation": 130,
    "SystemEntropyInterruptTimingCallback": 131,
    "SystemConsoleInformation": 132,
    "SystemPlatformBinaryInformation": 133,
    "SystemThrottleNotificationInformation": 134,
    "SystemHypervisorProcessorCountInformation": 135,
    "SystemDeviceDataInformation": 136,
    "SystemDeviceDataEnumerationInformation": 137,
    "SystemMemoryTopologyInformation": 138,
    "SystemMemoryChannelInformation": 139,
    "SystemBootLogoInformation": 140,
}
SYSTEM_INFORMATION_CLASS_INV = {
    0: "SystemBasicInformation",
    1: "SystemProcessorInformation",
    2: "SystemPerformanceInformation",
    3: "SystemTimeOfDayInformation",
    4: "SystemPathInformation",
    5: "SystemProcessInformation",
    6: "SystemCallCountInformation",
    7: "SystemDeviceInformation",
    8: "SystemProcessorPerformanceInformation",
    9: "SystemFlagsInformation",
    10: "SystemCallTimeInformation",
    11: "SystemModuleInformation",
    12: "SystemLocksInformation",
    13: "SystemStackTraceInformation",
    14: "SystemPagedPoolInformation",
    15: "SystemNonPagedPoolInformation",
    16: "SystemHandleInformation",
    17: "SystemObjectInformation",
    18: "SystemPageFileInformation",
    19: "SystemVdmInstemulInformation",
    20: "SystemVdmBopInformation",
    21: "SystemFileCacheInformation",
    22: "SystemPoolTagInformation",
    23: "SystemInterruptInformation",
    24: "SystemDpcBehaviorInformation",
    25: "SystemFullMemoryInformation",
    26: "SystemLoadGdiDriverInformation",
    27: "SystemUnloadGdiDriverInformation",
    28: "SystemTimeAdjustmentInformation",
    29: "SystemSummaryMemoryInformation",
    30: "SystemMirrorMemoryInformation",
    31: "SystemPerformanceTraceInformation",
    32: "SystemObsolete0",
    33: "SystemExceptionInformation",
    34: "SystemCrashDumpStateInformation",
    35: "SystemKernelDebuggerInformation",
    36: "SystemContextSwitchInformation",
    37: "SystemRegistryQuotaInformation",
    38: "SystemExtendServiceTableInformation",
    39: "SystemPrioritySeperation",
    40: "SystemVerifierAddDriverInformation",
    41: "SystemVerifierRemoveDriverInformation",
    42: "SystemProcessorIdleInformation",
    43: "SystemLegacyDriverInformation",
    44: "SystemCurrentTimeZoneInformation",
    45: "SystemLookasideInformation",
    46: "SystemTimeSlipNotification",
    47: "SystemSessionCreate",
    48: "SystemSessionDetach",
    49: "SystemSessionInformation",
    50: "SystemRangeStartInformation",
    51: "SystemVerifierInformation",
    52: "SystemVerifierThunkExtend",
    53: "SystemSessionProcessInformation",
    54: "SystemLoadGdiDriverInSystemSpace",
    55: "SystemNumaProcessorMap",
    56: "SystemPrefetcherInformation",
    57: "SystemExtendedProcessInformation",
    58: "SystemRecommendedSharedDataAlignment",
    59: "SystemComPlusPackage",
    60: "SystemNumaAvailableMemory",
    61: "SystemProcessorPowerInformation",
    62: "SystemEmulationBasicInformation",
    63: "SystemEmulationProcessorInformation",
    64: "SystemExtendedHandleInformation",
    65: "SystemLostDelayedWriteInformation",
    66: "SystemBigPoolInformation",
    67: "SystemSessionPoolTagInformation",
    68: "SystemSessionMappedViewInformation",
    69: "SystemHotpatchInformation",
    70: "SystemObjectSecurityMode",
    71: "SystemWatchdogTimerHandler",
    72: "SystemWatchdogTimerInformation",
    73: "SystemLogicalProcessorInformation",
    74: "SystemWow64SharedInformationObsolete",
    75: "SystemRegisterFirmwareTableInformationHandler",
    76: "SystemFirmwareTableInformation",
    77: "SystemModuleInformationEx",
    78: "SystemVerifierTriageInformation",
    79: "SystemSuperfetchInformation",
    80: "SystemMemoryListInformation",
    81: "SystemFileCacheInformationEx",
    82: "SystemThreadPriorityClientIdInformation",
    83: "SystemProcessorIdleCycleTimeInformation",
    84: "SystemVerifierCancellationInformation",
    85: "SystemProcessorPowerInformationEx",
    86: "SystemRefTraceInformation",
    87: "SystemSpecialPoolInformation",
    88: "SystemProcessIdInformation",
    89: "SystemErrorPortInformation",
    90: "SystemBootEnvironmentInformation",
    91: "SystemHypervisorInformation",
    92: "SystemVerifierInformationEx",
    93: "SystemTimeZoneInformation",
    94: "SystemImageFileExecutionOptionsInformation",
    95: "SystemCoverageInformation",
    96: "SystemPrefetchPatchInformation",
    97: "SystemVerifierFaultsInformation",
    98: "SystemSystemPartitionInformation",
    99: "SystemSystemDiskInformation",
    100: "SystemProcessorPerformanceDistribution",
    101: "SystemNumaProximityNodeInformation",
    102: "SystemDynamicTimeZoneInformation",
    103: "SystemCodeIntegrityInformation",
    104: "SystemProcessorMicrocodeUpdateInformation",
    105: "SystemProcessorBrandString",
    106: "SystemVirtualAddressInformation",
    107: "SystemLogicalProcessorAndGroupInformation",
    108: "SystemProcessorCycleTimeInformation",
    109: "SystemStoreInformation",
    110: "SystemRegistryAppendString",
    111: "SystemAitSamplingValue",
    112: "SystemVhdBootInformation",
    113: "SystemCpuQuotaInformation",
    114: "SystemNativeBasicInformation",
    115: "SystemErrorPortTimeouts",
    116: "SystemLowPriorityIoInformation",
    117: "SystemBootEntropyInformation",
    118: "SystemVerifierCountersInformation",
    119: "SystemPagedPoolInformationEx",
    120: "SystemSystemPtesInformationEx",
    121: "SystemNodeDistanceInformation",
    122: "SystemAcpiAuditInformation",
    123: "SystemBasicPerformanceInformation",
    124: "SystemQueryPerformanceCounterInformation",
    125: "SystemSessionBigPoolInformation",
    126: "SystemBootGraphicsInformation",
    127: "SystemScrubPhysicalMemoryInformation",
    128: "SystemBadPageInformation",
    129: "SystemProcessorProfileControlArea",
    130: "SystemCombinePhysicalMemoryInformation",
    131: "SystemEntropyInterruptTimingCallback",
    132: "SystemConsoleInformation",
    133: "SystemPlatformBinaryInformation",
    134: "SystemThrottleNotificationInformation",
    135: "SystemHypervisorProcessorCountInformation",
    136: "SystemDeviceDataInformation",
    137: "SystemDeviceDataEnumerationInformation",
    138: "SystemMemoryTopologyInformation",
    139: "SystemMemoryChannelInformation",
    140: "SystemBootLogoInformation",
}
_NtCreateDisposition_ = {
    "FILE_SUPERSEDE": 0x00000000,
    "FILE_OPEN": 0x00000001,
    "FILE_CREATE": 0x00000002,
    "FILE_OPEN_IF": 0x00000003,
    "FILE_OVERWRITE": 0x00000004,
    "FILE_OVERWRITE_IF": 0x00000005,
}
_NtCreateDisposition__INV = {
    0x00000000: "FILE_SUPERSEDE",
    0x00000001: "FILE_OPEN",
    0x00000002: "FILE_CREATE",
    0x00000003: "FILE_OPEN_IF",
    0x00000004: "FILE_OVERWRITE",
    0x00000005: "FILE_OVERWRITE_IF",
}
LPC_TYPE = {
    "LPC_NEW_MESSAGE": 0,
    "LPC_REQUEST": 1,
    "LPC_REPLY": 2,
    "LPC_DATAGRAM": 3,
    "LPC_LOST_REPLY": 4,
    "LPC_PORT_CLOSED": 5,
    "LPC_CLIENT_DIED": 6,
    "LPC_EXCEPTION": 7,
    "LPC_DEBUG_EVENT": 8,
    "LPC_ERROR_EVENT": 9,
    "LPC_CONNECTION_REQUEST": 10,
    "LPC_CONNECTION_REFUSED": 11,
}
LPC_TYPE_INV = {
    0: "LPC_NEW_MESSAGE",
    1: "LPC_REQUEST",
    2: "LPC_REPLY",
    3: "LPC_DATAGRAM",
    4: "LPC_LOST_REPLY",
    5: "LPC_PORT_CLOSED",
    6: "LPC_CLIENT_DIED",
    7: "LPC_EXCEPTION",
    8: "LPC_DEBUG_EVENT",
    9: "LPC_ERROR_EVENT",
    10: "LPC_CONNECTION_REQUEST",
    11: "LPC_CONNECTION_REFUSED",
}
_LDR_LOCK_LOADER_LOCK_DISPOSITION_ = {
    "LDR_LOCK_LOADER_LOCK_DISPOSITION_INVALID": 0,
    "LDR_LOCK_LOADER_LOCK_DISPOSITION_LOCK_ACQUIRED": 1,
    "LDR_LOCK_LOADER_LOCK_DISPOSITION_LOCK_NOT_ACQUIRED": 2,
}
_LDR_LOCK_LOADER_LOCK_DISPOSITION__INV = {
    0: "LDR_LOCK_LOADER_LOCK_DISPOSITION_INVALID",
    1: "LDR_LOCK_LOADER_LOCK_DISPOSITION_LOCK_ACQUIRED",
    2: "LDR_LOCK_LOADER_LOCK_DISPOSITION_LOCK_NOT_ACQUIRED",
}
TRANSACTIONMANAGER_INFORMATION_CLASS = {
    "TransactionManagerBasicInformation": 0,
    "TransactionManagerLogInformation": 1,
    "TransactionManagerLogPathInformation": 2,
    "TransactionManagerRecoveryInformation": 4,
}
TRANSACTIONMANAGER_INFORMATION_CLASS_INV = {
    0: "TransactionManagerBasicInformation",
    1: "TransactionManagerLogInformation",
    2: "TransactionManagerLogPathInformation",
    4: "TransactionManagerRecoveryInformation",
}
TRANSACTION_INFORMATION_CLASS = {
    "TransactionBasicInformation": 0,
    "TransactionPropertiesInformation": 1,
    "TransactionEnlistmentInformation": 2,
    "TransactionSuperiorEnlistmentInformation": 3,
}
TRANSACTION_INFORMATION_CLASS_INV = {
    0: "TransactionBasicInformation",
    1: "TransactionPropertiesInformation",
    2: "TransactionEnlistmentInformation",
    3: "TransactionSuperiorEnlistmentInformation",
}
ENLISTMENT_INFORMATION_CLASS = {
    "EnlistmentBasicInformation": 0,
    "EnlistmentRecoveryInformation": 1,
    "EnlistmentCrmInformation": 2,
}
ENLISTMENT_INFORMATION_CLASS_INV = {
    0: "EnlistmentBasicInformation",
    1: "EnlistmentRecoveryInformation",
    2: "EnlistmentCrmInformation",
}
RESOURCEMANAGER_INFORMATION_CLASS = {
    "ResourceManagerBasicInformation": 0,
    "ResourceManagerCompletionInformation": 1,
}
RESOURCEMANAGER_INFORMATION_CLASS_INV = {
    0: "ResourceManagerBasicInformation",
    1: "ResourceManagerCompletionInformation",
}
KTMOBJECT_TYPE = {
    "KTMOBJECT_TRANSACTION": 0,
    "KTMOBJECT_TRANSACTION_MANAGER": 1,
    "KTMOBJECT_RESOURCE_MANAGER": 2,
    "KTMOBJECT_ENLISTMENT": 3,
    "KTMOBJECT_INVALID": 4,
}
KTMOBJECT_TYPE_INV = {
    0: "KTMOBJECT_TRANSACTION",
    1: "KTMOBJECT_TRANSACTION_MANAGER",
    2: "KTMOBJECT_RESOURCE_MANAGER",
    3: "KTMOBJECT_ENLISTMENT",
    4: "KTMOBJECT_INVALID",
}
_HASH_STRING_ALGORITHM_ = {
    "HASH_STRING_ALGORITHM_DEFAULT": 0,
    "HASH_STRING_ALGORITHM_X65599": 1,
    "HASH_STRING_ALGORITHM_INVALID": 0xffffffff,
}
_HASH_STRING_ALGORITHM__INV = {
    0: "HASH_STRING_ALGORITHM_DEFAULT",
    1: "HASH_STRING_ALGORITHM_X65599",
    0xffffffff: "HASH_STRING_ALGORITHM_INVALID",
}

def ntdll_NtClearEvent(jitter):
    """
    NTSTATUS NtClearEvent(
        HANDLE EventHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateEvent(jitter):
    """
    NTSTATUS NtCreateEvent(
        PHANDLE EventHandle,
        [EVENT_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        EVENT_TYPE EventType,
        BOOLEAN InitialState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "DesiredAccess", "ObjectAttributes", "EventType", "InitialState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateEventPair(jitter):
    """
    NTSTATUS NtCreateEventPair(
        PHANDLE EventPairHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventPairHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateKeyedEvent(jitter):
    """
    NTSTATUS NtCreateKeyedEvent(
        PHANDLE KeyedEventHandle,
        [EVENT_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyedEventHandle", "DesiredAccess", "ObjectAttributes", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateMutant(jitter):
    """
    NTSTATUS NtCreateMutant(
        PHANDLE MutantHandle,
        [MUTANT_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        BOOLEAN InitialOwner
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MutantHandle", "DesiredAccess", "ObjectAttributes", "InitialOwner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateSemaphore(jitter):
    """
    NTSTATUS NtCreateSemaphore(
        PHANDLE SemaphoreHandle,
        [SEMAPHORE_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        LONG InitialCount,
        LONG MaximumCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SemaphoreHandle", "DesiredAccess", "ObjectAttributes", "InitialCount", "MaximumCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateTimer(jitter):
    """
    NTSTATUS NtCreateTimer(
        PHANDLE TimerHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        TIMER_TYPE TimerType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerHandle", "DesiredAccess", "ObjectAttributes", "TimerType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenEvent(jitter):
    """
    NTSTATUS NtOpenEvent(
        PHANDLE EventHandle,
        [EVENT_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenKeyedEvent(jitter):
    """
    NTSTATUS NtOpenKeyedEvent(
        PHANDLE EventHandle,
        [EVENT_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenEventPair(jitter):
    """
    NTSTATUS NtOpenEventPair(
        PHANDLE EventPairHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventPairHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenMutant(jitter):
    """
    NTSTATUS NtOpenMutant(
        PHANDLE MutantHandle,
        [MUTANT_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MutantHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenSemaphore(jitter):
    """
    NTSTATUS NtOpenSemaphore(
        PHANDLE SemaphoreHandle,
        [SEMAPHORE_ACCESS_MASK] DesiredAcces,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SemaphoreHandle", "DesiredAcces", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenTimer(jitter):
    """
    NTSTATUS NtOpenTimer(
        PHANDLE TimerHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPulseEvent(jitter):
    """
    NTSTATUS NtPulseEvent(
        HANDLE EventHandle,
        PLONG PulseCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "PulseCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryEvent(jitter):
    """
    NTSTATUS NtQueryEvent(
        HANDLE EventHandle,
        EVENT_INFORMATION_CLASS EventInformationClass,
        PVOID EventInformation,
        ULONG EventInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "EventInformationClass", "EventInformation", "EventInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryMutant(jitter):
    """
    NTSTATUS NtQueryMutant(
        HANDLE MutantHandle,
        MUTANT_INFORMATION_CLASS MutantInformationClass,
        PVOID MutantInformation,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MutantHandle", "MutantInformationClass", "MutantInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQuerySemaphore(jitter):
    """
    NTSTATUS NtQuerySemaphore(
        HANDLE SemaphoreHandle,
        SEMAPHORE_INFORMATION_CLASS SemaphoreInformationClass,
        PVOID SemaphoreInformation,
        ULONG Length,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SemaphoreHandle", "SemaphoreInformationClass", "SemaphoreInformation", "Length", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryTimer(jitter):
    """
    NTSTATUS NtQueryTimer(
        HANDLE TimerHandle,
        TIMER_INFORMATION_CLASS TimerInformationClass,
        PVOID TimerInformation,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerHandle", "TimerInformationClass", "TimerInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReleaseMutant(jitter):
    """
    NTSTATUS NtReleaseMutant(
        HANDLE MutantHandle,
        PLONG ReleaseCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MutantHandle", "ReleaseCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReleaseKeyedEvent(jitter):
    """
    NTSTATUS NtReleaseKeyedEvent(
        HANDLE EventHandle,
        PVOID Key,
        BOOLEAN Alertable,
        PLARGE_INTEGER Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "Key", "Alertable", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReleaseSemaphore(jitter):
    """
    NTSTATUS NtReleaseSemaphore(
        HANDLE SemaphoreHandle,
        LONG ReleaseCount,
        PLONG PreviousCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SemaphoreHandle", "ReleaseCount", "PreviousCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtResetEvent(jitter):
    """
    NTSTATUS NtResetEvent(
        HANDLE EventHandle,
        PLONG NumberOfWaitingThreads
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "NumberOfWaitingThreads"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetEvent(jitter):
    """
    NTSTATUS NtSetEvent(
        HANDLE EventHandle,
        PLONG PreviousState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "PreviousState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetEventBoostPriority(jitter):
    """
    NTSTATUS NtSetEventBoostPriority(
        HANDLE EventHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetHighEventPair(jitter):
    """
    NTSTATUS NtSetHighEventPair(
        HANDLE EventPairHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventPairHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetHighWaitLowEventPair(jitter):
    """
    NTSTATUS NtSetHighWaitLowEventPair(
        HANDLE EventPairHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventPairHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetLowEventPair(jitter):
    """
    NTSTATUS NtSetLowEventPair(
        HANDLE EventPair
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventPair"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetLowWaitHighEventPair(jitter):
    """
    NTSTATUS NtSetLowWaitHighEventPair(
        HANDLE EventPair
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventPair"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetTimer(jitter):
    """
    NTSTATUS NtSetTimer(
        HANDLE TimerHandle,
        PLARGE_INTEGER DueTime,
        PTIMER_APC_ROUTINE TimerApcRoutine,
        PVOID TimerContext,
        BOOLEAN WakeTimer,
        LONG Period,
        PBOOLEAN PreviousState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerHandle", "DueTime", "TimerApcRoutine", "TimerContext", "WakeTimer", "Period", "PreviousState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCancelTimer(jitter):
    """
    NTSTATUS NtCancelTimer(
        HANDLE TimerHandle,
        PBOOLEAN CurrentState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerHandle", "CurrentState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWaitForKeyedEvent(jitter):
    """
    NTSTATUS NtWaitForKeyedEvent(
        HANDLE EventHandle,
        PVOID Key,
        BOOLEAN Alertable,
        PLARGE_INTEGER Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle", "Key", "Alertable", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWaitHighEventPair(jitter):
    """
    NTSTATUS NtWaitHighEventPair(
        HANDLE EventPairHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventPairHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWaitLowEventPair(jitter):
    """
    NTSTATUS NtWaitLowEventPair(
        HANDLE EventPairHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventPairHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtTraceEvent(jitter):
    """
    NTSTATUS NtTraceEvent(
        ULONG TraceHandle,
        ULONG Flags,
        ULONG TraceHeaderLength,
        PEVENT_TRACE_HEADER TraceHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TraceHandle", "Flags", "TraceHeaderLength", "TraceHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSignalAndWaitForSingleObject(jitter):
    """
    [NT_WAIT_RESULT] NtSignalAndWaitForSingleObject(
        HANDLE SignalObject,
        HANDLE WaitObject,
        BOOLEAN Alertable,
        PLARGE_INTEGER Time
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SignalObject", "WaitObject", "Alertable", "Time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWaitForMultipleObjects(jitter):
    """
    [NT_WAIT_RESULT] NtWaitForMultipleObjects(
        ULONG Count,
        HANDLE [] Object,
        WAIT_TYPE WaitType,
        BOOLEAN Alertable,
        PLARGE_INTEGER Time
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Count", "Object", "WaitType", "Alertable", "Time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWaitForMultipleObjects32(jitter):
    """
    [NT_WAIT_RESULT] NtWaitForMultipleObjects32(
        ULONG ObjectCount,
        PLONG Handles,
        WAIT_TYPE WaitType,
        BOOLEAN Alertable,
        PLARGE_INTEGER TimeOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectCount", "Handles", "WaitType", "Alertable", "TimeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWaitForSingleObject(jitter):
    """
    [NT_WAIT_RESULT] NtWaitForSingleObject(
        HANDLE Object,
        BOOLEAN Alertable,
        PLARGE_INTEGER Time
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Object", "Alertable", "Time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCompressKey(jitter):
    """
    NTSTATUS NtCompressKey(
        HANDLE Key
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Key"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateKey(jitter):
    """
    NTSTATUS NtCreateKey(
        PHANDLE KeyHandle,
        [REGISTRY_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG TitleIndex,
        PUNICODE_STRING Class,
        ULONG CreateOptions,
        [RegDisposition-PULONG] Disposition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "DesiredAccess", "ObjectAttributes", "TitleIndex", "Class", "CreateOptions", "Disposition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateKeyTransacted(jitter):
    """
    NTSTATUS NtCreateKeyTransacted(
        PHANDLE KeyHandle,
        [REGISTRY_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG TitleIndex,
        PUNICODE_STRING Class,
        ULONG CreateOptions,
        HANDLE TransactionHandle,
        [RegDisposition-PULONG] Disposition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "DesiredAccess", "ObjectAttributes", "TitleIndex", "Class", "CreateOptions", "TransactionHandle", "Disposition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDeleteKey(jitter):
    """
    NTSTATUS NtDeleteKey(
        HANDLE KeyHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDeleteValueKey(jitter):
    """
    NTSTATUS NtDeleteValueKey(
        HANDLE KeyHandle,
        PUNICODE_STRING ValueName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "ValueName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtEnumerateKey(jitter):
    """
    NTSTATUS NtEnumerateKey(
        HANDLE KeyHandle,
        ULONG Index,
        KEY_INFORMATION_CLASS KeyInformationClass,
        PVOID KeyInformation,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "Index", "KeyInformationClass", "KeyInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtEnumerateValueKey(jitter):
    """
    NTSTATUS NtEnumerateValueKey(
        HANDLE KeyHandle,
        ULONG Index,
        KEY_VALUE_INFORMATION_CLASS KeyValueInformationClass,
        PVOID KeyValueInformation,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "Index", "KeyValueInformationClass", "KeyValueInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFlushKey(jitter):
    """
    NTSTATUS NtFlushKey(
        HANDLE KeyHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtInitializeRegistry(jitter):
    """
    NTSTATUS NtInitializeRegistry(
        USHORT Flag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtLoadKey(jitter):
    """
    NTSTATUS NtLoadKey(
        POBJECT_ATTRIBUTES KeyObjectAttributes,
        POBJECT_ATTRIBUTES FileObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyObjectAttributes", "FileObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtLoadKey2(jitter):
    """
    NTSTATUS NtLoadKey2(
        POBJECT_ATTRIBUTES KeyObjectAttributes,
        POBJECT_ATTRIBUTES FileObjectAttributes,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyObjectAttributes", "FileObjectAttributes", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtLockRegistryKey(jitter):
    """
    NTSTATUS NtLockRegistryKey(
        HANDLE KeyHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtNotifyChangeKey(jitter):
    """
    NTSTATUS NtNotifyChangeKey(
        HANDLE KeyHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        [REG_NOTIFY_CHANGE_FLAGS] CompletionFilter,
        BOOLEAN Asynchroneous,
        PVOID ChangeBuffer,
        ULONG Length,
        BOOLEAN WatchSubtree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "CompletionFilter", "Asynchroneous", "ChangeBuffer", "Length", "WatchSubtree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtNotifyChangeMultipleKeys(jitter):
    """
    NTSTATUS NtNotifyChangeMultipleKeys(
        HANDLE MasterKeyHandle,
        ULONG Count,
        OBJECT_ATTRIBUTES [] SubordinateObjects,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        [REG_NOTIFY_CHANGE_FLAGS] CompletionFilter,
        BOOLEAN WatchTree,
        PVOID Buffer,
        ULONG Length,
        BOOLEAN Asynchronous
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MasterKeyHandle", "Count", "SubordinateObjects", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "CompletionFilter", "WatchTree", "Buffer", "Length", "Asynchronous"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenKey(jitter):
    """
    NTSTATUS NtOpenKey(
        PHANDLE KeyHandle,
        [REGISTRY_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenKeyEx(jitter):
    """
    NTSTATUS NtOpenKeyEx(
        PHANDLE KeyHandle,
        [REGISTRY_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG OpenOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "DesiredAccess", "ObjectAttributes", "OpenOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenKeyTransacted(jitter):
    """
    NTSTATUS NtOpenKeyTransacted(
        PHANDLE KeyHandle,
        [REGISTRY_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        HANDLE TransactionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "DesiredAccess", "ObjectAttributes", "TransactionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenKeyTransactedEx(jitter):
    """
    NTSTATUS NtOpenKeyTransactedEx(
        PHANDLE KeyHandle,
        [REGISTRY_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG OpenOptions,
        HANDLE TransactionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "DesiredAccess", "ObjectAttributes", "OpenOptions", "TransactionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryKey(jitter):
    """
    NTSTATUS NtQueryKey(
        HANDLE KeyHandle,
        KEY_INFORMATION_CLASS KeyInformationClass,
        PVOID KeyInformation,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "KeyInformationClass", "KeyInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryMultipleValueKey(jitter):
    """
    NTSTATUS NtQueryMultipleValueKey(
        HANDLE KeyHandle,
        PKEY_VALUE_ENTRY ValueList,
        ULONG NumberOfValues,
        PVOID Buffer,
        PULONG Length,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "ValueList", "NumberOfValues", "Buffer", "Length", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryOpenSubKeys(jitter):
    """
    NTSTATUS NtQueryOpenSubKeys(
        POBJECT_ATTRIBUTES TargetKey,
        PULONG HandleCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetKey", "HandleCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryOpenSubKeysEx(jitter):
    """
    NTSTATUS NtQueryOpenSubKeysEx(
        POBJECT_ATTRIBUTES TargetKey,
        ULONG BufferLength,
        PVOID Buffer,
        PULONG RequiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetKey", "BufferLength", "Buffer", "RequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryValueKey(jitter):
    """
    NTSTATUS NtQueryValueKey(
        HANDLE KeyHandle,
        PUNICODE_STRING ValueName,
        KEY_VALUE_INFORMATION_CLASS KeyValueInformationClass,
        PVOID KeyValueInformation,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "ValueName", "KeyValueInformationClass", "KeyValueInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRenameKey(jitter):
    """
    NTSTATUS NtRenameKey(
        HANDLE KeyHandle,
        PUNICODE_STRING ReplacementName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "ReplacementName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReplaceKey(jitter):
    """
    NTSTATUS NtReplaceKey(
        POBJECT_ATTRIBUTES ObjectAttributes,
        HANDLE Key,
        POBJECT_ATTRIBUTES ReplacedObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectAttributes", "Key", "ReplacedObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRestoreKey(jitter):
    """
    NTSTATUS NtRestoreKey(
        HANDLE KeyHandle,
        HANDLE FileHandle,
        ULONG RestoreFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "FileHandle", "RestoreFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSaveKey(jitter):
    """
    NTSTATUS NtSaveKey(
        HANDLE KeyHandle,
        HANDLE FileHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "FileHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSaveKeyEx(jitter):
    """
    NTSTATUS NtSaveKeyEx(
        HANDLE KeyHandle,
        HANDLE FileHandle,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "FileHandle", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSaveMergedKeys(jitter):
    """
    NTSTATUS NtSaveMergedKeys(
        HANDLE HighPrecedenceKeyHandle,
        HANDLE LowPrecedenceKeyHandle,
        HANDLE FileHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HighPrecedenceKeyHandle", "LowPrecedenceKeyHandle", "FileHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationKey(jitter):
    """
    NTSTATUS NtSetInformationKey(
        HANDLE KeyHandle,
        KEY_SET_INFORMATION_CLASS KeyInformationClass,
        PVOID KeyInformation,
        ULONG KeyInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "KeyInformationClass", "KeyInformation", "KeyInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetValueKey(jitter):
    """
    NTSTATUS NtSetValueKey(
        HANDLE KeyHandle,
        PUNICODE_STRING ValueName,
        ULONG TitleIndex,
        ULONG Type,
        PVOID Data,
        ULONG DataSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "ValueName", "TitleIndex", "Type", "Data", "DataSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtUnloadKey(jitter):
    """
    NTSTATUS NtUnloadKey(
        POBJECT_ATTRIBUTES KeyObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtUnloadKey2(jitter):
    """
    NTSTATUS NtUnloadKey2(
        POBJECT_ATTRIBUTES TargetKey,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetKey", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtUnloadKeyEx(jitter):
    """
    NTSTATUS NtUnloadKeyEx(
        POBJECT_ATTRIBUTES TargetKey,
        HANDLE Event
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TargetKey", "Event"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCompactKeys(jitter):
    """
    NTSTATUS NtCompactKeys(
        ULONG NrOfKeys,
        HANDLE KeysArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NrOfKeys", "KeysArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFreezeRegistry(jitter):
    """
    NTSTATUS NtFreezeRegistry(
        USHORT TimeOutInSeconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimeOutInSeconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtThawRegistry(jitter):
    """
    NTSTATUS NtThawRegistry()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAddAtom(jitter):
    """
    NTSTATUS NtAddAtom(
        PWSTR AtomName,
        ULONG AtomNameLength,
        PRTL_ATOM Atom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomName", "AtomNameLength", "Atom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDeleteAtom(jitter):
    """
    NTSTATUS NtDeleteAtom(
        RTL_ATOM Atom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Atom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFindAtom(jitter):
    """
    NTSTATUS NtFindAtom(
        PWSTR AtomName,
        ULONG AtomNameLength,
        PRTL_ATOM Atom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomName", "AtomNameLength", "Atom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationAtom(jitter):
    """
    NTSTATUS NtQueryInformationAtom(
        RTL_ATOM Atom,
        ATOM_INFORMATION_CLASS AtomInformationClass,
        PVOID AtomInformation,
        ULONG AtomInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Atom", "AtomInformationClass", "AtomInformation", "AtomInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryDefaultLocale(jitter):
    """
    NTSTATUS NtQueryDefaultLocale(
        BOOLEAN UserProfile,
        PLCID DefaultLocaleId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UserProfile", "DefaultLocaleId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryDefaultUILanguage(jitter):
    """
    NTSTATUS NtQueryDefaultUILanguage(
        LANGID* LanguageId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LanguageId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInstallUILanguage(jitter):
    """
    NTSTATUS NtQueryInstallUILanguage(
        LANGID* LanguageId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LanguageId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetDefaultLocale(jitter):
    """
    NTSTATUS NtSetDefaultLocale(
        BOOLEAN UserProfile,
        LCID DefaultLocaleId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UserProfile", "DefaultLocaleId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetDefaultUILanguage(jitter):
    """
    NTSTATUS NtSetDefaultUILanguage(
        LANGID LanguageId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LanguageId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrAllocateCaptureBuffer(jitter):
    """
    PVOID CsrAllocateCaptureBuffer(
        ULONG ArgumentCount,
        ULONG BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ArgumentCount", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrAllocateMessagePointer(jitter):
    """
    ULONG CsrAllocateMessagePointer(
        CSR_CAPTURE_BUFFER* CaptureBuffer,
        ULONG MessageLength,
        PVOID* CaptureData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CaptureBuffer", "MessageLength", "CaptureData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrCaptureMessageBuffer(jitter):
    """
    VOID CsrCaptureMessageBuffer(
        CSR_CAPTURE_BUFFER* CaptureBuffer,
        PVOID MessageString,
        ULONG StringLength,
        PVOID* CapturedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CaptureBuffer", "MessageString", "StringLength", "CapturedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrClientConnectToServer(jitter):
    """
    NTSTATUS CsrClientConnectToServer(
        PWSTR ObjectDirectory,
        ULONG ServerId,
        PVOID ConnectionInfo,
        PULONG ConnectionInfoSize,
        PBOOLEAN ServerToServerCall
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectDirectory", "ServerId", "ConnectionInfo", "ConnectionInfoSize", "ServerToServerCall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrClientCallServer(jitter):
    """
    NTSTATUS CsrClientCallServer(
        CSR_API_MESSAGE* Request,
        CSR_CAPTURE_BUFFER* CaptureBuffer,
        ULONG ApiNumber,
        ULONG RequestLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Request", "CaptureBuffer", "ApiNumber", "RequestLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrIdentifyAlertableThread(jitter):
    """
    NTSTATUS CsrIdentifyAlertableThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrFreeCaptureBuffer(jitter):
    """
    VOID CsrFreeCaptureBuffer(
        CSR_CAPTURE_BUFFER* CaptureBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CaptureBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrGetProcessId(jitter):
    """
    HANDLE CsrGetProcessId()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrNewThread(jitter):
    """
    NTSTATUS CsrNewThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrSetPriorityClass(jitter):
    """
    NTSTATUS CsrSetPriorityClass(
        HANDLE Process,
        PULONG PriorityClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Process", "PriorityClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrProbeForRead(jitter):
    """
    VOID CsrProbeForRead(
        PVOID Address,
        ULONG Length,
        ULONG Alignment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address", "Length", "Alignment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_CsrProbeForWrite(jitter):
    """
    VOID CsrProbeForWrite(
        PVOID Address,
        ULONG Length,
        ULONG Alignment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address", "Length", "Alignment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUserBreakPoint(jitter):
    """
    VOID DbgUserBreakPoint()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgPrint(jitter):
    """
    [NTSTATUS_ULONG] DbgPrint(
        PCCH Format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgPrintEx(jitter):
    """
    [NTSTATUS_ULONG] DbgPrintEx(
        ULONG ComponentId,
        ULONG Level,
        PCCH Format,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComponentId", "Level", "Format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgPrompt(jitter):
    """
    [NTSTATUS_ULONG] DbgPrompt(
        PCCH Prompt,
        PCH Response,
        ULONG MaximumResponseLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Prompt", "Response", "MaximumResponseLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgBreakPoint(jitter):
    """
    VOID DbgBreakPoint()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgLoadImageSymbols(jitter):
    """
    NTSTATUS DbgLoadImageSymbols(
        PANSI_STRING Name,
        PVOID Base,
        ULONG_PTR ProcessId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "Base", "ProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUnLoadImageSymbols(jitter):
    """
    VOID DbgUnLoadImageSymbols(
        PANSI_STRING Name,
        PVOID Base,
        ULONG_PTR ProcessId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "Base", "ProcessId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgBreakPointWithStatus(jitter):
    """
    VOID DbgBreakPointWithStatus(
        ULONG Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiConnectToDbg(jitter):
    """
    NTSTATUS DbgUiConnectToDbg()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiContinue(jitter):
    """
    NTSTATUS DbgUiContinue(
        PCLIENT_ID ClientId,
        NTSTATUS ContinueStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientId", "ContinueStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiDebugActiveProcess(jitter):
    """
    NTSTATUS DbgUiDebugActiveProcess(
        HANDLE Process
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Process"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiStopDebugging(jitter):
    """
    NTSTATUS DbgUiStopDebugging(
        HANDLE Process
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Process"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiWaitStateChange(jitter):
    """
    NTSTATUS DbgUiWaitStateChange(
        PDBGUI_WAIT_STATE_CHANGE DbgUiWaitStateCange,
        PLARGE_INTEGER TimeOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DbgUiWaitStateCange", "TimeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiConvertStateChangeStructure(jitter):
    """
    NTSTATUS DbgUiConvertStateChangeStructure(
        PDBGUI_WAIT_STATE_CHANGE WaitStateChange,
        PVOID DebugEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["WaitStateChange", "DebugEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiRemoteBreakin(jitter):
    """
    VOID DbgUiRemoteBreakin()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiIssueRemoteBreakin(jitter):
    """
    NTSTATUS DbgUiIssueRemoteBreakin(
        HANDLE Process
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Process"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgUiGetThreadDebugObject(jitter):
    """
    HANDLE DbgUiGetThreadDebugObject()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_vDbgPrintEx(jitter):
    """
    [NTSTATUS_ULONG] vDbgPrintEx(
        ULONG ComponentId,
        ULONG Level,
        PCH Format,
        va_list arglist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComponentId", "Level", "Format", "arglist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_vDbgPrintExWithPrefix(jitter):
    """
    [NTSTATUS_ULONG] vDbgPrintExWithPrefix(
        PCH Prefix,
        ULONG ComponentId,
        ULONG Level,
        PCH Format,
        va_list arglist
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Prefix", "ComponentId", "Level", "Format", "arglist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgQueryDebugFilterState(jitter):
    """
    NTSTATUS DbgQueryDebugFilterState(
        ULONG ComponentId,
        ULONG Level
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComponentId", "Level"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_DbgSetDebugFilterState(jitter):
    """
    NTSTATUS DbgSetDebugFilterState(
        ULONG ComponentId,
        ULONG Level,
        BOOLEAN State
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComponentId", "Level", "State"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrAccessResource(jitter):
    """
    NTSTATUS LdrAccessResource(
        [HMODULE-PVOID] BaseAddress,
        PIMAGE_RESOURCE_DATA_ENTRY ResourceDataEntry,
        PVOID* Resource,
        PULONG Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "ResourceDataEntry", "Resource", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrFindResource_U(jitter):
    """
    NTSTATUS LdrFindResource_U(
        [HMODULE-PVOID] BaseAddress,
        PLDR_RESOURCE_INFO ResourceInfo,
        ULONG Level,
        PIMAGE_RESOURCE_DATA_ENTRY* ResourceDataEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "ResourceInfo", "Level", "ResourceDataEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrFindResourceDirectory_U(jitter):
    """
    NTSTATUS LdrFindResourceDirectory_U(
        [HMODULE-PVOID] BaseAddress,
        PLDR_RESOURCE_INFO ResourceInfo,
        ULONG Level,
        PIMAGE_RESOURCE_DIRECTORY* ResourceDirectory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "ResourceInfo", "Level", "ResourceDirectory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrUnloadAlternateResourceModule(jitter):
    """
    BOOLEAN LdrUnloadAlternateResourceModule(
        [HMODULE-PVOID] BaseAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrRelocateImage(jitter):
    """
    [NTSTATUS_ULONG] LdrRelocateImage(
        PVOID NewBase,
        PUCHAR LoaderName,
        ULONG Success,
        ULONG Conflict,
        ULONG Invalid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NewBase", "LoaderName", "Success", "Conflict", "Invalid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrLockLoaderLock(jitter):
    """
    NTSTATUS LdrLockLoaderLock(
        [LDR_LOCK_LOADER_LOCK_FLAG] Flags,
        [LDR_LOCK_LOADER_LOCK_DISPOSITION*] Disposition,
        PULONG Cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Disposition", "Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrUnlockLoaderLock(jitter):
    """
    NTSTATUS LdrUnlockLoaderLock(
        [LDR_UNLOCK_LOADER_LOCK_FLAG] Flags,
        ULONG Cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrVerifyMappedImageMatchesChecksum(jitter):
    """
    BOOLEAN LdrVerifyMappedImageMatchesChecksum(
        [HMODULE-PVOID] BaseAddress,
        ULONG NumberOfBytes,
        ULONG FileLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "NumberOfBytes", "FileLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrAddRefDll(jitter):
    """
    NTSTATUS LdrAddRefDll(
        [LDR_ADDREF_DLL_FLAGS] Flags,
        [HMODULE-PVOID] BaseAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrDisableThreadCalloutsForDll(jitter):
    """
    NTSTATUS LdrDisableThreadCalloutsForDll(
        [HMODULE-PVOID] BaseAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrGetDllHandle(jitter):
    """
    NTSTATUS LdrGetDllHandle(
        PWSTR DllPath,
        PULONG DllCharacteristics,
        PUNICODE_STRING DllName,
        HMODULE* DllHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DllPath", "DllCharacteristics", "DllName", "DllHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrGetDllHandleEx(jitter):
    """
    NTSTATUS LdrGetDllHandleEx(
        [LDR_GET_DLL_HANDLE_EX_FLAGS] Flags,
        PWSTR DllPath,
        PULONG DllCharacteristics,
        PUNICODE_STRING DllName,
        HMODULE* DllHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "DllPath", "DllCharacteristics", "DllName", "DllHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrFindEntryForAddress(jitter):
    """
    NTSTATUS LdrFindEntryForAddress(
        PVOID Address,
        PLDR_DATA_TABLE_ENTRY* Module
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address", "Module"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrGetProcedureAddress(jitter):
    """
    NTSTATUS LdrGetProcedureAddress(
        HMODULE BaseAddress,
        PANSI_STRING Name,
        ULONG Ordinal,
        PVOID* ProcedureAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "Name", "Ordinal", "ProcedureAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrInitializeThunk(jitter):
    """
    VOID LdrInitializeThunk(
        ULONG Unknown1,
        ULONG Unknown2,
        ULONG Unknown3,
        ULONG Unknown4
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Unknown1", "Unknown2", "Unknown3", "Unknown4"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrLoadDll(jitter):
    """
    NTSTATUS LdrLoadDll(
        PWSTR SearchPath,
        [IMAGE_FILE_CHARACTERISTICS_ULONG*] DllCharacteristics,
        PUNICODE_STRING Name,
        [HMODULE-PVOID*] BaseAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SearchPath", "DllCharacteristics", "Name", "BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrProcessRelocationBlock(jitter):
    """
    PIMAGE_BASE_RELOCATION LdrProcessRelocationBlock(
        ULONG_PTR Address,
        ULONG Count,
        PUSHORT TypeOffset,
        LONG_PTR Delta
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address", "Count", "TypeOffset", "Delta"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrQueryImageFileExecutionOptions(jitter):
    """
    NTSTATUS LdrQueryImageFileExecutionOptions(
        PUNICODE_STRING SubKey,
        PCWSTR ValueName,
        ULONG ValueSize,
        PVOID Buffer,
        ULONG BufferSize,
        PULONG RetunedLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubKey", "ValueName", "ValueSize", "Buffer", "BufferSize", "RetunedLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrQueryProcessModuleInformation(jitter):
    """
    NTSTATUS LdrQueryProcessModuleInformation(
        PRTL_PROCESS_MODULES ModuleInformation,
        ULONG Size,
        PULONG ReturnedSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ModuleInformation", "Size", "ReturnedSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrShutdownThread(jitter):
    """
    NTSTATUS LdrShutdownThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrUnloadDll(jitter):
    """
    NTSTATUS LdrUnloadDll(
        [HMODULE-PVOID] BaseAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrVerifyImageMatchesChecksum(jitter):
    """
    NTSTATUS LdrVerifyImageMatchesChecksum(
        HANDLE FileHandle,
        PLDR_CALLBACK Callback,
        PVOID CallbackContext,
        [IMAGE_FILE_CHARACTERISTICS_SHORT] ImageCharacteristics
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Callback", "CallbackContext", "ImageCharacteristics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrRelocateImageWithBias(jitter):
    """
    [NTSTATUS_ULONG] LdrRelocateImageWithBias(
        PVOID NewAddress,
        LONGLONG AdditionalBias,
        PCCH LoaderName,
        ULONG Success,
        ULONG Conflict,
        ULONG Invalid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NewAddress", "AdditionalBias", "LoaderName", "Success", "Conflict", "Invalid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrResFindResourceDirectory(jitter):
    """
    NTSTATUS LdrResFindResourceDirectory(
        [HMODULE-PVOID] BaseAddress,
        PVOID Unknown1,
        PVOID Unknown2,
        PVOID* ResourceDirectory,
        PVOID Unknown3,
        PVOID Unknown4,
        PVOID Unknown5
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "Unknown1", "Unknown2", "ResourceDirectory", "Unknown3", "Unknown4", "Unknown5"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAccessCheck(jitter):
    """
    NTSTATUS NtAccessCheck(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        HANDLE ClientToken,
        ACCESS_MASK DesiredAccess,
        PGENERIC_MAPPING GenericMapping,
        PPRIVILEGE_SET PrivilegeSet,
        PULONG ReturnLength,
        PACCESS_MASK GrantedAccess,
        PNTSTATUS AccessStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "ClientToken", "DesiredAccess", "GenericMapping", "PrivilegeSet", "ReturnLength", "GrantedAccess", "AccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAccessCheckByType(jitter):
    """
    NTSTATUS NtAccessCheckByType(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID PrincipalSelfSid,
        HANDLE ClientToken,
        ACCESS_MASK DesiredAccess,
        POBJECT_TYPE_LIST ObjectTypeList,
        ULONG ObjectTypeLength,
        PGENERIC_MAPPING GenericMapping,
        PPRIVILEGE_SET PrivilegeSet,
        ULONG PrivilegeSetLength,
        PACCESS_MASK GrantedAccess,
        PNTSTATUS AccessStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "PrincipalSelfSid", "ClientToken", "DesiredAccess", "ObjectTypeList", "ObjectTypeLength", "GenericMapping", "PrivilegeSet", "PrivilegeSetLength", "GrantedAccess", "AccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAccessCheckByTypeResultList(jitter):
    """
    NTSTATUS NtAccessCheckByTypeResultList(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID PrincipalSelfSid,
        HANDLE ClientToken,
        ACCESS_MASK DesiredAccess,
        POBJECT_TYPE_LIST ObjectTypeList,
        ULONG ObjectTypeLength,
        PGENERIC_MAPPING GenericMapping,
        PPRIVILEGE_SET PrivilegeSet,
        ULONG PrivilegeSetLength,
        PACCESS_MASK GrantedAccess,
        PNTSTATUS AccessStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "PrincipalSelfSid", "ClientToken", "DesiredAccess", "ObjectTypeList", "ObjectTypeLength", "GenericMapping", "PrivilegeSet", "PrivilegeSetLength", "GrantedAccess", "AccessStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAccessCheckAndAuditAlarm(jitter):
    """
    NTSTATUS NtAccessCheckAndAuditAlarm(
        PUNICODE_STRING SubsystemName,
        PVOID HandleId,
        PUNICODE_STRING ObjectTypeName,
        PUNICODE_STRING ObjectName,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        ACCESS_MASK DesiredAccess,
        PGENERIC_MAPPING GenericMapping,
        BOOLEAN ObjectCreation,
        PACCESS_MASK GrantedAccess,
        PNTSTATUS AccessStatus,
        PBOOLEAN GenerateOnClose
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ObjectTypeName", "ObjectName", "SecurityDescriptor", "DesiredAccess", "GenericMapping", "ObjectCreation", "GrantedAccess", "AccessStatus", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenThreadToken(jitter):
    """
    NTSTATUS NtOpenThreadToken(
        [ThreadHandle] ThreadHandle,
        [TOKEN_ACCESS_MASK] DesiredAccess,
        BOOLEAN OpenAsSelf,
        PHANDLE TokenHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "DesiredAccess", "OpenAsSelf", "TokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenThreadTokenEx(jitter):
    """
    NTSTATUS NtOpenThreadTokenEx(
        [ThreadHandle] ThreadHandle,
        [TOKEN_ACCESS_MASK] DesiredAccess,
        BOOLEAN OpenAsSelf,
        ULONG HandleAttributes,
        PHANDLE TokenHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "DesiredAccess", "OpenAsSelf", "HandleAttributes", "TokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAdjustGroupsToken(jitter):
    """
    NTSTATUS NtAdjustGroupsToken(
        HANDLE TokenHandle,
        BOOLEAN ResetToDefault,
        PTOKEN_GROUPS NewState,
        ULONG BufferLength,
        PTOKEN_GROUPS PreviousState,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "ResetToDefault", "NewState", "BufferLength", "PreviousState", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAdjustPrivilegesToken(jitter):
    """
    NTSTATUS NtAdjustPrivilegesToken(
        HANDLE TokenHandle,
        BOOLEAN DisableAllPrivileges,
        PTOKEN_PRIVILEGES NewState,
        ULONG BufferLength,
        PTOKEN_PRIVILEGES PreviousState,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "DisableAllPrivileges", "NewState", "BufferLength", "PreviousState", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCompareTokens(jitter):
    """
    NTSTATUS NtCompareTokens(
        HANDLE FirstTokenHandle,
        HANDLE SecondTokenHandle,
        PBOOLEAN Equal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FirstTokenHandle", "SecondTokenHandle", "Equal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateToken(jitter):
    """
    NTSTATUS NtCreateToken(
        PHANDLE TokenHandle,
        [TOKEN_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        TOKEN_TYPE TokenType,
        PLUID AuthenticationId,
        PLARGE_INTEGER ExpirationTime,
        PTOKEN_USER TokenUser,
        PTOKEN_GROUPS TokenGroups,
        PTOKEN_PRIVILEGES TokenPrivileges,
        PTOKEN_OWNER TokenOwner,
        PTOKEN_PRIMARY_GROUP TokenPrimaryGroup,
        PTOKEN_DEFAULT_DACL TokenDefaultDacl,
        PTOKEN_SOURCE TokenSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "DesiredAccess", "ObjectAttributes", "TokenType", "AuthenticationId", "ExpirationTime", "TokenUser", "TokenGroups", "TokenPrivileges", "TokenOwner", "TokenPrimaryGroup", "TokenDefaultDacl", "TokenSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDuplicateToken(jitter):
    """
    NTSTATUS NtDuplicateToken(
        HANDLE ExistingTokenHandle,
        [TOKEN_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        BOOLEAN EffectiveOnly,
        TOKEN_TYPE TokenType,
        PHANDLE NewTokenHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExistingTokenHandle", "DesiredAccess", "ObjectAttributes", "EffectiveOnly", "TokenType", "NewTokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtImpersonateAnonymousToken(jitter):
    """
    NTSTATUS NtImpersonateAnonymousToken(
        HANDLE Thread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Thread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenObjectAuditAlarm(jitter):
    """
    NTSTATUS NtOpenObjectAuditAlarm(
        PUNICODE_STRING SubsystemName,
        PVOID HandleId,
        PUNICODE_STRING ObjectTypeName,
        PUNICODE_STRING ObjectName,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        HANDLE ClientToken,
        ULONG DesiredAccess,
        ULONG GrantedAccess,
        PPRIVILEGE_SET Privileges,
        BOOLEAN ObjectCreation,
        BOOLEAN AccessGranted,
        PBOOLEAN GenerateOnClose
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ObjectTypeName", "ObjectName", "SecurityDescriptor", "ClientToken", "DesiredAccess", "GrantedAccess", "Privileges", "ObjectCreation", "AccessGranted", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCloseObjectAuditAlarm(jitter):
    """
    NTSTATUS NtCloseObjectAuditAlarm(
        PUNICODE_STRING SubsystemName,
        PVOID HandleId,
        BOOLEAN GenerateOnClose
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDeleteObjectAuditAlarm(jitter):
    """
    NTSTATUS NtDeleteObjectAuditAlarm(
        PUNICODE_STRING SubsystemName,
        PVOID HandleId,
        BOOLEAN GenerateOnClose
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenProcessToken(jitter):
    """
    NTSTATUS NtOpenProcessToken(
        [ProcessHandle] ProcessHandle,
        [TOKEN_ACCESS_MASK] DesiredAccess,
        PHANDLE TokenHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "DesiredAccess", "TokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenProcessTokenEx(jitter):
    """
    NTSTATUS NtOpenProcessTokenEx(
        [ProcessHandle] ProcessHandle,
        [TOKEN_ACCESS_MASK] DesiredAccess,
        ULONG HandleAttributes,
        PHANDLE TokenHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "DesiredAccess", "HandleAttributes", "TokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPrivilegeCheck(jitter):
    """
    NTSTATUS NtPrivilegeCheck(
        HANDLE ClientToken,
        PPRIVILEGE_SET RequiredPrivileges,
        PBOOLEAN Result
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientToken", "RequiredPrivileges", "Result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPrivilegedServiceAuditAlarm(jitter):
    """
    NTSTATUS NtPrivilegedServiceAuditAlarm(
        PUNICODE_STRING SubsystemName,
        PUNICODE_STRING ServiceName,
        HANDLE ClientToken,
        PPRIVILEGE_SET Privileges,
        BOOLEAN AccessGranted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "ServiceName", "ClientToken", "Privileges", "AccessGranted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPrivilegeObjectAuditAlarm(jitter):
    """
    NTSTATUS NtPrivilegeObjectAuditAlarm(
        PUNICODE_STRING SubsystemName,
        PVOID HandleId,
        HANDLE ClientToken,
        ULONG DesiredAccess,
        PPRIVILEGE_SET Privileges,
        BOOLEAN AccessGranted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ClientToken", "DesiredAccess", "Privileges", "AccessGranted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationToken(jitter):
    """
    NTSTATUS NtQueryInformationToken(
        HANDLE TokenHandle,
        TOKEN_INFORMATION_CLASS TokenInformationClass,
        PVOID TokenInformation,
        ULONG TokenInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "TokenInformationClass", "TokenInformation", "TokenInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAccessCheckByTypeAndAuditAlarm(jitter):
    """
    NTSTATUS NtAccessCheckByTypeAndAuditAlarm(
        PUNICODE_STRING SubsystemName,
        HANDLE HandleId,
        PUNICODE_STRING ObjectTypeName,
        PUNICODE_STRING ObjectName,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID PrincipalSelfSid,
        ACCESS_MASK DesiredAccess,
        AUDIT_EVENT_TYPE AuditType,
        ULONG Flags,
        POBJECT_TYPE_LIST ObjectTypeList,
        ULONG ObjectTypeLength,
        PGENERIC_MAPPING GenericMapping,
        BOOLEAN ObjectCreation,
        PACCESS_MASK GrantedAccess,
        PNTSTATUS AccessStatus,
        PBOOLEAN GenerateOnClose
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ObjectTypeName", "ObjectName", "SecurityDescriptor", "PrincipalSelfSid", "DesiredAccess", "AuditType", "Flags", "ObjectTypeList", "ObjectTypeLength", "GenericMapping", "ObjectCreation", "GrantedAccess", "AccessStatus", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAccessCheckByTypeResultListAndAuditAlarm(jitter):
    """
    NTSTATUS NtAccessCheckByTypeResultListAndAuditAlarm(
        PUNICODE_STRING SubsystemName,
        HANDLE HandleId,
        PUNICODE_STRING ObjectTypeName,
        PUNICODE_STRING ObjectName,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID PrincipalSelfSid,
        ACCESS_MASK DesiredAccess,
        AUDIT_EVENT_TYPE AuditType,
        ULONG Flags,
        POBJECT_TYPE_LIST ObjectTypeList,
        ULONG ObjectTypeLength,
        PGENERIC_MAPPING GenericMapping,
        BOOLEAN ObjectCreation,
        PACCESS_MASK GrantedAccess,
        PNTSTATUS AccessStatus,
        PBOOLEAN GenerateOnClose
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ObjectTypeName", "ObjectName", "SecurityDescriptor", "PrincipalSelfSid", "DesiredAccess", "AuditType", "Flags", "ObjectTypeList", "ObjectTypeLength", "GenericMapping", "ObjectCreation", "GrantedAccess", "AccessStatus", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAccessCheckByTypeResultListAndAuditAlarmByHandle(jitter):
    """
    NTSTATUS NtAccessCheckByTypeResultListAndAuditAlarmByHandle(
        PUNICODE_STRING SubsystemName,
        HANDLE HandleId,
        HANDLE ClientToken,
        PUNICODE_STRING ObjectTypeName,
        PUNICODE_STRING ObjectName,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID PrincipalSelfSid,
        ACCESS_MASK DesiredAccess,
        AUDIT_EVENT_TYPE AuditType,
        ULONG Flags,
        POBJECT_TYPE_LIST ObjectTypeList,
        ULONG ObjectTypeLength,
        PGENERIC_MAPPING GenericMapping,
        BOOLEAN ObjectCreation,
        PACCESS_MASK GrantedAccess,
        PNTSTATUS AccessStatus,
        PBOOLEAN GenerateOnClose
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubsystemName", "HandleId", "ClientToken", "ObjectTypeName", "ObjectName", "SecurityDescriptor", "PrincipalSelfSid", "DesiredAccess", "AuditType", "Flags", "ObjectTypeList", "ObjectTypeLength", "GenericMapping", "ObjectCreation", "GrantedAccess", "AccessStatus", "GenerateOnClose"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationToken(jitter):
    """
    NTSTATUS NtSetInformationToken(
        HANDLE TokenHandle,
        TOKEN_INFORMATION_CLASS TokenInformationClass,
        PVOID TokenInformation,
        ULONG TokenInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TokenHandle", "TokenInformationClass", "TokenInformation", "TokenInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtImpersonateThread(jitter):
    """
    NTSTATUS NtImpersonateThread(
        [ThreadHandle] ThreadHandle,
        HANDLE ThreadToImpersonate,
        PSECURITY_QUALITY_OF_SERVICE SecurityQualityOfService
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "ThreadToImpersonate", "SecurityQualityOfService"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateProcess(jitter):
    """
    NTSTATUS NtCreateProcess(
        PHANDLE ProcessHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        HANDLE ParentProcess,
        BOOLEAN InheritObjectTable,
        HANDLE SectionHandle,
        HANDLE DebugPort,
        HANDLE ExceptionPort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "DesiredAccess", "ObjectAttributes", "ParentProcess", "InheritObjectTable", "SectionHandle", "DebugPort", "ExceptionPort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateProcessEx(jitter):
    """
    NTSTATUS NtCreateProcessEx(
        PHANDLE ProcessHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        HANDLE ParentProcess,
        ULONG Flags,
        HANDLE SectionHandle,
        HANDLE DebugPort,
        HANDLE ExceptionPort,
        BOOLEAN InJob
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "DesiredAccess", "ObjectAttributes", "ParentProcess", "Flags", "SectionHandle", "DebugPort", "ExceptionPort", "InJob"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateThread(jitter):
    """
    NTSTATUS NtCreateThread(
        PHANDLE ThreadHandle,
        [THREAD_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        [ProcessHandle] ProcessHandle,
        PCLIENT_ID ClientId,
        PCONTEXT ThreadContext,
        PINITIAL_TEB UserStack,
        BOOLEAN CreateSuspended
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "DesiredAccess", "ObjectAttributes", "ProcessHandle", "ClientId", "ThreadContext", "UserStack", "CreateSuspended"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateThreadEx(jitter):
    """
    NTSTATUS NtCreateThreadEx(
        PHANDLE ThreadHandle,
        [THREAD_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        [ProcessHandle] ProcessHandle,
        PTHREAD_START_ROUTINE StartAddress,
        PVOID Parameter,
        BOOLEAN CreateSuspended,
        ULONG StackZeroBits,
        SIZE_T StackCommit,
        SIZE_T StackReserve,
        PTHREADEX_DATA pThreadExData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "DesiredAccess", "ObjectAttributes", "ProcessHandle", "StartAddress", "Parameter", "CreateSuspended", "StackZeroBits", "StackCommit", "StackReserve", "pThreadExData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenJobObject(jitter):
    """
    NTSTATUS NtOpenJobObject(
        PHANDLE JobHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["JobHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAssignProcessToJobObject(jitter):
    """
    NTSTATUS NtAssignProcessToJobObject(
        HANDLE JobHandle,
        [ProcessHandle] ProcessHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["JobHandle", "ProcessHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateJobObject(jitter):
    """
    NTSTATUS NtCreateJobObject(
        PHANDLE JobHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["JobHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateJobSet(jitter):
    """
    NTSTATUS NtCreateJobSet(
        ULONG NumJob,
        PJOB_SET_ARRAY UserJobSet,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NumJob", "UserJobSet", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationJobObject(jitter):
    """
    NTSTATUS NtQueryInformationJobObject(
        HANDLE JobHandle,
        JOBOBJECTINFOCLASS JobInformationClass,
        PVOID JobInformation,
        ULONG JobInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["JobHandle", "JobInformationClass", "JobInformation", "JobInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationProcess(jitter):
    """
    NTSTATUS NtQueryInformationProcess(
        [ProcessHandle] ProcessHandle,
        PROCESSINFOCLASS ProcessInformationClass,
        PVOID ProcessInformation,
        ULONG ProcessInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "ProcessInformationClass", "ProcessInformation", "ProcessInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationThread(jitter):
    """
    NTSTATUS NtQueryInformationThread(
        [ThreadHandle] ThreadHandle,
        THREADINFOCLASS ThreadInformationClass,
        PVOID ThreadInformation,
        ULONG ThreadInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "ThreadInformationClass", "ThreadInformation", "ThreadInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationJobObject(jitter):
    """
    NTSTATUS NtSetInformationJobObject(
        HANDLE JobHandle,
        JOBOBJECTINFOCLASS JobInformationClass,
        PVOID JobInformation,
        ULONG JobInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["JobHandle", "JobInformationClass", "JobInformation", "JobInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationProcess(jitter):
    """
    NTSTATUS NtSetInformationProcess(
        [ProcessHandle] ProcessHandle,
        PROCESSINFOCLASS ProcessInformationClass,
        PVOID ProcessInformation,
        ULONG ProcessInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "ProcessInformationClass", "ProcessInformation", "ProcessInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationThread(jitter):
    """
    NTSTATUS NtSetInformationThread(
        [ThreadHandle] ThreadHandle,
        THREADINFOCLASS ThreadInformationClass,
        PVOID ThreadInformation,
        ULONG ThreadInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "ThreadInformationClass", "ThreadInformation", "ThreadInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSuspendProcess(jitter):
    """
    NTSTATUS NtSuspendProcess(
        [ProcessHandle] ProcessHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSuspendThread(jitter):
    """
    NTSTATUS NtSuspendThread(
        [ThreadHandle] ThreadHandle,
        PULONG PreviousSuspendCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "PreviousSuspendCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtTerminateThread(jitter):
    """
    NTSTATUS NtTerminateThread(
        [ThreadHandle] ThreadHandle,
        NTSTATUS ExitStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "ExitStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtTerminateJobObject(jitter):
    """
    NTSTATUS NtTerminateJobObject(
        HANDLE JobHandle,
        NTSTATUS ExitStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["JobHandle", "ExitStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtIsProcessInJob(jitter):
    """
    NTSTATUS NtIsProcessInJob(
        [ProcessHandle] ProcessHandle,
        HANDLE JobHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "JobHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenProcess(jitter):
    """
    NTSTATUS NtOpenProcess(
        PHANDLE ProcessHandle,
        [PROCESS_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PCLIENT_ID ClientId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "DesiredAccess", "ObjectAttributes", "ClientId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenThread(jitter):
    """
    NTSTATUS NtOpenThread(
        PHANDLE ThreadHandle,
        [THREAD_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PCLIENT_ID ClientId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "DesiredAccess", "ObjectAttributes", "ClientId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtResumeThread(jitter):
    """
    NTSTATUS NtResumeThread(
        [ThreadHandle] ThreadHandle,
        PULONG SuspendCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "SuspendCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtResumeProcess(jitter):
    """
    NTSTATUS NtResumeProcess(
        [ProcessHandle] ProcessHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDelayExecution(jitter):
    """
    NTSTATUS NtDelayExecution(
        BOOLEAN Alertable,
        PLARGE_INTEGER DelayInterval
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Alertable", "DelayInterval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtYieldExecution(jitter):
    """
    NTSTATUS NtYieldExecution()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAlertResumeThread(jitter):
    """
    NTSTATUS NtAlertResumeThread(
        [ThreadHandle] ThreadHandle,
        PULONG SuspendCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "SuspendCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAlertThread(jitter):
    """
    NTSTATUS NtAlertThread(
        [ThreadHandle] ThreadHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueueApcThread(jitter):
    """
    NTSTATUS NtQueueApcThread(
        [ThreadHandle] ThreadHandle,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcRoutineContext,
        PIO_STATUS_BLOCK ApcStatusBlock,
        ULONG ApcReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "ApcRoutine", "ApcRoutineContext", "ApcStatusBlock", "ApcReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCurrentTeb(jitter):
    """
    PTEB NtCurrentTeb()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetHighWaitLowThread(jitter):
    """
    NTSTATUS NtSetHighWaitLowThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetLowWaitHighThread(jitter):
    """
    NTSTATUS NtSetLowWaitHighThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtGetCurrentProcessorNumber(jitter):
    """
    ULONG NtGetCurrentProcessorNumber()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtTestAlert(jitter):
    """
    NTSTATUS NtTestAlert()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateUserProcess(jitter):
    """
    NTSTATUS NtCreateUserProcess(
        PHANDLE ProcessHandle,
        PHANDLE ThreadHandle,
        [PROCESS_ACCESS_MASK] ProcessDesiredAccess,
        [THREAD_ACCESS_MASK] ThreadDesiredAccess,
        POBJECT_ATTRIBUTES ProcessObjectAttributes,
        POBJECT_ATTRIBUTES ThreadObjectAttributes,
        ULONG CreateProcessFlags,
        ULONG CreateThreadFlags,
        PRTL_USER_PROCESS_PARAMETERS ProcessParameters,
        PVOID Unknown,
        PVOID AttributeList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "ThreadHandle", "ProcessDesiredAccess", "ThreadDesiredAccess", "ProcessObjectAttributes", "ThreadObjectAttributes", "CreateProcessFlags", "CreateThreadFlags", "ProcessParameters", "Unknown", "AttributeList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtEnumerateSystemEnvironmentValuesEx(jitter):
    """
    NTSTATUS NtEnumerateSystemEnvironmentValuesEx(
        ULONG InformationClass,
        PVOID Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InformationClass", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQuerySystemEnvironmentValue(jitter):
    """
    NTSTATUS NtQuerySystemEnvironmentValue(
        PUNICODE_STRING Name,
        PWSTR Value,
        ULONG Length,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "Value", "Length", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQuerySystemEnvironmentValueEx(jitter):
    """
    NTSTATUS NtQuerySystemEnvironmentValueEx(
        PUNICODE_STRING VariableName,
        LPGUID VendorGuid,
        PVOID Value,
        PULONG ReturnLength,
        PULONG Attributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VariableName", "VendorGuid", "Value", "ReturnLength", "Attributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetSystemEnvironmentValue(jitter):
    """
    NTSTATUS NtSetSystemEnvironmentValue(
        PUNICODE_STRING VariableName,
        PUNICODE_STRING Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VariableName", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetSystemEnvironmentValueEx(jitter):
    """
    NTSTATUS NtSetSystemEnvironmentValueEx(
        PUNICODE_STRING VariableName,
        LPGUID VendorGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VariableName", "VendorGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAllocateVirtualMemory(jitter):
    """
    NTSTATUS NtAllocateVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID* BaseAddress,
        ULONG_PTR ZeroBits,
        PSIZE_T RegionSize,
        [MemoryAllocationFlags] AllocationType,
        [NtProtectionFlags] Protect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "ZeroBits", "RegionSize", "AllocationType", "Protect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFlushVirtualMemory(jitter):
    """
    NTSTATUS NtFlushVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID* BaseAddress,
        PSIZE_T RegionSize,
        PIO_STATUS_BLOCK IoStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "RegionSize", "IoStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFreeVirtualMemory(jitter):
    """
    NTSTATUS NtFreeVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID* BaseAddress,
        PSIZE_T RegionSize,
        [MemoryAllocationFlags] FreeType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "RegionSize", "FreeType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtLockVirtualMemory(jitter):
    """
    NTSTATUS NtLockVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID BaseAddress,
        SIZE_T NumberOfBytesToLock,
        PSIZE_T NumberOfBytesLocked
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "NumberOfBytesToLock", "NumberOfBytesLocked"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtProtectVirtualMemory(jitter):
    """
    NTSTATUS NtProtectVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID* BaseAddress,
        SIZE_T* NumberOfBytesToProtect,
        [NtProtectionFlags] NewAccessProtection,
        [NtProtectionFlags*] OldAccessProtection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "NumberOfBytesToProtect", "NewAccessProtection", "OldAccessProtection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryVirtualMemory(jitter):
    """
    NTSTATUS NtQueryVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID Address,
        MEMORY_INFORMATION_CLASS VirtualMemoryInformationClass,
        PVOID VirtualMemoryInformation,
        SIZE_T Length,
        PSIZE_T ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "Address", "VirtualMemoryInformationClass", "VirtualMemoryInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReadVirtualMemory(jitter):
    """
    NTSTATUS NtReadVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID BaseAddress,
        PVOID Buffer,
        SIZE_T NumberOfBytesToRead,
        PSIZE_T NumberOfBytesRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "Buffer", "NumberOfBytesToRead", "NumberOfBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtUnlockVirtualMemory(jitter):
    """
    NTSTATUS NtUnlockVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID BaseAddress,
        SIZE_T NumberOfBytesToUnlock,
        PSIZE_T NumberOfBytesUnlocked
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "NumberOfBytesToUnlock", "NumberOfBytesUnlocked"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWriteVirtualMemory(jitter):
    """
    NTSTATUS NtWriteVirtualMemory(
        [ProcessHandle] ProcessHandle,
        PVOID BaseAddress,
        PVOID Buffer,
        SIZE_T NumberOfBytesToWrite,
        PSIZE_T NumberOfBytesWritten
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "Buffer", "NumberOfBytesToWrite", "NumberOfBytesWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAllocateUserPhysicalPages(jitter):
    """
    NTSTATUS NtAllocateUserPhysicalPages(
        [ProcessHandle] ProcessHandle,
        PULONG_PTR NumberOfPages,
        PULONG_PTR UserPfnArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "NumberOfPages", "UserPfnArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFreeUserPhysicalPages(jitter):
    """
    NTSTATUS NtFreeUserPhysicalPages(
        [ProcessHandle] ProcessHandle,
        PULONG_PTR NumberOfPages,
        PULONG_PTR UserPfnArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "NumberOfPages", "UserPfnArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtMapUserPhysicalPages(jitter):
    """
    NTSTATUS NtMapUserPhysicalPages(
        PVOID VirtualAddresses,
        ULONG_PTR NumberOfPages,
        PULONG_PTR UserPfnArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualAddresses", "NumberOfPages", "UserPfnArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtMapUserPhysicalPagesScatter(jitter):
    """
    NTSTATUS NtMapUserPhysicalPagesScatter(
        PVOID* VirtualAddresses,
        ULONG_PTR NumberOfPages,
        PULONG_PTR UserPfnArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VirtualAddresses", "NumberOfPages", "UserPfnArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtGetWriteWatch(jitter):
    """
    NTSTATUS NtGetWriteWatch(
        [ProcessHandle] ProcessHandle,
        ULONG Flags,
        PVOID BaseAddress,
        SIZE_T RegionSize,
        PVOID* UserAddressArray,
        PULONG_PTR EntriesInUserAddressArray,
        PULONG Granularity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "Flags", "BaseAddress", "RegionSize", "UserAddressArray", "EntriesInUserAddressArray", "Granularity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtResetWriteWatch(jitter):
    """
    NTSTATUS NtResetWriteWatch(
        [ProcessHandle] ProcessHandle,
        PVOID BaseAddress,
        SIZE_T RegionSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "RegionSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCancelIoFile(jitter):
    """
    NTSTATUS NtCancelIoFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateFile(jitter):
    """
    NTSTATUS NtCreateFile(
        PHANDLE FileHandle,
        [FILE_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PIO_STATUS_BLOCK IoStatusBlock,
        PLARGE_INTEGER AllocationSize,
        [FILE_ATTRIBUTES_ULONG] FileAttributes,
        [FILE_SHARE_MODE] ShareAccess,
        [NtCreateDisposition] CreateDisposition,
        [NtCreateOptions] CreateOptions,
        PVOID EaBuffer,
        ULONG EaLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "DesiredAccess", "ObjectAttributes", "IoStatusBlock", "AllocationSize", "FileAttributes", "ShareAccess", "CreateDisposition", "CreateOptions", "EaBuffer", "EaLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateIoCompletion(jitter):
    """
    NTSTATUS NtCreateIoCompletion(
        PHANDLE IoCompletionHandle,
        [IO_COMPLETION_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG NumberOfConcurrentThreads
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IoCompletionHandle", "DesiredAccess", "ObjectAttributes", "NumberOfConcurrentThreads"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenFile(jitter):
    """
    NTSTATUS NtOpenFile(
        PHANDLE FileHandle,
        [FILE_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PIO_STATUS_BLOCK IoStatusBlock,
        [FILE_SHARE_MODE] ShareAccess,
        [NtCreateOptions] OpenOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "DesiredAccess", "ObjectAttributes", "IoStatusBlock", "ShareAccess", "OpenOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenIoCompletion(jitter):
    """
    NTSTATUS NtOpenIoCompletion(
        PHANDLE CompetionPort,
        [IO_COMPLETION_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CompetionPort", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryIoCompletion(jitter):
    """
    NTSTATUS NtQueryIoCompletion(
        HANDLE IoCompletionHandle,
        IO_COMPLETION_INFORMATION_CLASS IoCompletionInformationClass,
        PVOID IoCompletionInformation,
        ULONG IoCompletionInformationLength,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IoCompletionHandle", "IoCompletionInformationClass", "IoCompletionInformation", "IoCompletionInformationLength", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRemoveIoCompletion(jitter):
    """
    NTSTATUS NtRemoveIoCompletion(
        HANDLE IoCompletionHandle,
        PVOID* CompletionKey,
        PVOID* CompletionContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        PLARGE_INTEGER Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IoCompletionHandle", "CompletionKey", "CompletionContext", "IoStatusBlock", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetIoCompletion(jitter):
    """
    NTSTATUS NtSetIoCompletion(
        HANDLE IoCompletionPortHandle,
        PVOID CompletionKey,
        PVOID CompletionContext,
        NTSTATUS CompletionStatus,
        ULONG CompletionInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IoCompletionPortHandle", "CompletionKey", "CompletionContext", "CompletionStatus", "CompletionInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateSymbolicLinkObject(jitter):
    """
    NTSTATUS NtCreateSymbolicLinkObject(
        PHANDLE SymbolicLinkHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PUNICODE_STRING Name
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SymbolicLinkHandle", "DesiredAccess", "ObjectAttributes", "Name"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenSymbolicLinkObject(jitter):
    """
    NTSTATUS NtOpenSymbolicLinkObject(
        PHANDLE SymbolicLinkHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SymbolicLinkHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQuerySymbolicLinkObject(jitter):
    """
    NTSTATUS NtQuerySymbolicLinkObject(
        HANDLE SymLinkObjHandle,
        PUNICODE_STRING LinkTarget,
        PULONG DataWritten
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SymLinkObjHandle", "LinkTarget", "DataWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDeleteFile(jitter):
    """
    NTSTATUS NtDeleteFile(
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryFullAttributesFile(jitter):
    """
    NTSTATUS NtQueryFullAttributesFile(
        POBJECT_ATTRIBUTES ObjectAttributes,
        PFILE_NETWORK_OPEN_INFORMATION FileInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectAttributes", "FileInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationFile(jitter):
    """
    NTSTATUS NtQueryInformationFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID FileInformation,
        ULONG Length,
        FILE_INFORMATION_CLASS FileInformationClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "FileInformation", "Length", "FileInformationClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtLockFile(jitter):
    """
    NTSTATUS NtLockFile(
        HANDLE FileHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        PLARGE_INTEGER ByteOffset,
        PLARGE_INTEGER Length,
        ULONG Key,
        BOOLEAN FailImmediatedly,
        BOOLEAN ExclusiveLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "ByteOffset", "Length", "Key", "FailImmediatedly", "ExclusiveLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtUnlockFile(jitter):
    """
    NTSTATUS NtUnlockFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PLARGE_INTEGER ByteOffset,
        PLARGE_INTEGER Lenght,
        ULONG Key
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "ByteOffset", "Lenght", "Key"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWriteFile(jitter):
    """
    NTSTATUS NtWriteFile(
        HANDLE FileHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID Buffer,
        ULONG Length,
        PLARGE_INTEGER ByteOffset,
        PULONG Key
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "Buffer", "Length", "ByteOffset", "Key"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWriteFileGather(jitter):
    """
    NTSTATUS NtWriteFileGather(
        HANDLE FileHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        FILE_SEGMENT_ELEMENT[] BufferDescription,
        ULONG BufferLength,
        PLARGE_INTEGER ByteOffset,
        PULONG Key
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "BufferDescription", "BufferLength", "ByteOffset", "Key"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReadFile(jitter):
    """
    NTSTATUS NtReadFile(
        HANDLE FileHandle,
        HANDLE Event,
        PIO_APC_ROUTINE UserApcRoutine,
        PVOID UserApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID Buffer,
        ULONG BufferLength,
        PLARGE_INTEGER ByteOffset,
        PULONG Key
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Event", "UserApcRoutine", "UserApcContext", "IoStatusBlock", "Buffer", "BufferLength", "ByteOffset", "Key"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReadFileScatter(jitter):
    """
    NTSTATUS NtReadFileScatter(
        HANDLE FileHandle,
        HANDLE Event,
        PIO_APC_ROUTINE UserApcRoutine,
        PVOID UserApcContext,
        PIO_STATUS_BLOCK UserIoStatusBlock,
        FILE_SEGMENT_ELEMENT[] BufferDescription,
        ULONG BufferLength,
        PLARGE_INTEGER ByteOffset,
        PULONG Key
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Event", "UserApcRoutine", "UserApcContext", "UserIoStatusBlock", "BufferDescription", "BufferLength", "ByteOffset", "Key"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFlushBuffersFile(jitter):
    """
    NTSTATUS NtFlushBuffersFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFlushBuffersFileEx(jitter):
    """
    NTSTATUS NtFlushBuffersFileEx(
        HANDLE FileHandle,
        [FLUSH_FLAGS] Flags,
        PIO_STATUS_BLOCK IoStatusBlock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Flags", "IoStatusBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationFile(jitter):
    """
    NTSTATUS NtSetInformationFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID FileInformation,
        ULONG Length,
        FILE_INFORMATION_CLASS FileInformationClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "FileInformation", "Length", "FileInformationClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryAttributesFile(jitter):
    """
    NTSTATUS NtQueryAttributesFile(
        POBJECT_ATTRIBUTES ObjectAttributes,
        PFILE_BASIC_INFORMATION FileInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectAttributes", "FileInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryEaFile(jitter):
    """
    NTSTATUS NtQueryEaFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID Buffer,
        ULONG Length,
        BOOLEAN ReturnSingleEntry,
        PVOID EaList,
        ULONG EaListLength,
        PULONG EaIndex,
        BOOLEAN RestartScan
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "Buffer", "Length", "ReturnSingleEntry", "EaList", "EaListLength", "EaIndex", "RestartScan"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetEaFile(jitter):
    """
    NTSTATUS NtSetEaFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID EaBuffer,
        ULONG EaBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "EaBuffer", "EaBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryQuotaInformationFile(jitter):
    """
    NTSTATUS NtQueryQuotaInformationFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID Buffer,
        ULONG Length,
        BOOLEAN ReturnSingleEntry,
        PVOID SidList,
        ULONG SidListLength,
        PSID StartSid,
        BOOLEAN RestartScan
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "Buffer", "Length", "ReturnSingleEntry", "SidList", "SidListLength", "StartSid", "RestartScan"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetQuotaInformationFile(jitter):
    """
    NTSTATUS NtSetQuotaInformationFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID Buffer,
        ULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreatePagingFile(jitter):
    """
    NTSTATUS NtCreatePagingFile(
        PUNICODE_STRING FileName,
        PLARGE_INTEGER InitialSize,
        PLARGE_INTEGER MaxiumSize,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "InitialSize", "MaxiumSize", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtTranslateFilePath(jitter):
    """
    NTSTATUS NtTranslateFilePath(
        PFILE_PATH InputFilePath,
        ULONG OutputType,
        PFILE_PATH OutputFilePath,
        ULONG OutputFilePathLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InputFilePath", "OutputType", "OutputFilePath", "OutputFilePathLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateDirectoryObject(jitter):
    """
    NTSTATUS NtCreateDirectoryObject(
        PHANDLE DirectoryHandle,
        [DIRECTORY_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DirectoryHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenDirectoryObject(jitter):
    """
    NTSTATUS NtOpenDirectoryObject(
        PHANDLE FileHandle,
        [DIRECTORY_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryDirectoryObject(jitter):
    """
    NTSTATUS NtQueryDirectoryObject(
        HANDLE DirectoryHandle,
        PVOID Buffer,
        ULONG BufferLength,
        BOOLEAN ReturnSingleEntry,
        BOOLEAN RestartScan,
        PULONG Context,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DirectoryHandle", "Buffer", "BufferLength", "ReturnSingleEntry", "RestartScan", "Context", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtNotifyChangeDirectoryFile(jitter):
    """
    NTSTATUS NtNotifyChangeDirectoryFile(
        HANDLE FileHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID Buffer,
        ULONG BufferSize,
        [FILE_NOTIFY_CHANGE_FLAGS] CompletionFilter,
        BOOLEAN WatchTree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "Buffer", "BufferSize", "CompletionFilter", "WatchTree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryDirectoryFile(jitter):
    """
    NTSTATUS NtQueryDirectoryFile(
        HANDLE FileHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID FileInformation,
        ULONG Length,
        FILE_INFORMATION_CLASS FileInformationClass,
        BOOLEAN ReturnSingleEntry,
        PUNICODE_STRING FileName,
        BOOLEAN RestartScan
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "FileInformation", "Length", "FileInformationClass", "ReturnSingleEntry", "FileName", "RestartScan"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryOleDirectoryFile(jitter):
    """
    NTSTATUS NtQueryOleDirectoryFile(
        HANDLE FileHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID FileInformation,
        ULONG Length,
        FILE_INFORMATION_CLASS FileInformationClass,
        BOOLEAN ReturnSingleEntry,
        PUNICODE_STRING FileMask,
        BOOLEAN RestartScan
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "FileInformation", "Length", "FileInformationClass", "ReturnSingleEntry", "FileMask", "RestartScan"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryVolumeInformationFile(jitter):
    """
    NTSTATUS NtQueryVolumeInformationFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID FsInformation,
        ULONG Length,
        FS_INFORMATION_CLASS FsInformationClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "FsInformation", "Length", "FsInformationClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetVolumeInformationFile(jitter):
    """
    NTSTATUS NtSetVolumeInformationFile(
        HANDLE FileHandle,
        PIO_STATUS_BLOCK IoStatusBlock,
        PVOID FsInformation,
        ULONG Length,
        FS_INFORMATION_CLASS FsInformationClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "IoStatusBlock", "FsInformation", "Length", "FsInformationClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateSection(jitter):
    """
    NTSTATUS NtCreateSection(
        PHANDLE SectionHandle,
        [SECTION_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PLARGE_INTEGER MaximumSize,
        [NtProtectionFlags] SectionPageProtection,
        [SECTION_ALLOCATION] AllocationAttributes,
        HANDLE FileHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SectionHandle", "DesiredAccess", "ObjectAttributes", "MaximumSize", "SectionPageProtection", "AllocationAttributes", "FileHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtExtendSection(jitter):
    """
    NTSTATUS NtExtendSection(
        HANDLE SectionHandle,
        PLARGE_INTEGER NewMaximumSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SectionHandle", "NewMaximumSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtMapViewOfSection(jitter):
    """
    NTSTATUS NtMapViewOfSection(
        HANDLE SectionHandle,
        [ProcessHandle] ProcessHandle,
        PVOID* BaseAddress,
        ULONG_PTR ZeroBits,
        SIZE_T CommitSize,
        PLARGE_INTEGER SectionOffset,
        PSIZE_T ViewSize,
        SECTION_INHERIT InheritDisposition,
        [MemoryAllocationFlags] AllocationType,
        [NtProtectionFlags] AccessProtection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SectionHandle", "ProcessHandle", "BaseAddress", "ZeroBits", "CommitSize", "SectionOffset", "ViewSize", "InheritDisposition", "AllocationType", "AccessProtection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenSection(jitter):
    """
    NTSTATUS NtOpenSection(
        PHANDLE SectionHandle,
        [SECTION_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SectionHandle", "DesiredAccess", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQuerySection(jitter):
    """
    NTSTATUS NtQuerySection(
        HANDLE SectionHandle,
        SECTION_INFORMATION_CLASS SectionInformationClass,
        PVOID SectionInformation,
        SIZE_T Length,
        PSIZE_T ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SectionHandle", "SectionInformationClass", "SectionInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtUnmapViewOfSection(jitter):
    """
    NTSTATUS NtUnmapViewOfSection(
        [ProcessHandle] ProcessHandle,
        PVOID BaseAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAcceptConnectPort(jitter):
    """
    NTSTATUS NtAcceptConnectPort(
        PHANDLE PortHandle,
        PVOID PortContext,
        PPORT_MESSAGE ConnectionRequest,
        BOOLEAN AcceptConnection,
        PPORT_VIEW ServerView,
        PREMOTE_PORT_VIEW ClientView
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "PortContext", "ConnectionRequest", "AcceptConnection", "ServerView", "ClientView"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCompleteConnectPort(jitter):
    """
    NTSTATUS NtCompleteConnectPort(
        HANDLE PortHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtConnectPort(jitter):
    """
    NTSTATUS NtConnectPort(
        PHANDLE PortHandle,
        PUNICODE_STRING PortName,
        PSECURITY_QUALITY_OF_SERVICE SecurityQos,
        PPORT_VIEW ClientView,
        PREMOTE_PORT_VIEW ServerView,
        PULONG MaxMessageLength,
        PVOID ConnectionInformation,
        PULONG ConnectionInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "PortName", "SecurityQos", "ClientView", "ServerView", "MaxMessageLength", "ConnectionInformation", "ConnectionInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreatePort(jitter):
    """
    NTSTATUS NtCreatePort(
        PHANDLE PortHandle,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG MaxConnectionInfoLength,
        ULONG MaxMessageLength,
        ULONG MaxPoolUsage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "ObjectAttributes", "MaxConnectionInfoLength", "MaxMessageLength", "MaxPoolUsage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateWaitablePort(jitter):
    """
    NTSTATUS NtCreateWaitablePort(
        PHANDLE PortHandle,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG MaxConnectInfoLength,
        ULONG MaxDataLength,
        ULONG NPMessageQueueSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "ObjectAttributes", "MaxConnectInfoLength", "MaxDataLength", "NPMessageQueueSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtImpersonateClientOfPort(jitter):
    """
    NTSTATUS NtImpersonateClientOfPort(
        HANDLE PortHandle,
        PPORT_MESSAGE ClientMessage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "ClientMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtListenPort(jitter):
    """
    NTSTATUS NtListenPort(
        HANDLE PortHandle,
        PPORT_MESSAGE ConnectionRequest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "ConnectionRequest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationPort(jitter):
    """
    NTSTATUS NtQueryInformationPort(
        HANDLE PortHandle,
        PORT_INFORMATION_CLASS PortInformationClass,
        PVOID PortInformation,
        ULONG PortInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "PortInformationClass", "PortInformation", "PortInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryPortInformationProcess(jitter):
    """
    NTSTATUS NtQueryPortInformationProcess()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReadRequestData(jitter):
    """
    NTSTATUS NtReadRequestData(
        HANDLE PortHandle,
        PPORT_MESSAGE Message,
        ULONG Index,
        PVOID Buffer,
        ULONG BufferLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "Message", "Index", "Buffer", "BufferLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReplyPort(jitter):
    """
    NTSTATUS NtReplyPort(
        HANDLE PortHandle,
        PPORT_MESSAGE LpcReply
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "LpcReply"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReplyWaitReceivePort(jitter):
    """
    NTSTATUS NtReplyWaitReceivePort(
        HANDLE PortHandle,
        PVOID* PortContext,
        PPORT_MESSAGE ReplyMessage,
        PPORT_MESSAGE ReceiveMessage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "PortContext", "ReplyMessage", "ReceiveMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReplyWaitReceivePortEx(jitter):
    """
    NTSTATUS NtReplyWaitReceivePortEx(
        HANDLE PortHandle,
        PVOID* PortContext,
        PPORT_MESSAGE ReplyMessage,
        PPORT_MESSAGE ReceiveMessage,
        PLARGE_INTEGER Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "PortContext", "ReplyMessage", "ReceiveMessage", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReplyWaitReplyPort(jitter):
    """
    NTSTATUS NtReplyWaitReplyPort(
        HANDLE PortHandle,
        PPORT_MESSAGE ReplyMessage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "ReplyMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRequestPort(jitter):
    """
    NTSTATUS NtRequestPort(
        HANDLE PortHandle,
        PPORT_MESSAGE LpcMessage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "LpcMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRequestWaitReplyPort(jitter):
    """
    NTSTATUS NtRequestWaitReplyPort(
        HANDLE PortHandle,
        PPORT_MESSAGE LpcReply,
        PPORT_MESSAGE LpcRequest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "LpcReply", "LpcRequest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSecureConnectPort(jitter):
    """
    NTSTATUS NtSecureConnectPort(
        PHANDLE PortHandle,
        PUNICODE_STRING PortName,
        PSECURITY_QUALITY_OF_SERVICE SecurityQos,
        PPORT_VIEW ClientView,
        PSID Sid,
        PREMOTE_PORT_VIEW ServerView,
        PULONG MaxMessageLength,
        PVOID ConnectionInformation,
        PULONG ConnectionInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "PortName", "SecurityQos", "ClientView", "Sid", "ServerView", "MaxMessageLength", "ConnectionInformation", "ConnectionInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWriteRequestData(jitter):
    """
    NTSTATUS NtWriteRequestData(
        HANDLE PortHandle,
        PPORT_MESSAGE Message,
        ULONG Index,
        PVOID Buffer,
        ULONG BufferLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle", "Message", "Index", "Buffer", "BufferLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetDefaultHardErrorPort(jitter):
    """
    NTSTATUS NtSetDefaultHardErrorPort(
        HANDLE PortHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PortHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRegisterThreadTerminatePort(jitter):
    """
    NTSTATUS NtRegisterThreadTerminatePort(
        HANDLE TerminationPort
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TerminationPort"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAddBootEntry(jitter):
    """
    NTSTATUS NtAddBootEntry(
        PBOOT_ENTRY BootEntry,
        ULONG Id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BootEntry", "Id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAddDriverEntry(jitter):
    """
    NTSTATUS NtAddDriverEntry(
        PEFI_DRIVER_ENTRY BootEntry,
        ULONG Id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BootEntry", "Id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDeleteDriverEntry(jitter):
    """
    NTSTATUS NtDeleteDriverEntry(
        ULONG Id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDeleteBootEntry(jitter):
    """
    NTSTATUS NtDeleteBootEntry(
        ULONG Id
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Id"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtEnumerateBootEntries(jitter):
    """
    NTSTATUS NtEnumerateBootEntries(
        PVOID Buffer,
        PULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtEnumerateDriverEntries(jitter):
    """
    NTSTATUS NtEnumerateDriverEntries(
        PVOID Buffer,
        PULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtLoadDriver(jitter):
    """
    NTSTATUS NtLoadDriver(
        PUNICODE_STRING DriverServiceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DriverServiceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtModifyBootEntry(jitter):
    """
    NTSTATUS NtModifyBootEntry(
        PBOOT_ENTRY BootEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BootEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtModifyDriverEntry(jitter):
    """
    NTSTATUS NtModifyDriverEntry(
        PEFI_DRIVER_ENTRY DriverEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DriverEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryDriverEntryOrder(jitter):
    """
    NTSTATUS NtQueryDriverEntryOrder(
        PULONG Ids,
        PULONG Count
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Ids", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryBootEntryOrder(jitter):
    """
    NTSTATUS NtQueryBootEntryOrder(
        PULONG Ids,
        PULONG Count
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Ids", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryBootOptions(jitter):
    """
    NTSTATUS NtQueryBootOptions(
        PBOOT_OPTIONS BootOptions,
        PULONG BootOptionsLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BootOptions", "BootOptionsLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetBootEntryOrder(jitter):
    """
    NTSTATUS NtSetBootEntryOrder(
        PULONG Ids,
        PULONG Count
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Ids", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetBootOptions(jitter):
    """
    NTSTATUS NtSetBootOptions(
        PBOOT_OPTIONS BootOptions,
        ULONG FieldsToChange
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BootOptions", "FieldsToChange"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetDriverEntryOrder(jitter):
    """
    NTSTATUS NtSetDriverEntryOrder(
        PULONG Ids,
        PULONG Count
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Ids", "Count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtUnloadDriver(jitter):
    """
    NTSTATUS NtUnloadDriver(
        PUNICODE_STRING DriverServiceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DriverServiceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateProfile(jitter):
    """
    NTSTATUS NtCreateProfile(
        PHANDLE ProfileHandle,
        HANDLE Process,
        PVOID ImageBase,
        ULONG ImageSize,
        ULONG BucketSize,
        PVOID Buffer,
        ULONG BufferSize,
        KPROFILE_SOURCE ProfileSource,
        KAFFINITY Affinity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileHandle", "Process", "ImageBase", "ImageSize", "BucketSize", "Buffer", "BufferSize", "ProfileSource", "Affinity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryIntervalProfile(jitter):
    """
    NTSTATUS NtQueryIntervalProfile(
        KPROFILE_SOURCE ProfileSource,
        PULONG Interval
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileSource", "Interval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetIntervalProfile(jitter):
    """
    NTSTATUS NtSetIntervalProfile(
        ULONG Interval,
        KPROFILE_SOURCE Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Interval", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtStartProfile(jitter):
    """
    NTSTATUS NtStartProfile(
        HANDLE ProfileHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtStopProfile(jitter):
    """
    NTSTATUS NtStopProfile(
        HANDLE ProfileHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDebugActiveProcess(jitter):
    """
    NTSTATUS NtDebugActiveProcess(
        HANDLE Process,
        HANDLE DebugObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Process", "DebugObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDebugContinue(jitter):
    """
    NTSTATUS NtDebugContinue(
        HANDLE DebugObject,
        PCLIENT_ID AppClientId,
        NTSTATUS ContinueStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DebugObject", "AppClientId", "ContinueStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtWaitForDebugEvent(jitter):
    """
    NTSTATUS NtWaitForDebugEvent(
        HANDLE DebugObject,
        BOOLEAN Alertable,
        PLARGE_INTEGER Timeout,
        PDBGUI_WAIT_STATE_CHANGE StateChange
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DebugObject", "Alertable", "Timeout", "StateChange"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRemoveProcessDebug(jitter):
    """
    NTSTATUS NtRemoveProcessDebug(
        HANDLE Process,
        HANDLE DebugObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Process", "DebugObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationDebugObject(jitter):
    """
    NTSTATUS NtSetInformationDebugObject(
        HANDLE DebugObject,
        DEBUGOBJECTINFOCLASS InformationClass,
        PVOID Information,
        ULONG InformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DebugObject", "InformationClass", "Information", "InformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateDebugObject(jitter):
    """
    NTSTATUS NtCreateDebugObject(
        PHANDLE DebugHandle,
        [DEBUG_OBJECT_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        BOOLEAN KillProcessOnExit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DebugHandle", "DesiredAccess", "ObjectAttributes", "KillProcessOnExit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtGetContextThread(jitter):
    """
    NTSTATUS NtGetContextThread(
        [ThreadHandle] ThreadHandle,
        PCONTEXT pContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetContextThread(jitter):
    """
    NTSTATUS NtSetContextThread(
        [ThreadHandle] ThreadHandle,
        PCONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtContinue(jitter):
    """
    NTSTATUS NtContinue(
        PCONTEXT ThreadContext,
        BOOLEAN RaiseAlert
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadContext", "RaiseAlert"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFlushInstructionCache(jitter):
    """
    NTSTATUS NtFlushInstructionCache(
        [ProcessHandle] ProcessHandle,
        PVOID BaseAddress,
        ULONG NumberOfBytesToFlush
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "BaseAddress", "NumberOfBytesToFlush"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFlushWriteBuffer(jitter):
    """
    NTSTATUS NtFlushWriteBuffer()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSystemDebugControl(jitter):
    """
    NTSTATUS NtSystemDebugControl(
        SYSDBG_COMMAND ControlCode,
        PVOID InputBuffer,
        ULONG InputBufferLength,
        PVOID OutputBuffer,
        ULONG OutputBufferLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ControlCode", "InputBuffer", "InputBufferLength", "OutputBuffer", "OutputBufferLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQuerySystemTime(jitter):
    """
    NTSTATUS NtQuerySystemTime(
        PLARGE_INTEGER SystemTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetSystemTime(jitter):
    """
    NTSTATUS NtSetSystemTime(
        PLARGE_INTEGER SystemTime,
        PLARGE_INTEGER PreviousTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SystemTime", "PreviousTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtGetTickCount(jitter):
    """
    ULONG NtGetTickCount()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAllocateLocallyUniqueId(jitter):
    """
    NTSTATUS NtAllocateLocallyUniqueId(
        LUID* LocallyUniqueId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LocallyUniqueId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAllocateUuids(jitter):
    """
    NTSTATUS NtAllocateUuids(
        PULARGE_INTEGER Time,
        PULONG Range,
        PULONG Sequence,
        PUCHAR Seed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Time", "Range", "Sequence", "Seed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetUuidSeed(jitter):
    """
    NTSTATUS NtSetUuidSeed(
        PUCHAR UuidSeed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UuidSeed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryDebugFilterState(jitter):
    """
    NTSTATUS NtQueryDebugFilterState(
        ULONG ComponentId,
        ULONG Level
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComponentId", "Level"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetDebugFilterState(jitter):
    """
    NTSTATUS NtSetDebugFilterState(
        ULONG ComponentId,
        ULONG Level,
        BOOLEAN State
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComponentId", "Level", "State"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtApphelpCacheControl(jitter):
    """
    NTSTATUS NtApphelpCacheControl(
        APPHELPCACHESERVICECLASS Service,
        PVOID ServiceData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Service", "ServiceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtAreMappedFilesTheSame(jitter):
    """
    NTSTATUS NtAreMappedFilesTheSame(
        PVOID File1MappedAsAnImage,
        PVOID File2MappedAsFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["File1MappedAsAnImage", "File2MappedAsFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtShutdownSystem(jitter):
    """
    NTSTATUS NtShutdownSystem(
        SHUTDOWN_ACTION Action
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Action"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPowerInformation(jitter):
    """
    NTSTATUS NtPowerInformation(
        POWER_INFORMATION_LEVEL PowerInformationLevel,
        PVOID InputBuffer,
        ULONG InputBufferLength,
        PVOID OutputBuffer,
        ULONG OutputBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PowerInformationLevel", "InputBuffer", "InputBufferLength", "OutputBuffer", "OutputBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetSystemPowerState(jitter):
    """
    NTSTATUS NtSetSystemPowerState(
        POWER_ACTION SystemAction,
        SYSTEM_POWER_STATE MinSystemState,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SystemAction", "MinSystemState", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDisplayString(jitter):
    """
    NTSTATUS NtDisplayString(
        PUNICODE_STRING DisplayString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DisplayString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtInitiatePowerAction(jitter):
    """
    NTSTATUS NtInitiatePowerAction(
        POWER_ACTION SystemAction,
        SYSTEM_POWER_STATE MinSystemState,
        ULONG Flags,
        BOOLEAN Asynchronous
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SystemAction", "MinSystemState", "Flags", "Asynchronous"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryPerformanceCounter(jitter):
    """
    NTSTATUS NtQueryPerformanceCounter(
        PLARGE_INTEGER PerformanceCounter,
        PLARGE_INTEGER PerformanceFrequency
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PerformanceCounter", "PerformanceFrequency"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryTimerResolution(jitter):
    """
    NTSTATUS NtQueryTimerResolution(
        PULONG MinimumResolution,
        PULONG MaximumResolution,
        PULONG CurrentResolution
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MinimumResolution", "MaximumResolution", "CurrentResolution"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateMailslotFile(jitter):
    """
    NTSTATUS NtCreateMailslotFile(
        PHANDLE MailSlotFileHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PIO_STATUS_BLOCK IoStatusBlock,
        ULONG FileAttributes,
        [FILE_SHARE_MODE] ShareAccess,
        ULONG MaxMessageSize,
        PLARGE_INTEGER TimeOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MailSlotFileHandle", "DesiredAccess", "ObjectAttributes", "IoStatusBlock", "FileAttributes", "ShareAccess", "MaxMessageSize", "TimeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateNamedPipeFile(jitter):
    """
    NTSTATUS NtCreateNamedPipeFile(
        PHANDLE NamedPipeFileHandle,
        [PIPE_ACCESS_MASK] DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PIO_STATUS_BLOCK IoStatusBlock,
        [FILE_SHARE_MODE] ShareAccess,
        [NtCreateDisposition] CreateDisposition,
        [NtCreateOptions] CreateOptions,
        ULONG WriteModeMessage,
        ULONG ReadModeMessage,
        ULONG NonBlocking,
        ULONG MaxInstances,
        ULONG InBufferSize,
        ULONG OutBufferSize,
        PLARGE_INTEGER DefaultTimeOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NamedPipeFileHandle", "DesiredAccess", "ObjectAttributes", "IoStatusBlock", "ShareAccess", "CreateDisposition", "CreateOptions", "WriteModeMessage", "ReadModeMessage", "NonBlocking", "MaxInstances", "InBufferSize", "OutBufferSize", "DefaultTimeOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDeviceIoControlFile(jitter):
    """
    NTSTATUS NtDeviceIoControlFile(
        HANDLE DeviceHandle,
        HANDLE Event,
        PIO_APC_ROUTINE UserApcRoutine,
        PVOID UserApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        [IOCTL] IoControlCode,
        PVOID InputBuffer,
        ULONG InputBufferSize,
        PVOID OutputBuffer,
        ULONG OutputBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceHandle", "Event", "UserApcRoutine", "UserApcContext", "IoStatusBlock", "IoControlCode", "InputBuffer", "InputBufferSize", "OutputBuffer", "OutputBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFsControlFile(jitter):
    """
    NTSTATUS NtFsControlFile(
        HANDLE DeviceHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        PIO_STATUS_BLOCK IoStatusBlock,
        ULONG IoControlCode,
        PVOID InputBuffer,
        ULONG InputBufferSize,
        PVOID OutputBuffer,
        ULONG OutputBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceHandle", "Event", "ApcRoutine", "ApcContext", "IoStatusBlock", "IoControlCode", "InputBuffer", "InputBufferSize", "OutputBuffer", "OutputBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPlugPlayControl(jitter):
    """
    NTSTATUS NtPlugPlayControl(
        PLUGPLAY_CONTROL_CLASS PlugPlayControlClass,
        PVOID Buffer,
        ULONG BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PlugPlayControlClass", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtGetPlugPlayEvent(jitter):
    """
    NTSTATUS NtGetPlugPlayEvent(
        ULONG Reserved1,
        ULONG Reserved2,
        PPLUGPLAY_EVENT_BLOCK Buffer,
        ULONG BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Reserved1", "Reserved2", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtLockProductActivationKeys(jitter):
    """
    NTSTATUS NtLockProductActivationKeys(
        PULONG pPrivateVer,
        PULONG pSafeMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPrivateVer", "pSafeMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetTimerResolution(jitter):
    """
    NTSTATUS NtSetTimerResolution(
        ULONG DesiredResolution,
        BOOLEAN SetResolution,
        PULONG CurrentResolution
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DesiredResolution", "SetResolution", "CurrentResolution"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQuerySystemInformation(jitter):
    """
    NTSTATUS NtQuerySystemInformation(
        SYSTEM_INFORMATION_CLASS SystemInformationClass,
        PVOID SystemInformation,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SystemInformationClass", "SystemInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetSystemInformation(jitter):
    """
    NTSTATUS NtSetSystemInformation(
        SYSTEM_INFORMATION_CLASS SystemInformationClass,
        PVOID SystemInformation,
        ULONG SystemInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SystemInformationClass", "SystemInformation", "SystemInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRaiseHardError(jitter):
    """
    NTSTATUS NtRaiseHardError(
        NTSTATUS ErrorStatus,
        ULONG NumberOfParameters,
        ULONG UnicodeStringParameterMask,
        PULONG_PTR Parameters,
        ULONG ValidResponseOptions,
        PULONG Response
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ErrorStatus", "NumberOfParameters", "UnicodeStringParameterMask", "Parameters", "ValidResponseOptions", "Response"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtClose(jitter):
    """
    NTSTATUS NtClose(
        HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtDuplicateObject(jitter):
    """
    NTSTATUS NtDuplicateObject(
        [ProcessHandle] SourceProcessHandle,
        HANDLE SourceHandle,
        [ProcessHandle] TargetProcessHandle,
        PHANDLE TargetHandle,
        ACCESS_MASK DesiredAccess,
        ULONG HandleAttributes,
        ULONG Options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceProcessHandle", "SourceHandle", "TargetProcessHandle", "TargetHandle", "DesiredAccess", "HandleAttributes", "Options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtMakePermanentObject(jitter):
    """
    NTSTATUS NtMakePermanentObject(
        HANDLE Object
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtMakeTemporaryObject(jitter):
    """
    NTSTATUS NtMakeTemporaryObject(
        HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryObject(jitter):
    """
    NTSTATUS NtQueryObject(
        HANDLE ObjectHandle,
        OBJECT_INFORMATION_CLASS ObjectInformationClass,
        PVOID ObjectInformation,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectHandle", "ObjectInformationClass", "ObjectInformation", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQuerySecurityObject(jitter):
    """
    NTSTATUS NtQuerySecurityObject(
        HANDLE Handle,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        ULONG Length,
        PULONG ResultLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "SecurityInformation", "SecurityDescriptor", "Length", "ResultLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationObject(jitter):
    """
    NTSTATUS NtSetInformationObject(
        HANDLE ObjectHandle,
        OBJECT_INFORMATION_CLASS ObjectInformationClass,
        PVOID ObjectInformation,
        ULONG Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectHandle", "ObjectInformationClass", "ObjectInformation", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetSecurityObject(jitter):
    """
    NTSTATUS NtSetSecurityObject(
        HANDLE Handle,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "SecurityInformation", "SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAppendPathElement(jitter):
    """
    NTSTATUS RtlAppendPathElement(
        [RTL_APE_FLAGS] flags,
        PRTL_UNICODE_STRING_BUFFER pStrBuffer,
        PCUNICODE_STRING pAddend
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "pStrBuffer", "pAddend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopyMappedMemory(jitter):
    """
    NTSTATUS RtlCopyMappedMemory(
        void* pDest,
        const void* pSrc,
        SIZE_T bytesToCopy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDest", "pSrc", "bytesToCopy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDumpResource(jitter):
    """
    VOID RtlDumpResource(
        PRTL_RESOURCE pResource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetLengthWithoutLastFullDosOrNtPathElement(jitter):
    """
    NTSTATUS RtlGetLengthWithoutLastFullDosOrNtPathElement(
        ULONG flags,
        PUNICODE_STRING pStr,
        PULONG pOutLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "pStr", "pOutLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlMultiAppendUnicodeStringBuffer(jitter):
    """
    NTSTATUS RtlMultiAppendUnicodeStringBuffer(
        PRTL_UNICODE_STRING_BUFFER pStrBuffer,
        ULONG numAddends,
        PCUNICODE_STRING pAddends
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStrBuffer", "numAddends", "pAddends"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTraceDatabaseAdd(jitter):
    """
    BOOLEAN RtlTraceDatabaseAdd(
        PRTL_TRACE_DATABASE pDatabase,
        ULONG numFrames,
        PVOID* ppFrames,
        PRTL_TRACE_BLOCK* ppBlock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDatabase", "numFrames", "ppFrames", "ppBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTraceDatabaseCreate(jitter):
    """
    PRTL_TRACE_DATABASE RtlTraceDatabaseCreate(
        ULONG buckets,
        SIZE_T maximumSize,
        ULONG flags,
        ULONG tag,
        PRTL_TRACE_HASH_FUNCTION pfnHash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["buckets", "maximumSize", "flags", "tag", "pfnHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTraceDatabaseDestroy(jitter):
    """
    BOOLEAN RtlTraceDatabaseDestroy(
        PRTL_TRACE_DATABASE pDatabase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTraceDatabaseEnumerate(jitter):
    """
    BOOLEAN RtlTraceDatabaseEnumerate(
        PRTL_TRACE_DATABASE pDatabase,
        PRTL_TRACE_ENUM pEnumData,
        PRTL_TRACE_BLOCK* ppBlock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDatabase", "pEnumData", "ppBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTraceDatabaseFind(jitter):
    """
    BOOLEAN RtlTraceDatabaseFind(
        PRTL_TRACE_DATABASE pDatabase,
        ULONG numFrames,
        PVOID* ppFrames,
        PRTL_TRACE_BLOCK* ppBlock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDatabase", "numFrames", "ppFrames", "ppBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTraceDatabaseLock(jitter):
    """
    BOOLEAN RtlTraceDatabaseLock(
        PRTL_TRACE_DATABASE pDatabase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTraceDatabaseUnlock(jitter):
    """
    BOOLEAN RtlTraceDatabaseUnlock(
        PRTL_TRACE_DATABASE pDatabase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTraceDatabaseValidate(jitter):
    """
    BOOLEAN RtlTraceDatabaseValidate(
        PRTL_TRACE_DATABASE pDatabase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDatabase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlpEnsureBufferSize(jitter):
    """
    NTSTATUS RtlpEnsureBufferSize(
        ULONG flags,
        PRTL_BUFFER pBuffer,
        SIZE_T requiredSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "pBuffer", "requiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrRegisterDllNotification(jitter):
    """
    NTSTATUS LdrRegisterDllNotification(
        ULONG Flags,
        PLDR_DLL_NOTIFICATION_FUNCTION NotificationFunction,
        PVOID Context,
        PVOID* Cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "NotificationFunction", "Context", "Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_LdrUnregisterDllNotification(jitter):
    """
    NTSTATUS LdrUnregisterDllNotification(
        PVOID Cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExtendedIntegerMultiply(jitter):
    """
    LARGE_INTEGER RtlExtendedIntegerMultiply(
        LARGE_INTEGER Multiplicand,
        LONG Multiplier
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Multiplicand", "Multiplier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExtendedLargeIntegerDivide(jitter):
    """
    LARGE_INTEGER RtlExtendedLargeIntegerDivide(
        LARGE_INTEGER Dividend,
        ULONG Divisor,
        PULONG Remainder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Dividend", "Divisor", "Remainder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddGrowableFunctionTable(jitter):
    """
    NTSTATUS RtlAddGrowableFunctionTable(
        PVOID* DynamicTable,
        PRUNTIME_FUNCTION FunctionTable,
        ULONG EntryCount,
        ULONG MaximumEntryCount,
        ULONG_PTR RangeBase,
        ULONG_PTR RangeEnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DynamicTable", "FunctionTable", "EntryCount", "MaximumEntryCount", "RangeBase", "RangeEnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteGrowableFunctionTable(jitter):
    """
    VOID RtlDeleteGrowableFunctionTable(
        PVOID DynamicTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DynamicTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGrowFunctionTable(jitter):
    """
    VOID RtlGrowFunctionTable(
        PVOID DynamicTable,
        ULONG NewEntryCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DynamicTable", "NewEntryCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetFunctionTableListHead(jitter):
    """
    PLIST_ENTRY RtlGetFunctionTableListHead()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetUnhandledExceptionFilter(jitter):
    """
    PVOID RtlSetUnhandledExceptionFilter(
        PVOID TopLevelExceptionFilter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TopLevelExceptionFilter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDispatchException(jitter):
    """
    BOOLEAN RtlDispatchException(
        PEXCEPTION_RECORD ExceptionRecord,
        PCONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExceptionRecord", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRaiseStatus(jitter):
    """
    VOID RtlRaiseStatus(
        NTSTATUS Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnhandledExceptionFilter(jitter):
    """
    LONG RtlUnhandledExceptionFilter(
        EXCEPTION_POINTERS* ExceptionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExceptionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWalkFrameChain(jitter):
    """
    ULONG RtlWalkFrameChain(
        PVOID* Callers,
        ULONG Count,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Callers", "Count", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLogStackBackTrace(jitter):
    """
    USHORT RtlLogStackBackTrace()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFirstEntrySList(jitter):
    """
    PSLIST_ENTRY RtlFirstEntrySList(
        PSLIST_HEADER ListHead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeSListHead(jitter):
    """
    void RtlInitializeSListHead(
        PSLIST_HEADER ListHead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInterlockedFlushSList(jitter):
    """
    PSLIST_ENTRY RtlInterlockedFlushSList(
        PSLIST_HEADER ListHead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInterlockedPopEntrySList(jitter):
    """
    PSLIST_ENTRY RtlInterlockedPopEntrySList(
        PSLIST_HEADER ListHead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInterlockedPushEntrySList(jitter):
    """
    PSLIST_ENTRY RtlInterlockedPushEntrySList(
        PSLIST_HEADER ListHead,
        PSLIST_ENTRY ListEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ListHead", "ListEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryDepthSList(jitter):
    """
    WORD RtlQueryDepthSList(
        PSLIST_HEADER ListHead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ListHead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateTransactionManager(jitter):
    """
    NTSTATUS NtCreateTransactionManager(
        PHANDLE TmHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PUNICODE_STRING LogFileName,
        ULONG CreateOptions,
        ULONG CommitStrength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TmHandle", "DesiredAccess", "ObjectAttributes", "LogFileName", "CreateOptions", "CommitStrength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenTransactionManager(jitter):
    """
    NTSTATUS NtOpenTransactionManager(
        PHANDLE TmHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        PUNICODE_STRING LogFileName,
        LPGUID TmIdentity,
        ULONG OpenOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TmHandle", "DesiredAccess", "ObjectAttributes", "LogFileName", "TmIdentity", "OpenOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationTransactionManager(jitter):
    """
    NTSTATUS NtQueryInformationTransactionManager(
        HANDLE TransactionManagerHandle,
        TRANSACTIONMANAGER_INFORMATION_CLASS TransactionManagerInformationClass,
        PVOID TransactionManagerInformation,
        ULONG TransactionManagerInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerHandle", "TransactionManagerInformationClass", "TransactionManagerInformation", "TransactionManagerInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRecoverTransactionManager(jitter):
    """
    NTSTATUS NtRecoverTransactionManager(
        HANDLE TransactionManagerHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRenameTransactionManager(jitter):
    """
    NTSTATUS NtRenameTransactionManager(
        PUNICODE_STRING LogFileName,
        LPGUID ExistingTransactionManagerGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogFileName", "ExistingTransactionManagerGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRollforwardTransactionManager(jitter):
    """
    NTSTATUS NtRollforwardTransactionManager(
        HANDLE TransactionManagerHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationTransactionManager(jitter):
    """
    NTSTATUS NtSetInformationTransactionManager(
        HANDLE TransactionManagerHandle,
        TRANSACTIONMANAGER_INFORMATION_CLASS TransactionManagerInformationClass,
        PVOID TransactionManagerInformation,
        ULONG TransactionManagerInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionManagerHandle", "TransactionManagerInformationClass", "TransactionManagerInformation", "TransactionManagerInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCommitTransaction(jitter):
    """
    NTSTATUS NtCommitTransaction(
        HANDLE TransactionHandle,
        BOOLEAN Wait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "Wait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateTransaction(jitter):
    """
    NTSTATUS NtCreateTransaction(
        PHANDLE TransactionHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        LPGUID Uow,
        HANDLE TmHandle,
        ULONG CreateOptions,
        ULONG IsolationLevel,
        ULONG IsolationFlags,
        PLARGE_INTEGER Timeout,
        PUNICODE_STRING Description
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "DesiredAccess", "ObjectAttributes", "Uow", "TmHandle", "CreateOptions", "IsolationLevel", "IsolationFlags", "Timeout", "Description"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtEnumerateTransactionObject(jitter):
    """
    NTSTATUS NtEnumerateTransactionObject(
        HANDLE RootObjectHandle,
        KTMOBJECT_TYPE QueryType,
        PKTMOBJECT_CURSOR ObjectCursor,
        ULONG ObjectCursorLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RootObjectHandle", "QueryType", "ObjectCursor", "ObjectCursorLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenTransaction(jitter):
    """
    NTSTATUS NtOpenTransaction(
        PHANDLE TransactionHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        LPGUID Uow,
        HANDLE TmHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "DesiredAccess", "ObjectAttributes", "Uow", "TmHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationTransaction(jitter):
    """
    NTSTATUS NtQueryInformationTransaction(
        HANDLE TransactionHandle,
        TRANSACTION_INFORMATION_CLASS TransactionInformationClass,
        PVOID TransactionInformation,
        ULONG TransactionInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "TransactionInformationClass", "TransactionInformation", "TransactionInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRollbackTransaction(jitter):
    """
    NTSTATUS NtRollbackTransaction(
        HANDLE TransactionHandle,
        BOOLEAN Wait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "Wait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationTransaction(jitter):
    """
    NTSTATUS NtSetInformationTransaction(
        HANDLE TransactionHandle,
        TRANSACTION_INFORMATION_CLASS TransactionInformationClass,
        PVOID TransactionInformation,
        ULONG TransactionInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle", "TransactionInformationClass", "TransactionInformation", "TransactionInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtFreezeTransactions(jitter):
    """
    NTSTATUS NtFreezeTransactions(
        PLARGE_INTEGER FreezeTimeout,
        PLARGE_INTEGER ThawTimeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FreezeTimeout", "ThawTimeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtThawTransactions(jitter):
    """
    NTSTATUS NtThawTransactions()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCommitComplete(jitter):
    """
    NTSTATUS NtCommitComplete(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCommitEnlistment(jitter):
    """
    NTSTATUS NtCommitEnlistment(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateEnlistment(jitter):
    """
    NTSTATUS NtCreateEnlistment(
        PHANDLE EnlistmentHandle,
        ACCESS_MASK DesiredAccess,
        HANDLE ResourceManagerHandle,
        HANDLE TransactionHandle,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG CreateOptions,
        NOTIFICATION_MASK NotificationMask,
        PVOID EnlistmentKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "DesiredAccess", "ResourceManagerHandle", "TransactionHandle", "ObjectAttributes", "CreateOptions", "NotificationMask", "EnlistmentKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenEnlistment(jitter):
    """
    NTSTATUS NtOpenEnlistment(
        PHANDLE EnlistmentHandle,
        ACCESS_MASK DesiredAccess,
        HANDLE RmHandle,
        LPGUID EnlistmentGuid,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "DesiredAccess", "RmHandle", "EnlistmentGuid", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPrepareComplete(jitter):
    """
    NTSTATUS NtPrepareComplete(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPrePrepareComplete(jitter):
    """
    NTSTATUS NtPrePrepareComplete(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPrepareEnlistment(jitter):
    """
    NTSTATUS NtPrepareEnlistment(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtPrePrepareEnlistment(jitter):
    """
    NTSTATUS NtPrePrepareEnlistment(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationEnlistment(jitter):
    """
    NTSTATUS NtQueryInformationEnlistment(
        HANDLE EnlistmentHandle,
        ENLISTMENT_INFORMATION_CLASS EnlistmentInformationClass,
        PVOID EnlistmentInformation,
        ULONG EnlistmentInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "EnlistmentInformationClass", "EnlistmentInformation", "EnlistmentInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtReadOnlyEnlistment(jitter):
    """
    NTSTATUS NtReadOnlyEnlistment(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRecoverEnlistment(jitter):
    """
    NTSTATUS NtRecoverEnlistment(
        HANDLE EnlistmentHandle,
        PVOID EnlistmentKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "EnlistmentKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRollbackComplete(jitter):
    """
    NTSTATUS NtRollbackComplete(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRollbackEnlistment(jitter):
    """
    NTSTATUS NtRollbackEnlistment(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationEnlistment(jitter):
    """
    NTSTATUS NtSetInformationEnlistment(
        HANDLE EnlistmentHandle,
        ENLISTMENT_INFORMATION_CLASS EnlistmentInformationClass,
        PVOID EnlistmentInformation,
        ULONG EnlistmentInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "EnlistmentInformationClass", "EnlistmentInformation", "EnlistmentInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSinglePhaseReject(jitter):
    """
    NTSTATUS NtSinglePhaseReject(
        HANDLE EnlistmentHandle,
        PLARGE_INTEGER TmVirtualClock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnlistmentHandle", "TmVirtualClock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtCreateResourceManager(jitter):
    """
    NTSTATUS NtCreateResourceManager(
        PHANDLE ResourceManagerHandle,
        ACCESS_MASK DesiredAccess,
        HANDLE TmHandle,
        LPGUID ResourceManagerGuid,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG CreateOptions,
        PUNICODE_STRING Description
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle", "DesiredAccess", "TmHandle", "ResourceManagerGuid", "ObjectAttributes", "CreateOptions", "Description"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtGetNotificationResourceManager(jitter):
    """
    NTSTATUS NtGetNotificationResourceManager(
        HANDLE ResourceManagerHandle,
        PTRANSACTION_NOTIFICATION TransactionNotification,
        ULONG NotificationLength,
        PLARGE_INTEGER Timeout,
        PULONG ReturnLength,
        ULONG Asynchronous,
        ULONG_PTR AsynchronousContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle", "TransactionNotification", "NotificationLength", "Timeout", "ReturnLength", "Asynchronous", "AsynchronousContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtOpenResourceManager(jitter):
    """
    NTSTATUS NtOpenResourceManager(
        PHANDLE ResourceManagerHandle,
        ACCESS_MASK DesiredAccess,
        HANDLE TmHandle,
        LPGUID ResourceManagerGuid,
        POBJECT_ATTRIBUTES ObjectAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle", "DesiredAccess", "TmHandle", "ResourceManagerGuid", "ObjectAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtQueryInformationResourceManager(jitter):
    """
    NTSTATUS NtQueryInformationResourceManager(
        HANDLE ResourceManagerHandle,
        RESOURCEMANAGER_INFORMATION_CLASS ResourceManagerInformationClass,
        PVOID ResourceManagerInformation,
        ULONG ResourceManagerInformationLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle", "ResourceManagerInformationClass", "ResourceManagerInformation", "ResourceManagerInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtRecoverResourceManager(jitter):
    """
    NTSTATUS NtRecoverResourceManager(
        HANDLE ResourceManagerHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_NtSetInformationResourceManager(jitter):
    """
    NTSTATUS NtSetInformationResourceManager(
        HANDLE ResourceManagerHandle,
        RESOURCEMANAGER_INFORMATION_CLASS ResourceManagerInformationClass,
        PVOID ResourceManagerInformation,
        ULONG ResourceManagerInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ResourceManagerHandle", "ResourceManagerInformationClass", "ResourceManagerInformation", "ResourceManagerInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeGenericTableAvl(jitter):
    """
    VOID RtlInitializeGenericTableAvl(
        PRTL_AVL_TABLE Table,
        PRTL_AVL_COMPARE_ROUTINE CompareRoutine,
        PRTL_AVL_ALLOCATE_ROUTINE AllocateRoutine,
        PRTL_AVL_FREE_ROUTINE FreeRoutine,
        PVOID TableContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "CompareRoutine", "AllocateRoutine", "FreeRoutine", "TableContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInsertElementGenericTableAvl(jitter):
    """
    PVOID RtlInsertElementGenericTableAvl(
        PRTL_AVL_TABLE Table,
        PVOID Buffer,
        CLONG BufferSize,
        PBOOLEAN NewElement
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer", "BufferSize", "NewElement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInsertElementGenericTableFullAvl(jitter):
    """
    PVOID RtlInsertElementGenericTableFullAvl(
        PRTL_AVL_TABLE Table,
        PVOID Buffer,
        CLONG BufferSize,
        PBOOLEAN NewElement,
        PVOID NodeOrParent,
        TABLE_SEARCH_RESULT SearchResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer", "BufferSize", "NewElement", "NodeOrParent", "SearchResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteElementGenericTableAvl(jitter):
    """
    BOOLEAN RtlDeleteElementGenericTableAvl(
        PRTL_AVL_TABLE Table,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLookupElementGenericTableAvl(jitter):
    """
    PVOID RtlLookupElementGenericTableAvl(
        PRTL_AVL_TABLE Table,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLookupElementGenericTableFullAvl(jitter):
    """
    PVOID RtlLookupElementGenericTableFullAvl(
        PRTL_AVL_TABLE Table,
        PVOID Buffer,
        PVOID* NodeOrParent,
        TABLE_SEARCH_RESULT* SearchResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer", "NodeOrParent", "SearchResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnumerateGenericTableAvl(jitter):
    """
    PVOID RtlEnumerateGenericTableAvl(
        PRTL_AVL_TABLE Table,
        BOOLEAN Restart
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Restart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnumerateGenericTableWithoutSplayingAvl(jitter):
    """
    PVOID RtlEnumerateGenericTableWithoutSplayingAvl(
        PRTL_AVL_TABLE Table,
        PVOID* RestartKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "RestartKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLookupFirstMatchingElementGenericTableAvl(jitter):
    """
    PVOID RtlLookupFirstMatchingElementGenericTableAvl(
        PRTL_AVL_TABLE Table,
        PVOID Buffer,
        PVOID* RestartKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer", "RestartKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnumerateGenericTableLikeADirectory(jitter):
    """
    PVOID RtlEnumerateGenericTableLikeADirectory(
        PRTL_AVL_TABLE Table,
        PRTL_AVL_MATCH_FUNCTION MatchFunction,
        PVOID MatchData,
        ULONG NextFlag,
        PVOID* RestartKey,
        PULONG DeleteCount,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "MatchFunction", "MatchData", "NextFlag", "RestartKey", "DeleteCount", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetElementGenericTableAvl(jitter):
    """
    PVOID RtlGetElementGenericTableAvl(
        PRTL_AVL_TABLE Table,
        ULONG I
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "I"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNumberGenericTableElementsAvl(jitter):
    """
    ULONG RtlNumberGenericTableElementsAvl(
        PRTL_AVL_TABLE Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsGenericTableEmptyAvl(jitter):
    """
    BOOLEAN RtlIsGenericTableEmptyAvl(
        PRTL_AVL_TABLE Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSplay(jitter):
    """
    PRTL_SPLAY_LINKS RtlSplay(
        PRTL_SPLAY_LINKS Links
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Links"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDelete(jitter):
    """
    PRTL_SPLAY_LINKS RtlDelete(
        PRTL_SPLAY_LINKS Links
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Links"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteNoSplay(jitter):
    """
    VOID RtlDeleteNoSplay(
        PRTL_SPLAY_LINKS Links,
        PRTL_SPLAY_LINKS* Root
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Links", "Root"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSubtreeSuccessor(jitter):
    """
    PRTL_SPLAY_LINKS RtlSubtreeSuccessor(
        PRTL_SPLAY_LINKS Links
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Links"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSubtreePredecessor(jitter):
    """
    PRTL_SPLAY_LINKS RtlSubtreePredecessor(
        PRTL_SPLAY_LINKS Links
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Links"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRealSuccessor(jitter):
    """
    PRTL_SPLAY_LINKS RtlRealSuccessor(
        PRTL_SPLAY_LINKS Links
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Links"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRealPredecessor(jitter):
    """
    PRTL_SPLAY_LINKS RtlRealPredecessor(
        PRTL_SPLAY_LINKS Links
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Links"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeGenericTable(jitter):
    """
    VOID RtlInitializeGenericTable(
        PRTL_GENERIC_TABLE Table,
        PRTL_GENERIC_COMPARE_ROUTINE CompareRoutine,
        PRTL_GENERIC_ALLOCATE_ROUTINE AllocateRoutine,
        PRTL_GENERIC_FREE_ROUTINE FreeRoutine,
        PVOID TableContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "CompareRoutine", "AllocateRoutine", "FreeRoutine", "TableContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInsertElementGenericTable(jitter):
    """
    PVOID RtlInsertElementGenericTable(
        PRTL_GENERIC_TABLE Table,
        PVOID Buffer,
        ULONG BufferSize,
        PBOOLEAN NewElement
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer", "BufferSize", "NewElement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInsertElementGenericTableFull(jitter):
    """
    PVOID RtlInsertElementGenericTableFull(
        PRTL_GENERIC_TABLE Table,
        PVOID Buffer,
        ULONG BufferSize,
        PBOOLEAN NewElement,
        PVOID NodeOrParent,
        TABLE_SEARCH_RESULT SearchResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer", "BufferSize", "NewElement", "NodeOrParent", "SearchResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteElementGenericTable(jitter):
    """
    BOOLEAN RtlDeleteElementGenericTable(
        PRTL_GENERIC_TABLE Table,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLookupElementGenericTable(jitter):
    """
    PVOID RtlLookupElementGenericTable(
        PRTL_GENERIC_TABLE Table,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLookupElementGenericTableFull(jitter):
    """
    PVOID RtlLookupElementGenericTableFull(
        PRTL_GENERIC_TABLE Table,
        PVOID Buffer,
        PVOID* NodeOrParent,
        TABLE_SEARCH_RESULT* SearchResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Buffer", "NodeOrParent", "SearchResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnumerateGenericTable(jitter):
    """
    PVOID RtlEnumerateGenericTable(
        PRTL_GENERIC_TABLE Table,
        BOOLEAN Restart
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "Restart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnumerateGenericTableWithoutSplaying(jitter):
    """
    PVOID RtlEnumerateGenericTableWithoutSplaying(
        PRTL_GENERIC_TABLE Table,
        PVOID* RestartKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "RestartKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetElementGenericTable(jitter):
    """
    PVOID RtlGetElementGenericTable(
        PRTL_GENERIC_TABLE Table,
        ULONG I
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table", "I"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNumberGenericTableElements(jitter):
    """
    ULONG RtlNumberGenericTableElements(
        PRTL_GENERIC_TABLE Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsGenericTableEmpty(jitter):
    """
    BOOLEAN RtlIsGenericTableEmpty(
        PRTL_GENERIC_TABLE Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRbInsertNodeEx(jitter):
    """
    VOID RtlRbInsertNodeEx(
        PRTL_RB_TREE Tree,
        PRTL_BALANCED_NODE Parent,
        BOOLEAN Right,
        PRTL_BALANCED_NODE Node
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Tree", "Parent", "Right", "Node"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRbRemoveNode(jitter):
    """
    VOID RtlRbRemoveNode(
        PRTL_RB_TREE Tree,
        PRTL_BALANCED_NODE Node
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Tree", "Node"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateHashTable(jitter):
    """
    BOOLEAN RtlCreateHashTable(
        PRTL_DYNAMIC_HASH_TABLE* HashTable,
        ULONG Shift,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Shift", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteHashTable(jitter):
    """
    VOID RtlDeleteHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInsertEntryHashTable(jitter):
    """
    BOOLEAN RtlInsertEntryHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_ENTRY Entry,
        ULONG_PTR Signature,
        PRTL_DYNAMIC_HASH_TABLE_CONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Entry", "Signature", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRemoveEntryHashTable(jitter):
    """
    BOOLEAN RtlRemoveEntryHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_ENTRY Entry,
        PRTL_DYNAMIC_HASH_TABLE_CONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Entry", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLookupEntryHashTable(jitter):
    """
    PRTL_DYNAMIC_HASH_TABLE_ENTRY RtlLookupEntryHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        ULONG_PTR Signature,
        PRTL_DYNAMIC_HASH_TABLE_CONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Signature", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetNextEntryHashTable(jitter):
    """
    PRTL_DYNAMIC_HASH_TABLE_ENTRY RtlGetNextEntryHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_CONTEXT Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitEnumerationHashTable(jitter):
    """
    BOOLEAN RtlInitEnumerationHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_ENUMERATOR Enumerator
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Enumerator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnumerateEntryHashTable(jitter):
    """
    PRTL_DYNAMIC_HASH_TABLE_ENTRY RtlEnumerateEntryHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_ENUMERATOR Enumerator
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Enumerator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEndEnumerationHashTable(jitter):
    """
    VOID RtlEndEnumerationHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_ENUMERATOR Enumerator
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Enumerator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitWeakEnumerationHashTable(jitter):
    """
    BOOLEAN RtlInitWeakEnumerationHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_ENUMERATOR Enumerator
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Enumerator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWeaklyEnumerateEntryHashTable(jitter):
    """
    PRTL_DYNAMIC_HASH_TABLE_ENTRY RtlWeaklyEnumerateEntryHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_ENUMERATOR Enumerator
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Enumerator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEndWeakEnumerationHashTable(jitter):
    """
    VOID RtlEndWeakEnumerationHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable,
        PRTL_DYNAMIC_HASH_TABLE_ENUMERATOR Enumerator
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable", "Enumerator"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExpandHashTable(jitter):
    """
    BOOLEAN RtlExpandHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlContractHashTable(jitter):
    """
    BOOLEAN RtlContractHashTable(
        PRTL_DYNAMIC_HASH_TABLE HashTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HashTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeCriticalSection(jitter):
    """
    NTSTATUS RtlInitializeCriticalSection(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeCriticalSectionAndSpinCount(jitter):
    """
    NTSTATUS RtlInitializeCriticalSectionAndSpinCount(
        PRTL_CRITICAL_SECTION CriticalSection,
        ULONG SpinCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection", "SpinCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteCriticalSection(jitter):
    """
    NTSTATUS RtlDeleteCriticalSection(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnterCriticalSection(jitter):
    """
    NTSTATUS RtlEnterCriticalSection(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLeaveCriticalSection(jitter):
    """
    NTSTATUS RtlLeaveCriticalSection(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTryEnterCriticalSection(jitter):
    """
    BOOLEAN RtlTryEnterCriticalSection(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsCriticalSectionLocked(jitter):
    """
    LOGICAL RtlIsCriticalSectionLocked(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsCriticalSectionLockedByThread(jitter):
    """
    LOGICAL RtlIsCriticalSectionLockedByThread(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetCriticalSectionRecursionCount(jitter):
    """
    ULONG RtlGetCriticalSectionRecursionCount(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetCriticalSectionSpinCount(jitter):
    """
    ULONG RtlSetCriticalSectionSpinCount(
        PRTL_CRITICAL_SECTION CriticalSection,
        ULONG SpinCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection", "SpinCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryCriticalSectionOwner(jitter):
    """
    HANDLE RtlQueryCriticalSectionOwner(
        HANDLE EventHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EventHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCheckForOrphanedCriticalSections(jitter):
    """
    VOID RtlCheckForOrphanedCriticalSections(
        HANDLE hThread
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hThread"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlpUnWaitCriticalSection(jitter):
    """
    VOID RtlpUnWaitCriticalSection(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlpWaitForCriticalSection(jitter):
    """
    NTSTATUS RtlpWaitForCriticalSection(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeResource(jitter):
    """
    VOID RtlInitializeResource(
        PRTL_RESOURCE pResource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteResource(jitter):
    """
    VOID RtlDeleteResource(
        PRTL_RESOURCE pResource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAcquireResourceShared(jitter):
    """
    BOOLEAN RtlAcquireResourceShared(
        PRTL_RESOURCE pResource,
        BOOLEAN bWaitForAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResource", "bWaitForAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAcquireResourceExclusive(jitter):
    """
    BOOLEAN RtlAcquireResourceExclusive(
        PRTL_RESOURCE pResource,
        BOOLEAN bWaitForAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResource", "bWaitForAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReleaseResource(jitter):
    """
    VOID RtlReleaseResource(
        PRTL_RESOURCE pResource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlConvertSharedToExclusive(jitter):
    """
    VOID RtlConvertSharedToExclusive(
        PRTL_RESOURCE Resource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Resource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlConvertExclusiveToShared(jitter):
    """
    VOID RtlConvertExclusiveToShared(
        PRTL_RESOURCE Resource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Resource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeSRWLock(jitter):
    """
    VOID RtlInitializeSRWLock(
        PRTL_SRWLOCK SRWLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAcquireSRWLockExclusive(jitter):
    """
    VOID RtlAcquireSRWLockExclusive(
        PRTL_SRWLOCK SRWLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAcquireSRWLockShared(jitter):
    """
    VOID RtlAcquireSRWLockShared(
        PRTL_SRWLOCK SRWLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReleaseSRWLockExclusive(jitter):
    """
    VOID RtlReleaseSRWLockExclusive(
        PRTL_SRWLOCK SRWLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReleaseSRWLockShared(jitter):
    """
    VOID RtlReleaseSRWLockShared(
        PRTL_SRWLOCK SRWLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTryAcquireSRWLockExclusive(jitter):
    """
    BOOLEAN RtlTryAcquireSRWLockExclusive(
        PRTL_SRWLOCK SRWLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTryAcquireSRWLockShared(jitter):
    """
    BOOLEAN RtlTryAcquireSRWLockShared(
        PRTL_SRWLOCK SRWLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAcquireReleaseSRWLockExclusive(jitter):
    """
    VOID RtlAcquireReleaseSRWLockExclusive(
        PRTL_SRWLOCK SRWLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeConditionVariable(jitter):
    """
    VOID RtlInitializeConditionVariable(
        PRTL_CONDITION_VARIABLE ConditionVariable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSleepConditionVariableCS(jitter):
    """
    NTSTATUS RtlSleepConditionVariableCS(
        PRTL_CONDITION_VARIABLE ConditionVariable,
        PRTL_CRITICAL_SECTION CriticalSection,
        PLARGE_INTEGER Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable", "CriticalSection", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSleepConditionVariableSRW(jitter):
    """
    NTSTATUS RtlSleepConditionVariableSRW(
        PRTL_CONDITION_VARIABLE ConditionVariable,
        PRTL_SRWLOCK SRWLock,
        PLARGE_INTEGER Timeout,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable", "SRWLock", "Timeout", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWakeConditionVariable(jitter):
    """
    VOID RtlWakeConditionVariable(
        PRTL_CONDITION_VARIABLE ConditionVariable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWakeAllConditionVariable(jitter):
    """
    VOID RtlWakeAllConditionVariable(
        PRTL_CONDITION_VARIABLE ConditionVariable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConditionVariable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitBarrier(jitter):
    """
    NTSTATUS RtlInitBarrier(
        PRTL_BARRIER Barrier,
        ULONG TotalThreads,
        ULONG SpinCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Barrier", "TotalThreads", "SpinCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteBarrier(jitter):
    """
    NTSTATUS RtlDeleteBarrier(
        PRTL_BARRIER Barrier
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Barrier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlBarrier(jitter):
    """
    BOOLEAN RtlBarrier(
        PRTL_BARRIER Barrier,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Barrier", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlBarrierForDelete(jitter):
    """
    BOOLEAN RtlBarrierForDelete(
        PRTL_BARRIER Barrier,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Barrier", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitString(jitter):
    """
    VOID RtlInitString(
        PSTRING DestinationString,
        PCSZ SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitAnsiString(jitter):
    """
    VOID RtlInitAnsiString(
        PANSI_STRING DestinationString,
        PCSZ SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitAnsiStringEx(jitter):
    """
    NTSTATUS RtlInitAnsiStringEx(
        PANSI_STRING DestinationString,
        PCSZ SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeAnsiString(jitter):
    """
    VOID RtlFreeAnsiString(
        PANSI_STRING AnsiString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AnsiString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeOemString(jitter):
    """
    VOID RtlFreeOemString(
        POEM_STRING OemString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OemString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopyString(jitter):
    """
    VOID RtlCopyString(
        PSTRING DestinationString,
        const STRING* SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpperChar(jitter):
    """
    CHAR RtlUpperChar(
        CHAR Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompareString(jitter):
    """
    LONG RtlCompareString(
        const STRING* String1,
        const STRING* String2,
        BOOLEAN CaseInSensitive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String2", "CaseInSensitive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEqualString(jitter):
    """
    BOOLEAN RtlEqualString(
        const STRING* String1,
        const STRING* String2,
        BOOLEAN CaseInSensitive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String2", "CaseInSensitive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlPrefixString(jitter):
    """
    BOOLEAN RtlPrefixString(
        PCANSI_STRING String1,
        PCANSI_STRING String2,
        BOOLEAN CaseInsensitive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String2", "CaseInsensitive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAppendStringToString(jitter):
    """
    NTSTATUS RtlAppendStringToString(
        PSTRING Destination,
        const STRING* Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAppendAsciizToString(jitter):
    """
    NTSTATUS RtlAppendAsciizToString(
        PSTRING Destination,
        PSTR Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpperString(jitter):
    """
    VOID RtlUpperString(
        PSTRING DestinationString,
        const STRING* SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitUnicodeString(jitter):
    """
    VOID RtlInitUnicodeString(
        PUNICODE_STRING DestinationString,
        PCWSTR SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitUnicodeStringEx(jitter):
    """
    NTSTATUS RtlInitUnicodeStringEx(
        PUNICODE_STRING DestinationString,
        PCWSTR SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateUnicodeString(jitter):
    """
    BOOLEAN RtlCreateUnicodeString(
        PUNICODE_STRING DestinationString,
        PCWSTR SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateUnicodeStringFromAsciiz(jitter):
    """
    BOOLEAN RtlCreateUnicodeStringFromAsciiz(
        PUNICODE_STRING Destination,
        PCSZ Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeUnicodeString(jitter):
    """
    VOID RtlFreeUnicodeString(
        PUNICODE_STRING UnicodeString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDuplicateUnicodeString(jitter):
    """
    NTSTATUS RtlDuplicateUnicodeString(
        [RTL_DUPLICATE_UNICODE_STRING_FLAGS] Flags,
        PCUNICODE_STRING SourceString,
        PUNICODE_STRING DestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "SourceString", "DestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopyUnicodeString(jitter):
    """
    VOID RtlCopyUnicodeString(
        PUNICODE_STRING DestinationString,
        PCUNICODE_STRING SourceString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpcaseUnicodeChar(jitter):
    """
    WCHAR RtlUpcaseUnicodeChar(
        WCHAR Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDowncaseUnicodeChar(jitter):
    """
    WCHAR RtlDowncaseUnicodeChar(
        WCHAR Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompareUnicodeString(jitter):
    """
    LONG RtlCompareUnicodeString(
        PCUNICODE_STRING String1,
        PCUNICODE_STRING String2,
        BOOLEAN CaseInsensitive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String2", "CaseInsensitive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompareUnicodeStrings(jitter):
    """
    LONG RtlCompareUnicodeStrings(
        PWCH String1,
        SIZE_T String1Length,
        PWCH String2,
        SIZE_T String2Length,
        BOOLEAN CaseInSensitive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String1Length", "String2", "String2Length", "CaseInSensitive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEqualUnicodeString(jitter):
    """
    BOOLEAN RtlEqualUnicodeString(
        PCUNICODE_STRING String1,
        PCUNICODE_STRING String2,
        BOOLEAN CaseInsensitive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String2", "CaseInsensitive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlHashUnicodeString(jitter):
    """
    NTSTATUS RtlHashUnicodeString(
        CONST UNICODE_STRING* String,
        BOOLEAN CaseInSensitive,
        [HASH_STRING_ALGORITHM] HashAlgorithm,
        PULONG HashValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String", "CaseInSensitive", "HashAlgorithm", "HashValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlValidateUnicodeString(jitter):
    """
    NTSTATUS RtlValidateUnicodeString(
        ULONG Flags,
        PCUNICODE_STRING String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlPrefixUnicodeString(jitter):
    """
    BOOLEAN RtlPrefixUnicodeString(
        PCUNICODE_STRING String1,
        PCUNICODE_STRING String2,
        BOOLEAN CaseInsensitive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String2", "CaseInsensitive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindCharInUnicodeString(jitter):
    """
    NTSTATUS RtlFindCharInUnicodeString(
        [RTL_FIND_CHAR_IN_UNICODE_STRING_FLAGS] Flags,
        PUNICODE_STRING SearchString,
        PCUNICODE_STRING MatchString,
        PUSHORT Position
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "SearchString", "MatchString", "Position"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAppendUnicodeStringToString(jitter):
    """
    NTSTATUS RtlAppendUnicodeStringToString(
        PUNICODE_STRING Destination,
        PCUNICODE_STRING Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAppendUnicodeToString(jitter):
    """
    NTSTATUS RtlAppendUnicodeToString(
        PUNICODE_STRING Destination,
        PCWSTR Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpcaseUnicodeString(jitter):
    """
    NTSTATUS RtlUpcaseUnicodeString(
        PUNICODE_STRING DestinationString,
        PCUNICODE_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDowncaseUnicodeString(jitter):
    """
    NTSTATUS RtlDowncaseUnicodeString(
        PUNICODE_STRING UniDest,
        PCUNICODE_STRING UniSource,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UniDest", "UniSource", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEraseUnicodeString(jitter):
    """
    VOID RtlEraseUnicodeString(
        PUNICODE_STRING String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAnsiStringToUnicodeString(jitter):
    """
    NTSTATUS RtlAnsiStringToUnicodeString(
        PUNICODE_STRING DestinationString,
        PCANSI_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeStringToAnsiString(jitter):
    """
    NTSTATUS RtlUnicodeStringToAnsiString(
        PANSI_STRING DestinationString,
        PCUNICODE_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAnsiCharToUnicodeChar(jitter):
    """
    WCHAR RtlAnsiCharToUnicodeChar(
        PUCHAR* SourceCharacter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceCharacter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpcaseUnicodeStringToAnsiString(jitter):
    """
    NTSTATUS RtlUpcaseUnicodeStringToAnsiString(
        PANSI_STRING DestinationString,
        PUNICODE_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlOemStringToUnicodeString(jitter):
    """
    NTSTATUS RtlOemStringToUnicodeString(
        PUNICODE_STRING DestinationString,
        PCOEM_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeStringToOemString(jitter):
    """
    NTSTATUS RtlUnicodeStringToOemString(
        POEM_STRING DestinationString,
        PCUNICODE_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpcaseUnicodeStringToOemString(jitter):
    """
    NTSTATUS RtlUpcaseUnicodeStringToOemString(
        POEM_STRING DestinationString,
        PCUNICODE_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeStringToCountedOemString(jitter):
    """
    NTSTATUS RtlUnicodeStringToCountedOemString(
        POEM_STRING DestinationString,
        PCUNICODE_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpcaseUnicodeStringToCountedOemString(jitter):
    """
    NTSTATUS RtlUpcaseUnicodeStringToCountedOemString(
        POEM_STRING DestinationString,
        PCUNICODE_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlMultiByteToUnicodeN(jitter):
    """
    NTSTATUS RtlMultiByteToUnicodeN(
        PWCHAR UnicodeString,
        ULONG UnicodeSize,
        PULONG ResultSize,
        PCSTR MbString,
        ULONG MbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeString", "UnicodeSize", "ResultSize", "MbString", "MbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlMultiByteToUnicodeSize(jitter):
    """
    NTSTATUS RtlMultiByteToUnicodeSize(
        PULONG UnicodeSize,
        PCSTR MbString,
        ULONG MbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeSize", "MbString", "MbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeToMultiByteN(jitter):
    """
    NTSTATUS RtlUnicodeToMultiByteN(
        PCHAR MbString,
        ULONG MbSize,
        PULONG ResultSize,
        PWCHAR UnicodeString,
        ULONG UnicodeSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MbString", "MbSize", "ResultSize", "UnicodeString", "UnicodeSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeToMultiByteSize(jitter):
    """
    NTSTATUS RtlUnicodeToMultiByteSize(
        PULONG MbSize,
        PWCHAR UnicodeString,
        ULONG UnicodeSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MbSize", "UnicodeString", "UnicodeSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpcaseUnicodeToMultiByteN(jitter):
    """
    NTSTATUS RtlUpcaseUnicodeToMultiByteN(
        PCHAR MbString,
        ULONG MbSize,
        PULONG ResultSize,
        PWCHAR UnicodeString,
        ULONG UnicodeSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MbString", "MbSize", "ResultSize", "UnicodeString", "UnicodeSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlOemToUnicodeN(jitter):
    """
    NTSTATUS RtlOemToUnicodeN(
        PWSTR UnicodeString,
        ULONG MaxBytesInUnicodeString,
        PULONG BytesInUnicodeString,
        PCHAR OemString,
        ULONG BytesInOemString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeString", "MaxBytesInUnicodeString", "BytesInUnicodeString", "OemString", "BytesInOemString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeToOemN(jitter):
    """
    NTSTATUS RtlUnicodeToOemN(
        PCHAR OemString,
        ULONG OemSize,
        PULONG ResultSize,
        PWCHAR UnicodeString,
        ULONG UnicodeSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OemString", "OemSize", "ResultSize", "UnicodeString", "UnicodeSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpcaseUnicodeToOemN(jitter):
    """
    NTSTATUS RtlUpcaseUnicodeToOemN(
        PCHAR OemString,
        ULONG OemSize,
        PULONG ResultSize,
        PWCHAR UnicodeString,
        ULONG UnicodeSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OemString", "OemSize", "ResultSize", "UnicodeString", "UnicodeSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlConsoleMultiByteToUnicodeN(jitter):
    """
    NTSTATUS RtlConsoleMultiByteToUnicodeN(
        PWCH UnicodeString,
        ULONG MaxBytesInUnicodeString,
        PULONG BytesInUnicodeString,
        PCH MultiByteString,
        ULONG BytesInMultiByteString,
        PULONG pdwSpecialChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeString", "MaxBytesInUnicodeString", "BytesInUnicodeString", "MultiByteString", "BytesInMultiByteString", "pdwSpecialChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUTF8ToUnicodeN(jitter):
    """
    NTSTATUS RtlUTF8ToUnicodeN(
        PWSTR UnicodeStringDestination,
        ULONG UnicodeStringMaxByteCount,
        PULONG UnicodeStringActualByteCount,
        PCCH UTF8StringSource,
        ULONG UTF8StringByteCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeStringDestination", "UnicodeStringMaxByteCount", "UnicodeStringActualByteCount", "UTF8StringSource", "UTF8StringByteCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeToUTF8N(jitter):
    """
    NTSTATUS RtlUnicodeToUTF8N(
        PCHAR UTF8StringDestination,
        ULONG UTF8StringMaxByteCount,
        PULONG UTF8StringActualByteCount,
        PCWCH UnicodeStringSource,
        ULONG UnicodeStringByteCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UTF8StringDestination", "UTF8StringMaxByteCount", "UTF8StringActualByteCount", "UnicodeStringSource", "UnicodeStringByteCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCustomCPToUnicodeN(jitter):
    """
    NTSTATUS RtlCustomCPToUnicodeN(
        PCPTABLEINFO CustomCP,
        PWCH UnicodeString,
        ULONG MaxBytesInUnicodeString,
        PULONG BytesInUnicodeString,
        PCH CustomCPString,
        ULONG BytesInCustomCPString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CustomCP", "UnicodeString", "MaxBytesInUnicodeString", "BytesInUnicodeString", "CustomCPString", "BytesInCustomCPString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeToCustomCPN(jitter):
    """
    NTSTATUS RtlUnicodeToCustomCPN(
        PCPTABLEINFO CustomCP,
        PCH CustomCPString,
        ULONG MaxBytesInCustomCPString,
        PULONG BytesInCustomCPString,
        PWCH UnicodeString,
        ULONG BytesInUnicodeString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CustomCP", "CustomCPString", "MaxBytesInCustomCPString", "BytesInCustomCPString", "UnicodeString", "BytesInUnicodeString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpcaseUnicodeToCustomCPN(jitter):
    """
    NTSTATUS RtlUpcaseUnicodeToCustomCPN(
        PCPTABLEINFO CustomCP,
        PCH CustomCPString,
        ULONG MaxBytesInCustomCPString,
        PULONG BytesInCustomCPString,
        PWCH UnicodeString,
        ULONG BytesInUnicodeString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CustomCP", "CustomCPString", "MaxBytesInCustomCPString", "BytesInCustomCPString", "UnicodeString", "BytesInUnicodeString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitCodePageTable(jitter):
    """
    VOID RtlInitCodePageTable(
        PUSHORT TableBase,
        PCPTABLEINFO CodePageTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TableBase", "CodePageTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitNlsTables(jitter):
    """
    VOID RtlInitNlsTables(
        PUSHORT AnsiTableBase,
        PUSHORT OemTableBase,
        PUSHORT CaseTableBase,
        PNLSTABLEINFO NlsTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AnsiTableBase", "OemTableBase", "CaseTableBase", "NlsTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlResetRtlTranslations(jitter):
    """
    VOID RtlResetRtlTranslations(
        PNLSTABLEINFO NlsTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NlsTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsTextUnicode(jitter):
    """
    BOOLEAN RtlIsTextUnicode(
        PVOID Buffer,
        INT Length,
        [IsTextUnicodeFlags*] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "Length", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNormalizeString(jitter):
    """
    NTSTATUS RtlNormalizeString(
        ULONG NormForm,
        PCWSTR SourceString,
        LONG SourceStringLength,
        PWSTR DestinationString,
        PLONG DestinationStringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NormForm", "SourceString", "SourceStringLength", "DestinationString", "DestinationStringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsNormalizedString(jitter):
    """
    NTSTATUS RtlIsNormalizedString(
        ULONG NormForm,
        PCWSTR SourceString,
        LONG SourceStringLength,
        PBOOLEAN Normalized
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NormForm", "SourceString", "SourceStringLength", "Normalized"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsNameInExpression(jitter):
    """
    BOOLEAN RtlIsNameInExpression(
        PUNICODE_STRING Expression,
        PUNICODE_STRING Name,
        BOOLEAN IgnoreCase,
        PWCH UpcaseTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Expression", "Name", "IgnoreCase", "UpcaseTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEqualDomainName(jitter):
    """
    BOOLEAN RtlEqualDomainName(
        PUNICODE_STRING String1,
        PUNICODE_STRING String2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEqualComputerName(jitter):
    """
    BOOLEAN RtlEqualComputerName(
        PUNICODE_STRING String1,
        PUNICODE_STRING String2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String1", "String2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDnsHostNameToComputerName(jitter):
    """
    NTSTATUS RtlDnsHostNameToComputerName(
        PUNICODE_STRING ComputerNameString,
        PCUNICODE_STRING DnsHostNameString,
        BOOLEAN AllocateComputerNameString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerNameString", "DnsHostNameString", "AllocateComputerNameString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlStringFromGUID(jitter):
    """
    NTSTATUS RtlStringFromGUID(
        REFGUID Guid,
        PUNICODE_STRING GuidString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Guid", "GuidString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGUIDFromString(jitter):
    """
    NTSTATUS RtlGUIDFromString(
        PCUNICODE_STRING GuidString,
        GUID* Guid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["GuidString", "Guid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompareAltitudes(jitter):
    """
    LONG RtlCompareAltitudes(
        PUNICODE_STRING Altitude1,
        PUNICODE_STRING Altitude2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Altitude1", "Altitude2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlxUnicodeStringToAnsiSize(jitter):
    """
    ULONG RtlxUnicodeStringToAnsiSize(
        PCUNICODE_STRING UnicodeString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlxUnicodeStringToOemSize(jitter):
    """
    ULONG RtlxUnicodeStringToOemSize(
        PCUNICODE_STRING UnicodeString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlxOemStringToUnicodeSize(jitter):
    """
    ULONG RtlxOemStringToUnicodeSize(
        PCOEM_STRING OemString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OemString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlxAnsiStringToUnicodeSize(jitter):
    """
    ULONG RtlxAnsiStringToUnicodeSize(
        PCANSI_STRING AnsiString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AnsiString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetDefaultCodePage(jitter):
    """
    VOID RtlGetDefaultCodePage(
        PUSHORT AnsiCodePage,
        PUSHORT OemCodePage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AnsiCodePage", "OemCodePage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAnsiStringToUnicodeSize(jitter):
    """
    ULONG RtlAnsiStringToUnicodeSize(
        PANSI_STRING AnsiString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AnsiString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeStringToAnsiSize(jitter):
    """
    ULONG RtlUnicodeStringToAnsiSize(
        PUNICODE_STRING UnicodeString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnicodeString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlOemStringToCountedUnicodeString(jitter):
    """
    NTSTATUS RtlOemStringToCountedUnicodeString(
        PUNICODE_STRING DestinationString,
        PCOEM_STRING SourceString,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "SourceString", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_PfxInitialize(jitter):
    """
    VOID PfxInitialize(
        PPREFIX_TABLE PrefixTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_PfxInsertPrefix(jitter):
    """
    BOOLEAN PfxInsertPrefix(
        PPREFIX_TABLE PrefixTable,
        PSTRING Prefix,
        PPREFIX_TABLE_ENTRY PrefixTableEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable", "Prefix", "PrefixTableEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_PfxRemovePrefix(jitter):
    """
    VOID PfxRemovePrefix(
        PPREFIX_TABLE PrefixTable,
        PPREFIX_TABLE_ENTRY PrefixTableEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable", "PrefixTableEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_PfxFindPrefix(jitter):
    """
    PPREFIX_TABLE_ENTRY PfxFindPrefix(
        PPREFIX_TABLE PrefixTable,
        PSTRING FullName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable", "FullName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeUnicodePrefix(jitter):
    """
    VOID RtlInitializeUnicodePrefix(
        PUNICODE_PREFIX_TABLE PrefixTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInsertUnicodePrefix(jitter):
    """
    BOOLEAN RtlInsertUnicodePrefix(
        PUNICODE_PREFIX_TABLE PrefixTable,
        PUNICODE_STRING Prefix,
        PUNICODE_PREFIX_TABLE_ENTRY PrefixTableEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable", "Prefix", "PrefixTableEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRemoveUnicodePrefix(jitter):
    """
    VOID RtlRemoveUnicodePrefix(
        PUNICODE_PREFIX_TABLE PrefixTable,
        PUNICODE_PREFIX_TABLE_ENTRY PrefixTableEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable", "PrefixTableEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindUnicodePrefix(jitter):
    """
    PUNICODE_PREFIX_TABLE_ENTRY RtlFindUnicodePrefix(
        PUNICODE_PREFIX_TABLE PrefixTable,
        PUNICODE_STRING FullName,
        ULONG CaseInsensitiveIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable", "FullName", "CaseInsensitiveIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNextUnicodePrefix(jitter):
    """
    PUNICODE_PREFIX_TABLE_ENTRY RtlNextUnicodePrefix(
        PUNICODE_PREFIX_TABLE PrefixTable,
        BOOLEAN Restart
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrefixTable", "Restart"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetCompressionWorkSpaceSize(jitter):
    """
    NTSTATUS RtlGetCompressionWorkSpaceSize(
        USHORT CompressionFormatAndEngine,
        PULONG CompressBufferWorkSpaceSize,
        PULONG CompressFragmentWorkSpaceSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CompressionFormatAndEngine", "CompressBufferWorkSpaceSize", "CompressFragmentWorkSpaceSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompressBuffer(jitter):
    """
    NTSTATUS RtlCompressBuffer(
        USHORT CompressionFormatAndEngine,
        PUCHAR UncompressedBuffer,
        ULONG UncompressedBufferSize,
        PUCHAR CompressedBuffer,
        ULONG CompressedBufferSize,
        ULONG UncompressedChunkSize,
        PULONG FinalCompressedSize,
        PVOID WorkSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CompressionFormatAndEngine", "UncompressedBuffer", "UncompressedBufferSize", "CompressedBuffer", "CompressedBufferSize", "UncompressedChunkSize", "FinalCompressedSize", "WorkSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDecompressBuffer(jitter):
    """
    NTSTATUS RtlDecompressBuffer(
        USHORT CompressionFormat,
        PUCHAR UncompressedBuffer,
        ULONG UncompressedBufferSize,
        PUCHAR CompressedBuffer,
        ULONG CompressedBufferSize,
        PULONG FinalUncompressedSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CompressionFormat", "UncompressedBuffer", "UncompressedBufferSize", "CompressedBuffer", "CompressedBufferSize", "FinalUncompressedSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDecompressBufferEx(jitter):
    """
    NTSTATUS RtlDecompressBufferEx(
        USHORT CompressionFormat,
        PUCHAR UncompressedBuffer,
        ULONG UncompressedBufferSize,
        PUCHAR CompressedBuffer,
        ULONG CompressedBufferSize,
        PULONG FinalUncompressedSize,
        PVOID WorkSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CompressionFormat", "UncompressedBuffer", "UncompressedBufferSize", "CompressedBuffer", "CompressedBufferSize", "FinalUncompressedSize", "WorkSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDecompressFragment(jitter):
    """
    NTSTATUS RtlDecompressFragment(
        USHORT CompressionFormat,
        PUCHAR UncompressedFragment,
        ULONG UncompressedFragmentSize,
        PUCHAR CompressedBuffer,
        ULONG CompressedBufferSize,
        ULONG FragmentOffset,
        PULONG FinalUncompressedSize,
        PVOID WorkSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CompressionFormat", "UncompressedFragment", "UncompressedFragmentSize", "CompressedBuffer", "CompressedBufferSize", "FragmentOffset", "FinalUncompressedSize", "WorkSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDescribeChunk(jitter):
    """
    NTSTATUS RtlDescribeChunk(
        USHORT CompressionFormat,
        PUCHAR* CompressedBuffer,
        PUCHAR EndOfCompressedBufferPlus1,
        PUCHAR* ChunkBuffer,
        PULONG ChunkSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CompressionFormat", "CompressedBuffer", "EndOfCompressedBufferPlus1", "ChunkBuffer", "ChunkSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReserveChunk(jitter):
    """
    NTSTATUS RtlReserveChunk(
        USHORT CompressionFormat,
        PUCHAR* CompressedBuffer,
        PUCHAR EndOfCompressedBufferPlus1,
        PUCHAR* ChunkBuffer,
        ULONG ChunkSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CompressionFormat", "CompressedBuffer", "EndOfCompressedBufferPlus1", "ChunkBuffer", "ChunkSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDecompressChunks(jitter):
    """
    NTSTATUS RtlDecompressChunks(
        PUCHAR UncompressedBuffer,
        ULONG UncompressedBufferSize,
        PUCHAR CompressedBuffer,
        ULONG CompressedBufferSize,
        PUCHAR CompressedTail,
        ULONG CompressedTailSize,
        PCOMPRESSED_DATA_INFO CompressedDataInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncompressedBuffer", "UncompressedBufferSize", "CompressedBuffer", "CompressedBufferSize", "CompressedTail", "CompressedTailSize", "CompressedDataInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompressChunks(jitter):
    """
    NTSTATUS RtlCompressChunks(
        PUCHAR UncompressedBuffer,
        ULONG UncompressedBufferSize,
        PUCHAR CompressedBuffer,
        ULONG CompressedBufferSize,
        PCOMPRESSED_DATA_INFO CompressedDataInfo,
        ULONG CompressedDataInfoLength,
        PVOID WorkSpace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncompressedBuffer", "UncompressedBufferSize", "CompressedBuffer", "CompressedBufferSize", "CompressedDataInfo", "CompressedDataInfoLength", "WorkSpace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlConvertLCIDToString(jitter):
    """
    NTSTATUS RtlConvertLCIDToString(
        LCID LcidValue,
        ULONG Base,
        ULONG Padding,
        PWSTR pResultBuf,
        ULONG Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LcidValue", "Base", "Padding", "pResultBuf", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsValidLocaleName(jitter):
    """
    BOOLEAN RtlIsValidLocaleName(
        PWSTR LocaleName,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LocaleName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetParentLocaleName(jitter):
    """
    NTSTATUS RtlGetParentLocaleName(
        PWSTR LocaleName,
        PUNICODE_STRING ParentLocaleName,
        ULONG Flags,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LocaleName", "ParentLocaleName", "Flags", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLcidToLocaleName(jitter):
    """
    NTSTATUS RtlLcidToLocaleName(
        LCID lcid,
        PUNICODE_STRING LocaleName,
        ULONG Flags,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lcid", "LocaleName", "Flags", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLocaleNameToLcid(jitter):
    """
    NTSTATUS RtlLocaleNameToLcid(
        PWSTR LocaleName,
        PLCID lcid,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LocaleName", "lcid", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLCIDToCultureName(jitter):
    """
    BOOLEAN RtlLCIDToCultureName(
        LCID Lcid,
        PUNICODE_STRING String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Lcid", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCultureNameToLCID(jitter):
    """
    BOOLEAN RtlCultureNameToLCID(
        PUNICODE_STRING String,
        PLCID Lcid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String", "Lcid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCleanUpTEBLangLists(jitter):
    """
    VOID RtlCleanUpTEBLangLists()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetLocaleFileMappingAddress(jitter):
    """
    NTSTATUS RtlGetLocaleFileMappingAddress(
        PVOID* BaseAddress,
        PLCID DefaultLocaleId,
        PLARGE_INTEGER DefaultCasingTableSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "DefaultLocaleId", "DefaultCasingTableSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAcquirePebLock(jitter):
    """
    VOID RtlAcquirePebLock()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReleasePebLock(jitter):
    """
    VOID RtlReleasePebLock()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTryAcquirePebLock(jitter):
    """
    LOGICAL RtlTryAcquirePebLock()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAllocateFromPeb(jitter):
    """
    NTSTATUS RtlAllocateFromPeb(
        ULONG Size,
        PVOID* Block
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Size", "Block"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeToPeb(jitter):
    """
    NTSTATUS RtlFreeToPeb(
        PVOID Block,
        ULONG Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Block", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetCurrentPeb(jitter):
    """
    PPEB RtlGetCurrentPeb()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateProcessParameters(jitter):
    """
    NTSTATUS RtlCreateProcessParameters(
        PRTL_USER_PROCESS_PARAMETERS* ProcessParameters,
        PUNICODE_STRING ImagePathName,
        PUNICODE_STRING DllPath,
        PUNICODE_STRING CurrentDirectory,
        PUNICODE_STRING CommandLine,
        PWSTR Environment,
        PUNICODE_STRING WindowTitle,
        PUNICODE_STRING DesktopInfo,
        PUNICODE_STRING ShellInfo,
        PUNICODE_STRING RuntimeInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessParameters", "ImagePathName", "DllPath", "CurrentDirectory", "CommandLine", "Environment", "WindowTitle", "DesktopInfo", "ShellInfo", "RuntimeInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateProcessParametersEx(jitter):
    """
    NTSTATUS RtlCreateProcessParametersEx(
        PRTL_USER_PROCESS_PARAMETERS* pProcessParameters,
        PUNICODE_STRING ImagePathName,
        PUNICODE_STRING DllPath,
        PUNICODE_STRING CurrentDirectory,
        PUNICODE_STRING CommandLine,
        PVOID Environment,
        PUNICODE_STRING WindowTitle,
        PUNICODE_STRING DesktopInfo,
        PUNICODE_STRING ShellInfo,
        PUNICODE_STRING RuntimeData,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProcessParameters", "ImagePathName", "DllPath", "CurrentDirectory", "CommandLine", "Environment", "WindowTitle", "DesktopInfo", "ShellInfo", "RuntimeData", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDestroyProcessParameters(jitter):
    """
    NTSTATUS RtlDestroyProcessParameters(
        PRTL_USER_PROCESS_PARAMETERS ProcessParameters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNormalizeProcessParams(jitter):
    """
    PRTL_USER_PROCESS_PARAMETERS RtlNormalizeProcessParams(
        PRTL_USER_PROCESS_PARAMETERS ProcessParameters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeNormalizeProcessParams(jitter):
    """
    PRTL_USER_PROCESS_PARAMETERS RtlDeNormalizeProcessParams(
        PRTL_USER_PROCESS_PARAMETERS ProcessParameters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessParameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateUserProcess(jitter):
    """
    NTSTATUS RtlCreateUserProcess(
        PUNICODE_STRING ImageFileName,
        ULONG Attributes,
        PRTL_USER_PROCESS_PARAMETERS ProcessParameters,
        PSECURITY_DESCRIPTOR ProcessSecutityDescriptor,
        PSECURITY_DESCRIPTOR ThreadSecurityDescriptor,
        HANDLE ParentProcess,
        BOOLEAN CurrentDirectory,
        HANDLE DebugPort,
        HANDLE ExceptionPort,
        PRTL_USER_PROCESS_INFORMATION ProcessInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImageFileName", "Attributes", "ProcessParameters", "ProcessSecutityDescriptor", "ThreadSecurityDescriptor", "ParentProcess", "CurrentDirectory", "DebugPort", "ExceptionPort", "ProcessInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExitUserProcess(jitter):
    """
    VOID RtlExitUserProcess(
        NTSTATUS ExitStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExitStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCloneUserProcess(jitter):
    """
    NTSTATUS RtlCloneUserProcess(
        [RTL_CLONE_PROCESS_FLAGS] ProcessFlags,
        PSECURITY_DESCRIPTOR ProcessSecurityDescriptor,
        PSECURITY_DESCRIPTOR ThreadSecurityDescriptor,
        HANDLE DebugPort,
        PRTL_USER_PROCESS_INFORMATION ProcessInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessFlags", "ProcessSecurityDescriptor", "ThreadSecurityDescriptor", "DebugPort", "ProcessInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpdateClonedCriticalSection(jitter):
    """
    VOID RtlUpdateClonedCriticalSection(
        PRTL_CRITICAL_SECTION CriticalSection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CriticalSection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpdateClonedSRWLock(jitter):
    """
    VOID RtlUpdateClonedSRWLock(
        PRTL_SRWLOCK SRWLock,
        LOGICAL Shared
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SRWLock", "Shared"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateProcessReflection(jitter):
    """
    NTSTATUS RtlCreateProcessReflection(
        HANDLE ProcessHandle,
        ULONG Flags,
        PVOID StartRoutine,
        PVOID StartContext,
        HANDLE EventHandle,
        PRTLP_PROCESS_REFLECTION_REFLECTION_INFORMATION ReflectionInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "Flags", "StartRoutine", "StartContext", "EventHandle", "ReflectionInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetProcessIsCritical(jitter):
    """
    VOID RtlSetProcessIsCritical(
        BOOLEAN NewValue,
        PBOOLEAN OldValue,
        BOOLEAN IsWinlogon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NewValue", "OldValue", "IsWinlogon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetThreadIsCritical(jitter):
    """
    NTSTATUS RtlSetThreadIsCritical(
        BOOLEAN NewValue,
        PBOOLEAN OldValue,
        BOOLEAN CheckFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NewValue", "OldValue", "CheckFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateUserThread(jitter):
    """
    NTSTATUS RtlCreateUserThread(
        [ProcessHandle] ProcessHandle,
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        BOOLEAN CreateSuspended,
        ULONG StackZeroBits,
        SIZE_T StackReserve,
        SIZE_T StackCommit,
        PTHREAD_START_ROUTINE StartAddress,
        PVOID Parameter,
        PHANDLE ThreadHandle,
        PCLIENT_ID ClientId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "SecurityDescriptor", "CreateSuspended", "StackZeroBits", "StackReserve", "StackCommit", "StartAddress", "Parameter", "ThreadHandle", "ClientId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExitUserThread(jitter):
    """
    VOID RtlExitUserThread(
        NTSTATUS Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateUserStack(jitter):
    """
    NTSTATUS RtlCreateUserStack(
        SIZE_T CommittedStackSize,
        SIZE_T MaximumStackSize,
        ULONG_PTR ZeroBits,
        SIZE_T PageSize,
        ULONG_PTR ReserveAlignment,
        PINITIAL_TEB InitialTeb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CommittedStackSize", "MaximumStackSize", "ZeroBits", "PageSize", "ReserveAlignment", "InitialTeb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeContext(jitter):
    """
    VOID RtlInitializeContext(
        [ProcessHandle] ProcessHandle,
        PCONTEXT ThreadContext,
        PVOID ThreadStartParam,
        PTHREAD_START_ROUTINE ThreadStartAddress,
        PINITIAL_TEB InitialTeb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "ThreadContext", "ThreadStartParam", "ThreadStartAddress", "InitialTeb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRemoteCall(jitter):
    """
    NTSTATUS RtlRemoteCall(
        HANDLE Process,
        HANDLE Thread,
        PVOID CallSite,
        ULONG ArgumentCount,
        PULONG Arguments,
        BOOLEAN PassContext,
        BOOLEAN AlreadySuspended
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Process", "Thread", "CallSite", "ArgumentCount", "Arguments", "PassContext", "AlreadySuspended"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWow64GetThreadContext(jitter):
    """
    NTSTATUS RtlWow64GetThreadContext(
        HANDLE ThreadHandle,
        PWOW64_CONTEXT ThreadContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "ThreadContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWow64SetThreadContext(jitter):
    """
    NTSTATUS RtlWow64SetThreadContext(
        HANDLE ThreadHandle,
        PWOW64_CONTEXT ThreadContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "ThreadContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLockCurrentThread(jitter):
    """
    NTSTATUS RtlLockCurrentThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnlockCurrentThread(jitter):
    """
    NTSTATUS RtlUnlockCurrentThread()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlPcToFileHeader(jitter):
    """
    PVOID RtlPcToFileHeader(
        PVOID PcValue,
        PVOID* BaseOfImage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PcValue", "BaseOfImage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlImageNtHeader(jitter):
    """
    PIMAGE_NT_HEADERS RtlImageNtHeader(
        [HMODULE-PVOID] BaseAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlImageNtHeaderEx(jitter):
    """
    NTSTATUS RtlImageNtHeaderEx(
        [RTL_IMAGE_NT_HEADER_EX_FLAGS] Flags,
        [HMODULE-PVOID] BaseAddress,
        ULONGLONG Size,
        PIMAGE_NT_HEADERS* NtHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "BaseAddress", "Size", "NtHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddressInSectionTable(jitter):
    """
    PVOID RtlAddressInSectionTable(
        PIMAGE_NT_HEADERS NtHeaders,
        PVOID BaseOfImage,
        ULONG VirtualAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NtHeaders", "BaseOfImage", "VirtualAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSectionTableFromVirtualAddress(jitter):
    """
    PIMAGE_SECTION_HEADER RtlSectionTableFromVirtualAddress(
        PIMAGE_NT_HEADERS NtHeaders,
        PVOID BaseOfImage,
        ULONG VirtualAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NtHeaders", "BaseOfImage", "VirtualAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlImageDirectoryEntryToData(jitter):
    """
    PVOID RtlImageDirectoryEntryToData(
        [HMODULE-PVOID] BaseAddress,
        BOOLEAN MappedAsImage,
        USHORT Directory,
        PULONG Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "MappedAsImage", "Directory", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlImageRvaToSection(jitter):
    """
    PIMAGE_SECTION_HEADER RtlImageRvaToSection(
        PIMAGE_NT_HEADERS NtHeader,
        PVOID BaseAddress,
        ULONG Rva
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NtHeader", "BaseAddress", "Rva"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlImageRvaToVa(jitter):
    """
    PVOID RtlImageRvaToVa(
        PIMAGE_NT_HEADERS NtHeader,
        PVOID BaseAddress,
        ULONG Rva,
        PIMAGE_SECTION_HEADER* SectionHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NtHeader", "BaseAddress", "Rva", "SectionHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompareMemoryUlong(jitter):
    """
    SIZE_T RtlCompareMemoryUlong(
        PVOID Source,
        SIZE_T Length,
        ULONG Pattern
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Source", "Length", "Pattern"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFillMemoryUlong(jitter):
    """
    VOID RtlFillMemoryUlong(
        PVOID Destination,
        ULONG Length,
        ULONG Fill
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Length", "Fill"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFillMemoryUlonglong(jitter):
    """
    VOID RtlFillMemoryUlonglong(
        PVOID Destination,
        SIZE_T Length,
        ULONGLONG Pattern
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Length", "Pattern"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompareMemory(jitter):
    """
    SIZE_T RtlCompareMemory(
        const VOID* Source1,
        const VOID* Source2,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Source1", "Source2", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopyMemory(jitter):
    """
    VOID RtlCopyMemory(
        VOID* Destination,
        const VOID* Source,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Source", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlMoveMemory(jitter):
    """
    VOID RtlMoveMemory(
        VOID* Destination,
        const VOID* Source,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Source", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlZeroMemory(jitter):
    """
    VOID RtlZeroMemory(
        VOID* Destination,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateEnvironment(jitter):
    """
    NTSTATUS RtlCreateEnvironment(
        BOOLEAN Inherit,
        PWSTR* Environment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Inherit", "Environment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateEnvironmentEx(jitter):
    """
    NTSTATUS RtlCreateEnvironmentEx(
        PVOID SourceEnv,
        PVOID* Environment,
        [RTL_CREATE_ENVIRONMENT_EX_FLAGS] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceEnv", "Environment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDestroyEnvironment(jitter):
    """
    VOID RtlDestroyEnvironment(
        PWSTR Environment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Environment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetCurrentEnvironment(jitter):
    """
    VOID RtlSetCurrentEnvironment(
        PVOID NewEnvironment,
        PVOID* OldEnvironment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NewEnvironment", "OldEnvironment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetEnvironmentVar(jitter):
    """
    NTSTATUS RtlSetEnvironmentVar(
        PWSTR* Environment,
        PWSTR Name,
        SIZE_T NameLength,
        PWSTR Value,
        SIZE_T ValueLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Environment", "Name", "NameLength", "Value", "ValueLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetEnvironmentVariable(jitter):
    """
    NTSTATUS RtlSetEnvironmentVariable(
        PWSTR* Environment,
        PUNICODE_STRING Name,
        PUNICODE_STRING Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Environment", "Name", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryEnvironmentVariable(jitter):
    """
    NTSTATUS RtlQueryEnvironmentVariable(
        PVOID Environment,
        PWSTR Name,
        SIZE_T NameLength,
        PWSTR Value,
        SIZE_T ValueLength,
        PSIZE_T ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Environment", "Name", "NameLength", "Value", "ValueLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryEnvironmentVariable_U(jitter):
    """
    NTSTATUS RtlQueryEnvironmentVariable_U(
        PWSTR Environment,
        PUNICODE_STRING Name,
        PUNICODE_STRING Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Environment", "Name", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExpandEnvironmentStrings(jitter):
    """
    NTSTATUS RtlExpandEnvironmentStrings(
        PVOID Environment,
        PWSTR Src,
        SIZE_T SrcLength,
        PWSTR Dst,
        SIZE_T DstLength,
        PSIZE_T ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Environment", "Src", "SrcLength", "Dst", "DstLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExpandEnvironmentStrings_U(jitter):
    """
    NTSTATUS RtlExpandEnvironmentStrings_U(
        PWSTR Environment,
        PUNICODE_STRING Source,
        PUNICODE_STRING Destination,
        PULONG Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Environment", "Source", "Destination", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetEnvironmentStrings(jitter):
    """
    NTSTATUS RtlSetEnvironmentStrings(
        PWCHAR NewEnvironment,
        SIZE_T NewEnvironmentSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NewEnvironment", "NewEnvironmentSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGenerate8dot3Name(jitter):
    """
    VOID RtlGenerate8dot3Name(
        PUNICODE_STRING Name,
        BOOLEAN AllowExtendedCharacters,
        PGENERATE_NAME_CONTEXT Context,
        PUNICODE_STRING Name8dot3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "AllowExtendedCharacters", "Context", "Name8dot3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDetermineDosPathNameType_U(jitter):
    """
    RTL_PATH_TYPE RtlDetermineDosPathNameType_U(
        PCWSTR Path
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsDosDeviceName_U(jitter):
    """
    ULONG RtlIsDosDeviceName_U(
        PWSTR Name
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsDosDeviceName_Ustr(jitter):
    """
    ULONG RtlIsDosDeviceName_Ustr(
        PUNICODE_STRING Name
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetFullPathName_U(jitter):
    """
    ULONG RtlGetFullPathName_U(
        PCWSTR FileName,
        ULONG Size,
        PWSTR Buffer,
        PWSTR* ShortName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "Size", "Buffer", "ShortName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetFullPathName_UEx(jitter):
    """
    NTSTATUS RtlGetFullPathName_UEx(
        PWSTR FileName,
        ULONG BufferLength,
        PWSTR Buffer,
        PWSTR* FilePart,
        RTL_PATH_TYPE* InputPathType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "BufferLength", "Buffer", "FilePart", "InputPathType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetFullPathName_UstrEx(jitter):
    """
    NTSTATUS RtlGetFullPathName_UstrEx(
        PUNICODE_STRING FileName,
        PUNICODE_STRING StaticString,
        PUNICODE_STRING DynamicString,
        PUNICODE_STRING* StringUsed,
        SIZE_T* FilePartPrefixCch,
        PBOOLEAN NameInvalid,
        RTL_PATH_TYPE* InputPathType,
        SIZE_T* BytesRequired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "StaticString", "DynamicString", "StringUsed", "FilePartPrefixCch", "NameInvalid", "InputPathType", "BytesRequired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetCurrentDirectory_U(jitter):
    """
    ULONG RtlGetCurrentDirectory_U(
        ULONG MaximumLength,
        PWSTR Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MaximumLength", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetCurrentDirectory_U(jitter):
    """
    NTSTATUS RtlSetCurrentDirectory_U(
        PUNICODE_STRING name
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["name"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetLongestNtPathLength(jitter):
    """
    ULONG RtlGetLongestNtPathLength()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDosPathNameToNtPathName_U(jitter):
    """
    BOOLEAN RtlDosPathNameToNtPathName_U(
        PCWSTR DosPathName,
        PUNICODE_STRING NtPathName,
        PCWSTR* NtFileNamePart,
        CURDIR* DirectoryInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DosPathName", "NtPathName", "NtFileNamePart", "DirectoryInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDosPathNameToNtPathName_U_WithStatus(jitter):
    """
    NTSTATUS RtlDosPathNameToNtPathName_U_WithStatus(
        PWSTR DosFileName,
        PUNICODE_STRING NtFileName,
        PWSTR* FilePart,
        PRTL_RELATIVE_NAME_U RelativeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DosFileName", "NtFileName", "FilePart", "RelativeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDosPathNameToRelativeNtPathName_U(jitter):
    """
    BOOLEAN RtlDosPathNameToRelativeNtPathName_U(
        PWSTR DosFileName,
        PUNICODE_STRING NtFileName,
        PWSTR* FilePart,
        PRTL_RELATIVE_NAME_U RelativeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DosFileName", "NtFileName", "FilePart", "RelativeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDosPathNameToRelativeNtPathName_U_WithStatus(jitter):
    """
    NTSTATUS RtlDosPathNameToRelativeNtPathName_U_WithStatus(
        PWSTR DosFileName,
        PUNICODE_STRING NtFileName,
        PWSTR* FilePart,
        PRTL_RELATIVE_NAME_U RelativeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DosFileName", "NtFileName", "FilePart", "RelativeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReleaseRelativeName(jitter):
    """
    VOID RtlReleaseRelativeName(
        PRTL_RELATIVE_NAME_U RelativeName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RelativeName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDosSearchPath_U(jitter):
    """
    ULONG RtlDosSearchPath_U(
        PCWSTR Path,
        PCWSTR FileName,
        PCWSTR Extension,
        ULONG BufferSize,
        PWSTR Buffer,
        PWSTR* PartName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Path", "FileName", "Extension", "BufferSize", "Buffer", "PartName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDosSearchPath_Ustr(jitter):
    """
    NTSTATUS RtlDosSearchPath_Ustr(
        [RTL_DOS_SEARCH_PATH_FLAG] Flags,
        PUNICODE_STRING Path,
        PUNICODE_STRING FileName,
        PUNICODE_STRING DefaultExtension,
        PUNICODE_STRING StaticString,
        PUNICODE_STRING DynamicString,
        PCUNICODE_STRING* FullFileNameOut,
        SIZE_T* FilePartPrefixCch,
        SIZE_T* BytesRequired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Path", "FileName", "DefaultExtension", "StaticString", "DynamicString", "FullFileNameOut", "FilePartPrefixCch", "BytesRequired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDoesFileExists_U(jitter):
    """
    BOOLEAN RtlDoesFileExists_U(
        PCWSTR FileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDoesFileExists_UstrEx(jitter):
    """
    BOOLEAN RtlDoesFileExists_UstrEx(
        PCUNICODE_STRING FileName,
        BOOLEAN SucceedIfBusy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "SucceedIfBusy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDetermineDosPathNameType_Ustr(jitter):
    """
    ULONG RtlDetermineDosPathNameType_Ustr(
        PCUNICODE_STRING Path
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetFullPathName_Ustr(jitter):
    """
    ULONG RtlGetFullPathName_Ustr(
        PUNICODE_STRING FileName,
        ULONG Size,
        PWSTR Buffer,
        PWSTR* ShortName,
        PBOOLEAN InvalidName,
        RTL_PATH_TYPE* PathType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileName", "Size", "Buffer", "ShortName", "InvalidName", "PathType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsNameLegalDOS8Dot3(jitter):
    """
    BOOLEAN RtlIsNameLegalDOS8Dot3(
        PCUNICODE_STRING Name,
        POEM_STRING OemName,
        PBOOLEAN NameContainsSpaces
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "OemName", "NameContainsSpaces"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDosApplyFileIsolationRedirection_Ustr(jitter):
    """
    NTSTATUS RtlDosApplyFileIsolationRedirection_Ustr(
        BOOLEAN Unknown,
        PUNICODE_STRING OriginalName,
        PUNICODE_STRING Extension,
        PUNICODE_STRING RedirectedName,
        PUNICODE_STRING RedirectedName2,
        PUNICODE_STRING* OriginalName2,
        PVOID Unknown1,
        PVOID Unknown2,
        PVOID Unknown3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Unknown", "OriginalName", "Extension", "RedirectedName", "RedirectedName2", "OriginalName2", "Unknown1", "Unknown2", "Unknown3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateHeap(jitter):
    """
    PVOID RtlCreateHeap(
        [HEAP_FLAGS_ULONG] Flags,
        PVOID BaseAddress,
        SIZE_T SizeToReserve,
        SIZE_T SizeToCommit,
        PVOID Lock,
        PRTL_HEAP_PARAMETERS Parameters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "BaseAddress", "SizeToReserve", "SizeToCommit", "Lock", "Parameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDestroyHeap(jitter):
    """
    PVOID RtlDestroyHeap(
        PVOID HeapHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAllocateHeap(jitter):
    """
    PVOID RtlAllocateHeap(
        PVOID HeapHandle,
        [HEAP_FLAGS_ULONG] Flags,
        SIZE_T Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeHeap(jitter):
    """
    BOOLEAN RtlFreeHeap(
        PVOID HeapHandle,
        [HEAP_FLAGS_ULONG] Flags,
        PVOID HeapBase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "HeapBase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSizeHeap(jitter):
    """
    SIZE_T RtlSizeHeap(
        PVOID HeapHandle,
        [HEAP_FLAGS_ULONG] Flags,
        PVOID MemoryPointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "MemoryPointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlZeroHeap(jitter):
    """
    NTSTATUS RtlZeroHeap(
        PVOID HeapHandle,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlProtectHeap(jitter):
    """
    PVOID RtlProtectHeap(
        PVOID HeapHandle,
        BOOLEAN Protect
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Protect"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLockHeap(jitter):
    """
    BOOLEAN RtlLockHeap(
        PVOID HeapHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnlockHeap(jitter):
    """
    BOOLEAN RtlUnlockHeap(
        PVOID HeapHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReAllocateHeap(jitter):
    """
    PVOID RtlReAllocateHeap(
        PVOID HeapHandle,
        [HEAP_FLAGS_ULONG] Flags,
        PVOID Ptr,
        SIZE_T Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "Ptr", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetUserInfoHeap(jitter):
    """
    BOOLEAN RtlGetUserInfoHeap(
        PVOID HeapHandle,
        ULONG Flags,
        PVOID BaseAddress,
        PVOID* UserValue,
        PULONG UserFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "BaseAddress", "UserValue", "UserFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetUserValueHeap(jitter):
    """
    BOOLEAN RtlSetUserValueHeap(
        PVOID HeapHandle,
        ULONG Flags,
        PVOID BaseAddress,
        PVOID UserValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "BaseAddress", "UserValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetUserFlagsHeap(jitter):
    """
    BOOLEAN RtlSetUserFlagsHeap(
        PVOID HeapHandle,
        ULONG Flags,
        PVOID BaseAddress,
        ULONG UserFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "BaseAddress", "UserFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateTagHeap(jitter):
    """
    ULONG RtlCreateTagHeap(
        PVOID HeapHandle,
        ULONG Flags,
        PWSTR TagName,
        PWSTR TagSubName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "TagName", "TagSubName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryTagHeap(jitter):
    """
    PWSTR RtlQueryTagHeap(
        PVOID HeapHandle,
        ULONG Flags,
        USHORT TagIndex,
        BOOLEAN ResetCounters,
        PRTL_HEAP_TAG_INFO HeapTagInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "TagIndex", "ResetCounters", "HeapTagInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExtendHeap(jitter):
    """
    ULONG RtlExtendHeap(
        PVOID HeapHandle,
        [HEAP_FLAGS_ULONG] Flags,
        PVOID Base,
        SIZE_T Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "Base", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCompactHeap(jitter):
    """
    ULONG RtlCompactHeap(
        PVOID HeapHandle,
        [HEAP_FLAGS_ULONG] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlValidateHeap(jitter):
    """
    BOOLEAN RtlValidateHeap(
        PVOID HeapHandle,
        [HEAP_FLAGS_ULONG] Flags,
        PVOID BaseAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "BaseAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlValidateProcessHeaps(jitter):
    """
    BOOLEAN RtlValidateProcessHeaps()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetProcessHeaps(jitter):
    """
    ULONG RtlGetProcessHeaps(
        ULONG HeapCount,
        HANDLE* HeapArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapCount", "HeapArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnumProcessHeaps(jitter):
    """
    NTSTATUS RtlEnumProcessHeaps(
        PHEAP_ENUMERATION_ROUTINE HeapEnumerationRoutine,
        PVOID Param
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapEnumerationRoutine", "Param"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUsageHeap(jitter):
    """
    NTSTATUS RtlUsageHeap(
        PVOID HeapHandle,
        [HEAP_FLAGS_ULONG] Flags,
        PRTL_HEAP_USAGE Usage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "Usage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWalkHeap(jitter):
    """
    NTSTATUS RtlWalkHeap(
        PVOID HeapHandle,
        PVOID HeapEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "HeapEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryHeapInformation(jitter):
    """
    NTSTATUS RtlQueryHeapInformation(
        PVOID HeapHandle,
        HEAP_INFORMATION_CLASS HeapInformationClass,
        PVOID HeapInformation,
        SIZE_T HeapInformationLength,
        PSIZE_T ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "HeapInformationClass", "HeapInformation", "HeapInformationLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetHeapInformation(jitter):
    """
    NTSTATUS RtlSetHeapInformation(
        PVOID HeapHandle,
        HEAP_INFORMATION_CLASS HeapInformationClass,
        PVOID HeapInformation,
        SIZE_T HeapInformationLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "HeapInformationClass", "HeapInformation", "HeapInformationLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlMultipleAllocateHeap(jitter):
    """
    ULONG RtlMultipleAllocateHeap(
        PVOID HeapHandle,
        ULONG Flags,
        SIZE_T Size,
        ULONG Count,
        PVOID* Array
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "Size", "Count", "Array"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlMultipleFreeHeap(jitter):
    """
    ULONG RtlMultipleFreeHeap(
        PVOID HeapHandle,
        ULONG Flags,
        ULONG Count,
        PVOID* Array
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HeapHandle", "Flags", "Count", "Array"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDetectHeapLeaks(jitter):
    """
    VOID RtlDetectHeapLeaks()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateMemoryZone(jitter):
    """
    NTSTATUS RtlCreateMemoryZone(
        PVOID* MemoryZone,
        SIZE_T InitialSize,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryZone", "InitialSize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDestroyMemoryZone(jitter):
    """
    NTSTATUS RtlDestroyMemoryZone(
        PVOID MemoryZone
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryZone"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAllocateMemoryZone(jitter):
    """
    NTSTATUS RtlAllocateMemoryZone(
        PVOID MemoryZone,
        SIZE_T BlockSize,
        PVOID* Block
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryZone", "BlockSize", "Block"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlResetMemoryZone(jitter):
    """
    NTSTATUS RtlResetMemoryZone(
        PVOID MemoryZone
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryZone"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLockMemoryZone(jitter):
    """
    NTSTATUS RtlLockMemoryZone(
        PVOID MemoryZone
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryZone"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnlockMemoryZone(jitter):
    """
    NTSTATUS RtlUnlockMemoryZone(
        PVOID MemoryZone
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryZone"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateMemoryBlockLookaside(jitter):
    """
    NTSTATUS RtlCreateMemoryBlockLookaside(
        PVOID* MemoryBlockLookaside,
        ULONG Flags,
        ULONG InitialSize,
        ULONG MinimumBlockSize,
        ULONG MaximumBlockSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryBlockLookaside", "Flags", "InitialSize", "MinimumBlockSize", "MaximumBlockSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDestroyMemoryBlockLookaside(jitter):
    """
    NTSTATUS RtlDestroyMemoryBlockLookaside(
        PVOID MemoryBlockLookaside
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryBlockLookaside"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAllocateMemoryBlockLookaside(jitter):
    """
    NTSTATUS RtlAllocateMemoryBlockLookaside(
        PVOID MemoryBlockLookaside,
        ULONG BlockSize,
        PVOID* Block
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryBlockLookaside", "BlockSize", "Block"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeMemoryBlockLookaside(jitter):
    """
    NTSTATUS RtlFreeMemoryBlockLookaside(
        PVOID MemoryBlockLookaside,
        PVOID Block
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryBlockLookaside", "Block"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExtendMemoryBlockLookaside(jitter):
    """
    NTSTATUS RtlExtendMemoryBlockLookaside(
        PVOID MemoryBlockLookaside,
        ULONG Increment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryBlockLookaside", "Increment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlResetMemoryBlockLookaside(jitter):
    """
    NTSTATUS RtlResetMemoryBlockLookaside(
        PVOID MemoryBlockLookaside
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryBlockLookaside"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLockMemoryBlockLookaside(jitter):
    """
    NTSTATUS RtlLockMemoryBlockLookaside(
        PVOID MemoryBlockLookaside
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryBlockLookaside"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnlockMemoryBlockLookaside(jitter):
    """
    NTSTATUS RtlUnlockMemoryBlockLookaside(
        PVOID MemoryBlockLookaside
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryBlockLookaside"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetCurrentTransaction(jitter):
    """
    HANDLE RtlGetCurrentTransaction()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetCurrentTransaction(jitter):
    """
    LOGICAL RtlSetCurrentTransaction(
        HANDLE TransactionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TransactionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopyLuid(jitter):
    """
    VOID RtlCopyLuid(
        PLUID LuidDest,
        PLUID LuidSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LuidDest", "LuidSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopyLuidAndAttributesArray(jitter):
    """
    VOID RtlCopyLuidAndAttributesArray(
        ULONG Count,
        PLUID_AND_ATTRIBUTES Src,
        PLUID_AND_ATTRIBUTES Dest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Count", "Src", "Dest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateQueryDebugBuffer(jitter):
    """
    PRTL_DEBUG_INFORMATION RtlCreateQueryDebugBuffer(
        ULONG Size,
        BOOLEAN EventPair
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Size", "EventPair"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDestroyQueryDebugBuffer(jitter):
    """
    NTSTATUS RtlDestroyQueryDebugBuffer(
        PRTL_DEBUG_INFORMATION DebugBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DebugBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCommitDebugInfo(jitter):
    """
    PVOID RtlCommitDebugInfo(
        PRTL_DEBUG_INFORMATION Buffer,
        SIZE_T Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeCommitDebugInfo(jitter):
    """
    VOID RtlDeCommitDebugInfo(
        PRTL_DEBUG_INFORMATION Buffer,
        PVOID p,
        SIZE_T Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "p", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryProcessDebugInformation(jitter):
    """
    NTSTATUS RtlQueryProcessDebugInformation(
        ULONG ProcessId,
        [RTL_DEBUG_QUERY_FLAGS] DebugInfoClassMask,
        PRTL_DEBUG_INFORMATION DebugBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessId", "DebugInfoClassMask", "DebugBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindMessage(jitter):
    """
    NTSTATUS RtlFindMessage(
        PVOID BaseAddress,
        ULONG Type,
        ULONG Language,
        ULONG MessageId,
        PRTL_MESSAGE_RESOURCE_ENTRY* MessageResourceEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BaseAddress", "Type", "Language", "MessageId", "MessageResourceEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFormatMessage(jitter):
    """
    NTSTATUS RtlFormatMessage(
        PWSTR MessageFormat,
        ULONG MaximumWidth,
        BOOLEAN IgnoreInserts,
        BOOLEAN ArgumentsAreAnsi,
        BOOLEAN ArgumentsAreAnArray,
        va_list* Arguments,
        PWSTR Buffer,
        ULONG Length,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MessageFormat", "MaximumWidth", "IgnoreInserts", "ArgumentsAreAnsi", "ArgumentsAreAnArray", "Arguments", "Buffer", "Length", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFormatMessageEx(jitter):
    """
    NTSTATUS RtlFormatMessageEx(
        PWSTR MessageFormat,
        ULONG MaximumWidth,
        BOOLEAN IgnoreInserts,
        BOOLEAN ArgumentsAreAnsi,
        BOOLEAN ArgumentsAreAnArray,
        va_list* Arguments,
        PWSTR Buffer,
        ULONG Length,
        PULONG ReturnLength,
        PPARSE_MESSAGE_CONTEXT ParseContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MessageFormat", "MaximumWidth", "IgnoreInserts", "ArgumentsAreAnsi", "ArgumentsAreAnArray", "Arguments", "Buffer", "Length", "ReturnLength", "ParseContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNtStatusToDosError(jitter):
    """
    [ERROR_CODE_ULONG] RtlNtStatusToDosError(
        NTSTATUS Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNtStatusToDosErrorNoTeb(jitter):
    """
    [ERROR_CODE_ULONG] RtlNtStatusToDosErrorNoTeb(
        NTSTATUS Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetLastNtStatus(jitter):
    """
    NTSTATUS RtlGetLastNtStatus()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetLastWin32Error(jitter):
    """
    [ERROR_CODE] RtlGetLastWin32Error()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetLastWin32ErrorAndNtStatusFromNtStatus(jitter):
    """
    VOID RtlSetLastWin32ErrorAndNtStatusFromNtStatus(
        NTSTATUS Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetLastWin32Error(jitter):
    """
    void RtlSetLastWin32Error(
        [ERROR_CODE] err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRestoreLastWin32Error(jitter):
    """
    VOID RtlRestoreLastWin32Error(
        LONG Win32Error
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Win32Error"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetThreadErrorMode(jitter):
    """
    [RTL_ERRORMODE_FLAGS] RtlGetThreadErrorMode()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetThreadErrorMode(jitter):
    """
    NTSTATUS RtlSetThreadErrorMode(
        [RTL_ERRORMODE_FLAGS] NewMode,
        [RTL_ERRORMODE_FLAGS*] OldMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NewMode", "OldMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReportException(jitter):
    """
    NTSTATUS RtlReportException(
        PEXCEPTION_RECORD ExceptionRecord,
        PCONTEXT ContextRecord,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExceptionRecord", "ContextRecord", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWerpReportException(jitter):
    """
    NTSTATUS RtlWerpReportException(
        ULONG ProcessId,
        HANDLE CrashReportSharedMem,
        ULONG Flags,
        PHANDLE CrashVerticalProcessHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessId", "CrashReportSharedMem", "Flags", "CrashVerticalProcessHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReportSilentProcessExit(jitter):
    """
    NTSTATUS RtlReportSilentProcessExit(
        HANDLE ProcessHandle,
        NTSTATUS ExitStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProcessHandle", "ExitStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddVectoredExceptionHandler(jitter):
    """
    PVOID RtlAddVectoredExceptionHandler(
        ULONG FirstHandler,
        PVECTORED_EXCEPTION_HANDLER VectoredHandler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FirstHandler", "VectoredHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRemoveVectoredExceptionHandler(jitter):
    """
    ULONG RtlRemoveVectoredExceptionHandler(
        PVOID Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddVectoredContinueHandler(jitter):
    """
    PVOID RtlAddVectoredContinueHandler(
        ULONG First,
        PVECTORED_EXCEPTION_HANDLER Handler
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["First", "Handler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRemoveVectoredContinueHandler(jitter):
    """
    ULONG RtlRemoveVectoredContinueHandler(
        PVOID Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUniform(jitter):
    """
    ULONG RtlUniform(
        PULONG Seed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Seed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRandom(jitter):
    """
    ULONG RtlRandom(
        PULONG Seed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Seed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRandomEx(jitter):
    """
    ULONG RtlRandomEx(
        PULONG Seed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Seed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlComputeImportTableHash(jitter):
    """
    NTSTATUS RtlComputeImportTableHash(
        HANDLE hFile,
        PCHAR Hash,
        ULONG ImportTableHashRevision
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "Hash", "ImportTableHashRevision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIntegerToChar(jitter):
    """
    NTSTATUS RtlIntegerToChar(
        ULONG Value,
        ULONG Base,
        ULONG Length,
        PCHAR String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Base", "Length", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCharToInteger(jitter):
    """
    NTSTATUS RtlCharToInteger(
        PCSZ String,
        ULONG Base,
        PULONG Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String", "Base", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIntegerToUnicodeString(jitter):
    """
    NTSTATUS RtlIntegerToUnicodeString(
        ULONG Value,
        ULONG Base,
        PUNICODE_STRING String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Base", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInt64ToUnicodeString(jitter):
    """
    NTSTATUS RtlInt64ToUnicodeString(
        ULONGLONG Value,
        ULONG Base,
        PUNICODE_STRING String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Base", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnicodeStringToInteger(jitter):
    """
    NTSTATUS RtlUnicodeStringToInteger(
        PCUNICODE_STRING String,
        ULONG Base,
        PULONG Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String", "Base", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIntegerToUnicode(jitter):
    """
    NTSTATUS RtlIntegerToUnicode(
        ULONG Value,
        ULONG Base,
        ULONG Length,
        LPWSTR String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Base", "Length", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv4AddressToString(jitter, get_str, set_str):
    """
    LPTSTR RtlIpv4AddressToString(
        const IN_ADDR* Addr,
        LPTSTR S
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Addr", "S"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv4AddressToStringA(jitter):
    ntdll_RtlIpv4AddressToString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdll_RtlIpv4AddressToStringW(jitter):
    ntdll_RtlIpv4AddressToString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdll_RtlIpv4AddressToStringEx(jitter, get_str, set_str):
    """
    NTSTATUS RtlIpv4AddressToStringEx(
        const IN_ADDR* Address,
        USHORT Port,
        LPTSTR AddressString,
        PULONG AddressStringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address", "Port", "AddressString", "AddressStringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv4AddressToStringExA(jitter):
    ntdll_RtlIpv4AddressToStringEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdll_RtlIpv4AddressToStringExW(jitter):
    ntdll_RtlIpv4AddressToStringEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdll_RtlIpv6AddressToString(jitter, get_str, set_str):
    """
    LPTSTR RtlIpv6AddressToString(
        const IN6_ADDR* Addr,
        LPTSTR S
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Addr", "S"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv6AddressToStringA(jitter):
    ntdll_RtlIpv6AddressToString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdll_RtlIpv6AddressToStringW(jitter):
    ntdll_RtlIpv6AddressToString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdll_RtlIpv6AddressToStringEx(jitter, get_str, set_str):
    """
    NTSTATUS RtlIpv6AddressToStringEx(
        const IN6_ADDR* Address,
        ULONG ScopeId,
        USHORT Port,
        LPTSTR AddressString,
        PULONG AddressStringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address", "ScopeId", "Port", "AddressString", "AddressStringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv6AddressToStringExA(jitter):
    ntdll_RtlIpv6AddressToStringEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdll_RtlIpv6AddressToStringExW(jitter):
    ntdll_RtlIpv6AddressToStringEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdll_RtlIpv4StringToAddress(jitter, get_str, set_str):
    """
    NTSTATUS RtlIpv4StringToAddress(
        PCTSTR String,
        BOOLEAN Strict,
        LPTSTR* Terminator,
        IN_ADDR* Addr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String", "Strict", "Terminator", "Addr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv4StringToAddressA(jitter):
    ntdll_RtlIpv4StringToAddress(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdll_RtlIpv4StringToAddressW(jitter):
    ntdll_RtlIpv4StringToAddress(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdll_RtlIpv4StringToAddressEx(jitter, get_str, set_str):
    """
    NTSTATUS RtlIpv4StringToAddressEx(
        PCTSTR AddressString,
        BOOLEAN Strict,
        IN_ADDR* Address,
        PUSHORT Port
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AddressString", "Strict", "Address", "Port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv4StringToAddressExA(jitter):
    ntdll_RtlIpv4StringToAddressEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdll_RtlIpv4StringToAddressExW(jitter):
    ntdll_RtlIpv4StringToAddressEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdll_RtlIpv6StringToAddress(jitter, get_str, set_str):
    """
    NTSTATUS RtlIpv6StringToAddress(
        PCTSTR String,
        PCTSTR* Terminator,
        IN6_ADDR* Addr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String", "Terminator", "Addr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv6StringToAddressA(jitter):
    ntdll_RtlIpv6StringToAddress(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdll_RtlIpv6StringToAddressW(jitter):
    ntdll_RtlIpv6StringToAddress(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdll_RtlIpv6StringToAddressEx(jitter, get_str, set_str):
    """
    NTSTATUS RtlIpv6StringToAddressEx(
        PCTSTR AddressString,
        IN6_ADDR* Address,
        PULONG ScopeId,
        PUSHORT Port
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AddressString", "Address", "ScopeId", "Port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIpv6StringToAddressExA(jitter):
    ntdll_RtlIpv6StringToAddressEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def ntdll_RtlIpv6StringToAddressExW(jitter):
    ntdll_RtlIpv6StringToAddressEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def ntdll_RtlCutoverTimeToSystemTime(jitter):
    """
    BOOLEAN RtlCutoverTimeToSystemTime(
        PTIME_FIELDS CutoverTime,
        PLARGE_INTEGER SystemTime,
        PLARGE_INTEGER CurrentSystemTime,
        BOOLEAN ThisYear
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CutoverTime", "SystemTime", "CurrentSystemTime", "ThisYear"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSystemTimeToLocalTime(jitter):
    """
    NTSTATUS RtlSystemTimeToLocalTime(
        PLARGE_INTEGER SystemTime,
        PLARGE_INTEGER LocalTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SystemTime", "LocalTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLocalTimeToSystemTime(jitter):
    """
    NTSTATUS RtlLocalTimeToSystemTime(
        PLARGE_INTEGER LocalTime,
        PLARGE_INTEGER SystemTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LocalTime", "SystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTimeToElapsedTimeFields(jitter):
    """
    VOID RtlTimeToElapsedTimeFields(
        PLARGE_INTEGER Time,
        PTIME_FIELDS TimeFields
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Time", "TimeFields"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTimeToTimeFields(jitter):
    """
    VOID RtlTimeToTimeFields(
        PLARGE_INTEGER Time,
        PTIME_FIELDS TimeFields
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Time", "TimeFields"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTimeFieldsToTime(jitter):
    """
    BOOLEAN RtlTimeFieldsToTime(
        PTIME_FIELDS TimeFields,
        PLARGE_INTEGER Time
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimeFields", "Time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTimeToSecondsSince1980(jitter):
    """
    BOOLEAN RtlTimeToSecondsSince1980(
        PLARGE_INTEGER Time,
        PULONG ElapsedSeconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Time", "ElapsedSeconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSecondsSince1980ToTime(jitter):
    """
    VOID RtlSecondsSince1980ToTime(
        ULONG ElapsedSeconds,
        PLARGE_INTEGER Time
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ElapsedSeconds", "Time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTimeToSecondsSince1970(jitter):
    """
    BOOLEAN RtlTimeToSecondsSince1970(
        PLARGE_INTEGER Time,
        PULONG SecondsSince1970
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Time", "SecondsSince1970"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSecondsSince1970ToTime(jitter):
    """
    VOID RtlSecondsSince1970ToTime(
        ULONG SecondsSince1970,
        PLARGE_INTEGER Time
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecondsSince1970", "Time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryTimeZoneInformation(jitter):
    """
    NTSTATUS RtlQueryTimeZoneInformation(
        PRTL_TIME_ZONE_INFORMATION TimeZoneInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimeZoneInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetTimeZoneInformation(jitter):
    """
    NTSTATUS RtlSetTimeZoneInformation(
        PRTL_TIME_ZONE_INFORMATION TimeZoneInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimeZoneInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeBitMap(jitter):
    """
    VOID RtlInitializeBitMap(
        PRTL_BITMAP BitMapHeader,
        PULONG BitMapBuffer,
        ULONG SizeOfBitMap
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "BitMapBuffer", "SizeOfBitMap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlClearBit(jitter):
    """
    VOID RtlClearBit(
        PRTL_BITMAP BitMapHeader,
        ULONG BitNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "BitNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetBit(jitter):
    """
    VOID RtlSetBit(
        PRTL_BITMAP BitMapHeader,
        ULONG BitNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "BitNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlTestBit(jitter):
    """
    BOOLEAN RtlTestBit(
        PRTL_BITMAP BitMapHeader,
        ULONG BitNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "BitNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlClearAllBits(jitter):
    """
    VOID RtlClearAllBits(
        PRTL_BITMAP BitMapHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetAllBits(jitter):
    """
    VOID RtlSetAllBits(
        PRTL_BITMAP BitMapHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindClearBits(jitter):
    """
    ULONG RtlFindClearBits(
        PRTL_BITMAP BitMapHeader,
        ULONG NumberToFind,
        ULONG HintIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "NumberToFind", "HintIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindClearBitsAndSet(jitter):
    """
    ULONG RtlFindClearBitsAndSet(
        PRTL_BITMAP BitMapHeader,
        ULONG NumberToFind,
        ULONG HintIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "NumberToFind", "HintIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindSetBitsAndClear(jitter):
    """
    ULONG RtlFindSetBitsAndClear(
        PRTL_BITMAP BitMapHeader,
        ULONG NumberToFind,
        ULONG HintIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "NumberToFind", "HintIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlClearBits(jitter):
    """
    VOID RtlClearBits(
        PRTL_BITMAP BitMapHeader,
        ULONG StartingIndex,
        ULONG NumberToClear
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "StartingIndex", "NumberToClear"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetBits(jitter):
    """
    VOID RtlSetBits(
        PRTL_BITMAP BitMapHeader,
        ULONG StartingIndex,
        ULONG NumberToSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "StartingIndex", "NumberToSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindClearRuns(jitter):
    """
    ULONG RtlFindClearRuns(
        PRTL_BITMAP BitMapHeader,
        PRTL_BITMAP_RUN RunArray,
        ULONG SizeOfRunArray,
        BOOLEAN LocateLongestRuns
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "RunArray", "SizeOfRunArray", "LocateLongestRuns"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindLongestRunClear(jitter):
    """
    ULONG RtlFindLongestRunClear(
        PRTL_BITMAP BitMapHeader,
        PULONG StartingIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "StartingIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindFirstRunClear(jitter):
    """
    ULONG RtlFindFirstRunClear(
        PRTL_BITMAP BitMapHeader,
        PULONG StartingIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "StartingIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNumberOfClearBits(jitter):
    """
    ULONG RtlNumberOfClearBits(
        PRTL_BITMAP BitMapHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNumberOfSetBits(jitter):
    """
    ULONG RtlNumberOfSetBits(
        PRTL_BITMAP BitMapHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAreBitsClear(jitter):
    """
    BOOLEAN RtlAreBitsClear(
        PRTL_BITMAP BitMapHeader,
        ULONG StartingIndex,
        ULONG Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "StartingIndex", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAreBitsSet(jitter):
    """
    BOOLEAN RtlAreBitsSet(
        PRTL_BITMAP BitMapHeader,
        ULONG StartingIndex,
        ULONG Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "StartingIndex", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindNextForwardRunClear(jitter):
    """
    ULONG RtlFindNextForwardRunClear(
        PRTL_BITMAP BitMapHeader,
        ULONG FromIndex,
        PULONG StartingRunIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "FromIndex", "StartingRunIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindLastBackwardRunClear(jitter):
    """
    ULONG RtlFindLastBackwardRunClear(
        PRTL_BITMAP BitMapHeader,
        ULONG FromIndex,
        PULONG StartingRunIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "FromIndex", "StartingRunIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInterlockedClearBitRun(jitter):
    """
    VOID RtlInterlockedClearBitRun(
        PRTL_BITMAP BitMapHeader,
        ULONG StartingIndex,
        ULONG NumberToClear
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "StartingIndex", "NumberToClear"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInterlockedSetBitRun(jitter):
    """
    VOID RtlInterlockedSetBitRun(
        PRTL_BITMAP BitMapHeader,
        ULONG StartingIndex,
        ULONG NumberToSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "StartingIndex", "NumberToSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindLeastSignificantBit(jitter):
    """
    CCHAR RtlFindLeastSignificantBit(
        ULONGLONG Set
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Set"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindMostSignificantBit(jitter):
    """
    CCHAR RtlFindMostSignificantBit(
        ULONGLONG Set
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Set"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindSetBits(jitter):
    """
    ULONG RtlFindSetBits(
        PRTL_BITMAP BitMapHeader,
        ULONG NumberToFind,
        ULONG HintIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BitMapHeader", "NumberToFind", "HintIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNumberOfSetBitsUlongPtr(jitter):
    """
    ULONG RtlNumberOfSetBitsUlongPtr(
        ULONG_PTR Target
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Target"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeHandleTable(jitter):
    """
    VOID RtlInitializeHandleTable(
        ULONG TableSize,
        ULONG HandleSize,
        PRTL_HANDLE_TABLE HandleTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TableSize", "HandleSize", "HandleTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDestroyHandleTable(jitter):
    """
    VOID RtlDestroyHandleTable(
        PRTL_HANDLE_TABLE HandleTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAllocateHandle(jitter):
    """
    PRTL_HANDLE_TABLE_ENTRY RtlAllocateHandle(
        PRTL_HANDLE_TABLE HandleTable,
        PULONG Index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleTable", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeHandle(jitter):
    """
    BOOLEAN RtlFreeHandle(
        PRTL_HANDLE_TABLE HandleTable,
        PRTL_HANDLE_TABLE_ENTRY Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleTable", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsValidHandle(jitter):
    """
    BOOLEAN RtlIsValidHandle(
        PRTL_HANDLE_TABLE HandleTable,
        PRTL_HANDLE_TABLE_ENTRY Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleTable", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsValidIndexHandle(jitter):
    """
    BOOLEAN RtlIsValidIndexHandle(
        PRTL_HANDLE_TABLE HandleTable,
        ULONG Index,
        PRTL_HANDLE_TABLE_ENTRY* Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HandleTable", "Index", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateAtomTable(jitter):
    """
    NTSTATUS RtlCreateAtomTable(
        ULONG TableSize,
        PRTL_ATOM_TABLE* AtomTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TableSize", "AtomTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDestroyAtomTable(jitter):
    """
    NTSTATUS RtlDestroyAtomTable(
        PRTL_ATOM_TABLE AtomTable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomTable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEmptyAtomTable(jitter):
    """
    NTSTATUS RtlEmptyAtomTable(
        PVOID AtomTableHandle,
        BOOLEAN IncludePinnedAtoms
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomTableHandle", "IncludePinnedAtoms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAtomToAtomTable(jitter):
    """
    NTSTATUS RtlAddAtomToAtomTable(
        PRTL_ATOM_TABLE AtomTable,
        PWSTR AtomName,
        PRTL_ATOM Atom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomTable", "AtomName", "Atom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLookupAtomInAtomTable(jitter):
    """
    NTSTATUS RtlLookupAtomInAtomTable(
        PRTL_ATOM_TABLE AtomTable,
        PWSTR AtomName,
        PRTL_ATOM Atom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomTable", "AtomName", "Atom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteAtomFromAtomTable(jitter):
    """
    NTSTATUS RtlDeleteAtomFromAtomTable(
        PRTL_ATOM_TABLE AtomTable,
        RTL_ATOM Atom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomTable", "Atom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlPinAtomInAtomTable(jitter):
    """
    NTSTATUS RtlPinAtomInAtomTable(
        PRTL_ATOM_TABLE AtomTable,
        RTL_ATOM Atom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomTable", "Atom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryAtomInAtomTable(jitter):
    """
    NTSTATUS RtlQueryAtomInAtomTable(
        PRTL_ATOM_TABLE AtomTable,
        RTL_ATOM Atom,
        PULONG RefCount,
        PULONG PinCount,
        PWSTR AtomName,
        PULONG NameLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomTable", "Atom", "RefCount", "PinCount", "AtomName", "NameLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetIntegerAtom(jitter):
    """
    BOOLEAN RtlGetIntegerAtom(
        PWSTR AtomName,
        PUSHORT IntegerAtom
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AtomName", "IntegerAtom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlValidSid(jitter):
    """
    BOOLEAN RtlValidSid(
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEqualSid(jitter):
    """
    BOOLEAN RtlEqualSid(
        PSID Sid1,
        PSID Sid2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid1", "Sid2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLengthRequiredSid(jitter):
    """
    ULONG RtlLengthRequiredSid(
        ULONG SubAuthorityCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubAuthorityCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeSid(jitter):
    """
    PVOID RtlFreeSid(
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAllocateAndInitializeSid(jitter):
    """
    NTSTATUS RtlAllocateAndInitializeSid(
        PSID_IDENTIFIER_AUTHORITY IdentifierAuthority,
        UCHAR SubAuthorityCount,
        ULONG SubAuthority0,
        ULONG SubAuthority1,
        ULONG SubAuthority2,
        ULONG SubAuthority3,
        ULONG SubAuthority4,
        ULONG SubAuthority5,
        ULONG SubAuthority6,
        ULONG SubAuthority7,
        PSID* Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IdentifierAuthority", "SubAuthorityCount", "SubAuthority0", "SubAuthority1", "SubAuthority2", "SubAuthority3", "SubAuthority4", "SubAuthority5", "SubAuthority6", "SubAuthority7", "Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlInitializeSid(jitter):
    """
    NTSTATUS RtlInitializeSid(
        PSID Sid,
        PSID_IDENTIFIER_AUTHORITY IdentifierAuthority,
        UCHAR SubAuthorityCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid", "IdentifierAuthority", "SubAuthorityCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIdentifierAuthoritySid(jitter):
    """
    PSID_IDENTIFIER_AUTHORITY RtlIdentifierAuthoritySid(
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSubAuthoritySid(jitter):
    """
    PULONG RtlSubAuthoritySid(
        PSID Sid,
        ULONG SubAuthority
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid", "SubAuthority"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSubAuthorityCountSid(jitter):
    """
    PUCHAR RtlSubAuthorityCountSid(
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLengthSid(jitter):
    """
    ULONG RtlLengthSid(
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopySid(jitter):
    """
    NTSTATUS RtlCopySid(
        ULONG Length,
        PSID Destination,
        PSID Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Length", "Destination", "Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateServiceSid(jitter):
    """
    NTSTATUS RtlCreateServiceSid(
        PUNICODE_STRING ServiceName,
        PSID ServiceSid,
        PULONG ServiceSidLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServiceName", "ServiceSid", "ServiceSidLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSidDominates(jitter):
    """
    NTSTATUS RtlSidDominates(
        PSID Sid1,
        PSID Sid2,
        PBOOLEAN pbDominate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid1", "Sid2", "pbDominate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSidEqualLevel(jitter):
    """
    NTSTATUS RtlSidEqualLevel(
        PSID Sid1,
        PSID Sid2,
        PBOOLEAN pbEqual
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid1", "Sid2", "pbEqual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSidIsHigherLevel(jitter):
    """
    NTSTATUS RtlSidIsHigherLevel(
        PSID Sid1,
        PSID Sid2,
        PBOOLEAN pbHigher
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid1", "Sid2", "pbHigher"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateVirtualAccountSid(jitter):
    """
    NTSTATUS RtlCreateVirtualAccountSid(
        PUNICODE_STRING Name,
        ULONG BaseSubAuthority,
        PSID Sid,
        PULONG SidLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "BaseSubAuthority", "Sid", "SidLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReplaceSidInSd(jitter):
    """
    NTSTATUS RtlReplaceSidInSd(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID OldSid,
        PSID NewSid,
        ULONG* NumChanges
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "OldSid", "NewSid", "NumChanges"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlConvertSidToUnicodeString(jitter):
    """
    NTSTATUS RtlConvertSidToUnicodeString(
        PUNICODE_STRING DestinationString,
        PSID Sid,
        BOOLEAN AllocateDestinationString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestinationString", "Sid", "AllocateDestinationString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSidHashInitialize(jitter):
    """
    NTSTATUS RtlSidHashInitialize(
        PSID_AND_ATTRIBUTES SidAttr,
        ULONG SidCount,
        PSID_AND_ATTRIBUTES_HASH SidAttrHash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SidAttr", "SidCount", "SidAttrHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSidHashLookup(jitter):
    """
    PSID_AND_ATTRIBUTES RtlSidHashLookup(
        PSID_AND_ATTRIBUTES_HASH SidAttrHash,
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SidAttrHash", "Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopySidAndAttributesArray(jitter):
    """
    NTSTATUS RtlCopySidAndAttributesArray(
        ULONG Count,
        PSID_AND_ATTRIBUTES Src,
        ULONG SidAreaSize,
        PSID_AND_ATTRIBUTES Dest,
        PVOID SidArea,
        PVOID* RemainingSidArea,
        PULONG RemainingSidAreaSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Count", "Src", "SidAreaSize", "Dest", "SidArea", "RemainingSidArea", "RemainingSidAreaSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateSecurityDescriptor(jitter):
    """
    NTSTATUS RtlCreateSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        ULONG Revision
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "Revision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlValidSecurityDescriptor(jitter):
    """
    BOOLEAN RtlValidSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLengthSecurityDescriptor(jitter):
    """
    ULONG RtlLengthSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlValidRelativeSecurityDescriptor(jitter):
    """
    BOOLEAN RtlValidRelativeSecurityDescriptor(
        PSECURITY_DESCRIPTOR_RELATIVE SecurityDescriptorInput,
        ULONG SecurityDescriptorLength,
        SECURITY_INFORMATION RequiredInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptorInput", "SecurityDescriptorLength", "RequiredInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetControlSecurityDescriptor(jitter):
    """
    NTSTATUS RtlGetControlSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSECURITY_DESCRIPTOR_CONTROL Control,
        PULONG Revision
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "Control", "Revision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetControlSecurityDescriptor(jitter):
    """
    NTSTATUS RtlSetControlSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        SECURITY_DESCRIPTOR_CONTROL ControlBitsOfInterest,
        SECURITY_DESCRIPTOR_CONTROL ControlBitsToSet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "ControlBitsOfInterest", "ControlBitsToSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetAttributesSecurityDescriptor(jitter):
    """
    NTSTATUS RtlSetAttributesSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        SECURITY_DESCRIPTOR_CONTROL Control,
        PULONG Revision
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "Control", "Revision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetSecurityDescriptorRMControl(jitter):
    """
    BOOLEAN RtlGetSecurityDescriptorRMControl(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PUCHAR RMControl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "RMControl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetSecurityDescriptorRMControl(jitter):
    """
    VOID RtlSetSecurityDescriptorRMControl(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PUCHAR RMControl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "RMControl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetDaclSecurityDescriptor(jitter):
    """
    NTSTATUS RtlSetDaclSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        BOOLEAN DaclPresent,
        PACL Dacl,
        BOOLEAN DaclDefaulted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "DaclPresent", "Dacl", "DaclDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetDaclSecurityDescriptor(jitter):
    """
    NTSTATUS RtlGetDaclSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PBOOLEAN DaclPresent,
        PACL* Dacl,
        PBOOLEAN DaclDefaulted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "DaclPresent", "Dacl", "DaclDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetSaclSecurityDescriptor(jitter):
    """
    NTSTATUS RtlSetSaclSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        BOOLEAN SaclPresent,
        PACL Sacl,
        BOOLEAN SaclDefaulted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "SaclPresent", "Sacl", "SaclDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetSaclSecurityDescriptor(jitter):
    """
    NTSTATUS RtlGetSaclSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PBOOLEAN SaclPresent,
        PACL* Sacl,
        PBOOLEAN SaclDefaulted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "SaclPresent", "Sacl", "SaclDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetOwnerSecurityDescriptor(jitter):
    """
    NTSTATUS RtlSetOwnerSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID Owner,
        BOOLEAN OwnerDefaulted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "Owner", "OwnerDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetOwnerSecurityDescriptor(jitter):
    """
    NTSTATUS RtlGetOwnerSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID* Owner,
        PBOOLEAN OwnerDefaulted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "Owner", "OwnerDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetGroupSecurityDescriptor(jitter):
    """
    NTSTATUS RtlSetGroupSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID Group,
        BOOLEAN GroupDefaulted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "Group", "GroupDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetGroupSecurityDescriptor(jitter):
    """
    NTSTATUS RtlGetGroupSecurityDescriptor(
        PSECURITY_DESCRIPTOR SecurityDescriptor,
        PSID* Group,
        PBOOLEAN GroupDefaulted
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "Group", "GroupDefaulted"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlMakeSelfRelativeSD(jitter):
    """
    NTSTATUS RtlMakeSelfRelativeSD(
        PSECURITY_DESCRIPTOR AbsoluteSD,
        PSECURITY_DESCRIPTOR_RELATIVE SelfRelativeSD,
        PULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AbsoluteSD", "SelfRelativeSD", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAbsoluteToSelfRelativeSD(jitter):
    """
    NTSTATUS RtlAbsoluteToSelfRelativeSD(
        PSECURITY_DESCRIPTOR AbsoluteSecurityDescriptor,
        PSECURITY_DESCRIPTOR_RELATIVE SelfRelativeSecurityDescriptor,
        PULONG BufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AbsoluteSecurityDescriptor", "SelfRelativeSecurityDescriptor", "BufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSelfRelativeToAbsoluteSD(jitter):
    """
    NTSTATUS RtlSelfRelativeToAbsoluteSD(
        PSECURITY_DESCRIPTOR_RELATIVE SelfRelativeSD,
        PSECURITY_DESCRIPTOR AbsoluteSD,
        PULONG AbsoluteSDSize,
        PACL Dacl,
        PULONG DaclSize,
        PACL Sacl,
        PULONG SaclSize,
        PSID Owner,
        PULONG OwnerSize,
        PSID PrimaryGroup,
        PULONG PrimaryGroupSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SelfRelativeSD", "AbsoluteSD", "AbsoluteSDSize", "Dacl", "DaclSize", "Sacl", "SaclSize", "Owner", "OwnerSize", "PrimaryGroup", "PrimaryGroupSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSelfRelativeToAbsoluteSD2(jitter):
    """
    NTSTATUS RtlSelfRelativeToAbsoluteSD2(
        PSECURITY_DESCRIPTOR_RELATIVE SelfRelativeSD,
        PULONG BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SelfRelativeSD", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCopySecurityDescriptor(jitter):
    """
    NTSTATUS RtlCopySecurityDescriptor(
        PSECURITY_DESCRIPTOR pSourceSecurityDescriptor,
        PSECURITY_DESCRIPTOR pDestinationSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSourceSecurityDescriptor", "pDestinationSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateSecurityDescriptorRelative(jitter):
    """
    NTSTATUS RtlCreateSecurityDescriptorRelative(
        PISECURITY_DESCRIPTOR_RELATIVE SecurityDescriptor,
        ULONG Revision
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityDescriptor", "Revision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAreAllAccessesGranted(jitter):
    """
    BOOLEAN RtlAreAllAccessesGranted(
        ACCESS_MASK GrantedAccess,
        ACCESS_MASK DesiredAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["GrantedAccess", "DesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAreAnyAccessesGranted(jitter):
    """
    BOOLEAN RtlAreAnyAccessesGranted(
        ACCESS_MASK GrantedAccess,
        ACCESS_MASK DesiredAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["GrantedAccess", "DesiredAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlMapGenericMask(jitter):
    """
    VOID RtlMapGenericMask(
        PACCESS_MASK AccessMask,
        PGENERIC_MAPPING GenericMapping
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AccessMask", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateAcl(jitter):
    """
    NTSTATUS RtlCreateAcl(
        PACL Acl,
        ULONG AclSize,
        ULONG AclRevision
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "AclSize", "AclRevision"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlValidAcl(jitter):
    """
    BOOLEAN RtlValidAcl(
        PACL Acl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryInformationAcl(jitter):
    """
    NTSTATUS RtlQueryInformationAcl(
        PACL Acl,
        PVOID Information,
        ULONG InformationLength,
        ACL_INFORMATION_CLASS InformationClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Information", "InformationLength", "InformationClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetInformationAcl(jitter):
    """
    NTSTATUS RtlSetInformationAcl(
        PACL Acl,
        PVOID Information,
        ULONG InformationLength,
        ACL_INFORMATION_CLASS InformationClass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Information", "InformationLength", "InformationClass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAce(jitter):
    """
    NTSTATUS RtlAddAce(
        PACL Acl,
        ULONG AceRevision,
        ULONG StartingAceIndex,
        PVOID AceList,
        ULONG AceListLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "AceRevision", "StartingAceIndex", "AceList", "AceListLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteAce(jitter):
    """
    NTSTATUS RtlDeleteAce(
        PACL Acl,
        ULONG AceIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "AceIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetAce(jitter):
    """
    NTSTATUS RtlGetAce(
        PACL Acl,
        ULONG AceIndex,
        PACE* Ace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "AceIndex", "Ace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFirstFreeAce(jitter):
    """
    BOOLEAN RtlFirstFreeAce(
        PACL Acl,
        PACE* Ace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Ace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindAceByType(jitter):
    """
    PVOID RtlFindAceByType(
        PACL pAcl,
        [ACE_TYPE|UCHAR] AceType,
        PULONG pIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "AceType", "pIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlOwnerAcesPresent(jitter):
    """
    BOOLEAN RtlOwnerAcesPresent(
        PACL pAcl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAcl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAccessAllowedAce(jitter):
    """
    NTSTATUS RtlAddAccessAllowedAce(
        PACL Acl,
        ULONG AceRevision,
        ACCESS_MASK AccessMask,
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "AceRevision", "AccessMask", "Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAccessAllowedAceEx(jitter):
    """
    NTSTATUS RtlAddAccessAllowedAceEx(
        PACL pAcl,
        ULONG AceRevision,
        [ACE_FLAGS_ULONG] AceFlags,
        ACCESS_MASK AccessMask,
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "AceRevision", "AceFlags", "AccessMask", "Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAccessDeniedAce(jitter):
    """
    NTSTATUS RtlAddAccessDeniedAce(
        PACL Acl,
        ULONG Revision,
        ACCESS_MASK AccessMask,
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Revision", "AccessMask", "Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAccessDeniedAceEx(jitter):
    """
    NTSTATUS RtlAddAccessDeniedAceEx(
        PACL Acl,
        ULONG Revision,
        ULONG Flags,
        ACCESS_MASK AccessMask,
        PSID Sid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Revision", "Flags", "AccessMask", "Sid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAuditAccessAce(jitter):
    """
    NTSTATUS RtlAddAuditAccessAce(
        PACL Acl,
        ULONG Revision,
        ACCESS_MASK AccessMask,
        PSID Sid,
        BOOLEAN Success,
        BOOLEAN Failure
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Revision", "AccessMask", "Sid", "Success", "Failure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAuditAccessAceEx(jitter):
    """
    NTSTATUS RtlAddAuditAccessAceEx(
        PACL Acl,
        ULONG Revision,
        ULONG Flags,
        ACCESS_MASK AccessMask,
        PSID Sid,
        BOOLEAN Success,
        BOOLEAN Failure
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Revision", "Flags", "AccessMask", "Sid", "Success", "Failure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAccessAllowedObjectAce(jitter):
    """
    NTSTATUS RtlAddAccessAllowedObjectAce(
        PACL pAcl,
        ULONG dwAceRevision,
        [ACE_FLAGS_ULONG] AceFlags,
        ACCESS_MASK AccessMask,
        GUID* ObjectTypeGuid,
        GUID* InheritedObjectTypeGuid,
        PSID pSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "ObjectTypeGuid", "InheritedObjectTypeGuid", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAccessDeniedObjectAce(jitter):
    """
    NTSTATUS RtlAddAccessDeniedObjectAce(
        PACL pAcl,
        ULONG dwAceRevision,
        [ACE_FLAGS_ULONG] AceFlags,
        ACCESS_MASK AccessMask,
        GUID* ObjectTypeGuid,
        GUID* InheritedObjectTypeGuid,
        PSID pSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAcl", "dwAceRevision", "AceFlags", "AccessMask", "ObjectTypeGuid", "InheritedObjectTypeGuid", "pSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddAuditAccessObjectAce(jitter):
    """
    NTSTATUS RtlAddAuditAccessObjectAce(
        PACL Acl,
        ULONG Revision,
        ULONG Flags,
        ACCESS_MASK AccessMask,
        GUID* ObjectTypeGuid,
        GUID* InheritedObjectTypeGuid,
        PSID Sid,
        BOOLEAN Success,
        BOOLEAN Failure
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Revision", "Flags", "AccessMask", "ObjectTypeGuid", "InheritedObjectTypeGuid", "Sid", "Success", "Failure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddCompoundAce(jitter):
    """
    NTSTATUS RtlAddCompoundAce(
        PACL Acl,
        ULONG AceRevision,
        [ACE_TYPE|UCHAR] AceType,
        ACCESS_MASK AccessMask,
        PSID ServerSid,
        PSID ClientSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "AceRevision", "AceType", "AccessMask", "ServerSid", "ClientSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddMandatoryAce(jitter):
    """
    NTSTATUS RtlAddMandatoryAce(
        PACL Acl,
        ULONG Revision,
        ULONG Flags,
        ULONG MandatoryFlags,
        [ACE_TYPE|UCHAR] AceType,
        PSID LabelSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Acl", "Revision", "Flags", "MandatoryFlags", "AceType", "LabelSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNewSecurityObject(jitter):
    """
    NTSTATUS RtlNewSecurityObject(
        PSECURITY_DESCRIPTOR ParentDescriptor,
        PSECURITY_DESCRIPTOR CreatorDescriptor,
        PSECURITY_DESCRIPTOR* NewDescriptor,
        BOOLEAN IsDirectoryObject,
        HANDLE Token,
        PGENERIC_MAPPING GenericMapping
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptor", "CreatorDescriptor", "NewDescriptor", "IsDirectoryObject", "Token", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNewSecurityObjectEx(jitter):
    """
    NTSTATUS RtlNewSecurityObjectEx(
        PSECURITY_DESCRIPTOR ParentDescriptor,
        PSECURITY_DESCRIPTOR CreatorDescriptor,
        PSECURITY_DESCRIPTOR* NewDescriptor,
        GUID* ObjectType,
        BOOLEAN IsDirectoryObject,
        ULONG AutoInheritFlags,
        HANDLE Token,
        PGENERIC_MAPPING GenericMapping
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptor", "CreatorDescriptor", "NewDescriptor", "ObjectType", "IsDirectoryObject", "AutoInheritFlags", "Token", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNewSecurityObjectWithMultipleInheritance(jitter):
    """
    NTSTATUS RtlNewSecurityObjectWithMultipleInheritance(
        PSECURITY_DESCRIPTOR ParentDescriptor,
        PSECURITY_DESCRIPTOR CreatorDescriptor,
        PSECURITY_DESCRIPTOR* NewDescriptor,
        GUID** ObjectType,
        ULONG GuidCount,
        BOOLEAN IsDirectoryObject,
        ULONG AutoInheritFlags,
        HANDLE Token,
        PGENERIC_MAPPING GenericMapping
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptor", "CreatorDescriptor", "NewDescriptor", "ObjectType", "GuidCount", "IsDirectoryObject", "AutoInheritFlags", "Token", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteSecurityObject(jitter):
    """
    NTSTATUS RtlDeleteSecurityObject(
        PSECURITY_DESCRIPTOR* ObjectDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQuerySecurityObject(jitter):
    """
    NTSTATUS RtlQuerySecurityObject(
        PSECURITY_DESCRIPTOR ObjectDescriptor,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR ResultantDescriptor,
        ULONG DescriptorLength,
        PULONG ReturnLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectDescriptor", "SecurityInformation", "ResultantDescriptor", "DescriptorLength", "ReturnLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetSecurityObject(jitter):
    """
    NTSTATUS RtlSetSecurityObject(
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR ModificationDescriptor,
        PSECURITY_DESCRIPTOR* ObjectsSecurityDescriptor,
        PGENERIC_MAPPING GenericMapping,
        HANDLE Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityInformation", "ModificationDescriptor", "ObjectsSecurityDescriptor", "GenericMapping", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetSecurityObjectEx(jitter):
    """
    NTSTATUS RtlSetSecurityObjectEx(
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR ModificationDescriptor,
        PSECURITY_DESCRIPTOR* ObjectsSecurityDescriptor,
        ULONG AutoInheritFlags,
        PGENERIC_MAPPING GenericMapping,
        HANDLE Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SecurityInformation", "ModificationDescriptor", "ObjectsSecurityDescriptor", "AutoInheritFlags", "GenericMapping", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlConvertToAutoInheritSecurityObject(jitter):
    """
    NTSTATUS RtlConvertToAutoInheritSecurityObject(
        PSECURITY_DESCRIPTOR ParentDescriptor,
        PSECURITY_DESCRIPTOR CurrentSecurityDescriptor,
        PSECURITY_DESCRIPTOR* NewSecurityDescriptor,
        GUID* ObjectType,
        BOOLEAN IsDirectoryObject,
        PGENERIC_MAPPING GenericMapping
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptor", "CurrentSecurityDescriptor", "NewSecurityDescriptor", "ObjectType", "IsDirectoryObject", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlNewInstanceSecurityObject(jitter):
    """
    NTSTATUS RtlNewInstanceSecurityObject(
        BOOLEAN ParentDescriptorChanged,
        BOOLEAN CreatorDescriptorChanged,
        PLUID OldClientTokenModifiedId,
        PLUID NewClientTokenModifiedId,
        PSECURITY_DESCRIPTOR ParentDescriptor,
        PSECURITY_DESCRIPTOR CreatorDescriptor,
        PSECURITY_DESCRIPTOR* NewDescriptor,
        BOOLEAN IsDirectoryObject,
        HANDLE Token,
        PGENERIC_MAPPING GenericMapping
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ParentDescriptorChanged", "CreatorDescriptorChanged", "OldClientTokenModifiedId", "NewClientTokenModifiedId", "ParentDescriptor", "CreatorDescriptor", "NewDescriptor", "IsDirectoryObject", "Token", "GenericMapping"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRunEncodeUnicodeString(jitter):
    """
    VOID RtlRunEncodeUnicodeString(
        PUCHAR Seed,
        PUNICODE_STRING String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Seed", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRunDecodeUnicodeString(jitter):
    """
    VOID RtlRunDecodeUnicodeString(
        UCHAR Seed,
        PUNICODE_STRING String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Seed", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlImpersonateSelf(jitter):
    """
    NTSTATUS RtlImpersonateSelf(
        SECURITY_IMPERSONATION_LEVEL ImpersonationLevel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImpersonationLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlImpersonateSelfEx(jitter):
    """
    NTSTATUS RtlImpersonateSelfEx(
        SECURITY_IMPERSONATION_LEVEL ImpersonationLevel,
        ACCESS_MASK AdditionalAccess,
        PHANDLE ThreadToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ImpersonationLevel", "AdditionalAccess", "ThreadToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAdjustPrivilege(jitter):
    """
    NTSTATUS RtlAdjustPrivilege(
        ULONG Privilege,
        BOOLEAN NewValue,
        BOOLEAN ForThread,
        PBOOLEAN OldValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Privilege", "NewValue", "ForThread", "OldValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAcquirePrivilege(jitter):
    """
    NTSTATUS RtlAcquirePrivilege(
        PULONG Privilege,
        ULONG NumPriv,
        [RTL_ACQUIRE_PRIVILEGE_FLAGS] Flags,
        PVOID* ReturnedState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Privilege", "NumPriv", "Flags", "ReturnedState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReleasePrivilege(jitter):
    """
    VOID RtlReleasePrivilege(
        PVOID ReturnedState
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReturnedState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRemovePrivileges(jitter):
    """
    NTSTATUS RtlRemovePrivileges(
        HANDLE hToken,
        PULONG PrivilegesToKeep,
        ULONG PrivilegeCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hToken", "PrivilegesToKeep", "PrivilegeCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateBoundaryDescriptor(jitter):
    """
    PVOID RtlCreateBoundaryDescriptor(
        PUNICODE_STRING Name,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Name", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteBoundaryDescriptor(jitter):
    """
    VOID RtlDeleteBoundaryDescriptor(
        PVOID BoundaryDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BoundaryDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddSIDToBoundaryDescriptor(jitter):
    """
    NTSTATUS RtlAddSIDToBoundaryDescriptor(
        PVOID* BoundaryDescriptor,
        PSID RequiredSid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BoundaryDescriptor", "RequiredSid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddIntegrityLabelToBoundaryDescriptor(jitter):
    """
    NTSTATUS RtlAddIntegrityLabelToBoundaryDescriptor(
        PVOID* BoundaryDescriptor,
        PSID IntegrityLabel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BoundaryDescriptor", "IntegrityLabel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetVersion(jitter):
    """
    NTSTATUS RtlGetVersion(
        PRTL_OSVERSIONINFOW lpVersionInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpVersionInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlVerifyVersionInfo(jitter):
    """
    NTSTATUS RtlVerifyVersionInfo(
        PRTL_OSVERSIONINFOEXW VersionInfo,
        [NtVerType] TypeMask,
        ULONGLONG ConditionMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["VersionInfo", "TypeMask", "ConditionMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetNtGlobalFlags(jitter):
    """
    ULONG RtlGetNtGlobalFlags()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetNtProductType(jitter):
    """
    BOOLEAN RtlGetNtProductType(
        PNT_PRODUCT_TYPE ProductType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProductType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetNtVersionNumbers(jitter):
    """
    VOID RtlGetNtVersionNumbers(
        PULONG pNtMajorVersion,
        PULONG pNtMinorVersion,
        PULONG pNtBuildNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pNtMajorVersion", "pNtMinorVersion", "pNtBuildNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRegisterWait(jitter):
    """
    NTSTATUS RtlRegisterWait(
        PHANDLE phNewWaitObject,
        HANDLE hObject,
        WAITORTIMERCALLBACKFUNC Callback,
        PVOID pvContext,
        ULONG ulMilliseconds,
        ULONG ulFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phNewWaitObject", "hObject", "Callback", "pvContext", "ulMilliseconds", "ulFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeregisterWait(jitter):
    """
    NTSTATUS RtlDeregisterWait(
        HANDLE hWaitHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWaitHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeregisterWaitEx(jitter):
    """
    NTSTATUS RtlDeregisterWaitEx(
        HANDLE hWaitHandle,
        HANDLE hCompletionEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWaitHandle", "hCompletionEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueueWorkItem(jitter):
    """
    NTSTATUS RtlQueueWorkItem(
        WORKERCALLBACKFUNC Function,
        PVOID Context,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Function", "Context", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlSetIoCompletionCallback(jitter):
    """
    NTSTATUS RtlSetIoCompletionCallback(
        HANDLE FileHandle,
        PIO_APC_ROUTINE Callback,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FileHandle", "Callback", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateTimerQueue(jitter):
    """
    NTSTATUS RtlCreateTimerQueue(
        PHANDLE TimerQueue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateTimer(jitter):
    """
    NTSTATUS RtlCreateTimer(
        HANDLE TimerQueue,
        PHANDLE phNewTimer,
        WAITORTIMERCALLBACKFUNC Callback,
        PVOID Parameter,
        ULONG DueTime,
        ULONG Period,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue", "phNewTimer", "Callback", "Parameter", "DueTime", "Period", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUpdateTimer(jitter):
    """
    NTSTATUS RtlUpdateTimer(
        HANDLE TimerQueue,
        HANDLE Timer,
        ULONG DueTime,
        ULONG Period
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue", "Timer", "DueTime", "Period"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteTimer(jitter):
    """
    NTSTATUS RtlDeleteTimer(
        HANDLE TimerQueue,
        HANDLE Timer,
        HANDLE CompletionEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue", "Timer", "CompletionEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteTimerQueue(jitter):
    """
    NTSTATUS RtlDeleteTimerQueue(
        HANDLE TimerQueue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteTimerQueueEx(jitter):
    """
    NTSTATUS RtlDeleteTimerQueueEx(
        HANDLE TimerQueue,
        HANDLE CompletionEvent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TimerQueue", "CompletionEvent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFormatCurrentUserKeyPath(jitter):
    """
    NTSTATUS RtlFormatCurrentUserKeyPath(
        PUNICODE_STRING KeyPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlOpenCurrentUser(jitter):
    """
    NTSTATUS RtlOpenCurrentUser(
        ACCESS_MASK DesiredAccess,
        PHANDLE KeyHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DesiredAccess", "KeyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateRegistryKey(jitter):
    """
    NTSTATUS RtlCreateRegistryKey(
        [RTL_REGISTRY_RELATIVE_TO] RelativeTo,
        PWSTR Path
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RelativeTo", "Path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCheckRegistryKey(jitter):
    """
    NTSTATUS RtlCheckRegistryKey(
        [RTL_REGISTRY_RELATIVE_TO] RelativeTo,
        PWSTR Path
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RelativeTo", "Path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryRegistryValues(jitter):
    """
    NTSTATUS RtlQueryRegistryValues(
        [RTL_REGISTRY_RELATIVE_TO] RelativeTo,
        PCWSTR Path,
        PRTL_QUERY_REGISTRY_TABLE QueryTable,
        PVOID Context,
        PVOID Environment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RelativeTo", "Path", "QueryTable", "Context", "Environment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlWriteRegistryValue(jitter):
    """
    NTSTATUS RtlWriteRegistryValue(
        [RTL_REGISTRY_RELATIVE_TO] RelativeTo,
        PCWSTR Path,
        PCWSTR ValueName,
        ULONG ValueType,
        PVOID ValueData,
        ULONG ValueLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RelativeTo", "Path", "ValueName", "ValueType", "ValueData", "ValueLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeleteRegistryValue(jitter):
    """
    NTSTATUS RtlDeleteRegistryValue(
        [RTL_REGISTRY_RELATIVE_TO] RelativeTo,
        PCWSTR Path,
        PCWSTR ValueName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RelativeTo", "Path", "ValueName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnableThreadProfiling(jitter):
    """
    NTSTATUS RtlEnableThreadProfiling(
        HANDLE ThreadHandle,
        ULONG Flags,
        ULONG64 HardwareCounters,
        PVOID* PerformanceDataHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "Flags", "HardwareCounters", "PerformanceDataHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDisableThreadProfiling(jitter):
    """
    NTSTATUS RtlDisableThreadProfiling(
        PVOID PerformanceDataHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PerformanceDataHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryThreadProfiling(jitter):
    """
    NTSTATUS RtlQueryThreadProfiling(
        HANDLE ThreadHandle,
        PBOOLEAN Enabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "Enabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReadThreadProfilingData(jitter):
    """
    NTSTATUS RtlReadThreadProfilingData(
        HANDLE PerformanceDataHandle,
        ULONG Flags,
        PPERFORMANCE_DATA PerformanceData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PerformanceDataHandle", "Flags", "PerformanceData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlComputePrivatizedDllName_U(jitter):
    """
    NTSTATUS RtlComputePrivatizedDllName_U(
        PUNICODE_STRING DllName,
        PUNICODE_STRING RealName,
        PUNICODE_STRING LocalName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DllName", "RealName", "LocalName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFreeRangeList(jitter):
    """
    VOID RtlFreeRangeList(
        PRTL_RANGE_LIST RangeList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RangeList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlpNtOpenKey(jitter):
    """
    NTSTATUS RtlpNtOpenKey(
        HANDLE KeyHandle,
        ACCESS_MASK DesiredAccess,
        POBJECT_ATTRIBUTES ObjectAttributes,
        ULONG Unused
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["KeyHandle", "DesiredAccess", "ObjectAttributes", "Unused"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRegisterSecureMemoryCacheCallback(jitter):
    """
    NTSTATUS RtlRegisterSecureMemoryCacheCallback(
        PRTL_SECURE_MEMORY_CACHE_CALLBACK Callback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Callback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFlushSecureMemoryCache(jitter):
    """
    BOOLEAN RtlFlushSecureMemoryCache(
        PVOID MemoryCache,
        SIZE_T MemoryLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MemoryCache", "MemoryLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCaptureStackBackTrace(jitter):
    """
    USHORT RtlCaptureStackBackTrace(
        ULONG FramesToSkip,
        ULONG FramesToCapture,
        PVOID* BackTrace,
        PULONG BackTraceHash
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FramesToSkip", "FramesToCapture", "BackTrace", "BackTraceHash"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAssert(jitter):
    """
    VOID RtlAssert(
        PVOID FailedAssertion,
        PVOID FileName,
        ULONG LineNumber,
        PCHAR Message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FailedAssertion", "FileName", "LineNumber", "Message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCaptureContext(jitter):
    """
    VOID RtlCaptureContext(
        PCONTEXT ContextRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDebugCreateHeap(jitter):
    """
    PVOID RtlDebugCreateHeap(
        [HEAP_FLAGS_ULONG] Flags,
        PVOID BaseAddress,
        SIZE_T SizeToReserve,
        SIZE_T SizeToCommit,
        PVOID Lock,
        PRTL_HEAP_PARAMETERS Parameters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Flags", "BaseAddress", "SizeToReserve", "SizeToCommit", "Lock", "Parameters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetCallersAddress(jitter):
    """
    PVOID RtlGetCallersAddress(
        PVOID* CallersAddress,
        PVOID* CallersCaller
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CallersAddress", "CallersCaller"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCmDecodeMemIoResource(jitter):
    """
    ULONGLONG RtlCmDecodeMemIoResource(
        PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor,
        PULONGLONG Start
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Descriptor", "Start"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCmEncodeMemIoResource(jitter):
    """
    NTSTATUS RtlCmEncodeMemIoResource(
        PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor,
        UCHAR Type,
        ULONGLONG Length,
        ULONGLONG Start
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Descriptor", "Type", "Length", "Start"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnlargedIntegerMultiply(jitter):
    """
    LARGE_INTEGER RtlEnlargedIntegerMultiply(
        LONG Multiplicand,
        LONG Multiplier
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Multiplicand", "Multiplier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnlargedUnsignedDivide(jitter):
    """
    ULONG RtlEnlargedUnsignedDivide(
        ULARGE_INTEGER Dividend,
        ULONG Divisor,
        PULONG Remainder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Dividend", "Divisor", "Remainder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEnlargedUnsignedMultiply(jitter):
    """
    LARGE_INTEGER RtlEnlargedUnsignedMultiply(
        ULONG Multiplicand,
        ULONG Multiplier
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Multiplicand", "Multiplier"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlExtendedMagicDivide(jitter):
    """
    LARGE_INTEGER RtlExtendedMagicDivide(
        LARGE_INTEGER Dividend,
        LARGE_INTEGER MagicDivisor,
        CCHAR ShiftCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Dividend", "MagicDivisor", "ShiftCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFillMemory(jitter):
    """
    VOID RtlFillMemory(
        VOID* Destination,
        SIZE_T Length,
        UCHAR Fill
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Destination", "Length", "Fill"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetEnabledExtendedFeatures(jitter):
    """
    [XSTATE_MASK_ULONG64] RtlGetEnabledExtendedFeatures(
        [XSTATE_MASK_ULONG64] FeatureMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FeatureMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIoDecodeMemIoResource(jitter):
    """
    ULONGLONG RtlIoDecodeMemIoResource(
        PIO_RESOURCE_DESCRIPTOR Descriptor,
        PULONGLONG Alignment,
        PULONGLONG MinimumAddress,
        PULONGLONG MaximumAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Descriptor", "Alignment", "MinimumAddress", "MaximumAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIoEncodeMemIoResource(jitter):
    """
    NTSTATUS RtlIoEncodeMemIoResource(
        PIO_RESOURCE_DESCRIPTOR Descriptor,
        UCHAR Type,
        ULONGLONG Length,
        ULONGLONG Alignment,
        ULONGLONG MinimumAddress,
        ULONGLONG MaximumAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Descriptor", "Type", "Length", "Alignment", "MinimumAddress", "MaximumAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUlongByteSwap(jitter):
    """
    ULONG RtlUlongByteSwap(
        ULONG Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUlonglongByteSwap(jitter):
    """
    ULONGLONG RtlUlonglongByteSwap(
        ULONGLONG Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUshortByteSwap(jitter):
    """
    USHORT RtlUshortByteSwap(
        USHORT Source
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Source"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetCurrentProcessorNumber(jitter):
    """
    ULONG RtlGetCurrentProcessorNumber()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlComputeCrc32(jitter):
    """
    ULONG RtlComputeCrc32(
        USHORT PartialCrc,
        PUCHAR Buffer,
        ULONG Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PartialCrc", "Buffer", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEncodePointer(jitter):
    """
    PVOID RtlEncodePointer(
        PVOID Pointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Pointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDecodePointer(jitter):
    """
    PVOID RtlDecodePointer(
        PVOID Pointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Pointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEncodeSystemPointer(jitter):
    """
    PVOID RtlEncodeSystemPointer(
        PVOID Pointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Pointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDecodeSystemPointer(jitter):
    """
    PVOID RtlDecodeSystemPointer(
        PVOID Pointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Pointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlIsThreadWithinLoaderCallout(jitter):
    """
    BOOLEAN RtlIsThreadWithinLoaderCallout()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryElevationFlags(jitter):
    """
    NTSTATUS RtlQueryElevationFlags(
        [ElevationFlags*] pFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRegisterThreadWithCsrss(jitter):
    """
    NTSTATUS RtlRegisterThreadWithCsrss()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLockModuleSection(jitter):
    """
    NTSTATUS RtlLockModuleSection(
        PVOID Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlUnlockModuleSection(jitter):
    """
    NTSTATUS RtlUnlockModuleSection(
        PVOID Address
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetUnloadEventTrace(jitter):
    """
    RTL_UNLOAD_EVENT_TRACE [RTL_UNLOAD_EVENT_TRACE_NUMBER] RtlGetUnloadEventTrace()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetUnloadEventTraceEx(jitter):
    """
    VOID RtlGetUnloadEventTraceEx(
        PULONG* ElementSize,
        PULONG* ElementCount,
        PVOID* EventTrace
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ElementSize", "ElementCount", "EventTrace"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryPerformanceCounter(jitter):
    """
    LOGICAL RtlQueryPerformanceCounter(
        PLARGE_INTEGER PerformanceCounter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PerformanceCounter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryPerformanceFrequency(jitter):
    """
    LOGICAL RtlQueryPerformanceFrequency(
        PLARGE_INTEGER PerformanceFrequency
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PerformanceFrequency"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlEqualPrefixSid(jitter):
    """
    BOOLEAN RtlEqualPrefixSid(
        PSID Sid1,
        PSID Sid2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Sid1", "Sid2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlConvertLongToLargeInteger(jitter):
    """
    LARGE_INTEGER RtlConvertLongToLargeInteger(
        LONG SignedInteger
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SignedInteger"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlConvertUlongToLargeInteger(jitter):
    """
    LARGE_INTEGER RtlConvertUlongToLargeInteger(
        ULONG UnsignedInteger
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UnsignedInteger"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLargeIntegerAdd(jitter):
    """
    LARGE_INTEGER RtlLargeIntegerAdd(
        LARGE_INTEGER Addend1,
        LARGE_INTEGER Addend2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Addend1", "Addend2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLargeIntegerArithmeticShift(jitter):
    """
    LARGE_INTEGER RtlLargeIntegerArithmeticShift(
        LARGE_INTEGER LargeInteger,
        CCHAR ShiftCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LargeInteger", "ShiftCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLargeIntegerDivide(jitter):
    """
    LARGE_INTEGER RtlLargeIntegerDivide(
        LARGE_INTEGER Dividend,
        LARGE_INTEGER Divisor,
        PLARGE_INTEGER Remainder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Dividend", "Divisor", "Remainder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLargeIntegerNegate(jitter):
    """
    LARGE_INTEGER RtlLargeIntegerNegate(
        LARGE_INTEGER Subtrahend
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Subtrahend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLargeIntegerShiftLeft(jitter):
    """
    LARGE_INTEGER RtlLargeIntegerShiftLeft(
        LARGE_INTEGER LargeInteger,
        CCHAR ShiftCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LargeInteger", "ShiftCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLargeIntegerShiftRight(jitter):
    """
    LARGE_INTEGER RtlLargeIntegerShiftRight(
        LARGE_INTEGER LargeInteger,
        CCHAR ShiftCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LargeInteger", "ShiftCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLargeIntegerSubtract(jitter):
    """
    LARGE_INTEGER RtlLargeIntegerSubtract(
        LARGE_INTEGER Minuend,
        LARGE_INTEGER Subtrahend
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Minuend", "Subtrahend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlLargeIntegerToChar(jitter):
    """
    NTSTATUS RtlLargeIntegerToChar(
        PLARGE_INTEGER Value,
        ULONG Base,
        ULONG Length,
        PCHAR String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Value", "Base", "Length", "String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlActivateActivationContext(jitter):
    """
    NTSTATUS RtlActivateActivationContext(
        ULONG Unknown,
        HANDLE Handle,
        PULONG_PTR Cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Unknown", "Handle", "Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAddRefActivationContext(jitter):
    """
    VOID RtlAddRefActivationContext(
        PVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlAllocateActivationContextStack(jitter):
    """
    NTSTATUS RtlAllocateActivationContextStack(
        PVOID* Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlCreateActivationContext(jitter):
    """
    NTSTATUS RtlCreateActivationContext(
        DWORD dwFlags,
        PVOID ActivationContextData,
        ULONG ExtraBytes,
        PVOID NotificationRoutine,
        PVOID NotificationContext,
        PHANDLE ActCtx
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "ActivationContextData", "ExtraBytes", "NotificationRoutine", "NotificationContext", "ActCtx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlDeactivateActivationContext(jitter):
    """
    LONG RtlDeactivateActivationContext(
        DWORD dwFlags,
        ULONG_PTR ulCookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "ulCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlFindActivationContextSectionString(jitter):
    """
    NTSTATUS RtlFindActivationContextSectionString(
        [FIND_ACTCTX_SECTION_FLAGS] dwFlags,
        const GUID* ExtensionGuid,
        [ACTIVATION_CONTEXT_SECTION] SectionType,
        PUNICODE_STRING SectionName,
        PVOID ReturnedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "ExtensionGuid", "SectionType", "SectionName", "ReturnedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlGetActiveActivationContext(jitter):
    """
    NTSTATUS RtlGetActiveActivationContext(
        PVOID* Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlQueryInformationActivationContext(jitter):
    """
    NTSTATUS RtlQueryInformationActivationContext(
        DWORD dwFlags,
        PVOID Context,
        PVOID pvSubInstance,
        ULONG ulInfoClass,
        PVOID pvBuffer,
        SIZE_T cbBuffer,
        SIZE_T* pcbWrittenOrRequired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "Context", "pvSubInstance", "ulInfoClass", "pvBuffer", "cbBuffer", "pcbWrittenOrRequired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlReleaseActivationContext(jitter):
    """
    VOID RtlReleaseActivationContext(
        PVOID* Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlZombifyActivationContext(jitter):
    """
    NTSTATUS RtlZombifyActivationContext(
        PVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRunOnceBeginInitialize(jitter):
    """
    NTSTATUS RtlRunOnceBeginInitialize(
        PRTL_RUN_ONCE RunOnce,
        [RTL_RUN_ONCE_FLAGS] Flags,
        PVOID* Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RunOnce", "Flags", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRunOnceComplete(jitter):
    """
    NTSTATUS RtlRunOnceComplete(
        PRTL_RUN_ONCE RunOnce,
        [RTL_RUN_ONCE_FLAGS] Flags,
        PVOID Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RunOnce", "Flags", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRunOnceExecuteOnce(jitter):
    """
    NTSTATUS RtlRunOnceExecuteOnce(
        PRTL_RUN_ONCE RunOnce,
        PRTL_RUN_ONCE_INIT_FN InitFn,
        PVOID Parameter,
        PVOID* Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RunOnce", "InitFn", "Parameter", "Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def ntdll_RtlRunOnceInitialize(jitter):
    """
    VOID RtlRunOnceInitialize(
        PRTL_RUN_ONCE RunOnce
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RunOnce"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
