###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def wsock32_inet_addr(jitter):
    """
    [INET_ADDR_OUTPUT] inet_addr(
        const char* cp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsock32_inet_ntoa(jitter):
    """
    char* inet_ntoa(
        struct in_addr in
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["in"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsock32_ioctlsocket(jitter):
    """
    [SocketCode-int] ioctlsocket(
        SOCKET s,
        [Socket_IOCTL] cmd,
        u_long* argp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["s", "cmd", "argp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
