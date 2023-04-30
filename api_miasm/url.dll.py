
def url_InetIsOffline(jitter):
    """"
    [url.dll] BOOL InetIsOffline(DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def url_MIMEAssociationDialog(jitter):
    """"
    [url.dll] HRESULT MIMEAssociationDialog(HWND hwndParent, DWORD dwInFlags, LPCTSTR pcszFile, LPCTSTR pcszMIMEContentType, LPTSTR pszAppBuf, UINT ucAppBufLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwInFlags", "pcszFile", "pcszMIMEContentType", "pszAppBuf", "ucAppBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def url_TranslateURL(jitter):
    """"
    [url.dll] HRESULT TranslateURL(LPCSTR pcszURL, DWORD dwInFlags, LPSTR* ppszTranslatedURL)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcszURL", "dwInFlags", "ppszTranslatedURL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def url_URLAssociationDialog(jitter):
    """"
    [url.dll] HRESULT URLAssociationDialog(HWND hwndParent, DWORD dwInFlags, LPCTSTR pcszFile, LPCTSTR pcszURL, LPTSTR pszAppBuf, UINT ucAppBufLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "dwInFlags", "pcszFile", "pcszURL", "pszAppBuf", "ucAppBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
