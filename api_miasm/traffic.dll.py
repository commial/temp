_QOS_OBJECT_HDR_TYPE_ = {
    "QOS_OBJECT_END_OF_LIST": 2001,
    "QOS_OBJECT_SD_MODE": 2002,
    "QOS_OBJECT_SHAPING_RATE": 2003,
    "QOS_OBJECT_DESTADDR": 2004,
    "RSVP_OBJECT_STATUS_INFO": 1000,
    "RSVP_OBJECT_RESERVE_INFO": 1001,
    "RSVP_OBJECT_ADSPEC": 1002,
    "RSVP_OBJECT_POLICY_INFO": 1003,
    "RSVP_OBJECT_FILTERSPEC_LIST": 1004,
}

def traffic_TcAddFilter(jitter):
    """
    [ERROR_CODE_ULONG] TcAddFilter(
        HANDLE FlowHandle,
        PTC_GEN_FILTER pGenericFilter,
        PHANDLE pFilterHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FlowHandle", "pGenericFilter", "pFilterHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcAddFlow(jitter):
    """
    [ERROR_CODE_ULONG] TcAddFlow(
        HANDLE IfcHandle,
        HANDLE ClFlowCtx,
        ULONG Flags,
        PTC_GEN_FLOW pGenericFlow,
        PHANDLE pFlowHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfcHandle", "ClFlowCtx", "Flags", "pGenericFlow", "pFlowHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcCloseInterface(jitter):
    """
    [ERROR_CODE_ULONG] TcCloseInterface(
        HANDLE IfcHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfcHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcDeleteFilter(jitter):
    """
    [ERROR_CODE_ULONG] TcDeleteFilter(
        HANDLE FilterHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FilterHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcDeleteFlow(jitter):
    """
    [ERROR_CODE_ULONG] TcDeleteFlow(
        HANDLE FlowHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FlowHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcDeregisterClient(jitter):
    """
    [ERROR_CODE_ULONG] TcDeregisterClient(
        HANDLE ClientHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcEnumerateFlows(jitter):
    """
    [ERROR_CODE_ULONG] TcEnumerateFlows(
        HANDLE IfcHandle,
        PHANDLE pEnumToken,
        PULONG pFlowCount,
        PULONG pBufSize,
        PENUMERATION_BUFFER Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfcHandle", "pEnumToken", "pFlowCount", "pBufSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcEnumerateInterfaces(jitter):
    """
    [ERROR_CODE_ULONG] TcEnumerateInterfaces(
        HANDLE ClientHandle,
        PULONG pBufferSize,
        PTC_IFC_DESCRIPTOR InterfaceBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientHandle", "pBufferSize", "InterfaceBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcGetFlowName(jitter, get_str, set_str):
    """
    [ERROR_CODE_ULONG] TcGetFlowName(
        HANDLE FlowHandle,
        ULONG StrSize,
        LPTSTR pFlowName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FlowHandle", "StrSize", "pFlowName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcGetFlowNameA(jitter):
    traffic_TcGetFlowName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def traffic_TcGetFlowNameW(jitter):
    traffic_TcGetFlowName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def traffic_TcModifyFlow(jitter):
    """
    [ERROR_CODE_ULONG] TcModifyFlow(
        HANDLE FlowHandle,
        PTC_GEN_FLOW pGenericFlow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FlowHandle", "pGenericFlow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcOpenInterface(jitter, get_str, set_str):
    """
    [ERROR_CODE_ULONG] TcOpenInterface(
        LPTSTR pInterfaceName,
        HANDLE ClientHandle,
        HANDLE ClIfcCtx,
        PHANDLE pIfcHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pInterfaceName", "ClientHandle", "ClIfcCtx", "pIfcHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcOpenInterfaceA(jitter):
    traffic_TcOpenInterface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def traffic_TcOpenInterfaceW(jitter):
    traffic_TcOpenInterface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def traffic_TcQueryFlow(jitter, get_str, set_str):
    """
    [ERROR_CODE_ULONG] TcQueryFlow(
        LPTSTR FlowName,
        LPGUID pGuidParam,
        PULONG pBufferSize,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["FlowName", "pGuidParam", "pBufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcQueryFlowA(jitter):
    traffic_TcQueryFlow(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def traffic_TcQueryFlowW(jitter):
    traffic_TcQueryFlow(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def traffic_TcQueryInterface(jitter):
    """
    [ERROR_CODE_ULONG] TcQueryInterface(
        HANDLE IfcHandle,
        LPGUID pGuidParam,
        BOOLEAN NotifyChange,
        PULONG BufferSize,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfcHandle", "pGuidParam", "NotifyChange", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcRegisterClient(jitter):
    """
    [ERROR_CODE_ULONG] TcRegisterClient(
        ULONG TciVersion,
        HANDLE ClRegCtx,
        PTCI_CLIENT_FUNC_LIST pClientHandlerList,
        PHANDLE pClientHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TciVersion", "ClRegCtx", "pClientHandlerList", "pClientHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcSetFlow(jitter, get_str, set_str):
    """
    [ERROR_CODE_ULONG] TcSetFlow(
        LPTSTR pFlowName,
        LPGUID pGuidParam,
        ULONG BufferSize,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlowName", "pGuidParam", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def traffic_TcSetFlowA(jitter):
    traffic_TcSetFlow(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def traffic_TcSetFlowW(jitter):
    traffic_TcSetFlow(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def traffic_TcSetInterface(jitter):
    """
    [ERROR_CODE_ULONG] TcSetInterface(
        HANDLE IfcHandle,
        LPGUID pGuidParam,
        ULONG BufferSize,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfcHandle", "pGuidParam", "BufferSize", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
