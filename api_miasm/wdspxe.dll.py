PXE_BOOT_ACTION = {
    "PXE_BA_NBP": 1,
    "PXE_BA_CUSTOM": 2,
    "PXE_BA_IGNORE": 3,
    "PXE_BA_REJECTED": 4,
}
PXE_SEVERITY = {
    "PXE_TRACE_VERBOSE": 0x00010000,
    "PXE_TRACE_INFO": 0x00020000,
    "PXE_TRACE_WARNING": 0x00040000,
    "PXE_TRACE_ERROR": 0x00080000,
    "PXE_TRACE_FATAL": 0x00100000,
}
PXE_GSI_TYPE = {
    "PXE_GSI_TRACE_ENABLED": 1,
}
PXE_REG_INDEX = {
    "PXE_REG_INDEX_TOP": 0,
    "PXE_REG_INDEX_BOTTOM": 0xFFFFFFFF,
}
PXE_PROVIDER_ATTRIBUTE = {
    "PXE_PROV_ATTR_FILTER": 0,
}
PXE_CALLBACK_TYPE = {
    "PXE_CALLBACK_RECV_REQUEST": 0,
    "PXE_CALLBACK_SHUTDOWN": 1,
    "PXE_CALLBACK_SERVICE_CONTROL": 2,
}

