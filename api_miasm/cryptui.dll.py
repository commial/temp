###### Enums ######
_CRYPTUI_WIZ_IMPORT_SRC_INFO_CHOICE_ = {
    "CRYPTUI_WIZ_IMPORT_SUBJECT_FILE": 1,
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_CONTEXT": 2,
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CTL_CONTEXT": 3,
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CRL_CONTEXT": 4,
    "CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_STORE": 5,
}
_CRYPTUI_WIZ_IMPORT_SRC_INFO_CHOICE__INV = {
    1: "CRYPTUI_WIZ_IMPORT_SUBJECT_FILE",
    2: "CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_CONTEXT",
    3: "CRYPTUI_WIZ_IMPORT_SUBJECT_CTL_CONTEXT",
    4: "CRYPTUI_WIZ_IMPORT_SUBJECT_CRL_CONTEXT",
    5: "CRYPTUI_WIZ_IMPORT_SUBJECT_CERT_STORE",
}
_CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_CHOICE_ = {
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE": 0x01,
    "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_PROV": 0x02,
}
_CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_CHOICE__INV = {
    0x01: "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE",
    0x02: "CRYPTUI_WIZ_DIGITAL_SIGN_PVK_PROV",
}

###################

###### Types ######
PFNCFILTERPROC = LPVOID
PFNCCERTDISPLAYPROC = LPVOID
_CRYPTUI_WIZ_EXPORT_INFO_u_ = Union([
    ("pCertContext", PCCERT_CONTEXT),
    ("pCTLContext", PCCTL_CONTEXT),
    ("pCRLContext", PCCRL_CONTEXT),
    ("hCertStore", HCERTSTORE),
])

class CRYPTUI_WIZ_EXPORT_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("pwszExportFileName", LPCWSTR()),
        ("dwSubjectChoice", DWORD()),
        (None, _CRYPTUI_WIZ_EXPORT_INFO_u_()),
        ("cStores", DWORD()),
        ("rghStores", HCERTSTORE_PTR()),
    ]

PCCRYPTUI_WIZ_EXPORT_INFO = Ptr("<I", CRYPTUI_WIZ_EXPORT_INFO())
_CRYPTUI_WIZ_IMPORT_SRC_INFO_CHOICE_ = DWORD
_CRYPTUI_WIZ_IMPORT_SRC_INFO_u_ = Union([
    ("pwszFileName", LPCWSTR),
    ("pCertContext", PCCERT_CONTEXT),
    ("pCTLContext", PCCTL_CONTEXT),
    ("pCRLContext", PCCRL_CONTEXT),
    ("hCertStore", HCERTSTORE),
])

class CRYPTUI_WIZ_IMPORT_SRC_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("dwSubjectChoice", _CRYPTUI_WIZ_IMPORT_SRC_INFO_CHOICE_()),
        (None, _CRYPTUI_WIZ_IMPORT_SRC_INFO_u_()),
        ("dwFlags", DWORD()),
        ("pwszPassword", LPCWSTR()),
    ]

PCCRYPTUI_WIZ_IMPORT_SRC_INFO = Ptr("<I", CRYPTUI_WIZ_IMPORT_SRC_INFO())
_CRYPTUI_VIEWCERTIFICATE_STRUCT_u_ = Union([
    ("pCryptProviderData", CRYPT_PROVIDER_DATA_PTR),
    ("hWVTStateData", HANDLE),
])
_CRYPTUI_VIEWCERTIFICATE_STRUCT_FLAGS_ = DWORD

class CRYPTUI_VIEWCERTIFICATE_STRUCT(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndParent", HWND()),
        ("dwFlags", _CRYPTUI_VIEWCERTIFICATE_STRUCT_FLAGS_()),
        ("szTitle", LPCTSTR()),
        ("pCertContext", PCCERT_CONTEXT()),
        ("rgszPurposes", LPCSTR_PTR()),
        ("cPurposes", DWORD()),
        (None, _CRYPTUI_VIEWCERTIFICATE_STRUCT_u_()),
        ("fpCryptProviderDataTrustedUsage", BOOL()),
        ("idxSigner", DWORD()),
        ("idxCert", DWORD()),
        ("fCounterSigner", BOOL()),
        ("idxCounterSigner", DWORD()),
        ("cStores", DWORD()),
        ("rghStores", HCERTSTORE_PTR()),
        ("cPropSheetPages", DWORD()),
        ("rgPropSheetPages", LPCPROPSHEETPAGE()),
        ("nStartPage", DWORD()),
    ]

PCCRYPTUI_VIEWCERTIFICATE_STRUCT = Ptr("<I", CRYPTUI_VIEWCERTIFICATE_STRUCT())

