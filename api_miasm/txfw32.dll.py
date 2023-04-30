###### Enums ######

###################

###### Types ######

class TXF_ID(MemStruct):
    fields = [
        ("LowPart", LONGLONG()),
        ("HighPart", LONGLONG()),
    ]

PTXF_ID = Ptr("<I", TXF_ID())

###################

###### Functions ######

def txfw32_TxfLogCreateFileReadContext(jitter):
    """
    BOOL TxfLogCreateFileReadContext(
        LPCWSTR LogPath,
        CLFS_LSN BeginningLsn,
        CLFS_LSN EndingLSN,
        PTXF_ID TxfFileId,
        PVOID* TxfLogContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogPath", "BeginningLsn", "EndingLSN", "TxfFileId", "TxfLogContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def txfw32_TxfLogDestroyReadContext(jitter):
    """
    BOOL TxfLogDestroyReadContext(
        PVOID TxfLogContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TxfLogContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def txfw32_TxfLogReadRecords(jitter):
    """
    BOOL TxfLogReadRecords(
        PVOID TxfLogContext,
        ULONG BufferLength,
        PVOID Buffer,
        PULONG BytesUsed,
        PULONG RecordCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TxfLogContext", "BufferLength", "Buffer", "BytesUsed", "RecordCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
