
def clfsw32_AlignReservedLog(jitter):
    """"
    [Clfsw32.dll] BOOL AlignReservedLog(PVOID pvMarshal, ULONG cReservedRecords, LONGLONG [] rgcbReservation, PLONGLONG pcbAlignReservation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "cReservedRecords", "rgcbReservation", "pcbAlignReservation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_AllocReservedLog(jitter):
    """"
    [Clfsw32.dll] BOOL AllocReservedLog(PVOID pvMarshal, ULONG cReservedRecords, PLONGLONG pcbAdjustment)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "cReservedRecords", "pcbAdjustment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_CloseAndResetLogFile(jitter):
    """"
    [Clfsw32.dll] BOOL CloseAndResetLogFile(HANDLE hLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_CreateLogFile(jitter):
    """"
    [Clfsw32.dll] HANDLE CreateLogFile(LPCWSTR pszLogFileName, ACCESS_MASK fDesiredAccess, [FILE_SHARE_MODE] dwShareMode, LPSECURITY_ATTRIBUTES psaLogFile, [CREATE_LOG_DISPOSITION] fCreateDisposition, [CREATE_LOG_FLAGS_ATTRIBUTES] fFlagsAndAttributes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszLogFileName", "fDesiredAccess", "dwShareMode", "psaLogFile", "fCreateDisposition", "fFlagsAndAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DeleteLogByHandle(jitter):
    """"
    [Clfsw32.dll] BOOL DeleteLogByHandle(HANDLE hLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DeleteLogFile(jitter):
    """"
    [Clfsw32.dll] BOOL DeleteLogFile(LPCWSTR pszLogFileName, PVOID pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszLogFileName", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DumpLogRecords(jitter):
    """"
    [Clfsw32.dll] BOOL DumpLogRecords(PWSTR pwszLogFileName, CLFS_RECORD_TYPE fRecordType, PCLFS_LSN plsnStart, PCLFS_LSN plsnEnd, PFILE pstrmOut, CLFS_PRINT_RECORD_ROUTINE pfnPrintRecord, CLFS_BLOCK_ALLOCATION pfnAllocBlock, CLFS_BLOCK_DEALLOCATION pfnFreeBlock, PVOID pvBlockAllocContext, ULONG cbBlock, ULONG cMaxBlocks)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pwszLogFileName", "fRecordType", "plsnStart", "plsnEnd", "pstrmOut", "pfnPrintRecord", "pfnAllocBlock", "pfnFreeBlock", "pvBlockAllocContext", "cbBlock", "cMaxBlocks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_FlushLogBuffers(jitter):
    """"
    [Clfsw32.dll] BOOL FlushLogBuffers(PVOID pvMarshal, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_FlushLogToLsn(jitter):
    """"
    [Clfsw32.dll] BOOL FlushLogToLsn(PVOID pvMarshalContext, PCLFS_LSN plsnFlush, PCLFS_LSN plsnLastFlushed, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshalContext", "plsnFlush", "plsnLastFlushed", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_FreeReservedLog(jitter):
    """"
    [Clfsw32.dll] BOOL FreeReservedLog(PVOID pvMarshal, ULONG cReservedRecords, PLONGLONG pcbAdjustment)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "cReservedRecords", "pcbAdjustment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReserveAndAppendLog(jitter):
    """"
    [Clfsw32.dll] BOOL ReserveAndAppendLog(PVOID pvMarshal, PCLFS_WRITE_ENTRY rgWriteEntries, ULONG cWriteEntries, PCLFS_LSN plsnUndoNext, PCLFS_LSN plsnPrevious, ULONG cReserveRecords, LONGLONG [] rgcbReservation, ULONG fFlags, PCLFS_LSN plsn, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "rgWriteEntries", "cWriteEntries", "plsnUndoNext", "plsnPrevious", "cReserveRecords", "rgcbReservation", "fFlags", "plsn", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReserveAndAppendLogAligned(jitter):
    """"
    [Clfsw32.dll] BOOL ReserveAndAppendLogAligned(PVOID pvMarshal, PCLFS_WRITE_ENTRY rgWriteEntries, ULONG cWriteEntries, ULONG cbEntryAlignment, PCLFS_LSN plsnUndoNext, PCLFS_LSN plsnPrevious, ULONG cReserveRecords, LONGLONG [] rgcbReservation, ULONG fFlags, PCLFS_LSN plsn, LPOVERLAPPED overlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "rgWriteEntries", "cWriteEntries", "cbEntryAlignment", "plsnUndoNext", "plsnPrevious", "cReserveRecords", "rgcbReservation", "fFlags", "plsn", "overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetLogFileInformation(jitter):
    """"
    [Clfsw32.dll] BOOL GetLogFileInformation(HANDLE hLog, PCLFS_INFORMATION pinfoBuffer, PULONG cbBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pinfoBuffer", "cbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetLogIoStatistics(jitter):
    """"
    [Clfsw32.dll] BOOL GetLogIoStatistics(HANDLE hLog, PVOID pvStatsBuffer, ULONG cbStatsBuffer, CLFS_IOSTATS_CLASS eStatsClass, PULONG pcbStatsWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pvStatsBuffer", "cbStatsBuffer", "eStatsClass", "pcbStatsWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadLogRecord(jitter):
    """"
    [Clfsw32.dll] BOOL ReadLogRecord(PVOID pvMarshal, PCLFS_LSN plsnFirst, CLFS_CONTEXT_MODE eContextMode, PVOID* ppvReadBuffer, PULONG pcbReadBuffer, PCLFS_RECORD_TYPE peRecordType, PCLFS_LSN plsnUndoNext, PCLFS_LSN plsnPrevious, PVOID* ppvReadContext, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "plsnFirst", "eContextMode", "ppvReadBuffer", "pcbReadBuffer", "peRecordType", "plsnUndoNext", "plsnPrevious", "ppvReadContext", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadNextLogRecord(jitter):
    """"
    [Clfsw32.dll] BOOL ReadNextLogRecord(PVOID pvReadContext, PVOID* ppvBuffer, PULONG pcbBuffer, PCLFS_RECORD_TYPE peRecordType, PCLFS_LSN plsnUser, PCLFS_LSN plsnUndoNext, PCLFS_LSN plsnPrevious, PCLFS_LSN plsnRecord, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvReadContext", "ppvBuffer", "pcbBuffer", "peRecordType", "plsnUser", "plsnUndoNext", "plsnPrevious", "plsnRecord", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_SetEndOfLog(jitter):
    """"
    [Clfsw32.dll] BOOL SetEndOfLog(HANDLE hLog, PCLFS_LSN plsnEnd, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "plsnEnd", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_TruncateLog(jitter):
    """"
    [Clfsw32.dll] BOOL TruncateLog(PVOID pvMarshal, PCLFS_LSN plsnEnd, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "plsnEnd", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_TerminateReadLog(jitter):
    """"
    [Clfsw32.dll] BOOL TerminateReadLog(PVOID pvCursorContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvCursorContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetLogReservationInfo(jitter):
    """"
    [Clfsw32.dll] BOOL GetLogReservationInfo(PVOID pvMarshal, PULONG pcbRecordNumber, PLONGLONG pcbUserReservation, PLONGLONG pcbCommitReservation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "pcbRecordNumber", "pcbUserReservation", "pcbCommitReservation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_AddLogContainer(jitter):
    """"
    [Clfsw32.dll] BOOL AddLogContainer(HANDLE hLog, PULONGLONG pcbContainer, LPWSTR pwszContainerPath, LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pcbContainer", "pwszContainerPath", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_AddLogContainerSet(jitter):
    """"
    [Clfsw32.dll] BOOL AddLogContainerSet(HANDLE hLog, USHORT cContainers, PULONGLONG pcbContainer, LPWSTR* rgwszContainerPath, PVOID Reserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cContainers", "pcbContainer", "rgwszContainerPath", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_CreateLogContainerScanContext(jitter):
    """"
    [Clfsw32.dll] BOOL CreateLogContainerScanContext(HANDLE hLog, ULONG cFromContainer, ULONG cContainers, CLFS_SCAN_MODE eScanMode, PCLFS_SCAN_CONTEXT pcxScan, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cFromContainer", "cContainers", "eScanMode", "pcxScan", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ScanLogContainers(jitter):
    """"
    [Clfsw32.dll] BOOL ScanLogContainers(PCLFS_SCAN_CONTEXT pcxScan, CLFS_SCAN_MODE eScanMode, LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcxScan", "eScanMode", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetLogContainerName(jitter):
    """"
    [Clfsw32.dll] BOOL GetLogContainerName(HANDLE hLog, CLFS_CONTAINER_ID cidLogicalContainer, LPCWSTR pwstrContainerName, ULONG cLenContainerName, PULONG pcActualLenContainerName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cidLogicalContainer", "pwstrContainerName", "cLenContainerName", "pcActualLenContainerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RemoveLogContainer(jitter):
    """"
    [Clfsw32.dll] BOOL RemoveLogContainer(HANDLE hLog, LPWSTR pwszContainerPath, BOOL fForce, LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pwszContainerPath", "fForce", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RemoveLogContainerSet(jitter):
    """"
    [Clfsw32.dll] BOOL RemoveLogContainerSet(HANDLE hLog, USHORT cContainers, LPWSTR* rgwszContainerPath, BOOL fForce, LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cContainers", "rgwszContainerPath", "fForce", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_AdvanceLogBase(jitter):
    """"
    [Clfsw32.dll] BOOL AdvanceLogBase(PVOID pvMarshal, PCLFS_LSN plsnBase, ULONG fFlags, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "plsnBase", "fFlags", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadLogRestartArea(jitter):
    """"
    [Clfsw32.dll] BOOL ReadLogRestartArea(PVOID pvMarshal, PVOID* ppvRestartBuffer, PULONG pcbRestartBuffer, PCLFS_LSN plsn, PVOID* ppvContext, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "ppvRestartBuffer", "pcbRestartBuffer", "plsn", "ppvContext", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadPreviousLogRestartArea(jitter):
    """"
    [Clfsw32.dll] BOOL ReadPreviousLogRestartArea(PVOID pvReadContext, PVOID* ppvRestartBuffer, PULONG pcbRestartBuffer, PCLFS_LSN plsnRestart, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvReadContext", "ppvRestartBuffer", "pcbRestartBuffer", "plsnRestart", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_WriteLogRestartArea(jitter):
    """"
    [Clfsw32.dll] BOOL WriteLogRestartArea(PVOID pvMarshal, PVOID pvRestartBuffer, ULONG cbRestartBuffer, PCLFS_LSN plsnBase, ULONG fFlags, PULONG pcbWritten, PCLFS_LSN plsnNext, LPOVERLAPPED pOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal", "pvRestartBuffer", "cbRestartBuffer", "plsnBase", "fFlags", "pcbWritten", "plsnNext", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_GetNextLogArchiveExtent(jitter):
    """"
    [Clfsw32.dll] BOOL GetNextLogArchiveExtent(CLFS_LOG_ARCHIVE_CONTEXT pvArchiveContext, CLFS_ARCHIVE_DESCRIPTOR [] rgadExtent, ULONG cDescriptors, PULONG pcDescriptorsReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvArchiveContext", "rgadExtent", "cDescriptors", "pcDescriptorsReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_PrepareLogArchive(jitter):
    """"
    [Clfsw32.dll] BOOL PrepareLogArchive(HANDLE hLog, PWSTR pszBaseLogFileName, ULONG cLen, const PCLFS_LSN plsnLow, const PCLFS_LSN plsnHigh, PULONG pcActualLength, PULONGLONG poffBaseLogFileData, PULONGLONG pcbBaseLogFileLength, PCLFS_LSN plsnBase, PCLFS_LSN plsnLast, PCLFS_LSN plsnCurrentArchiveTail, PCLFS_LOG_ARCHIVE_CONTEXT ppvArchiveContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pszBaseLogFileName", "cLen", "plsnLow", "plsnHigh", "pcActualLength", "poffBaseLogFileData", "pcbBaseLogFileLength", "plsnBase", "plsnLast", "plsnCurrentArchiveTail", "ppvArchiveContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadLogArchiveMetadata(jitter):
    """"
    [Clfsw32.dll] BOOL ReadLogArchiveMetadata(CLFS_LOG_ARCHIVE_CONTEXT pvArchiveContext, ULONG cbOffset, ULONG cbBytesToRead, PBYTE pbReadBuffer, PULONG pcbBytesRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvArchiveContext", "cbOffset", "cbBytesToRead", "pbReadBuffer", "pcbBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_SetLogArchiveMode(jitter):
    """"
    [Clfsw32.dll] BOOL SetLogArchiveMode(HANDLE hLog, CLFS_LOG_ARCHIVE_MODE eMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "eMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_SetLogArchiveTail(jitter):
    """"
    [Clfsw32.dll] BOOL SetLogArchiveTail(HANDLE hLog, PCLFS_LSN plsnArchiveTail, LPVOID pReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "plsnArchiveTail", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_TerminateLogArchive(jitter):
    """"
    [Clfsw32.dll] BOOL TerminateLogArchive(CLFS_LOG_ARCHIVE_CONTEXT pvArchiveContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvArchiveContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ValidateLog(jitter):
    """"
    [Clfsw32.dll] BOOL ValidateLog(LPCWSTR pszLogFileName, LPSECURITY_ATTRIBUTES psaLogFile, PCLFS_INFORMATION pinfoBuffer, PULONG pcbBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszLogFileName", "psaLogFile", "pinfoBuffer", "pcbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_CreateLogMarshallingArea(jitter):
    """"
    [Clfsw32.dll] BOOL CreateLogMarshallingArea(HANDLE hLog, CLFS_BLOCK_ALLOCATION pfnAllocBuffer, CLFS_BLOCK_DEALLOCATION pfnFreeBuffer, PVOID pvBlockAllocContext, ULONG cbMarshallingBuffer, ULONG cMaxWriteBuffers, ULONG cMaxReadBuffers, PVOID* ppvMarshal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pfnAllocBuffer", "pfnFreeBuffer", "pvBlockAllocContext", "cbMarshallingBuffer", "cMaxWriteBuffers", "cMaxReadBuffers", "ppvMarshal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DeleteLogMarshallingArea(jitter):
    """"
    [Clfsw32.dll] BOOL DeleteLogMarshallingArea(PVOID pvMarshal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvMarshal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnBlockOffset(jitter):
    """"
    [Clfsw32.dll] ULONG LsnBlockOffset(const CLFS_LSN* plsn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnContainer(jitter):
    """"
    [Clfsw32.dll] CLFS_CONTAINER_ID LsnContainer(const CLFS_LSN* plsn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnCreate(jitter):
    """"
    [Clfsw32.dll] CLFS_LSN LsnCreate(CLFS_CONTAINER_ID cidContainer, ULONG offBlock, ULONG cRecord)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cidContainer", "offBlock", "cRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnEqual(jitter):
    """"
    [Clfsw32.dll] BOOL LsnEqual(const CLFS_LSN* plsn1, const CLFS_LSN* plsn2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn1", "plsn2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnGreater(jitter):
    """"
    [Clfsw32.dll] BOOL LsnGreater(const CLFS_LSN* plsn1, const CLFS_LSN* plsn2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn1", "plsn2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnLess(jitter):
    """"
    [Clfsw32.dll] BOOL LsnLess(const CLFS_LSN* plsn1, const CLFS_LSN* plsn2)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn1", "plsn2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnNull(jitter):
    """"
    [Clfsw32.dll] BOOL LsnNull(const CLFS_LSN* plsn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnRecordSequence(jitter):
    """"
    [Clfsw32.dll] ULONG LsnRecordSequence(const CLFS_LSN* plsn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnDecrement(jitter):
    """"
    [Clfsw32.dll] CLFS_LSN LsnDecrement(PCLFS_LSN plsn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnIncrement(jitter):
    """"
    [Clfsw32.dll] CLFS_LSN LsnIncrement(PCLFS_LSN plsn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LsnInvalid(jitter):
    """"
    [Clfsw32.dll] BOOL LsnInvalid(const CLFS_LSN* plsn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["plsn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_DeregisterManageableLogClient(jitter):
    """"
    [Clfsw32.dll] BOOL DeregisterManageableLogClient(HANDLE hLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_HandleLogFull(jitter):
    """"
    [Clfsw32.dll] BOOL HandleLogFull(HANDLE hLog)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_InstallLogPolicy(jitter):
    """"
    [Clfsw32.dll] BOOL InstallLogPolicy(HANDLE hLog, PCLFS_MGMT_POLICY pPolicy)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pPolicy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_LogTailAdvanceFailure(jitter):
    """"
    [Clfsw32.dll] BOOL LogTailAdvanceFailure(HANDLE hLog, [ERROR_CODE] dwReason)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "dwReason"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_QueryLogPolicy(jitter):
    """"
    [Clfsw32.dll] BOOL QueryLogPolicy(HANDLE hLog, CLFS_MGMT_POLICY_TYPE ePolicyType, PCLFS_MGMT_POLICY pPolicyBuffer, PULONG pcbPolicyBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "ePolicyType", "pPolicyBuffer", "pcbPolicyBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_ReadLogNotification(jitter):
    """"
    [Clfsw32.dll] BOOL ReadLogNotification(HANDLE hLog, PCLFS_MGMT_NOTIFICATION pNotification, LPOVERLAPPED lpOverlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pNotification", "lpOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RegisterForLogWriteNotification(jitter):
    """"
    [Clfsw32.dll] BOOL RegisterForLogWriteNotification(HANDLE hLog, ULONG cbThreshold, BOOL fEnable)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "cbThreshold", "fEnable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RemoveLogPolicy(jitter):
    """"
    [Clfsw32.dll] BOOL RemoveLogPolicy(HANDLE hLog, CLFS_MGMT_POLICY_TYPE ePolicyType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "ePolicyType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_RegisterManageableLogClient(jitter):
    """"
    [Clfsw32.dll] BOOL RegisterManageableLogClient(HANDLE hLog, PLOG_MANAGEMENT_CALLBACKS pCallbacks)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pCallbacks"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def clfsw32_SetLogFileSizeWithPolicy(jitter):
    """"
    [Clfsw32.dll] BOOL SetLogFileSizeWithPolicy(HANDLE hLog, PULONGLONG pDesiredSize, PULONGLONG pResultingSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hLog", "pDesiredSize", "pResultingSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
