
def sxs_CreateAssemblyCache(jitter):
    """
    [SxS.dll] HRESULT CreateAssemblyCache(IAssemblyCache** ppAsmCache, DWORD dwReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppAsmCache", "dwReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def sxs_CreateAssemblyNameObject(jitter):
    """
    [SxS.dll] HRESULT CreateAssemblyNameObject(LPASSEMBLYNAME* ppAssemblyNameObj, LPCWSTR szAssemblyName, [CreateAsmNameObjFlags] dwFlags, LPVOID pvReserved)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppAssemblyNameObj", "szAssemblyName", "dwFlags", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
