SECURITY_LOGON_TYPE = {
    "UndefinedLogonType": 0,
    "Interactive": 2,
    "Network": 3,
    "Batch": 4,
    "Service": 5,
    "Proxy": 6,
    "Unlock": 7,
    "NetworkCleartext": 8,
    "NewCredentials": 9,
    "RemoteInteractive": 10,
    "CachedInteractive": 11,
    "CachedRemoteInteractive": 12,
    "CachedUnlock": 13,
}
SECURITY_LOGON_TYPE_INV = {
    0: "UndefinedLogonType",
    2: "Interactive",
    3: "Network",
    4: "Batch",
    5: "Service",
    6: "Proxy",
    7: "Unlock",
    8: "NetworkCleartext",
    9: "NewCredentials",
    10: "RemoteInteractive",
    11: "CachedInteractive",
    12: "CachedRemoteInteractive",
    13: "CachedUnlock",
}
EXTENDED_NAME_FORMAT = {
    "NameUnknown": 0,
    "NameFullyQualifiedDN": 1,
    "NameSamCompatible": 2,
    "NameDisplay": 3,
    "NameUniqueId": 6,
    "NameCanonical": 7,
    "NameUserPrincipal": 8,
    "NameCanonicalEx": 9,
    "NameServicePrincipal": 10,
    "NameDnsDomain": 12,
}
EXTENDED_NAME_FORMAT_INV = {
    0: "NameUnknown",
    1: "NameFullyQualifiedDN",
    2: "NameSamCompatible",
    3: "NameDisplay",
    6: "NameUniqueId",
    7: "NameCanonical",
    8: "NameUserPrincipal",
    9: "NameCanonicalEx",
    10: "NameServicePrincipal",
    12: "NameDnsDomain",
}
POLICY_NOTIFICATION_INFORMATION_CLASS = {
    "PolicyNotifyAuditEventsInformation": 1,
    "PolicyNotifyAccountDomainInformation": 2,
    "PolicyNotifyServerRoleInformation": 3,
    "PolicyNotifyDnsDomainInformation": 4,
    "PolicyNotifyDomainEfsInformation": 5,
    "PolicyNotifyDomainKerberosTicketInformation": 6,
    "PolicyNotifyMachineAccountPasswordInformation": 7,
}
POLICY_NOTIFICATION_INFORMATION_CLASS_INV = {
    1: "PolicyNotifyAuditEventsInformation",
    2: "PolicyNotifyAccountDomainInformation",
    3: "PolicyNotifyServerRoleInformation",
    4: "PolicyNotifyDnsDomainInformation",
    5: "PolicyNotifyDomainEfsInformation",
    6: "PolicyNotifyDomainKerberosTicketInformation",
    7: "PolicyNotifyMachineAccountPasswordInformation",
}
_SecCredentialUse_ = {
    "SECPKG_CRED_INBOUND": 0x00000001,
    "SECPKG_CRED_OUTBOUND": 0x00000002,
    "SECPKG_CRED_BOTH": 0x00000003,
    "SECPKG_CRED_DEFAULT": 0x00000004,
    "SECPKG_CRED_RESERVED": 0xF0000000,
    "SECPKG_CRED_AUTOLOGON_RESTRICTED": 0x00000010,
    "SECPKG_CRED_PROCESS_POLICY_ONLY": 0x00000020,
}
_SecCredentialUse__INV = {
    0x00000001: "SECPKG_CRED_INBOUND",
    0x00000002: "SECPKG_CRED_OUTBOUND",
    0x00000003: "SECPKG_CRED_BOTH",
    0x00000004: "SECPKG_CRED_DEFAULT",
    0xF0000000: "SECPKG_CRED_RESERVED",
    0x00000010: "SECPKG_CRED_AUTOLOGON_RESTRICTED",
    0x00000020: "SECPKG_CRED_PROCESS_POLICY_ONLY",
}
_SecContextAttr_ = {
    "SECPKG_ATTR_SIZES": 0,
    "SECPKG_ATTR_NAMES": 1,
    "SECPKG_ATTR_LIFESPAN": 2,
    "SECPKG_ATTR_DCE_INFO": 3,
    "SECPKG_ATTR_STREAM_SIZES": 4,
    "SECPKG_ATTR_KEY_INFO": 5,
    "SECPKG_ATTR_AUTHORITY": 6,
    "SECPKG_ATTR_PROTO_INFO": 7,
    "SECPKG_ATTR_PASSWORD_EXPIRY": 8,
    "SECPKG_ATTR_SESSION_KEY": 9,
    "SECPKG_ATTR_PACKAGE_INFO": 10,
    "SECPKG_ATTR_USER_FLAGS": 11,
    "SECPKG_ATTR_NEGOTIATION_INFO": 12,
    "SECPKG_ATTR_NATIVE_NAMES": 13,
    "SECPKG_ATTR_FLAGS": 14,
    "SECPKG_ATTR_USE_VALIDATED": 15,
    "SECPKG_ATTR_CREDENTIAL_NAME": 16,
    "SECPKG_ATTR_TARGET_INFORMATION": 17,
    "SECPKG_ATTR_ACCESS_TOKEN": 18,
    "SECPKG_ATTR_TARGET": 19,
    "SECPKG_ATTR_AUTHENTICATION_ID": 20,
    "SECPKG_ATTR_LOGOFF_TIME": 21,
    "SECPKG_ATTR_NEGO_KEYS": 22,
    "SECPKG_ATTR_PROMPTING_NEEDED": 24,
    "SECPKG_ATTR_UNIQUE_BINDINGS": 25,
    "SECPKG_ATTR_ENDPOINT_BINDINGS": 26,
    "SECPKG_ATTR_CLIENT_SPECIFIED_TARGET": 27,
    "SECPKG_ATTR_LAST_CLIENT_TOKEN_STATUS": 30,
    "SECPKG_ATTR_NEGO_PKG_INFO": 31,
    "SECPKG_ATTR_NEGO_STATUS": 32,
    "SECPKG_ATTR_CONTEXT_DELETED": 33,
    "SECPKG_ATTR_ISSUER_LIST": 0x50,
    "SECPKG_ATTR_REMOTE_CRED": 0x51,
    "SECPKG_ATTR_LOCAL_CRED": 0x52,
    "SECPKG_ATTR_REMOTE_CERT_CONTEXT": 0x53,
    "SECPKG_ATTR_LOCAL_CERT_CONTEXT": 0x54,
    "SECPKG_ATTR_ROOT_STORE": 0x55,
    "SECPKG_ATTR_SUPPORTED_ALGS": 0x56,
    "SECPKG_ATTR_CIPHER_STRENGTHS": 0x57,
    "SECPKG_ATTR_SUPPORTED_PROTOCOLS": 0x58,
    "SECPKG_ATTR_ISSUER_LIST_EX": 0x59,
    "SECPKG_ATTR_CONNECTION_INFO": 0x5a,
    "SECPKG_ATTR_EAP_KEY_BLOCK": 0x5b,
    "SECPKG_ATTR_MAPPED_CRED_ATTR": 0x5c,
    "SECPKG_ATTR_SESSION_INFO": 0x5d,
    "SECPKG_ATTR_APP_DATA": 0x5e,
    "SECPKG_ATTR_REMOTE_CERTIFICATES": 0x5F,
    "SECPKG_ATTR_CLIENT_CERT_POLICY": 0x60,
    "SECPKG_ATTR_CC_POLICY_RESULT": 0x61,
    "SECPKG_ATTR_USE_NCRYPT": 0x62,
    "SECPKG_ATTR_LOCAL_CERT_INFO": 0x63,
    "SECPKG_ATTR_CIPHER_INFO": 0x64,
    "SECPKG_ATTR_EAP_PRF_INFO": 0x65,
    "SECPKG_ATTR_SUPPORTED_SIGNATURES": 0x66,
    "SECPKG_ATTR_SUBJECT_SECURITY_ATTRIBUTES": 128,
}
_SecContextAttr__INV = {
    0: "SECPKG_ATTR_SIZES",
    1: "SECPKG_ATTR_NAMES",
    2: "SECPKG_ATTR_LIFESPAN",
    3: "SECPKG_ATTR_DCE_INFO",
    4: "SECPKG_ATTR_STREAM_SIZES",
    5: "SECPKG_ATTR_KEY_INFO",
    6: "SECPKG_ATTR_AUTHORITY",
    7: "SECPKG_ATTR_PROTO_INFO",
    8: "SECPKG_ATTR_PASSWORD_EXPIRY",
    9: "SECPKG_ATTR_SESSION_KEY",
    10: "SECPKG_ATTR_PACKAGE_INFO",
    11: "SECPKG_ATTR_USER_FLAGS",
    12: "SECPKG_ATTR_NEGOTIATION_INFO",
    13: "SECPKG_ATTR_NATIVE_NAMES",
    14: "SECPKG_ATTR_FLAGS",
    15: "SECPKG_ATTR_USE_VALIDATED",
    16: "SECPKG_ATTR_CREDENTIAL_NAME",
    17: "SECPKG_ATTR_TARGET_INFORMATION",
    18: "SECPKG_ATTR_ACCESS_TOKEN",
    19: "SECPKG_ATTR_TARGET",
    20: "SECPKG_ATTR_AUTHENTICATION_ID",
    21: "SECPKG_ATTR_LOGOFF_TIME",
    22: "SECPKG_ATTR_NEGO_KEYS",
    24: "SECPKG_ATTR_PROMPTING_NEEDED",
    25: "SECPKG_ATTR_UNIQUE_BINDINGS",
    26: "SECPKG_ATTR_ENDPOINT_BINDINGS",
    27: "SECPKG_ATTR_CLIENT_SPECIFIED_TARGET",
    30: "SECPKG_ATTR_LAST_CLIENT_TOKEN_STATUS",
    31: "SECPKG_ATTR_NEGO_PKG_INFO",
    32: "SECPKG_ATTR_NEGO_STATUS",
    33: "SECPKG_ATTR_CONTEXT_DELETED",
    0x50: "SECPKG_ATTR_ISSUER_LIST",
    0x51: "SECPKG_ATTR_REMOTE_CRED",
    0x52: "SECPKG_ATTR_LOCAL_CRED",
    0x53: "SECPKG_ATTR_REMOTE_CERT_CONTEXT",
    0x54: "SECPKG_ATTR_LOCAL_CERT_CONTEXT",
    0x55: "SECPKG_ATTR_ROOT_STORE",
    0x56: "SECPKG_ATTR_SUPPORTED_ALGS",
    0x57: "SECPKG_ATTR_CIPHER_STRENGTHS",
    0x58: "SECPKG_ATTR_SUPPORTED_PROTOCOLS",
    0x59: "SECPKG_ATTR_ISSUER_LIST_EX",
    0x5a: "SECPKG_ATTR_CONNECTION_INFO",
    0x5b: "SECPKG_ATTR_EAP_KEY_BLOCK",
    0x5c: "SECPKG_ATTR_MAPPED_CRED_ATTR",
    0x5d: "SECPKG_ATTR_SESSION_INFO",
    0x5e: "SECPKG_ATTR_APP_DATA",
    0x5F: "SECPKG_ATTR_REMOTE_CERTIFICATES",
    0x60: "SECPKG_ATTR_CLIENT_CERT_POLICY",
    0x61: "SECPKG_ATTR_CC_POLICY_RESULT",
    0x62: "SECPKG_ATTR_USE_NCRYPT",
    0x63: "SECPKG_ATTR_LOCAL_CERT_INFO",
    0x64: "SECPKG_ATTR_CIPHER_INFO",
    0x65: "SECPKG_ATTR_EAP_PRF_INFO",
    0x66: "SECPKG_ATTR_SUPPORTED_SIGNATURES",
    128: "SECPKG_ATTR_SUBJECT_SECURITY_ATTRIBUTES",
}

