
def rpcrt4_DceErrorInqText(jitter, get_str, set_str):
    """
    RPC_STATUS DceErrorInqText(
        unsigned long StatusToConvert,
        RPC_TSTR ErrorText
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatusToConvert", "ErrorText"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_DceErrorInqTextA(jitter):
    rpcrt4_DceErrorInqText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_DceErrorInqTextW(jitter):
    rpcrt4_DceErrorInqText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_MesBufferHandleReset(jitter):
    """
    RPC_STATUS MesBufferHandleReset(
        handle_t Handle,
        MIDL_ES_HANDLE_STYLE HandleStyle,
        MIDL_ES_CODE OpCode,
        char** ppBuffer,
        unsigned long BufferSize,
        unsigned long* pEncodedSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "HandleStyle", "OpCode", "ppBuffer", "BufferSize", "pEncodedSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_MesDecodeBufferHandleCreate(jitter):
    """
    RPC_STATUS MesDecodeBufferHandleCreate(
        [LPVOID|char*] Buffer,
        unsigned long BufferSize,
        handle_t* pHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "BufferSize", "pHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_MesDecodeIncrementalHandleCreate(jitter):
    """
    RPC_STATUS MesDecodeIncrementalHandleCreate(
        void* UserState,
        MIDL_ES_READ ReadFn,
        handle_t* pHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UserState", "ReadFn", "pHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_MesEncodeDynBufferHandleCreate(jitter):
    """
    RPC_STATUS MesEncodeDynBufferHandleCreate(
        char** ppBuffer,
        unsigned long* pEncodedSize,
        handle_t* pHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppBuffer", "pEncodedSize", "pHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_MesEncodeFixedBufferHandleCreate(jitter):
    """
    RPC_STATUS MesEncodeFixedBufferHandleCreate(
        [LPVOID|char*] Buffer,
        unsigned long BufferSize,
        unsigned long* pEncodedSize,
        handle_t* pHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "BufferSize", "pEncodedSize", "pHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_MesEncodeIncrementalHandleCreate(jitter):
    """
    RPC_STATUS MesEncodeIncrementalHandleCreate(
        void* UserState,
        MIDL_ES_ALLOC AllocFn,
        MIDL_ES_WRITE WriteFn,
        handle_t* pHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UserState", "AllocFn", "WriteFn", "pHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_MesHandleFree(jitter):
    """
    RPC_STATUS MesHandleFree(
        handle_t Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_MesIncrementalHandleReset(jitter):
    """
    RPC_STATUS MesIncrementalHandleReset(
        handle_t Handle,
        void* UserState,
        MIDL_ES_ALLOC AllocFn,
        MIDL_ES_WRITE WriteFn,
        MIDL_ES_READ ReadFn,
        MIDL_ES_CODE OpCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "UserState", "AllocFn", "WriteFn", "ReadFn", "OpCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_MesInqProcEncodingId(jitter):
    """
    RPC_STATUS MesInqProcEncodingId(
        handle_t Handle,
        PRPC_SYNTAX_IDENTIFIER pInterfaceId,
        unsigned long* pProcNum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pInterfaceId", "pProcNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcAsyncAbortCall(jitter):
    """
    RPC_STATUS RpcAsyncAbortCall(
        PRPC_ASYNC_STATE pAsync,
        unsigned long ExceptionCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAsync", "ExceptionCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcAsyncCancelCall(jitter):
    """
    RPC_STATUS RpcAsyncCancelCall(
        PRPC_ASYNC_STATE pAsync,
        BOOL fAbortCall
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAsync", "fAbortCall"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcAsyncCompleteCall(jitter):
    """
    RPC_STATUS RpcAsyncCompleteCall(
        PRPC_ASYNC_STATE pAsync,
        PVOID Reply
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAsync", "Reply"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcAsyncGetCallStatus(jitter):
    """
    RPC_STATUS RpcAsyncGetCallStatus(
        PRPC_ASYNC_STATE pAsync
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAsync"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcAsyncInitializeHandle(jitter):
    """
    RPC_STATUS RpcAsyncInitializeHandle(
        PRPC_ASYNC_STATE pAsync,
        unsigned int Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAsync", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcAsyncRegisterInfo(jitter):
    """
    void RpcAsyncRegisterInfo()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingBind(jitter):
    """
    RPC_STATUS RpcBindingBind(
        PRPC_ASYNC_STATE pAsync,
        RPC_BINDING_HANDLE Binding,
        RPC_IF_HANDLE IfSpec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAsync", "Binding", "IfSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingCopy(jitter):
    """
    RPC_STATUS RpcBindingCopy(
        RPC_BINDING_HANDLE SourceBinding,
        RPC_BINDING_HANDLE* DestinationBinding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceBinding", "DestinationBinding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingCreate(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingCreate(
        RPC_BINDING_HANDLE_TEMPLATE_V1* Template,
        RPC_BINDING_HANDLE_SECURITY_V1* Security,
        RPC_BINDING_HANDLE_OPTIONS_V1* Options,
        RPC_BINDING_HANDLE* Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Template", "Security", "Options", "Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingCreateA(jitter):
    rpcrt4_RpcBindingCreate(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingCreateW(jitter):
    rpcrt4_RpcBindingCreate(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingFree(jitter):
    """
    RPC_STATUS RpcBindingFree(
        RPC_BINDING_HANDLE* Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingFromStringBinding(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingFromStringBinding(
        RPC_TSTR StringBinding,
        RPC_BINDING_HANDLE* Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StringBinding", "Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingFromStringBindingA(jitter):
    rpcrt4_RpcBindingFromStringBinding(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingFromStringBindingW(jitter):
    rpcrt4_RpcBindingFromStringBinding(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingInqAuthClient(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingInqAuthClient(
        RPC_BINDING_HANDLE ClientBinding,
        RPC_AUTHZ_HANDLE* Privs,
        RPC_TSTR* ServerPrincName,
        [RPC_C_AUTHN_LEVEL*] AuthnLevel,
        [RPC_C_AUTHN_SVC*] AuthnSvc,
        [RPC_C_AUTHZ*] AuthzSvc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientBinding", "Privs", "ServerPrincName", "AuthnLevel", "AuthnSvc", "AuthzSvc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingInqAuthClientA(jitter):
    rpcrt4_RpcBindingInqAuthClient(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingInqAuthClientW(jitter):
    rpcrt4_RpcBindingInqAuthClient(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingInqAuthClientEx(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingInqAuthClientEx(
        RPC_BINDING_HANDLE ClientBinding,
        RPC_AUTHZ_HANDLE* Privs,
        RPC_TSTR* ServerPrincName,
        [RPC_C_AUTHN_LEVEL*] AuthnLevel,
        [RPC_C_AUTHN_SVC*] AuthnSvc,
        [RPC_C_AUTHZ*] AuthzSvc,
        unsigned long flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientBinding", "Privs", "ServerPrincName", "AuthnLevel", "AuthnSvc", "AuthzSvc", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingInqAuthClientExA(jitter):
    rpcrt4_RpcBindingInqAuthClientEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingInqAuthClientExW(jitter):
    rpcrt4_RpcBindingInqAuthClientEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingInqAuthInfo(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingInqAuthInfo(
        RPC_BINDING_HANDLE Binding,
        RPC_TSTR* ServerPrincName,
        [RPC_C_AUTHN_LEVEL*] AuthnLevel,
        [RPC_C_AUTHN_SVC*] AuthnSvc,
        RPC_AUTH_IDENTITY_HANDLE* AuthIdentity,
        [RPC_C_AUTHZ*] AuthzSvc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "ServerPrincName", "AuthnLevel", "AuthnSvc", "AuthIdentity", "AuthzSvc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingInqAuthInfoA(jitter):
    rpcrt4_RpcBindingInqAuthInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingInqAuthInfoW(jitter):
    rpcrt4_RpcBindingInqAuthInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingInqAuthInfoEx(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingInqAuthInfoEx(
        RPC_BINDING_HANDLE Binding,
        RPC_TSTR ServerPrincName,
        [RPC_C_AUTHN_LEVEL*] AuthnLevel,
        [RPC_C_AUTHN_SVC*] AuthnSvc,
        RPC_AUTH_IDENTITY_HANDLE* AuthIdentity,
        [RPC_C_AUTHZ*] AuthzSvc,
        unsigned long RpcQosVersion,
        RPC_SECURITY_QOS* SecurityQos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "ServerPrincName", "AuthnLevel", "AuthnSvc", "AuthIdentity", "AuthzSvc", "RpcQosVersion", "SecurityQos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingInqAuthInfoExA(jitter):
    rpcrt4_RpcBindingInqAuthInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingInqAuthInfoExW(jitter):
    rpcrt4_RpcBindingInqAuthInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingInqObject(jitter):
    """
    RPC_STATUS RpcBindingInqObject(
        RPC_BINDING_HANDLE Binding,
        UUID* ObjectUuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "ObjectUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingInqOption(jitter):
    """
    RPC_STATUS RpcBindingInqOption(
        RPC_BINDING_HANDLE hBinding,
        unsigned long Option,
        unsigned long* pOptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBinding", "Option", "pOptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingReset(jitter):
    """
    RPC_STATUS RpcBindingReset(
        RPC_BINDING_HANDLE Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingServerFromClient(jitter):
    """
    RPC_STATUS RpcBindingServerFromClient(
        RPC_BINDING_HANDLE ClientBinding,
        RPC_BINDING_HANDLE* ServerBinding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientBinding", "ServerBinding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingSetAuthInfo(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingSetAuthInfo(
        RPC_BINDING_HANDLE Binding,
        RPC_TSTR ServerPrincName,
        [RPC_C_AUTHN_LEVEL] AuthnLevel,
        [RPC_C_AUTHN_SVC] AuthnSvc,
        RPC_AUTH_IDENTITY_HANDLE AuthIdentity,
        unsigned long AuthzService
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "ServerPrincName", "AuthnLevel", "AuthnSvc", "AuthIdentity", "AuthzService"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingSetAuthInfoA(jitter):
    rpcrt4_RpcBindingSetAuthInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingSetAuthInfoW(jitter):
    rpcrt4_RpcBindingSetAuthInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingSetAuthInfoEx(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingSetAuthInfoEx(
        RPC_BINDING_HANDLE Binding,
        RPC_TSTR ServerPrincName,
        [RPC_C_AUTHN_LEVEL] AuthnLevel,
        [RPC_C_AUTHN_SVC] AuthnSvc,
        RPC_AUTH_IDENTITY_HANDLE AuthIdentity,
        [RPC_C_AUTHZ] AuthzSvc,
        RPC_SECURITY_QOS* SecurityQOS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "ServerPrincName", "AuthnLevel", "AuthnSvc", "AuthIdentity", "AuthzSvc", "SecurityQOS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingSetAuthInfoExA(jitter):
    rpcrt4_RpcBindingSetAuthInfoEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingSetAuthInfoExW(jitter):
    rpcrt4_RpcBindingSetAuthInfoEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingSetObject(jitter):
    """
    RPC_STATUS RpcBindingSetObject(
        RPC_BINDING_HANDLE Binding,
        UUID* ObjectUuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "ObjectUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingSetOption(jitter):
    """
    RPC_STATUS RpcBindingSetOption(
        RPC_BINDING_HANDLE hBinding,
        [BindingOptions] Option,
        unsigned long OptionValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hBinding", "Option", "OptionValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingToStringBinding(jitter, get_str, set_str):
    """
    RPC_STATUS RpcBindingToStringBinding(
        RPC_BINDING_HANDLE Binding,
        RPC_TSTR* StringBinding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "StringBinding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingToStringBindingA(jitter):
    rpcrt4_RpcBindingToStringBinding(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcBindingToStringBindingW(jitter):
    rpcrt4_RpcBindingToStringBinding(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcBindingUnbind(jitter):
    """
    RPC_STATUS RpcBindingUnbind(
        RPC_BINDING_HANDLE Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcBindingVectorFree(jitter):
    """
    RPC_STATUS RpcBindingVectorFree(
        RPC_BINDING_VECTOR** BindingVector
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingVector"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcCancelThread(jitter):
    """
    RPC_STATUS RpcCancelThread(
        HANDLE ThreadHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcCancelThreadEx(jitter):
    """
    RPC_STATUS RpcCancelThreadEx(
        HANDLE ThreadHandle,
        LONG Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadHandle", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcCertGeneratePrincipalName(jitter, get_str, set_str):
    """
    void RpcCertGeneratePrincipalName(
        PCCERT_CONTEXT Context,
        DWORD Flags,
        UCHAR** pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context", "Flags", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcCertGeneratePrincipalNameA(jitter):
    rpcrt4_RpcCertGeneratePrincipalName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcCertGeneratePrincipalNameW(jitter):
    rpcrt4_RpcCertGeneratePrincipalName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcEpRegister(jitter, get_str, set_str):
    """
    RPC_STATUS RpcEpRegister(
        RPC_IF_HANDLE IfSpec,
        RPC_BINDING_VECTOR* BindingVector,
        UUID_VECTOR* UuidVector,
        RPC_TSTR Annotation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "BindingVector", "UuidVector", "Annotation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcEpRegisterA(jitter):
    rpcrt4_RpcEpRegister(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcEpRegisterW(jitter):
    rpcrt4_RpcEpRegister(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcEpRegisterNoReplace(jitter, get_str, set_str):
    """
    RPC_STATUS RpcEpRegisterNoReplace(
        RPC_IF_HANDLE IfSpec,
        RPC_BINDING_VECTOR* BindingVector,
        UUID_VECTOR* UuidVector,
        RPC_TSTR Annotation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "BindingVector", "UuidVector", "Annotation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcEpRegisterNoReplaceA(jitter):
    rpcrt4_RpcEpRegisterNoReplace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcEpRegisterNoReplaceW(jitter):
    rpcrt4_RpcEpRegisterNoReplace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcEpResolveBinding(jitter):
    """
    RPC_STATUS RpcEpResolveBinding(
        RPC_BINDING_HANDLE Binding,
        RPC_IF_HANDLE IfSpec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "IfSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcEpUnregister(jitter):
    """
    RPC_STATUS RpcEpUnregister(
        RPC_IF_HANDLE IfSpec,
        RPC_BINDING_VECTOR* BindingVector,
        UUID_VECTOR* UuidVector
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "BindingVector", "UuidVector"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorAddRecord(jitter):
    """
    RPC_STATUS RpcErrorAddRecord(
        RPC_EXTENDED_ERROR_INFO* ErrorInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ErrorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorClearInformation(jitter):
    """
    void RpcErrorClearInformation()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorEndEnumeration(jitter):
    """
    RPC_STATUS RpcErrorEndEnumeration(
        RPC_ERROR_ENUM_HANDLE* EnumHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnumHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorGetNextRecord(jitter):
    """
    RPC_STATUS RpcErrorGetNextRecord(
        RPC_ERROR_ENUM_HANDLE* EnumHandle,
        BOOL CopyStrings,
        RPC_EXTENDED_ERROR_INFO* ErrorInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnumHandle", "CopyStrings", "ErrorInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorGetNumberOfRecords(jitter):
    """
    RPC_STATUS RpcErrorGetNumberOfRecords(
        RPC_ERROR_ENUM_HANDLE* EnumHandle,
        int* Records
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnumHandle", "Records"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorLoadErrorInfo(jitter):
    """
    RPC_STATUS RpcErrorLoadErrorInfo(
        PVOID ErrorBlob,
        size_t BlobSize,
        RPC_ERROR_ENUM_HANDLE* EnumHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ErrorBlob", "BlobSize", "EnumHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorResetEnumeration(jitter):
    """
    RPC_STATUS RpcErrorResetEnumeration(
        RPC_ERROR_ENUM_HANDLE* EnumHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnumHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorSaveErrorInfo(jitter):
    """
    RPC_STATUS RpcErrorSaveErrorInfo(
        RPC_ERROR_ENUM_HANDLE* EnumHandle,
        PVOID* ErrorBlob,
        size_t* BlobSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnumHandle", "ErrorBlob", "BlobSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcErrorStartEnumeration(jitter):
    """
    RPC_STATUS RpcErrorStartEnumeration(
        RPC_ERROR_ENUM_HANDLE* EnumHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EnumHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcIfIdVectorFree(jitter):
    """
    RPC_STATUS RpcIfIdVectorFree(
        RPC_IF_ID_VECTOR** IfIdVec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfIdVec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcIfInqId(jitter):
    """
    RPC_STATUS RpcIfInqId(
        RPC_IF_HANDLE RpcIfHandle,
        RPC_IF_ID* RpcIfId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RpcIfHandle", "RpcIfId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcImpersonateClient(jitter):
    """
    RPC_STATUS RpcImpersonateClient(
        RPC_BINDING_HANDLE BindingHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtEnableIdleCleanup(jitter):
    """
    RPC_STATUS RpcMgmtEnableIdleCleanup()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtEpEltInqBegin(jitter):
    """
    RPC_STATUS RpcMgmtEpEltInqBegin(
        RPC_BINDING_HANDLE EpBinding,
        unsigned long InquiryType,
        RPC_IF_ID* IfId,
        unsigned long VersOption,
        UUID* ObjectUuid,
        RPC_EP_INQ_HANDLE* InquiryContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EpBinding", "InquiryType", "IfId", "VersOption", "ObjectUuid", "InquiryContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtEpEltInqDone(jitter):
    """
    RPC_STATUS RpcMgmtEpEltInqDone(
        RPC_EP_INQ_HANDLE* InquiryContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtEpEltInqNext(jitter, get_str, set_str):
    """
    RPC_STATUS RpcMgmtEpEltInqNext(
        RPC_EP_INQ_HANDLE InquiryContext,
        RPC_IF_ID* IfId,
        RPC_BINDING_HANDLE* Binding,
        UUID* ObjectUuid,
        RPC_TSTR* Annotation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryContext", "IfId", "Binding", "ObjectUuid", "Annotation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtEpEltInqNextA(jitter):
    rpcrt4_RpcMgmtEpEltInqNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcMgmtEpEltInqNextW(jitter):
    rpcrt4_RpcMgmtEpEltInqNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcMgmtEpUnregister(jitter):
    """
    RPC_STATUS RpcMgmtEpUnregister(
        RPC_BINDING_HANDLE EpBinding,
        RPC_IF_ID* IfId,
        RPC_BINDING_HANDLE Binding,
        UUID* ObjectUuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EpBinding", "IfId", "Binding", "ObjectUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtInqComTimeout(jitter):
    """
    RPC_STATUS RpcMgmtInqComTimeout(
        RPC_BINDING_HANDLE Binding,
        unsigned int* Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtInqDefaultProtectLevel(jitter):
    """
    RPC_STATUS RpcMgmtInqDefaultProtectLevel(
        [RPC_C_AUTHN_SVC] AuthnSvc,
        [RPC_C_AUTHN_LEVEL-unsigned-int*] AuthnLevel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthnSvc", "AuthnLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtInqIfIds(jitter):
    """
    RPC_STATUS RpcMgmtInqIfIds(
        RPC_BINDING_HANDLE Binding,
        RPC_IF_ID_VECTOR** IfIdVector
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "IfIdVector"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtInqServerPrincName(jitter, get_str, set_str):
    """
    RPC_STATUS RpcMgmtInqServerPrincName(
        RPC_BINDING_HANDLE Binding,
        [RPC_C_AUTHN_SVC] AuthnSvc,
        RPC_TSTR* ServerPrincName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "AuthnSvc", "ServerPrincName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtInqServerPrincNameA(jitter):
    rpcrt4_RpcMgmtInqServerPrincName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcMgmtInqServerPrincNameW(jitter):
    rpcrt4_RpcMgmtInqServerPrincName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcMgmtInqStats(jitter):
    """
    RPC_STATUS RpcMgmtInqStats(
        RPC_BINDING_HANDLE Binding,
        RPC_STATS_VECTOR** Statistics
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Statistics"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtIsServerListening(jitter):
    """
    RPC_STATUS RpcMgmtIsServerListening(
        RPC_BINDING_HANDLE Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtSetAuthorizationFn(jitter):
    """
    RPC_STATUS RpcMgmtSetAuthorizationFn(
        RPC_MGMT_AUTHORIZATION_FN AuthorizationFn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthorizationFn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtSetCancelTimeout(jitter):
    """
    RPC_STATUS RpcMgmtSetCancelTimeout(
        signed int Seconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Seconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtSetComTimeout(jitter):
    """
    RPC_STATUS RpcMgmtSetComTimeout(
        RPC_BINDING_HANDLE Binding,
        unsigned int Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtSetServerStackSize(jitter):
    """
    RPC_STATUS RpcMgmtSetServerStackSize(
        unsigned int ThreadStackSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ThreadStackSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtStatsVectorFree(jitter):
    """
    RPC_STATUS RpcMgmtStatsVectorFree(
        RPC_STATS_VECTOR** StatsVector
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StatsVector"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtStopServerListening(jitter):
    """
    RPC_STATUS RpcMgmtStopServerListening(
        RPC_BINDING_HANDLE Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcMgmtWaitServerListen(jitter):
    """
    RPC_STATUS RpcMgmtWaitServerListen()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcNetworkInqProtseqs(jitter, get_str, set_str):
    """
    RPC_STATUS RpcNetworkInqProtseqs(
        RPC_PROTSEQ_VECTOR** ProtSeqVector
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProtSeqVector"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcNetworkInqProtseqsA(jitter):
    rpcrt4_RpcNetworkInqProtseqs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcNetworkInqProtseqsW(jitter):
    rpcrt4_RpcNetworkInqProtseqs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcNetworkIsProtseqValid(jitter, get_str, set_str):
    """
    RPC_STATUS RpcNetworkIsProtseqValid(
        RPC_TSTR Protseq
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Protseq"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcNetworkIsProtseqValidA(jitter):
    rpcrt4_RpcNetworkIsProtseqValid(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcNetworkIsProtseqValidW(jitter):
    rpcrt4_RpcNetworkIsProtseqValid(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcNsBindingInqEntryName(jitter, get_str, set_str):
    """
    RPC_STATUS RpcNsBindingInqEntryName(
        RPC_BINDING_HANDLE Binding,
        unsigned long EntryNameSyntax,
        RPC_TSTR* EntryName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "EntryNameSyntax", "EntryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcNsBindingInqEntryNameA(jitter):
    rpcrt4_RpcNsBindingInqEntryName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcNsBindingInqEntryNameW(jitter):
    rpcrt4_RpcNsBindingInqEntryName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcObjectInqType(jitter):
    """
    RPC_STATUS RpcObjectInqType(
        UUID* ObjUuid,
        UUID* TypeUuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjUuid", "TypeUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcObjectSetInqFn(jitter):
    """
    RPC_STATUS RpcObjectSetInqFn(
        RPC_OBJECT_INQ_FN InquiryFn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InquiryFn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcObjectSetType(jitter):
    """
    RPC_STATUS RpcObjectSetType(
        UUID* ObjUuid,
        UUID* TypeUuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjUuid", "TypeUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcProtseqVectorFree(jitter, get_str, set_str):
    """
    RPC_STATUS RpcProtseqVectorFree(
        RPC_PROTSEQ_VECTOR** ProtSeqVector
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProtSeqVector"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcProtseqVectorFreeA(jitter):
    rpcrt4_RpcProtseqVectorFree(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcProtseqVectorFreeW(jitter):
    rpcrt4_RpcProtseqVectorFree(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcRevertToSelf(jitter):
    """
    RPC_STATUS RpcRevertToSelf()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcRevertToSelfEx(jitter):
    """
    RPC_STATUS RpcRevertToSelfEx(
        RPC_BINDING_HANDLE BindingHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInqBindings(jitter):
    """
    RPC_STATUS RpcServerInqBindings(
        RPC_BINDING_VECTOR** BindingVector
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingVector"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInqCallAttributes(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerInqCallAttributes(
        RPC_BINDING_HANDLE ClientBinding,
        void* RpcCallAttributes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientBinding", "RpcCallAttributes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInqCallAttributesA(jitter):
    rpcrt4_RpcServerInqCallAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerInqCallAttributesW(jitter):
    rpcrt4_RpcServerInqCallAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerInqDefaultPrincName(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerInqDefaultPrincName(
        [RPC_C_AUTHN_SVC] AuthnSvc,
        RPC_TSTR* PrincName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthnSvc", "PrincName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInqDefaultPrincNameA(jitter):
    rpcrt4_RpcServerInqDefaultPrincName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerInqDefaultPrincNameW(jitter):
    rpcrt4_RpcServerInqDefaultPrincName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerInqBindingHandle(jitter):
    """
    RPC_STATUS RpcServerInqBindingHandle(
        RPC_BINDING_HANDLE* Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInqIf(jitter):
    """
    RPC_STATUS RpcServerInqIf(
        RPC_IF_HANDLE IfSpec,
        UUID* MgrTypeUuid,
        RPC_MGR_EPV** MgrEpv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "MgrTypeUuid", "MgrEpv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerListen(jitter):
    """
    RPC_STATUS RpcServerListen(
        unsigned int MinimumCallThreads,
        unsigned int MaxCalls,
        unsigned int DontWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MinimumCallThreads", "MaxCalls", "DontWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerRegisterAuthInfo(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerRegisterAuthInfo(
        RPC_TSTR ServerPrincName,
        [RPC_C_AUTHN_SVC] AuthnSvc,
        RPC_AUTH_KEY_RETRIEVAL_FN GetKeyFn,
        void* Arg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerPrincName", "AuthnSvc", "GetKeyFn", "Arg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerRegisterAuthInfoA(jitter):
    rpcrt4_RpcServerRegisterAuthInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerRegisterAuthInfoW(jitter):
    rpcrt4_RpcServerRegisterAuthInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerRegisterIf(jitter):
    """
    RPC_STATUS RpcServerRegisterIf(
        RPC_IF_HANDLE IfSpec,
        UUID* MgrTypeUuid,
        RPC_MGR_EPV* MgrEpv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "MgrTypeUuid", "MgrEpv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerRegisterIf2(jitter):
    """
    RPC_STATUS RpcServerRegisterIf2(
        RPC_IF_HANDLE IfSpec,
        UUID* MgrTypeUuid,
        RPC_MGR_EPV* MgrEpv,
        [InterfaceRegistrationFlags] Flags,
        unsigned int MaxCalls,
        unsigned int MaxRpcSize,
        RPC_IF_CALLBACK_FN* IfCallbackFn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "MgrTypeUuid", "MgrEpv", "Flags", "MaxCalls", "MaxRpcSize", "IfCallbackFn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerRegisterIfEx(jitter):
    """
    RPC_STATUS RpcServerRegisterIfEx(
        RPC_IF_HANDLE IfSpec,
        UUID* MgrTypeUuid,
        RPC_MGR_EPV* MgrEpv,
        [InterfaceRegistrationFlags] Flags,
        unsigned int MaxCalls,
        RPC_IF_CALLBACK_FN* IfCallback
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "MgrTypeUuid", "MgrEpv", "Flags", "MaxCalls", "IfCallback"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerSubscribeForNotification(jitter):
    """
    RPC_STATUS RpcServerSubscribeForNotification(
        RPC_BINDING_HANDLE Binding,
        RPC_NOTIFICATIONS Notification,
        RPC_NOTIFICATION_TYPES NotificationType,
        RPC_ASYNC_NOTIFICATION_INFO* NotificationInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Notification", "NotificationType", "NotificationInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerTestCancel(jitter):
    """
    RPC_STATUS RpcServerTestCancel(
        RPC_BINDING_HANDLE BindingHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUnregisterIf(jitter):
    """
    RPC_STATUS RpcServerUnregisterIf(
        RPC_IF_HANDLE IfSpec,
        UUID* MgrTypeUuid,
        unsigned int WaitForCallsToComplete
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "MgrTypeUuid", "WaitForCallsToComplete"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUnregisterIfEx(jitter):
    """
    RPC_STATUS RpcServerUnregisterIfEx(
        RPC_IF_HANDLE IfSpec,
        UUID* MgrTypeUuid,
        int RundownContextHandles
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "MgrTypeUuid", "RundownContextHandles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUnsubscribeForNotification(jitter):
    """
    RPC_STATUS RpcServerUnsubscribeForNotification(
        RPC_BINDING_HANDLE Binding,
        RPC_NOTIFICATIONS Notification,
        unsigned long* NotificationsQueued
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Notification", "NotificationsQueued"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseAllProtseqs(jitter):
    """
    RPC_STATUS RpcServerUseAllProtseqs(
        unsigned int MaxCalls,
        void* SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MaxCalls", "SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseAllProtseqsEx(jitter):
    """
    RPC_STATUS RpcServerUseAllProtseqsEx(
        unsigned int MaxCalls,
        void* SecurityDescriptor,
        PRPC_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MaxCalls", "SecurityDescriptor", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseAllProtseqsIf(jitter):
    """
    RPC_STATUS RpcServerUseAllProtseqsIf(
        unsigned int MaxCalls,
        RPC_IF_HANDLE IfSpec,
        void* SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MaxCalls", "IfSpec", "SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseAllProtseqsIfEx(jitter):
    """
    RPC_STATUS RpcServerUseAllProtseqsIfEx(
        unsigned int MaxCalls,
        RPC_IF_HANDLE IfSpec,
        void* SecurityDescriptor,
        PRPC_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MaxCalls", "IfSpec", "SecurityDescriptor", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseProtseq(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerUseProtseq(
        RPC_TSTR ProtSeq,
        unsigned int MaxCalls,
        void* SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProtSeq", "MaxCalls", "SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseProtseqA(jitter):
    rpcrt4_RpcServerUseProtseq(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqW(jitter):
    rpcrt4_RpcServerUseProtseq(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqEx(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerUseProtseqEx(
        RPC_TSTR ProtSeq,
        unsigned int MaxCalls,
        void* SecurityDescriptor,
        PRPC_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProtSeq", "MaxCalls", "SecurityDescriptor", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseProtseqExA(jitter):
    rpcrt4_RpcServerUseProtseqEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqExW(jitter):
    rpcrt4_RpcServerUseProtseqEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqEp(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerUseProtseqEp(
        RPC_TSTR Protseq,
        unsigned int MaxCalls,
        RPC_TSTR Endpoint,
        void* SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Protseq", "MaxCalls", "Endpoint", "SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseProtseqEpA(jitter):
    rpcrt4_RpcServerUseProtseqEp(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqEpW(jitter):
    rpcrt4_RpcServerUseProtseqEp(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqEpEx(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerUseProtseqEpEx(
        RPC_TSTR Protseq,
        unsigned int MaxCalls,
        RPC_TSTR Endpoint,
        void* SecurityDescriptor,
        PRPC_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Protseq", "MaxCalls", "Endpoint", "SecurityDescriptor", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseProtseqEpExA(jitter):
    rpcrt4_RpcServerUseProtseqEpEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqEpExW(jitter):
    rpcrt4_RpcServerUseProtseqEpEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqIf(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerUseProtseqIf(
        RPC_TSTR Protseq,
        unsigned int MaxCalls,
        RPC_IF_HANDLE IfSpec,
        void* SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Protseq", "MaxCalls", "IfSpec", "SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseProtseqIfA(jitter):
    rpcrt4_RpcServerUseProtseqIf(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqIfW(jitter):
    rpcrt4_RpcServerUseProtseqIf(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqIfEx(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerUseProtseqIfEx(
        RPC_TSTR Protseq,
        unsigned int MaxCalls,
        RPC_IF_HANDLE IfSpec,
        void* SecurityDescriptor,
        PRPC_POLICY Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Protseq", "MaxCalls", "IfSpec", "SecurityDescriptor", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerUseProtseqIfExA(jitter):
    rpcrt4_RpcServerUseProtseqIfEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerUseProtseqIfExW(jitter):
    rpcrt4_RpcServerUseProtseqIfEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcSmAllocate(jitter):
    """
    void* RpcSmAllocate(
        size_t Size,
        RPC_STATUS* pStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Size", "pStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmClientFree(jitter):
    """
    RPC_STATUS RpcSmClientFree(
        void* NodeToFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NodeToFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmDestroyClientContext(jitter):
    """
    RPC_STATUS RpcSmDestroyClientContext(
        void** ContextHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmDisableAllocate(jitter):
    """
    RPC_STATUS RpcSmDisableAllocate()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmEnableAllocate(jitter):
    """
    RPC_STATUS RpcSmEnableAllocate()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmFree(jitter):
    """
    RPC_STATUS RpcSmFree(
        void* NodeToFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NodeToFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmGetThreadHandle(jitter):
    """
    RPC_SS_THREAD_HANDLE RpcSmGetThreadHandle(
        RPC_STATUS* pStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmSetClientAllocFree(jitter):
    """
    RPC_STATUS RpcSmSetClientAllocFree(
        RPC_CLIENT_ALLOC* pfnAllocate,
        RPC_CLIENT_FREE* pfnFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfnAllocate", "pfnFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmSetThreadHandle(jitter):
    """
    RPC_STATUS RpcSmSetThreadHandle(
        RPC_SS_THREAD_HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSmSwapClientAllocFree(jitter):
    """
    RPC_STATUS RpcSmSwapClientAllocFree(
        RPC_CLIENT_ALLOC* pfnAllocate,
        RPC_CLIENT_FREE* pfnFree,
        RPC_CLIENT_ALLOC** pfnOldAllocate,
        RPC_CLIENT_FREE** pfnOldFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfnAllocate", "pfnFree", "pfnOldAllocate", "pfnOldFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsAllocate(jitter):
    """
    void* RpcSsAllocate(
        size_t Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsContextLockExclusive(jitter):
    """
    RPC_STATUS RpcSsContextLockExclusive(
        RPC_BINDING_HANDLE ServerBindingHandle,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerBindingHandle", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsContextLockShared(jitter):
    """
    RPC_STATUS RpcSsContextLockShared(
        RPC_BINDING_HANDLE ServerBindingHandle,
        PVOID UserContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerBindingHandle", "UserContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsDestroyClientContext(jitter):
    """
    void RpcSsDestroyClientContext(
        void** ContextHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsDisableAllocate(jitter):
    """
    void RpcSsDisableAllocate()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsDontSerializeContext(jitter):
    """
    void RpcSsDontSerializeContext()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsEnableAllocate(jitter):
    """
    void RpcSsEnableAllocate()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsFree(jitter):
    """
    void RpcSsFree(
        void* NodeToFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NodeToFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsGetThreadHandle(jitter):
    """
    RPC_SS_THREAD_HANDLE RpcSsGetThreadHandle()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsSetClientAllocFree(jitter):
    """
    void RpcSsSetClientAllocFree(
        RPC_CLIENT_ALLOC* pfnAllocate,
        RPC_CLIENT_FREE* pfnFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfnAllocate", "pfnFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsSetThreadHandle(jitter):
    """
    void RpcSsSetThreadHandle(
        RPC_SS_THREAD_HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsSwapClientAllocFree(jitter):
    """
    void RpcSsSwapClientAllocFree(
        RPC_CLIENT_ALLOC* pfnAllocate,
        RPC_CLIENT_FREE* pfnFree,
        RPC_CLIENT_ALLOC** pfnOldAllocate,
        RPC_CLIENT_FREE** pfnOldFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfnAllocate", "pfnFree", "pfnOldAllocate", "pfnOldFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcStringBindingCompose(jitter, get_str, set_str):
    """
    RPC_STATUS RpcStringBindingCompose(
        TCHAR* ObjUuid,
        TCHAR* ProtSeq,
        TCHAR* NetworkAddr,
        TCHAR* EndPoint,
        TCHAR* Options,
        TCHAR** StringBinding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjUuid", "ProtSeq", "NetworkAddr", "EndPoint", "Options", "StringBinding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcStringBindingComposeA(jitter):
    rpcrt4_RpcStringBindingCompose(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcStringBindingComposeW(jitter):
    rpcrt4_RpcStringBindingCompose(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcStringBindingParse(jitter, get_str, set_str):
    """
    RPC_STATUS RpcStringBindingParse(
        TCHAR* StringBinding,
        TCHAR** ObjectUuid,
        TCHAR** ProtSeq,
        TCHAR** NetworkAddr,
        TCHAR** EndPoint,
        TCHAR** NetworkOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StringBinding", "ObjectUuid", "ProtSeq", "NetworkAddr", "EndPoint", "NetworkOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcStringBindingParseA(jitter):
    rpcrt4_RpcStringBindingParse(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcStringBindingParseW(jitter):
    rpcrt4_RpcStringBindingParse(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcStringFree(jitter, get_str, set_str):
    """
    RPC_STATUS RpcStringFree(
        RPC_TSTR* String
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["String"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcStringFreeA(jitter):
    rpcrt4_RpcStringFree(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcStringFreeW(jitter):
    rpcrt4_RpcStringFree(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcTestCancel(jitter):
    """
    RPC_STATUS RpcTestCancel()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingInqLocalClientPID(jitter):
    """
    RPC_STATUS I_RpcBindingInqLocalClientPID(
        RPC_BINDING_HANDLE Binding,
        unsigned long* Pid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Pid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcFreeAuthorizationContext(jitter):
    """
    RPC_STATUS RpcFreeAuthorizationContext(
        PVOID* pAuthzClientContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAuthzClientContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcGetAuthorizationContextForClient(jitter):
    """
    RPC_STATUS RpcGetAuthorizationContextForClient(
        RPC_BINDING_HANDLE ClientBinding,
        BOOL ImpersonateOnReturn,
        PVOID Reserved1,
        PLARGE_INTEGER pExpirationTime,
        LUID Reserved2,
        DWORD Reserved3,
        PVOID Reserved4,
        PVOID* pAuthzClientContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientBinding", "ImpersonateOnReturn", "Reserved1", "pExpirationTime", "Reserved2", "Reserved3", "Reserved4", "pAuthzClientContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInterfaceGroupActivate(jitter):
    """
    RPC_STATUS RpcServerInterfaceGroupActivate(
        RPC_INTERFACE_GROUP IfGroup
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfGroup"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInterfaceGroupClose(jitter):
    """
    RPC_STATUS RpcServerInterfaceGroupClose(
        RPC_INTERFACE_GROUP IfGroup
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfGroup"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInterfaceGroupCreate(jitter, get_str, set_str):
    """
    RPC_STATUS RpcServerInterfaceGroupCreate(
        RPC_INTERFACE_TEMPLATE* Interfaces,
        unsigned long NumIfs,
        RPC_ENDPOINT_TEMPLATE* Endpoints,
        unsigned long NumEndpoints,
        unsigned long IdlePeriod,
        RPC_INTERFACE_GROUP_IDLE_CALLBACK_FN IdleCallbackFn,
        void* IdleCallbackContext,
        PRPC_INTERFACE_GROUP IfGroup
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Interfaces", "NumIfs", "Endpoints", "NumEndpoints", "IdlePeriod", "IdleCallbackFn", "IdleCallbackContext", "IfGroup"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInterfaceGroupCreateA(jitter):
    rpcrt4_RpcServerInterfaceGroupCreate(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_RpcServerInterfaceGroupCreateW(jitter):
    rpcrt4_RpcServerInterfaceGroupCreate(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_RpcServerInterfaceGroupDeactivate(jitter):
    """
    RPC_STATUS RpcServerInterfaceGroupDeactivate(
        RPC_INTERFACE_GROUP IfGroup,
        unsigned long ForceDeactivation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfGroup", "ForceDeactivation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerInterfaceGroupInqBindings(jitter):
    """
    RPC_STATUS RpcServerInterfaceGroupInqBindings(
        RPC_INTERFACE_GROUP IfGroup,
        RPC_BINDING_VECTOR** BindingVector
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfGroup", "BindingVector"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerRegisterIf3(jitter):
    """
    RPC_STATUS RpcServerRegisterIf3(
        RPC_IF_HANDLE IfSpec,
        UUID* MgrTypeUuid,
        RPC_MGR_EPV* MgrEpv,
        [InterfaceRegistrationFlags] Flags,
        unsigned int MaxCalls,
        unsigned int MaxRpcSize,
        RPC_IF_CALLBACK_FN* IfCallback,
        void* SecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfSpec", "MgrTypeUuid", "MgrEpv", "Flags", "MaxCalls", "MaxRpcSize", "IfCallback", "SecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcAllocate(jitter):
    """
    void* I_RpcAllocate(
        unsigned int Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcAsyncAbortCall(jitter):
    """
    RPC_STATUS I_RpcAsyncAbortCall(
        PRPC_ASYNC_STATE pAsync,
        unsigned long ExceptionCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAsync", "ExceptionCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcAsyncSetHandle(jitter):
    """
    RPC_STATUS I_RpcAsyncSetHandle(
        PRPC_MESSAGE Message,
        PRPC_ASYNC_STATE pAsync
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message", "pAsync"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingCopy(jitter):
    """
    RPC_STATUS I_RpcBindingCopy(
        RPC_BINDING_HANDLE SourceBinding,
        RPC_BINDING_HANDLE* DestinationBinding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceBinding", "DestinationBinding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingCreateNP(jitter):
    """
    RPC_STATUS I_RpcBindingCreateNP(
        RPC_WSTR ServerName,
        RPC_WSTR ServiceName,
        RPC_WSTR NetworkOptions,
        RPC_BINDING_HANDLE* Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "ServiceName", "NetworkOptions", "Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingHandleToAsyncHandle(jitter):
    """
    RPC_STATUS I_RpcBindingHandleToAsyncHandle(
        RPC_BINDING_HANDLE Binding,
        void** AsyncHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "AsyncHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingInqDynamicEndpoint(jitter):
    """
    RPC_STATUS I_RpcBindingInqDynamicEndpoint(
        RPC_BINDING_HANDLE Binding,
        RPC_CSTR* DynamicEndpoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "DynamicEndpoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingInqDynamicEndpoint(jitter, get_str, set_str):
    """
    RPC_STATUS I_RpcBindingInqDynamicEndpoint(
        RPC_BINDING_HANDLE Binding,
        RPC_TSTR* DynamicEndpoint
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "DynamicEndpoint"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingInqDynamicEndpointA(jitter):
    rpcrt4_I_RpcBindingInqDynamicEndpoint(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_I_RpcBindingInqDynamicEndpointW(jitter):
    rpcrt4_I_RpcBindingInqDynamicEndpoint(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_I_RpcBindingInqMarshalledTargetInfo(jitter):
    """
    RPC_STATUS I_RpcBindingInqMarshalledTargetInfo(
        RPC_BINDING_HANDLE Binding,
        unsigned long* MarshalledTargetInfoSize,
        RPC_CSTR* MarshalledTargetInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "MarshalledTargetInfoSize", "MarshalledTargetInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingInqSecurityContext(jitter):
    """
    RPC_STATUS I_RpcBindingInqSecurityContext(
        RPC_BINDING_HANDLE Binding,
        void** SecurityContextHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "SecurityContextHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingInqSecurityContextKeyInfo(jitter):
    """
    RPC_STATUS I_RpcBindingInqSecurityContextKeyInfo(
        RPC_BINDING_HANDLE Binding,
        void* KeyInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "KeyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingInqTransportType(jitter):
    """
    RPC_STATUS I_RpcBindingInqTransportType(
        RPC_BINDING_HANDLE Binding,
        [RPC_TRANSPORT_TYPE*] Type
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingInqWireIdForSnego(jitter):
    """
    RPC_STATUS I_RpcBindingInqWireIdForSnego(
        RPC_BINDING_HANDLE Binding,
        unsigned char* WireId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "WireId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingIsClientLocal(jitter):
    """
    RPC_STATUS I_RpcBindingIsClientLocal(
        RPC_BINDING_HANDLE BindingHandle,
        unsigned int* ClientLocalFlag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle", "ClientLocalFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcBindingToStaticStringBindingW(jitter):
    """
    RPC_STATUS I_RpcBindingToStaticStringBindingW(
        RPC_BINDING_HANDLE Binding,
        unsigned short** StringBinding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "StringBinding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcClearMutex(jitter):
    """
    void I_RpcClearMutex(
        I_RPC_MUTEX Mutex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Mutex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcConnectionInqSockBuffSize(jitter):
    """
    RPC_STATUS I_RpcConnectionInqSockBuffSize(
        unsigned long* RecvBuffSize,
        unsigned long* SendBuffSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RecvBuffSize", "SendBuffSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcConnectionSetSockBuffSize(jitter):
    """
    RPC_STATUS I_RpcConnectionSetSockBuffSize(
        unsigned long RecvBuffSize,
        unsigned long SendBuffSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RecvBuffSize", "SendBuffSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcDeleteMutex(jitter):
    """
    void I_RpcDeleteMutex(
        I_RPC_MUTEX Mutex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Mutex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcFree(jitter):
    """
    void I_RpcFree(
        void* Object
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcFreeBuffer(jitter):
    """
    RPC_STATUS I_RpcFreeBuffer(
        RPC_MESSAGE* Message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcFreePipeBuffer(jitter):
    """
    RPC_STATUS I_RpcFreePipeBuffer(
        RPC_MESSAGE* Message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcGetBuffer(jitter):
    """
    RPC_STATUS I_RpcGetBuffer(
        RPC_MESSAGE* Message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcGetBufferWithObject(jitter):
    """
    RPC_STATUS I_RpcGetBufferWithObject(
        RPC_MESSAGE* Message,
        UUID* ObjectUuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message", "ObjectUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcGetCurrentCallHandle(jitter):
    """
    RPC_BINDING_HANDLE I_RpcGetCurrentCallHandle()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcGetExtendedError(jitter):
    """
    RPC_STATUS I_RpcGetExtendedError()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcIfInqTransferSyntaxes(jitter):
    """
    RPC_STATUS I_RpcIfInqTransferSyntaxes(
        RPC_IF_HANDLE RpcIfHandle,
        RPC_TRANSFER_SYNTAX* TransferSyntaxes,
        unsigned int TransferSyntaxSize,
        unsigned int* TransferSyntaxCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RpcIfHandle", "TransferSyntaxes", "TransferSyntaxSize", "TransferSyntaxCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcMapWin32Status(jitter):
    """
    long I_RpcMapWin32Status(
        RPC_STATUS Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcMgmtEnableDedicatedThreadPool(jitter):
    """
    RPC_STATUS I_RpcMgmtEnableDedicatedThreadPool()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcNegotiateTransferSyntax(jitter):
    """
    RPC_STATUS I_RpcNegotiateTransferSyntax(
        RPC_MESSAGE* Message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcNsBindingSetEntryName(jitter):
    """
    RPC_STATUS I_RpcNsBindingSetEntryName(
        RPC_BINDING_HANDLE Binding,
        unsigned long EntryNameSyntax,
        RPC_CSTR EntryName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "EntryNameSyntax", "EntryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcNsBindingSetEntryName(jitter, get_str, set_str):
    """
    RPC_STATUS I_RpcNsBindingSetEntryName(
        RPC_BINDING_HANDLE Binding,
        unsigned long EntryNameSyntax,
        RPC_TSTR EntryName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "EntryNameSyntax", "EntryName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcNsBindingSetEntryNameA(jitter):
    rpcrt4_I_RpcNsBindingSetEntryName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_I_RpcNsBindingSetEntryNameW(jitter):
    rpcrt4_I_RpcNsBindingSetEntryName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_I_RpcNsInterfaceExported(jitter):
    """
    RPC_STATUS I_RpcNsInterfaceExported(
        unsigned long EntryNameSyntax,
        unsigned short* EntryName,
        RPC_SERVER_INTERFACE* RpcInterfaceInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "RpcInterfaceInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcNsInterfaceUnexported(jitter):
    """
    RPC_STATUS I_RpcNsInterfaceUnexported(
        unsigned long EntryNameSyntax,
        unsigned short* EntryName,
        RPC_SERVER_INTERFACE* RpcInterfaceInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EntryNameSyntax", "EntryName", "RpcInterfaceInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcOpenClientProcess(jitter):
    """
    RPC_STATUS I_RpcOpenClientProcess(
        RPC_BINDING_HANDLE Binding,
        unsigned long DesiredAccess,
        void** ClientProcess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "DesiredAccess", "ClientProcess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcPauseExecution(jitter):
    """
    void I_RpcPauseExecution(
        unsigned long Milliseconds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Milliseconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcReallocPipeBuffer(jitter):
    """
    RPC_STATUS I_RpcReallocPipeBuffer(
        PRPC_MESSAGE Message,
        unsigned int NewSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message", "NewSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcReceive(jitter):
    """
    RPC_STATUS I_RpcReceive(
        PRPC_MESSAGE Message,
        unsigned int Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcRecordCalloutFailure(jitter):
    """
    void I_RpcRecordCalloutFailure(
        RPC_STATUS RpcStatus,
        RDR_CALLOUT_STATE* CallOutState,
        unsigned short* DllName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["RpcStatus", "CallOutState", "DllName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcRequestMutex(jitter):
    """
    void I_RpcRequestMutex(
        I_RPC_MUTEX* Mutex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Mutex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcSend(jitter):
    """
    RPC_STATUS I_RpcSend(
        PRPC_MESSAGE Message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcSendReceive(jitter):
    """
    RPC_STATUS I_RpcSendReceive(
        RPC_MESSAGE* Message
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Message"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerCheckClientRestriction(jitter):
    """
    RPC_STATUS I_RpcServerCheckClientRestriction(
        RPC_BINDING_HANDLE Context
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerInqAddressChangeFn(jitter):
    """
    RPC_ADDRESS_CHANGE_FN* I_RpcServerInqAddressChangeFn()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerInqLocalConnAddress(jitter):
    """
    RPC_STATUS I_RpcServerInqLocalConnAddress(
        RPC_BINDING_HANDLE Binding,
        void* Buffer,
        unsigned long* BufferSize,
        unsigned long* AddressFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Buffer", "BufferSize", "AddressFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerInqRemoteConnAddress(jitter):
    """
    RPC_STATUS I_RpcServerInqRemoteConnAddress(
        RPC_BINDING_HANDLE Binding,
        void* Buffer,
        unsigned long* BufferSize,
        unsigned long* AddressFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Binding", "Buffer", "BufferSize", "AddressFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerInqTransportType(jitter):
    """
    RPC_STATUS I_RpcServerInqTransportType(
        [RPC_TRANSPORT_TYPE*] Type
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerRegisterForwardFunction(jitter):
    """
    RPC_STATUS I_RpcServerRegisterForwardFunction(
        RPC_FORWARD_FUNCTION* pForwardFunction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pForwardFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerSetAddressChangeFn(jitter):
    """
    RPC_STATUS I_RpcServerSetAddressChangeFn(
        RPC_ADDRESS_CHANGE_FN* pAddressChangeFn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAddressChangeFn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerStartService(jitter):
    """
    RPC_STATUS I_RpcServerStartService(
        RPC_WSTR Protseq,
        RPC_WSTR Endpoint,
        RPC_IF_HANDLE IfSpec
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Protseq", "Endpoint", "IfSpec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerUseProtseq2(jitter, get_str, set_str):
    """
    RPC_STATUS I_RpcServerUseProtseq2(
        RPC_TSTR NetworkAddress,
        RPC_TSTR Protseq,
        unsigned int MaxCalls,
        void* SecurityDescriptor,
        void* Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NetworkAddress", "Protseq", "MaxCalls", "SecurityDescriptor", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerUseProtseq2A(jitter):
    rpcrt4_I_RpcServerUseProtseq2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_I_RpcServerUseProtseq2W(jitter):
    rpcrt4_I_RpcServerUseProtseq2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_I_RpcServerUseProtseqEp2(jitter, get_str, set_str):
    """
    RPC_STATUS I_RpcServerUseProtseqEp2(
        RPC_TSTR NetworkAddress,
        RPC_TSTR Protseq,
        unsigned int MaxCalls,
        RPC_TSTR Endpoint,
        void* SecurityDescriptor,
        void* Policy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NetworkAddress", "Protseq", "MaxCalls", "Endpoint", "SecurityDescriptor", "Policy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcServerUseProtseqEp2A(jitter):
    rpcrt4_I_RpcServerUseProtseqEp2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_I_RpcServerUseProtseqEp2W(jitter):
    rpcrt4_I_RpcServerUseProtseqEp2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_I_RpcSessionStrictContextHandle(jitter):
    """
    void I_RpcSessionStrictContextHandle()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcSsDontSerializeContext(jitter):
    """
    void I_RpcSsDontSerializeContext()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_RpcTurnOnEEInfoPropagation(jitter):
    """
    RPC_STATUS I_RpcTurnOnEEInfoPropagation()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_I_UuidCreate(jitter):
    """
    RPC_STATUS I_UuidCreate(
        UUID* Uuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Uuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerCompleteSecurityCallback(jitter):
    """
    RPC_STATUS RpcServerCompleteSecurityCallback(
        RPC_BINDING_HANDLE BindingHandle,
        RPC_STATUS Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle", "Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcServerYield(jitter):
    """
    void RpcServerYield()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcSsGetContextBinding(jitter):
    """
    RPC_STATUS RpcSsGetContextBinding(
        void* ContextHandle,
        RPC_BINDING_HANDLE* Binding
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle", "Binding"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_RpcUserFree(jitter):
    """
    void RpcUserFree(
        handle_t AsyncHandle,
        void* pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AsyncHandle", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidCompare(jitter):
    """
    signed int UuidCompare(
        UUID* Uuid1,
        UUID* Uuid2,
        RPC_STATUS* Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Uuid1", "Uuid2", "Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidCreate(jitter):
    """
    RPC_STATUS UuidCreate(
        UUID* Uuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Uuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidCreateSequential(jitter):
    """
    RPC_STATUS UuidCreateSequential(
        UUID* Uuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Uuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidCreateNil(jitter):
    """
    RPC_STATUS UuidCreateNil(
        UUID* Nil_Uuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Nil_Uuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidEqual(jitter):
    """
    [BOOL|int] UuidEqual(
        UUID* Uuid1,
        UUID* Uuid2,
        RPC_STATUS* Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Uuid1", "Uuid2", "Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidFromString(jitter, get_str, set_str):
    """
    RPC_STATUS UuidFromString(
        RPC_TSTR StringUuid,
        UUID* Uuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StringUuid", "Uuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidFromStringA(jitter):
    rpcrt4_UuidFromString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_UuidFromStringW(jitter):
    rpcrt4_UuidFromString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_UuidHash(jitter):
    """
    unsigned short UuidHash(
        UUID* Uuid,
        RPC_STATUS* Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Uuid", "Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidIsNil(jitter):
    """
    [BOOL|int] UuidIsNil(
        UUID* Uuid,
        RPC_STATUS* Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Uuid", "Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidToString(jitter, get_str, set_str):
    """
    RPC_STATUS UuidToString(
        UUID* Uuid,
        RPC_TSTR* StringUuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Uuid", "StringUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_UuidToStringA(jitter):
    rpcrt4_UuidToString(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def rpcrt4_UuidToStringW(jitter):
    rpcrt4_UuidToString(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def rpcrt4_CStdStubBuffer_AddRef(jitter):
    """
    ULONG CStdStubBuffer_AddRef(
        IRpcStubBuffer* This
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_CStdStubBuffer_Connect(jitter):
    """
    HRESULT CStdStubBuffer_Connect(
        IRpcStubBuffer* This,
        IUnknown* pUnkServer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pUnkServer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_CStdStubBuffer_CountRefs(jitter):
    """
    ULONG CStdStubBuffer_CountRefs(
        IRpcStubBuffer* This
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_CStdStubBuffer_DebugServerQueryInterface(jitter):
    """
    HRESULT CStdStubBuffer_DebugServerQueryInterface(
        IRpcStubBuffer* This,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_CStdStubBuffer_DebugServerRelease(jitter):
    """
    void CStdStubBuffer_DebugServerRelease(
        IRpcStubBuffer* This,
        void* pv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_CStdStubBuffer_Disconnect(jitter):
    """
    void CStdStubBuffer_Disconnect(
        IRpcStubBuffer* This
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_CStdStubBuffer_Invoke(jitter):
    """
    HRESULT CStdStubBuffer_Invoke(
        IRpcStubBuffer* This,
        RPCOLEMESSAGE* pRpcMsg,
        IRpcChannelBuffer* pRpcChannelBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pRpcMsg", "pRpcChannelBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_CStdStubBuffer_IsIIDSupported(jitter):
    """
    IRpcStubBuffer* CStdStubBuffer_IsIIDSupported(
        IRpcStubBuffer* This,
        REFIID riid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "riid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_CStdStubBuffer_QueryInterface(jitter):
    """
    HRESULT CStdStubBuffer_QueryInterface(
        IRpcStubBuffer* This,
        REFIID riid,
        void** ppvObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "riid", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_IUnknown_AddRef_Proxy(jitter):
    """
    ULONG IUnknown_AddRef_Proxy(
        IUnknown* This
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_IUnknown_QueryInterface_Proxy(jitter):
    """
    HRESULT IUnknown_QueryInterface_Proxy(
        IUnknown* This,
        REFIID riid,
        void** ppvObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "riid", "ppvObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_IUnknown_Release_Proxy(jitter):
    """
    ULONG IUnknown_Release_Proxy(
        IUnknown* This
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrClearOutParameters(jitter):
    """
    void NdrClearOutParameters(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat,
        void* ArgAddr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat", "ArgAddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrContextHandleInitialize(jitter):
    """
    NDR_SCONTEXT NdrContextHandleInitialize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrContextHandleSize(jitter):
    """
    void NdrContextHandleSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrContextHandleMemorySize(jitter):
    """
    unsigned long NdrContextHandleMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConvert(jitter):
    """
    void NdrConvert(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrCStdStubBuffer_Release(jitter):
    """
    ULONG NdrCStdStubBuffer_Release(
        IRpcStubBuffer* This,
        IPSFactoryBuffer* pPSF
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pPSF"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrCStdStubBuffer2_Release(jitter):
    """
    ULONG NdrCStdStubBuffer2_Release(
        IRpcStubBuffer* This,
        IPSFactoryBuffer* pPSF
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pPSF"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrDllCanUnloadNow(jitter):
    """
    HRESULT NdrDllCanUnloadNow(
        CStdPSFactoryBuffer* pPSFactoryBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPSFactoryBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrDllGetClassObject(jitter):
    """
    HRESULT NdrDllGetClassObject(
        REFCLSID rclsid,
        REFIID riid,
        void** ppv,
        const ProxyFileInfo** pProxyFileList,
        const CLSID* pclsid,
        CStdPSFactoryBuffer* pPSFactoryBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "riid", "ppv", "pProxyFileList", "pclsid", "pPSFactoryBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrDllRegisterProxy(jitter):
    """
    HRESULT NdrDllRegisterProxy(
        HMODULE hDll,
        const ProxyFileInfo** pProxyFileList,
        const CLSID* pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDll", "pProxyFileList", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrDllUnregisterProxy(jitter):
    """
    HRESULT NdrDllUnregisterProxy(
        HMODULE hDll,
        const ProxyFileInfo** pProxyFileList,
        const CLSID* pclsid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hDll", "pProxyFileList", "pclsid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrOleAllocate(jitter):
    """
    void* NdrOleAllocate(
        size_t size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrOleFree(jitter):
    """
    void NdrOleFree(
        void* NodeToFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NodeToFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPointerBufferSize(jitter):
    """
    void NdrPointerBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPointerFree(jitter):
    """
    void NdrPointerFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPointerMarshall(jitter):
    """
    unsigned char* NdrPointerMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPointerUnmarshall(jitter):
    """
    unsigned char* NdrPointerUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** pMemory,
        PFORMAT_STRING pFormat,
        unsigned char fSkipRefCheck
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat", "fSkipRefCheck"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrProxyErrorHandler(jitter):
    """
    HRESULT NdrProxyErrorHandler(
        DWORD dwExceptionCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwExceptionCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrProxyFreeBuffer(jitter):
    """
    void NdrProxyFreeBuffer(
        void* This,
        MIDL_STUB_MESSAGE* pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrProxyGetBuffer(jitter):
    """
    void NdrProxyGetBuffer(
        void* This,
        PMIDL_STUB_MESSAGE pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrProxyInitialize(jitter):
    """
    void NdrProxyInitialize(
        void* This,
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor,
        unsigned int ProcNum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pRpcMsg", "pStubMsg", "pStubDescriptor", "ProcNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrProxySendReceive(jitter):
    """
    void NdrProxySendReceive(
        void* This,
        MIDL_STUB_MESSAGE* pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrSimpleTypeMarshall(jitter):
    """
    void NdrSimpleTypeMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        unsigned char FormatChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "FormatChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrSimpleTypeUnmarshall(jitter):
    """
    void NdrSimpleTypeUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        unsigned char FormatChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "FormatChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrStubForwardingFunction(jitter):
    """
    void NdrStubForwardingFunction(
        IRpcStubBuffer* pThis,
        IRpcChannelBuffer* pChannel,
        PRPC_MESSAGE pMsg,
        DWORD* pdwStubPhase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pThis", "pChannel", "pMsg", "pdwStubPhase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrStubGetBuffer(jitter):
    """
    void NdrStubGetBuffer(
        IRpcStubBuffer* This,
        IRpcChannelBuffer* pRpcChannelBuffer,
        PMIDL_STUB_MESSAGE pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["This", "pRpcChannelBuffer", "pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrStubInitialize(jitter):
    """
    void NdrStubInitialize(
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor,
        IRpcChannelBuffer* pRpcChannelBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg", "pStubMsg", "pStubDescriptor", "pRpcChannelBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrAllocate(jitter):
    """
    void* NdrAllocate(
        PMIDL_STUB_MESSAGE pStubMsg,
        size_t Len
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "Len"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrClientContextMarshall(jitter):
    """
    void NdrClientContextMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        NDR_CCONTEXT ContextHandle,
        int fCheck
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ContextHandle", "fCheck"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrClientContextUnmarshall(jitter):
    """
    void NdrClientContextUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        NDR_CCONTEXT* pContextHandle,
        RPC_BINDING_HANDLE BindHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pContextHandle", "BindHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConvert2(jitter):
    """
    void NdrConvert2(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat,
        long NumberParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat", "NumberParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrCorrelationFree(jitter):
    """
    void NdrCorrelationFree(
        PMIDL_STUB_MESSAGE pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrCorrelationInitialize(jitter):
    """
    void NdrCorrelationInitialize(
        PMIDL_STUB_MESSAGE pStubMsg,
        void* pMemory,
        unsigned long CacheSize,
        unsigned long flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "CacheSize", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrCorrelationPass(jitter):
    """
    void NdrCorrelationPass(
        PMIDL_STUB_MESSAGE pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrCreateServerInterfaceFromStub(jitter):
    """
    RPC_STATUS NdrCreateServerInterfaceFromStub(
        IRpcStubBuffer* pStub,
        RPC_SERVER_INTERFACE* pServerIf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStub", "pServerIf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMapCommAndFaultStatus(jitter):
    """
    RPC_STATUS NdrMapCommAndFaultStatus(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned long* pCommStatus,
        unsigned long* pFaultStatus,
        RPC_STATUS Status
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pCommStatus", "pFaultStatus", "Status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesProcEncodeDecode(jitter):
    """
    void NdrMesProcEncodeDecode(
        handle_t Handle,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pStubDesc", "pFormatString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesProcEncodeDecode2(jitter):
    """
    CLIENT_CALL_RETURN NdrMesProcEncodeDecode2(
        handle_t Handle,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pStubDesc", "pFormatString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesSimpleTypeAlignSize(jitter):
    """
    size_t NdrMesSimpleTypeAlignSize(
        handle_t Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesSimpleTypeDecode(jitter):
    """
    void NdrMesSimpleTypeDecode(
        handle_t Handle,
        void* pObject,
        short Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pObject", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesSimpleTypeEncode(jitter):
    """
    void NdrMesSimpleTypeEncode(
        handle_t Handle,
        const MIDL_STUB_DESC* pStubDesc,
        const void* pObject,
        short Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pStubDesc", "pObject", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesTypeAlignSize(jitter):
    """
    size_t NdrMesTypeAlignSize(
        handle_t Handle,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        const void* pObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pStubDesc", "pFormatString", "pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesTypeAlignSize2(jitter):
    """
    size_t NdrMesTypeAlignSize2(
        handle_t Handle,
        const MIDL_TYPE_PICKLING_INFO* pPicklingInfo,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        const void* pObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pPicklingInfo", "pStubDesc", "pFormatString", "pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesTypeDecode(jitter):
    """
    void NdrMesTypeDecode(
        handle_t Handle,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        void* pObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pStubDesc", "pFormatString", "pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesTypeDecode2(jitter):
    """
    void NdrMesTypeDecode2(
        handle_t Handle,
        const MIDL_TYPE_PICKLING_INFO* pPicklingInfo,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        void* pObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pPicklingInfo", "pStubDesc", "pFormatString", "pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesTypeEncode(jitter):
    """
    void NdrMesTypeEncode(
        handle_t Handle,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        const void* pObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pStubDesc", "pFormatString", "pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesTypeEncode2(jitter):
    """
    void NdrMesTypeEncode2(
        handle_t Handle,
        const MIDL_TYPE_PICKLING_INFO* pPicklingInfo,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        const void* pObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pPicklingInfo", "pStubDesc", "pFormatString", "pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrMesTypeFree2(jitter):
    """
    void NdrMesTypeFree2(
        handle_t Handle,
        const MIDL_TYPE_PICKLING_INFO* pPicklingInfo,
        const MIDL_STUB_DESC* pStubDesc,
        PFORMAT_STRING pFormatString,
        void* pObject
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "pPicklingInfo", "pStubDesc", "pFormatString", "pObject"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPartialIgnoreClientBufferSize(jitter):
    """
    void NdrPartialIgnoreClientBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        void* pMemory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPartialIgnoreClientMarshall(jitter):
    """
    void NdrPartialIgnoreClientMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        void* pMemory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPartialIgnoreServerInitialize(jitter):
    """
    void NdrPartialIgnoreServerInitialize(
        PMIDL_STUB_MESSAGE pStubMsg,
        void** ppMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPartialIgnoreServerUnmarshall(jitter):
    """
    void NdrPartialIgnoreServerUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        void** ppMemory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrPointerMemorySize(jitter):
    """
    unsigned long NdrPointerMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrRangeUnmarshall(jitter):
    """
    unsigned char* NdrRangeUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrRpcSmClientAllocate(jitter):
    """
    void* NdrRpcSmClientAllocate(
        size_t Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrRpcSmClientFree(jitter):
    """
    void NdrRpcSmClientFree(
        void* NodeToFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NodeToFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrRpcSmSetClientToOsf(jitter):
    """
    void NdrRpcSmSetClientToOsf(
        PMIDL_STUB_MESSAGE pMessage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrRpcSsDefaultAllocate(jitter):
    """
    void* NdrRpcSsDefaultAllocate(
        size_t Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrRpcSsDefaultFree(jitter):
    """
    void NdrRpcSsDefaultFree(
        void* NodeToFree
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NodeToFree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrRpcSsDisableAllocate(jitter):
    """
    void NdrRpcSsDisableAllocate(
        PMIDL_STUB_MESSAGE pMessage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrRpcSsEnableAllocate(jitter):
    """
    void NdrRpcSsEnableAllocate(
        PMIDL_STUB_MESSAGE pMessage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerContextMarshall(jitter):
    """
    void NdrServerContextMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        NDR_SCONTEXT ContextHandle,
        NDR_RUNDOWN RundownRoutine
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ContextHandle", "RundownRoutine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerContextNewMarshall(jitter):
    """
    void NdrServerContextNewMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        NDR_SCONTEXT ContextHandle,
        NDR_RUNDOWN RundownRoutine,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ContextHandle", "RundownRoutine", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerContextNewUnmarshall(jitter):
    """
    NDR_SCONTEXT NdrServerContextNewUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerContextUnmarshall(jitter):
    """
    NDR_SCONTEXT NdrServerContextUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRCContextBinding(jitter):
    """
    RPC_BINDING_HANDLE NDRCContextBinding(
        NDR_CCONTEXT CContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRCContextMarshall(jitter):
    """
    void NDRCContextMarshall(
        NDR_CCONTEXT CContext,
        void* pBuff
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CContext", "pBuff"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRCContextUnmarshall(jitter):
    """
    void NDRCContextUnmarshall(
        NDR_CCONTEXT* pCContext,
        RPC_BINDING_HANDLE hBinding,
        void* pBuff,
        unsigned long DataRepresentation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCContext", "hBinding", "pBuff", "DataRepresentation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRSContextMarshall(jitter):
    """
    void NDRSContextMarshall(
        NDR_SCONTEXT CContext,
        void* pBuff,
        NDR_RUNDOWN userRunDownIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CContext", "pBuff", "userRunDownIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRSContextMarshall2(jitter):
    """
    void NDRSContextMarshall2(
        RPC_BINDING_HANDLE BindingHandle,
        NDR_SCONTEXT CContext,
        void* pBuff,
        NDR_RUNDOWN userRunDownIn,
        void* CtxGuard,
        unsigned long Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle", "CContext", "pBuff", "userRunDownIn", "CtxGuard", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRSContextMarshallEx(jitter):
    """
    void NDRSContextMarshallEx(
        RPC_BINDING_HANDLE BindingHandle,
        NDR_SCONTEXT CContext,
        void* pBuff,
        NDR_RUNDOWN userRunDownIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle", "CContext", "pBuff", "userRunDownIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRSContextUnmarshall(jitter):
    """
    NDR_SCONTEXT NDRSContextUnmarshall(
        void* pBuff,
        unsigned long DataRepresentation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBuff", "DataRepresentation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRSContextUnmarshall2(jitter):
    """
    NDR_SCONTEXT NDRSContextUnmarshall2(
        RPC_BINDING_HANDLE BindingHandle,
        void* pBuff,
        unsigned long DataRepresentation,
        void* CtxGuard,
        unsigned long Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle", "pBuff", "DataRepresentation", "CtxGuard", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NDRSContextUnmarshallEx(jitter):
    """
    NDR_SCONTEXT NDRSContextUnmarshallEx(
        RPC_BINDING_HANDLE BindingHandle,
        void* pBuff,
        unsigned long DataRepresentation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle", "pBuff", "DataRepresentation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStringBufferSize(jitter):
    """
    void NdrConformantStringBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStringMarshall(jitter):
    """
    unsigned char* NdrConformantStringMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStringUnmarshall(jitter):
    """
    unsigned char* NdrConformantStringUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStringMemorySize(jitter):
    """
    unsigned long NdrConformantStringMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonConformantStringBufferSize(jitter):
    """
    void NdrNonConformantStringBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonConformantStringMarshall(jitter):
    """
    unsigned char* NdrNonConformantStringMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonConformantStringMemorySize(jitter):
    """
    unsigned long NdrNonConformantStringMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonConformantStringUnmarshall(jitter):
    """
    unsigned char* NdrNonConformantStringUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrEncapsulatedUnionBufferSize(jitter):
    """
    void NdrEncapsulatedUnionBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrEncapsulatedUnionFree(jitter):
    """
    void NdrEncapsulatedUnionFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrEncapsulatedUnionMarshall(jitter):
    """
    unsigned char* NdrEncapsulatedUnionMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrEncapsulatedUnionMemorySize(jitter):
    """
    unsigned long NdrEncapsulatedUnionMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrEncapsulatedUnionUnmarshall(jitter):
    """
    unsigned char* NdrEncapsulatedUnionUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonEncapsulatedUnionBufferSize(jitter):
    """
    void NdrNonEncapsulatedUnionBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonEncapsulatedUnionFree(jitter):
    """
    void NdrNonEncapsulatedUnionFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonEncapsulatedUnionMarshall(jitter):
    """
    unsigned char* NdrNonEncapsulatedUnionMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonEncapsulatedUnionMemorySize(jitter):
    """
    unsigned long NdrNonEncapsulatedUnionMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNonEncapsulatedUnionUnmarshall(jitter):
    """
    unsigned char* NdrNonEncapsulatedUnionUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFixedArrayBufferSize(jitter):
    """
    void NdrFixedArrayBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFixedArrayFree(jitter):
    """
    void NdrFixedArrayFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFixedArrayMarshall(jitter):
    """
    unsigned char* NdrFixedArrayMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFixedArrayMemorySize(jitter):
    """
    unsigned long NdrFixedArrayMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFixedArrayUnmarshall(jitter):
    """
    unsigned char* NdrFixedArrayUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantArrayUnmarshall(jitter):
    """
    unsigned char* NdrConformantArrayUnmarshall(
        PMIDL_STUB_MESSAGE NdrConformantArrayUnmarshall,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NdrConformantArrayUnmarshall", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantArrayBufferSize(jitter):
    """
    void NdrConformantArrayBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantArrayMarshall(jitter):
    """
    unsigned char* NdrConformantArrayMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantArrayFree(jitter):
    """
    void NdrConformantArrayFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantArrayMemorySize(jitter):
    """
    unsigned long NdrConformantArrayMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexArrayBufferSize(jitter):
    """
    void NdrComplexArrayBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexArrayMarshall(jitter):
    """
    unsigned char* NdrComplexArrayMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexArrayUnmarshall(jitter):
    """
    unsigned char* NdrComplexArrayUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexArrayFree(jitter):
    """
    void NdrComplexArrayFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexArrayMemorySize(jitter):
    """
    unsigned long NdrComplexArrayMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingArrayBufferSize(jitter):
    """
    void NdrConformantVaryingArrayBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingArrayFree(jitter):
    """
    void NdrConformantVaryingArrayFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingArrayMarshall(jitter):
    """
    unsigned char* NdrConformantVaryingArrayMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingArrayMemorySize(jitter):
    """
    unsigned long NdrConformantVaryingArrayMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingArrayUnmarshall(jitter):
    """
    unsigned char* NdrConformantVaryingArrayUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrVaryingArrayBufferSize(jitter):
    """
    void NdrVaryingArrayBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrVaryingArrayFree(jitter):
    """
    void NdrVaryingArrayFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrVaryingArrayMarshall(jitter):
    """
    unsigned char* NdrVaryingArrayMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrVaryingArrayMemorySize(jitter):
    """
    unsigned long NdrVaryingArrayMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrVaryingArrayUnmarshall(jitter):
    """
    unsigned char* NdrVaryingArrayUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrSimpleStructBufferSize(jitter):
    """
    void NdrSimpleStructBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrSimpleStructMarshall(jitter):
    """
    unsigned char* NdrSimpleStructMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrSimpleStructUnmarshall(jitter):
    """
    unsigned char* NdrSimpleStructUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrSimpleStructFree(jitter):
    """
    void NdrSimpleStructFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrSimpleStructMemorySize(jitter):
    """
    unsigned long NdrSimpleStructMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexStructBufferSize(jitter):
    """
    void NdrComplexStructBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexStructMarshall(jitter):
    """
    unsigned char* NdrComplexStructMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexStructUnmarshall(jitter):
    """
    unsigned char* NdrComplexStructUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexStructFree(jitter):
    """
    void NdrComplexStructFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrComplexStructMemorySize(jitter):
    """
    unsigned long NdrComplexStructMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingStructBufferSize(jitter):
    """
    void NdrConformantVaryingStructBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingStructFree(jitter):
    """
    void NdrConformantVaryingStructFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingStructMarshall(jitter):
    """
    unsigned char* NdrConformantVaryingStructMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingStructMemorySize(jitter):
    """
    unsigned long NdrConformantVaryingStructMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantVaryingStructUnmarshall(jitter):
    """
    unsigned char* NdrConformantVaryingStructUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStructBufferSize(jitter):
    """
    void NdrConformantStructBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStructFree(jitter):
    """
    void NdrConformantStructFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStructMarshall(jitter):
    """
    unsigned char* NdrConformantStructMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStructMemorySize(jitter):
    """
    unsigned long NdrConformantStructMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrConformantStructUnmarshall(jitter):
    """
    unsigned char* NdrConformantStructUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrXmitOrRepAsBufferSize(jitter):
    """
    void NdrXmitOrRepAsBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrXmitOrRepAsFree(jitter):
    """
    void NdrXmitOrRepAsFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrXmitOrRepAsMarshall(jitter):
    """
    unsigned char* NdrXmitOrRepAsMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrXmitOrRepAsMemorySize(jitter):
    """
    unsigned long NdrXmitOrRepAsMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrXmitOrRepAsUnmarshall(jitter):
    """
    unsigned char* NdrXmitOrRepAsUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrInterfacePointerBufferSize(jitter):
    """
    void NdrInterfacePointerBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrInterfacePointerFree(jitter):
    """
    void NdrInterfacePointerFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrInterfacePointerMarshall(jitter):
    """
    unsigned char* NdrInterfacePointerMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrInterfacePointerUnmarshall(jitter):
    """
    unsigned char* NdrInterfacePointerUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrInterfacePointerMemorySize(jitter):
    """
    unsigned long NdrInterfacePointerMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrGetUserMarshalInfo(jitter):
    """
    RPC_STATUS NdrGetUserMarshalInfo(
        unsigned long* pFlags,
        unsigned long InformationLevel,
        NDR_USER_MARSHAL_INFO* pMarshalInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "InformationLevel", "pMarshalInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrUserMarshalBufferSize(jitter):
    """
    void NdrUserMarshalBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrUserMarshalFree(jitter):
    """
    void NdrUserMarshalFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrUserMarshalMarshall(jitter):
    """
    unsigned char* NdrUserMarshalMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrUserMarshalUnmarshall(jitter):
    """
    unsigned char* NdrUserMarshalUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrUserMarshalMemorySize(jitter):
    """
    unsigned long NdrUserMarshalMemorySize(
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrUserMarshalSimpleTypeConvert(jitter):
    """
    unsigned char* NdrUserMarshalSimpleTypeConvert(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        unsigned char FormatChar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "FormatChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrByteCountPointerBufferSize(jitter):
    """
    void NdrByteCountPointerBufferSize(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrByteCountPointerFree(jitter):
    """
    void NdrByteCountPointerFree(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrByteCountPointerMarshall(jitter):
    """
    unsigned char* NdrByteCountPointerMarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pMemory,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pMemory", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrByteCountPointerUnmarshall(jitter):
    """
    unsigned char* NdrByteCountPointerUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char** ppMemory,
        PFORMAT_STRING pFormat,
        unsigned char fMustAlloc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "ppMemory", "pFormat", "fMustAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrClientInitializeNew(jitter):
    """
    void NdrClientInitializeNew(
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor,
        unsigned int ProcNum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg", "pStubMsg", "pStubDescriptor", "ProcNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerInitializeNew(jitter):
    """
    unsigned char* NdrServerInitializeNew(
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg", "pStubMsg", "pStubDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerInitializePartial(jitter):
    """
    void NdrServerInitializePartial(
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor,
        unsigned long RequestedBufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg", "pStubMsg", "pStubDescriptor", "RequestedBufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrClientInitialize(jitter):
    """
    void NdrClientInitialize(
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor,
        unsigned int ProcNum
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg", "pStubMsg", "pStubDescriptor", "ProcNum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerInitialize(jitter):
    """
    unsigned char* NdrServerInitialize(
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg", "pStubMsg", "pStubDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerInitializeUnmarshall(jitter):
    """
    unsigned char* NdrServerInitializeUnmarshall(
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor,
        PRPC_MESSAGE pRpcMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pStubDescriptor", "pRpcMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerInitializeMarshall(jitter):
    """
    void NdrServerInitializeMarshall(
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg", "pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrGetBuffer(jitter):
    """
    unsigned char* NdrGetBuffer(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned long BufferLength,
        RPC_BINDING_HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "BufferLength", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNsGetBuffer(jitter):
    """
    unsigned char* NdrNsGetBuffer(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned long BufferLength,
        RPC_BINDING_HANDLE Handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "BufferLength", "Handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrSendReceive(jitter):
    """
    unsigned char* NdrSendReceive(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pBufferEnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pBufferEnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrNsSendReceive(jitter):
    """
    unsigned char* NdrNsSendReceive(
        PMIDL_STUB_MESSAGE pStubMsg,
        unsigned char* pBufferEnd,
        RPC_BINDING_HANDLE* pAutoHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pBufferEnd", "pAutoHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFreeBuffer(jitter):
    """
    void NdrFreeBuffer(
        PMIDL_STUB_MESSAGE pStubMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrGetDcomProtocolVersion(jitter):
    """
    RPC_STATUS NdrGetDcomProtocolVersion(
        PMIDL_STUB_MESSAGE pStubMsg,
        RPC_VERSION* pVersion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubMsg", "pVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrClientCall2(jitter):
    """
    CLIENT_CALL_RETURN NdrClientCall2(
        PMIDL_STUB_DESC pStubDescriptor,
        PFORMAT_STRING pFormat,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubDescriptor", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrClientCall(jitter):
    """
    CLIENT_CALL_RETURN NdrClientCall(
        PMIDL_STUB_DESC pStubDescriptor,
        PFORMAT_STRING pFormat,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubDescriptor", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrAsyncClientCall(jitter):
    """
    CLIENT_CALL_RETURN NdrAsyncClientCall(
        PMIDL_STUB_DESC pStubDescriptor,
        PFORMAT_STRING pFormat,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubDescriptor", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrDcomAsyncClientCall(jitter):
    """
    CLIENT_CALL_RETURN NdrDcomAsyncClientCall(
        PMIDL_STUB_DESC pStubDescriptor,
        PFORMAT_STRING pFormat,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStubDescriptor", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrAsyncServerCall(jitter):
    """
    void NdrAsyncServerCall(
        PRPC_MESSAGE pRpcMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrAsyncStubCall(jitter):
    """
    long NdrAsyncStubCall(
        IRpcStubBuffer* pThis,
        IRpcChannelBuffer* pChannel,
        PRPC_MESSAGE pRpcMsg,
        unsigned long* pdwStubPhase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pThis", "pChannel", "pRpcMsg", "pdwStubPhase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrDcomAsyncStubCall(jitter):
    """
    long NdrDcomAsyncStubCall(
        IRpcStubBuffer* pThis,
        IRpcChannelBuffer* pChannel,
        PRPC_MESSAGE pRpcMsg,
        unsigned long* pdwStubPhase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pThis", "pChannel", "pRpcMsg", "pdwStubPhase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrStubCall2(jitter):
    """
    long NdrStubCall2(
        IRpcStubBuffer* pThis,
        IRpcChannelBuffer* pChannel,
        PRPC_MESSAGE pRpcMsg,
        unsigned long* pdwStubPhase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pThis", "pChannel", "pRpcMsg", "pdwStubPhase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerCall2(jitter):
    """
    void NdrServerCall2(
        PRPC_MESSAGE pRpcMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrStubCall(jitter):
    """
    long NdrStubCall(
        IRpcStubBuffer* pThis,
        IRpcChannelBuffer* pChannel,
        PRPC_MESSAGE pRpcMsg,
        unsigned long* pdwStubPhase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pThis", "pChannel", "pRpcMsg", "pdwStubPhase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerCall(jitter):
    """
    void NdrServerCall(
        PRPC_MESSAGE pRpcMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerUnmarshall(jitter):
    """
    int NdrServerUnmarshall(
        IRpcChannelBuffer* pChannel,
        PRPC_MESSAGE pRpcMsg,
        PMIDL_STUB_MESSAGE pStubMsg,
        PMIDL_STUB_DESC pStubDescriptor,
        PFORMAT_STRING pFormat,
        void* pParamList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pChannel", "pRpcMsg", "pStubMsg", "pStubDescriptor", "pFormat", "pParamList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerMarshall(jitter):
    """
    void NdrServerMarshall(
        IRpcStubBuffer* pThis,
        IRpcChannelBuffer* pChannel,
        PMIDL_STUB_MESSAGE pStubMsg,
        PFORMAT_STRING pFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pThis", "pChannel", "pStubMsg", "pFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_Ndr64AsyncClientCall(jitter):
    """
    CLIENT_CALL_RETURN Ndr64AsyncClientCall(
        MIDL_STUBLESS_PROXY_INFO* pProxyInfo,
        unsigned long nProcNum,
        void* pReturnValue,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyInfo", "nProcNum", "pReturnValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_Ndr64AsyncServerCall64(jitter):
    """
    void Ndr64AsyncServerCall64(
        PRPC_MESSAGE pRpcMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_Ndr64AsyncServerCallAll(jitter):
    """
    void Ndr64AsyncServerCallAll(
        PRPC_MESSAGE pRpcMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_Ndr64DcomAsyncClientCall(jitter):
    """
    CLIENT_CALL_RETURN Ndr64DcomAsyncClientCall(
        MIDL_STUBLESS_PROXY_INFO* pProxyInfo,
        unsigned long nProcNum,
        void* pReturnValue,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProxyInfo", "nProcNum", "pReturnValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_Ndr64DcomAsyncStubCall(jitter):
    """
    long Ndr64DcomAsyncStubCall(
        IRpcStubBuffer* pThis,
        IRpcChannelBuffer* pChannel,
        PRPC_MESSAGE pRpcMsg,
        unsigned long* pdwStubPhase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pThis", "pChannel", "pRpcMsg", "pdwStubPhase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerCallAll(jitter):
    """
    void NdrServerCallAll(
        PRPC_MESSAGE pRpcMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrServerCallNdr64(jitter):
    """
    void NdrServerCallNdr64(
        PRPC_MESSAGE pRpcMsg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRpcMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrStubCall3(jitter):
    """
    long NdrStubCall3(
        IRpcStubBuffer* pThis,
        IRpcChannelBuffer* pChannel,
        PRPC_MESSAGE pRpcMsg,
        unsigned long* pdwStubPhase
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pThis", "pChannel", "pRpcMsg", "pdwStubPhase"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFullPointerXlatInit(jitter):
    """
    PFULL_PTR_XLAT_TABLES NdrFullPointerXlatInit(
        unsigned long NumberOfPointers,
        XLAT_SIDE XlatSide
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NumberOfPointers", "XlatSide"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFullPointerXlatFree(jitter):
    """
    void NdrFullPointerXlatFree(
        PFULL_PTR_XLAT_TABLES pXlatTables
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pXlatTables"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFullPointerQueryPointer(jitter):
    """
    int NdrFullPointerQueryPointer(
        PFULL_PTR_XLAT_TABLES pXlatTables,
        void* pPointer,
        unsigned char QueryType,
        unsigned long* pRefId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pXlatTables", "pPointer", "QueryType", "pRefId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFullPointerQueryRefId(jitter):
    """
    int NdrFullPointerQueryRefId(
        PFULL_PTR_XLAT_TABLES pXlatTables,
        unsigned long RefId,
        unsigned char QueryType,
        void** ppPointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pXlatTables", "RefId", "QueryType", "ppPointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFullPointerInsertRefId(jitter):
    """
    void NdrFullPointerInsertRefId(
        PFULL_PTR_XLAT_TABLES pXlatTables,
        unsigned long RefId,
        void* pPointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pXlatTables", "RefId", "pPointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def rpcrt4_NdrFullPointerFree(jitter):
    """
    int NdrFullPointerFree(
        PFULL_PTR_XLAT_TABLES pXlatTables,
        void* Pointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pXlatTables", "Pointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
