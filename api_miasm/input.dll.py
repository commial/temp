
def input_EnumEnabledLayoutOrTip(jitter):
    """
    UINT EnumEnabledLayoutOrTip(
        LPCWSTR pszUserSidString,
        LAYOUTORTIPPROFILE* pLayoutOrTipProfile,
        UINT uBufLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserSidString", "pLayoutOrTipProfile", "uBufLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_EnumLayoutOrTipForSetup(jitter):
    """
    UINT EnumLayoutOrTipForSetup(
        UINT uBufLength,
        LAYOUTORTIP* pLayoutOrTip,
        UINT uBufLength,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uBufLength", "pLayoutOrTip", "uBufLength", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_InstallLayoutOrTip(jitter):
    """
    BOOL InstallLayoutOrTip(
        LPCWSTR psz,
        [IlotFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_InstallLayoutOrTipUserReg(jitter):
    """
    BOOL InstallLayoutOrTipUserReg(
        LPCWSTR pszUserReg,
        LPCWSTR pszSystemReg,
        LPCWSTR pszSoftwareReg,
        LPCWSTR psz,
        [IlotFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserReg", "pszSystemReg", "pszSoftwareReg", "psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_QueryLayoutOrTipString(jitter):
    """
    HRESULT QueryLayoutOrTipString(
        LPCWSTR psz,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_QueryLayoutOrTipStringUserReg(jitter):
    """
    HRESULT QueryLayoutOrTipStringUserReg(
        LPCWSTR pszUserReg,
        LPCWSTR pszSystemReg,
        LPCWSTR pszSoftwareReg,
        LPCWSTR psz,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserReg", "pszSystemReg", "pszSoftwareReg", "psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_SaveDefaultUserInputSettings(jitter):
    """
    BOOL SaveDefaultUserInputSettings(
        HWND hwndParent,
        HKEY hSourceRegKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hSourceRegKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_SaveSystemAcctInputSettings(jitter):
    """
    BOOL SaveSystemAcctInputSettings(
        HWND hwndParent,
        HKEY hSourceRegKey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hSourceRegKey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_SetDefaultLayoutOrTip(jitter):
    """
    BOOL SetDefaultLayoutOrTip(
        LPCWSTR psz,
        [SdlotFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def input_SetDefaultLayoutOrTipUserReg(jitter):
    """
    BOOL SetDefaultLayoutOrTipUserReg(
        LPCWSTR pszUserReg,
        LPCWSTR pszSystemReg,
        LPCWSTR pszSoftwareReg,
        LPCWSTR psz,
        [SdlotFlags] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserReg", "pszSystemReg", "pszSoftwareReg", "psz", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
