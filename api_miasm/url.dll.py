
def url_InetIsOffline(jitter):
    """
    BOOL InetIsOffline(
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def url_MIMEAssociationDialog(jitter, get_str, set_str):
    """
    HRESULT MIMEAssociationDialog(
        HWND hwndParent,
        DWORD dwInFlags,
        LPCTSTR pcszFile,
        LPCTSTR pcszMIMEContentType,
        LPTSTR pszAppBuf,
        UINT ucAppBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwInFlags", "pcszFile", "pcszMIMEContentType", "pszAppBuf", "ucAppBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def url_MIMEAssociationDialogA(jitter):
    url_MIMEAssociationDialog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def url_MIMEAssociationDialogW(jitter):
    url_MIMEAssociationDialog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def url_TranslateURL(jitter, get_str, set_str):
    """
    HRESULT TranslateURL(
        LPCSTR pcszURL,
        DWORD dwInFlags,
        LPSTR* ppszTranslatedURL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcszURL", "dwInFlags", "ppszTranslatedURL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def url_TranslateURLA(jitter):
    url_TranslateURL(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def url_TranslateURLW(jitter):
    url_TranslateURL(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def url_URLAssociationDialog(jitter, get_str, set_str):
    """
    HRESULT URLAssociationDialog(
        HWND hwndParent,
        DWORD dwInFlags,
        LPCTSTR pcszFile,
        LPCTSTR pcszURL,
        LPTSTR pszAppBuf,
        UINT ucAppBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwInFlags", "pcszFile", "pcszURL", "pszAppBuf", "ucAppBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def url_URLAssociationDialogA(jitter):
    url_URLAssociationDialog(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def url_URLAssociationDialogW(jitter):
    url_URLAssociationDialog(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
