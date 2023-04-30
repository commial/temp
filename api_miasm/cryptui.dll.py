
def cryptui_CryptUIWizDigitalSign(jitter):
    """"
    [Cryptui.dll] BOOL CryptUIWizDigitalSign(DWORD dwFlags, HWND hwndParent, LPCWSTR pwszWizardTitle, PCCRYPTUI_WIZ_DIGITAL_SIGN_INFO pDigitalSignInfo, PCCRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT* ppSignContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hwndParent", "pwszWizardTitle", "pDigitalSignInfo", "ppSignContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIWizFreeDigitalSignContext(jitter):
    """"
    [Cryptui.dll] BOOL CryptUIWizFreeDigitalSignContext(PCCRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT pSignContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pSignContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIWizExport(jitter):
    """"
    [Cryptui.dll] BOOL CryptUIWizExport([CryptUiWizFlags] dwFlags, HWND hwndParent, LPCWSTR pwszWizardTitle, PCCRYPTUI_WIZ_EXPORT_INFO pExportInfo, void* pvoid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hwndParent", "pwszWizardTitle", "pExportInfo", "pvoid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIWizImport(jitter):
    """"
    [Cryptui.dll] BOOL CryptUIWizImport([CryptUiWizFlags] dwFlags, HWND hwndParent, LPCWSTR pwszWizardTitle, PCCRYPTUI_WIZ_IMPORT_SRC_INFO pImportSrc, HCERTSTORE hDestCertStore)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hwndParent", "pwszWizardTitle", "pImportSrc", "hDestCertStore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgCertMgr(jitter):
    """"
    [Cryptui.dll] BOOL CryptUIDlgCertMgr(PCCRYPTUI_CERT_MGR_STRUCT pCryptUICertMgr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCryptUICertMgr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgSelectCertificate(jitter):
    """"
    [Cryptui.dll] PCCERT_CONTEXT CryptUIDlgSelectCertificate(PCCRYPTUI_SELECTCERTIFICATE_STRUCT pcsc)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcsc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgSelectCertificateFromStore(jitter):
    """"
    [Cryptui.dll] PCCERT_CONTEXT CryptUIDlgSelectCertificateFromStore(HCERTSTORE hCertStore, HWND hwnd, LPCWSTR pwszTitle, LPCWSTR pwszDisplayString, DWORD dwDontUseColumn, DWORD dwFlags, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "hwnd", "pwszTitle", "pwszDisplayString", "dwDontUseColumn", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgViewCertificate(jitter):
    """"
    [Cryptui.dll] BOOL CryptUIDlgViewCertificate(PCCRYPTUI_VIEWCERTIFICATE_STRUCT pCertViewInfo, BOOL* pfPropertiesChanged)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertViewInfo", "pfPropertiesChanged"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgViewContext(jitter):
    """"
    [Cryptui.dll] BOOL CryptUIDlgViewContext(DWORD dwContextType, const void* pvContext, HWND hwnd, LPCWSTR pwszTitle, DWORD dwFlags, void* pvReserved)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwContextType", "pvContext", "hwnd", "pwszTitle", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgViewSignerInfo(jitter):
    """"
    [Cryptui.dll] BOOL CryptUIDlgViewSignerInfo(CRYPTUI_VIEWSIGNERINFO_STRUCT* pcvsi)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcvsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