def secur32_GetComputerObjectName(jitter, get_str, set_str):
    """
    BOOLEAN GetComputerObjectName(
        EXTENDED_NAME_FORMAT NameFormat,
        LPTSTR lpNameBuffer,
        PULONG lpnSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NameFormat", "lpNameBuffer", "lpnSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_GetComputerObjectNameA(jitter):
    secur32_GetComputerObjectName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_GetComputerObjectNameW(jitter):
    secur32_GetComputerObjectName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_GetUserNameEx(jitter, get_str, set_str):
    """
    BOOLEAN GetUserNameEx(
        EXTENDED_NAME_FORMAT NameFormat,
        LPTSTR lpNameBuffer,
        PULONG lpnSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NameFormat", "lpNameBuffer", "lpnSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_GetUserNameExA(jitter):
    secur32_GetUserNameEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_GetUserNameExW(jitter):
    secur32_GetUserNameEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_TranslateName(jitter, get_str, set_str):
    """
    BOOLEAN TranslateName(
        LPCTSTR lpAccountName,
        EXTENDED_NAME_FORMAT AccountNameFormat,
        EXTENDED_NAME_FORMAT DesiredNameFormat,
        LPTSTR lpTranslatedName,
        PULONG nSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpAccountName", "AccountNameFormat", "DesiredNameFormat", "lpTranslatedName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_TranslateNameA(jitter):
    secur32_TranslateName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_TranslateNameW(jitter):
    secur32_TranslateName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_EnumerateSecurityPackages(jitter, get_str, set_str):
    """
    SECURITY_STATUS EnumerateSecurityPackages(
        PULONG pcPackages,
        PSecPkgInfo* ppPackageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcPackages", "ppPackageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_EnumerateSecurityPackagesA(jitter):
    secur32_EnumerateSecurityPackages(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_EnumerateSecurityPackagesW(jitter):
    secur32_EnumerateSecurityPackages(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_InitSecurityInterface(jitter, get_str, set_str):
    """
    PSecurityFunctionTable InitSecurityInterface()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_InitSecurityInterfaceA(jitter):
    secur32_InitSecurityInterface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_InitSecurityInterfaceW(jitter):
    secur32_InitSecurityInterface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_QuerySecurityPackageInfo(jitter, get_str, set_str):
    """
    SECURITY_STATUS QuerySecurityPackageInfo(
        SEC_CHAR* pszPackageName,
        PSecPkgInfo* ppPackageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPackageName", "ppPackageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_QuerySecurityPackageInfoA(jitter):
    secur32_QuerySecurityPackageInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_QuerySecurityPackageInfoW(jitter):
    secur32_QuerySecurityPackageInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_AcquireCredentialsHandle(jitter, get_str, set_str):
    """
    SECURITY_STATUS AcquireCredentialsHandle(
        SEC_CHAR* pszPrincipal,
        SEC_CHAR* pszPackage,
        [SecCredentialUse] fCredentialUse,
        PLUID pvLogonID,
        PVOID pAuthData,
        SEC_GET_KEY_FN pGetKeyFn,
        PVOID pvGetKeyArgument,
        PCredHandle phCredential,
        PTimeStamp ptsExpiry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPrincipal", "pszPackage", "fCredentialUse", "pvLogonID", "pAuthData", "pGetKeyFn", "pvGetKeyArgument", "phCredential", "ptsExpiry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_AcquireCredentialsHandleA(jitter):
    secur32_AcquireCredentialsHandle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_AcquireCredentialsHandleW(jitter):
    secur32_AcquireCredentialsHandle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_ExportSecurityContext(jitter):
    """
    SECURITY_STATUS ExportSecurityContext(
        PCtxtHandle phContext,
        Ulong fFlags,
        PSecBuffer pPackedContext,
        HANDLE* pToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "fFlags", "pPackedContext", "pToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_FreeCredentialsHandle(jitter):
    """
    SECURITY_STATUS FreeCredentialsHandle(
        PCredHandle phCredential
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCredential"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ImportSecurityContext(jitter, get_str, set_str):
    """
    SECURITY_STATUS ImportSecurityContext(
        PSECURITY_STRING pszPackage,
        PSecBuffer pPackedContext,
        HANDLE pToken,
        PCtxtHandle phContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPackage", "pPackedContext", "pToken", "phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ImportSecurityContextA(jitter):
    secur32_ImportSecurityContext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_ImportSecurityContextW(jitter):
    secur32_ImportSecurityContext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_QueryCredentialsAttributes(jitter, get_str, set_str):
    """
    SECURITY_STATUS QueryCredentialsAttributes(
        PCredHandle phCredential,
        ULONG ulAttribute,
        PVOID pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "ulAttribute", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_QueryCredentialsAttributesA(jitter):
    secur32_QueryCredentialsAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_QueryCredentialsAttributesW(jitter):
    secur32_QueryCredentialsAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_AcceptSecurityContext(jitter):
    """
    SECURITY_STATUS AcceptSecurityContext(
        PCredHandle phCredential,
        PCtxtHandle phContext,
        PSecBufferDesc pInput,
        [AcceptSecurityContextRequestFlags] fContextReq,
        ULONG TargetDataRep,
        PCtxtHandle phNewContext,
        PSecBufferDesc pOutput,
        [AcceptSecurityContextRetFlags*] pfContextAttr,
        PTimeStamp ptsTimeStamp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "phContext", "pInput", "fContextReq", "TargetDataRep", "phNewContext", "pOutput", "pfContextAttr", "ptsTimeStamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ApplyControlToken(jitter):
    """
    SECURITY_STATUS ApplyControlToken(
        PCtxtHandle phContext,
        PSecBufferDesc pInput
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "pInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_CompleteAuthToken(jitter):
    """
    SECURITY_STATUS CompleteAuthToken(
        PCtxtHandle phContext,
        PSecBufferDesc pToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "pToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_DeleteSecurityContext(jitter):
    """
    SECURITY_STATUS DeleteSecurityContext(
        PCtxtHandle phContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_FreeContextBuffer(jitter):
    """
    SECURITY_STATUS FreeContextBuffer(
        PVOID pvContextBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvContextBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ImpersonateSecurityContext(jitter):
    """
    SECURITY_STATUS ImpersonateSecurityContext(
        PCtxtHandle phContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_InitializeSecurityContext(jitter, get_str, set_str):
    """
    SECURITY_STATUS InitializeSecurityContext(
        PCredHandle phCredential,
        PCtxtHandle phContext,
        SEC_CHAR* pszTargetName,
        [InitializeSecurityContextRequestFlags] fContextReq,
        ULONG Reserved1,
        ULONG TargetDataRep,
        PSecBufferDesc pInput,
        ULONG Reserved2,
        PCtxtHandle phNewContext,
        PSecBufferDesc pOutput,
        [InitializeSecurityContextRetFlags*] pfContextAttr,
        PTimeStamp ptsExpiry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "phContext", "pszTargetName", "fContextReq", "Reserved1", "TargetDataRep", "pInput", "Reserved2", "phNewContext", "pOutput", "pfContextAttr", "ptsExpiry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_InitializeSecurityContextA(jitter):
    secur32_InitializeSecurityContext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_InitializeSecurityContextW(jitter):
    secur32_InitializeSecurityContext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_QueryContextAttributes(jitter, get_str, set_str):
    """
    SECURITY_STATUS QueryContextAttributes(
        PCtxtHandle phContext,
        [SecContextAttr] ulAttribute,
        PVOID pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "ulAttribute", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_QueryContextAttributesA(jitter):
    secur32_QueryContextAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_QueryContextAttributesW(jitter):
    secur32_QueryContextAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_QuerySecurityContextToken(jitter):
    """
    SECURITY_STATUS QuerySecurityContextToken(
        PCtxtHandle phContext,
        HANDLE* phToken
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "phToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SetContextAttributes(jitter, get_str, set_str):
    """
    SECURITY_STATUS SetContextAttributes(
        PCtxtHandle phContext,
        [SecContextAttr] ulAttribute,
        void* pBuffer,
        ULONG cbBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "ulAttribute", "pBuffer", "cbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SetContextAttributesA(jitter):
    secur32_SetContextAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SetContextAttributesW(jitter):
    secur32_SetContextAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_RevertSecurityContext(jitter):
    """
    SECURITY_STATUS RevertSecurityContext(
        PCtxtHandle phContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_DecryptMessage(jitter):
    """
    SECURITY_STATUS DecryptMessage(
        PCtxtHandle phContext,
        PSecBufferDesc pMessage,
        ULONG MessageSeqNo,
        PULONG pfQOP
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "pMessage", "MessageSeqNo", "pfQOP"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_EncryptMessage(jitter):
    """
    SECURITY_STATUS EncryptMessage(
        PCtxtHandle phContext,
        ULONG fQOP,
        PSecBufferDesc pMessage,
        ULONG MessageSeqNo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "fQOP", "pMessage", "MessageSeqNo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_MakeSignature(jitter):
    """
    SECURITY_STATUS MakeSignature(
        PCtxtHandle phContext,
        ULONG fQOP,
        PSecBufferDesc pMessage,
        ULONG MessageSeqNo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "fQOP", "pMessage", "MessageSeqNo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_VerifySignature(jitter):
    """
    SECURITY_STATUS VerifySignature(
        PCtxtHandle phContext,
        PSecBufferDesc pMessage,
        ULONG MessageSeqNo,
        PULONG pfQOP
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phContext", "pMessage", "MessageSeqNo", "pfQOP"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaCallAuthenticationPackage(jitter):
    """
    NTSTATUS LsaCallAuthenticationPackage(
        HANDLE LsaHandle,
        ULONG AuthenticationPackage,
        PVOID ProtocolSubmitBuffer,
        ULONG SubmitBufferLength,
        PVOID* ProtocolReturnBuffer,
        PULONG ReturnBufferLength,
        PNTSTATUS ProtocolStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle", "AuthenticationPackage", "ProtocolSubmitBuffer", "SubmitBufferLength", "ProtocolReturnBuffer", "ReturnBufferLength", "ProtocolStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaConnectUntrusted(jitter):
    """
    NTSTATUS LsaConnectUntrusted(
        PHANDLE LsaHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaDeregisterLogonProcess(jitter):
    """
    NTSTATUS LsaDeregisterLogonProcess(
        HANDLE LsaHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaEnumerateLogonSessions(jitter):
    """
    NTSTATUS LsaEnumerateLogonSessions(
        PULONG LogonSessionCount,
        PLUID* LogonSessionList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogonSessionCount", "LogonSessionList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaFreeReturnBuffer(jitter):
    """
    NTSTATUS LsaFreeReturnBuffer(
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaGetLogonSessionData(jitter):
    """
    NTSTATUS LsaGetLogonSessionData(
        PLUID LogonId,
        PSECURITY_LOGON_SESSION_DATA* ppLogonSessionData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogonId", "ppLogonSessionData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaLogonUser(jitter):
    """
    NTSTATUS LsaLogonUser(
        HANDLE LsaHandle,
        PLSA_STRING OriginName,
        SECURITY_LOGON_TYPE LogonType,
        ULONG AuthenticationPackage,
        PVOID AuthenticationInformation,
        ULONG AuthenticationInformationLength,
        PTOKEN_GROUPS LocalGroups,
        PTOKEN_SOURCE SourceContext,
        PVOID* ProfileBuffer,
        PULONG ProfileBufferLength,
        PLUID LogonId,
        PHANDLE Token,
        PQUOTA_LIMITS Quotas,
        PNTSTATUS SubStatus
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle", "OriginName", "LogonType", "AuthenticationPackage", "AuthenticationInformation", "AuthenticationInformationLength", "LocalGroups", "SourceContext", "ProfileBuffer", "ProfileBufferLength", "LogonId", "Token", "Quotas", "SubStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaLookupAuthenticationPackage(jitter):
    """
    NTSTATUS LsaLookupAuthenticationPackage(
        HANDLE LsaHandle,
        PLSA_STRING PackageName,
        PULONG AuthenticationPackage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle", "PackageName", "AuthenticationPackage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaRegisterLogonProcess(jitter):
    """
    NTSTATUS LsaRegisterLogonProcess(
        PLSA_STRING LogonProcessName,
        PHANDLE LsaHandle,
        PLSA_OPERATIONAL_MODE SecurityMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LogonProcessName", "LsaHandle", "SecurityMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslAcceptSecurityContext(jitter):
    """
    SECURITY_STATUS SaslAcceptSecurityContext(
        PCredHandle phCredential,
        PCtxtHandle phContext,
        PSecBufferDesc pInput,
        [AcceptSecurityContextRequestFlags] fContextReq,
        unsigned long TargetDataRep,
        PCtxtHandle phNewContext,
        PSecBufferDesc pOutput,
        [AcceptSecurityContextRetFlags*] pfContextAttr,
        PTimeStamp ptsExpiry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "phContext", "pInput", "fContextReq", "TargetDataRep", "phNewContext", "pOutput", "pfContextAttr", "ptsExpiry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslEnumerateProfiles(jitter, get_str, set_str):
    """
    SECURITY_STATUS SaslEnumerateProfiles(
        LPTSTR* ProfileList,
        ULONG* ProfileCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileList", "ProfileCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslEnumerateProfilesA(jitter):
    secur32_SaslEnumerateProfiles(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SaslEnumerateProfilesW(jitter):
    secur32_SaslEnumerateProfiles(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_SaslGetContextOption(jitter):
    """
    SECURITY_STATUS SaslGetContextOption(
        PCtxtHandle ContextHandle,
        ULONG Option,
        PVOID Value,
        ULONG Size,
        PULONG Needed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle", "Option", "Value", "Size", "Needed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslGetProfilePackage(jitter, get_str, set_str):
    """
    SECURITY_STATUS SaslGetProfilePackage(
        LPTSTR ProfileName,
        PSecPkgInfo* PackageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ProfileName", "PackageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslGetProfilePackageA(jitter):
    secur32_SaslGetProfilePackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SaslGetProfilePackageW(jitter):
    secur32_SaslGetProfilePackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_SaslIdentifyPackage(jitter, get_str, set_str):
    """
    SECURITY_STATUS SaslIdentifyPackage(
        PSecBufferDesc pInput,
        PSecPkgInfo* PackageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pInput", "PackageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslIdentifyPackageA(jitter):
    secur32_SaslIdentifyPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SaslIdentifyPackageW(jitter):
    secur32_SaslIdentifyPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_SaslInitializeSecurityContext(jitter, get_str, set_str):
    """
    SECURITY_STATUS SaslInitializeSecurityContext(
        PCredHandle phCredential,
        PCtxtHandle phContext,
        LPTSTR pszTargetName,
        [InitializeSecurityContextRequestFlags] fContextReq,
        unsigned long Reserved1,
        unsigned long TargetDataRep,
        PSecBufferDesc pInput,
        unsigned long Reserved2,
        PCtxtHandle phNewContext,
        PSecBufferDesc pOutput,
        [InitializeSecurityContextRetFlags-unsigned-long*] pfContextAttr,
        PTimeStamp ptsExpiry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "phContext", "pszTargetName", "fContextReq", "Reserved1", "TargetDataRep", "pInput", "Reserved2", "phNewContext", "pOutput", "pfContextAttr", "ptsExpiry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslInitializeSecurityContextA(jitter):
    secur32_SaslInitializeSecurityContext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SaslInitializeSecurityContextW(jitter):
    secur32_SaslInitializeSecurityContext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_SaslSetContextOption(jitter):
    """
    SECURITY_STATUS SaslSetContextOption(
        PCtxtHandle ContextHandle,
        ULONG Option,
        PVOID Value,
        ULONG Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle", "Option", "Value", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_AddSecurityPackage(jitter, get_str, set_str):
    """
    SECURITY_STATUS AddSecurityPackage(
        LPTSTR pszPackageName,
        PSECURITY_PACKAGE_OPTIONS pOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPackageName", "pOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_AddSecurityPackageA(jitter):
    secur32_AddSecurityPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_AddSecurityPackageW(jitter):
    secur32_AddSecurityPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_ChangeAccountPassword(jitter, get_str, set_str):
    """
    SECURITY_STATUS ChangeAccountPassword(
        SEC_WCHAR* pszPackageName,
        SEC_WCHAR* pszDomainName,
        SEC_WCHAR* pszAccountName,
        SEC_WCHAR* pszOldPassword,
        SEC_WCHAR* pszNewPassword,
        BOOLEAN bImpersonating,
        unsigned long dwReserved,
        PSecBufferDesc pOutput
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPackageName", "pszDomainName", "pszAccountName", "pszOldPassword", "pszNewPassword", "bImpersonating", "dwReserved", "pOutput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ChangeAccountPasswordA(jitter):
    secur32_ChangeAccountPassword(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_ChangeAccountPasswordW(jitter):
    secur32_ChangeAccountPassword(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_DeleteSecurityPackage(jitter, get_str, set_str):
    """
    SECURITY_STATUS DeleteSecurityPackage(
        LPTSTR pszPackageName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszPackageName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_DeleteSecurityPackageA(jitter):
    secur32_DeleteSecurityPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_DeleteSecurityPackageW(jitter):
    secur32_DeleteSecurityPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_LsaRegisterPolicyChangeNotification(jitter):
    """
    NTSTATUS LsaRegisterPolicyChangeNotification(
        POLICY_NOTIFICATION_INFORMATION_CLASS InformationClass,
        HANDLE NotificationEventHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InformationClass", "NotificationEventHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaUnregisterPolicyChangeNotification(jitter):
    """
    NTSTATUS LsaUnregisterPolicyChangeNotification(
        POLICY_NOTIFICATION_INFORMATION_CLASS InformationClass,
        HANDLE NotificationEventHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InformationClass", "NotificationEventHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
