
def icmp_IcmpCloseHandle(jitter):
    """
    BOOL IcmpCloseHandle(
        HANDLE IcmpHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icmp_IcmpCreateFile(jitter):
    """
    HANDLE IcmpCreateFile()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icmp_IcmpParseReplies(jitter):
    """
    DWORD IcmpParseReplies(
        LPVOID ReplyBuffer,
        DWORD ReplySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReplyBuffer", "ReplySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icmp_IcmpSendEcho(jitter):
    """
    DWORD IcmpSendEcho(
        HANDLE IcmpHandle,
        IPAddr DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icmp_IcmpSendEcho2(jitter):
    """
    DWORD IcmpSendEcho2(
        HANDLE IcmpHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        IPAddr DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "Event", "ApcRoutine", "ApcContext", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
