
def dsprop_ADsPropCheckIfWritable(jitter):
    """
    BOOL ADsPropCheckIfWritable(
        const PWSTR pwzAttr,
        const PADS_ATTR_INFO pWritableAttrs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzAttr", "pWritableAttrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropCreateNotifyObj(jitter):
    """
    HRESULT ADsPropCreateNotifyObj(
        LPDATAOBJECT pAppThdDataObj,
        PWSTR pwzADsObjName,
        HWND* phNotifyObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppThdDataObj", "pwzADsObjName", "phNotifyObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropGetInitInfo(jitter):
    """
    BOOL ADsPropGetInitInfo(
        HWND hNotifyObject,
        PADSPROPINITPARAMS pInitParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "pInitParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSendErrorMessage(jitter):
    """
    BOOL ADsPropSendErrorMessage(
        HWND hNotifyObject,
        PADSPROPERROR pError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "pError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSetHwnd(jitter):
    """
    BOOL ADsPropSetHwnd(
        HWND hNotifyObject,
        HWND hPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSetHwndWithTitle(jitter):
    """
    BOOL ADsPropSetHwndWithTitle(
        HWND hNotifyObject,
        HWND hPage,
        PTSTR ptzTitle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage", "ptzTitle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropShowErrorDialog(jitter):
    """
    BOOL ADsPropShowErrorDialog(
        HWND hNotifyObject,
        HWND hPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
