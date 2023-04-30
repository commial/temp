
def msvcrxx__memccpy(jitter):
    """"
    [msvcrxx.dll] void* _memccpy(void* dest, const void* src, int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memchr(jitter):
    """"
    [msvcrxx.dll] void* memchr(const void* buf, int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buf", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memcmp(jitter):
    """"
    [msvcrxx.dll] int memcmp(const void* buf1, const void* buf2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buf1", "buf2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memcpy(jitter):
    """"
    [msvcrxx.dll] void* memcpy(void* dest, const void* src, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memcpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t memcpy_s(void* dest, size_t numberOfElements, const void* src, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "numberOfElements", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wmemcpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t wmemcpy_s(wchar_t* dest, size_t numberOfElements, const wchar_t* src, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "numberOfElements", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__memicmp(jitter):
    """"
    [msvcrxx.dll] int _memicmp(const void* buf1, const void* buf2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buf1", "buf2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__memicmp_l(jitter):
    """"
    [msvcrxx.dll] int _memicmp_l(const void* buf1, const void* buf2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buf1", "buf2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memmove(jitter):
    """"
    [msvcrxx.dll] void* memmove(void* dest, const void* src, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memmove_s(jitter):
    """"
    [msvcrxx.dll] errno_t memmove_s(void* dest, size_t numberOfElements, const void* src, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "numberOfElements", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wmemmove_s(jitter):
    """"
    [msvcrxx.dll] errno_t wmemmove_s(wchar_t* dest, size_t numberOfElements, const wchar_t* src, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "numberOfElements", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_memset(jitter):
    """"
    [msvcrxx.dll] void* memset(void* dest, int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swab(jitter):
    """"
    [msvcrxx.dll] void _swab(char* src, char* dest, int n)
    """"
    ret_ad, args = jitter.func_args_cdecl(["src", "dest", "n"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isleadbyte(jitter):
    """"
    [msvcrxx.dll] int isleadbyte(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isleadbyte_l(jitter):
    """"
    [msvcrxx.dll] int _isleadbyte_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbalnum(jitter):
    """"
    [msvcrxx.dll] int _ismbbalnum(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbalnum_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbalnum_l(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbalpha(jitter):
    """"
    [msvcrxx.dll] int _ismbbalpha(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbalpha_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbalpha_l(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbgraph(jitter):
    """"
    [msvcrxx.dll] int _ismbbgraph(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbgraph_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbgraph_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkalnum(jitter):
    """"
    [msvcrxx.dll] int _ismbbkalnum(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkalnum_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbkalnum_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkana(jitter):
    """"
    [msvcrxx.dll] int _ismbbkana(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkana_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbkana_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkprint(jitter):
    """"
    [msvcrxx.dll] int _ismbbkprint(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkprint_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbkprint_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkpunct(jitter):
    """"
    [msvcrxx.dll] int _ismbbkpunct(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbkpunct_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbkpunct_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbblead(jitter):
    """"
    [msvcrxx.dll] int _ismbblead(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbblead_l(jitter):
    """"
    [msvcrxx.dll] int _ismbblead_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbprint(jitter):
    """"
    [msvcrxx.dll] int _ismbbprint(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbprint_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbprint_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbpunct(jitter):
    """"
    [msvcrxx.dll] int _ismbbpunct(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbpunct_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbpunct_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbtrail(jitter):
    """"
    [msvcrxx.dll] int _ismbbtrail(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbbtrail_l(jitter):
    """"
    [msvcrxx.dll] int _ismbbtrail_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbslead(jitter):
    """"
    [msvcrxx.dll] int _ismbslead(const unsigned char* str, const unsigned char* current)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "current"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbstrail(jitter):
    """"
    [msvcrxx.dll] int _ismbstrail(const unsigned char* str, const unsigned char* current)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "current"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbslead_l(jitter):
    """"
    [msvcrxx.dll] int _ismbslead_l(const unsigned char* str, const unsigned char* current, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "current", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbstrail_l(jitter):
    """"
    [msvcrxx.dll] int _ismbstrail_l(const unsigned char* str, const unsigned char* current, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "current", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbbtype(jitter):
    """"
    [msvcrxx.dll] [byte_type] _mbbtype(unsigned char c, int type)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbbtype_l(jitter):
    """"
    [msvcrxx.dll] [byte_type] _mbbtype_l(unsigned char c, int type, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "type", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsbtype(jitter):
    """"
    [msvcrxx.dll] [byte_type] _mbsbtype(const unsigned char* mbstr, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsbtype_l(jitter):
    """"
    [msvcrxx.dll] [byte_type] _mbsbtype_l(const unsigned char* mbstr, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isalnum(jitter):
    """"
    [msvcrxx.dll] int isalnum(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswalnum(jitter):
    """"
    [msvcrxx.dll] int iswalnum(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isalnum_l(jitter):
    """"
    [msvcrxx.dll] int _isalnum_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswalnum_l(jitter):
    """"
    [msvcrxx.dll] int _iswalnum_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcalnum(jitter):
    """"
    [msvcrxx.dll] int _ismbcalnum(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcalnum_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcalnum_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcalpha(jitter):
    """"
    [msvcrxx.dll] int _ismbcalpha(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcalpha_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcalpha_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcdigit(jitter):
    """"
    [msvcrxx.dll] int _ismbcdigit(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcdigit_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcdigit_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isalpha(jitter):
    """"
    [msvcrxx.dll] int isalpha(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswalpha(jitter):
    """"
    [msvcrxx.dll] int iswalpha(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isalpha_l(jitter):
    """"
    [msvcrxx.dll] int _isalpha_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswalpha_l(jitter):
    """"
    [msvcrxx.dll] int _iswalpha_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___isascii(jitter):
    """"
    [msvcrxx.dll] int __isascii(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswascii(jitter):
    """"
    [msvcrxx.dll] int iswascii(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iscntrl(jitter):
    """"
    [msvcrxx.dll] int iscntrl(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswcntrl(jitter):
    """"
    [msvcrxx.dll] int iswcntrl(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iscntrl_l(jitter):
    """"
    [msvcrxx.dll] int _iscntrl_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswcntrl_l(jitter):
    """"
    [msvcrxx.dll] int _iswcntrl_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___iscsym(jitter):
    """"
    [msvcrxx.dll] int __iscsym(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___iswcsym(jitter):
    """"
    [msvcrxx.dll] int __iswcsym(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___iscsymf(jitter):
    """"
    [msvcrxx.dll] int __iscsymf(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___iswcsymf(jitter):
    """"
    [msvcrxx.dll] int __iswcsymf(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswcsym_l(jitter):
    """"
    [msvcrxx.dll] int _iswcsym_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswcsymf_l(jitter):
    """"
    [msvcrxx.dll] int _iswcsymf_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isdigit(jitter):
    """"
    [msvcrxx.dll] int isdigit(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswdigit(jitter):
    """"
    [msvcrxx.dll] int iswdigit(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isdigit_l(jitter):
    """"
    [msvcrxx.dll] int _isdigit_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswdigit_l(jitter):
    """"
    [msvcrxx.dll] int _iswdigit_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isgraph(jitter):
    """"
    [msvcrxx.dll] int isgraph(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswgraph(jitter):
    """"
    [msvcrxx.dll] int iswgraph(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isgraph_l(jitter):
    """"
    [msvcrxx.dll] int _isgraph_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswgraph_l(jitter):
    """"
    [msvcrxx.dll] int _iswgraph_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcgraph(jitter):
    """"
    [msvcrxx.dll] int _ismbcgraph(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcgraph_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcgraph_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcprint(jitter):
    """"
    [msvcrxx.dll] int _ismbcprint(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcprint_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcprint_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcpunct(jitter):
    """"
    [msvcrxx.dll] int _ismbcpunct(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcpunct_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcpunct_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcspace(jitter):
    """"
    [msvcrxx.dll] int _ismbcspace(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcspace_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcspace_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_islower(jitter):
    """"
    [msvcrxx.dll] int islower(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswlower(jitter):
    """"
    [msvcrxx.dll] int iswlower(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__islower_l(jitter):
    """"
    [msvcrxx.dll] int _islower_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswlower_l(jitter):
    """"
    [msvcrxx.dll] int _iswlower_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbclower(jitter):
    """"
    [msvcrxx.dll] int _ismbclower(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbclower_l(jitter):
    """"
    [msvcrxx.dll] int _ismbclower_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcupper(jitter):
    """"
    [msvcrxx.dll] int _ismbcupper(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcupper_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcupper_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbchira(jitter):
    """"
    [msvcrxx.dll] int _ismbchira(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbchira_l(jitter):
    """"
    [msvcrxx.dll] int _ismbchira_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbckata(jitter):
    """"
    [msvcrxx.dll] int _ismbckata(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbckata_l(jitter):
    """"
    [msvcrxx.dll] int _ismbckata_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbclegal(jitter):
    """"
    [msvcrxx.dll] int _ismbclegal(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbclegal_l(jitter):
    """"
    [msvcrxx.dll] int _ismbclegal_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcsymbol(jitter):
    """"
    [msvcrxx.dll] int _ismbcsymbol(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcsymbol_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcsymbol_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl0(jitter):
    """"
    [msvcrxx.dll] int _ismbcl0(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl0_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcl0_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl1(jitter):
    """"
    [msvcrxx.dll] int _ismbcl1(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl1_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcl1_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl2(jitter):
    """"
    [msvcrxx.dll] int _ismbcl2(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ismbcl2_l(jitter):
    """"
    [msvcrxx.dll] int _ismbcl2_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isprint(jitter):
    """"
    [msvcrxx.dll] int isprint(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswprint(jitter):
    """"
    [msvcrxx.dll] int iswprint(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isprint_l(jitter):
    """"
    [msvcrxx.dll] int _isprint_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswprint_l(jitter):
    """"
    [msvcrxx.dll] int _iswprint_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ispunct(jitter):
    """"
    [msvcrxx.dll] int ispunct(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswpunct(jitter):
    """"
    [msvcrxx.dll] int iswpunct(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ispunct_l(jitter):
    """"
    [msvcrxx.dll] int _ispunct_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswpunct_l(jitter):
    """"
    [msvcrxx.dll] int _iswpunct_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isspace(jitter):
    """"
    [msvcrxx.dll] int isspace(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswspace(jitter):
    """"
    [msvcrxx.dll] int iswspace(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isspace_l(jitter):
    """"
    [msvcrxx.dll] int _isspace_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswspace_l(jitter):
    """"
    [msvcrxx.dll] int _iswspace_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isupper(jitter):
    """"
    [msvcrxx.dll] int isupper(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isupper_l(jitter):
    """"
    [msvcrxx.dll] int _isupper_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswupper(jitter):
    """"
    [msvcrxx.dll] int iswupper(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswupper_l(jitter):
    """"
    [msvcrxx.dll] int _iswupper_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isctype(jitter):
    """"
    [msvcrxx.dll] int _isctype(int c, _ctype_t mask)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isctype_l(jitter):
    """"
    [msvcrxx.dll] int _isctype_l(int c, _ctype_t mask, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "mask", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswctype(jitter):
    """"
    [msvcrxx.dll] int iswctype(wint_t c, wctype_t mask)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_is_wctype(jitter):
    """"
    [msvcrxx.dll] int is_wctype(wint_t c, wctype_t mask)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswctype_l(jitter):
    """"
    [msvcrxx.dll] int _iswctype_l(wint_t c, wctype_t mask, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "mask", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_isxdigit(jitter):
    """"
    [msvcrxx.dll] int isxdigit(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_iswxdigit(jitter):
    """"
    [msvcrxx.dll] int iswxdigit(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isxdigit_l(jitter):
    """"
    [msvcrxx.dll] int _isxdigit_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__iswxdigit_l(jitter):
    """"
    [msvcrxx.dll] int _iswxdigit_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctype(jitter):
    """"
    [msvcrxx.dll] wctype_t _wctype(const char* property)
    """"
    ret_ad, args = jitter.func_args_cdecl(["property"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___pctype_func(jitter):
    """"
    [msvcrxx.dll] const unsigned short* __pctype_func()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_free(jitter):
    """"
    [msvcrxx.dll] void _aligned_free(void* memblock)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_free_dbg(jitter):
    """"
    [msvcrxx.dll] void _aligned_free_dbg(void* memblock)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_malloc(jitter):
    """"
    [msvcrxx.dll] void* _aligned_malloc(size_t size, size_t alignment)
    """"
    ret_ad, args = jitter.func_args_cdecl(["size", "alignment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_malloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _aligned_malloc_dbg(size_t size, size_t alignment, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["size", "alignment", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_msize(jitter):
    """"
    [msvcrxx.dll] size_t _aligned_msize(void* memblock, size_t alignment, size_t offset)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_msize_dbg(jitter):
    """"
    [msvcrxx.dll] size_t _aligned_msize_dbg(void* memblock, size_t alignment, size_t offset)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_malloc(jitter):
    """"
    [msvcrxx.dll] void* _aligned_offset_malloc(size_t size, size_t alignment, size_t offset)
    """"
    ret_ad, args = jitter.func_args_cdecl(["size", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_malloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _aligned_offset_malloc_dbg(size_t size, size_t alignment, size_t offset, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["size", "alignment", "offset", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_realloc(jitter):
    """"
    [msvcrxx.dll] void* _aligned_offset_realloc(void* memblock, size_t size, size_t alignment, size_t offset)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_realloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _aligned_offset_realloc_dbg(void* memblock, size_t size, size_t alignment, size_t offset, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size", "alignment", "offset", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_recalloc(jitter):
    """"
    [msvcrxx.dll] void* _aligned_offset_recalloc(void* memblock, size_t num, size_t size, size_t alignment, size_t offset)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "num", "size", "alignment", "offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_offset_recalloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _aligned_offset_recalloc_dbg(void* memblock, size_t num, size_t size, size_t alignment, size_t offset, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "num", "size", "alignment", "offset", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_realloc(jitter):
    """"
    [msvcrxx.dll] void* _aligned_realloc(void* memblock, size_t size, size_t alignment)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size", "alignment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_realloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _aligned_realloc_dbg(void* memblock, size_t size, size_t alignment, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size", "alignment", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_recalloc(jitter):
    """"
    [msvcrxx.dll] void* _aligned_recalloc(void* memblock, size_t num, size_t size, size_t alignment)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "num", "size", "alignment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__aligned_recalloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _aligned_recalloc_dbg(void* memblock, size_t num, size_t size, size_t alignment, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "num", "size", "alignment", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_abs(jitter):
    """"
    [msvcrxx.dll] int abs(int n)
    """"
    ret_ad, args = jitter.func_args_cdecl(["n"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__abs64(jitter):
    """"
    [msvcrxx.dll] __int64 _abs64(__int64 n)
    """"
    ret_ad, args = jitter.func_args_cdecl(["n"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtof(jitter):
    """"
    [msvcrxx.dll] double _wtof(const wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtof_l(jitter):
    """"
    [msvcrxx.dll] double _wtof_l(const wchar_t* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtoi(jitter):
    """"
    [msvcrxx.dll] int _wtoi(const wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtoi_l(jitter):
    """"
    [msvcrxx.dll] int _wtoi_l(const wchar_t* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtol(jitter):
    """"
    [msvcrxx.dll] long _wtol(const wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtol_l(jitter):
    """"
    [msvcrxx.dll] long _wtol_l(const wchar_t* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__itoa(jitter):
    """"
    [msvcrxx.dll] char* _itoa(int value, char* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__i64toa(jitter):
    """"
    [msvcrxx.dll] char* _i64toa(__int64 value, char* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ui64toa(jitter):
    """"
    [msvcrxx.dll] char* _ui64toa(unsigned __int64 value, char* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__itow(jitter):
    """"
    [msvcrxx.dll] wchar_t* _itow(int value, wchar_t* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__i64tow(jitter):
    """"
    [msvcrxx.dll] wchar_t* _i64tow(__int64 value, wchar_t* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ui64tow(jitter):
    """"
    [msvcrxx.dll] wchar_t* _ui64tow(unsigned __int64 value, wchar_t* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__itoa_s(jitter):
    """"
    [msvcrxx.dll] errno_t _itoa_s(int value, char* buffer, size_t sizeInCharacters, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__i64toa_s(jitter):
    """"
    [msvcrxx.dll] errno_t _i64toa_s(__int64 value, char* buffer, size_t sizeInCharacters, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ui64toa_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ui64toa_s(unsigned __int64 value, char* buffer, size_t sizeInCharacters, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__itow_s(jitter):
    """"
    [msvcrxx.dll] errno_t _itow_s(int value, wchar_t* buffer, size_t sizeInCharacters, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__i64tow_s(jitter):
    """"
    [msvcrxx.dll] errno_t _i64tow_s(__int64 value, wchar_t* buffer, size_t sizeInCharacters, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ui64tow_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ui64tow_s(unsigned __int64 value, wchar_t* buffer, size_t sizeInCharacters, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "buffer", "sizeInCharacters", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_labs(jitter):
    """"
    [msvcrxx.dll] long labs(long n)
    """"
    ret_ad, args = jitter.func_args_cdecl(["n"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ltoa(jitter):
    """"
    [msvcrxx.dll] char* _ltoa(long value, char* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ltow(jitter):
    """"
    [msvcrxx.dll] wchar_t* _ltow(long value, wchar_t* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ltoa_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ltoa_s(long value, char* str, size_t sizeOfstr, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "sizeOfstr", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ltow_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ltow_s(long value, wchar_t* str, size_t sizeOfstr, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "sizeOfstr", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbbtombc(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbbtombc(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbbtombc_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbbtombc_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbcjistojms(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbcjistojms(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbcjistojms_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbcjistojms_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbcjmstojis(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbcjmstojis(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbcjmstojis_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbcjmstojis_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctohira(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctohira(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctohira_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctohira_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctokata(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctokata(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctokata_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctokata_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctombb(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctombb(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctombb_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctombb_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___toascii(jitter):
    """"
    [msvcrxx.dll] int __toascii(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tolower(jitter):
    """"
    [msvcrxx.dll] int tolower(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tolower(jitter):
    """"
    [msvcrxx.dll] int _tolower(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_towlower(jitter):
    """"
    [msvcrxx.dll] int towlower(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tolower_l(jitter):
    """"
    [msvcrxx.dll] int _tolower_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__towlower_l(jitter):
    """"
    [msvcrxx.dll] int _towlower_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_toupper(jitter):
    """"
    [msvcrxx.dll] int toupper(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__toupper(jitter):
    """"
    [msvcrxx.dll] int _toupper(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_towupper(jitter):
    """"
    [msvcrxx.dll] int towupper(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__toupper_l(jitter):
    """"
    [msvcrxx.dll] int _toupper_l(int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__towupper_l(jitter):
    """"
    [msvcrxx.dll] int _towupper_l(wint_t c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ultoa(jitter):
    """"
    [msvcrxx.dll] char* _ultoa(unsigned long value, char* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ultow(jitter):
    """"
    [msvcrxx.dll] wchar_t* _ultow(unsigned long value, wchar_t* str, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ultoa_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ultoa_s(unsigned long value, char* str, size_t sizeOfstr, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "sizeOfstr", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ultow_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ultow_s(unsigned long value, wchar_t* str, size_t sizeOfstr, int radix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "sizeOfstr", "radix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fcvt(jitter):
    """"
    [msvcrxx.dll] char* _fcvt(double value, int count, int* dec, int* sign)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "count", "dec", "sign"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fcvt_s(jitter):
    """"
    [msvcrxx.dll] errno_t _fcvt_s(char* buffer, size_t sizeInBytes, double value, int count, int* dec, int* sign)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInBytes", "value", "count", "dec", "sign"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gcvt(jitter):
    """"
    [msvcrxx.dll] char* _gcvt(double value, int digits, char* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "digits", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gcvt_s(jitter):
    """"
    [msvcrxx.dll] errno_t _gcvt_s(char* buffer, size_t sizeInBytes, double value, int digits)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInBytes", "value", "digits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atol_l(jitter):
    """"
    [msvcrxx.dll] long _atol_l(const char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoi_l(jitter):
    """"
    [msvcrxx.dll] int _atoi_l(const char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atof(jitter):
    """"
    [msvcrxx.dll] double atof(const char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atof_l(jitter):
    """"
    [msvcrxx.dll] double _atof_l(const char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoi64_l(jitter):
    """"
    [msvcrxx.dll] __int64 _atoi64_l(const char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atoi(jitter):
    """"
    [msvcrxx.dll] int atoi(const char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoi64(jitter):
    """"
    [msvcrxx.dll] __int64 _atoi64(const char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atol(jitter):
    """"
    [msvcrxx.dll] long atol(const char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atodbl(jitter):
    """"
    [msvcrxx.dll] int _atodbl(_CRT_DOUBLE* value, char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atodbl_l(jitter):
    """"
    [msvcrxx.dll] int _atodbl_l(_CRT_DOUBLE* value, char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoldbl(jitter):
    """"
    [msvcrxx.dll] int _atoldbl(_LDOUBLE* value, char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoldbl_l(jitter):
    """"
    [msvcrxx.dll] int _atoldbl_l(_LDOUBLE* value, char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoflt(jitter):
    """"
    [msvcrxx.dll] int _atoflt(_CRT_FLOAT* value, char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__atoflt_l(jitter):
    """"
    [msvcrxx.dll] int _atoflt_l(_CRT_FLOAT* value, char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtoi64(jitter):
    """"
    [msvcrxx.dll] __int64 _wtoi64(const wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtoi64_l(jitter):
    """"
    [msvcrxx.dll] __int64 _wtoi64_l(const wchar_t* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtoul(jitter):
    """"
    [msvcrxx.dll] unsigned long strtoul(const char* nptr, char** endptr, int base)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoul_l(jitter):
    """"
    [msvcrxx.dll] unsigned long _strtoul_l(const char* nptr, char** endptr, int base, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstoul(jitter):
    """"
    [msvcrxx.dll] unsigned long wcstoul(const wchar_t* nptr, wchar_t** endptr, int base)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoul_l(jitter):
    """"
    [msvcrxx.dll] unsigned long _wcstoul_l(const wchar_t* nptr, wchar_t** endptr, int base, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtod(jitter):
    """"
    [msvcrxx.dll] double strtod(const char* nptr, char** endptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtod_l(jitter):
    """"
    [msvcrxx.dll] double _strtod_l(const char* nptr, char** endptr, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstod(jitter):
    """"
    [msvcrxx.dll] double wcstod(const wchar_t* nptr, wchar_t** endptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstod_l(jitter):
    """"
    [msvcrxx.dll] double _wcstod_l(const wchar_t* nptr, wchar_t** endptr, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtol(jitter):
    """"
    [msvcrxx.dll] long strtol(const char* nptr, char** endptr, int base)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstol(jitter):
    """"
    [msvcrxx.dll] long wcstol(const wchar_t* nptr, wchar_t** endptr, int base)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtol_l(jitter):
    """"
    [msvcrxx.dll] long _strtol_l(const char* nptr, char** endptr, int base, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstol_l(jitter):
    """"
    [msvcrxx.dll] long _wcstol_l(const wchar_t* nptr, wchar_t** endptr, int base, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbtowc(jitter):
    """"
    [msvcrxx.dll] int mbtowc(wchar_t* wchar, const char* mbchar, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["wchar", "mbchar", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbtowc_l(jitter):
    """"
    [msvcrxx.dll] int _mbtowc_l(wchar_t* wchar, const char* mbchar, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["wchar", "mbchar", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbstowcs(jitter):
    """"
    [msvcrxx.dll] size_t mbstowcs(wchar_t* wcstr, const char* mbstr, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["wcstr", "mbstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstowcs_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbstowcs_l(wchar_t* wcstr, const char* mbstr, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["wcstr", "mbstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbstowcs_s(jitter):
    """"
    [msvcrxx.dll] errno_t mbstowcs_s(size_t* pReturnValue, wchar_t* wcstr, size_t sizeInWords, const char* mbstr, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "wcstr", "sizeInWords", "mbstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstowcs_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbstowcs_s_l(size_t* pReturnValue, wchar_t* wcstr, size_t sizeInWords, const char* mbstr, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "wcstr", "sizeInWords", "mbstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstombs(jitter):
    """"
    [msvcrxx.dll] size_t wcstombs(char* mbstr, const wchar_t* wcstr, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "wcstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstombs_l(jitter):
    """"
    [msvcrxx.dll] size_t _wcstombs_l(char* mbstr, const wchar_t* wcstr, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "wcstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstombs_s(jitter):
    """"
    [msvcrxx.dll] errno_t wcstombs_s(size_t* pReturnValue, char* mbstr, size_t sizeInBytes, const wchar_t* wcstr, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "mbstr", "sizeInBytes", "wcstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstombs_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _wcstombs_s_l(size_t* pReturnValue, char* mbstr, size_t sizeInBytes, const wchar_t* wcstr, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "mbstr", "sizeInBytes", "wcstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wctomb(jitter):
    """"
    [msvcrxx.dll] int wctomb(char* mbchar, wchar_t wchar)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbchar", "wchar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctomb_l(jitter):
    """"
    [msvcrxx.dll] int _wctomb_l(char* mbchar, wchar_t wchar, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbchar", "wchar", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wctomb_s(jitter):
    """"
    [msvcrxx.dll] errno_t wctomb_s(int* pRetValue, char* mbchar, size_t sizeInBytes, wchar_t wchar)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pRetValue", "mbchar", "sizeInBytes", "wchar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctomb_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _wctomb_s_l(int* pRetValue, char* mbchar, size_t sizeInBytes, wchar_t wchar, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pRetValue", "mbchar", "sizeInBytes", "wchar", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctoupper_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctoupper_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctoupper(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctoupper(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctolower(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctolower(unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbctolower_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbctolower_l(unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ecvt(jitter):
    """"
    [msvcrxx.dll] char* _ecvt(double value, int count, int* dec, int* sign)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "count", "dec", "sign"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ecvt_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ecvt_s(char* _Buffer, size_t _SizeInBytes, double _Value, int _Count, int* _Dec, int* _Sign)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_Buffer", "_SizeInBytes", "_Value", "_Count", "_Dec", "_Sign"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbrtowc(jitter):
    """"
    [msvcrxx.dll] size_t mbrtowc(wchar_t* wchar, const char* mbchar, size_t count, mbstate_t mbstate)
    """"
    ret_ad, args = jitter.func_args_cdecl(["wchar", "mbchar", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbsrtowcs(jitter):
    """"
    [msvcrxx.dll] size_t mbsrtowcs(wchar_t* wcstr, const char** mbstr, size_t count, mbstate_t* mbstate)
    """"
    ret_ad, args = jitter.func_args_cdecl(["wcstr", "mbstr", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbsrtowcs_s(jitter):
    """"
    [msvcrxx.dll] errno_t mbsrtowcs_s(size_t* pReturnValue, wchar_t* wcstr, size_t sizeInWords, const char** mbstr, size_t count, mbstate_t* mbstate)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "wcstr", "sizeInWords", "mbstr", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoi64(jitter):
    """"
    [msvcrxx.dll] __int64 _strtoi64(const char* nptr, char** endptr, int base)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoi64(jitter):
    """"
    [msvcrxx.dll] __int64 _wcstoi64(const wchar_t* nptr, wchar_t** endptr, int base)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoi64_l(jitter):
    """"
    [msvcrxx.dll] __int64 _strtoi64_l(const char* nptr, char** endptr, int base, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoi64_l(jitter):
    """"
    [msvcrxx.dll] __int64 _wcstoi64_l(const wchar_t* nptr, wchar_t** endptr, int base, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoui64(jitter):
    """"
    [msvcrxx.dll] unsigned __int64 _strtoui64(const char* nptr, char** endptr, int base)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoui64(jitter):
    """"
    [msvcrxx.dll] unsigned __int64 _wcstoui64(const wchar_t* nptr, wchar_t** endptr, int base)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtoui64_l(jitter):
    """"
    [msvcrxx.dll] unsigned __int64 _strtoui64_l(const char* nptr, char** endptr, int base, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcstoui64_l(jitter):
    """"
    [msvcrxx.dll] unsigned __int64 _wcstoui64_l(const wchar_t* nptr, wchar_t** endptr, int base, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["nptr", "endptr", "base", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcrtomb(jitter):
    """"
    [msvcrxx.dll] size_t wcrtomb(char* mbchar, wchar_t wchar, mbstate_t* mbstate)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbchar", "wchar", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcrtomb_s(jitter):
    """"
    [msvcrxx.dll] errno_t wcrtomb_s(size_t* pReturnValue, char* mbchar, size_t sizeOfmbchar, wchar_t* wchar, mbstate_t* mbstate)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "mbchar", "sizeOfmbchar", "wchar", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsrtombs(jitter):
    """"
    [msvcrxx.dll] size_t wcsrtombs(char* mbstr, const wchar_t** wcstr, size_t count, mbstate_t* mbstate)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "wcstr", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsrtombs_s(jitter):
    """"
    [msvcrxx.dll] errno_t wcsrtombs_s(size_t* pReturnValue, char* mbstr, size_t sizeInBytes, const wchar_t** wcstr, size_t count, mbstate_t* mbstate)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "mbstr", "sizeInBytes", "wcstr", "count", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wctob(jitter):
    """"
    [msvcrxx.dll] int wctob(wint_t wchar)
    """"
    ret_ad, args = jitter.func_args_cdecl(["wchar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__byteswap_ushort(jitter):
    """"
    [msvcrxx.dll] unsigned short _byteswap_ushort(unsigned short val)
    """"
    ret_ad, args = jitter.func_args_cdecl(["val"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__byteswap_ulong(jitter):
    """"
    [msvcrxx.dll] unsigned long _byteswap_ulong(unsigned long val)
    """"
    ret_ad, args = jitter.func_args_cdecl(["val"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__byteswap_uint64(jitter):
    """"
    [msvcrxx.dll] unsigned __int64 _byteswap_uint64(unsigned __int64 val)
    """"
    ret_ad, args = jitter.func_args_cdecl(["val"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_btowc(jitter):
    """"
    [msvcrxx.dll] wint_t btowc(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtCheckMemory(jitter):
    """"
    [msvcrxx.dll] int _CrtCheckMemory()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDbgBreak(jitter):
    """"
    [msvcrxx.dll] void _CrtDbgBreak()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDbgReport(jitter):
    """"
    [msvcrxx.dll] int _CrtDbgReport([CRT_REPORT_TYPE] reportType, const char* filename, int linenumber, const char* moduleName, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["reportType", "filename", "linenumber", "moduleName", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDbgReportW(jitter):
    """"
    [msvcrxx.dll] int _CrtDbgReportW([CRT_REPORT_TYPE] reportType, const wchar_t* filename, int linenumber, const wchar_t* moduleName, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["reportType", "filename", "linenumber", "moduleName", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDoForAllClientObjects(jitter):
    """"
    [msvcrxx.dll] void _CrtDoForAllClientObjects(void* pfn, void* context)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pfn", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtDumpMemoryLeaks(jitter):
    """"
    [msvcrxx.dll] int _CrtDumpMemoryLeaks()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtIsMemoryBlock(jitter):
    """"
    [msvcrxx.dll] int _CrtIsMemoryBlock(const void* userData, unsigned int size, long* requestNumber, char** filename, int* linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["userData", "size", "requestNumber", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtIsValidHeapPointer(jitter):
    """"
    [msvcrxx.dll] int _CrtIsValidHeapPointer(const void* userData)
    """"
    ret_ad, args = jitter.func_args_cdecl(["userData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtIsValidPointer(jitter):
    """"
    [msvcrxx.dll] int _CrtIsValidPointer(const void* address, unsigned int size, int access)
    """"
    ret_ad, args = jitter.func_args_cdecl(["address", "size", "access"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtMemCheckpoint(jitter):
    """"
    [msvcrxx.dll] void _CrtMemCheckpoint(_CrtMemState* state)
    """"
    ret_ad, args = jitter.func_args_cdecl(["state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtMemDifference(jitter):
    """"
    [msvcrxx.dll] int _CrtMemDifference(_CrtMemState* stateDiff, const _CrtMemState* oldState, const _CrtMemState* newState)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stateDiff", "oldState", "newState"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtMemDumpAllObjectsSince(jitter):
    """"
    [msvcrxx.dll] void _CrtMemDumpAllObjectsSince(const _CrtMemState* state)
    """"
    ret_ad, args = jitter.func_args_cdecl(["state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtMemDumpStatistics(jitter):
    """"
    [msvcrxx.dll] void _CrtMemDumpStatistics(const _CrtMemState* state)
    """"
    ret_ad, args = jitter.func_args_cdecl(["state"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtReportBlockType(jitter):
    """"
    [msvcrxx.dll] int _CrtReportBlockType(const void* pBlock)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetAllocHook(jitter):
    """"
    [msvcrxx.dll] _CRT_ALLOC_HOOK _CrtSetAllocHook(_CRT_ALLOC_HOOK allocHook)
    """"
    ret_ad, args = jitter.func_args_cdecl(["allocHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetBreakAlloc(jitter):
    """"
    [msvcrxx.dll] long _CrtSetBreakAlloc(long lBreakAlloc)
    """"
    ret_ad, args = jitter.func_args_cdecl(["lBreakAlloc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetDbgFlag(jitter):
    """"
    [msvcrxx.dll] int _CrtSetDbgFlag([CRTDBG_FLAG] newFlag)
    """"
    ret_ad, args = jitter.func_args_cdecl(["newFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetDumpClient(jitter):
    """"
    [msvcrxx.dll] _CRT_DUMP_CLIENT _CrtSetDumpClient(_CRT_DUMP_CLIENT dumpClient)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dumpClient"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportFile(jitter):
    """"
    [msvcrxx.dll] _HFILE _CrtSetReportFile([CRT_REPORT_TYPE] reportType, _HFILE reportFile)
    """"
    ret_ad, args = jitter.func_args_cdecl(["reportType", "reportFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportHook(jitter):
    """"
    [msvcrxx.dll] _CRT_REPORT_HOOK _CrtSetReportHook(_CRT_REPORT_HOOK reportHook)
    """"
    ret_ad, args = jitter.func_args_cdecl(["reportHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportHook2(jitter):
    """"
    [msvcrxx.dll] int _CrtSetReportHook2([CRT_RPTHOOK_MODE] mode, _CRT_REPORT_HOOK pfnNewHook)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "pfnNewHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportHookW2(jitter):
    """"
    [msvcrxx.dll] int _CrtSetReportHookW2([CRT_RPTHOOK_MODE] mode, _CRT_REPORT_HOOKW pfnNewHook)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "pfnNewHook"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetReportMode(jitter):
    """"
    [msvcrxx.dll] [CRTDBG_MODE] _CrtSetReportMode([CRT_REPORT_TYPE] reportType, [CRTDBG_MODE] reportMode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["reportType", "reportMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtGetAllocHook(jitter):
    """"
    [msvcrxx.dll] _CRT_ALLOC_HOOK _CrtGetAllocHook()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtGetDumpClient(jitter):
    """"
    [msvcrxx.dll] _CRT_DUMP_CLIENT _CrtGetDumpClient()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtGetReportHook(jitter):
    """"
    [msvcrxx.dll] _CRT_REPORT_HOOK _CrtGetReportHook()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__CrtSetDebugFillThreshold(jitter):
    """"
    [msvcrxx.dll] size_t _CrtSetDebugFillThreshold(size_t _NewThreshold)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_NewThreshold"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chdir(jitter):
    """"
    [msvcrxx.dll] int _chdir(const char* dirname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wchdir(jitter):
    """"
    [msvcrxx.dll] int _wchdir(const wchar_t* dirname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chdrive(jitter):
    """"
    [msvcrxx.dll] int _chdrive(int drive)
    """"
    ret_ad, args = jitter.func_args_cdecl(["drive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getcwd(jitter):
    """"
    [msvcrxx.dll] char* _getcwd(char* buffer, int maxlen)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getcwd_dbg(jitter):
    """"
    [msvcrxx.dll] char* _getcwd_dbg(char* buffer, int maxlen, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "maxlen", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetcwd(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wgetcwd(wchar_t* buffer, int maxlen)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetcwd_dbg(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wgetcwd_dbg(wchar_t* buffer, int maxlen, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "maxlen", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdcwd(jitter):
    """"
    [msvcrxx.dll] char* _getdcwd(int drive, char* buffer, int maxlen)
    """"
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdcwd_dbg(jitter):
    """"
    [msvcrxx.dll] char* _getdcwd_dbg(int drive, char* buffer, int maxlen, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetdcwd(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wgetdcwd(int drive, wchar_t* buffer, int maxlen)
    """"
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetdcwd_dbg(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wgetdcwd_dbg(int drive, wchar_t* buffer, int maxlen, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdiskfree(jitter):
    """"
    [msvcrxx.dll] errno_t _getdiskfree(unsigned drive, struct _diskfree_t* driveinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["drive", "driveinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdrive(jitter):
    """"
    [msvcrxx.dll] int _getdrive()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdrives(jitter):
    """"
    [msvcrxx.dll] unsigned long _getdrives()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mkdir(jitter):
    """"
    [msvcrxx.dll] int _mkdir(const char* dirname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmkdir(jitter):
    """"
    [msvcrxx.dll] int _wmkdir(const wchar_t* dirname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rmdir(jitter):
    """"
    [msvcrxx.dll] int _rmdir(const char* dirname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wrmdir(jitter):
    """"
    [msvcrxx.dll] int _wrmdir(const wchar_t* dirname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dirname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__searchenv(jitter):
    """"
    [msvcrxx.dll] void _searchenv(const char* filename, const char* varname, char* pathname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "varname", "pathname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsearchenv(jitter):
    """"
    [msvcrxx.dll] void _wsearchenv(const wchar_t* filename, const wchar_t* varname, wchar_t* pathname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "varname", "pathname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__searchenv_s(jitter):
    """"
    [msvcrxx.dll] errno_t _searchenv_s(const char* filename, const char* varname, char* pathname, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "varname", "pathname", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsearchenv_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wsearchenv_s(const wchar_t* filename, const wchar_t* varname, wchar_t* pathname, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "varname", "pathname", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_error_mode(jitter):
    """"
    [msvcrxx.dll] [set_error_mode] _set_error_mode([set_error_mode] modeval)
    """"
    ret_ad, args = jitter.func_args_cdecl(["modeval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__seterrormode(jitter):
    """"
    [msvcrxx.dll] [set_error_mode] _seterrormode([set_error_mode] mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__purecall(jitter):
    """"
    [msvcrxx.dll] void _purecall()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_purecall_handler(jitter):
    """"
    [msvcrxx.dll] _purecall_handler _set_purecall_handler(_purecall_handler function)
    """"
    ret_ad, args = jitter.func_args_cdecl(["function"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_doserrno(jitter):
    """"
    [msvcrxx.dll] errno_t _get_doserrno(int* pValue)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_errno(jitter):
    """"
    [msvcrxx.dll] errno_t _get_errno(int* pValue)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_doserrno(jitter):
    """"
    [msvcrxx.dll] errno_t _set_doserrno(int value)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_errno(jitter):
    """"
    [msvcrxx.dll] errno_t _set_errno(int value)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_abort_behavior(jitter):
    """"
    [msvcrxx.dll] [abort_flag] _set_abort_behavior([abort_flag] flags, [abort_flag] mask)
    """"
    ret_ad, args = jitter.func_args_cdecl(["flags", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_invalid_parameter_handler(jitter):
    """"
    [msvcrxx.dll] _invalid_parameter_handler _get_invalid_parameter_handler()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_invalid_parameter_handler(jitter):
    """"
    [msvcrxx.dll] _invalid_parameter_handler _set_invalid_parameter_handler(_invalid_parameter_handler pNew)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__amsg_exit(jitter):
    """"
    [msvcrxx.dll] void _amsg_exit(int rterrnum)
    """"
    ret_ad, args = jitter.func_args_cdecl(["rterrnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_set_se_translator@@YAP6AXIPAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z(jitter):
    """"
    [msvcrxx.dll] _se_translator_function ?_set_se_translator@@YAP6AXIPAU_EXCEPTION_POINTERS@@@ZP6AXI0@Z@Z(_se_translator_function seTransFunction)
    """"
    ret_ad, args = jitter.func_args_cdecl(["seTransFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_terminate(jitter):
    """"
    [msvcrxx.dll] terminate_function _get_terminate()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?set_terminate@@YAP6AXXZP6AXXZ@Z(jitter):
    """"
    [msvcrxx.dll] terminate_function ?set_terminate@@YAP6AXXZP6AXXZ@Z(terminate_function termFunction)
    """"
    ret_ad, args = jitter.func_args_cdecl(["termFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_unexpected(jitter):
    """"
    [msvcrxx.dll] unexpected_function _get_unexpected()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?set_unexpected@@YAP6AXXZP6AXXZ@Z(jitter):
    """"
    [msvcrxx.dll] unexpected_function ?set_unexpected@@YAP6AXXZP6AXXZ@Z(unexpected_function unexpFunction)
    """"
    ret_ad, args = jitter.func_args_cdecl(["unexpFunction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?terminate@@YAXXZ(jitter):
    """"
    [msvcrxx.dll] void ?terminate@@YAXXZ()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?unexpected@@YAXXZ(jitter):
    """"
    [msvcrxx.dll] void ?unexpected@@YAXXZ()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___CxxFrameHandler(jitter):
    """"
    [msvcrxx.dll] EXCEPTION_DISPOSITION __CxxFrameHandler(EHExceptionRecord* pExcept, EHRegistrationNode* pRN, void* pContext, DispatcherContext* pDC)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pExcept", "pRN", "pContext", "pDC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__except_handler3(jitter):
    """"
    [msvcrxx.dll] [disposition_type] _except_handler3(PEXCEPTION_RECORD exception_record, PEXCEPTION_REGISTRATION registration, PCONTEXT context, PEXCEPTION_REGISTRATION dispatcher)
    """"
    ret_ad, args = jitter.func_args_cdecl(["exception_record", "registration", "context", "dispatcher"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___uncaught_exception(jitter):
    """"
    [msvcrxx.dll] bool __uncaught_exception()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__XcptFilter(jitter):
    """"
    [msvcrxx.dll] [xcpt_action] _XcptFilter([xcpt_num] xcptnum, PEXCEPTION_POINTERS pxcptinfoptrs)
    """"
    ret_ad, args = jitter.func_args_cdecl(["xcptnum", "pxcptinfoptrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__resetstkoflw(jitter):
    """"
    [msvcrxx.dll] int _resetstkoflw()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__abnormal_termination(jitter):
    """"
    [msvcrxx.dll] int _abnormal_termination()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chsize(jitter):
    """"
    [msvcrxx.dll] int _chsize(int fd, long size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chsize_s(jitter):
    """"
    [msvcrxx.dll] errno_t _chsize_s(int fd, __int64 size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__filelength(jitter):
    """"
    [msvcrxx.dll] long _filelength(int fd)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__filelengthi64(jitter):
    """"
    [msvcrxx.dll] __int64 _filelengthi64(int fd)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat(jitter):
    """"
    [msvcrxx.dll] int _fstat(int fd, struct _stat* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat32(jitter):
    """"
    [msvcrxx.dll] int _fstat32(int fd, struct _stat32* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat64(jitter):
    """"
    [msvcrxx.dll] int _fstat64(int fd, struct _stat64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstati64(jitter):
    """"
    [msvcrxx.dll] int _fstati64(int fd, struct _stati64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat32i64(jitter):
    """"
    [msvcrxx.dll] int _fstat32i64(int fd, struct _stat32i64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fstat64i32(jitter):
    """"
    [msvcrxx.dll] int _fstat64i32(int fd, struct _stat64i32* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_osfhandle(jitter):
    """"
    [msvcrxx.dll] intptr_t _get_osfhandle(int fd)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isatty(jitter):
    """"
    [msvcrxx.dll] int _isatty(int fd)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__locking(jitter):
    """"
    [msvcrxx.dll] int _locking(int fd, [_LK_MODE] mode, long nbytes)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "mode", "nbytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__open_osfhandle(jitter):
    """"
    [msvcrxx.dll] int _open_osfhandle(intptr_t osfhandle, int flags)
    """"
    ret_ad, args = jitter.func_args_cdecl(["osfhandle", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__access(jitter):
    """"
    [msvcrxx.dll] int _access(const char* path, int mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__waccess(jitter):
    """"
    [msvcrxx.dll] int _waccess(const wchar_t* path, int mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__access_s(jitter):
    """"
    [msvcrxx.dll] errno_t _access_s(const char* path, int mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__waccess_s(jitter):
    """"
    [msvcrxx.dll] errno_t _waccess_s(const wchar_t* path, int mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chmod(jitter):
    """"
    [msvcrxx.dll] int _chmod(const char* filename, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wchmod(jitter):
    """"
    [msvcrxx.dll] int _wchmod(const wchar_t* filename, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fullpath(jitter):
    """"
    [msvcrxx.dll] char* _fullpath(char* absPath, const char* relPath, size_t maxLength)
    """"
    ret_ad, args = jitter.func_args_cdecl(["absPath", "relPath", "maxLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fullpath_dbg(jitter):
    """"
    [msvcrxx.dll] char* _fullpath_dbg(char* absPath, const char* relPath, size_t maxLength, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["absPath", "relPath", "maxLength", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfullpath(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wfullpath(wchar_t* absPath, const wchar_t* relPath, size_t maxLength)
    """"
    ret_ad, args = jitter.func_args_cdecl(["absPath", "relPath", "maxLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfullpath_dbg(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wfullpath_dbg(wchar_t* absPath, const wchar_t* relPath, size_t maxLength, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["absPath", "relPath", "maxLength", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__makepath(jitter):
    """"
    [msvcrxx.dll] void _makepath(char* path, const char* drive, const char* dir, const char* fname, const char* ext)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmakepath(jitter):
    """"
    [msvcrxx.dll] void _wmakepath(wchar_t* path, const wchar_t* drive, const wchar_t* dir, const wchar_t* fname, const wchar_t* ext)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__makepath_s(jitter):
    """"
    [msvcrxx.dll] errno_t _makepath_s(char* path, size_t sizeInBytes, const char* drive, const char* dir, const char* fname, const char* ext)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "sizeInBytes", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmakepath_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wmakepath_s(wchar_t* path, size_t sizeInWords, const wchar_t* drive, const wchar_t* dir, const wchar_t* fname, const wchar_t* ext)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "sizeInWords", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mktemp(jitter):
    """"
    [msvcrxx.dll] char* _mktemp(char* template)
    """"
    ret_ad, args = jitter.func_args_cdecl(["template"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmktemp(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wmktemp(wchar_t* template)
    """"
    ret_ad, args = jitter.func_args_cdecl(["template"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mktemp_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mktemp_s(char* template, size_t sizeInChars)
    """"
    ret_ad, args = jitter.func_args_cdecl(["template", "sizeInChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wmktemp_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wmktemp_s(wchar_t* template, size_t sizeInChars)
    """"
    ret_ad, args = jitter.func_args_cdecl(["template", "sizeInChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_remove(jitter):
    """"
    [msvcrxx.dll] int remove(const char* path)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wremove(jitter):
    """"
    [msvcrxx.dll] int _wremove(const wchar_t* path)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_rename(jitter):
    """"
    [msvcrxx.dll] int rename(const char* oldname, const char* newname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["oldname", "newname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wrename(jitter):
    """"
    [msvcrxx.dll] int _wrename(const wchar_t* oldname, const wchar_t* newname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["oldname", "newname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__splitpath(jitter):
    """"
    [msvcrxx.dll] void _splitpath(const char* path, char* drive, char* dir, char* fname, char* ext)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsplitpath(jitter):
    """"
    [msvcrxx.dll] void _wsplitpath(const wchar_t* path, wchar_t* drive, wchar_t* dir, wchar_t* fname, wchar_t* ext)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "dir", "fname", "ext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__splitpath_s(jitter):
    """"
    [msvcrxx.dll] errno_t _splitpath_s(const char* path, char* drive, size_t driveNumberOfElements, char* dir, size_t dirNumberOfElements, char* fname, size_t nameNumberOfElements, char* ext, size_t extNumberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "driveNumberOfElements", "dir", "dirNumberOfElements", "fname", "nameNumberOfElements", "ext", "extNumberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsplitpath_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wsplitpath_s(const wchar_t* path, wchar_t* drive, size_t driveNumberOfElements, wchar_t* dir, size_t dirNumberOfElements, wchar_t* fname, size_t nameNumberOfElements, wchar_t* ext, size_t extNumberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "drive", "driveNumberOfElements", "dir", "dirNumberOfElements", "fname", "nameNumberOfElements", "ext", "extNumberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat(jitter):
    """"
    [msvcrxx.dll] int _stat(const char* path, struct _stat* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat32(jitter):
    """"
    [msvcrxx.dll] int _stat32(const char* path, struct _stat32* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat64(jitter):
    """"
    [msvcrxx.dll] int _stat64(const char* path, struct _stat64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stati64(jitter):
    """"
    [msvcrxx.dll] int _stati64(const char* path, struct _stati64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat32i64(jitter):
    """"
    [msvcrxx.dll] int _stat32i64(const char* path, struct _stat32i64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stat64i32(jitter):
    """"
    [msvcrxx.dll] int _stat64i32(const char* path, struct _stat64i32* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat(jitter):
    """"
    [msvcrxx.dll] int _wstat(const wchar_t* path, struct _stat* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat32(jitter):
    """"
    [msvcrxx.dll] int _wstat32(const wchar_t* path, struct _stat32* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat64(jitter):
    """"
    [msvcrxx.dll] int _wstat64(const wchar_t* path, struct _stat64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstati64(jitter):
    """"
    [msvcrxx.dll] int _wstati64(const wchar_t* path, struct _stati64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat32i64(jitter):
    """"
    [msvcrxx.dll] int _wstat32i64(const wchar_t* path, struct _stat32i64* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstat64i32(jitter):
    """"
    [msvcrxx.dll] int _wstat64i32(const wchar_t* path, struct _stat64i32* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__unlink(jitter):
    """"
    [msvcrxx.dll] int _unlink(const char* filename)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wunlink(jitter):
    """"
    [msvcrxx.dll] int _wunlink(const wchar_t* filename)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_acos(jitter):
    """"
    [msvcrxx.dll] double acos(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_acosf(jitter):
    """"
    [msvcrxx.dll] float acosf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_asin(jitter):
    """"
    [msvcrxx.dll] double asin(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_asinf(jitter):
    """"
    [msvcrxx.dll] float asinf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atan(jitter):
    """"
    [msvcrxx.dll] double atan(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atan2(jitter):
    """"
    [msvcrxx.dll] double atan2(double y, double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["y", "x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atanf(jitter):
    """"
    [msvcrxx.dll] float atanf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atan2f(jitter):
    """"
    [msvcrxx.dll] float atan2f(float y, float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["y", "x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cabs(jitter):
    """"
    [msvcrxx.dll] double _cabs(struct _complex z)
    """"
    ret_ad, args = jitter.func_args_cdecl(["z"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ceil(jitter):
    """"
    [msvcrxx.dll] double ceil(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ceilf(jitter):
    """"
    [msvcrxx.dll] float ceilf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chgsign(jitter):
    """"
    [msvcrxx.dll] double _chgsign(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__chgsignf(jitter):
    """"
    [msvcrxx.dll] float _chgsignf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__clearfp(jitter):
    """"
    [msvcrxx.dll] [_SW_FLOAT] _clearfp()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__control87(jitter):
    """"
    [msvcrxx.dll] unsigned int _control87([control_bits] new, [control_mask] mask)
    """"
    ret_ad, args = jitter.func_args_cdecl(["new", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__controlfp(jitter):
    """"
    [msvcrxx.dll] unsigned int _controlfp([control_bits] new, [control_mask] mask)
    """"
    ret_ad, args = jitter.func_args_cdecl(["new", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___control87_2(jitter):
    """"
    [msvcrxx.dll] int __control87_2([control_bits] new, [control_mask] mask, unsigned int* x86_cw, unsigned int* sse2_cw)
    """"
    ret_ad, args = jitter.func_args_cdecl(["new", "mask", "x86_cw", "sse2_cw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__controlfp_s(jitter):
    """"
    [msvcrxx.dll] errno_t _controlfp_s(unsigned int* currentControl, [control_bits] newControl, [control_mask] mask)
    """"
    ret_ad, args = jitter.func_args_cdecl(["currentControl", "newControl", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__copysign(jitter):
    """"
    [msvcrxx.dll] double _copysign(double x, double y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__copysignf(jitter):
    """"
    [msvcrxx.dll] float _copysignf(float x, float y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_cos(jitter):
    """"
    [msvcrxx.dll] double cos(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_cosf(jitter):
    """"
    [msvcrxx.dll] float cosf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_cosh(jitter):
    """"
    [msvcrxx.dll] double cosh(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_coshf(jitter):
    """"
    [msvcrxx.dll] float coshf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_div(jitter):
    """"
    [msvcrxx.dll] div_t div(int numer, int denom)
    """"
    ret_ad, args = jitter.func_args_cdecl(["numer", "denom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_exp(jitter):
    """"
    [msvcrxx.dll] double exp(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_expf(jitter):
    """"
    [msvcrxx.dll] float expf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fabs(jitter):
    """"
    [msvcrxx.dll] double fabs(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__finite(jitter):
    """"
    [msvcrxx.dll] int _finite(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_floor(jitter):
    """"
    [msvcrxx.dll] double floor(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_floorf(jitter):
    """"
    [msvcrxx.dll] float floorf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fmod(jitter):
    """"
    [msvcrxx.dll] double fmod(double x, double y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fmodf(jitter):
    """"
    [msvcrxx.dll] float fmodf(float x, float y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fpclass(jitter):
    """"
    [msvcrxx.dll] [_FPCLASS] _fpclass(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fpieee_flt(jitter):
    """"
    [msvcrxx.dll] int _fpieee_flt(unsigned long excCode, struct _EXCEPTION_POINTERS* excInfo, void* handler)
    """"
    ret_ad, args = jitter.func_args_cdecl(["excCode", "excInfo", "handler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fpreset(jitter):
    """"
    [msvcrxx.dll] void _fpreset()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_frexp(jitter):
    """"
    [msvcrxx.dll] double frexp(double x, int* expptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "expptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__hypot(jitter):
    """"
    [msvcrxx.dll] double _hypot(double x, double y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__hypotf(jitter):
    """"
    [msvcrxx.dll] float _hypotf(float x, float y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__isnan(jitter):
    """"
    [msvcrxx.dll] int _isnan(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ldexp(jitter):
    """"
    [msvcrxx.dll] double ldexp(double x, int exp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "exp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ldiv(jitter):
    """"
    [msvcrxx.dll] ldiv_t ldiv(long int numer, long int denom)
    """"
    ret_ad, args = jitter.func_args_cdecl(["numer", "denom"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_log(jitter):
    """"
    [msvcrxx.dll] double log(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_logf(jitter):
    """"
    [msvcrxx.dll] float logf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_log10(jitter):
    """"
    [msvcrxx.dll] double log10(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_log10f(jitter):
    """"
    [msvcrxx.dll] float log10f(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__logb(jitter):
    """"
    [msvcrxx.dll] double _logb(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lrotl(jitter):
    """"
    [msvcrxx.dll] unsigned long _lrotl(unsigned long value, int shift)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lrotr(jitter):
    """"
    [msvcrxx.dll] unsigned long _lrotr(unsigned long value, int shift)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__matherr(jitter):
    """"
    [msvcrxx.dll] int _matherr(struct _exception* except)
    """"
    ret_ad, args = jitter.func_args_cdecl(["except"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___setusermatherr(jitter):
    """"
    [msvcrxx.dll] void __setusermatherr(_HANDLE_MATH_ERROR pf)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_modf(jitter):
    """"
    [msvcrxx.dll] double modf(double x, double* intptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "intptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_modff(jitter):
    """"
    [msvcrxx.dll] float modff(float x, float* intptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "intptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__nextafter(jitter):
    """"
    [msvcrxx.dll] double _nextafter(double x, double y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_pow(jitter):
    """"
    [msvcrxx.dll] double pow(double x, double y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_powf(jitter):
    """"
    [msvcrxx.dll] float powf(float x, float y)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_rand(jitter):
    """"
    [msvcrxx.dll] int rand()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_rand_s(jitter):
    """"
    [msvcrxx.dll] errno_t rand_s(unsigned int* randomValue)
    """"
    ret_ad, args = jitter.func_args_cdecl(["randomValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rotl(jitter):
    """"
    [msvcrxx.dll] unsigned int _rotl(unsigned int value, int shift)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rotl64(jitter):
    """"
    [msvcrxx.dll] unsigned __int64 _rotl64(unsigned __int64 value, int shift)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rotr(jitter):
    """"
    [msvcrxx.dll] unsigned int _rotr(unsigned int value, int shift)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rotr64(jitter):
    """"
    [msvcrxx.dll] unsigned __int64 _rotr64(unsigned __int64 value, int shift)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value", "shift"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scalb(jitter):
    """"
    [msvcrxx.dll] double _scalb(double x, long exp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x", "exp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_controlfp(jitter):
    """"
    [msvcrxx.dll] void _set_controlfp(unsigned int newControl, unsigned int mask)
    """"
    ret_ad, args = jitter.func_args_cdecl(["newControl", "mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sin(jitter):
    """"
    [msvcrxx.dll] double sin(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sinf(jitter):
    """"
    [msvcrxx.dll] float sinf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sinh(jitter):
    """"
    [msvcrxx.dll] double sinh(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sinhf(jitter):
    """"
    [msvcrxx.dll] float sinhf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sqrt(jitter):
    """"
    [msvcrxx.dll] double sqrt(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sqrtf(jitter):
    """"
    [msvcrxx.dll] float sqrtf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_srand(jitter):
    """"
    [msvcrxx.dll] void srand(unsigned int seed)
    """"
    ret_ad, args = jitter.func_args_cdecl(["seed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__statusfp(jitter):
    """"
    [msvcrxx.dll] unsigned int _statusfp()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tan(jitter):
    """"
    [msvcrxx.dll] double tan(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tanf(jitter):
    """"
    [msvcrxx.dll] float tanf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tanh(jitter):
    """"
    [msvcrxx.dll] double tanh(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tanhf(jitter):
    """"
    [msvcrxx.dll] float tanhf(float x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__y0(jitter):
    """"
    [msvcrxx.dll] double _y0(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__y1(jitter):
    """"
    [msvcrxx.dll] double _y1(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__yn(jitter):
    """"
    [msvcrxx.dll] double _yn(int n, double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["n", "x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__j0(jitter):
    """"
    [msvcrxx.dll] double _j0(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__j1(jitter):
    """"
    [msvcrxx.dll] double _j1(double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__jn(jitter):
    """"
    [msvcrxx.dll] double _jn(int n, double x)
    """"
    ret_ad, args = jitter.func_args_cdecl(["n", "x"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_SSE2_enable(jitter):
    """"
    [msvcrxx.dll] int _set_SSE2_enable(int flag)
    """"
    ret_ad, args = jitter.func_args_cdecl(["flag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_fmode(jitter):
    """"
    [msvcrxx.dll] errno_t _set_fmode([file_translation_mode] mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_fmode(jitter):
    """"
    [msvcrxx.dll] errno_t _get_fmode([file_translation_mode*] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__setmode(jitter):
    """"
    [msvcrxx.dll] [file_translation_mode] _setmode(int fd, [file_translation_mode] mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___p__fmode(jitter):
    """"
    [msvcrxx.dll] [file_translation_mode*] __p__fmode()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_clearerr(jitter):
    """"
    [msvcrxx.dll] void clearerr(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_clearerr_s(jitter):
    """"
    [msvcrxx.dll] errno_t clearerr_s(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fclose(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fclose(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fcloseall(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fcloseall()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fdopen(jitter):
    """"
    [msvcrxx.dll] FILE* _fdopen(int fd, const char* mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfdopen(jitter):
    """"
    [msvcrxx.dll] FILE* _wfdopen(int fd, const wchar_t* mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_feof(jitter):
    """"
    [msvcrxx.dll] int feof(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ferror(jitter):
    """"
    [msvcrxx.dll] int ferror(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fflush(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fflush(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgetc(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fgetc(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgetwc(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] fgetwc(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgetpos(jitter):
    """"
    [msvcrxx.dll] int fgetpos(FILE* stream, fpos_t* pos)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "pos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgets(jitter):
    """"
    [msvcrxx.dll] char* fgets(char* str, int n, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "n", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fgetws(jitter):
    """"
    [msvcrxx.dll] wchar_t* fgetws(wchar_t* str, int n, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "n", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fileno(jitter):
    """"
    [msvcrxx.dll] int _fileno(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__flushall(jitter):
    """"
    [msvcrxx.dll] int _flushall()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fopen(jitter):
    """"
    [msvcrxx.dll] FILE* fopen(const char* filename, const char* mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfopen(jitter):
    """"
    [msvcrxx.dll] FILE* _wfopen(const wchar_t* filename, const wchar_t* mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fopen_s(jitter):
    """"
    [msvcrxx.dll] errno_t fopen_s(FILE** pFile, const char* filename, const char* mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pFile", "filename", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfopen_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wfopen_s(FILE** pFile, const wchar_t* filename, const wchar_t* mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pFile", "filename", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fprintf(jitter):
    """"
    [msvcrxx.dll] int fprintf(FILE* stream, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fprintf_l(jitter):
    """"
    [msvcrxx.dll] int _fprintf_l(FILE* stream, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwprintf(jitter):
    """"
    [msvcrxx.dll] int fwprintf(FILE* stream, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _fwprintf_l(FILE* stream, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fprintf_s(jitter):
    """"
    [msvcrxx.dll] int fprintf_s(FILE* stream, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _fprintf_s_l(FILE* stream, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwprintf_s(jitter):
    """"
    [msvcrxx.dll] int fwprintf_s(FILE* stream, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _fwprintf_s_l(FILE* stream, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fputc(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fputc(int c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fputwc(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] fputwc(wchar_t c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fputs(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fputs(const char* str, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fputws(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF_INT] fputws(const wchar_t* str, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fread(jitter):
    """"
    [msvcrxx.dll] size_t fread(void* buffer, size_t size, size_t count, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "size", "count", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_freopen(jitter):
    """"
    [msvcrxx.dll] FILE* freopen(const char* path, const char* mode, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "mode", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfreopen(jitter):
    """"
    [msvcrxx.dll] FILE* _wfreopen(const wchar_t* path, const wchar_t* mode, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["path", "mode", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_freopen_s(jitter):
    """"
    [msvcrxx.dll] errno_t freopen_s(FILE** pFile, const char* path, const char* mode, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pFile", "path", "mode", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfreopen_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wfreopen_s(FILE** pFile, const wchar_t* path, const wchar_t* mode, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pFile", "path", "mode", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fscanf(FILE* stream, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fscanf_l(FILE* stream, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fwscanf(FILE* stream, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fwscanf_l(FILE* stream, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fscanf_s(FILE* stream, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fscanf_s_l(FILE* stream, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] fwscanf_s(FILE* stream, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fwscanf_s_l(FILE* stream, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fseek(jitter):
    """"
    [msvcrxx.dll] int fseek(FILE* stream, long offset, [SEEK_TYPE] origin)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fseeki64(jitter):
    """"
    [msvcrxx.dll] int _fseeki64(FILE* stream, __int64 offset, [SEEK_TYPE] origin)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fsetpos(jitter):
    """"
    [msvcrxx.dll] int fsetpos(FILE* stream, const fpos_t* pos)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "pos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fsopen(jitter):
    """"
    [msvcrxx.dll] FILE* _fsopen(const char* filename, const char* mode, [share_flag] shflag)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "mode", "shflag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfsopen(jitter):
    """"
    [msvcrxx.dll] FILE* _wfsopen(const wchar_t* filename, const wchar_t* mode, [share_flag] shflag)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "mode", "shflag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ftell(jitter):
    """"
    [msvcrxx.dll] long ftell(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftelli64(jitter):
    """"
    [msvcrxx.dll] __int64 _ftelli64(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_fwrite(jitter):
    """"
    [msvcrxx.dll] size_t fwrite(const void* buffer, size_t size, size_t count, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "size", "count", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getc(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] getc(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getwc(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] getwc(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getmaxstdio(jitter):
    """"
    [msvcrxx.dll] int _getmaxstdio()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_gets(jitter):
    """"
    [msvcrxx.dll] char* gets(char* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getws(jitter):
    """"
    [msvcrxx.dll] wchar_t* _getws(wchar_t* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_gets_s(jitter):
    """"
    [msvcrxx.dll] char* gets_s(char* buffer, size_t sizeInCharacters)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInCharacters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getws_s(jitter):
    """"
    [msvcrxx.dll] wchar_t* _getws_s(wchar_t* buffer, size_t sizeInCharacters)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInCharacters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getw(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _getw(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_putc(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] putc(int c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_putwc(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] putwc(wchar_t c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_puts(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] puts(const char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putws(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF_INT] _putws(const wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putw(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _putw(int binint, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["binint", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_rewind(jitter):
    """"
    [msvcrxx.dll] void rewind(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__rmtmp(jitter):
    """"
    [msvcrxx.dll] int _rmtmp()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_setbuf(jitter):
    """"
    [msvcrxx.dll] void setbuf(FILE* stream, char* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__setmaxstdio(jitter):
    """"
    [msvcrxx.dll] int _setmaxstdio(int newmax)
    """"
    ret_ad, args = jitter.func_args_cdecl(["newmax"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_setvbuf(jitter):
    """"
    [msvcrxx.dll] int setvbuf(FILE* stream, char* buffer, [buffer_mode] mode, size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "buffer", "mode", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tempnam(jitter):
    """"
    [msvcrxx.dll] char* _tempnam(const char* dir, const char* prefix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dir", "prefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tempnam_dbg(jitter):
    """"
    [msvcrxx.dll] char* _tempnam_dbg(const char* dir, const char* prefix, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dir", "prefix", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtempnam(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wtempnam(const wchar_t* dir, const wchar_t* prefix)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dir", "prefix"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtempnam_dbg(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wtempnam_dbg(const wchar_t* dir, const wchar_t* prefix, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dir", "prefix", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tmpnam(jitter):
    """"
    [msvcrxx.dll] char* tmpnam(char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtmpnam(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wtmpnam(wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tmpfile(jitter):
    """"
    [msvcrxx.dll] FILE* tmpfile()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tmpfile_s(jitter):
    """"
    [msvcrxx.dll] errno_t tmpfile_s(FILE** pFilePtr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pFilePtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_tmpnam_s(jitter):
    """"
    [msvcrxx.dll] errno_t tmpnam_s(char* str, size_t sizeInChars)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "sizeInChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wtmpnam_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wtmpnam_s(wchar_t* str, size_t sizeInChars)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "sizeInChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ungetc(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] ungetc(int c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ungetwc(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] ungetwc(wint_t c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_s(jitter):
    """"
    [msvcrxx.dll] int _vcprintf_s(const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vcprintf_s_l(const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_s(jitter):
    """"
    [msvcrxx.dll] int _vcwprintf_s(const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vcwprintf_s_l(const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vfprintf_s(jitter):
    """"
    [msvcrxx.dll] int vfprintf_s(FILE* stream, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vfprintf_s_l(FILE* stream, const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vfwprintf_s(jitter):
    """"
    [msvcrxx.dll] int vfwprintf_s(FILE* stream, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfwprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vfwprintf_s_l(FILE* stream, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vprintf_s(jitter):
    """"
    [msvcrxx.dll] int vprintf_s(const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vprintf_s_l(const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vwprintf_s(jitter):
    """"
    [msvcrxx.dll] int vwprintf_s(const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vwprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vwprintf_s_l(const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_printf(jitter):
    """"
    [msvcrxx.dll] int printf(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__printf_l(jitter):
    """"
    [msvcrxx.dll] int _printf_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wprintf(jitter):
    """"
    [msvcrxx.dll] int wprintf(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wprintf_l(jitter):
    """"
    [msvcrxx.dll] int _wprintf_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_printf_s(jitter):
    """"
    [msvcrxx.dll] int printf_s(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__printf_s_l(jitter):
    """"
    [msvcrxx.dll] int _printf_s_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wprintf_s(jitter):
    """"
    [msvcrxx.dll] int wprintf_s(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _wprintf_s_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_scanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] scanf(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _scanf_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] wscanf(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _wscanf_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_scanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] scanf_s(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _scanf_s_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] wscanf_s(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _wscanf_s_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf(jitter):
    """"
    [msvcrxx.dll] int _vcprintf(const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vcprintf_l(const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf(jitter):
    """"
    [msvcrxx.dll] int _vcwprintf(const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vcwprintf_l(const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vcprintf_p(const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vcprintf_p_l(const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vcwprintf_p(const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vcwprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vcwprintf_p_l(const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vfprintf(jitter):
    """"
    [msvcrxx.dll] int vfprintf(FILE* stream, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vfprintf_l(FILE* stream, const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vfwprintf(jitter):
    """"
    [msvcrxx.dll] int vfwprintf(FILE* stream, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vfwprintf_l(FILE* stream, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vfprintf_p(FILE* stream, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vfprintf_p_l(FILE* stream, const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfwprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vfwprintf_p(FILE* stream, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vfwprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vfwprintf_p_l(FILE* stream, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vprintf(jitter):
    """"
    [msvcrxx.dll] int vprintf(const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vprintf_l(const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vwprintf(jitter):
    """"
    [msvcrxx.dll] int vwprintf(const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vwprintf_l(const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vprintf_p(const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vprintf_p_l(const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vwprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vwprintf_p(const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vwprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vwprintf_p_l(const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscprintf(jitter):
    """"
    [msvcrxx.dll] int _vscprintf(const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vscprintf_l(const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscwprintf(jitter):
    """"
    [msvcrxx.dll] int _vscwprintf(const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vscwprintf_l(const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vscprintf_p(const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vscprintf_p_l(const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscwprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vscwprintf_p(const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vscwprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vscwprintf_p_l(const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wprintf_p(jitter):
    """"
    [msvcrxx.dll] int _wprintf_p(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _wprintf_p_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fprintf_p(jitter):
    """"
    [msvcrxx.dll] int _fprintf_p(FILE* stream, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _fprintf_p_l(FILE* stream, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwprintf_p(jitter):
    """"
    [msvcrxx.dll] int _fwprintf_p(FILE* stream, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _fwprintf_p_l(FILE* stream, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__printf_p(jitter):
    """"
    [msvcrxx.dll] int _printf_p(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__printf_p_l(jitter):
    """"
    [msvcrxx.dll] int _printf_p_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_putchar(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] putchar(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_putwchar(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] putwchar(wchar_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getchar(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] getchar()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getwchar(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] getwchar()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fgetchar(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fgetchar()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fgetwchar(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _fgetwchar()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fputchar(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fputchar(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fputwchar(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _fputwchar(wchar_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lock_file(jitter):
    """"
    [msvcrxx.dll] void _lock_file(FILE* file)
    """"
    ret_ad, args = jitter.func_args_cdecl(["file"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__unlock_file(jitter):
    """"
    [msvcrxx.dll] void _unlock_file(FILE* file)
    """"
    ret_ad, args = jitter.func_args_cdecl(["file"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__close(jitter):
    """"
    [msvcrxx.dll] int _close(int fd)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__commit(jitter):
    """"
    [msvcrxx.dll] int _commit(int fd)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__creat(jitter):
    """"
    [msvcrxx.dll] int _creat(const char* filename, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcreat(jitter):
    """"
    [msvcrxx.dll] int _wcreat(const wchar_t* filename, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__dup(jitter):
    """"
    [msvcrxx.dll] int _dup(int fd)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__dup2(jitter):
    """"
    [msvcrxx.dll] int _dup2(int fd1, int fd2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd1", "fd2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__eof(jitter):
    """"
    [msvcrxx.dll] int _eof(int fd)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lseek(jitter):
    """"
    [msvcrxx.dll] long _lseek(int fd, long offset, [SEEK_TYPE] origin)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lseeki64(jitter):
    """"
    [msvcrxx.dll] __int64 _lseeki64(int fd, __int64 offset, [SEEK_TYPE] origin)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__open(jitter):
    """"
    [msvcrxx.dll] int _open(const char* filename, [open_flag] oflag, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "oflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wopen(jitter):
    """"
    [msvcrxx.dll] int _wopen(const wchar_t* filename, [open_flag] oflag, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "oflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__read(jitter):
    """"
    [msvcrxx.dll] int _read(int fd, void* buffer, unsigned int count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sopen(jitter):
    """"
    [msvcrxx.dll] int _sopen(const char* filename, [open_flag] oflag, [share_flag] shflag, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "oflag", "shflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsopen(jitter):
    """"
    [msvcrxx.dll] int _wsopen(const wchar_t* filename, [open_flag] oflag, [share_flag] shflag, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "oflag", "shflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sopen_s(jitter):
    """"
    [msvcrxx.dll] errno_t _sopen_s(int* pfh, const char* filename, [open_flag] oflag, [share_flag] shflag, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pfh", "filename", "oflag", "shflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsopen_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wsopen_s(int* pfh, const wchar_t* filename, [open_flag] oflag, [share_flag] shflag, [perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pfh", "filename", "oflag", "shflag", "pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tell(jitter):
    """"
    [msvcrxx.dll] long _tell(int handle)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__telli64(jitter):
    """"
    [msvcrxx.dll] __int64 _telli64(int handle)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__umask(jitter):
    """"
    [msvcrxx.dll] [perm_mode] _umask([perm_mode] pmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__umask_s(jitter):
    """"
    [msvcrxx.dll] errno_t _umask_s([perm_mode] mode, [perm_mode*] pOldMode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "pOldMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__write(jitter):
    """"
    [msvcrxx.dll] int _write(int fd, const void* buffer, unsigned int count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "buffer", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cgets(jitter):
    """"
    [msvcrxx.dll] char* _cgets(char* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cgetws(jitter):
    """"
    [msvcrxx.dll] wchar_t* _cgetws(wchar_t* buffer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cgets_s(jitter):
    """"
    [msvcrxx.dll] errno_t _cgets_s(char* buffer, size_t numberOfElements, size_t* pSizeRead)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "pSizeRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cgetws_s(jitter):
    """"
    [msvcrxx.dll] errno_t _cgetws_s(wchar_t* buffer, size_t* pSizeRead)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "pSizeRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf(jitter):
    """"
    [msvcrxx.dll] int _cprintf(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_l(jitter):
    """"
    [msvcrxx.dll] int _cprintf_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf(jitter):
    """"
    [msvcrxx.dll] int _cwprintf(const wchar* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _cwprintf_l(const wchar* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_s(jitter):
    """"
    [msvcrxx.dll] int _cprintf_s(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _cprintf_s_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_s(jitter):
    """"
    [msvcrxx.dll] int _cwprintf_s(const wchar* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _cwprintf_s_l(const wchar* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cputs(jitter):
    """"
    [msvcrxx.dll] int _cputs(const char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cputws(jitter):
    """"
    [msvcrxx.dll] int _cputws(const wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _cscanf(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _cscanf_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _cwscanf(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _cwscanf_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _cscanf_s(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _cscanf_s_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _cwscanf_s(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _cwscanf_s_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getch(jitter):
    """"
    [msvcrxx.dll] int _getch()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getwch(jitter):
    """"
    [msvcrxx.dll] wint_t _getwch()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getche(jitter):
    """"
    [msvcrxx.dll] int _getche()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getwche(jitter):
    """"
    [msvcrxx.dll] wint_t _getwche()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__inp(jitter):
    """"
    [msvcrxx.dll] int _inp(unsigned short port)
    """"
    ret_ad, args = jitter.func_args_cdecl(["port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__inpw(jitter):
    """"
    [msvcrxx.dll] unsigned short _inpw(unsigned short port)
    """"
    ret_ad, args = jitter.func_args_cdecl(["port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__inpd(jitter):
    """"
    [msvcrxx.dll] unsigned long _inpd(unsigned short port)
    """"
    ret_ad, args = jitter.func_args_cdecl(["port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__kbhit(jitter):
    """"
    [msvcrxx.dll] int _kbhit()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__outp(jitter):
    """"
    [msvcrxx.dll] int _outp(unsigned short port, int databyte)
    """"
    ret_ad, args = jitter.func_args_cdecl(["port", "databyte"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__outpw(jitter):
    """"
    [msvcrxx.dll] unsigned short _outpw(unsigned short port, unsigned short dataword)
    """"
    ret_ad, args = jitter.func_args_cdecl(["port", "dataword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__outpd(jitter):
    """"
    [msvcrxx.dll] unsigned long _outpd(unsigned short port, unsigned long dataword)
    """"
    ret_ad, args = jitter.func_args_cdecl(["port", "dataword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putch(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _putch(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putwch(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _putwch(wchar_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetch(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _ungetch(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetwch(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _ungetwch(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_p(jitter):
    """"
    [msvcrxx.dll] int _cprintf_p(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _cprintf_p_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_p(jitter):
    """"
    [msvcrxx.dll] int _cwprintf_p(const wchar* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _cwprintf_p_l(const wchar* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fclose_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fclose_nolock(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fflush_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _fflush_nolock(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fgetwc_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _fgetwc_nolock(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fread_nolock(jitter):
    """"
    [msvcrxx.dll] size_t _fread_nolock(void* buffer, size_t size, size_t count, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "size", "count", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fseek_nolock(jitter):
    """"
    [msvcrxx.dll] int _fseek_nolock(FILE* stream, long offset, [SEEK_TYPE] origin)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fseeki64_nolock(jitter):
    """"
    [msvcrxx.dll] int _fseeki64_nolock(FILE* stream, __int64 offset, [SEEK_TYPE] origin)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream", "offset", "origin"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftell_nolock(jitter):
    """"
    [msvcrxx.dll] long _ftell_nolock(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftelli64_nolock(jitter):
    """"
    [msvcrxx.dll] __int64 _ftelli64_nolock(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fwrite_nolock(jitter):
    """"
    [msvcrxx.dll] size_t _fwrite_nolock(const void* buffer, size_t size, size_t count, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "size", "count", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getc_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _getc_nolock(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getch_nolock(jitter):
    """"
    [msvcrxx.dll] int _getch_nolock()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getwch_nolock(jitter):
    """"
    [msvcrxx.dll] wint_t _getwch_nolock()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getche_nolock(jitter):
    """"
    [msvcrxx.dll] int _getche_nolock()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getwche_nolock(jitter):
    """"
    [msvcrxx.dll] wint_t _getwche_nolock()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdcwd_nolock(jitter):
    """"
    [msvcrxx.dll] char* _getdcwd_nolock(int drive, char* buffer, int maxlen)
    """"
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetdcwd_nolock(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wgetdcwd_nolock(int drive, wchar_t* buffer, int maxlen)
    """"
    ret_ad, args = jitter.func_args_cdecl(["drive", "buffer", "maxlen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putch_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _putch_nolock(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putwch_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _putwch_nolock(wchar_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetc_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _ungetc_nolock(int c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetwc_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _ungetwc_nolock(wint_t c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetch_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _ungetch_nolock(int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ungetwch_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _ungetwch_nolock(wint_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__fputwc_nolock(jitter):
    """"
    [msvcrxx.dll] [RET_WEOF] _fputwc_nolock(wchar_t c, FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c", "stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_setlocale(jitter):
    """"
    [msvcrxx.dll] char* setlocale([locale_category] category, const char* locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["category", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsetlocale(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wsetlocale([locale_category] category, const wchar_t* locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["category", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__create_locale(jitter):
    """"
    [msvcrxx.dll] _locale_t _create_locale([locale_category] category, const char* locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["category", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___create_locale(jitter):
    """"
    [msvcrxx.dll] _locale_t __create_locale([locale_category] category, const char* locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["category", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__free_locale(jitter):
    """"
    [msvcrxx.dll] void _free_locale(_locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___free_locale(jitter):
    """"
    [msvcrxx.dll] void __free_locale(_locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_current_locale(jitter):
    """"
    [msvcrxx.dll] _locale_t _get_current_locale()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___get_current_locale(jitter):
    """"
    [msvcrxx.dll] _locale_t __get_current_locale()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__configthreadlocale(jitter):
    """"
    [msvcrxx.dll] [thread_locale_type] _configthreadlocale([thread_locale_type] type)
    """"
    ret_ad, args = jitter.func_args_cdecl(["type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_localeconv(jitter):
    """"
    [msvcrxx.dll] struct lconv* localeconv()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbccpy(jitter):
    """"
    [msvcrxx.dll] void _mbccpy(unsigned char* dest, const unsigned char* src)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "src"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbccpy_l(jitter):
    """"
    [msvcrxx.dll] void _mbccpy_l(unsigned char* dest, const unsigned char* src, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbccpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbccpy_s(unsigned char* dest, size_t buffSizeInBytes, int* pCopied, const unsigned char* src)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "buffSizeInBytes", "pCopied", "src"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbccpy_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbccpy_s_l(unsigned char* dest, size_t buffSizeInBytes, int* pCopied, const unsigned char* src, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "buffSizeInBytes", "pCopied", "src", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getmbcp(jitter):
    """"
    [msvcrxx.dll] int _getmbcp()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__setmbcp(jitter):
    """"
    [msvcrxx.dll] int _setmbcp([_MB_CP_TYPE] codepage)
    """"
    ret_ad, args = jitter.func_args_cdecl(["codepage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx____mb_cur_max_func(jitter):
    """"
    [msvcrxx.dll] int ___mb_cur_max_func()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___mb_cur_max(jitter):
    """"
    [msvcrxx.dll] int __mb_cur_max()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx____lc_codepage_func(jitter):
    """"
    [msvcrxx.dll] UINT ___lc_codepage_func()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx____lc_handle_func(jitter):
    """"
    [msvcrxx.dll] LCID* ___lc_handle_func()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___crtLCMapStringW(jitter):
    """"
    [msvcrxx.dll] int __crtLCMapStringW(LCID Locale, [LocaleMappingFlags] dwMapFlags, LPCWSTR lpSrcStr, int cchSrc, LPWSTR lpDestStr, int cchDest)
    """"
    ret_ad, args = jitter.func_args_cdecl(["Locale", "dwMapFlags", "lpSrcStr", "cchSrc", "lpDestStr", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_calloc(jitter):
    """"
    [msvcrxx.dll] void* calloc(size_t num, size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["num", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??3@YAXPAX@Z(jitter):
    """"
    [msvcrxx.dll] void ??3@YAXPAX@Z(void* object)
    """"
    ret_ad, args = jitter.func_args_cdecl(["object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??3@YAXPEAX@Z(jitter):
    """"
    [msvcrxx.dll] void ??3@YAXPEAX@Z(void* object)
    """"
    ret_ad, args = jitter.func_args_cdecl(["object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??_V@YAXPAX@Z(jitter):
    """"
    [msvcrxx.dll] void ??_V@YAXPAX@Z(void* object)
    """"
    ret_ad, args = jitter.func_args_cdecl(["object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??_V@YAXPEAX@Z(jitter):
    """"
    [msvcrxx.dll] void ??_V@YAXPEAX@Z(void* object)
    """"
    ret_ad, args = jitter.func_args_cdecl(["object"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__expand(jitter):
    """"
    [msvcrxx.dll] void* _expand(void* memblock, size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_free(jitter):
    """"
    [msvcrxx.dll] void free(void* memblock)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__freea(jitter):
    """"
    [msvcrxx.dll] void _freea(void* memblock)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_heap_handle(jitter):
    """"
    [msvcrxx.dll] intptr_t _get_heap_handle()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_sbh_threshold(jitter):
    """"
    [msvcrxx.dll] size_t _get_sbh_threshold()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapadd(jitter):
    """"
    [msvcrxx.dll] int _heapadd(void* memblock, size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapchk(jitter):
    """"
    [msvcrxx.dll] [HEAP_RESULT] _heapchk()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapmin(jitter):
    """"
    [msvcrxx.dll] int _heapmin()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapset(jitter):
    """"
    [msvcrxx.dll] [HEAP_RESULT] _heapset(unsigned int fill)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fill"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__heapwalk(jitter):
    """"
    [msvcrxx.dll] [HEAP_RESULT] _heapwalk(_HEAPINFO* entryinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["entryinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_malloc(jitter):
    """"
    [msvcrxx.dll] void* malloc(size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__msize(jitter):
    """"
    [msvcrxx.dll] size_t _msize(void* memblock)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??2@YAPAXI@Z(jitter):
    """"
    [msvcrxx.dll] void* ??2@YAPAXI@Z(size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??2@YAPEAX_K@Z(jitter):
    """"
    [msvcrxx.dll] void* ??2@YAPEAX_K@Z(size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??_U@YAPAXI@Z(jitter):
    """"
    [msvcrxx.dll] void* ??_U@YAPAXI@Z(size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_??_U@YAPEAX_K@Z(jitter):
    """"
    [msvcrxx.dll] void* ??_U@YAPEAX_K@Z(size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_query_new_handler@@YAP6AHI@ZXZ(jitter):
    """"
    [msvcrxx.dll] _PNH ?_query_new_handler@@YAP6AHI@ZXZ()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_query_new_mode@@YAHXZ(jitter):
    """"
    [msvcrxx.dll] int ?_query_new_mode@@YAHXZ()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_realloc(jitter):
    """"
    [msvcrxx.dll] void* realloc(void* memblock, size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__callnewh(jitter):
    """"
    [msvcrxx.dll] int _callnewh(size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_set_new_handler@@YAP6AHI@ZP6AHI@Z@Z(jitter):
    """"
    [msvcrxx.dll] _PNH ?_set_new_handler@@YAP6AHI@ZP6AHI@Z@Z(_PNH pNewHandler)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pNewHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_?_set_new_mode@@YAHH@Z(jitter):
    """"
    [msvcrxx.dll] int ?_set_new_mode@@YAHH@Z(int newhandlermode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["newhandlermode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__expand_dbg(jitter):
    """"
    [msvcrxx.dll] void* _expand_dbg(void* userData, size_t newSize, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["userData", "newSize", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__calloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _calloc_dbg(size_t num, size_t size, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["num", "size", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__free_dbg(jitter):
    """"
    [msvcrxx.dll] void _free_dbg(void* userData, [DBG_BLOCK_TYPE] blockType)
    """"
    ret_ad, args = jitter.func_args_cdecl(["userData", "blockType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__malloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _malloc_dbg(size_t size, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["size", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__msize_dbg(jitter):
    """"
    [msvcrxx.dll] size_t _msize_dbg(void* userData, [DBG_BLOCK_TYPE] blockType)
    """"
    ret_ad, args = jitter.func_args_cdecl(["userData", "blockType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__realloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _realloc_dbg(void* userData, size_t newSize, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["userData", "newSize", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__recalloc(jitter):
    """"
    [msvcrxx.dll] void* _recalloc(void* memblock, size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["memblock", "size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__recalloc_dbg(jitter):
    """"
    [msvcrxx.dll] void* _recalloc_dbg(void* userData, size_t num, size_t size, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["userData", "num", "size", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_amblksiz(jitter):
    """"
    [msvcrxx.dll] errno_t _get_amblksiz(size_t* blockSize)
    """"
    ret_ad, args = jitter.func_args_cdecl(["blockSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_amblksiz(jitter):
    """"
    [msvcrxx.dll] errno_t _set_amblksiz(size_t blockSize)
    """"
    ret_ad, args = jitter.func_args_cdecl(["blockSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_sbh_threshold(jitter):
    """"
    [msvcrxx.dll] int _set_sbh_threshold(size_t size)
    """"
    ret_ad, args = jitter.func_args_cdecl(["size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_abort(jitter):
    """"
    [msvcrxx.dll] void abort()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_atexit(jitter):
    """"
    [msvcrxx.dll] int atexit(void* func)
    """"
    ret_ad, args = jitter.func_args_cdecl(["func"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__beginthread(jitter):
    """"
    [msvcrxx.dll] uintptr_t _beginthread(void* start_address, unsigned stack_size, void* arglist)
    """"
    ret_ad, args = jitter.func_args_cdecl(["start_address", "stack_size", "arglist"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__beginthreadex(jitter):
    """"
    [msvcrxx.dll] uintptr_t _beginthreadex(void* security, unsigned stack_size, void* start_address, void* arglist, [thread_initflag] initflag, unsigned* thrdaddr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["security", "stack_size", "start_address", "arglist", "initflag", "thrdaddr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cexit(jitter):
    """"
    [msvcrxx.dll] void _cexit()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__c_exit(jitter):
    """"
    [msvcrxx.dll] void _c_exit()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__cwait(jitter):
    """"
    [msvcrxx.dll] intptr_t _cwait(int* termstat, intptr_t procHandle, int action)
    """"
    ret_ad, args = jitter.func_args_cdecl(["termstat", "procHandle", "action"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__endthread(jitter):
    """"
    [msvcrxx.dll] void _endthread()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__endthreadex(jitter):
    """"
    [msvcrxx.dll] void _endthreadex(unsigned retval)
    """"
    ret_ad, args = jitter.func_args_cdecl(["retval"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execl(jitter):
    """"
    [msvcrxx.dll] intptr_t _execl(const char* cmdname, const char* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecl(jitter):
    """"
    [msvcrxx.dll] intptr_t _wexecl(const wchar_t* cmdname, const wchar_t* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execle(jitter):
    """"
    [msvcrxx.dll] intptr_t _execle(const char* cmdname, const char* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecle(jitter):
    """"
    [msvcrxx.dll] intptr_t _wexecle(const wchar_t* cmdname, const wchar_t* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execlp(jitter):
    """"
    [msvcrxx.dll] intptr_t _execlp(const char* cmdname, const char* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexeclp(jitter):
    """"
    [msvcrxx.dll] intptr_t _wexeclp(const wchar_t* cmdname, const wchar_t* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execlpe(jitter):
    """"
    [msvcrxx.dll] intptr_t _execlpe(const char* cmdname, const char* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexeclpe(jitter):
    """"
    [msvcrxx.dll] intptr_t _wexeclpe(const wchar_t* cmdname, const wchar_t* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execv(jitter):
    """"
    [msvcrxx.dll] intptr_t _execv(const char* cmdname, const char** argv)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecv(jitter):
    """"
    [msvcrxx.dll] intptr_t _wexecv(const wchar_t* cmdname, const wchar_t** argv)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execve(jitter):
    """"
    [msvcrxx.dll] intptr_t _execve(const char* cmdname, const char** argv, const char** envp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecve(jitter):
    """"
    [msvcrxx.dll] intptr_t _wexecve(const wchar_t* cmdname, const wchar_t** argv, const wchar_t** envp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execvp(jitter):
    """"
    [msvcrxx.dll] intptr_t _execvp(const char* cmdname, const char** argv)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecvp(jitter):
    """"
    [msvcrxx.dll] intptr_t _wexecvp(const wchar_t* cmdname, const wchar_t** argv)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__execvpe(jitter):
    """"
    [msvcrxx.dll] intptr_t _execvpe(const char* cmdname, const char** argv, const char** envp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wexecvpe(jitter):
    """"
    [msvcrxx.dll] intptr_t _wexecvpe(const wchar_t* cmdname, const wchar_t** argv, const wchar_t** envp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_exit(jitter):
    """"
    [msvcrxx.dll] void exit(int status)
    """"
    ret_ad, args = jitter.func_args_cdecl(["status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__exit(jitter):
    """"
    [msvcrxx.dll] void _exit(int status)
    """"
    ret_ad, args = jitter.func_args_cdecl(["status"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getenv(jitter):
    """"
    [msvcrxx.dll] char* getenv(const char* varname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetenv(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wgetenv(const wchar_t* varname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_getenv_s(jitter):
    """"
    [msvcrxx.dll] errno_t getenv_s(size_t* pReturnValue, char* buffer, size_t numberOfElements, const char* varname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "buffer", "numberOfElements", "varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wgetenv_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wgetenv_s(size_t* pReturnValue, wchar_t* buffer, size_t numberOfElements, const wchar_t* varname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "buffer", "numberOfElements", "varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getpid(jitter):
    """"
    [msvcrxx.dll] int _getpid()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__onexit(jitter):
    """"
    [msvcrxx.dll] _onexit_t _onexit(_onexit_t function)
    """"
    ret_ad, args = jitter.func_args_cdecl(["function"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__pclose(jitter):
    """"
    [msvcrxx.dll] int _pclose(FILE* stream)
    """"
    ret_ad, args = jitter.func_args_cdecl(["stream"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_perror(jitter):
    """"
    [msvcrxx.dll] void perror(const char* string)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wperror(jitter):
    """"
    [msvcrxx.dll] void _wperror(const wchar_t* string)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__pipe(jitter):
    """"
    [msvcrxx.dll] int _pipe(int* pfds, unsigned int psize, [open_flag] textmode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pfds", "psize", "textmode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__popen(jitter):
    """"
    [msvcrxx.dll] FILE* _popen(const char* command, const char* mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["command", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wpopen(jitter):
    """"
    [msvcrxx.dll] FILE* _wpopen(const wchar_t* command, const wchar_t* mode)
    """"
    ret_ad, args = jitter.func_args_cdecl(["command", "mode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putenv(jitter):
    """"
    [msvcrxx.dll] int _putenv(const char* envstring)
    """"
    ret_ad, args = jitter.func_args_cdecl(["envstring"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wputenv(jitter):
    """"
    [msvcrxx.dll] int _wputenv(const wchar_t* envstring)
    """"
    ret_ad, args = jitter.func_args_cdecl(["envstring"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__putenv_s(jitter):
    """"
    [msvcrxx.dll] errno_t _putenv_s(const char* name, const char* value)
    """"
    ret_ad, args = jitter.func_args_cdecl(["name", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wputenv_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wputenv_s(const wchar_t* name, const wchar_t* value)
    """"
    ret_ad, args = jitter.func_args_cdecl(["name", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_raise(jitter):
    """"
    [msvcrxx.dll] int raise([SIGNAL] sig)
    """"
    ret_ad, args = jitter.func_args_cdecl(["sig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_signal(jitter):
    """"
    [msvcrxx.dll] [SIGNAL_FUNC] signal([SIGNAL] sig, [SIGNAL_FUNC] func)
    """"
    ret_ad, args = jitter.func_args_cdecl(["sig", "func"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnl(jitter):
    """"
    [msvcrxx.dll] intptr_t _spawnl([spawn_mode] mode, const char* cmdname, const char* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnl(jitter):
    """"
    [msvcrxx.dll] intptr_t _wspawnl([spawn_mode] mode, const wchar_t* cmdname, const wchar_t* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnle(jitter):
    """"
    [msvcrxx.dll] intptr_t _spawnle([spawn_mode] mode, const char* cmdname, const char* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnle(jitter):
    """"
    [msvcrxx.dll] intptr_t _wspawnle([spawn_mode] mode, const wchar_t* cmdname, const wchar_t* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnlp(jitter):
    """"
    [msvcrxx.dll] intptr_t _spawnlp([spawn_mode] mode, const char* cmdname, const char* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnlp(jitter):
    """"
    [msvcrxx.dll] intptr_t _wspawnlp([spawn_mode] mode, const wchar_t* cmdname, const wchar_t* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnlpe(jitter):
    """"
    [msvcrxx.dll] intptr_t _spawnlpe([spawn_mode] mode, const char* cmdname, const char* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnlpe(jitter):
    """"
    [msvcrxx.dll] intptr_t _wspawnlpe([spawn_mode] mode, const wchar_t* cmdname, const wchar_t* args)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "args"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnv(jitter):
    """"
    [msvcrxx.dll] intptr_t _spawnv([spawn_mode] mode, const char* cmdname, const char** argv)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnv(jitter):
    """"
    [msvcrxx.dll] intptr_t _wspawnv([spawn_mode] mode, const wchar_t* cmdname, const wchar_t** argv)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnve(jitter):
    """"
    [msvcrxx.dll] intptr_t _spawnve([spawn_mode] mode, const char* cmdname, const char** argv, const char** envp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnve(jitter):
    """"
    [msvcrxx.dll] intptr_t _wspawnve([spawn_mode] mode, const wchar_t* cmdname, const wchar_t** argv, const wchar_t** envp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnvp(jitter):
    """"
    [msvcrxx.dll] intptr_t _spawnvp([spawn_mode] mode, const char* cmdname, const char** argv)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnvp(jitter):
    """"
    [msvcrxx.dll] intptr_t _wspawnvp([spawn_mode] mode, const wchar_t* cmdname, const wchar_t** argv)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__spawnvpe(jitter):
    """"
    [msvcrxx.dll] intptr_t _spawnvpe([spawn_mode] mode, const char* cmdname, const char** argv, const char** envp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wspawnvpe(jitter):
    """"
    [msvcrxx.dll] intptr_t _wspawnvpe([spawn_mode] mode, const wchar_t* cmdname, const wchar_t** argv, const wchar_t** envp)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mode", "cmdname", "argv", "envp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_system(jitter):
    """"
    [msvcrxx.dll] int system(const char* command)
    """"
    ret_ad, args = jitter.func_args_cdecl(["command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wsystem(jitter):
    """"
    [msvcrxx.dll] int _wsystem(const wchar_t* command)
    """"
    ret_ad, args = jitter.func_args_cdecl(["command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__dupenv_s(jitter):
    """"
    [msvcrxx.dll] errno_t _dupenv_s(char** buffer, size_t* numberOfElements, const char* varname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wdupenv_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wdupenv_s(wchar_t** buffer, size_t* numberOfElements, const wchar_t* varname)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "varname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__dupenv_s_dbg(jitter):
    """"
    [msvcrxx.dll] errno_t _dupenv_s_dbg(char** buffer, size_t* numberOfElements, const char* varname, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "varname", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wdupenv_s_dbg(jitter):
    """"
    [msvcrxx.dll] errno_t _wdupenv_s_dbg(wchar_t** buffer, size_t* numberOfElements, const wchar_t* varname, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "varname", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___getmainargs(jitter):
    """"
    [msvcrxx.dll] int __getmainargs(int* _Argc, char*** _Argv, char*** _Env, int _DoWildCard, _startupinfo* _StartInfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_Argc", "_Argv", "_Env", "_DoWildCard", "_StartInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___wgetmainargs(jitter):
    """"
    [msvcrxx.dll] int __wgetmainargs(int* _Argc, wchar_t*** _Argv, wchar_t*** _Env, int _DoWildCard, _startupinfo* _StartInfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_Argc", "_Argv", "_Env", "_DoWildCard", "_StartInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_pgmptr(jitter):
    """"
    [msvcrxx.dll] errno_t _get_pgmptr(char** pValue)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_wpgmptr(jitter):
    """"
    [msvcrxx.dll] errno_t _get_wpgmptr(wchar_t** pValue)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_fileinfo(jitter):
    """"
    [msvcrxx.dll] errno_t _get_fileinfo(int* pFileInfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pFileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_fileinfo(jitter):
    """"
    [msvcrxx.dll] errno_t _set_fileinfo(int value)
    """"
    ret_ad, args = jitter.func_args_cdecl(["value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___set_app_type(jitter):
    """"
    [msvcrxx.dll] void __set_app_type([C_APP_TYPE] at)
    """"
    ret_ad, args = jitter.func_args_cdecl(["at"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___dllonexit(jitter):
    """"
    [msvcrxx.dll] _onexit_t __dllonexit(_onexit_t func, _PVFV** pbegin, _PVFV** pend)
    """"
    ret_ad, args = jitter.func_args_cdecl(["func", "pbegin", "pend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sleep(jitter):
    """"
    [msvcrxx.dll] void _sleep(unsigned long duration)
    """"
    ret_ad, args = jitter.func_args_cdecl(["duration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__loaddll(jitter):
    """"
    [msvcrxx.dll] intptr_t _loaddll(char* filename)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__unloaddll(jitter):
    """"
    [msvcrxx.dll] int _unloaddll(intptr_t handle)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getdllprocaddr(jitter):
    """"
    [msvcrxx.dll] void* _getdllprocaddr(intptr_t handle, char* procedureName, intptr_t ordinal)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "procedureName", "ordinal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_bsearch(jitter):
    """"
    [msvcrxx.dll] void* bsearch(const void* key, const void* base, size_t num, size_t width, [compare_function] compare)
    """"
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "width", "compare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_bsearch_s(jitter):
    """"
    [msvcrxx.dll] void* bsearch_s(const void* key, const void* base, size_t num, size_t width, [compare_s_function] compare, void* context)
    """"
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "width", "compare", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lfind(jitter):
    """"
    [msvcrxx.dll] void* _lfind(const void* key, const void* base, unsigned int* num, unsigned int width, [compare_function] compare)
    """"
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "width", "compare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lfind_s(jitter):
    """"
    [msvcrxx.dll] void* _lfind_s(const void* key, const void* base, unsigned int* num, size_t size, [compare_s_function] compare, void* context)
    """"
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "size", "compare", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lsearch(jitter):
    """"
    [msvcrxx.dll] void* _lsearch(const void* key, void* base, unsigned int* num, unsigned int width, [compare_function] compare)
    """"
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "width", "compare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lsearch_s(jitter):
    """"
    [msvcrxx.dll] void* _lsearch_s(const void* key, void* base, unsigned int* num, size_t size, [compare_s_function] compare, void* context)
    """"
    ret_ad, args = jitter.func_args_cdecl(["key", "base", "num", "size", "compare", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_qsort(jitter):
    """"
    [msvcrxx.dll] void qsort(void* base, size_t num, size_t width, [compare_s_function] compare)
    """"
    ret_ad, args = jitter.func_args_cdecl(["base", "num", "width", "compare"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_qsort_s(jitter):
    """"
    [msvcrxx.dll] void qsort_s(void* base, size_t num, size_t width, [compare_s_function] compare, void* context)
    """"
    ret_ad, args = jitter.func_args_cdecl(["base", "num", "width", "compare", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsdec(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsdec(const unsigned char* start, const unsigned char* current)
    """"
    ret_ad, args = jitter.func_args_cdecl(["start", "current"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsdec_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsdec_l(const unsigned char* start, const unsigned char* current, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["start", "current", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsinc(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsinc(const unsigned char* current)
    """"
    ret_ad, args = jitter.func_args_cdecl(["current"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsinc_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsinc_l(const unsigned char* current, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["current", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcat(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsnbcat(unsigned char* dest, const unsigned char* src, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcat_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsnbcat_l(unsigned char* dest, const unsigned char* src, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "src", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcat_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsnbcat_s(unsigned char* dest, size_t sizeInBytes, const unsigned char* src, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "sizeInBytes", "src", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcat_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsnbcat_s_l(unsigned char* dest, size_t sizeInBytes, const unsigned char* src, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["dest", "sizeInBytes", "src", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnbcmp(const unsigned char* string1, const unsigned char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcmp_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnbcmp_l(const unsigned char* string1, const unsigned char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcnt(jitter):
    """"
    [msvcrxx.dll] size_t _mbsnbcnt(const unsigned char* str, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcnt_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbsnbcnt_l(const unsigned char* str, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnccnt(jitter):
    """"
    [msvcrxx.dll] size_t _mbsnccnt(const unsigned char* str, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnccnt_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbsnccnt_l(const unsigned char* str, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___strncnt(jitter):
    """"
    [msvcrxx.dll] size_t __strncnt(const char* str, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___wcsncnt(jitter):
    """"
    [msvcrxx.dll] size_t __wcsncnt(const wchar_t* str, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcpy(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsnbcpy(unsigned char* strDest, const unsigned char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcpy_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsnbcpy_l(unsigned char* strDest, const unsigned char* strSource, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsnbcpy_s(unsigned char* strDest, size_t sizeInBytes, const unsigned char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "sizeInBytes", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcpy_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsnbcpy_s_l(unsigned char* strDest, size_t sizeInBytes, const unsigned char* strSource, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "sizeInBytes", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbicmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnbicmp(const unsigned char* string1, const unsigned char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbset(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsnbset(unsigned char* str, unsigned int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbset_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsnbset_l(unsigned char* str, unsigned int c, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnextc(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbsnextc(const unsigned char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnextc_l(jitter):
    """"
    [msvcrxx.dll] unsigned int _mbsnextc_l(const unsigned char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsninc(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsninc(const unsigned char* str, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsninc_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsninc_l(const unsigned char* str, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsspnp(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsspnp(const unsigned char* str, const unsigned char* charset)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "charset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsspnp_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsspnp_l(const unsigned char* str, const unsigned char* charset, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "charset", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scprintf(jitter):
    """"
    [msvcrxx.dll] int _scprintf(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scprintf_l(jitter):
    """"
    [msvcrxx.dll] int _scprintf_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scwprintf(jitter):
    """"
    [msvcrxx.dll] int _scwprintf(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _scwprintf_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _snscanf(const char* input, size_t length, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _snscanf_l(const char* input, size_t length, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _snwscanf(const wchar_t* input, size_t length, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _snwscanf_l(const wchar_t* input, size_t length, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] sscanf(const char* buffer, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _sscanf_l(const char* buffer, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_swscanf(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] swscanf(const wchar_t* buffer, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swscanf_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _swscanf_l(const wchar_t* buffer, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sprintf(jitter):
    """"
    [msvcrxx.dll] int sprintf(char* buffer, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sprintf_l(jitter):
    """"
    [msvcrxx.dll] int _sprintf_l(char* buffer, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_swprintf(jitter):
    """"
    [msvcrxx.dll] int swprintf(wchar_t* buffer, size_t count, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swprintf(jitter):
    """"
    [msvcrxx.dll] int _swprintf(wchar_t* buffer, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___swprintf_l(jitter):
    """"
    [msvcrxx.dll] int __swprintf_l(wchar_t* buffer, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sprintf_p(jitter):
    """"
    [msvcrxx.dll] int _sprintf_p(char* buffer, size_t sizeOfBuffer, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _sprintf_p_l(char* buffer, size_t sizeOfBuffer, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swprintf_p(jitter):
    """"
    [msvcrxx.dll] int _swprintf_p(wchar_t* buffer, size_t sizeOfBuffer, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _swprintf_p_l(wchar_t* buffer, size_t sizeOfBuffer, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcat(jitter):
    """"
    [msvcrxx.dll] char* strcat(char* strDestination, const char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscat(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcscat(wchar_t* strDestination, const wchar_t* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscat(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbscat(unsigned char* strDestination, const unsigned char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcat_s(jitter):
    """"
    [msvcrxx.dll] errno_t strcat_s(char* strDestination, size_t numberOfElements, const char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscat_s(jitter):
    """"
    [msvcrxx.dll] errno_t wcscat_s(wchar_t* strDestination, size_t numberOfElements, const wchar_t* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscat_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbscat_s(unsigned char* strDestination, size_t numberOfElements, const unsigned char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strchr(jitter):
    """"
    [msvcrxx.dll] char* strchr(const char* str, int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcschr(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcschr(const wchar_t* str, wchar_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbschr(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbschr(const unsigned char* str, unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbschr_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbschr_l(const unsigned char* str, unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcmp(jitter):
    """"
    [msvcrxx.dll] int strcmp(const char* string1, const char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscmp(jitter):
    """"
    [msvcrxx.dll] int wcscmp(const wchar_t* string1, const wchar_t* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbscmp(const unsigned char* string1, const unsigned char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcpy(jitter):
    """"
    [msvcrxx.dll] char* strcpy(char* strDestination, const char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscpy(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcscpy(wchar_t* strDestination, const wchar_t* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscpy(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbscpy(unsigned char* strDestination, const unsigned char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t strcpy_s(char* strDestination, size_t numberOfElements, const char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t wcscpy_s(wchar_t* strDestination, size_t numberOfElements, const wchar_t* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbscpy_s(unsigned char* strDestination, size_t numberOfElements, const unsigned char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDestination", "numberOfElements", "strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcspn(jitter):
    """"
    [msvcrxx.dll] size_t strcspn(const char* str, const char* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscspn(jitter):
    """"
    [msvcrxx.dll] size_t wcscspn(const wchar_t* str, const wchar_t* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscspn(jitter):
    """"
    [msvcrxx.dll] size_t _mbscspn(const unsigned char* str, const unsigned char* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscspn_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbscspn_l(const unsigned char* str, const unsigned char* strCharSet, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strdup(jitter):
    """"
    [msvcrxx.dll] char* _strdup(const char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsdup(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcsdup(const wchar_t* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsdup(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsdup(const unsigned char* strSource)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strerror(jitter):
    """"
    [msvcrxx.dll] char* strerror(int errnum)
    """"
    ret_ad, args = jitter.func_args_cdecl(["errnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strerror(jitter):
    """"
    [msvcrxx.dll] char* _strerror(const char* strErrMsg)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strErrMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcserror(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcserror(int errnum)
    """"
    ret_ad, args = jitter.func_args_cdecl(["errnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___wcserror(jitter):
    """"
    [msvcrxx.dll] wchar_t* __wcserror(const wchar_t* strErrMsg)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strErrMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strerror_s(jitter):
    """"
    [msvcrxx.dll] errno_t strerror_s(char* buffer, size_t numberOfElements, int errnum)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "errnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strerror_s(jitter):
    """"
    [msvcrxx.dll] errno_t _strerror_s(char* buffer, size_t numberOfElements, const char* strErrMsg)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "strErrMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcserror_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wcserror_s(wchar_t* buffer, size_t numberOfElements, int errnum)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "errnum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___wcserror_s(jitter):
    """"
    [msvcrxx.dll] errno_t __wcserror_s(wchar_t* buffer, size_t numberOfElements, const wchar_t* strErrMsg)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "strErrMsg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strnlen(jitter):
    """"
    [msvcrxx.dll] size_t strnlen(const char* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsnlen(jitter):
    """"
    [msvcrxx.dll] size_t wcsnlen(const wchar_t* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnlen(jitter):
    """"
    [msvcrxx.dll] size_t _mbsnlen(const unsigned char* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnlen_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbsnlen_l(const unsigned char* str, size_t numberOfElements, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstrnlen(jitter):
    """"
    [msvcrxx.dll] size_t _mbstrnlen(const char* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstrnlen_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbstrnlen_l(const char* str, size_t numberOfElements, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strlwr(jitter):
    """"
    [msvcrxx.dll] char* _strlwr(char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcslwr(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcslwr(wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslwr(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbslwr(unsigned char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strlwr_l(jitter):
    """"
    [msvcrxx.dll] char* _strlwr_l(char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcslwr_l(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcslwr_l(wchar_t* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslwr_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbslwr_l(unsigned char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncat(jitter):
    """"
    [msvcrxx.dll] char* strncat(char* strDest, const char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncat(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcsncat(wchar_t* strDest, const wchar_t* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncat(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsncat(unsigned char* strDest, const unsigned char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncat_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsncat_l(unsigned char* strDest, const unsigned char* strSource, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncat_s(jitter):
    """"
    [msvcrxx.dll] errno_t strncat_s(char* strDest, size_t numberOfElements, const char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncat_s(jitter):
    """"
    [msvcrxx.dll] errno_t wcsncat_s(wchar_t* strDest, size_t numberOfElements, const wchar_t* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncat_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsncat_s(unsigned char* strDest, size_t numberOfElements, const unsigned char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncat_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsncat_s_l(unsigned char* strDest, size_t numberOfElements, const unsigned char* strSource, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncmp(jitter):
    """"
    [msvcrxx.dll] int strncmp(const char* string1, const char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncmp(jitter):
    """"
    [msvcrxx.dll] int wcsncmp(const wchar_t* string1, const wchar_t* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsncmp(const unsigned char* string1, const unsigned char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncmp_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsncmp_l(const unsigned char* string1, const unsigned char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncpy(jitter):
    """"
    [msvcrxx.dll] char* strncpy(char* strDest, const char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncpy(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcsncpy(wchar_t* strDest, const wchar_t* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncpy(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsncpy(unsigned char* strDest, const unsigned char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncpy_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsncpy_l(unsigned char* strDest, const unsigned char* strSource, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strncpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t strncpy_s(char* strDest, size_t numberOfElements, const char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsncpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t wcsncpy_s(wchar_t* strDest, size_t numberOfElements, const wchar_t* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncpy_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsncpy_s(unsigned char* strDest, size_t numberOfElements, const unsigned char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncpy_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsncpy_s_l(unsigned char* strDest, size_t numberOfElements, const unsigned char* strSource, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "numberOfElements", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnset(jitter):
    """"
    [msvcrxx.dll] char* _strnset(char* str, int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnset(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcsnset(wchar_t* str, wchar_t c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnset(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsnset(unsigned char* str, unsigned int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnset_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsnset_l(unsigned char* str, unsigned int c, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strpbrk(jitter):
    """"
    [msvcrxx.dll] char* strpbrk(const char* str, const char* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcspbrk(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcspbrk(const wchar_t* str, const wchar_t* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbspbrk(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbspbrk(const unsigned char* str, const unsigned char* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbspbrk_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbspbrk_l(const unsigned char* str, const unsigned char* strCharSet, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strrchr(jitter):
    """"
    [msvcrxx.dll] char* strrchr(const char* str, int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsrchr(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcsrchr(const wchar_t* str, wchar_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsrchr(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsrchr(const unsigned char* str, unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsrchr_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsrchr_l(const unsigned char* str, unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strrev(jitter):
    """"
    [msvcrxx.dll] char* _strrev(char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsrev(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcsrev(wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsrev(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsrev(unsigned char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsrev_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsrev_l(unsigned char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strset(jitter):
    """"
    [msvcrxx.dll] char* _strset(char* str, int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsset(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcsset(wchar_t* str, wchar_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsset(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsset(unsigned char* str, unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsset_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsset_l(unsigned char* str, unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strspn(jitter):
    """"
    [msvcrxx.dll] size_t strspn(const char* str, const char* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsspn(jitter):
    """"
    [msvcrxx.dll] size_t wcsspn(const wchar_t* str, const wchar_t* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsspn(jitter):
    """"
    [msvcrxx.dll] size_t _mbsspn(const unsigned char* str, const unsigned char* strCharSet)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsspn_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbsspn_l(const unsigned char* str, const unsigned char* strCharSet, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strCharSet", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strstr(jitter):
    """"
    [msvcrxx.dll] char* strstr(const char* str, const char* strSearch)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strSearch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsstr(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcsstr(const wchar_t* str, const wchar_t* strSearch)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strSearch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsstr(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsstr(const unsigned char* str, const unsigned char* strSearch)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strSearch"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsstr_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsstr_l(const unsigned char* str, const unsigned char* strSearch, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "strSearch", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtok(jitter):
    """"
    [msvcrxx.dll] char* strtok(char* strToken, const char* strDelimit)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstok(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcstok(wchar_t* strToken, const wchar_t* strDelimit)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstok(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbstok(unsigned char* strToken, const unsigned char* strDelimit)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstok_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbstok_l(unsigned char* strToken, const unsigned char* strDelimit, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strtok_s(jitter):
    """"
    [msvcrxx.dll] char* strtok_s(char* strToken, const char* strDelimit, char** context)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcstok_s(jitter):
    """"
    [msvcrxx.dll] wchar_t* wcstok_s(wchar_t* strToken, const wchar_t* strDelimit, wchar_t** context)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstok_s(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbstok_s(unsigned char* strToken, const unsigned char* strDelimit, char** context)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "context"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstok_s_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbstok_s_l(unsigned char* strToken, const unsigned char* strDelimit, char** context, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strToken", "strDelimit", "context", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strupr(jitter):
    """"
    [msvcrxx.dll] char* _strupr(char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsupr(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcsupr(wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsupr(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsupr(unsigned char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strupr_l(jitter):
    """"
    [msvcrxx.dll] char* _strupr_l(char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsupr_l(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcsupr_l(wchar_t* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsupr_l(jitter):
    """"
    [msvcrxx.dll] unsigned char* _mbsupr_l(unsigned char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vsprintf(jitter):
    """"
    [msvcrxx.dll] int vsprintf(char* buffer, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vsprintf_l(char* buffer, const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vswprintf(jitter):
    """"
    [msvcrxx.dll] int vswprintf(wchar_t* buffer, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf(jitter):
    """"
    [msvcrxx.dll] int _vswprintf(wchar_t* buffer, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vswprintf_l(wchar_t* buffer, size_t count, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___vswprintf_l(jitter):
    """"
    [msvcrxx.dll] int __vswprintf_l(wchar_t* buffer, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vsprintf_p(char* buffer, size_t sizeInBytes, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInBytes", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vsprintf_p_l(char* buffer, size_t sizeInBytes, const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeInBytes", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf_p(jitter):
    """"
    [msvcrxx.dll] int _vswprintf_p(wchar_t* buffer, size_t count, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _vswprintf_p_l(wchar_t* buffer, size_t count, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vsnprintf(jitter):
    """"
    [msvcrxx.dll] int vsnprintf(char* buffer, size_t count, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnprintf(jitter):
    """"
    [msvcrxx.dll] int _vsnprintf(char* buffer, size_t count, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vsnprintf_l(char* buffer, size_t count, const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnwprintf(jitter):
    """"
    [msvcrxx.dll] int _vsnwprintf(wchar_t* buffer, size_t count, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _vsnwprintf_l(wchar_t* buffer, size_t count, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strlen(jitter):
    """"
    [msvcrxx.dll] size_t strlen(const char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslen(jitter):
    """"
    [msvcrxx.dll] size_t _mbslen(const unsigned char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslen_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbslen_l(const unsigned char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstrlen(jitter):
    """"
    [msvcrxx.dll] size_t _mbstrlen(const char* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbstrlen_l(jitter):
    """"
    [msvcrxx.dll] size_t _mbstrlen_l(const char* str, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcslen(jitter):
    """"
    [msvcrxx.dll] size_t wcslen(const wchar_t* str)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbclen(jitter):
    """"
    [msvcrxx.dll] size_t _mbclen(const unsigned char* c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mblen(jitter):
    """"
    [msvcrxx.dll] int mblen(const char* mbstr, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mblen_l(jitter):
    """"
    [msvcrxx.dll] int _mblen_l(const char* mbstr, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["mbstr", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strcoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] strcoll(const char* string1, const char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcscoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] wcscoll(const wchar_t* string1, const wchar_t* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbscoll(const unsigned char* string1, const unsigned char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strcoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _strcoll_l(const char* string1, const char* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcscoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcscoll_l(const wchar_t* string1, const wchar_t* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbscoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbscoll_l(const unsigned char* string1, const unsigned char* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stricoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _stricoll(const char* string1, const char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsicoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsicoll(const wchar_t* string1, const wchar_t* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsicoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsicoll(const unsigned char* string1, const unsigned char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stricoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _stricoll_l(const char* string1, const char* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsicoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsicoll_l(const wchar_t* string1, const wchar_t* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsicoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsicoll_l(const unsigned char* string1, const unsigned char* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strncoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _strncoll(const char* string1, const char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsncoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsncoll(const wchar_t* string1, const wchar_t* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsncoll(const unsigned char* string1, const unsigned char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strncoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _strncoll_l(const char* string1, const char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsncoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsncoll_l(const wchar_t* string1, const wchar_t* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsncoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsncoll_l(const unsigned char* string1, const unsigned char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnicoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _strnicoll(const char* string1, const char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnicoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsnicoll(const wchar_t* string1, const wchar_t* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnicoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnicoll(const unsigned char* string1, const unsigned char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnicoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _strnicoll_l(const char* string1, const char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnicoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsnicoll_l(const wchar_t* string1, const wchar_t* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnicoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnicoll_l(const unsigned char* string1, const unsigned char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strcmpi(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _strcmpi(const char* string1, const char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stricmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _stricmp(const char* string1, const char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsicmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsicmp(const wchar_t* string1, const wchar_t* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsicmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsicmp(const unsigned char* string1, const unsigned char* string2)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__stricmp_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _stricmp_l(const char* string1, const char* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsicmp_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsicmp_l(const wchar_t* string1, const wchar_t* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsicmp_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsicmp_l(const unsigned char* string1, const unsigned char* string2, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnicmp_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsnicmp_l(const wchar_t* string1, const wchar_t* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnicmp_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnicmp_l(const unsigned char* string1, const unsigned char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnicmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnicmp(const unsigned char* string1, const unsigned char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnicmp_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _strnicmp_l(const char* string1, const char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnicmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _wcsnicmp(const wchar_t* string1, const wchar_t* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnicmp(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _strnicmp(const char* string1, const char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strupr_s(jitter):
    """"
    [msvcrxx.dll] errno_t _strupr_s(char* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsupr_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wcsupr_s(wchar_t* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strupr_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _strupr_s_l(char* str, size_t numberOfElements, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsupr_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _wcsupr_s_l(wchar_t* str, size_t numberOfElements, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsupr_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsupr_s(unsigned char* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsupr_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsupr_s_l(unsigned char* str, size_t numberOfElements, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strlwr_s(jitter):
    """"
    [msvcrxx.dll] errno_t _strlwr_s(char* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strlwr_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _strlwr_s_l(char* str, size_t numberOfElements, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslwr_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbslwr_s(unsigned char* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbslwr_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbslwr_s_l(unsigned char* str, size_t numberOfElements, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcslwr_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wcslwr_s(wchar_t* str, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcslwr_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _wcslwr_s_l(wchar_t* str, size_t numberOfElements, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _snscanf_s(const char* input, size_t length, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _snscanf_s_l(const char* input, size_t length, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _snwscanf_s(const wchar_t* input, size_t length, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _snwscanf_s_l(const wchar_t* input, size_t length, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["input", "length", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnprintf_s(jitter):
    """"
    [msvcrxx.dll] int _vsnprintf_s(char* buffer, size_t sizeOfBuffer, size_t count, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vsnprintf_s_l(char* buffer, size_t sizeOfBuffer, size_t count, const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnwprintf_s(jitter):
    """"
    [msvcrxx.dll] int _vsnwprintf_s(wchar_t* buffer, size_t sizeOfBuffer, size_t count, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsnwprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vsnwprintf_s_l(wchar_t* buffer, size_t sizeOfBuffer, size_t count, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_swprintf_s(jitter):
    """"
    [msvcrxx.dll] int swprintf_s(wchar_t* buffer, size_t sizeOfBuffer, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _swprintf_s_l(wchar_t* buffer, size_t sizeOfBuffer, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _sprintf_s_l(char* buffer, size_t sizeOfBuffer, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sprintf_s(jitter):
    """"
    [msvcrxx.dll] int sprintf_s(char* buffer, size_t sizeOfBuffer, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__swscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _swscanf_s_l(const wchar_t* buffer, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_swscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] swscanf_s(const wchar_t* buffer, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__sscanf_s_l(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] _sscanf_s_l(const char* buffer, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_sscanf_s(jitter):
    """"
    [msvcrxx.dll] [RET_EOF] sscanf_s(const char* buffer, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vswprintf_s(jitter):
    """"
    [msvcrxx.dll] int vswprintf_s(wchar_t* buffer, size_t numberOfElements, const wchar_t* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vswprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vswprintf_s_l(wchar_t* buffer, size_t numberOfElements, const wchar_t* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__vsprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _vsprintf_s_l(char* buffer, size_t numberOfElements, const char* format, _locale_t locale, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "format", "locale", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_vsprintf_s(jitter):
    """"
    [msvcrxx.dll] int vsprintf_s(char* buffer, size_t numberOfElements, const char* format, va_list argptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "format", "argptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strdup_dbg(jitter):
    """"
    [msvcrxx.dll] char* _strdup_dbg(const char* strSource, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strSource", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsdup_dbg(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wcsdup_dbg(const wchar_t* strSource, [DBG_BLOCK_TYPE] blockType, const char* filename, int linenumber)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strSource", "blockType", "filename", "linenumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strxfrm(jitter):
    """"
    [msvcrxx.dll] [size_t_INT_MAX] strxfrm(char* strDest, const char* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsxfrm(jitter):
    """"
    [msvcrxx.dll] [size_t_INT_MAX] wcsxfrm(wchar_t* strDest, const wchar_t* strSource, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strxfrm_l(jitter):
    """"
    [msvcrxx.dll] [size_t_INT_MAX] _strxfrm_l(char* strDest, const char* strSource, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsxfrm_l(jitter):
    """"
    [msvcrxx.dll] [size_t_INT_MAX] _wcsxfrm_l(wchar_t* strDest, const wchar_t* strSource, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "strSource", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mbrlen(jitter):
    """"
    [msvcrxx.dll] size_t mbrlen(const char* str, size_t maxSize, mbstate_t mbstate)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "maxSize", "mbstate"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnbcoll(const unsigned char* string1, const unsigned char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbcoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnbcoll_l(const unsigned char* string1, const unsigned char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbicoll(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnbicoll(const unsigned char* string1, const unsigned char* string2, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbicoll_l(jitter):
    """"
    [msvcrxx.dll] [_NLSCMPERROR] _mbsnbicoll_l(const unsigned char* string1, const unsigned char* string2, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["string1", "string2", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbset_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsnbset_s(unsigned char* str, size_t size, unsigned int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "size", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnbset_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsnbset_s_l(unsigned char* str, size_t size, unsigned int c, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "size", "c", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scprintf_p(jitter):
    """"
    [msvcrxx.dll] int _scprintf_p(const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _scprintf_p_l(const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scwprintf_p(jitter):
    """"
    [msvcrxx.dll] int _scwprintf_p(const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__scwprintf_p_l(jitter):
    """"
    [msvcrxx.dll] int _scwprintf_p_l(const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snprintf_s(jitter):
    """"
    [msvcrxx.dll] int _snprintf_s(char* buffer, size_t sizeOfBuffer, size_t count, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _snprintf_s_l(char* buffer, size_t sizeOfBuffer, size_t count, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwprintf_s(jitter):
    """"
    [msvcrxx.dll] int _snwprintf_s(wchar_t* buffer, size_t sizeOfBuffer, size_t count, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwprintf_s_l(jitter):
    """"
    [msvcrxx.dll] int _snwprintf_s_l(wchar_t* buffer, size_t sizeOfBuffer, size_t count, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "sizeOfBuffer", "count", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snprintf(jitter):
    """"
    [msvcrxx.dll] int _snprintf(char* buffer, size_t count, const char* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snprintf_l(jitter):
    """"
    [msvcrxx.dll] int _snprintf_l(char* buffer, size_t count, const char* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwprintf(jitter):
    """"
    [msvcrxx.dll] int _snwprintf(wchar_t* buffer, size_t count, const wchar_t* format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__snwprintf_l(jitter):
    """"
    [msvcrxx.dll] int _snwprintf_l(wchar_t* buffer, size_t count, const wchar_t* format, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "count", "format", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strnset_s(jitter):
    """"
    [msvcrxx.dll] errno_t _strnset_s(char* str, size_t numberOfElements, int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsnset_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wcsnset_s(wchar_t* str, size_t numberOfElements, wchar_t c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnset_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsnset_s(unsigned char* str, size_t numberOfElements, unsigned int c, size_t count)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "count"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsnset_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsnset_s_l(unsigned char* str, size_t numberOfElements, unsigned int c, size_t count, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "count", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strset_s(jitter):
    """"
    [msvcrxx.dll] errno_t _strset_s(char* str, size_t numberOfElements, int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsset_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wcsset_s(wchar_t* str, size_t numberOfElements, wchar_t c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsset_s(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsset_s(unsigned char* str, size_t numberOfElements, unsigned int c)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mbsset_s_l(jitter):
    """"
    [msvcrxx.dll] errno_t _mbsset_s_l(unsigned char* str, size_t numberOfElements, unsigned int c, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["str", "numberOfElements", "c", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findclose(jitter):
    """"
    [msvcrxx.dll] int _findclose(intptr_t handle)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst(jitter):
    """"
    [msvcrxx.dll] intptr_t _findfirst(const char* filespec, struct _finddata_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst32(jitter):
    """"
    [msvcrxx.dll] intptr_t _findfirst32(const char* filespec, struct _finddata32_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst64(jitter):
    """"
    [msvcrxx.dll] intptr_t _findfirst64(const char* filespec, struct __finddata64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirsti64(jitter):
    """"
    [msvcrxx.dll] intptr_t _findfirsti64(const char* filespec, struct _finddatai64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst32i64(jitter):
    """"
    [msvcrxx.dll] intptr_t _findfirst32i64(const char* filespec, struct _finddata32i64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findfirst64i32(jitter):
    """"
    [msvcrxx.dll] intptr_t _findfirst64i32(const char* filespec, struct _finddata64i32_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst(jitter):
    """"
    [msvcrxx.dll] intptr_t _wfindfirst(const wchar_t* filespec, struct _wfinddata_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst32(jitter):
    """"
    [msvcrxx.dll] intptr_t _wfindfirst32(const wchar_t* filespec, struct _wfinddata32_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst64(jitter):
    """"
    [msvcrxx.dll] intptr_t _wfindfirst64(const wchar_t* filespec, struct _wfinddata64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirsti64(jitter):
    """"
    [msvcrxx.dll] intptr_t _wfindfirsti64(const wchar_t* filespec, struct _wfinddatai64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst32i64(jitter):
    """"
    [msvcrxx.dll] intptr_t _wfindfirst32i64(const wchar_t* filespec, struct _wfinddata32i64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindfirst64i32(jitter):
    """"
    [msvcrxx.dll] intptr_t _wfindfirst64i32(const wchar_t* filespec, struct _wfinddata64i32_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filespec", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext(jitter):
    """"
    [msvcrxx.dll] int _findnext(intptr_t handle, struct _finddata_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext32(jitter):
    """"
    [msvcrxx.dll] int _findnext32(intptr_t handle, struct _finddata32_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext64(jitter):
    """"
    [msvcrxx.dll] int _findnext64(intptr_t handle, struct __finddata64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnexti64(jitter):
    """"
    [msvcrxx.dll] int _findnexti64(intptr_t handle, struct _finddatai64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext32i64(jitter):
    """"
    [msvcrxx.dll] int _findnext32i64(intptr_t handle, struct _finddata32i64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__findnext64i32(jitter):
    """"
    [msvcrxx.dll] int _findnext64i32(intptr_t handle, struct _finddata64i32_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext(jitter):
    """"
    [msvcrxx.dll] int _wfindnext(intptr_t handle, struct _wfinddata_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext32(jitter):
    """"
    [msvcrxx.dll] int _wfindnext32(intptr_t handle, struct _wfinddata32_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext64(jitter):
    """"
    [msvcrxx.dll] int _wfindnext64(intptr_t handle, struct _wfinddata64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnexti64(jitter):
    """"
    [msvcrxx.dll] int _wfindnexti64(intptr_t handle, struct _wfinddatai64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext32i64(jitter):
    """"
    [msvcrxx.dll] int _wfindnext32i64(intptr_t handle, struct _wfinddatai64_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wfindnext64i32(jitter):
    """"
    [msvcrxx.dll] int _wfindnext64i32(intptr_t handle, struct _wfinddata64i32_t* fileinfo)
    """"
    ret_ad, args = jitter.func_args_cdecl(["handle", "fileinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_asctime(jitter):
    """"
    [msvcrxx.dll] char* asctime(const struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wasctime(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wasctime(const struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_asctime_s(jitter):
    """"
    [msvcrxx.dll] errno_t asctime_s(char* buffer, size_t numberOfElements, const struct tm* _tm)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "_tm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wasctime_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wasctime_s(wchar_t* buffer, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_clock(jitter):
    """"
    [msvcrxx.dll] clock_t clock()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_ctime(jitter):
    """"
    [msvcrxx.dll] char* ctime(const time_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ctime32(jitter):
    """"
    [msvcrxx.dll] char* _ctime32(const __time32_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ctime64(jitter):
    """"
    [msvcrxx.dll] char* _ctime64(const __time64_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wctime(const time_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime32(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wctime32(const __time32_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime64(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wctime64(const __time64_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ctime32_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ctime32_s(char* buffer, size_t numberOfElements, const __time32_t* time)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ctime64_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ctime64_s(char* buffer, size_t numberOfElements, const __time64_t* time)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime32_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wctime32_s(wchar_t* buffer, size_t numberOfElements, const __time32_t* time)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wctime64_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wctime64_s(wchar_t* buffer, size_t numberOfElements, const __time64_t* time)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime(jitter):
    """"
    [msvcrxx.dll] void _ftime(struct _timeb* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime32(jitter):
    """"
    [msvcrxx.dll] void _ftime32(struct __timeb32* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime64(jitter):
    """"
    [msvcrxx.dll] void _ftime64(struct __timeb64* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime32_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ftime32_s(struct __timeb32* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__ftime64_s(jitter):
    """"
    [msvcrxx.dll] errno_t _ftime64_s(struct __timeb64* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__futime(jitter):
    """"
    [msvcrxx.dll] int _futime(int fd, struct _utimbuf* filetime)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "filetime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__futime32(jitter):
    """"
    [msvcrxx.dll] int _futime32(int fd, struct __utimbuf32* filetime)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "filetime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__futime64(jitter):
    """"
    [msvcrxx.dll] int _futime64(int fd, struct __utimbuf64* filetime)
    """"
    ret_ad, args = jitter.func_args_cdecl(["fd", "filetime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_gmtime(jitter):
    """"
    [msvcrxx.dll] struct tm* gmtime(const time_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gmtime32(jitter):
    """"
    [msvcrxx.dll] struct tm* _gmtime32(const __time32_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gmtime64(jitter):
    """"
    [msvcrxx.dll] struct tm* _gmtime64(const __time64_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gmtime32_s(jitter):
    """"
    [msvcrxx.dll] errno_t _gmtime32_s(struct tm* _tm, const __time32_t* time)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_tm", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__gmtime64_s(jitter):
    """"
    [msvcrxx.dll] errno_t _gmtime64_s(struct tm* _tm, const __time64_t* time)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_tm", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_localtime(jitter):
    """"
    [msvcrxx.dll] struct tm* localtime(const time_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__localtime32(jitter):
    """"
    [msvcrxx.dll] struct tm* _localtime32(const __time32_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__localtime64(jitter):
    """"
    [msvcrxx.dll] struct tm* _localtime64(const __time64_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__localtime32_s(jitter):
    """"
    [msvcrxx.dll] errno_t _localtime32_s(struct tm* _tm, const __time32_t* time)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_tm", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__localtime64_s(jitter):
    """"
    [msvcrxx.dll] errno_t _localtime64_s(struct tm* _tm, const __time64_t* time)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_tm", "time"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mkgmtime(jitter):
    """"
    [msvcrxx.dll] time_t _mkgmtime(struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mkgmtime32(jitter):
    """"
    [msvcrxx.dll] __time32_t _mkgmtime32(struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mkgmtime64(jitter):
    """"
    [msvcrxx.dll] __time64_t _mkgmtime64(struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_mktime(jitter):
    """"
    [msvcrxx.dll] time_t mktime(struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mktime32(jitter):
    """"
    [msvcrxx.dll] __time32_t _mktime32(struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__mktime64(jitter):
    """"
    [msvcrxx.dll] __time64_t _mktime64(struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strdate(jitter):
    """"
    [msvcrxx.dll] char* _strdate(char* datestr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["datestr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstrdate(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wstrdate(wchar_t* datestr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["datestr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strdate_s(jitter):
    """"
    [msvcrxx.dll] errno_t _strdate_s(char* buffer, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstrdate_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wstrdate_s(wchar_t* buffer, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtime(jitter):
    """"
    [msvcrxx.dll] char* _strtime(char* timestr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timestr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstrtime(jitter):
    """"
    [msvcrxx.dll] wchar_t* _wstrtime(wchar_t* timestr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timestr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strtime_s(jitter):
    """"
    [msvcrxx.dll] errno_t _strtime_s(char* buffer, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wstrtime_s(jitter):
    """"
    [msvcrxx.dll] errno_t _wstrtime_s(wchar_t* buffer, size_t numberOfElements)
    """"
    ret_ad, args = jitter.func_args_cdecl(["buffer", "numberOfElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_time(jitter):
    """"
    [msvcrxx.dll] time_t time(time_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__time32(jitter):
    """"
    [msvcrxx.dll] __time32_t _time32(__time32_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__time64(jitter):
    """"
    [msvcrxx.dll] __time64_t _time64(__time64_t* timer)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__tzset(jitter):
    """"
    [msvcrxx.dll] void _tzset()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__utime(jitter):
    """"
    [msvcrxx.dll] int _utime(const char* filename, struct _utimbuf* times)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__utime32(jitter):
    """"
    [msvcrxx.dll] int _utime32(const char* filename, struct __utimbuf32* times)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__utime64(jitter):
    """"
    [msvcrxx.dll] int _utime64(const char* filename, struct __utimbuf64* times)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wutime(jitter):
    """"
    [msvcrxx.dll] int _wutime(const wchar_t* filename, struct _utimbuf* times)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wutime32(jitter):
    """"
    [msvcrxx.dll] int _wutime32(const wchar_t* filename, struct __utimbuf32* times)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wutime64(jitter):
    """"
    [msvcrxx.dll] int _wutime64(const wchar_t* filename, struct __utimbuf64* times)
    """"
    ret_ad, args = jitter.func_args_cdecl(["filename", "times"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__difftime32(jitter):
    """"
    [msvcrxx.dll] double _difftime32(__time32_t timer1, __time32_t timer0)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer1", "timer0"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__difftime64(jitter):
    """"
    [msvcrxx.dll] double _difftime64(__time64_t timer1, __time64_t timer0)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer1", "timer0"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_difftime(jitter):
    """"
    [msvcrxx.dll] double difftime(time_t timer1, time_t timer0)
    """"
    ret_ad, args = jitter.func_args_cdecl(["timer1", "timer0"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_strftime(jitter):
    """"
    [msvcrxx.dll] size_t strftime(char* strDest, size_t maxsize, const char* format, const struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "maxsize", "format", "timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__strftime_l(jitter):
    """"
    [msvcrxx.dll] size_t _strftime_l(char* strDest, size_t maxsize, const char* format, const struct tm* timeptr, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "maxsize", "format", "timeptr", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx_wcsftime(jitter):
    """"
    [msvcrxx.dll] size_t wcsftime(wchar_t* strDest, size_t maxsize, const wchar_t* format, const struct tm* timeptr)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "maxsize", "format", "timeptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__wcsftime_l(jitter):
    """"
    [msvcrxx.dll] size_t _wcsftime_l(wchar_t* strDest, size_t maxsize, const wchar_t* format, const struct tm* timeptr, _locale_t locale)
    """"
    ret_ad, args = jitter.func_args_cdecl(["strDest", "maxsize", "format", "timeptr", "locale"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_dstbias(jitter):
    """"
    [msvcrxx.dll] errno_t _get_dstbias(int* seconds)
    """"
    ret_ad, args = jitter.func_args_cdecl(["seconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_daylight(jitter):
    """"
    [msvcrxx.dll] errno_t _get_daylight(int* hours)
    """"
    ret_ad, args = jitter.func_args_cdecl(["hours"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_timezone(jitter):
    """"
    [msvcrxx.dll] errno_t _get_timezone(long* seconds)
    """"
    ret_ad, args = jitter.func_args_cdecl(["seconds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_tzname(jitter):
    """"
    [msvcrxx.dll] errno_t _get_tzname(size_t* pReturnValue, char* timeZoneName, size_t sizeInBytes, int index)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pReturnValue", "timeZoneName", "sizeInBytes", "index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__getsystime(jitter):
    """"
    [msvcrxx.dll] unsigned _getsystime(struct tm* _tm)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_tm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__setsystime(jitter):
    """"
    [msvcrxx.dll] unsigned _setsystime(struct tm* _tm, unsigned millisec)
    """"
    ret_ad, args = jitter.func_args_cdecl(["_tm", "millisec"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_output_format(jitter):
    """"
    [msvcrxx.dll] [output_format] _get_output_format()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_output_format(jitter):
    """"
    [msvcrxx.dll] [output_format] _set_output_format([output_format] format)
    """"
    ret_ad, args = jitter.func_args_cdecl(["format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__get_printf_count_output(jitter):
    """"
    [msvcrxx.dll] int _get_printf_count_output()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__set_printf_count_output(jitter):
    """"
    [msvcrxx.dll] int _set_printf_count_output(int enable)
    """"
    ret_ad, args = jitter.func_args_cdecl(["enable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__lock(jitter):
    """"
    [msvcrxx.dll] void _lock([LOCK_NUM] locknum)
    """"
    ret_ad, args = jitter.func_args_cdecl(["locknum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__unlock(jitter):
    """"
    [msvcrxx.dll] void _unlock([LOCK_NUM] locknum)
    """"
    ret_ad, args = jitter.func_args_cdecl(["locknum"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__initterm(jitter):
    """"
    [msvcrxx.dll] void _initterm(_PVFV* pfbegin, _PVFV* pfend)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pfbegin", "pfend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__initterm_e(jitter):
    """"
    [msvcrxx.dll] int _initterm_e(_PVFV* pfbegin, _PVFV* pfend)
    """"
    ret_ad, args = jitter.func_args_cdecl(["pfbegin", "pfend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___RTDynamicCast(jitter):
    """"
    [msvcrxx.dll] PVOID __RTDynamicCast(PVOID inptr, LONG VfDelta, PVOID SrcType, PVOID TargetType, BOOL isReference)
    """"
    ret_ad, args = jitter.func_args_cdecl(["inptr", "VfDelta", "SrcType", "TargetType", "isReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx___p__commode(jitter):
    """"
    [msvcrxx.dll] int* __p__commode()
    """"
    ret_ad, args = jitter.func_args_cdecl([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)

def msvcrxx__beep(jitter):
    """"
    [msvcrxx.dll] void _beep(unsigned frequency, unsigned duration)
    """"
    ret_ad, args = jitter.func_args_cdecl(["frequency", "duration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_cdecl(ret_ad, ret_value)
