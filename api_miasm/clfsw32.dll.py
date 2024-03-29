###### Enums ######
CLFS_RECORD_TYPE = {
    "ClfsNullRecord": 0x00,
    "ClfsDataRecord": 0x01,
    "ClfsRestartRecord": 0x02,
}
CLFS_RECORD_TYPE_INV = {
    0x00: "ClfsNullRecord",
    0x01: "ClfsDataRecord",
    0x02: "ClfsRestartRecord",
}
CLFS_IOSTATS_CLASS = {
    "ClfsIoStatsDefault": 0x0000,
}
CLFS_IOSTATS_CLASS_INV = {
    0x0000: "ClfsIoStatsDefault",
}
CLFS_CONTEXT_MODE = {
    "ClfsContextNone": 0x00,
    "ClfsContextUndoNext": 0x01,
    "ClfsContextPrevious": 0x02,
    "ClfsContextForward": 0x03,
}
CLFS_CONTEXT_MODE_INV = {
    0x00: "ClfsContextNone",
    0x01: "ClfsContextUndoNext",
    0x02: "ClfsContextPrevious",
    0x03: "ClfsContextForward",
}
CLFS_LOG_ARCHIVE_MODE = {
    "ClfsLogArchiveEnabled": 0x01,
    "ClfsLogArchiveDisabled": 0x02,
}
CLFS_LOG_ARCHIVE_MODE_INV = {
    0x01: "ClfsLogArchiveEnabled",
    0x02: "ClfsLogArchiveDisabled",
}
CLFS_MGMT_POLICY_TYPE = {
    "ClfsMgmtPolicyMaximumSize": 0,
    "ClfsMgmtPolicyMinimumSize": 1,
    "ClfsMgmtPolicyNewContainerSize": 2,
    "ClfsMgmtPolicyGrowthRate": 3,
    "ClfsMgmtPolicyLogTail": 4,
    "ClfsMgmtPolicyAutoShrink": 5,
    "ClfsMgmtPolicyAutoGrow": 6,
    "ClfsMgmtPolicyNewContainerPrefix": 7,
    "ClfsMgmtPolicyNewContainerSuffix": 8,
    "ClfsMgmtPolicyNewContainerExtension": 9,
}
CLFS_MGMT_POLICY_TYPE_INV = {
    0: "ClfsMgmtPolicyMaximumSize",
    1: "ClfsMgmtPolicyMinimumSize",
    2: "ClfsMgmtPolicyNewContainerSize",
    3: "ClfsMgmtPolicyGrowthRate",
    4: "ClfsMgmtPolicyLogTail",
    5: "ClfsMgmtPolicyAutoShrink",
    6: "ClfsMgmtPolicyAutoGrow",
    7: "ClfsMgmtPolicyNewContainerPrefix",
    8: "ClfsMgmtPolicyNewContainerSuffix",
    9: "ClfsMgmtPolicyNewContainerExtension",
}
CLFS_MGMT_NOTIFICATION_TYPE = {
    "ClfsMgmtAdvanceTailNotification": 0,
    "ClfsMgmtLogFullHandlerNotification": 1,
    "ClfsMgmtLogUnpinnedNotification": 2,
    "ClfsMgmtLogWriteNotification": 3,
}
CLFS_MGMT_NOTIFICATION_TYPE_INV = {
    0: "ClfsMgmtAdvanceTailNotification",
    1: "ClfsMgmtLogFullHandlerNotification",
    2: "ClfsMgmtLogUnpinnedNotification",
    3: "ClfsMgmtLogWriteNotification",
}
_CREATE_LOG_DISPOSITION_ = {
    "CREATE_NEW": 1,
    "OPEN_EXISTING": 3,
    "OPEN_ALWAYS": 4,
}
_CREATE_LOG_DISPOSITION__INV = {
    1: "CREATE_NEW",
    3: "OPEN_EXISTING",
    4: "OPEN_ALWAYS",
}
_CREATE_LOG_FLAGS_ATTRIBUTES_ = {
    "FILE_ATTRIBUTE_ARCHIVE": 0x00000020,
    "FILE_FLAG_OVERLAPPED": 0x40000000,
}
_CREATE_LOG_FLAGS_ATTRIBUTES__INV = {
    0x00000020: "FILE_ATTRIBUTE_ARCHIVE",
    0x40000000: "FILE_FLAG_OVERLAPPED",
}

###################

