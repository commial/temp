
def sspicli_SspiCompareAuthIdentities(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiCompareAuthIdentities(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity1, PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity2, PBOOLEAN SameSuppliedUser, PBOOLEAN SameSuppliedIdentity)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity1", "AuthIdentity2", "SameSuppliedUser", "SameSuppliedIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiCopyAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiCopyAuthIdentity(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData, PSEC_WINNT_AUTH_IDENTITY_OPAQUE* AuthDataCopy)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData", "AuthDataCopy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiDecryptAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiDecryptAuthIdentity(PSEC_WINNT_AUTH_IDENTITY_OPAQUE EncryptedAuthData)
    """
    ret_ad, args = jitter.func_args_stdcall(["EncryptedAuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiEncodeAuthIdentityAsStrings(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiEncodeAuthIdentityAsStrings(PSEC_WINNT_AUTH_IDENTITY_OPAQUE pAuthIdentity, PCWSTR* ppszUserName, PCWSTR* ppszDomainName, PCWSTR* ppszPackedCredentialsString)
    """
    ret_ad, args = jitter.func_args_stdcall(["pAuthIdentity", "ppszUserName", "ppszDomainName", "ppszPackedCredentialsString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiEncodeStringsAsAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiEncodeStringsAsAuthIdentity(PCWSTR pszUserName, PCWSTR pszDomainName, PCWSTR pszPackedCredentialsString, PSEC_WINNT_AUTH_IDENTITY_OPAQUE* ppAuthIdentity)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserName", "pszDomainName", "pszPackedCredentialsString", "ppAuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiEncryptAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiEncryptAuthIdentity(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiExcludePackage(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiExcludePackage(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity, PCWSTR pszPackageName, PSEC_WINNT_AUTH_IDENTITY_OPAQUE* ppNewAuthIdentity)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity", "pszPackageName", "ppNewAuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiFreeAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiFreeAuthIdentity(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiGetTargetHostName(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiGetTargetHostName(PCWSTR pszTargetName, PWSTR* pszHostName)
    """
    ret_ad, args = jitter.func_args_stdcall(["pszTargetName", "pszHostName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiIsAuthIdentityEncrypted(jitter):
    """
    [SspiCli.dll] BOOLEAN SspiIsAuthIdentityEncrypted(PSEC_WINNT_AUTH_IDENTITY_OPAQUE EncryptedAuthData)
    """
    ret_ad, args = jitter.func_args_stdcall(["EncryptedAuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiLocalFree(jitter):
    """
    [SspiCli.dll] VOID SspiLocalFree(PVOID DataBuffer)
    """
    ret_ad, args = jitter.func_args_stdcall(["DataBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiMarshalAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiMarshalAuthIdentity(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity, unsigned long* AuthIdentityLength, unsigned long* AuthIdentityByteArray)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity", "AuthIdentityLength", "AuthIdentityByteArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiPrepareForCredRead(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiPrepareForCredRead(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity, PCWSTR pszTargetName, PULONG pCredmanCredentialType, PCWSTR* ppszCredmanTargetName)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity", "pszTargetName", "pCredmanCredentialType", "ppszCredmanTargetName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiPrepareForCredWrite(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiPrepareForCredWrite(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity, PCWSTR pszTargetName, PULONG pCredmanCredentialType, PCWSTR* ppszCredmanTargetName, PCWSTR* ppszCredmanUserName, PUCHAR* ppCredentialBlob, PULONG pCredentialBlobSize)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity", "pszTargetName", "pCredmanCredentialType", "ppszCredmanTargetName", "ppszCredmanUserName", "ppCredentialBlob", "pCredentialBlobSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiUnmarshalAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiUnmarshalAuthIdentity(unsigned long AuthIdentityLength, char* AuthIdentityByteArray, PSEC_WINNT_AUTH_IDENTITY_OPAQUE* ppAuthIdentity)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentityLength", "AuthIdentityByteArray", "ppAuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiValidateAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiValidateAuthIdentity(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiZeroAuthIdentity(jitter):
    """
    [SspiCli.dll] SECURITY_STATUS SspiZeroAuthIdentity(PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData)
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
