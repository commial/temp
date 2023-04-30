
def input_EnumEnabledLayoutOrTip(jitter):
    """
    [input.dll] UINT EnumEnabledLayoutOrTip(LPCWSTR pszUserSidString, LAYOUTORTIPPROFILE* pLayoutOrTipProfile, UINT uBufLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserSidString", "pLayoutOrTipProfile", "uBufLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_EnumLayoutOrTipForSetup(jitter):
    """
    [input.dll] UINT EnumLayoutOrTipForSetup(UINT uBufLength, LAYOUTORTIP* pLayoutOrTip, UINT uBufLength, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["uBufLength", "pLayoutOrTip", "uBufLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_InstallLayoutOrTip(jitter):
    """
    [input.dll] BOOL InstallLayoutOrTip(LPCWSTR psz, [IlotFlags] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_InstallLayoutOrTipUserReg(jitter):
    """
    [input.dll] BOOL InstallLayoutOrTipUserReg(LPCWSTR pszUserReg, LPCWSTR pszSystemReg, LPCWSTR pszSoftwareReg, LPCWSTR psz, [IlotFlags] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserReg", "pszSystemReg", "pszSoftwareReg", "psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_QueryLayoutOrTipString(jitter):
    """
    [input.dll] HRESULT QueryLayoutOrTipString(LPCWSTR psz, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_QueryLayoutOrTipStringUserReg(jitter):
    """
    [input.dll] HRESULT QueryLayoutOrTipStringUserReg(LPCWSTR pszUserReg, LPCWSTR pszSystemReg, LPCWSTR pszSoftwareReg, LPCWSTR psz, DWORD dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserReg", "pszSystemReg", "pszSoftwareReg", "psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_SaveDefaultUserInputSettings(jitter):
    """
    [input.dll] BOOL SaveDefaultUserInputSettings(HWND hwndParent, HKEY hSourceRegKey)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hSourceRegKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_SaveSystemAcctInputSettings(jitter):
    """
    [input.dll] BOOL SaveSystemAcctInputSettings(HWND hwndParent, HKEY hSourceRegKey)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hSourceRegKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_SetDefaultLayoutOrTip(jitter):
    """
    [input.dll] BOOL SetDefaultLayoutOrTip(LPCWSTR psz, [SdlotFlags] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_SetDefaultLayoutOrTipUserReg(jitter):
    """
    [input.dll] BOOL SetDefaultLayoutOrTipUserReg(LPCWSTR pszUserReg, LPCWSTR pszSystemReg, LPCWSTR pszSoftwareReg, LPCWSTR psz, [SdlotFlags] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserReg", "pszSystemReg", "pszSoftwareReg", "psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
