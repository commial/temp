
def storprop_CdromDisableDigitalPlayback(jitter):
    """
    [Storprop.dll] [ERROR_CODE|LONG] CdromDisableDigitalPlayback(HDEVINFO DevInfo, PSP_DEVINFO_DATA DevInfoData)
    """
    ret_ad, args = jitter.func_args_stdcall(["DevInfo", "DevInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def storprop_CdromEnableDigitalPlayback(jitter):
    """
    [Storprop.dll] [ERROR_CODE|LONG] CdromEnableDigitalPlayback(HDEVINFO DevInfo, PSP_DEVINFO_DATA DevInfoData, BOOLEAN ForceUnknown)
    """
    ret_ad, args = jitter.func_args_stdcall(["DevInfo", "DevInfoData", "ForceUnknown"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def storprop_CdromIsDigitalPlaybackEnabled(jitter):
    """
    [Storprop.dll] [ERROR_CODE|LONG] CdromIsDigitalPlaybackEnabled(HDEVINFO DevInfo, PSP_DEVINFO_DATA DevInfoData, PBOOLEAN Enabled)
    """
    ret_ad, args = jitter.func_args_stdcall(["DevInfo", "DevInfoData", "Enabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def storprop_CdromKnownGoodDigitalPlayback(jitter):
    """
    [Storprop.dll] BOOL CdromKnownGoodDigitalPlayback(HDEVINFO DevInfo, PSP_DEVINFO_DATA DevInfoData)
    """
    ret_ad, args = jitter.func_args_stdcall(["DevInfo", "DevInfoData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def storprop_DvdLauncher(jitter):
    """
    [Storprop.dll] BOOL DvdLauncher(HWND HWnd, CHAR DriveLetter)
    """
    ret_ad, args = jitter.func_args_stdcall(["HWnd", "DriveLetter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
