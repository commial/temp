
def usp10_ScriptApplyDigitSubstitution(jitter):
    """
    [Usp10.dll] HRESULT ScriptApplyDigitSubstitution(const SCRIPT_DIGITSUBSTITUTE* psds, SCRIPT_CONTROL* psc, SCRIPT_STATE* pss)
    """
    ret_ad, args = jitter.func_args_stdcall(["psds", "psc", "pss"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptApplyLogicalWidth(jitter):
    """
    [Usp10.dll] HRESULT ScriptApplyLogicalWidth(const int* piDx, int cChars, int cGlyphs, const WORD* pwLogClust, const SCRIPT_VISATTR* psva, const int* piAdvance, const SCRIPT_ANALYSIS* psa, ABC* pABC, int* piJustify)
    """
    ret_ad, args = jitter.func_args_stdcall(["piDx", "cChars", "cGlyphs", "pwLogClust", "psva", "piAdvance", "psa", "pABC", "piJustify"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptBreak(jitter):
    """
    [Usp10.dll] HRESULT ScriptBreak(const WCHAR* pwcChars, int cChars, const SCRIPT_ANALYSIS* psa, SCRIPT_LOGATTR* psla)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcChars", "cChars", "psa", "psla"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptCacheGetHeight(jitter):
    """
    [Usp10.dll] HRESULT ScriptCacheGetHeight(HDC hdc, SCRIPT_CACHE* psc, long* tmHeight)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "tmHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptCPtoX(jitter):
    """
    [Usp10.dll] HRESULT ScriptCPtoX(int iCP, BOOL fTrailing, int cChars, int cGlyphs, const WORD* pwLogClust, const SCRIPT_VISATTR* psva, const int* piAdvance, const SCRIPT_ANALYSIS* psa, int* piX)
    """
    ret_ad, args = jitter.func_args_stdcall(["iCP", "fTrailing", "cChars", "cGlyphs", "pwLogClust", "psva", "piAdvance", "psa", "piX"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptFreeCache(jitter):
    """
    [Usp10.dll] HRESULT ScriptFreeCache(SCRIPT_CACHE* psc)
    """
    ret_ad, args = jitter.func_args_stdcall(["psc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetCMap(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetCMap(HDC hdc, SCRIPT_CACHE* psc, const WCHAR* pwcInChars, int cChars, [SGCM_FLAGS] dwFlags, WORD* pwOutGlyphs)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "pwcInChars", "cChars", "dwFlags", "pwOutGlyphs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetFontAlternateGlyphs(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetFontAlternateGlyphs(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_ANALYSIS* psa, OPENTYPE_TAG tagScript, OPENTYPE_TAG tagLangSys, OPENTYPE_TAG tagFeature, WORD wGlyphId, int cMaxAlternates, WORD* pAlternateGlyphs, int* pcAlternates)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "psa", "tagScript", "tagLangSys", "tagFeature", "wGlyphId", "cMaxAlternates", "pAlternateGlyphs", "pcAlternates"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetFontFeatureTags(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetFontFeatureTags(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_ANALYSIS* psa, OPENTYPE_TAG tagScript, OPENTYPE_TAG tagLangSys, int cMaxTags, OPENTYPE_TAG* pFeatureTags, int* pcTags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "psa", "tagScript", "tagLangSys", "cMaxTags", "pFeatureTags", "pcTags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetFontLanguageTags(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetFontLanguageTags(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_ANALYSIS* psa, OPENTYPE_TAG tagScript, int cMaxTags, OPENTYPE_TAG* pLangSysTags, int* pcTags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "psa", "tagScript", "cMaxTags", "pLangSysTags", "pcTags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetFontProperties(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetFontProperties(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_FONTPROPERTIES* sfp)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "sfp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetFontScriptTags(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetFontScriptTags(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_ANALYSIS* psa, int cMaxTags, OPENTYPE_TAG* pScriptTags, int* pcTags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "psa", "cMaxTags", "pScriptTags", "pcTags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetGlyphABCWidth(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetGlyphABCWidth(HDC hdc, SCRIPT_CACHE* psc, WORD wGlyph, ABC* pABC)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "wGlyph", "pABC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetLogicalWidths(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetLogicalWidths(const SCRIPT_ANALYSIS* psa, int cChars, int cGlyphs, const int* piGlyphWidth, const WORD* pwLogClust, const SCRIPT_VISATTR* psva, int* piDx)
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "cChars", "cGlyphs", "piGlyphWidth", "pwLogClust", "psva", "piDx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptGetProperties(jitter):
    """
    [Usp10.dll] HRESULT ScriptGetProperties(const SCRIPT_PROPERTIES*** ppSp, int* piNumScripts)
    """
    ret_ad, args = jitter.func_args_stdcall(["ppSp", "piNumScripts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptIsComplex(jitter):
    """
    [Usp10.dll] HRESULT ScriptIsComplex(const WCHAR* pwcInChars, int cInChars, [SIC_FLAGS] dwFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcInChars", "cInChars", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptItemize(jitter):
    """
    [Usp10.dll] HRESULT ScriptItemize(const WCHAR* pwcInChars, int cInChars, int cMaxItems, const SCRIPT_CONTROL* psControl, const SCRIPT_STATE* psState, SCRIPT_ITEM* pItems, int* pcItems)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcInChars", "cInChars", "cMaxItems", "psControl", "psState", "pItems", "pcItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptItemizeOpenType(jitter):
    """
    [Usp10.dll] HRESULT ScriptItemizeOpenType(const WCHAR* pwcInChars, int cInChars, int cMaxItems, const SCRIPT_CONTROL* psControl, const SCRIPT_STATE* psState, SCRIPT_ITEM* pItems, OPENTYPE_TAG* pScriptTags, int* pcItems)
    """
    ret_ad, args = jitter.func_args_stdcall(["pwcInChars", "cInChars", "cMaxItems", "psControl", "psState", "pItems", "pScriptTags", "pcItems"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptJustify(jitter):
    """
    [Usp10.dll] HRESULT ScriptJustify(const SCRIPT_VISATTR* psva, const int* piAdvance, int cGlyphs, int iDx, int iMinKashida, int* piJustify)
    """
    ret_ad, args = jitter.func_args_stdcall(["psva", "piAdvance", "cGlyphs", "iDx", "iMinKashida", "piJustify"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptLayout(jitter):
    """
    [Usp10.dll] HRESULT ScriptLayout(int cRuns, const BYTE* pbLevel, int* piVisualToLogical, int* piLogicalToVisual)
    """
    ret_ad, args = jitter.func_args_stdcall(["cRuns", "pbLevel", "piVisualToLogical", "piLogicalToVisual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptPlace(jitter):
    """
    [Usp10.dll] HRESULT ScriptPlace(HDC hdc, SCRIPT_CACHE* psc, const WORD* pwGlyphs, int cGlyphs, const SCRIPT_VISATTR* psva, SCRIPT_ANALYSIS* psa, int* piAdvance, GOFFSET* pGoffset, ABC* pABC)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "pwGlyphs", "cGlyphs", "psva", "psa", "piAdvance", "pGoffset", "pABC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptPlaceOpenType(jitter):
    """
    [Usp10.dll] HRESULT ScriptPlaceOpenType(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_ANALYSIS* psa, OPENTYPE_TAG tagScript, OPENTYPE_TAG tagLangSys, int* rcRangeChars, TEXTRANGE_PROPERTIES** rpRangeProperties, int cRanges, const WCHAR* pwcChars, WORD* pwLogClust, SCRIPT_CHARPROP* pCharProps, int cChars, const WORD* pwGlyphs, const SCRIPT_GLYPHPROP* pGlyphProps, int cGlyphs, int* piAdvance, GOFFSET* pGoffset, ABC* pABC)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "psa", "tagScript", "tagLangSys", "rcRangeChars", "rpRangeProperties", "cRanges", "pwcChars", "pwLogClust", "pCharProps", "cChars", "pwGlyphs", "pGlyphProps", "cGlyphs", "piAdvance", "pGoffset", "pABC"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptPositionSingleGlyph(jitter):
    """
    [Usp10.dll] HRESULT ScriptPositionSingleGlyph(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_ANALYSIS* psa, OPENTYPE_TAG tagScript, OPENTYPE_TAG tagLangSys, OPENTYPE_TAG tagFeature, LONG lParameter, WORD wGlyphId, int iAdvance, GOFFSET Goffset, int* piOutAdvance, GOFFSET* pOutGoffset)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "psa", "tagScript", "tagLangSys", "tagFeature", "lParameter", "wGlyphId", "iAdvance", "Goffset", "piOutAdvance", "pOutGoffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptRecordDigitSubstitution(jitter):
    """
    [Usp10.dll] HRESULT ScriptRecordDigitSubstitution(LCID Locale, SCRIPT_DIGITSUBSTITUTE* psds)
    """
    ret_ad, args = jitter.func_args_stdcall(["Locale", "psds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptShape(jitter):
    """
    [Usp10.dll] HRESULT ScriptShape(HDC hdc, SCRIPT_CACHE* psc, const WCHAR* pwcChars, int cChars, int cMaxGlyphs, SCRIPT_ANALYSIS* psa, WORD* pwOutGlyphs, WORD* pwLogClust, SCRIPT_VISATTR* psva, int* pcGlyphs)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "pwcChars", "cChars", "cMaxGlyphs", "psa", "pwOutGlyphs", "pwLogClust", "psva", "pcGlyphs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptShapeOpenType(jitter):
    """
    [Usp10.dll] HRESULT ScriptShapeOpenType(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_ANALYSIS* psa, OPENTYPE_TAG tagScript, OPENTYPE_TAG tagLangSys, int* rcRangeChars, TEXTRANGE_PROPERTIES** rpRangeProperties, int cRanges, const WCHAR* pwcChars, int cChars, int cMaxGlyphs, WORD* pwLogClust, SCRIPT_CHARPROP* pCharProps, WORD* pwOutGlyphs, SCRIPT_GLYPHPROP* pOutGlyphProps, int* pcGlyphs)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "psa", "tagScript", "tagLangSys", "rcRangeChars", "rpRangeProperties", "cRanges", "pwcChars", "cChars", "cMaxGlyphs", "pwLogClust", "pCharProps", "pwOutGlyphs", "pOutGlyphProps", "pcGlyphs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptStringAnalyse(jitter):
    """
    [Usp10.dll] HRESULT ScriptStringAnalyse(HDC hdc, const void* pString, int cString, int cGlyphs, int iCharset, [SSA_FLAGS] dwFlags, int iReqWidth, SCRIPT_CONTROL* psControl, SCRIPT_STATE* psState, const int* piDx, SCRIPT_TABDEF* pTabdef, const BYTE* pbInClass, SCRIPT_STRING_ANALYSIS* pssa)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "pString", "cString", "cGlyphs", "iCharset", "dwFlags", "iReqWidth", "psControl", "psState", "piDx", "pTabdef", "pbInClass", "pssa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptStringCPtoX(jitter):
    """
    [Usp10.dll] HRESULT ScriptStringCPtoX(SCRIPT_STRING_ANALYSIS ssa, int icp, BOOL fTrailing, int* pX)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa", "icp", "fTrailing", "pX"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptStringFree(jitter):
    """
    [Usp10.dll] HRESULT ScriptStringFree(SCRIPT_STRING_ANALYSIS* pssa)
    """
    ret_ad, args = jitter.func_args_stdcall(["pssa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptStringGetLogicalWidths(jitter):
    """
    [Usp10.dll] HRESULT ScriptStringGetLogicalWidths(SCRIPT_STRING_ANALYSIS ssa, int* piDx)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa", "piDx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptStringGetOrder(jitter):
    """
    [Usp10.dll] HRESULT ScriptStringGetOrder(SCRIPT_STRING_ANALYSIS ssa, UINT* puOrder)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa", "puOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptStringOut(jitter):
    """
    [Usp10.dll] HRESULT ScriptStringOut(SCRIPT_STRING_ANALYSIS ssa, int iX, int iY, [ExtTextOutFlags] uOptions, const RECT* prc, int iMinSel, int iMaxSel, BOOL fDisabled)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa", "iX", "iY", "uOptions", "prc", "iMinSel", "iMaxSel", "fDisabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptString_pcOutChars(jitter):
    """
    [Usp10.dll] const int* ScriptString_pcOutChars(SCRIPT_STRING_ANALYSIS ssa)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptString_pLogAttr(jitter):
    """
    [Usp10.dll] const SCRIPT_LOGATTR* ScriptString_pLogAttr(SCRIPT_STRING_ANALYSIS ssa)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptString_pSize(jitter):
    """
    [Usp10.dll] const SIZE* ScriptString_pSize(SCRIPT_STRING_ANALYSIS ssa)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptStringValidate(jitter):
    """
    [Usp10.dll] HRESULT ScriptStringValidate(SCRIPT_STRING_ANALYSIS ssa)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptStringXtoCP(jitter):
    """
    [Usp10.dll] HRESULT ScriptStringXtoCP(SCRIPT_STRING_ANALYSIS ssa, int iX, int* piCh, int* piTrailing)
    """
    ret_ad, args = jitter.func_args_stdcall(["ssa", "iX", "piCh", "piTrailing"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptSubstituteSingleGlyph(jitter):
    """
    [Usp10.dll] HRESULT ScriptSubstituteSingleGlyph(HDC hdc, SCRIPT_CACHE* psc, SCRIPT_ANALYSIS* psa, OPENTYPE_TAG tagScript, OPENTYPE_TAG tagLangSys, OPENTYPE_TAG tagFeature, LONG lParameter, WORD wGlyphId, WORD* pwOutGlyphId)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "psa", "tagScript", "tagLangSys", "tagFeature", "lParameter", "wGlyphId", "pwOutGlyphId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptTextOut(jitter):
    """
    [Usp10.dll] HRESULT ScriptTextOut(const HDC hdc, SCRIPT_CACHE* psc, int x, int y, [ExtTextOutFlags] fuOptions, const RECT* lprc, const SCRIPT_ANALYSIS* psa, const WCHAR* pwcReserved, int iReserved, const WORD* pwGlyphs, int cGlyphs, const int* piAdvance, const int* piJustify, const GOFFSET* pGoffset)
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "psc", "x", "y", "fuOptions", "lprc", "psa", "pwcReserved", "iReserved", "pwGlyphs", "cGlyphs", "piAdvance", "piJustify", "pGoffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def usp10_ScriptXtoCP(jitter):
    """
    [Usp10.dll] HRESULT ScriptXtoCP(int iX, int cChars, int cGlyphs, const WORD* pwLogClust, const SCRIPT_VISATTR* psva, const int* piAdvance, const SCRIPT_ANALYSIS* psa, int* piCP, int* piTrailing)
    """
    ret_ad, args = jitter.func_args_stdcall(["iX", "cChars", "cGlyphs", "pwLogClust", "psva", "piAdvance", "psa", "piCP", "piTrailing"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
