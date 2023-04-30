
def secur32_GetComputerObjectName(jitter, get_str, set_str):
    """"
    [Secur32.dll] BOOLEAN GetComputerObjectName(EXTENDED_NAME_FORMAT NameFormat, LPTSTR lpNameBuffer, PULONG lpnSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NameFormat", "lpNameBuffer", "lpnSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_GetComputerObjectNameA(jitter):
    secur32_GetComputerObjectName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_GetComputerObjectNameW(jitter):
    secur32_GetComputerObjectName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_GetUserNameEx(jitter, get_str, set_str):
    """"
    [Secur32.dll] BOOLEAN GetUserNameEx(EXTENDED_NAME_FORMAT NameFormat, LPTSTR lpNameBuffer, PULONG lpnSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NameFormat", "lpNameBuffer", "lpnSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_GetUserNameExA(jitter):
    secur32_GetUserNameEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_GetUserNameExW(jitter):
    secur32_GetUserNameEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_TranslateName(jitter, get_str, set_str):
    """"
    [Secur32.dll] BOOLEAN TranslateName(LPCTSTR lpAccountName, EXTENDED_NAME_FORMAT AccountNameFormat, EXTENDED_NAME_FORMAT DesiredNameFormat, LPTSTR lpTranslatedName, PULONG nSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpAccountName", "AccountNameFormat", "DesiredNameFormat", "lpTranslatedName", "nSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_TranslateNameA(jitter):
    secur32_TranslateName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_TranslateNameW(jitter):
    secur32_TranslateName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_EnumerateSecurityPackages(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS EnumerateSecurityPackages(PULONG pcPackages, PSecPkgInfo* ppPackageInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcPackages", "ppPackageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_EnumerateSecurityPackagesA(jitter):
    secur32_EnumerateSecurityPackages(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_EnumerateSecurityPackagesW(jitter):
    secur32_EnumerateSecurityPackages(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_InitSecurityInterface(jitter, get_str, set_str):
    """"
    [Secur32.dll] PSecurityFunctionTable InitSecurityInterface()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_InitSecurityInterfaceA(jitter):
    secur32_InitSecurityInterface(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_InitSecurityInterfaceW(jitter):
    secur32_InitSecurityInterface(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_QuerySecurityPackageInfo(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS QuerySecurityPackageInfo(SEC_CHAR* pszPackageName, PSecPkgInfo* ppPackageInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPackageName", "ppPackageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_QuerySecurityPackageInfoA(jitter):
    secur32_QuerySecurityPackageInfo(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_QuerySecurityPackageInfoW(jitter):
    secur32_QuerySecurityPackageInfo(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_AcquireCredentialsHandle(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS AcquireCredentialsHandle(SEC_CHAR* pszPrincipal, SEC_CHAR* pszPackage, [SecCredentialUse] fCredentialUse, PLUID pvLogonID, PVOID pAuthData, SEC_GET_KEY_FN pGetKeyFn, PVOID pvGetKeyArgument, PCredHandle phCredential, PTimeStamp ptsExpiry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPrincipal", "pszPackage", "fCredentialUse", "pvLogonID", "pAuthData", "pGetKeyFn", "pvGetKeyArgument", "phCredential", "ptsExpiry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_AcquireCredentialsHandleA(jitter):
    secur32_AcquireCredentialsHandle(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_AcquireCredentialsHandleW(jitter):
    secur32_AcquireCredentialsHandle(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_ExportSecurityContext(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS ExportSecurityContext(PCtxtHandle phContext, Ulong fFlags, PSecBuffer pPackedContext, HANDLE* pToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "fFlags", "pPackedContext", "pToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_FreeCredentialsHandle(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS FreeCredentialsHandle(PCredHandle phCredential)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phCredential"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ImportSecurityContext(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS ImportSecurityContext(PSECURITY_STRING pszPackage, PSecBuffer pPackedContext, HANDLE pToken, PCtxtHandle phContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPackage", "pPackedContext", "pToken", "phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ImportSecurityContextA(jitter):
    secur32_ImportSecurityContext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_ImportSecurityContextW(jitter):
    secur32_ImportSecurityContext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_QueryCredentialsAttributes(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS QueryCredentialsAttributes(PCredHandle phCredential, ULONG ulAttribute, PVOID pBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "ulAttribute", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_QueryCredentialsAttributesA(jitter):
    secur32_QueryCredentialsAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_QueryCredentialsAttributesW(jitter):
    secur32_QueryCredentialsAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_AcceptSecurityContext(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS AcceptSecurityContext(PCredHandle phCredential, PCtxtHandle phContext, PSecBufferDesc pInput, [AcceptSecurityContextRequestFlags] fContextReq, ULONG TargetDataRep, PCtxtHandle phNewContext, PSecBufferDesc pOutput, [AcceptSecurityContextRetFlags*] pfContextAttr, PTimeStamp ptsTimeStamp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "phContext", "pInput", "fContextReq", "TargetDataRep", "phNewContext", "pOutput", "pfContextAttr", "ptsTimeStamp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ApplyControlToken(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS ApplyControlToken(PCtxtHandle phContext, PSecBufferDesc pInput)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "pInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_CompleteAuthToken(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS CompleteAuthToken(PCtxtHandle phContext, PSecBufferDesc pToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "pToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_DeleteSecurityContext(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS DeleteSecurityContext(PCtxtHandle phContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_FreeContextBuffer(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS FreeContextBuffer(PVOID pvContextBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pvContextBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ImpersonateSecurityContext(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS ImpersonateSecurityContext(PCtxtHandle phContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_InitializeSecurityContext(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS InitializeSecurityContext(PCredHandle phCredential, PCtxtHandle phContext, SEC_CHAR* pszTargetName, [InitializeSecurityContextRequestFlags] fContextReq, ULONG Reserved1, ULONG TargetDataRep, PSecBufferDesc pInput, ULONG Reserved2, PCtxtHandle phNewContext, PSecBufferDesc pOutput, [InitializeSecurityContextRetFlags*] pfContextAttr, PTimeStamp ptsExpiry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "phContext", "pszTargetName", "fContextReq", "Reserved1", "TargetDataRep", "pInput", "Reserved2", "phNewContext", "pOutput", "pfContextAttr", "ptsExpiry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_InitializeSecurityContextA(jitter):
    secur32_InitializeSecurityContext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_InitializeSecurityContextW(jitter):
    secur32_InitializeSecurityContext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_QueryContextAttributes(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS QueryContextAttributes(PCtxtHandle phContext, [SecContextAttr] ulAttribute, PVOID pBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "ulAttribute", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_QueryContextAttributesA(jitter):
    secur32_QueryContextAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_QueryContextAttributesW(jitter):
    secur32_QueryContextAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_QuerySecurityContextToken(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS QuerySecurityContextToken(PCtxtHandle phContext, HANDLE* phToken)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "phToken"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SetContextAttributes(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS SetContextAttributes(PCtxtHandle phContext, [SecContextAttr] ulAttribute, void* pBuffer, ULONG cbBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "ulAttribute", "pBuffer", "cbBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SetContextAttributesA(jitter):
    secur32_SetContextAttributes(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SetContextAttributesW(jitter):
    secur32_SetContextAttributes(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_RevertSecurityContext(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS RevertSecurityContext(PCtxtHandle phContext)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_DecryptMessage(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS DecryptMessage(PCtxtHandle phContext, PSecBufferDesc pMessage, ULONG MessageSeqNo, PULONG pfQOP)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "pMessage", "MessageSeqNo", "pfQOP"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_EncryptMessage(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS EncryptMessage(PCtxtHandle phContext, ULONG fQOP, PSecBufferDesc pMessage, ULONG MessageSeqNo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "fQOP", "pMessage", "MessageSeqNo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_MakeSignature(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS MakeSignature(PCtxtHandle phContext, ULONG fQOP, PSecBufferDesc pMessage, ULONG MessageSeqNo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "fQOP", "pMessage", "MessageSeqNo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_VerifySignature(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS VerifySignature(PCtxtHandle phContext, PSecBufferDesc pMessage, ULONG MessageSeqNo, PULONG pfQOP)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phContext", "pMessage", "MessageSeqNo", "pfQOP"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaCallAuthenticationPackage(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaCallAuthenticationPackage(HANDLE LsaHandle, ULONG AuthenticationPackage, PVOID ProtocolSubmitBuffer, ULONG SubmitBufferLength, PVOID* ProtocolReturnBuffer, PULONG ReturnBufferLength, PNTSTATUS ProtocolStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle", "AuthenticationPackage", "ProtocolSubmitBuffer", "SubmitBufferLength", "ProtocolReturnBuffer", "ReturnBufferLength", "ProtocolStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaConnectUntrusted(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaConnectUntrusted(PHANDLE LsaHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaDeregisterLogonProcess(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaDeregisterLogonProcess(HANDLE LsaHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaEnumerateLogonSessions(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaEnumerateLogonSessions(PULONG LogonSessionCount, PLUID* LogonSessionList)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogonSessionCount", "LogonSessionList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaFreeReturnBuffer(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaFreeReturnBuffer(PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaGetLogonSessionData(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaGetLogonSessionData(PLUID LogonId, PSECURITY_LOGON_SESSION_DATA* ppLogonSessionData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogonId", "ppLogonSessionData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaLogonUser(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaLogonUser(HANDLE LsaHandle, PLSA_STRING OriginName, SECURITY_LOGON_TYPE LogonType, ULONG AuthenticationPackage, PVOID AuthenticationInformation, ULONG AuthenticationInformationLength, PTOKEN_GROUPS LocalGroups, PTOKEN_SOURCE SourceContext, PVOID* ProfileBuffer, PULONG ProfileBufferLength, PLUID LogonId, PHANDLE Token, PQUOTA_LIMITS Quotas, PNTSTATUS SubStatus)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle", "OriginName", "LogonType", "AuthenticationPackage", "AuthenticationInformation", "AuthenticationInformationLength", "LocalGroups", "SourceContext", "ProfileBuffer", "ProfileBufferLength", "LogonId", "Token", "Quotas", "SubStatus"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaLookupAuthenticationPackage(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaLookupAuthenticationPackage(HANDLE LsaHandle, PLSA_STRING PackageName, PULONG AuthenticationPackage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LsaHandle", "PackageName", "AuthenticationPackage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaRegisterLogonProcess(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaRegisterLogonProcess(PLSA_STRING LogonProcessName, PHANDLE LsaHandle, PLSA_OPERATIONAL_MODE SecurityMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LogonProcessName", "LsaHandle", "SecurityMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslAcceptSecurityContext(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS SaslAcceptSecurityContext(PCredHandle phCredential, PCtxtHandle phContext, PSecBufferDesc pInput, [AcceptSecurityContextRequestFlags] fContextReq, unsigned long TargetDataRep, PCtxtHandle phNewContext, PSecBufferDesc pOutput, [AcceptSecurityContextRetFlags*] pfContextAttr, PTimeStamp ptsExpiry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "phContext", "pInput", "fContextReq", "TargetDataRep", "phNewContext", "pOutput", "pfContextAttr", "ptsExpiry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslEnumerateProfiles(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS SaslEnumerateProfiles(LPTSTR* ProfileList, ULONG* ProfileCount)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProfileList", "ProfileCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslEnumerateProfilesA(jitter):
    secur32_SaslEnumerateProfiles(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SaslEnumerateProfilesW(jitter):
    secur32_SaslEnumerateProfiles(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_SaslGetContextOption(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS SaslGetContextOption(PCtxtHandle ContextHandle, ULONG Option, PVOID Value, ULONG Size, PULONG Needed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle", "Option", "Value", "Size", "Needed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslGetProfilePackage(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS SaslGetProfilePackage(LPTSTR ProfileName, PSecPkgInfo* PackageInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ProfileName", "PackageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslGetProfilePackageA(jitter):
    secur32_SaslGetProfilePackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SaslGetProfilePackageW(jitter):
    secur32_SaslGetProfilePackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_SaslIdentifyPackage(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS SaslIdentifyPackage(PSecBufferDesc pInput, PSecPkgInfo* PackageInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pInput", "PackageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslIdentifyPackageA(jitter):
    secur32_SaslIdentifyPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SaslIdentifyPackageW(jitter):
    secur32_SaslIdentifyPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_SaslInitializeSecurityContext(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS SaslInitializeSecurityContext(PCredHandle phCredential, PCtxtHandle phContext, LPTSTR pszTargetName, [InitializeSecurityContextRequestFlags] fContextReq, unsigned long Reserved1, unsigned long TargetDataRep, PSecBufferDesc pInput, unsigned long Reserved2, PCtxtHandle phNewContext, PSecBufferDesc pOutput, [InitializeSecurityContextRetFlags-unsigned-long*] pfContextAttr, PTimeStamp ptsExpiry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["phCredential", "phContext", "pszTargetName", "fContextReq", "Reserved1", "TargetDataRep", "pInput", "Reserved2", "phNewContext", "pOutput", "pfContextAttr", "ptsExpiry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_SaslInitializeSecurityContextA(jitter):
    secur32_SaslInitializeSecurityContext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_SaslInitializeSecurityContextW(jitter):
    secur32_SaslInitializeSecurityContext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_SaslSetContextOption(jitter):
    """"
    [Secur32.dll] SECURITY_STATUS SaslSetContextOption(PCtxtHandle ContextHandle, ULONG Option, PVOID Value, ULONG Size)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle", "Option", "Value", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_AddSecurityPackage(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS AddSecurityPackage(LPTSTR pszPackageName, PSECURITY_PACKAGE_OPTIONS pOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPackageName", "pOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_AddSecurityPackageA(jitter):
    secur32_AddSecurityPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_AddSecurityPackageW(jitter):
    secur32_AddSecurityPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_ChangeAccountPassword(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS ChangeAccountPassword(SEC_WCHAR* pszPackageName, SEC_WCHAR* pszDomainName, SEC_WCHAR* pszAccountName, SEC_WCHAR* pszOldPassword, SEC_WCHAR* pszNewPassword, BOOLEAN bImpersonating, unsigned long dwReserved, PSecBufferDesc pOutput)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPackageName", "pszDomainName", "pszAccountName", "pszOldPassword", "pszNewPassword", "bImpersonating", "dwReserved", "pOutput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_ChangeAccountPasswordA(jitter):
    secur32_ChangeAccountPassword(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_ChangeAccountPasswordW(jitter):
    secur32_ChangeAccountPassword(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_DeleteSecurityPackage(jitter, get_str, set_str):
    """"
    [Secur32.dll] SECURITY_STATUS DeleteSecurityPackage(LPTSTR pszPackageName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPackageName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_DeleteSecurityPackageA(jitter):
    secur32_DeleteSecurityPackage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def secur32_DeleteSecurityPackageW(jitter):
    secur32_DeleteSecurityPackage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def secur32_LsaRegisterPolicyChangeNotification(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaRegisterPolicyChangeNotification(POLICY_NOTIFICATION_INFORMATION_CLASS InformationClass, HANDLE NotificationEventHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InformationClass", "NotificationEventHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def secur32_LsaUnregisterPolicyChangeNotification(jitter):
    """"
    [Secur32.dll] NTSTATUS LsaUnregisterPolicyChangeNotification(POLICY_NOTIFICATION_INFORMATION_CLASS InformationClass, HANDLE NotificationEventHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InformationClass", "NotificationEventHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
