
def msctf_SetInputScope(jitter):
    """
    [msctf.dll] HRESULT SetInputScope(HWND hwnd, InputScope inputscope)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "inputscope"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_SetInputScopes(jitter):
    """
    [msctf.dll] HRESULT SetInputScopes(HWND hwnd, const InputScope* pInputScopes, UINT cInputScopes, WCHAR** ppszPhraseList, UINT cPhrases, WCHAR* pszRegExp, WCHAR* pszSRGS)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pInputScopes", "cInputScopes", "ppszPhraseList", "cPhrases", "pszRegExp", "pszSRGS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_SetInputScopes2(jitter):
    """
    [msctf.dll] HRESULT SetInputScopes2(HWND hwnd, const InputScope* pInputScopes, UINT cInputScopes, IEnumString* pEnumString, WCHAR* pszRegExp, WCHAR* pszSRGS)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pInputScopes", "cInputScopes", "pEnumString", "pszRegExp", "pszSRGS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_SetInputScopeXML(jitter):
    """
    [msctf.dll] void SetInputScopeXML()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateCategoryMgr(jitter):
    """
    [msctf.dll] HRESULT TF_CreateCategoryMgr(ITfCategoryMgr** ppcat)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppcat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateDisplayAttributeMgr(jitter):
    """
    [msctf.dll] HRESULT TF_CreateDisplayAttributeMgr(ITfDisplayAttributeMgr** ppdam)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppdam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateInputProcessorProfiles(jitter):
    """
    [msctf.dll] HRESULT TF_CreateInputProcessorProfiles(ITfInputProcessorProfiles** ppipr)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppipr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateLangBarItemMgr(jitter):
    """
    [msctf.dll] HRESULT TF_CreateLangBarItemMgr(ITfLangBarItemMgr** pplbim)
    """
    ret_ad, args = jitter.func_args_stdcall(["pplbim"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateLangBarMgr(jitter):
    """
    [msctf.dll] HRESULT TF_CreateLangBarMgr(ITfLangBarMgr** pppbm)
    """
    ret_ad, args = jitter.func_args_stdcall(["pppbm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateThreadMgr(jitter):
    """
    [msctf.dll] HRESULT TF_CreateThreadMgr(ITfThreadMgr** pptim)
    """
    ret_ad, args = jitter.func_args_stdcall(["pptim"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_GetThreadMgr(jitter):
    """
    [msctf.dll] HRESULT TF_GetThreadMgr(ITfThreadMgr** pptim)
    """
    ret_ad, args = jitter.func_args_stdcall(["pptim"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_InvalidAssemblyListCacheIfExist(jitter):
    """
    [msctf.dll] HRESULT TF_InvalidAssemblyListCacheIfExist()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_MsimtfIsWindowFiltered(jitter):
    """
    [msctf.dll] BOOL MsimtfIsWindowFiltered(HWND hwnd)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
