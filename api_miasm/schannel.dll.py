
def schannel_SslCrackCertificate(jitter):
    """"
    [Schannel.dll] BOOL SslCrackCertificate(PUCHAR pbCertificate, DWORD dwCertificate, DWORD dwFlags, PX509Certificate* ppCertificate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pbCertificate", "dwCertificate", "dwFlags", "ppCertificate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def schannel_SslEmptyCache(jitter):
    """"
    [Schannel.dll] BOOL SslEmptyCache(LPSTR pszTargetName, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszTargetName", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def schannel_SslFreeCertificate(jitter):
    """"
    [Schannel.dll] void SslFreeCertificate(PX509Certificate pCertificate)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pCertificate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def schannel_SslGetServerIdentity(jitter):
    """"
    [Schannel.dll] SECURITY_STATUS SslGetServerIdentity(PBYTE ClientHello, DWORD ClientHelloSize, PBYTE* ServerIdentity, PDWORD ServerIdentitySize, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ClientHello", "ClientHelloSize", "ServerIdentity", "ServerIdentitySize", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
