
def shdocvw_ShellDDEInit(jitter):
    """
    [Shdocvw.dll] void ShellDDEInit(BOOL init)
    """
    ret_ad, args = jitter.func_args_stdcall(["init"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shdocvw_SoftwareUpdateMessageBox(jitter):
    """
    [Shdocvw.dll] DWORD SoftwareUpdateMessageBox(HWND hWnd, LPCWSTR pszDistUnit, DWORD dwFlags, LPSOFTDISTINFO psdi)
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pszDistUnit", "dwFlags", "psdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shdocvw_DoPrivacyDlg(jitter):
    """
    [Shdocvw.dll] HRESULT DoPrivacyDlg(HWND hwndParent, LPCWSTR pszUrl, IEnumPrivacyRecords* pPrivacyEnum, BOOL fReportAllSites)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pszUrl", "pPrivacyEnum", "fReportAllSites"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shdocvw_ImportPrivacySettings(jitter):
    """
    [Shdocvw.dll] BOOL ImportPrivacySettings(LPCWSTR szFilename, BOOL* pfParsePrivacyPreferences, BOOL* pfParsePerSiteRules)
    """
    ret_ad, args = jitter.func_args_stdcall(["szFilename", "pfParsePrivacyPreferences", "pfParsePerSiteRules"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