###### Types ######
PCLFS_SCAN_CONTEXT = LPVOID
PFILE = LPVOID
CLFS_PRINT_RECORD_ROUTINE = LPVOID
CLFS_BLOCK_ALLOCATION = LPVOID
CLFS_BLOCK_DEALLOCATION = LPVOID
CLFS_CONTAINER_ID = ULONG
CLFS_LOG_ARCHIVE_CONTEXT = LPVOID
PCLFS_LOG_ARCHIVE_CONTEXT = Ptr("<I", CLFS_LOG_ARCHIVE_CONTEXT())
LONGLONG___ = Ptr("<I", LONGLONG())
PLOG_TAIL_ADVANCE_CALLBACK = LPVOID
PLOG_FULL_HANDLER_CALLBACK = LPVOID
PLOG_UNPINNED_CALLBACK = LPVOID
WCHAR__CLFS_MAX_CONTAINER_INFO_ = Array(WCHAR, 256)
CLFS_CONTAINER_STATE = UINT32

class CLS_CONTAINER_INFORMATION(MemStruct):
    fields = [
        ("FileAttributes", ULONG()),
        ("CreationTime", ULONGLONG()),
        ("LastAccessTime", ULONGLONG()),
        ("LastWriteTime", ULONGLONG()),
        ("ContainerSize", LONGLONG()),
        ("FileNameActualLength", ULONG()),
        ("FileNameLength", ULONG()),
        ("FileName", WCHAR__CLFS_MAX_CONTAINER_INFO_()),
        ("State", CLFS_CONTAINER_STATE()),
        ("PhysicalContainerId", CLFS_CONTAINER_ID()),
        ("LogicalContainerId", CLFS_CONTAINER_ID()),
    ]


class CLFS_ARCHIVE_DESCRIPTOR(MemStruct):
    fields = [
        ("coffLow", ULONGLONG()),
        ("coffHigh", ULONGLONG()),
        ("infoContainer", CLS_CONTAINER_INFORMATION()),
    ]

CLFS_ARCHIVE_DESCRIPTOR___ = Ptr("<I", CLFS_ARCHIVE_DESCRIPTOR())
CLFS_RECORD_TYPE = UINT8
PCLFS_RECORD_TYPE = Ptr("<I", CLFS_RECORD_TYPE())
CLFS_IOSTATS_CLASS = UINT
CLFS_CONTEXT_MODE = UINT
CLFS_SCAN_MODE = UINT8
CLFS_LOG_ARCHIVE_MODE = UINT

class CLS_LSN(MemStruct):
    fields = [
        ("Internal", ULONGLONG()),
    ]

CLFS_LSN = CLS_LSN
PCLFS_LSN = Ptr("<I", CLFS_LSN())
const_PCLFS_LSN = PCLFS_LSN
const_CLFS_LSN_PTR = PCLFS_LSN

class CLFS_WRITE_ENTRY(MemStruct):
    fields = [
        ("Buffer", PVOID()),
        ("ByteLength", ULONG()),
    ]

PCLFS_WRITE_ENTRY = Ptr("<I", CLFS_WRITE_ENTRY())

class CLFS_INFORMATION(MemStruct):
    fields = [
        ("TotalAvailable", LONGLONG()),
        ("CurrentAvailable", LONGLONG()),
        ("TotalReservation", LONGLONG()),
        ("BaseFileSize", ULONGLONG()),
        ("ContainerSize", ULONGLONG()),
        ("TotalContainers", ULONG()),
        ("FreeContainers", ULONG()),
        ("TotalClients", ULONG()),
        ("Attributes", ULONG()),
        ("FlushThreshold", ULONG()),
        ("SectorSize", ULONG()),
        ("MinArchiveTailLsn", CLS_LSN()),
        ("BaseLsn", CLS_LSN()),
        ("LastFlushedLsn", CLS_LSN()),
        ("LastLsn", CLS_LSN()),
        ("RestartLsn", CLS_LSN()),
        ("Identity", GUID()),
    ]

PCLFS_INFORMATION = Ptr("<I", CLFS_INFORMATION())
CLFS_MGMT_POLICY_TYPE = UINT

class _CLFS_MGMT_POLICY_u_s1_(MemStruct):
    fields = [
        ("Containers", ULONG()),
    ]


class _CLFS_MGMT_POLICY_u_s2_(MemStruct):
    fields = [
        ("Containers", ULONG()),
    ]


