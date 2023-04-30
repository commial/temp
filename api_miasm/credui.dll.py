
def credui_CredUICmdLinePromptForCredentials(jitter):
    """"
    [Credui.dll] [ERROR_CODE] CredUICmdLinePromptForCredentials(PCTSTR pszTargetName, PCtxtHandle Reserved, DWORD dwAuthError, PTSTR pszUserName, ULONG ulUserNameMaxChars, PTSTR pszPassword, ULONG ulPasswordMaxChars, PBOOL pfSave, [CredUIFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszTargetName", "Reserved", "dwAuthError", "pszUserName", "ulUserNameMaxChars", "pszPassword", "ulPasswordMaxChars", "pfSave", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_CredUIConfirmCredentials(jitter):
    """"
    [Credui.dll] [ERROR_CODE] CredUIConfirmCredentials(PCTSTR pszTargetName, BOOL bConfirm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszTargetName", "bConfirm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_CredUIParseUserName(jitter):
    """"
    [Credui.dll] [ERROR_CODE] CredUIParseUserName(PCTSTR pszUserName, PTSTR pszUser, ULONG ulUserMaxChars, PTSTR pszDomain, ULONG ulDomainMaxChars)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszUserName", "pszUser", "ulUserMaxChars", "pszDomain", "ulDomainMaxChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_CredUIPromptForCredentials(jitter):
    """"
    [Credui.dll] [ERROR_CODE] CredUIPromptForCredentials(PCREDUI_INFO pUiInfo, PCTSTR pszTargetName, PCtxtHandle Reserved, DWORD dwAuthError, PCTSTR pszUserName, ULONG ulUserNameMaxChars, PCTSTR pszPassword, ULONG ulPasswordMaxChars, PBOOL pfSave, [CredUIFlags] dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUiInfo", "pszTargetName", "Reserved", "dwAuthError", "pszUserName", "ulUserNameMaxChars", "pszPassword", "ulPasswordMaxChars", "pfSave", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_CredUIPromptForWindowsCredentials(jitter):
    """"
    [Credui.dll] [ERROR_CODE] CredUIPromptForWindowsCredentials(PCREDUI_INFO pUiInfo, DWORD dwAuthError, ULONG* pulAuthPackage, LPCVOID pvInAuthBuffer, ULONG ulInAuthBufferSize, LPVOID* ppvOutAuthBuffer, ULONG* pulOutAuthBufferSize, BOOL* pfSave, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pUiInfo", "dwAuthError", "pulAuthPackage", "pvInAuthBuffer", "ulInAuthBufferSize", "ppvOutAuthBuffer", "pulOutAuthBufferSize", "pfSave", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_CredUIReadSSOCredW(jitter):
    """"
    [Credui.dll] [ERROR_CODE] CredUIReadSSOCredW(PCWSTR pszRealm, PWSTR* ppszUsername)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszRealm", "ppszUsername"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_CredUIStoreSSOCredW(jitter):
    """"
    [Credui.dll] [ERROR_CODE] CredUIStoreSSOCredW(PCWSTR pszRealm, PCWSTR pszUsername, PCWSTR pszPassword, BOOL bPersist)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszRealm", "pszUsername", "pszPassword", "bPersist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_CredPackAuthenticationBuffer(jitter):
    """"
    [Credui.dll] BOOL CredPackAuthenticationBuffer(DWORD dwFlags, LPTSTR pszUserName, LPTSTR pszPassword, PBYTE pPackedCredentials, DWORD* pcbPackedCredentials)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pszUserName", "pszPassword", "pPackedCredentials", "pcbPackedCredentials"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_CredUnPackAuthenticationBuffer(jitter):
    """"
    [Credui.dll] BOOL CredUnPackAuthenticationBuffer(DWORD dwFlags, PVOID pAuthBuffer, DWORD cbAuthBuffer, LPTSTR pszUserName, DWORD* pcchMaxUserName, LPTSTR pszDomainName, DWORD* pcchMaxDomainame, LPTSTR pszPassword, DWORD* pcchMaxPassword)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pAuthBuffer", "cbAuthBuffer", "pszUserName", "pcchMaxUserName", "pszDomainName", "pcchMaxDomainame", "pszPassword", "pcchMaxPassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_SspiGetCredUIContext(jitter):
    """"
    [Credui.dll] SECURITY_STATUS SspiGetCredUIContext(HANDLE ContextHandle, GUID* CredType, LUID* LogonId, PSEC_WINNT_CREDUI_CONTEXT_VECTOR* CredUIContexts, HANDLE* TokenHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle", "CredType", "LogonId", "CredUIContexts", "TokenHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_SspiIsPromptingNeeded(jitter):
    """"
    [Credui.dll] BOOLEAN SspiIsPromptingNeeded(unsigned long ErrorOrNtStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ErrorOrNtStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_SspiPromptForCredentials(jitter):
    """"
    [Credui.dll] SECURITY_STATUS SspiPromptForCredentials(PCTSTR pszTargetName, PCREDUI_INFOW pUiInfo, DWORD dwAuthError, PCTSTR pszPackage, PSEC_WINNT_AUTH_IDENTITY_OPAQUE pInputAuthIdentity, PSEC_WINNT_AUTH_IDENTITY_OPAQUE* ppAuthIdentity, PBOOL pfSave, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszTargetName", "pUiInfo", "dwAuthError", "pszPackage", "pInputAuthIdentity", "ppAuthIdentity", "pfSave", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_SspiUnmarshalCredUIContext(jitter):
    """"
    [Credui.dll] SECURITY_STATUS SspiUnmarshalCredUIContext(PUCHAR MarshaledCredUIContext, ULONG MarshaledCredUIContextLength, PSEC_WINNT_CREDUI_CONTEXT* CredUIContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["MarshaledCredUIContext", "MarshaledCredUIContextLength", "CredUIContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def credui_SspiUpdateCredentials(jitter):
    """"
    [Credui.dll] SECURITY_STATUS SspiUpdateCredentials(HANDLE ContextHandle, GUID* CredType, ULONG FlatCredUIContextLength, PUCHAR FlatCredUIContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle", "CredType", "FlatCredUIContextLength", "FlatCredUIContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)