LSA_LOOKUP_DOMAIN_INFO_CLASS = {
    "AccountDomainInformation": 5,
    "DnsDomainInformation": 12,
}
LSA_LOOKUP_DOMAIN_INFO_CLASS_INV = {
    5: "AccountDomainInformation",
    12: "DnsDomainInformation",
}

def sechost_LookupAccountNameLocal(jitter, get_str, set_str):
    """
    BOOL LookupAccountNameLocal(
        LPCTSTR lpAccountName,
        PSID Sid,
        LPDWORD cbSid,
        LPTSTR ReferencedDomainName,
        LPDWORD cchReferencedDomainName,
        PSID_NAME_USE peUse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpAccountName", "Sid", "cbSid", "ReferencedDomainName", "cchReferencedDomainName", "peUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LookupAccountNameLocalA(jitter):
    sechost_LookupAccountNameLocal(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def sechost_LookupAccountNameLocalW(jitter):
    sechost_LookupAccountNameLocal(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def sechost_LookupAccountSidLocal(jitter, get_str, set_str):
    """
    BOOL LookupAccountSidLocal(
        PSID lpSid,
        LPTSTR lpName,
        LPDWORD cchName,
        LPTSTR lpReferencedDomainName,
        LPDWORD cchReferencedDomainName,
        PSID_NAME_USE peUse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSid", "lpName", "cchName", "lpReferencedDomainName", "cchReferencedDomainName", "peUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LookupAccountSidLocalA(jitter):
    sechost_LookupAccountSidLocal(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def sechost_LookupAccountSidLocalW(jitter):
    sechost_LookupAccountSidLocal(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def sechost_LsaLookupClose(jitter):
    """
    NTSTATUS LsaLookupClose(
        LSA_LOOKUP_HANDLE ObjectHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupFreeMemory(jitter):
    """
    NTSTATUS LsaLookupFreeMemory(
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupGetDomainInfo(jitter):
    """
    NTSTATUS LsaLookupGetDomainInfo(
        LSA_LOOKUP_HANDLE PolicyHandle,
        LSA_LOOKUP_DOMAIN_INFO_CLASS DomainInfoClass,
        PVOID* DomainInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "DomainInfoClass", "DomainInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupOpenLocalPolicy(jitter):
    """
    NTSTATUS LsaLookupOpenLocalPolicy(
        PLSA_OBJECT_ATTRIBUTES ObjectAttributes,
        ACCESS_MASK AccessMask,
        PLSA_LOOKUP_HANDLE PolicyHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ObjectAttributes", "AccessMask", "PolicyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupTranslateNames(jitter):
    """
    NTSTATUS LsaLookupTranslateNames(
        LSA_LOOKUP_HANDLE PolicyHandle,
        ULONG Flags,
        ULONG Count,
        PLSA_UNICODE_STRING Names,
        PLSA_REFERENCED_DOMAIN_LIST* ReferencedDomains,
        PLSA_TRANSLATED_SID2* Sids
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "Flags", "Count", "Names", "ReferencedDomains", "Sids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupTranslateSids(jitter):
    """
    NTSTATUS LsaLookupTranslateSids(
        LSA_LOOKUP_HANDLE PolicyHandle,
        ULONG Count,
        PSID* Sids,
        PLSA_REFERENCED_DOMAIN_LIST* ReferencedDomains,
        PLSA_TRANSLATED_NAME* Names
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "Count", "Sids", "ReferencedDomains", "Names"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