class _CLFS_MGMT_POLICY_u_s3_(MemStruct):
    fields = [
        ("SizeInBytes", ULONG()),
    ]


class _CLFS_MGMT_POLICY_u_s4_(MemStruct):
    fields = [
        ("AbsoluteGrowthInContainers", ULONG()),
        ("RelativeGrowthPercentage", ULONG()),
    ]


class _CLFS_MGMT_POLICY_u_s5_(MemStruct):
    fields = [
        ("MinimumAvailablePercentage", ULONG()),
        ("MinimumAvailableContainers", ULONG()),
    ]


class _CLFS_MGMT_POLICY_u_s6_(MemStruct):
    fields = [
        ("Percentage", ULONG()),
    ]


class _CLFS_MGMT_POLICY_u_s7_(MemStruct):
    fields = [
        ("Enabled", ULONG()),
    ]


class _CLFS_MGMT_POLICY_u_s8_(MemStruct):
    fields = [
        ("PrefixLengthInBytes", USHORT()),
        ("PrefixString", WCHAR__1_()),
    ]


class _CLFS_MGMT_POLICY_u_s9_(MemStruct):
    fields = [
        ("NextContainerSuffix", ULONGLONG()),
    ]


class _CLFS_MGMT_POLICY_u_s10_(MemStruct):
    fields = [
        ("ExtensionLengthInBytes", USHORT()),
        ("ExtensionString", WCHAR__1_()),
    ]

_CLFS_MGMT_POLICY_u_ = Union([
    ("MaximumSize", _CLFS_MGMT_POLICY_u_s1_),
    ("MinimumSize", _CLFS_MGMT_POLICY_u_s2_),
    ("NewContainerSize", _CLFS_MGMT_POLICY_u_s3_),
    ("GrowthRate", _CLFS_MGMT_POLICY_u_s4_),
    ("LogTail", _CLFS_MGMT_POLICY_u_s5_),
    ("AutoShrink", _CLFS_MGMT_POLICY_u_s6_),
    ("AutoGrow", _CLFS_MGMT_POLICY_u_s7_),
    ("NewContainerPrefix", _CLFS_MGMT_POLICY_u_s8_),
    ("NewContainerSuffix", _CLFS_MGMT_POLICY_u_s9_),
    ("NewContainerExtension", _CLFS_MGMT_POLICY_u_s10_),
])

class CLFS_MGMT_POLICY(MemStruct):
    fields = [
        ("Version", ULONG()),
        ("LengthInBytes", ULONG()),
        ("PolicyFlags", ULONG()),
        ("PolicyType", CLFS_MGMT_POLICY_TYPE()),
        ("PolicyParameters", _CLFS_MGMT_POLICY_u_()),
    ]

PCLFS_MGMT_POLICY = Ptr("<I", CLFS_MGMT_POLICY())
CLFS_MGMT_NOTIFICATION_TYPE = UINT

class CLFS_MGMT_NOTIFICATION(MemStruct):
    fields = [
        ("Notification", CLFS_MGMT_NOTIFICATION_TYPE()),
        ("Lsn", CLFS_LSN()),
        ("LogIsPinned", USHORT()),
    ]

PCLFS_MGMT_NOTIFICATION = Ptr("<I", CLFS_MGMT_NOTIFICATION())

class LOG_MANAGEMENT_CALLBACKS(MemStruct):
    fields = [
        ("CallbackContext", PVOID()),
        ("AdvanceTailCallback", PLOG_TAIL_ADVANCE_CALLBACK()),
        ("LogFullHandlerCallback", PLOG_FULL_HANDLER_CALLBACK()),
        ("LogUnpinnedCallback", PLOG_UNPINNED_CALLBACK()),
    ]

PLOG_MANAGEMENT_CALLBACKS = Ptr("<I", LOG_MANAGEMENT_CALLBACKS())
_CREATE_LOG_DISPOSITION_ = ULONG
_CREATE_LOG_FLAGS_ATTRIBUTES_ = ULONG

###################

###### Functions ######

