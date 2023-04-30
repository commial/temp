
def rpcdiag_RpcDiagnoseError(jitter):
    """
    RPC_STATUS RpcDiagnoseError(
        RPC_BINDING_HANDLE BindingHandle,
        RPC_IF_HANDLE IfSpec,
        RPC_STATUS RpcStatus,
        RPC_ERROR_ENUM_HANDLE* EnumHandle,
        ULONG Options,
        HWND ParentWindow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["BindingHandle", "IfSpec", "RpcStatus", "EnumHandle", "Options", "ParentWindow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
