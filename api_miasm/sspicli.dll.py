
def sspicli_SspiCompareAuthIdentities(jitter):
    """
    SECURITY_STATUS SspiCompareAuthIdentities(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity1,
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity2,
        PBOOLEAN SameSuppliedUser,
        PBOOLEAN SameSuppliedIdentity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity1", "AuthIdentity2", "SameSuppliedUser", "SameSuppliedIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiCopyAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiCopyAuthIdentity(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData,
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE* AuthDataCopy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData", "AuthDataCopy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiDecryptAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiDecryptAuthIdentity(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE EncryptedAuthData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EncryptedAuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiEncodeAuthIdentityAsStrings(jitter):
    """
    SECURITY_STATUS SspiEncodeAuthIdentityAsStrings(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE pAuthIdentity,
        PCWSTR* ppszUserName,
        PCWSTR* ppszDomainName,
        PCWSTR* ppszPackedCredentialsString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAuthIdentity", "ppszUserName", "ppszDomainName", "ppszPackedCredentialsString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiEncodeStringsAsAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiEncodeStringsAsAuthIdentity(
        PCWSTR pszUserName,
        PCWSTR pszDomainName,
        PCWSTR pszPackedCredentialsString,
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE* ppAuthIdentity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszUserName", "pszDomainName", "pszPackedCredentialsString", "ppAuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiEncryptAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiEncryptAuthIdentity(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiExcludePackage(jitter):
    """
    SECURITY_STATUS SspiExcludePackage(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity,
        PCWSTR pszPackageName,
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE* ppNewAuthIdentity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity", "pszPackageName", "ppNewAuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiFreeAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiFreeAuthIdentity(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiGetTargetHostName(jitter):
    """
    SECURITY_STATUS SspiGetTargetHostName(
        PCWSTR pszTargetName,
        PWSTR* pszHostName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszTargetName", "pszHostName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiIsAuthIdentityEncrypted(jitter):
    """
    BOOLEAN SspiIsAuthIdentityEncrypted(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE EncryptedAuthData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["EncryptedAuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiLocalFree(jitter):
    """
    VOID SspiLocalFree(
        PVOID DataBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DataBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiMarshalAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiMarshalAuthIdentity(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity,
        unsigned long* AuthIdentityLength,
        unsigned long* AuthIdentityByteArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity", "AuthIdentityLength", "AuthIdentityByteArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiPrepareForCredRead(jitter):
    """
    SECURITY_STATUS SspiPrepareForCredRead(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity,
        PCWSTR pszTargetName,
        PULONG pCredmanCredentialType,
        PCWSTR* ppszCredmanTargetName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity", "pszTargetName", "pCredmanCredentialType", "ppszCredmanTargetName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiPrepareForCredWrite(jitter):
    """
    SECURITY_STATUS SspiPrepareForCredWrite(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthIdentity,
        PCWSTR pszTargetName,
        PULONG pCredmanCredentialType,
        PCWSTR* ppszCredmanTargetName,
        PCWSTR* ppszCredmanUserName,
        PUCHAR* ppCredentialBlob,
        PULONG pCredentialBlobSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentity", "pszTargetName", "pCredmanCredentialType", "ppszCredmanTargetName", "ppszCredmanUserName", "ppCredentialBlob", "pCredentialBlobSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiUnmarshalAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiUnmarshalAuthIdentity(
        unsigned long AuthIdentityLength,
        char* AuthIdentityByteArray,
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE* ppAuthIdentity
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthIdentityLength", "AuthIdentityByteArray", "ppAuthIdentity"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiValidateAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiValidateAuthIdentity(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sspicli_SspiZeroAuthIdentity(jitter):
    """
    SECURITY_STATUS SspiZeroAuthIdentity(
        PSEC_WINNT_AUTH_IDENTITY_OPAQUE AuthData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AuthData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
