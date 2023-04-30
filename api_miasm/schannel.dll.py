
def schannel_SslCrackCertificate(jitter):
    """
    BOOL SslCrackCertificate(
        PUCHAR pbCertificate,
        DWORD dwCertificate,
        DWORD dwFlags,
        PX509Certificate* ppCertificate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbCertificate", "dwCertificate", "dwFlags", "ppCertificate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def schannel_SslEmptyCache(jitter, get_str, set_str):
    """
    BOOL SslEmptyCache(
        LPSTR pszTargetName,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszTargetName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def schannel_SslEmptyCacheA(jitter):
    schannel_SslEmptyCache(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def schannel_SslEmptyCacheW(jitter):
    schannel_SslEmptyCache(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def schannel_SslFreeCertificate(jitter):
    """
    void SslFreeCertificate(
        PX509Certificate pCertificate
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCertificate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def schannel_SslGetServerIdentity(jitter):
    """
    SECURITY_STATUS SslGetServerIdentity(
        PBYTE ClientHello,
        DWORD ClientHelloSize,
        PBYTE* ServerIdentity,
        PDWORD ServerIdentitySize,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ClientHello", "ClientHelloSize", "ServerIdentity", "ServerIdentitySize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