class CRYPTUI_VIEWSIGNERINFO_STRUCT(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndParent", HWND()),
        ("dwFlags", DWORD()),
        ("szTitle", LPCTSTR()),
        ("pSignerInfo", CMSG_SIGNER_INFO_PTR()),
        ("hMsg", HCRYPTMSG()),
        ("pszOID", LPCSTR()),
        ("dwReserved", DWORD_PTR()),
        ("cStores", DWORD()),
        ("rghStores", HCERTSTORE_PTR()),
        ("cPropSheetPages", DWORD()),
        ("rgPropSheetPages", LPCPROPSHEETPAGE()),
    ]

CRYPTUI_VIEWSIGNERINFO_STRUCT_PTR = Ptr("<I", CRYPTUI_VIEWSIGNERINFO_STRUCT())
_CRYPTUI_SELECT_FLAGS_ = DWORD

class CRYPTUI_SELECTCERTIFICATE_STRUCT(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndParent", HWND()),
        ("dwFlags", DWORD()),
        ("szTitle", LPCTSTR()),
        ("dwDontUseColumn", _CRYPTUI_SELECT_FLAGS_()),
        ("szDisplayString", LPCTSTR()),
        ("pFilterCallback", PFNCFILTERPROC()),
        ("pDisplayCallback", PFNCCERTDISPLAYPROC()),
        ("pvCallbackData", void_PTR()),
        ("cDisplayStores", DWORD()),
        ("rghDisplayStores", HCERTSTORE_PTR()),
        ("cStores", DWORD()),
        ("rghStores", HCERTSTORE_PTR()),
        ("cPropSheetPages", DWORD()),
        ("rgPropSheetPages", LPCPROPSHEETPAGE()),
        ("hSelectedCertStore", HCERTSTORE()),
    ]

PCCRYPTUI_SELECTCERTIFICATE_STRUCT = Ptr("<I", CRYPTUI_SELECTCERTIFICATE_STRUCT())

class CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("pGuidSubject", GUID_PTR()),
        ("cbBlob", DWORD()),
        # Length is `cbBlob`
        ("pbBlob", BYTE_PTR()),
        ("pwszDisplayName", LPCWSTR()),
    ]

PCCRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO = Ptr("<I", CRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO())
_CRYPTUI_WIZ_DIGITAL_SIGN_INFO_u1_ = Union([
    ("pwszFileName", LPCWSTR),
    ("pSignBlobInfo", PCCRYPTUI_WIZ_DIGITAL_SIGN_BLOB_INFO),
])

class CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("cCertStore", DWORD()),
        ("rghCertStore", HCERTSTORE_PTR()),
        ("pFilterCallback", PFNCFILTERPROC()),
        ("pvCallbackData", void_PTR()),
    ]

PCCRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO = Ptr("<I", CRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO())

class CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("pwszPvkFileName", LPWSTR()),
        ("pwszProvName", LPWSTR()),
        ("dwProvType", _CryptProv_()),
    ]

PCCRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO = Ptr("<I", CRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO())
_CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_u_ = Union([
    ("pPvkFileInfo", PCCRYPTUI_WIZ_DIGITAL_SIGN_PVK_FILE_INFO),
    ("pPvkProvInfo", PCRYPT_KEY_PROV_INFO),
])
_CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_CHOICE_ = DWORD

class CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("pwszSigningCertFileName", LPWSTR()),
        ("dwPvkChoice", _CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_CHOICE_()),
        (None, _CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO_u_()),
    ]

PCCRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO = Ptr("<I", CRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO())
_CRYPTUI_WIZ_DIGITAL_SIGN_INFO_u2_ = Union([
    ("pSigningCertContext", PCCERT_CONTEXT),
    ("pSigningCertStore", PCCRYPTUI_WIZ_DIGITAL_SIGN_STORE_INFO),
    ("pSigningCertPvkInfo", PCCRYPTUI_WIZ_DIGITAL_SIGN_CERT_PVK_INFO),
])
_CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO_FLAGS_ = DWORD

class CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("dwAttrFlags", _CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO_FLAGS_()),
        ("pwszDescription", LPCWSTR()),
        ("pwszMoreInfoLocation", LPCWSTR()),
        ("pszHashAlg", LPCSTR()),
        ("pwszSigningCertDisplayString", LPCWSTR()),
        ("hAdditionalCertStore", HCERTSTORE()),
        ("psAuthenticated", PCRYPT_ATTRIBUTES()),
        ("psUnauthenticated", PCRYPT_ATTRIBUTES()),
    ]

PCCRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO = Ptr("<I", CRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO())

class CRYPTUI_WIZ_DIGITAL_SIGN_INFO(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("dwSubjectChoice", DWORD()),
        (None, _CRYPTUI_WIZ_DIGITAL_SIGN_INFO_u1_()),
        ("dwSigningCertChoice", DWORD()),
        (None, _CRYPTUI_WIZ_DIGITAL_SIGN_INFO_u2_()),
        ("pwszTimestampURL", LPCWSTR()),
        ("dwAdditionalCertChoice", DWORD()),
        ("pSignExtInfo", PCCRYPTUI_WIZ_DIGITAL_SIGN_EXTENDED_INFO()),
    ]

