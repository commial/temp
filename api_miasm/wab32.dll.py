###### Enums ######

###################

###### Types ######
LPWABOBJECT_PTR = IWABObject_PTR_PTR
_WAB_PARAM_Flags_ = ULONG

class WAB_PARAM(MemStruct):
    fields = [
        ("cbSize", ULONG()),
        ("hwnd", HWND()),
        ("szFileName", LPSTR()),
        ("ulFlags", _WAB_PARAM_Flags_()),
        ("guidPSExt", GUID()),
    ]

LPWAB_PARAM = Ptr("<I", WAB_PARAM())

###################

###### Functions ######

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
