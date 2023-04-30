
def wab32_WABOpen(jitter):
    """
    HRESULT WABOpen(
        LPADRBOOK* lppAdrBook,
        LPWABOBJECT* lppWABObject,
        LPWAB_PARAM lpWABParam,
        DWORD Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppAdrBook", "lppWABObject", "lpWABParam", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wab32_WABOpenEx(jitter):
    """
    HRESULT WABOpenEx(
        LPADRBOOK* lppAdrBook,
        LPWABOBJECT* lppWABObject,
        LPWAB_PARAM lpWABParam,
        DWORD Reserved2,
        ALLOCATEBUFFER* lpfnAllocateBuffer,
        ALLOCATEMORE* lpfnAllocateMore,
        FREEBUFFER* lpfnFreeBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppAdrBook", "lppWABObject", "lpWABParam", "Reserved2", "lpfnAllocateBuffer", "lpfnAllocateMore", "lpfnFreeBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
