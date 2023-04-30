
def normaliz_IdnToAscii(jitter):
    """"
    [Normaliz.dll] int IdnToAscii([IdnFlags] dwFlags, LPCWSTR lpUnicodeCharStr, int cchUnicodeChar, LPWSTR lpASCIICharStr, int cchASCIIChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpUnicodeCharStr", "cchUnicodeChar", "lpASCIICharStr", "cchASCIIChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def normaliz_IdnToNameprepUnicode(jitter):
    """"
    [Normaliz.dll] int IdnToNameprepUnicode([IdnFlags] dwFlags, LPCWSTR lpUnicodeCharStr, int cchUnicodeChar, LPWSTR lpNameprepCharStr, int cchNameprepChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpUnicodeCharStr", "cchUnicodeChar", "lpNameprepCharStr", "cchNameprepChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def normaliz_IdnToUnicode(jitter):
    """"
    [Normaliz.dll] int IdnToUnicode([IdnFlags] dwFlags, LPCWSTR lpASCIICharStr, int cchASCIIChar, LPWSTR lpUnicodeCharStr, int cchUnicodeChar)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "lpASCIICharStr", "cchASCIIChar", "lpUnicodeCharStr", "cchUnicodeChar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def normaliz_IsNormalizedString(jitter):
    """"
    [Normaliz.dll] BOOL IsNormalizedString(NORM_FORM NormForm, LPCWSTR lpString, int cwLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NormForm", "lpString", "cwLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def normaliz_NormalizeString(jitter):
    """"
    [Normaliz.dll] int NormalizeString(NORM_FORM NormForm, LPCWSTR lpSrcString, int cwSrcLength, LPWSTR lpDstString, int cwDstLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["NormForm", "lpSrcString", "cwSrcLength", "lpDstString", "cwDstLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
