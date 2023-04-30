
def query_CIState(jitter):
    """
    [query.dll] STDAPI CIState(WCHAR const* pwcsCat, WCHAR const* pwcsMachine, CI_STATE* pCiState)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsCat", "pwcsMachine", "pCiState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_LocateCatalogs(jitter, get_str, set_str):
    """
    [query.dll] STDAPI LocateCatalogs(TCHAR const* pwszScope, ULONG iBmk, TCHAR* pwszMachine, ULONG* pcMachine, TCHAR* pwszCat, ULONG* pcCat)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszScope", "iBmk", "pwszMachine", "pcMachine", "pwszCat", "pcCat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_LocateCatalogsA(jitter):
    query_LocateCatalogs(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def query_LocateCatalogsW(jitter):
    query_LocateCatalogs(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def query_SetCatalogState(jitter):
    """
    [query.dll] STDAPI SetCatalogState(WCHAR const* pwcsCat, WCHAR const* pwcsMachine, DWORD dwNewState, DWORD* pdwOldState)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsCat", "pwcsMachine", "dwNewState", "pdwOldState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CICreateCommand(jitter):
    """
    [query.dll] STDAPI CICreateCommand(IUnknown** ppICommand, IUnknown* pUnkOuter, REFIID riid, WCHAR const* pwcsCatalog, WCHAR const* pwcsMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppICommand", "pUnkOuter", "riid", "pwcsCatalog", "pwcsMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CIMakeICommand(jitter):
    """
    [query.dll] STDAPI CIMakeICommand(ICommand** ppCommand, ULONG cScope, DWORD const* aDepths, WCHAR const* const* awcsScope, WCHAR const* const* awcsCatalogs, WCHAR const* const* awcsMachine)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppCommand", "cScope", "aDepths", "awcsScope", "awcsCatalogs", "awcsMachine"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CIBuildQueryNode(jitter):
    """
    [query.dll] STDAPI CIBuildQueryNode(WCHAR const* wcsProperty, DBCOMMANDOP dbOperator, PROPVARIANT const* pvarPropertyValue, DBCOMMANDTREE** ppTree, ULONG cProperties, CIPROPERTYDEF const* pProperty, LCID LocaleID)
    """
    ret_ad, args = jitter.func_args_stdcall(["wcsProperty", "dbOperator", "pvarPropertyValue", "ppTree", "cProperties", "pProperty", "LocaleID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CIBuildQueryTree(jitter):
    """
    [query.dll] STDAPI CIBuildQueryTree(DBCOMMANDTREE const* pExistingTree, ULONG cSiblings, DBCOMMANDTREE const* const* ppSibsToCombine, DBCOMMANDTREE** ppTree)
    """
    ret_ad, args = jitter.func_args_stdcall(["pExistingTree", "cSiblings", "ppSibsToCombine", "ppTree"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CIRestrictionToFullTree(jitter):
    """
    [query.dll] STDAPI CIRestrictionToFullTree(DBCOMMANDTREE const* pTree, WCHAR const* pwszColumns, WCHAR const* pwszSortColumns, WCHAR const* pwszGroupings, DBCOMMANDTREE** ppTree, ULONG cProperties, CIPROPERTYDEF* pProperties, LCID LocaleID)
    """
    ret_ad, args = jitter.func_args_stdcall(["pTree", "pwszColumns", "pwszSortColumns", "pwszGroupings", "ppTree", "cProperties", "pProperties", "LocaleID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CITextToFullTree(jitter):
    """
    [query.dll] STDAPI CITextToFullTree(WCHAR const* pwszRestriction, WCHAR const* pwszColumns, WCHAR const* pwszSortColumns, WCHAR const* pwszGroupings, DBCOMMANDTREE** ppTree, ULONG cProperties, CIPROPERTYDEF* pProperties, LCID LocaleID)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszRestriction", "pwszColumns", "pwszSortColumns", "pwszGroupings", "ppTree", "cProperties", "pProperties", "LocaleID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CITextToFullTreeEx(jitter):
    """
    [query.dll] STDAPI CITextToFullTreeEx(WCHAR const* pwszRestriction, ULONG ulDialect, WCHAR const* pwszColumns, WCHAR const* pwszSortColumns, WCHAR const* pwszGroupings, DBCOMMANDTREE** ppTree, ULONG cProperties, CIPROPERTYDEF* pProperties, LCID LocaleID)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszRestriction", "ulDialect", "pwszColumns", "pwszSortColumns", "pwszGroupings", "ppTree", "cProperties", "pProperties", "LocaleID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CITextToSelectTree(jitter):
    """
    [query.dll] STDAPI CITextToSelectTree(WCHAR const* pwszRestriction, DBCOMMANDTREE** ppTree, ULONG cProperties, CIPROPERTYDEF* pProperties, LCID LocaleID)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszRestriction", "ppTree", "cProperties", "pProperties", "LocaleID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_CITextToSelectTreeEx(jitter):
    """
    [query.dll] STDAPI CITextToSelectTreeEx(WCHAR const* pwszRestriction, ULONG ulDialect, DBCOMMANDTREE** ppTree, ULONG cProperties, CIPROPERTYDEF* pProperties, LCID LocaleID)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwszRestriction", "ulDialect", "ppTree", "cProperties", "pProperties", "LocaleID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_LoadIFilter(jitter):
    """
    [query.dll] STDAPI LoadIFilter(WCHAR const* pwcsPath, IUnknown* pUnkOuter, void** ppIUnk)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcsPath", "pUnkOuter", "ppIUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_BindIFilterFromStorage(jitter):
    """
    [query.dll] STDAPI BindIFilterFromStorage(IStorage* pStg, IUnknown* pUnkOuter, void** ppIUnk)
    """
    ret_ad, args = jitter.func_args_stdcall(["pStg", "pUnkOuter", "ppIUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def query_BindIFilterFromStream(jitter):
    """
    [query.dll] STDAPI BindIFilterFromStream(IStream* pStm, IUnknown* pUnkOuter, void** ppIUnk)
    """
    ret_ad, args = jitter.func_args_stdcall(["pStm", "pUnkOuter", "ppIUnk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
