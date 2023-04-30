
def dsprop_ADsPropCheckIfWritable(jitter):
    """
    [Dsprop.dll] BOOL ADsPropCheckIfWritable(const PWSTR pwzAttr, const PADS_ATTR_INFO pWritableAttrs)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwzAttr", "pWritableAttrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropCreateNotifyObj(jitter):
    """
    [Dsprop.dll] HRESULT ADsPropCreateNotifyObj(LPDATAOBJECT pAppThdDataObj, PWSTR pwzADsObjName, HWND* phNotifyObj)
    """
    ret_ad, args = jitter.func_args_stdcall(["pAppThdDataObj", "pwzADsObjName", "phNotifyObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropGetInitInfo(jitter):
    """
    [Dsprop.dll] BOOL ADsPropGetInitInfo(HWND hNotifyObject, PADSPROPINITPARAMS pInitParams)
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "pInitParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSendErrorMessage(jitter):
    """
    [Dsprop.dll] BOOL ADsPropSendErrorMessage(HWND hNotifyObject, PADSPROPERROR pError)
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "pError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSetHwnd(jitter):
    """
    [Dsprop.dll] BOOL ADsPropSetHwnd(HWND hNotifyObject, HWND hPage)
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropSetHwndWithTitle(jitter):
    """
    [Dsprop.dll] BOOL ADsPropSetHwndWithTitle(HWND hNotifyObject, HWND hPage, PTSTR ptzTitle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage", "ptzTitle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dsprop_ADsPropShowErrorDialog(jitter):
    """
    [Dsprop.dll] BOOL ADsPropShowErrorDialog(HWND hNotifyObject, HWND hPage)
    """
    ret_ad, args = jitter.func_args_stdcall(["hNotifyObject", "hPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