PCCRYPTUI_WIZ_DIGITAL_SIGN_INFO = Ptr("<I", CRYPTUI_WIZ_DIGITAL_SIGN_INFO())

class CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("cbBlob", DWORD()),
        # Length is `cbBlob`
        ("pbBlob", BYTE_PTR()),
    ]

PCCRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT = Ptr("<I", CRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT())
PCCRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT_PTR = Ptr("<I", PCCRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT())

class CRYPTUI_CERT_MGR_STRUCT(MemStruct):
    fields = [
        ("dwSize", DWORD()),
        ("hwndParent", HWND()),
        ("dwFlags", DWORD()),
        ("pwszTitle", LPCWSTR()),
        ("pszInitUsageOID", LPCSTR()),
    ]

PCCRYPTUI_CERT_MGR_STRUCT = Ptr("<I", CRYPTUI_CERT_MGR_STRUCT())
_CryptUiWizFlags_ = DWORD

###################

###### Functions ######

def cryptui_CryptUIWizDigitalSign(jitter):
    """
    BOOL CryptUIWizDigitalSign(
        DWORD dwFlags,
        HWND hwndParent,
        LPCWSTR pwszWizardTitle,
        PCCRYPTUI_WIZ_DIGITAL_SIGN_INFO pDigitalSignInfo,
        PCCRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT* ppSignContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hwndParent", "pwszWizardTitle", "pDigitalSignInfo", "ppSignContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIWizFreeDigitalSignContext(jitter):
    """
    BOOL CryptUIWizFreeDigitalSignContext(
        PCCRYPTUI_WIZ_DIGITAL_SIGN_CONTEXT pSignContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSignContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIWizExport(jitter):
    """
    BOOL CryptUIWizExport(
        [CryptUiWizFlags] dwFlags,
        HWND hwndParent,
        LPCWSTR pwszWizardTitle,
        PCCRYPTUI_WIZ_EXPORT_INFO pExportInfo,
        void* pvoid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hwndParent", "pwszWizardTitle", "pExportInfo", "pvoid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIWizImport(jitter):
    """
    BOOL CryptUIWizImport(
        [CryptUiWizFlags] dwFlags,
        HWND hwndParent,
        LPCWSTR pwszWizardTitle,
        PCCRYPTUI_WIZ_IMPORT_SRC_INFO pImportSrc,
        HCERTSTORE hDestCertStore
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "hwndParent", "pwszWizardTitle", "pImportSrc", "hDestCertStore"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgCertMgr(jitter):
    """
    BOOL CryptUIDlgCertMgr(
        PCCRYPTUI_CERT_MGR_STRUCT pCryptUICertMgr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCryptUICertMgr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgSelectCertificate(jitter, get_str, set_str):
    """
    PCCERT_CONTEXT CryptUIDlgSelectCertificate(
        PCCRYPTUI_SELECTCERTIFICATE_STRUCT pcsc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcsc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgSelectCertificateA(jitter):
    cryptui_CryptUIDlgSelectCertificate(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cryptui_CryptUIDlgSelectCertificateW(jitter):
    cryptui_CryptUIDlgSelectCertificate(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cryptui_CryptUIDlgSelectCertificateFromStore(jitter):
    """
    PCCERT_CONTEXT CryptUIDlgSelectCertificateFromStore(
        HCERTSTORE hCertStore,
        HWND hwnd,
        LPCWSTR pwszTitle,
        LPCWSTR pwszDisplayString,
        DWORD dwDontUseColumn,
        DWORD dwFlags,
        void* pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hCertStore", "hwnd", "pwszTitle", "pwszDisplayString", "dwDontUseColumn", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgViewCertificate(jitter, get_str, set_str):
    """
    BOOL CryptUIDlgViewCertificate(
        PCCRYPTUI_VIEWCERTIFICATE_STRUCT pCertViewInfo,
        BOOL* pfPropertiesChanged
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCertViewInfo", "pfPropertiesChanged"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgViewCertificateA(jitter):
    cryptui_CryptUIDlgViewCertificate(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cryptui_CryptUIDlgViewCertificateW(jitter):
    cryptui_CryptUIDlgViewCertificate(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def cryptui_CryptUIDlgViewContext(jitter):
    """
    BOOL CryptUIDlgViewContext(
        DWORD dwContextType,
        const void* pvContext,
        HWND hwnd,
        LPCWSTR pwszTitle,
        DWORD dwFlags,
        void* pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwContextType", "pvContext", "hwnd", "pwszTitle", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgViewSignerInfo(jitter, get_str, set_str):
    """
    BOOL CryptUIDlgViewSignerInfo(
        CRYPTUI_VIEWSIGNERINFO_STRUCT* pcvsi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcvsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def cryptui_CryptUIDlgViewSignerInfoA(jitter):
    cryptui_CryptUIDlgViewSignerInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def cryptui_CryptUIDlgViewSignerInfoW(jitter):
    cryptui_CryptUIDlgViewSignerInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