def clfsw32_AlignReservedLog(jitter):
    """
    BOOL AlignReservedLog(
        PVOID pvMarshal,
        ULONG cReservedRecords,
        LONGLONG [] rgcbReservation,
        PLONGLONG pcbAlignReservation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "cReservedRecords", "rgcbReservation", "pcbAlignReservation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_AllocReservedLog(jitter):
    """
    BOOL AllocReservedLog(
        PVOID pvMarshal,
        ULONG cReservedRecords,
        PLONGLONG pcbAdjustment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "cReservedRecords", "pcbAdjustment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_CloseAndResetLogFile(jitter):
    """
    BOOL CloseAndResetLogFile(
        HANDLE hLog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_CreateLogFile(jitter):
    """
    HANDLE CreateLogFile(
        LPCWSTR pszLogFileName,
        ACCESS_MASK fDesiredAccess,
        [FILE_SHARE_MODE] dwShareMode,
        LPSECURITY_ATTRIBUTES psaLogFile,
        [CREATE_LOG_DISPOSITION] fCreateDisposition,
        [CREATE_LOG_FLAGS_ATTRIBUTES] fFlagsAndAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLogFileName", "fDesiredAccess", "dwShareMode", "psaLogFile", "fCreateDisposition", "fFlagsAndAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DeleteLogByHandle(jitter):
    """
    BOOL DeleteLogByHandle(
        HANDLE hLog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DeleteLogFile(jitter):
    """
    BOOL DeleteLogFile(
        LPCWSTR pszLogFileName,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLogFileName", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DumpLogRecords(jitter):
    """
    BOOL DumpLogRecords(
        PWSTR pwszLogFileName,
        CLFS_RECORD_TYPE fRecordType,
        PCLFS_LSN plsnStart,
        PCLFS_LSN plsnEnd,
        PFILE pstrmOut,
        CLFS_PRINT_RECORD_ROUTINE pfnPrintRecord,
        CLFS_BLOCK_ALLOCATION pfnAllocBlock,
        CLFS_BLOCK_DEALLOCATION pfnFreeBlock,
        PVOID pvBlockAllocContext,
        ULONG cbBlock,
        ULONG cMaxBlocks
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszLogFileName", "fRecordType", "plsnStart", "plsnEnd", "pstrmOut", "pfnPrintRecord", "pfnAllocBlock", "pfnFreeBlock", "pvBlockAllocContext", "cbBlock", "cMaxBlocks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_FlushLogBuffers(jitter):
    """
    BOOL FlushLogBuffers(
        PVOID pvMarshal,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_FlushLogToLsn(jitter):
    """
    BOOL FlushLogToLsn(
        PVOID pvMarshalContext,
        PCLFS_LSN plsnFlush,
        PCLFS_LSN plsnLastFlushed,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshalContext", "plsnFlush", "plsnLastFlushed", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_FreeReservedLog(jitter):
    """
    BOOL FreeReservedLog(
        PVOID pvMarshal,
        ULONG cReservedRecords,
        PLONGLONG pcbAdjustment
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "cReservedRecords", "pcbAdjustment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReserveAndAppendLog(jitter):
    """
    BOOL ReserveAndAppendLog(
        PVOID pvMarshal,
        PCLFS_WRITE_ENTRY rgWriteEntries,
        ULONG cWriteEntries,
        PCLFS_LSN plsnUndoNext,
        PCLFS_LSN plsnPrevious,
        ULONG cReserveRecords,
        LONGLONG [] rgcbReservation,
        ULONG fFlags,
        PCLFS_LSN plsn,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "rgWriteEntries", "cWriteEntries", "plsnUndoNext", "plsnPrevious", "cReserveRecords", "rgcbReservation", "fFlags", "plsn", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReserveAndAppendLogAligned(jitter):
    """
    BOOL ReserveAndAppendLogAligned(
        PVOID pvMarshal,
        PCLFS_WRITE_ENTRY rgWriteEntries,
        ULONG cWriteEntries,
        ULONG cbEntryAlignment,
        PCLFS_LSN plsnUndoNext,
        PCLFS_LSN plsnPrevious,
        ULONG cReserveRecords,
        LONGLONG [] rgcbReservation,
        ULONG fFlags,
        PCLFS_LSN plsn,
        LPOVERLAPPED overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "rgWriteEntries", "cWriteEntries", "cbEntryAlignment", "plsnUndoNext", "plsnPrevious", "cReserveRecords", "rgcbReservation", "fFlags", "plsn", "overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetLogFileInformation(jitter):
    """
    BOOL GetLogFileInformation(
        HANDLE hLog,
        PCLFS_INFORMATION pinfoBuffer,
        PULONG cbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pinfoBuffer", "cbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetLogIoStatistics(jitter):
    """
    BOOL GetLogIoStatistics(
        HANDLE hLog,
        PVOID pvStatsBuffer,
        ULONG cbStatsBuffer,
        CLFS_IOSTATS_CLASS eStatsClass,
        PULONG pcbStatsWritten
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pvStatsBuffer", "cbStatsBuffer", "eStatsClass", "pcbStatsWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadLogRecord(jitter):
    """
    BOOL ReadLogRecord(
        PVOID pvMarshal,
        PCLFS_LSN plsnFirst,
        CLFS_CONTEXT_MODE eContextMode,
        PVOID* ppvReadBuffer,
        PULONG pcbReadBuffer,
        PCLFS_RECORD_TYPE peRecordType,
        PCLFS_LSN plsnUndoNext,
        PCLFS_LSN plsnPrevious,
        PVOID* ppvReadContext,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "plsnFirst", "eContextMode", "ppvReadBuffer", "pcbReadBuffer", "peRecordType", "plsnUndoNext", "plsnPrevious", "ppvReadContext", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadNextLogRecord(jitter):
    """
    BOOL ReadNextLogRecord(
        PVOID pvReadContext,
        PVOID* ppvBuffer,
        PULONG pcbBuffer,
        PCLFS_RECORD_TYPE peRecordType,
        PCLFS_LSN plsnUser,
        PCLFS_LSN plsnUndoNext,
        PCLFS_LSN plsnPrevious,
        PCLFS_LSN plsnRecord,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvReadContext", "ppvBuffer", "pcbBuffer", "peRecordType", "plsnUser", "plsnUndoNext", "plsnPrevious", "plsnRecord", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_SetEndOfLog(jitter):
    """
    BOOL SetEndOfLog(
        HANDLE hLog,
        PCLFS_LSN plsnEnd,
        LPOVERLAPPED lpOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "plsnEnd", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_TruncateLog(jitter):
    """
    BOOL TruncateLog(
        PVOID pvMarshal,
        PCLFS_LSN plsnEnd,
        LPOVERLAPPED lpOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "plsnEnd", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_TerminateReadLog(jitter):
    """
    BOOL TerminateReadLog(
        PVOID pvCursorContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvCursorContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetLogReservationInfo(jitter):
    """
    BOOL GetLogReservationInfo(
        PVOID pvMarshal,
        PULONG pcbRecordNumber,
        PLONGLONG pcbUserReservation,
        PLONGLONG pcbCommitReservation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "pcbRecordNumber", "pcbUserReservation", "pcbCommitReservation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_AddLogContainer(jitter):
    """
    BOOL AddLogContainer(
        HANDLE hLog,
        PULONGLONG pcbContainer,
        LPWSTR pwszContainerPath,
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pcbContainer", "pwszContainerPath", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_AddLogContainerSet(jitter):
    """
    BOOL AddLogContainerSet(
        HANDLE hLog,
        USHORT cContainers,
        PULONGLONG pcbContainer,
        LPWSTR* rgwszContainerPath,
        PVOID Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cContainers", "pcbContainer", "rgwszContainerPath", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_CreateLogContainerScanContext(jitter):
    """
    BOOL CreateLogContainerScanContext(
        HANDLE hLog,
        ULONG cFromContainer,
        ULONG cContainers,
        CLFS_SCAN_MODE eScanMode,
        PCLFS_SCAN_CONTEXT pcxScan,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cFromContainer", "cContainers", "eScanMode", "pcxScan", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ScanLogContainers(jitter):
    """
    BOOL ScanLogContainers(
        PCLFS_SCAN_CONTEXT pcxScan,
        CLFS_SCAN_MODE eScanMode,
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcxScan", "eScanMode", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetLogContainerName(jitter):
    """
    BOOL GetLogContainerName(
        HANDLE hLog,
        CLFS_CONTAINER_ID cidLogicalContainer,
        LPCWSTR pwstrContainerName,
        ULONG cLenContainerName,
        PULONG pcActualLenContainerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cidLogicalContainer", "pwstrContainerName", "cLenContainerName", "pcActualLenContainerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RemoveLogContainer(jitter):
    """
    BOOL RemoveLogContainer(
        HANDLE hLog,
        LPWSTR pwszContainerPath,
        BOOL fForce,
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pwszContainerPath", "fForce", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RemoveLogContainerSet(jitter):
    """
    BOOL RemoveLogContainerSet(
        HANDLE hLog,
        USHORT cContainers,
        LPWSTR* rgwszContainerPath,
        BOOL fForce,
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cContainers", "rgwszContainerPath", "fForce", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_AdvanceLogBase(jitter):
    """
    BOOL AdvanceLogBase(
        PVOID pvMarshal,
        PCLFS_LSN plsnBase,
        ULONG fFlags,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "plsnBase", "fFlags", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadLogRestartArea(jitter):
    """
    BOOL ReadLogRestartArea(
        PVOID pvMarshal,
        PVOID* ppvRestartBuffer,
        PULONG pcbRestartBuffer,
        PCLFS_LSN plsn,
        PVOID* ppvContext,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "ppvRestartBuffer", "pcbRestartBuffer", "plsn", "ppvContext", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadPreviousLogRestartArea(jitter):
    """
    BOOL ReadPreviousLogRestartArea(
        PVOID pvReadContext,
        PVOID* ppvRestartBuffer,
        PULONG pcbRestartBuffer,
        PCLFS_LSN plsnRestart,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvReadContext", "ppvRestartBuffer", "pcbRestartBuffer", "plsnRestart", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_WriteLogRestartArea(jitter):
    """
    BOOL WriteLogRestartArea(
        PVOID pvMarshal,
        PVOID pvRestartBuffer,
        ULONG cbRestartBuffer,
        PCLFS_LSN plsnBase,
        ULONG fFlags,
        PULONG pcbWritten,
        PCLFS_LSN plsnNext,
        LPOVERLAPPED pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "pvRestartBuffer", "cbRestartBuffer", "plsnBase", "fFlags", "pcbWritten", "plsnNext", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetNextLogArchiveExtent(jitter):
    """
    BOOL GetNextLogArchiveExtent(
        CLFS_LOG_ARCHIVE_CONTEXT pvArchiveContext,
        CLFS_ARCHIVE_DESCRIPTOR [] rgadExtent,
        ULONG cDescriptors,
        PULONG pcDescriptorsReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvArchiveContext", "rgadExtent", "cDescriptors", "pcDescriptorsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_PrepareLogArchive(jitter):
    """
    BOOL PrepareLogArchive(
        HANDLE hLog,
        PWSTR pszBaseLogFileName,
        ULONG cLen,
        const PCLFS_LSN plsnLow,
        const PCLFS_LSN plsnHigh,
        PULONG pcActualLength,
        PULONGLONG poffBaseLogFileData,
        PULONGLONG pcbBaseLogFileLength,
        PCLFS_LSN plsnBase,
        PCLFS_LSN plsnLast,
        PCLFS_LSN plsnCurrentArchiveTail,
        PCLFS_LOG_ARCHIVE_CONTEXT ppvArchiveContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pszBaseLogFileName", "cLen", "plsnLow", "plsnHigh", "pcActualLength", "poffBaseLogFileData", "pcbBaseLogFileLength", "plsnBase", "plsnLast", "plsnCurrentArchiveTail", "ppvArchiveContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadLogArchiveMetadata(jitter):
    """
    BOOL ReadLogArchiveMetadata(
        CLFS_LOG_ARCHIVE_CONTEXT pvArchiveContext,
        ULONG cbOffset,
        ULONG cbBytesToRead,
        PBYTE pbReadBuffer,
        PULONG pcbBytesRead
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvArchiveContext", "cbOffset", "cbBytesToRead", "pbReadBuffer", "pcbBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_SetLogArchiveMode(jitter):
    """
    BOOL SetLogArchiveMode(
        HANDLE hLog,
        CLFS_LOG_ARCHIVE_MODE eMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "eMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_SetLogArchiveTail(jitter):
    """
    BOOL SetLogArchiveTail(
        HANDLE hLog,
        PCLFS_LSN plsnArchiveTail,
        LPVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "plsnArchiveTail", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_TerminateLogArchive(jitter):
    """
    BOOL TerminateLogArchive(
        CLFS_LOG_ARCHIVE_CONTEXT pvArchiveContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvArchiveContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ValidateLog(jitter):
    """
    BOOL ValidateLog(
        LPCWSTR pszLogFileName,
        LPSECURITY_ATTRIBUTES psaLogFile,
        PCLFS_INFORMATION pinfoBuffer,
        PULONG pcbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszLogFileName", "psaLogFile", "pinfoBuffer", "pcbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_CreateLogMarshallingArea(jitter):
    """
    BOOL CreateLogMarshallingArea(
        HANDLE hLog,
        CLFS_BLOCK_ALLOCATION pfnAllocBuffer,
        CLFS_BLOCK_DEALLOCATION pfnFreeBuffer,
        PVOID pvBlockAllocContext,
        ULONG cbMarshallingBuffer,
        ULONG cMaxWriteBuffers,
        ULONG cMaxReadBuffers,
        PVOID* ppvMarshal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pfnAllocBuffer", "pfnFreeBuffer", "pvBlockAllocContext", "cbMarshallingBuffer", "cMaxWriteBuffers", "cMaxReadBuffers", "ppvMarshal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DeleteLogMarshallingArea(jitter):
    """
    BOOL DeleteLogMarshallingArea(
        PVOID pvMarshal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnBlockOffset(jitter):
    """
    ULONG LsnBlockOffset(
        const CLFS_LSN* plsn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnContainer(jitter):
    """
    CLFS_CONTAINER_ID LsnContainer(
        const CLFS_LSN* plsn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnCreate(jitter):
    """
    CLFS_LSN LsnCreate(
        CLFS_CONTAINER_ID cidContainer,
        ULONG offBlock,
        ULONG cRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cidContainer", "offBlock", "cRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnEqual(jitter):
    """
    BOOL LsnEqual(
        const CLFS_LSN* plsn1,
        const CLFS_LSN* plsn2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn1", "plsn2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnGreater(jitter):
    """
    BOOL LsnGreater(
        const CLFS_LSN* plsn1,
        const CLFS_LSN* plsn2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn1", "plsn2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnLess(jitter):
    """
    BOOL LsnLess(
        const CLFS_LSN* plsn1,
        const CLFS_LSN* plsn2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn1", "plsn2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnNull(jitter):
    """
    BOOL LsnNull(
        const CLFS_LSN* plsn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnRecordSequence(jitter):
    """
    ULONG LsnRecordSequence(
        const CLFS_LSN* plsn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnDecrement(jitter):
    """
    CLFS_LSN LsnDecrement(
        PCLFS_LSN plsn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnIncrement(jitter):
    """
    CLFS_LSN LsnIncrement(
        PCLFS_LSN plsn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnInvalid(jitter):
    """
    BOOL LsnInvalid(
        const CLFS_LSN* plsn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DeregisterManageableLogClient(jitter):
    """
    BOOL DeregisterManageableLogClient(
        HANDLE hLog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_HandleLogFull(jitter):
    """
    BOOL HandleLogFull(
        HANDLE hLog
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_InstallLogPolicy(jitter):
    """
    BOOL InstallLogPolicy(
        HANDLE hLog,
        PCLFS_MGMT_POLICY pPolicy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LogTailAdvanceFailure(jitter):
    """
    BOOL LogTailAdvanceFailure(
        HANDLE hLog,
        [ERROR_CODE] dwReason
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "dwReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_QueryLogPolicy(jitter):
    """
    BOOL QueryLogPolicy(
        HANDLE hLog,
        CLFS_MGMT_POLICY_TYPE ePolicyType,
        PCLFS_MGMT_POLICY pPolicyBuffer,
        PULONG pcbPolicyBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "ePolicyType", "pPolicyBuffer", "pcbPolicyBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadLogNotification(jitter):
    """
    BOOL ReadLogNotification(
        HANDLE hLog,
        PCLFS_MGMT_NOTIFICATION pNotification,
        LPOVERLAPPED lpOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pNotification", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RegisterForLogWriteNotification(jitter):
    """
    BOOL RegisterForLogWriteNotification(
        HANDLE hLog,
        ULONG cbThreshold,
        BOOL fEnable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cbThreshold", "fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RemoveLogPolicy(jitter):
    """
    BOOL RemoveLogPolicy(
        HANDLE hLog,
        CLFS_MGMT_POLICY_TYPE ePolicyType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "ePolicyType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RegisterManageableLogClient(jitter):
    """
    BOOL RegisterManageableLogClient(
        HANDLE hLog,
        PLOG_MANAGEMENT_CALLBACKS pCallbacks
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pCallbacks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_SetLogFileSizeWithPolicy(jitter):
    """
    BOOL SetLogFileSizeWithPolicy(
        HANDLE hLog,
        PULONGLONG pDesiredSize,
        PULONGLONG pResultingSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pDesiredSize", "pResultingSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
