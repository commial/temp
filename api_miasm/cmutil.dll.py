
def cmutil_CmFree(jitter):
    """
    [CmUtil.dll] void* CmFree(void* pvPtr)
    """
    ret_ad, args = jitter.func_args_stdcall(["pvPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cmutil_CmMalloc(jitter):
    """
    [CmUtil.dll] void* CmMalloc(size_t nBytes)
    """
    ret_ad, args = jitter.func_args_stdcall(["nBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
