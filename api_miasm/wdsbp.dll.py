###### Enums ######

###################

###### Types ######
_WDSBP_PK_TYPE_ = BYTE
_WDSBP_PK_TYPE_PTR_ = Ptr("<I", _WDSBP_PK_TYPE_())

###################

###### Functions ######

def wdsbp_WdsBpAddOption(jitter):
    """
    HRESULT WdsBpAddOption(
        HANDLE hHandle,
        ULONG uOption,
        ULONG uValueLen,
        PVOID pValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHandle", "uOption", "uValueLen", "pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsbp_WdsBpCloseHandle(jitter):
    """
    HRESULT WdsBpCloseHandle(
        HANDLE hHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsbp_WdsBpGetOptionBuffer(jitter):
    """
    HRESULT WdsBpGetOptionBuffer(
        HANDLE hHandle,
        ULONG uBufferLen,
        PVOID pBuffer,
        PULONG puBytes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHandle", "uBufferLen", "pBuffer", "puBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsbp_WdsBpInitialize(jitter):
    """
    HRESULT WdsBpInitialize(
        [WDSBP_PK_TYPE] bPacketType,
        HANDLE* phHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bPacketType", "phHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsbp_WdsBpParseInitialize(jitter):
    """
    HRESULT WdsBpParseInitialize(
        PVOID pPacket,
        ULONG uPacketLen,
        [WDSBP_PK_TYPE] pbPacketType,
        HANDLE* phHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPacket", "uPacketLen", "pbPacketType", "phHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsbp_WdsBpQueryOption(jitter):
    """
    HRESULT WdsBpQueryOption(
        HANDLE hHandle,
        ULONG uOption,
        ULONG uValueLen,
        PVOID pValue,
        PULONG puBytes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hHandle", "uOption", "uValueLen", "pValue", "puBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdsbp_WdsBpParseInitializev6(jitter):
    """
    HRESULT WdsBpParseInitializev6(
        PVOID pPacket,
        ULONG uPacketLen,
        [WDSBP_PK_TYPE] pbPacketType,
        HANDLE* phHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPacket", "uPacketLen", "pbPacketType", "phHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