def wdspxe_PxeAsyncRecvDone(jitter):
    """
    [ERROR_CODE] PxeAsyncRecvDone(
        HANDLE hClientRequest,
        PXE_BOOT_ACTION Action
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientRequest", "Action"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpAppendOption(jitter):
    """
    [ERROR_CODE] PxeDhcpAppendOption(
        PVOID pReplyPacket,
        ULONG uMaxReplyPacketLen,
        PULONG puReplyPacketLen,
        BYTE bOption,
        BYTE bOptionLen,
        PVOID pValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pReplyPacket", "uMaxReplyPacketLen", "puReplyPacketLen", "bOption", "bOptionLen", "pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpv6AppendOption(jitter):
    """
    [ERROR_CODE] PxeDhcpv6AppendOption(
        PVOID pReply,
        ULONG cbReply,
        PULONG pcbReplyUsed,
        WORD wOptionType,
        WORD cbOption,
        PVOID pOption
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pReply", "cbReply", "pcbReplyUsed", "wOptionType", "cbOption", "pOption"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpv6AppendOptionRaw(jitter):
    """
    [ERROR_CODE] PxeDhcpv6AppendOptionRaw(
        PVOID pReply,
        ULONG cbReply,
        PULONG pcbReplyUsed,
        USHORT cbBuffer,
        PVOID pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pReply", "cbReply", "pcbReplyUsed", "cbBuffer", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpGetOptionValue(jitter):
    """
    [ERROR_CODE] PxeDhcpGetOptionValue(
        PVOID pPacket,
        ULONG uPacketLen,
        ULONG uInstance,
        BYTE bOption,
        PBYTE pbOptionLen,
        PVOID* ppOptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPacket", "uPacketLen", "uInstance", "bOption", "pbOptionLen", "ppOptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpv6GetOptionValue(jitter):
    """
    [ERROR_CODE] PxeDhcpv6GetOptionValue(
        PVOID pPacket,
        ULONG uPacketLen,
        ULONG uInstance,
        WORD wOption,
        PWORD pwOptionLen,
        PVOID* ppOptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPacket", "uPacketLen", "uInstance", "wOption", "pwOptionLen", "ppOptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpGetVendorOptionValue(jitter):
    """
    [ERROR_CODE] PxeDhcpGetVendorOptionValue(
        PVOID pPacket,
        ULONG uPacketLen,
        BYTE bOption,
        ULONG uInstance,
        PBYTE pbOptionLen,
        PVOID* ppOptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPacket", "uPacketLen", "bOption", "uInstance", "pbOptionLen", "ppOptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpv6GetVendorOptionValue(jitter):
    """
    [ERROR_CODE] PxeDhcpv6GetVendorOptionValue(
        PVOID pPacket,
        ULONG uPacketLen,
        DWORD dwEnterpriseNumber,
        WORD wOption,
        ULONG uInstance,
        PWORD pwOptionLen,
        PVOID* ppOptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPacket", "uPacketLen", "dwEnterpriseNumber", "wOption", "uInstance", "pwOptionLen", "ppOptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpInitialize(jitter):
    """
    [ERROR_CODE] PxeDhcpInitialize(
        PVOID pRecvPacket,
        ULONG uRecvPacketLen,
        PVOID pReplyPacket,
        ULONG uMaxReplyPacketLen,
        PULONG puReplyPacketLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecvPacket", "uRecvPacketLen", "pReplyPacket", "uMaxReplyPacketLen", "puReplyPacketLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpv6Initialize(jitter):
    """
    [ERROR_CODE] PxeDhcpv6Initialize(
        PVOID pRequest,
        ULONG cbRequest,
        PVOID pReply,
        ULONG cbReply,
        PULONG pcbReplyUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRequest", "cbRequest", "pReply", "cbReply", "pcbReplyUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpIsValid(jitter):
    """
    [ERROR_CODE] PxeDhcpIsValid(
        PVOID pPacket,
        ULONG uPacketLen,
        BOOL bRequestPacket,
        PBOOL pbPxeOptionPresent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPacket", "uPacketLen", "bRequestPacket", "pbPxeOptionPresent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpv6IsValid(jitter):
    """
    [ERROR_CODE] PxeDhcpv6IsValid(
        PVOID pPacket,
        ULONG uPacketLen,
        BOOL bRequestPacket,
        PBOOL pbPxeOptionPresent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPacket", "uPacketLen", "bRequestPacket", "pbPxeOptionPresent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeGetServerInfo(jitter):
    """
    [ERROR_CODE] PxeGetServerInfo(
        PXE_GSI_TYPE uInfoType,
        PVOID pBuffer,
        ULONG uBufferLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uInfoType", "pBuffer", "uBufferLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeGetServerInfoEx(jitter):
    """
    [ERROR_CODE] PxeGetServerInfoEx(
        PXE_GSI_TYPE uInfoType,
        PVOID pBuffer,
        ULONG uBufferLen,
        PULONG puBufferUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uInfoType", "pBuffer", "uBufferLen", "puBufferUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxePacketAllocate(jitter):
    """
    PVOID PxePacketAllocate(
        HANDLE hProvider,
        HANDLE hClientRequest,
        ULONG uSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "hClientRequest", "uSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxePacketFree(jitter):
    """
    [ERROR_CODE] PxePacketFree(
        HANDLE hProvider,
        HANDLE hClientRequest,
        PVOID pPacket
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "hClientRequest", "pPacket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeProviderEnumClose(jitter):
    """
    [ERROR_CODE] PxeProviderEnumClose(
        HANDLE hEnum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeProviderEnumFirst(jitter):
    """
    [ERROR_CODE] PxeProviderEnumFirst(
        HANDLE* phEnum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phEnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeProviderEnumNext(jitter):
    """
    [ERROR_CODE] PxeProviderEnumNext(
        HANDLE hEnum,
        PPXE_PROVIDER* ppProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hEnum", "ppProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeProviderFreeInfo(jitter):
    """
    [ERROR_CODE] PxeProviderFreeInfo(
        PPXE_PROVIDER pProvider
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeProviderQueryIndex(jitter):
    """
    [ERROR_CODE] PxeProviderQueryIndex(
        LPCWSTR pszProviderName,
        PULONG puIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszProviderName", "puIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeProviderRegister(jitter):
    """
    [ERROR_CODE] PxeProviderRegister(
        LPCWSTR pszProviderName,
        LPCWSTR pszModulePath,
        PXE_REG_INDEX Index,
        BOOL bIsCritical,
        PHKEY phProviderKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszProviderName", "pszModulePath", "Index", "bIsCritical", "phProviderKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeProviderSetAttribute(jitter):
    """
    [ERROR_CODE] PxeProviderSetAttribute(
        HANDLE hProvider,
        PXE_PROVIDER_ATTRIBUTE Attribute,
        PVOID pParameterBuffer,
        ULONG uParamLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "Attribute", "pParameterBuffer", "uParamLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeProviderUnRegister(jitter):
    """
    [ERROR_CODE] PxeProviderUnRegister(
        LPCWSTR pszProviderName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszProviderName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeRegisterCallback(jitter):
    """
    [ERROR_CODE] PxeRegisterCallback(
        HANDLE hProvider,
        PXE_CALLBACK_TYPE CallbackType,
        PVOID pCallbackFunction,
        PVOID pContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "CallbackType", "pCallbackFunction", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeSendReply(jitter):
    """
    [ERROR_CODE] PxeSendReply(
        HANDLE hClientRequest,
        PVOID pPacket,
        ULONG uPacketLen,
        PXE_ADDRESS* pAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientRequest", "pPacket", "uPacketLen", "pAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeTrace(jitter):
    """
    [ERROR_CODE] PxeTrace(
        HANDLE hProvider,
        PXE_SEVERITY Severity,
        LPCWSTR pszFormat,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "Severity", "pszFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpv6ParseRelayForw(jitter):
    """
    [ERROR_CODE] PxeDhcpv6ParseRelayForw(
        PVOID pRelayForwPacket,
        ULONG uRelayForwPacketLen,
        PPXE_DHCPV6_NESTED_RELAY_MESSAGE pRelayMessages,
        ULONG nRelayMessages,
        PULONG pnRelayMessages,
        PBYTE* ppInnerPacket,
        PULONG pcbInnerPacket
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRelayForwPacket", "uRelayForwPacketLen", "pRelayMessages", "nRelayMessages", "pnRelayMessages", "ppInnerPacket", "pcbInnerPacket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wdspxe_PxeDhcpv6CreateRelayRepl(jitter):
    """
    [ERROR_CODE] PxeDhcpv6CreateRelayRepl(
        PPXE_DHCPV6_NESTED_RELAY_MESSAGE pRelayMessages,
        ULONG nRelayMessages,
        PBYTE pInnerPacket,
        ULONG cbInnerPacket,
        PVOID pReplyBuffer,
        ULONG cbReplyBuffer,
        PULONG pcbReplyBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRelayMessages", "nRelayMessages", "pInnerPacket", "cbInnerPacket", "pReplyBuffer", "cbReplyBuffer", "pcbReplyBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
