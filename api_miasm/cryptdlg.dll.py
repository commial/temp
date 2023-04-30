
def cryptdlg_CertSelectCertificate(jitter):
    """"
    [CryptDlg.dll] BOOL CertSelectCertificate(PCERT_SELECT_STRUCT pCertSelectInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertSelectInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptdlg_GetFriendlyNameOfCert(jitter):
    """"
    [CryptDlg.dll] DWORD GetFriendlyNameOfCert(PCCERT_CONTEXT pccert, LPTSTR pchBuffer, DWORD cchBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pccert", "pchBuffer", "cchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptdlg_CertModifyCertificatesToTrust(jitter):
    """"
    [CryptDlg.dll] HRESULT CertModifyCertificatesToTrust(int cCerts, PCTL_MODIFY_REQUEST rgCerts, LPCSTR szPurpose, HWND hwnd, HCERTSTORE hcertstoreTrust, PCCERT_CONTEXT pccertSigner)
    """"
    ret_ad, args = jitter.func_args_stdcall(["cCerts", "rgCerts", "szPurpose", "hwnd", "hcertstoreTrust", "pccertSigner"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
