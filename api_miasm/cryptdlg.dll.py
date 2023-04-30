###### Enums ######

###################

###### Types ######
PFNCMHOOKPROC = LPVOID
PFNCMFILTERPROC = LPVOID

class CERT_SELECT_STRUCT(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndParent", HWND()),
        ("hInstance", HINSTANCE()),
        ("pTemplateName", LPCTSTR()),
        ("dwFlags", DWORD()),
        ("szTitle", LPCTSTR()),
        ("cCertStore", DWORD()),
        ("arrayCertStore", HCERTSTORE_PTR()),
        ("szPurposeOid", LPCTSTR()),
        ("cCertContext", DWORD()),
        ("arrayCertContext", PCCERT_CONTEXT_PTR()),
        ("lCustData", LPARAM()),
        ("pfnHook", PFNCMHOOKPROC()),
        ("pfnFilter", PFNCMFILTERPROC()),
        ("szHelpFileName", LPCTSTR()),
        ("dwHelpId", DWORD()),
        ("hprov", HCRYPTPROV()),
    ]

PCERT_SELECT_STRUCT = Ptr("<I", CERT_SELECT_STRUCT())

class CTL_MODIFY_REQUEST(MemStruct):
    fields = [
        ("pccert", PCCERT_CONTEXT()),
        ("dwOperation", DWORD()),
        ("dwError", DWORD()),
    ]

PCTL_MODIFY_REQUEST = Ptr("<I", CTL_MODIFY_REQUEST())

###################

###### Functions ######

def cryptdlg_CertSelectCertificate(jitter, get_str, set_str):
    """
    BOOL CertSelectCertificate(
        PCERT_SELECT_STRUCT pCertSelectInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCertSelectInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptdlg_CertSelectCertificateA(jitter):
    cryptdlg_CertSelectCertificate(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cryptdlg_CertSelectCertificateW(jitter):
    cryptdlg_CertSelectCertificate(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cryptdlg_GetFriendlyNameOfCert(jitter, get_str, set_str):
    """
    DWORD GetFriendlyNameOfCert(
        PCCERT_CONTEXT pccert,
        LPTSTR pchBuffer,
        DWORD cchBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pccert", "pchBuffer", "cchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptdlg_GetFriendlyNameOfCertA(jitter):
    cryptdlg_GetFriendlyNameOfCert(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cryptdlg_GetFriendlyNameOfCertW(jitter):
    cryptdlg_GetFriendlyNameOfCert(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cryptdlg_CertModifyCertificatesToTrust(jitter):
    """
    HRESULT CertModifyCertificatesToTrust(
        int cCerts,
        PCTL_MODIFY_REQUEST rgCerts,
        LPCSTR szPurpose,
        HWND hwnd,
        HCERTSTORE hcertstoreTrust,
        PCCERT_CONTEXT pccertSigner
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cCerts", "rgCerts", "szPurpose", "hwnd", "hcertstoreTrust", "pccertSigner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
