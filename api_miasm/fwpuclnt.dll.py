###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def fwpuclnt_WSADeleteSocketPeerTargetName(jitter):
    """
    [SocketCode-int] WSADeleteSocketPeerTargetName(
        SOCKET Socket,
        const struct sockaddr* PeerAddr,
        ULONG PeerAddrLen,
        LPWSAOVERLAPPED Overlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE CompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Socket", "PeerAddr", "PeerAddrLen", "Overlapped", "CompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fwpuclnt_WSAImpersonateSocketPeer(jitter):
    """
    [SocketCode-int] WSAImpersonateSocketPeer(
        SOCKET Socket,
        const sockaddr* PeerAddress,
        ULONG peerAddressLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Socket", "PeerAddress", "peerAddressLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fwpuclnt_WSAQuerySocketSecurity(jitter):
    """
    [SocketCode-int] WSAQuerySocketSecurity(
        SOCKET Socket,
        const SOCKET_SECURITY_QUERY_TEMPLATE* SecurityQueryTemplate,
        ULONG SecurityQueryTemplateLen,
        SOCKET_SECURITY_QUERY_INFO* SecurityQueryInfo,
        ULONG* SecurityQueryInfoLen,
        LPWSAOVERLAPPED Overlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE CompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Socket", "SecurityQueryTemplate", "SecurityQueryTemplateLen", "SecurityQueryInfo", "SecurityQueryInfoLen", "Overlapped", "CompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fwpuclnt_WSARevertImpersonation(jitter):
    """
    [SocketCode-int] WSARevertImpersonation()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fwpuclnt_WSASetSocketPeerTargetName(jitter):
    """
    [SocketCode-int] WSASetSocketPeerTargetName(
        SOCKET Socket,
        const SOCKET_PEER_TARGET_NAME* PeerTargetName,
        ULONG PeerTargetNameLen,
        LPWSAOVERLAPPED Overlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE CompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Socket", "PeerTargetName", "PeerTargetNameLen", "Overlapped", "CompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def fwpuclnt_WSASetSocketSecurity(jitter):
    """
    [SocketCode-int] WSASetSocketSecurity(
        SOCKET Socket,
        const SOCKET_SECURITY_SETTINGS* SecuritySettings,
        ULONG SecuritySettingsLen,
        LPWSAOVERLAPPED Overlapped,
        LPWSAOVERLAPPED_COMPLETION_ROUTINE CompletionRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Socket", "SecuritySettings", "SecuritySettingsLen", "Overlapped", "CompletionRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
