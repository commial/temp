InputScope = {
    "IS_DEFAULT": 0,
    "IS_URL": 1,
    "IS_FILE_FULLFILEPATH": 2,
    "IS_FILE_FILENAME": 3,
    "IS_EMAIL_USERNAME": 4,
    "IS_EMAIL_SMTPEMAILADDRESS": 5,
    "IS_LOGINNAME": 6,
    "IS_PERSONALNAME_FULLNAME": 7,
    "IS_PERSONALNAME_PREFIX": 8,
    "IS_PERSONALNAME_GIVENNAME": 9,
    "IS_PERSONALNAME_MIDDLENAME": 10,
    "IS_PERSONALNAME_SURNAME": 11,
    "IS_PERSONALNAME_SUFFIX": 12,
    "IS_ADDRESS_FULLPOSTALADDRESS": 13,
    "IS_ADDRESS_POSTALCODE": 14,
    "IS_ADDRESS_STREET": 15,
    "IS_ADDRESS_STATEORPROVINCE": 16,
    "IS_ADDRESS_CITY": 17,
    "IS_ADDRESS_COUNTRYNAME": 18,
    "IS_ADDRESS_COUNTRYSHORTNAME": 19,
    "IS_CURRENCY_AMOUNTANDSYMBOL": 20,
    "IS_CURRENCY_AMOUNT": 21,
    "IS_DATE_FULLDATE": 22,
    "IS_DATE_MONTH": 23,
    "IS_DATE_DAY": 24,
    "IS_DATE_YEAR": 25,
    "IS_DATE_MONTHNAME": 26,
    "IS_DATE_DAYNAME": 27,
    "IS_DIGITS": 28,
    "IS_NUMBER": 29,
    "IS_ONECHAR": 30,
    "IS_PASSWORD": 31,
    "IS_TELEPHONE_FULLTELEPHONENUMBER": 32,
    "IS_TELEPHONE_COUNTRYCODE": 33,
    "IS_TELEPHONE_AREACODE": 34,
    "IS_TELEPHONE_LOCALNUMBER": 35,
    "IS_TIME_FULLTIME": 36,
    "IS_TIME_HOUR": 37,
    "IS_TIME_MINORSEC": 38,
    "IS_NUMBER_FULLWIDTH": 39,
    "IS_ALPHANUMERIC_HALFWIDTH": 40,
    "IS_ALPHANUMERIC_FULLWIDTH": 41,
    "IS_CURRENCY_CHINESE": 42,
    "IS_BOPOMOFO": 43,
    "IS_HIRAGANA": 44,
    "IS_KATAKANA_HALFWIDTH": 45,
    "IS_KATAKANA_FULLWIDTH": 46,
    "IS_HANJA": 47,
    "IS_HANGUL_HALFWIDTH": 48,
    "IS_HANGUL_FULLWIDTH": 49,
    "IS_PHRASELIST": -1,
    "IS_REGULAREXPRESSION": -2,
    "IS_SRGS": -3,
    "IS_XML": -4,
    "IS_ENUMSTRING": -5,
}

def msctf_SetInputScope(jitter):
    """
    HRESULT SetInputScope(
        HWND hwnd,
        InputScope inputscope
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "inputscope"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_SetInputScopes(jitter):
    """
    HRESULT SetInputScopes(
        HWND hwnd,
        const InputScope* pInputScopes,
        UINT cInputScopes,
        WCHAR** ppszPhraseList,
        UINT cPhrases,
        WCHAR* pszRegExp,
        WCHAR* pszSRGS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pInputScopes", "cInputScopes", "ppszPhraseList", "cPhrases", "pszRegExp", "pszSRGS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_SetInputScopes2(jitter):
    """
    HRESULT SetInputScopes2(
        HWND hwnd,
        const InputScope* pInputScopes,
        UINT cInputScopes,
        IEnumString* pEnumString,
        WCHAR* pszRegExp,
        WCHAR* pszSRGS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pInputScopes", "cInputScopes", "pEnumString", "pszRegExp", "pszSRGS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_SetInputScopeXML(jitter):
    """
    void SetInputScopeXML()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateCategoryMgr(jitter):
    """
    HRESULT TF_CreateCategoryMgr(
        ITfCategoryMgr** ppcat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppcat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateDisplayAttributeMgr(jitter):
    """
    HRESULT TF_CreateDisplayAttributeMgr(
        ITfDisplayAttributeMgr** ppdam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppdam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateInputProcessorProfiles(jitter):
    """
    HRESULT TF_CreateInputProcessorProfiles(
        ITfInputProcessorProfiles** ppipr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppipr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateLangBarItemMgr(jitter):
    """
    HRESULT TF_CreateLangBarItemMgr(
        ITfLangBarItemMgr** pplbim
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pplbim"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateLangBarMgr(jitter):
    """
    HRESULT TF_CreateLangBarMgr(
        ITfLangBarMgr** pppbm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pppbm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_CreateThreadMgr(jitter):
    """
    HRESULT TF_CreateThreadMgr(
        ITfThreadMgr** pptim
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pptim"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_GetThreadMgr(jitter):
    """
    HRESULT TF_GetThreadMgr(
        ITfThreadMgr** pptim
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pptim"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_TF_InvalidAssemblyListCacheIfExist(jitter):
    """
    HRESULT TF_InvalidAssemblyListCacheIfExist()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctf_MsimtfIsWindowFiltered(jitter):
    """
    BOOL MsimtfIsWindowFiltered(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
