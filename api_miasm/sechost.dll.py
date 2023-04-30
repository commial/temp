
def sechost_LookupAccountNameLocal(jitter):
    """"
    [Sechost.dll] BOOL LookupAccountNameLocal(LPCTSTR lpAccountName, PSID Sid, LPDWORD cbSid, LPTSTR ReferencedDomainName, LPDWORD cchReferencedDomainName, PSID_NAME_USE peUse)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAccountName", "Sid", "cbSid", "ReferencedDomainName", "cchReferencedDomainName", "peUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LookupAccountSidLocal(jitter):
    """"
    [Sechost.dll] BOOL LookupAccountSidLocal(PSID lpSid, LPTSTR lpName, LPDWORD cchName, LPTSTR lpReferencedDomainName, LPDWORD cchReferencedDomainName, PSID_NAME_USE peUse)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSid", "lpName", "cchName", "lpReferencedDomainName", "cchReferencedDomainName", "peUse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupClose(jitter):
    """"
    [Sechost.dll] NTSTATUS LsaLookupClose(LSA_LOOKUP_HANDLE ObjectHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupFreeMemory(jitter):
    """"
    [Sechost.dll] NTSTATUS LsaLookupFreeMemory(PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupGetDomainInfo(jitter):
    """"
    [Sechost.dll] NTSTATUS LsaLookupGetDomainInfo(LSA_LOOKUP_HANDLE PolicyHandle, LSA_LOOKUP_DOMAIN_INFO_CLASS DomainInfoClass, PVOID* DomainInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "DomainInfoClass", "DomainInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupOpenLocalPolicy(jitter):
    """"
    [Sechost.dll] NTSTATUS LsaLookupOpenLocalPolicy(PLSA_OBJECT_ATTRIBUTES ObjectAttributes, ACCESS_MASK AccessMask, PLSA_LOOKUP_HANDLE PolicyHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ObjectAttributes", "AccessMask", "PolicyHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupTranslateNames(jitter):
    """"
    [Sechost.dll] NTSTATUS LsaLookupTranslateNames(LSA_LOOKUP_HANDLE PolicyHandle, ULONG Flags, ULONG Count, PLSA_UNICODE_STRING Names, PLSA_REFERENCED_DOMAIN_LIST* ReferencedDomains, PLSA_TRANSLATED_SID2* Sids)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "Flags", "Count", "Names", "ReferencedDomains", "Sids"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sechost_LsaLookupTranslateSids(jitter):
    """"
    [Sechost.dll] NTSTATUS LsaLookupTranslateSids(LSA_LOOKUP_HANDLE PolicyHandle, ULONG Count, PSID* Sids, PLSA_REFERENCED_DOMAIN_LIST* ReferencedDomains, PLSA_TRANSLATED_NAME* Names)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PolicyHandle", "Count", "Sids", "ReferencedDomains", "Names"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
