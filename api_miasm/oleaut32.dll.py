###### Enums ######
_OleLoadPictureExFlags_ = {
    "LP_DEFAULT": 0x00,
    "LP_MONOCHROME": 0x01,
    "LP_VGACOLOR": 0x02,
    "LP_COLOR": 0x04,
}
_OleLoadPictureExFlags__INV = {
    0x00: "LP_DEFAULT",
    0x01: "LP_MONOCHROME",
    0x02: "LP_VGACOLOR",
    0x04: "LP_COLOR",
}
REGKIND = {
    "REGKIND_DEFAULT": 0,
    "REGKIND_REGISTER": 1,
    "REGKIND_NONE": 2,
}
REGKIND_INV = {
    0: "REGKIND_DEFAULT",
    1: "REGKIND_REGISTER",
    2: "REGKIND_NONE",
}

###################

###### Types ######
DECIMAL_PTR = LPVOID
LPDECIMAL = LPVOID
const_DECIMAL_PTR = LPVOID
OLE_COLOR = DWORD
LPBSTR = Ptr("<I", BSTR())
SHORT_PTR = Ptr("<I", SHORT())

class _PICTDESC_u_s1_(MemStruct):
    fields = [
        ("hbitmap", HBITMAP()),
        ("hpal", HPALETTE()),
    ]


class _PICTDESC_u_s2_(MemStruct):
    fields = [
        ("hmeta", HMETAFILE()),
        ("xExt", int()),
        ("yExt", int()),
    ]


class _PICTDESC_u_s3_(MemStruct):
    fields = [
        ("hicon", HICON()),
    ]


class _PICTDESC_u_s4_(MemStruct):
    fields = [
        ("hemf", HENHMETAFILE()),
    ]

_PICTDESC_u_ = Union([
    ("bmp", _PICTDESC_u_s1_),
    ("wmf", _PICTDESC_u_s2_),
    ("icon", _PICTDESC_u_s3_),
    ("emf", _PICTDESC_u_s4_),
])
_PICTYPE_ = UINT

class PICTDESC(MemStruct):
    fields = [
        ("cbSizeofstruct", UINT()),
        ("picType", _PICTYPE_()),
        (None, _PICTDESC_u_()),
    ]

LPPICTDESC = Ptr("<I", PICTDESC())

class CY(MemStruct):
    fields = [
        ("Lo", unsigned_long()),
        ("Hi", long()),
    ]

CY_PTR = Ptr("<I", CY())
LPCY = Ptr("<I", CY())

class FONTDESC(MemStruct):
    fields = [
        ("cbSizeofstruct", UINT()),
        ("lpstrName", LPOLESTR()),
        ("cySize", CY()),
        ("sWeight", SHORT()),
        ("sCharset", SHORT()),
        ("fItalic", BOOL()),
        ("fUnderline", BOOL()),
        ("fStrikethrough", BOOL()),
    ]

LPFONTDESC = Ptr("<I", FONTDESC())

class OCPFIPARAMS(MemStruct):
    fields = [
        ("cbStructSize", ULONG()),
        ("hWndOwner", HWND()),
        ("x", int()),
        ("y", int()),
        ("lpszCaption", LPCOLESTR()),
        ("cObjects", ULONG()),
        ("lplpUnk", LPUNKNOWN_PTR()),
        ("cPages", ULONG()),
        ("lpPages", CLSID_PTR()),
        ("lcid", LCID()),
        ("dispidInitialProperty", DISPID()),
    ]

LPOCPFIPARAMS = Ptr("<I", OCPFIPARAMS())
_OleLoadPictureExFlags_ = DWORD
REGKIND = UINT

class UDATE(MemStruct):
    fields = [
        ("st", SYSTEMTIME()),
        ("wDayOfYear", USHORT()),
    ]

UDATE_PTR = Ptr("<I", UDATE())
_NUMPRS_FLAG_ = ULONG

class NUMPARSE(MemStruct):
    fields = [
        ("cDig", INT()),
        ("dwInFlags", _NUMPRS_FLAG_()),
        ("dwOutFlags", _NUMPRS_FLAG_()),
        ("cchUsed", INT()),
        ("nBaseShift", INT()),
        ("nPwr10", INT()),
    ]

NUMPARSE_PTR = Ptr("<I", NUMPARSE())

class PARAMDATA(MemStruct):
    fields = [
        ("szName", OLECHAR_PTR()),
        ("vt", VARTYPE()),
    ]

PARAMDATA_PTR = Ptr("<I", PARAMDATA())

class METHODDATA(MemStruct):
    fields = [
        ("szName", OLECHAR_PTR()),
        ("ppdata", PARAMDATA_PTR()),
        ("dispid", DISPID()),
        ("iMeth", UINT()),
        ("cc", CALLCONV()),
        ("cArgs", UINT()),
        ("wFlags", _InvokeFlags_()),
        ("vtReturn", VARTYPE()),
    ]

METHODDATA_PTR = Ptr("<I", METHODDATA())

class INTERFACEDATA(MemStruct):
    fields = [
        ("pmethdata", METHODDATA_PTR()),
        ("cMembers", UINT()),
    ]

INTERFACEDATA_PTR = Ptr("<I", INTERFACEDATA())

###################

###### Functions ######

def oleaut32_OleIconToCursor(jitter):
    """
    HCURSOR OleIconToCursor(
        HINSTANCE hinstExe,
        HICON hIcon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hinstExe", "hIcon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleCreateFontIndirect(jitter):
    """
    HRESULT OleCreateFontIndirect(
        LPFONTDESC lpFontDesc,
        REFIID riid,
        LPVOID* lplpvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpFontDesc", "riid", "lplpvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleCreatePictureIndirect(jitter):
    """
    HRESULT OleCreatePictureIndirect(
        LPPICTDESC lpPictDesc,
        REFIID riid,
        BOOL fOwn,
        LPVOID* lplpvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpPictDesc", "riid", "fOwn", "lplpvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleLoadPicture(jitter):
    """
    HRESULT OleLoadPicture(
        LPSTREAM lpstream,
        LONG lSize,
        BOOL fRunmode,
        REFIID riid,
        LPVOID* lplpvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpstream", "lSize", "fRunmode", "riid", "lplpvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleLoadPictureEx(jitter):
    """
    HRESULT OleLoadPictureEx(
        LPSTREAM lpstream,
        LONG lSize,
        BOOL fRunmode,
        REFIID riid,
        DWORD xSizeDesired,
        DWORD ySizeDesired,
        [OleLoadPictureExFlags] dwFlags,
        LPVOID* lplpvObj
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpstream", "lSize", "fRunmode", "riid", "xSizeDesired", "ySizeDesired", "dwFlags", "lplpvObj"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleCreatePropertyFrame(jitter):
    """
    HRESULT OleCreatePropertyFrame(
        HWND hwndOwner,
        UINT x,
        UINT y,
        LPCOLESTR lpszCaption,
        ULONG cObjects,
        LPUNKNOWN* ppUnk,
        ULONG cPages,
        LPCLSID pPageClsID,
        LCID lcid,
        DWORD dwReserved,
        LPVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndOwner", "x", "y", "lpszCaption", "cObjects", "ppUnk", "cPages", "pPageClsID", "lcid", "dwReserved", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleCreatePropertyFrameIndirect(jitter):
    """
    HRESULT OleCreatePropertyFrameIndirect(
        LPOCPFIPARAMS lpParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleLoadPicturePath(jitter):
    """
    HRESULT OleLoadPicturePath(
        LPOLESTR szURLorPath,
        LPUNKNOWN punkCaller,
        DWORD dwReserved,
        OLE_COLOR clrReserved,
        REFIID riid,
        LPVOID* ppvRet
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szURLorPath", "punkCaller", "dwReserved", "clrReserved", "riid", "ppvRet"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleTranslateColor(jitter):
    """
    HRESULT OleTranslateColor(
        OLE_COLOR clr,
        HPALETTE hpal,
        COLORREF* lpcolorref
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["clr", "hpal", "lpcolorref"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayAccessData(jitter):
    """
    HRESULT SafeArrayAccessData(
        SAFEARRAY* psa,
        void** ppvData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "ppvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayAllocData(jitter):
    """
    HRESULT SafeArrayAllocData(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayAllocDescriptor(jitter):
    """
    HRESULT SafeArrayAllocDescriptor(
        UINT cDims,
        SAFEARRAY** ppsaOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cDims", "ppsaOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayAllocDescriptorEx(jitter):
    """
    HRESULT SafeArrayAllocDescriptorEx(
        VARTYPE vt,
        UINT cDims,
        SAFEARRAY** ppsaOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vt", "cDims", "ppsaOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayCopy(jitter):
    """
    HRESULT SafeArrayCopy(
        SAFEARRAY* psa,
        SAFEARRAY** ppsaOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "ppsaOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayCopyData(jitter):
    """
    HRESULT SafeArrayCopyData(
        SAFEARRAY* psaSource,
        SAFEARRAY* psaTarget
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psaSource", "psaTarget"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayCreate(jitter):
    """
    SAFEARRAY* SafeArrayCreate(
        VARTYPE vt,
        UINT cDims,
        SAFEARRAYBOUND* rgsabound
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vt", "cDims", "rgsabound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayCreateEx(jitter):
    """
    SAFEARRAY* SafeArrayCreateEx(
        VARTYPE vt,
        UINT cDims,
        SAFEARRAYBOUND* rgsabound,
        PVOID pvExtra
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vt", "cDims", "rgsabound", "pvExtra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayCreateVector(jitter):
    """
    SAFEARRAY* SafeArrayCreateVector(
        VARTYPE vt,
        LONG lLbound,
        ULONG cElements
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vt", "lLbound", "cElements"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayCreateVectorEx(jitter):
    """
    SAFEARRAY* SafeArrayCreateVectorEx(
        VARTYPE vt,
        LONG lLbound,
        ULONG cElements,
        PVOID pvExtra
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vt", "lLbound", "cElements", "pvExtra"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayDestroy(jitter):
    """
    HRESULT SafeArrayDestroy(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayDestroyData(jitter):
    """
    HRESULT SafeArrayDestroyData(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayDestroyDescriptor(jitter):
    """
    HRESULT SafeArrayDestroyDescriptor(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayGetDim(jitter):
    """
    UINT SafeArrayGetDim(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayGetElement(jitter):
    """
    HRESULT SafeArrayGetElement(
        SAFEARRAY* psa,
        LONG* rgIndices,
        void* pv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "rgIndices", "pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayGetElemsize(jitter):
    """
    UINT SafeArrayGetElemsize(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayGetIID(jitter):
    """
    HRESULT SafeArrayGetIID(
        SAFEARRAY* psa,
        GUID* pguid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "pguid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayGetLBound(jitter):
    """
    HRESULT SafeArrayGetLBound(
        SAFEARRAY* psa,
        UINT nDim,
        LONG* plLbound
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "nDim", "plLbound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayGetRecordInfo(jitter):
    """
    HRESULT SafeArrayGetRecordInfo(
        SAFEARRAY* psa,
        IRecordInfo** prinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "prinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayGetUBound(jitter):
    """
    HRESULT SafeArrayGetUBound(
        SAFEARRAY* psa,
        UINT nDim,
        LONG* plUbound
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "nDim", "plUbound"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayGetVartype(jitter):
    """
    HRESULT SafeArrayGetVartype(
        SAFEARRAY* psa,
        VARTYPE* pvt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "pvt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayLock(jitter):
    """
    HRESULT SafeArrayLock(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayPtrOfIndex(jitter):
    """
    HRESULT SafeArrayPtrOfIndex(
        SAFEARRAY* psa,
        LONG* rgIndices,
        void** ppvData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "rgIndices", "ppvData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayPutElement(jitter):
    """
    HRESULT SafeArrayPutElement(
        SAFEARRAY* psa,
        LONG* rgIndices,
        void* pv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "rgIndices", "pv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayRedim(jitter):
    """
    HRESULT SafeArrayRedim(
        SAFEARRAY* psa,
        SAFEARRAYBOUND* psaboundNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "psaboundNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArraySetIID(jitter):
    """
    HRESULT SafeArraySetIID(
        SAFEARRAY* psa,
        REFGUID guid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "guid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArraySetRecordInfo(jitter):
    """
    HRESULT SafeArraySetRecordInfo(
        SAFEARRAY* psa,
        IRecordInfo* prinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "prinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayUnaccessData(jitter):
    """
    HRESULT SafeArrayUnaccessData(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SafeArrayUnlock(jitter):
    """
    HRESULT SafeArrayUnlock(
        SAFEARRAY* psa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BstrFromVector(jitter):
    """
    HRESULT BstrFromVector(
        SAFEARRAY* psa,
        BSTR* pbstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psa", "pbstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SetOaNoCache(jitter):
    """
    void SetOaNoCache()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrCat(jitter):
    """
    HRESULT VarBstrCat(
        BSTR bstrLeft,
        BSTR bstrRight,
        LPBSTR pbstrResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bstrLeft", "bstrRight", "pbstrResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrCmp(jitter):
    """
    HRESULT VarBstrCmp(
        BSTR bstrLeft,
        BSTR bstrRight,
        LCID lcid,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bstrLeft", "bstrRight", "lcid", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VectorFromBstr(jitter):
    """
    HRESULT VectorFromBstr(
        BSTR bstr,
        SAFEARRAY** ppsa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bstr", "ppsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyAbs(jitter):
    """
    HRESULT VarCyAbs(
        CY cyIn,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyAdd(jitter):
    """
    HRESULT VarCyAdd(
        CY cyLeft,
        CY cyRight,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyLeft", "cyRight", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyCmp(jitter):
    """
    HRESULT VarCyCmp(
        CY cyLeft,
        CY cyRight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyLeft", "cyRight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyCmpR8(jitter):
    """
    HRESULT VarCyCmpR8(
        CY cyLeft,
        double dblRight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyLeft", "dblRight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFix(jitter):
    """
    HRESULT VarCyFix(
        CY cyIn,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyInt(jitter):
    """
    HRESULT VarCyInt(
        CY cyIn,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyMul(jitter):
    """
    HRESULT VarCyMul(
        CY cyLeft,
        CY cyRight,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyLeft", "cyRight", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyMulI4(jitter):
    """
    HRESULT VarCyMulI4(
        CY cyLeft,
        long lRight,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyLeft", "lRight", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyMulI8(jitter):
    """
    HRESULT VarCyMulI8(
        CY cyLeft,
        LONG64 lRight,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyLeft", "lRight", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyNeg(jitter):
    """
    HRESULT VarCyNeg(
        CY cyIn,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyRound(jitter):
    """
    HRESULT VarCyRound(
        CY cyIn,
        int cDecimals,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "cDecimals", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCySub(jitter):
    """
    HRESULT VarCySub(
        CY cyLeft,
        CY cyRight,
        LPCY pcyResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyLeft", "cyRight", "pcyResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_GetVarConversionLocaleSetting(jitter):
    """
    HRESULT GetVarConversionLocaleSetting(
        ULONG* dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SetVarConversionLocaleSetting(jitter):
    """
    HRESULT SetVarConversionLocaleSetting(
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromUI1(jitter):
    """
    HRESULT VarI1FromUI1(
        BYTE bIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromUI2(jitter):
    """
    HRESULT VarI1FromUI2(
        USHORT uiIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromUI4(jitter):
    """
    HRESULT VarI1FromUI4(
        ULONG ulIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromUI8(jitter):
    """
    HRESULT VarI1FromUI8(
        ULONG64 i64In,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromI2(jitter):
    """
    HRESULT VarI1FromI2(
        SHORT uiIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromI4(jitter):
    """
    HRESULT VarI1FromI4(
        LONG lIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromI8(jitter):
    """
    HRESULT VarI1FromI8(
        LONG64 i64In,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromR4(jitter):
    """
    HRESULT VarI1FromR4(
        FLOAT fltIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromR8(jitter):
    """
    HRESULT VarI1FromR8(
        DOUBLE dblIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromCy(jitter):
    """
    HRESULT VarI1FromCy(
        CY cyIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromDec(jitter):
    """
    HRESULT VarI1FromDec(
        const DECIMAL* pdecIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromDate(jitter):
    """
    HRESULT VarI1FromDate(
        DATE dateIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromStr(jitter):
    """
    HRESULT VarI1FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromDisp(jitter):
    """
    HRESULT VarI1FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI1FromBool(jitter):
    """
    HRESULT VarI1FromBool(
        VARIANT_BOOL boolIn,
        CHAR* pcOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pcOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromUI2(jitter):
    """
    HRESULT VarUI1FromUI2(
        USHORT uiIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromUI4(jitter):
    """
    HRESULT VarUI1FromUI4(
        ULONG ulIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromUI8(jitter):
    """
    HRESULT VarUI1FromUI8(
        ULONG64 i64In,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromI1(jitter):
    """
    HRESULT VarUI1FromI1(
        CHAR cIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromI2(jitter):
    """
    HRESULT VarUI1FromI2(
        SHORT sIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromI4(jitter):
    """
    HRESULT VarUI1FromI4(
        LONG lIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromI8(jitter):
    """
    HRESULT VarUI1FromI8(
        LONG64 i64In,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromR4(jitter):
    """
    HRESULT VarUI1FromR4(
        FLOAT fltIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromR8(jitter):
    """
    HRESULT VarUI1FromR8(
        DOUBLE dblIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromCy(jitter):
    """
    HRESULT VarUI1FromCy(
        CY cyIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromDec(jitter):
    """
    HRESULT VarUI1FromDec(
        const DECIMAL* pdecIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromDate(jitter):
    """
    HRESULT VarUI1FromDate(
        DATE dateIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromStr(jitter):
    """
    HRESULT VarUI1FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromDisp(jitter):
    """
    HRESULT VarUI1FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI1FromBool(jitter):
    """
    HRESULT VarUI1FromBool(
        VARIANT_BOOL boolIn,
        BYTE* pbOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pbOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromUI1(jitter):
    """
    HRESULT VarI2FromUI1(
        BYTE bIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromUI2(jitter):
    """
    HRESULT VarI2FromUI2(
        USHORT uiIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromUI4(jitter):
    """
    HRESULT VarI2FromUI4(
        ULONG ulIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromUI8(jitter):
    """
    HRESULT VarI2FromUI8(
        ULONG64 ui64In,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromI1(jitter):
    """
    HRESULT VarI2FromI1(
        CHAR cIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromI4(jitter):
    """
    HRESULT VarI2FromI4(
        LONG lIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromI8(jitter):
    """
    HRESULT VarI2FromI8(
        LONG64 i64In,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromR4(jitter):
    """
    HRESULT VarI2FromR4(
        FLOAT fltIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromR8(jitter):
    """
    HRESULT VarI2FromR8(
        DOUBLE dblIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromCy(jitter):
    """
    HRESULT VarI2FromCy(
        CY cyIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromDec(jitter):
    """
    HRESULT VarI2FromDec(
        const DECIMAL* pdecIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromDate(jitter):
    """
    HRESULT VarI2FromDate(
        DATE dateIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromStr(jitter):
    """
    HRESULT VarI2FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromDisp(jitter):
    """
    HRESULT VarI2FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI2FromBool(jitter):
    """
    HRESULT VarI2FromBool(
        VARIANT_BOOL boolIn,
        SHORT* psOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "psOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromI1(jitter):
    """
    HRESULT VarUI2FromI1(
        CHAR cIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromI2(jitter):
    """
    HRESULT VarUI2FromI2(
        SHORT uiIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromI4(jitter):
    """
    HRESULT VarUI2FromI4(
        LONG lIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromI8(jitter):
    """
    HRESULT VarUI2FromI8(
        LONG64 i64In,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromUI1(jitter):
    """
    HRESULT VarUI2FromUI1(
        BYTE bIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromUI4(jitter):
    """
    HRESULT VarUI2FromUI4(
        ULONG ulIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromUI8(jitter):
    """
    HRESULT VarUI2FromUI8(
        ULONG64 i64In,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromR4(jitter):
    """
    HRESULT VarUI2FromR4(
        FLOAT fltIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromR8(jitter):
    """
    HRESULT VarUI2FromR8(
        DOUBLE dblIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromCy(jitter):
    """
    HRESULT VarUI2FromCy(
        CY cyIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromDec(jitter):
    """
    HRESULT VarUI2FromDec(
        const DECIMAL* pdecIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromDate(jitter):
    """
    HRESULT VarUI2FromDate(
        DATE dateIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromStr(jitter):
    """
    HRESULT VarUI2FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromDisp(jitter):
    """
    HRESULT VarUI2FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI2FromBool(jitter):
    """
    HRESULT VarUI2FromBool(
        VARIANT_BOOL boolIn,
        USHORT* puiOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "puiOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromUI2(jitter):
    """
    HRESULT VarI4FromUI2(
        USHORT uiIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromUI4(jitter):
    """
    HRESULT VarI4FromUI4(
        ULONG ulIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromUI8(jitter):
    """
    HRESULT VarI4FromUI8(
        ULONG64 ui64In,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromI1(jitter):
    """
    HRESULT VarI4FromI1(
        CHAR cIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromUI1(jitter):
    """
    HRESULT VarI4FromUI1(
        BYTE bIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromI2(jitter):
    """
    HRESULT VarI4FromI2(
        SHORT sIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromI8(jitter):
    """
    HRESULT VarI4FromI8(
        LONG64 i64In,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromR4(jitter):
    """
    HRESULT VarI4FromR4(
        FLOAT fltIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromR8(jitter):
    """
    HRESULT VarI4FromR8(
        DOUBLE dblIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromCy(jitter):
    """
    HRESULT VarI4FromCy(
        CY cyIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromDec(jitter):
    """
    HRESULT VarI4FromDec(
        const DECIMAL* pdecIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromDate(jitter):
    """
    HRESULT VarI4FromDate(
        DATE dateIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromStr(jitter):
    """
    HRESULT VarI4FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromDisp(jitter):
    """
    HRESULT VarI4FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI4FromBool(jitter):
    """
    HRESULT VarI4FromBool(
        VARIANT_BOOL boolIn,
        LONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromUI2(jitter):
    """
    HRESULT VarUI4FromUI2(
        USHORT uiIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromI1(jitter):
    """
    HRESULT VarUI4FromI1(
        CHAR cIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromI2(jitter):
    """
    HRESULT VarUI4FromI2(
        SHORT uiIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromUI1(jitter):
    """
    HRESULT VarUI4FromUI1(
        BYTE bIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromUI8(jitter):
    """
    HRESULT VarUI4FromUI8(
        ULONG64 ui64In,
        ULONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromI4(jitter):
    """
    HRESULT VarUI4FromI4(
        LONG lIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromI8(jitter):
    """
    HRESULT VarUI4FromI8(
        LONG64 i64In,
        ULONG* plOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "plOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromR4(jitter):
    """
    HRESULT VarUI4FromR4(
        FLOAT fltIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromR8(jitter):
    """
    HRESULT VarUI4FromR8(
        DOUBLE dblIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromCy(jitter):
    """
    HRESULT VarUI4FromCy(
        CY cyIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromDec(jitter):
    """
    HRESULT VarUI4FromDec(
        const DECIMAL* pdecIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromDate(jitter):
    """
    HRESULT VarUI4FromDate(
        DATE dateIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromStr(jitter):
    """
    HRESULT VarUI4FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromDisp(jitter):
    """
    HRESULT VarUI4FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI4FromBool(jitter):
    """
    HRESULT VarUI4FromBool(
        VARIANT_BOOL boolIn,
        ULONG* pulOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pulOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromUI2(jitter):
    """
    HRESULT VarR4FromUI2(
        USHORT uiIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromUI4(jitter):
    """
    HRESULT VarR4FromUI4(
        ULONG ulIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromUI8(jitter):
    """
    HRESULT VarR4FromUI8(
        ULONG64 ui64In,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromI1(jitter):
    """
    HRESULT VarR4FromI1(
        CHAR cIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromUI1(jitter):
    """
    HRESULT VarR4FromUI1(
        BYTE bIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromI2(jitter):
    """
    HRESULT VarR4FromI2(
        SHORT sIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromI4(jitter):
    """
    HRESULT VarR4FromI4(
        LONG lIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromI8(jitter):
    """
    HRESULT VarR4FromI8(
        LONG64 i64In,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromR8(jitter):
    """
    HRESULT VarR4FromR8(
        DOUBLE dblIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromCy(jitter):
    """
    HRESULT VarR4FromCy(
        CY cyIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromDec(jitter):
    """
    HRESULT VarR4FromDec(
        const DECIMAL* pdecIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromDate(jitter):
    """
    HRESULT VarR4FromDate(
        DATE dateIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromStr(jitter):
    """
    HRESULT VarR4FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromDisp(jitter):
    """
    HRESULT VarR4FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4FromBool(jitter):
    """
    HRESULT VarR4FromBool(
        VARIANT_BOOL boolIn,
        FLOAT* pfltOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pfltOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromUI2(jitter):
    """
    HRESULT VarR8FromUI2(
        USHORT uiIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromUI4(jitter):
    """
    HRESULT VarR8FromUI4(
        ULONG ulIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromUI8(jitter):
    """
    HRESULT VarR8FromUI8(
        ULONG64 ui64In,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromI1(jitter):
    """
    HRESULT VarR8FromI1(
        CHAR cIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromUI1(jitter):
    """
    HRESULT VarR8FromUI1(
        BYTE bIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromI2(jitter):
    """
    HRESULT VarR8FromI2(
        SHORT sIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromI4(jitter):
    """
    HRESULT VarR8FromI4(
        LONG lIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromI8(jitter):
    """
    HRESULT VarR8FromI8(
        LONG64 i64In,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromR4(jitter):
    """
    HRESULT VarR8FromR4(
        FLOAT fltIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromCy(jitter):
    """
    HRESULT VarR8FromCy(
        CY cyIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromDec(jitter):
    """
    HRESULT VarR8FromDec(
        const DECIMAL* pdecIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromDate(jitter):
    """
    HRESULT VarR8FromDate(
        DATE dateIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromStr(jitter):
    """
    HRESULT VarR8FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromDisp(jitter):
    """
    HRESULT VarR8FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8FromBool(jitter):
    """
    HRESULT VarR8FromBool(
        VARIANT_BOOL boolIn,
        DOUBLE* pdblOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pdblOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromUI2(jitter):
    """
    HRESULT VarDateFromUI2(
        USHORT uiIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromUI4(jitter):
    """
    HRESULT VarDateFromUI4(
        ULONG ulIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromUI8(jitter):
    """
    HRESULT VarDateFromUI8(
        ULONG64 ui64In,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromI1(jitter):
    """
    HRESULT VarDateFromI1(
        CHAR cIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromUI1(jitter):
    """
    HRESULT VarDateFromUI1(
        BYTE bIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromI2(jitter):
    """
    HRESULT VarDateFromI2(
        SHORT sIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromI4(jitter):
    """
    HRESULT VarDateFromI4(
        LONG lIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromI8(jitter):
    """
    HRESULT VarDateFromI8(
        LONG64 i64In,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromR4(jitter):
    """
    HRESULT VarDateFromR4(
        FLOAT fltIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromR8(jitter):
    """
    HRESULT VarDateFromR8(
        DOUBLE dblIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromCy(jitter):
    """
    HRESULT VarDateFromCy(
        CY cyIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromDec(jitter):
    """
    HRESULT VarDateFromDec(
        const DECIMAL* pdecIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromStr(jitter):
    """
    HRESULT VarDateFromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromDisp(jitter):
    """
    HRESULT VarDateFromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromBool(jitter):
    """
    HRESULT VarDateFromBool(
        VARIANT_BOOL boolIn,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromUI2(jitter):
    """
    HRESULT VarCyFromUI2(
        USHORT uiIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromUI4(jitter):
    """
    HRESULT VarCyFromUI4(
        ULONG ulIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromUI8(jitter):
    """
    HRESULT VarCyFromUI8(
        ULONG64 ui64In,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromI1(jitter):
    """
    HRESULT VarCyFromI1(
        CHAR cIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromUI1(jitter):
    """
    HRESULT VarCyFromUI1(
        BYTE bIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromI2(jitter):
    """
    HRESULT VarCyFromI2(
        SHORT sIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromI4(jitter):
    """
    HRESULT VarCyFromI4(
        LONG lIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromI8(jitter):
    """
    HRESULT VarCyFromI8(
        LONG64 i64In,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromR4(jitter):
    """
    HRESULT VarCyFromR4(
        FLOAT fltIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromR8(jitter):
    """
    HRESULT VarCyFromR8(
        DOUBLE dblIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromDec(jitter):
    """
    HRESULT VarCyFromDec(
        const DECIMAL* pdecIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromDate(jitter):
    """
    HRESULT VarCyFromDate(
        DATE dateIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromStr(jitter):
    """
    HRESULT VarCyFromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromDisp(jitter):
    """
    HRESULT VarCyFromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCyFromBool(jitter):
    """
    HRESULT VarCyFromBool(
        VARIANT_BOOL boolIn,
        CY* pcyOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pcyOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromUI2(jitter):
    """
    HRESULT VarBstrFromUI2(
        USHORT uiIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromUI4(jitter):
    """
    HRESULT VarBstrFromUI4(
        ULONG ulIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromUI8(jitter):
    """
    HRESULT VarBstrFromUI8(
        ULONG64 ui64In,
        LCID lcid,
        unsigned long dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromI1(jitter):
    """
    HRESULT VarBstrFromI1(
        CHAR cIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromUI1(jitter):
    """
    HRESULT VarBstrFromUI1(
        BYTE bVal,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bVal", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromI2(jitter):
    """
    HRESULT VarBstrFromI2(
        SHORT iVal,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iVal", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromI4(jitter):
    """
    HRESULT VarBstrFromI4(
        LONG lIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromI8(jitter):
    """
    HRESULT VarBstrFromI8(
        LONG64 i64In,
        LCID lcid,
        unsigned long dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromR4(jitter):
    """
    HRESULT VarBstrFromR4(
        FLOAT fltIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromR8(jitter):
    """
    HRESULT VarBstrFromR8(
        DOUBLE dblIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromCy(jitter):
    """
    HRESULT VarBstrFromCy(
        CY cyIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromDec(jitter):
    """
    HRESULT VarBstrFromDec(
        const DECIMAL* pdecIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromDate(jitter):
    """
    HRESULT VarBstrFromDate(
        DATE dateIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromDisp(jitter):
    """
    HRESULT VarBstrFromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBstrFromBool(jitter):
    """
    HRESULT VarBstrFromBool(
        VARIANT_BOOL boolIn,
        LCID lcid,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "lcid", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromUI2(jitter):
    """
    HRESULT VarBoolFromUI2(
        USHORT uiIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromUI4(jitter):
    """
    HRESULT VarBoolFromUI4(
        ULONG ulIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromUI8(jitter):
    """
    HRESULT VarBoolFromUI8(
        ULONG64 i64In,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromI1(jitter):
    """
    HRESULT VarBoolFromI1(
        CHAR cIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromUI1(jitter):
    """
    HRESULT VarBoolFromUI1(
        BYTE bIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromI2(jitter):
    """
    HRESULT VarBoolFromI2(
        SHORT sIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromI4(jitter):
    """
    HRESULT VarBoolFromI4(
        LONG lIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromI8(jitter):
    """
    HRESULT VarBoolFromI8(
        LONG64 i64In,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromR4(jitter):
    """
    HRESULT VarBoolFromR4(
        FLOAT fltIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromR8(jitter):
    """
    HRESULT VarBoolFromR8(
        DOUBLE dblIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromCy(jitter):
    """
    HRESULT VarBoolFromCy(
        CY cyIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromDec(jitter):
    """
    HRESULT VarBoolFromDec(
        const DECIMAL* pdecIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromDate(jitter):
    """
    HRESULT VarBoolFromDate(
        DATE dateIn,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromStr(jitter):
    """
    HRESULT VarBoolFromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarBoolFromDisp(jitter):
    """
    HRESULT VarBoolFromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        VARIANT_BOOL* pboolOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pboolOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromUI2(jitter):
    """
    HRESULT VarDecFromUI2(
        USHORT uiIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromUI4(jitter):
    """
    HRESULT VarDecFromUI4(
        ULONG ulIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromUI8(jitter):
    """
    HRESULT VarDecFromUI8(
        ULONG64 ui64In,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromI1(jitter):
    """
    HRESULT VarDecFromI1(
        CHAR cIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromUI1(jitter):
    """
    HRESULT VarDecFromUI1(
        BYTE bIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromI2(jitter):
    """
    HRESULT VarDecFromI2(
        SHORT uiIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromI4(jitter):
    """
    HRESULT VarDecFromI4(
        LONG lIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromI8(jitter):
    """
    HRESULT VarDecFromI8(
        LONG64 i64In,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["i64In", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromR4(jitter):
    """
    HRESULT VarDecFromR4(
        FLOAT fltIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromR8(jitter):
    """
    HRESULT VarDecFromR8(
        DOUBLE dblIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromCy(jitter):
    """
    HRESULT VarDecFromCy(
        CY cyIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromDate(jitter):
    """
    HRESULT VarDecFromDate(
        DATE dateIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromStr(jitter):
    """
    HRESULT VarDecFromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromDisp(jitter):
    """
    HRESULT VarDecFromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFromBool(jitter):
    """
    HRESULT VarDecFromBool(
        VARIANT_BOOL boolIn,
        DECIMAL* pdecOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pdecOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromBool(jitter):
    """
    HRESULT VarI8FromBool(
        VARIANT_BOOL boolIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromCy(jitter):
    """
    HRESULT VarI8FromCy(
        CY cyIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromDate(jitter):
    """
    HRESULT VarI8FromDate(
        DATE dateIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromDec(jitter):
    """
    HRESULT VarI8FromDec(
        const DECIMAL* pdecIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromDisp(jitter):
    """
    HRESULT VarI8FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromI1(jitter):
    """
    HRESULT VarI8FromI1(
        CHAR cIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromI2(jitter):
    """
    HRESULT VarI8FromI2(
        SHORT sIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromR4(jitter):
    """
    HRESULT VarI8FromR4(
        FLOAT fltIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromR8(jitter):
    """
    HRESULT VarI8FromR8(
        DOUBLE dblIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromStr(jitter):
    """
    HRESULT VarI8FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        unsigned long dwFlags,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromUI1(jitter):
    """
    HRESULT VarI8FromUI1(
        BYTE bIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromUI2(jitter):
    """
    HRESULT VarI8FromUI2(
        USHORT uiIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromUI4(jitter):
    """
    HRESULT VarI8FromUI4(
        ULONG ulIn,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarI8FromUI8(jitter):
    """
    HRESULT VarI8FromUI8(
        ULONG64 ui64In,
        LONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromBool(jitter):
    """
    HRESULT VarUI8FromBool(
        VARIANT_BOOL boolIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["boolIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromCy(jitter):
    """
    HRESULT VarUI8FromCy(
        CY cyIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cyIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromDate(jitter):
    """
    HRESULT VarUI8FromDate(
        DATE dateIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromDec(jitter):
    """
    HRESULT VarUI8FromDec(
        const DECIMAL* pdecIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromDisp(jitter):
    """
    HRESULT VarUI8FromDisp(
        IDispatch* pdispIn,
        LCID lcid,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispIn", "lcid", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromI1(jitter):
    """
    HRESULT VarUI8FromI1(
        CHAR cIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromI2(jitter):
    """
    HRESULT VarUI8FromI2(
        SHORT sIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromI8(jitter):
    """
    HRESULT VarUI8FromI8(
        LONG64 ui64In,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ui64In", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromR4(jitter):
    """
    HRESULT VarUI8FromR4(
        FLOAT fltIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromR8(jitter):
    """
    HRESULT VarUI8FromR8(
        DOUBLE dblIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromStr(jitter):
    """
    HRESULT VarUI8FromStr(
        LPCOLESTR strIn,
        LCID lcid,
        unsigned long dwFlags,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromUI1(jitter):
    """
    HRESULT VarUI8FromUI1(
        BYTE bIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromUI2(jitter):
    """
    HRESULT VarUI8FromUI2(
        USHORT uiIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUI8FromUI4(jitter):
    """
    HRESULT VarUI8FromUI4(
        ULONG ulIn,
        ULONG64* pi64Out
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ulIn", "pi64Out"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_DosDateTimeToVariantTime(jitter):
    """
    INT DosDateTimeToVariantTime(
        USHORT wDosDate,
        USHORT wDosTime,
        DOUBLE* pvtime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["wDosDate", "wDosTime", "pvtime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_GetAltMonthNames(jitter):
    """
    HRESULT GetAltMonthNames(
        LCID lcid,
        LPOLESTR** prgp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lcid", "prgp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SystemTimeToVariantTime(jitter):
    """
    INT SystemTimeToVariantTime(
        LPSYSTEMTIME lpSystemTime,
        DOUBLE* pvtime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSystemTime", "pvtime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromUdate(jitter):
    """
    HRESULT VarDateFromUdate(
        UDATE* pudateIn,
        ULONG dwFlags,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pudateIn", "dwFlags", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDateFromUdateEx(jitter):
    """
    HRESULT VarDateFromUdateEx(
        UDATE* pudateIn,
        LCID lcid,
        ULONG dwFlags,
        DATE* pdateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pudateIn", "lcid", "dwFlags", "pdateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VariantTimeToDosDateTime(jitter):
    """
    INT VariantTimeToDosDateTime(
        DOUBLE vtime,
        USHORT* pwDosDate,
        USHORT* pwDosTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vtime", "pwDosDate", "pwDosTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VariantTimeToSystemTime(jitter):
    """
    INT VariantTimeToSystemTime(
        DOUBLE vtime,
        LPSYSTEMTIME lpSystemTime
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vtime", "lpSystemTime"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarUdateFromDate(jitter):
    """
    HRESULT VarUdateFromDate(
        DATE dateIn,
        ULONG dwFlags,
        UDATE* pudateOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dateIn", "dwFlags", "pudateOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecAbs(jitter):
    """
    HRESULT VarDecAbs(
        LPDECIMAL pdecIn,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecAdd(jitter):
    """
    HRESULT VarDecAdd(
        LPDECIMAL pdecLeft,
        LPDECIMAL pdecRight,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecLeft", "pdecRight", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecCmp(jitter):
    """
    HRESULT VarDecCmp(
        LPDECIMAL pdecLeft,
        LPDECIMAL pdecRight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecLeft", "pdecRight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecCmpR8(jitter):
    """
    HRESULT VarDecCmpR8(
        LPDECIMAL pdecLeft,
        double dblRight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecLeft", "dblRight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecDiv(jitter):
    """
    HRESULT VarDecDiv(
        LPDECIMAL pdecLeft,
        LPDECIMAL pdecRight,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecLeft", "pdecRight", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecFix(jitter):
    """
    HRESULT VarDecFix(
        LPDECIMAL pdecIn,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecInt(jitter):
    """
    HRESULT VarDecInt(
        LPDECIMAL pdecIn,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecMul(jitter):
    """
    HRESULT VarDecMul(
        LPDECIMAL pdecLeft,
        LPDECIMAL pdecRight,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecLeft", "pdecRight", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecNeg(jitter):
    """
    HRESULT VarDecNeg(
        LPDECIMAL pdecIn,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecRound(jitter):
    """
    HRESULT VarDecRound(
        LPDECIMAL pdecIn,
        int cDecimals,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecIn", "cDecimals", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDecSub(jitter):
    """
    HRESULT VarDecSub(
        LPDECIMAL pdecLeft,
        LPDECIMAL pdecRight,
        LPDECIMAL pdecResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdecLeft", "pdecRight", "pdecResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarNumFromParseNum(jitter):
    """
    HRESULT VarNumFromParseNum(
        NUMPARSE* pnumprs,
        BYTE* rgbDig,
        ULONG dwVtBits,
        VARIANT* pvar
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pnumprs", "rgbDig", "dwVtBits", "pvar"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarParseNumFromStr(jitter):
    """
    HRESULT VarParseNumFromStr(
        LPCOLESTR strIn,
        LCID lcid,
        ULONG dwFlags,
        NUMPARSE* pnumprs,
        BYTE* rgbDig
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "lcid", "dwFlags", "pnumprs", "rgbDig"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BSTR_UserFree(jitter):
    """
    void BSTR_UserFree(
        unsigned long* pFlags,
        BSTR* pBstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BSTR_UserFree64(jitter):
    """
    void BSTR_UserFree64(
        unsigned long* pFlags,
        BSTR* pBstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BSTR_UserMarshal(jitter):
    """
    unsigned char* BSTR_UserMarshal(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        BSTR* pBstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "pBstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BSTR_UserMarshal64(jitter):
    """
    unsigned char* BSTR_UserMarshal64(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        BSTR* pBstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "pBstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BSTR_UserSize(jitter):
    """
    unsigned long BSTR_UserSize(
        unsigned long* pFlags,
        unsigned long Offset,
        BSTR* pBstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "Offset", "pBstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BSTR_UserSize64(jitter):
    """
    unsigned long BSTR_UserSize64(
        unsigned long* pFlags,
        unsigned long Offset,
        BSTR* pBstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "Offset", "pBstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BSTR_UserUnmarshal(jitter):
    """
    unsigned char* BSTR_UserUnmarshal(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        BSTR* pBstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "pBstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_BSTR_UserUnmarshal64(jitter):
    """
    unsigned char* BSTR_UserUnmarshal64(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        BSTR* pBstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "pBstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LPSAFEARRAY_Marshal(jitter):
    """
    unsigned char* LPSAFEARRAY_Marshal(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        LPSAFEARRAY* ppSafeArray,
        const IID* piid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppSafeArray", "piid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LPSAFEARRAY_Size(jitter):
    """
    unsigned long LPSAFEARRAY_Size(
        unsigned long* pFlags,
        unsigned long Offset,
        LPSAFEARRAY* ppSafeArray,
        const IID* piid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "Offset", "ppSafeArray", "piid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LPSAFEARRAY_Unmarshal(jitter):
    """
    unsigned char* LPSAFEARRAY_Unmarshal(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        LPSAFEARRAY* ppSafeArray,
        const IID* piid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppSafeArray", "piid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LPSAFEARRAY_UserFree(jitter):
    """
    void LPSAFEARRAY_UserFree(
        unsigned long* pFlags,
        LPSAFEARRAY* ppSafeArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "ppSafeArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LPSAFEARRAY_UserMarshal(jitter):
    """
    unsigned char* LPSAFEARRAY_UserMarshal(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        LPSAFEARRAY* ppSafeArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppSafeArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LPSAFEARRAY_UserSize(jitter):
    """
    unsigned long LPSAFEARRAY_UserSize(
        unsigned long* pFlags,
        unsigned long Offset,
        LPSAFEARRAY* ppSafeArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "Offset", "ppSafeArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LPSAFEARRAY_UserUnmarshal(jitter):
    """
    unsigned char* LPSAFEARRAY_UserUnmarshal(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        LPSAFEARRAY* ppSafeArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "ppSafeArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VARIANT_UserFree(jitter):
    """
    void VARIANT_UserFree(
        unsigned long* pFlags,
        VARIANT* pVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VARIANT_UserFree64(jitter):
    """
    void VARIANT_UserFree64(
        unsigned long* pFlags,
        VARIANT* pVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VARIANT_UserMarshal(jitter):
    """
    unsigned char* VARIANT_UserMarshal(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        VARIANT* pVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "pVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VARIANT_UserMarshal64(jitter):
    """
    unsigned char* VARIANT_UserMarshal64(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        VARIANT* pVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "pVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VARIANT_UserSize(jitter):
    """
    unsigned long VARIANT_UserSize(
        unsigned long* pFlags,
        unsigned long Offset,
        VARIANT* pVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "Offset", "pVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VARIANT_UserSize64(jitter):
    """
    unsigned long VARIANT_UserSize64(
        unsigned long* pFlags,
        unsigned long Offset,
        VARIANT* pVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "Offset", "pVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VARIANT_UserUnmarshal(jitter):
    """
    unsigned char* VARIANT_UserUnmarshal(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        VARIANT* pVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "pVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VARIANT_UserUnmarshal64(jitter):
    """
    unsigned char* VARIANT_UserUnmarshal64(
        unsigned long* pFlags,
        unsigned char* pBuffer,
        VARIANT* pVariant
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFlags", "pBuffer", "pVariant"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SysAllocString(jitter):
    """
    BSTR SysAllocString(
        const OLECHAR* psz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SysAllocStringByteLen(jitter):
    """
    BSTR SysAllocStringByteLen(
        LPCSTR psz,
        UINT len
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["psz", "len"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SysAllocStringLen(jitter):
    """
    BSTR SysAllocStringLen(
        const OLECHAR* strIn,
        UINT ui
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["strIn", "ui"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SysFreeString(jitter):
    """
    void SysFreeString(
        BSTR bstrString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bstrString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SysReAllocString(jitter):
    """
    INT SysReAllocString(
        BSTR* pbstr,
        const OLECHAR* psz
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbstr", "psz"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SysReAllocStringLen(jitter):
    """
    INT SysReAllocStringLen(
        BSTR* pbstr,
        const OLECHAR* psz,
        unsigned int len
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbstr", "psz", "len"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SysStringByteLen(jitter):
    """
    UINT SysStringByteLen(
        BSTR bstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SysStringLen(jitter):
    """
    UINT SysStringLen(
        BSTR bstr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bstr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarAbs(jitter):
    """
    HRESULT VarAbs(
        LPVARIANT pvarIn,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarAdd(jitter):
    """
    HRESULT VarAdd(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarAnd(jitter):
    """
    HRESULT VarAnd(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCat(jitter):
    """
    HRESULT VarCat(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarCmp(jitter):
    """
    HRESULT VarCmp(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LCID lcid,
        ULONG dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "lcid", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarDiv(jitter):
    """
    HRESULT VarDiv(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarEqv(jitter):
    """
    HRESULT VarEqv(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarFix(jitter):
    """
    HRESULT VarFix(
        LPVARIANT pvarIn,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarIdiv(jitter):
    """
    HRESULT VarIdiv(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarImp(jitter):
    """
    HRESULT VarImp(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarInt(jitter):
    """
    HRESULT VarInt(
        LPVARIANT pvarIn,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarMod(jitter):
    """
    HRESULT VarMod(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarMul(jitter):
    """
    HRESULT VarMul(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarNeg(jitter):
    """
    HRESULT VarNeg(
        LPVARIANT pvarIn,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarNot(jitter):
    """
    HRESULT VarNot(
        LPVARIANT pvarIn,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarOr(jitter):
    """
    HRESULT VarOr(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarPow(jitter):
    """
    HRESULT VarPow(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR4CmpR8(jitter):
    """
    HRESULT VarR4CmpR8(
        float fltLeft,
        double dblRight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fltLeft", "dblRight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8Pow(jitter):
    """
    HRESULT VarR8Pow(
        double dblLeft,
        double dblRight,
        double* pdblResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblLeft", "dblRight", "pdblResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarR8Round(jitter):
    """
    HRESULT VarR8Round(
        double dblIn,
        int cDecimals,
        double* pdblResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dblIn", "cDecimals", "pdblResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarRound(jitter):
    """
    HRESULT VarRound(
        LPVARIANT pvarIn,
        int cDecimals,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "cDecimals", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarSub(jitter):
    """
    HRESULT VarSub(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarXor(jitter):
    """
    HRESULT VarXor(
        LPVARIANT pvarLeft,
        LPVARIANT pvarRight,
        LPVARIANT pvarResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarLeft", "pvarRight", "pvarResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VariantChangeType(jitter):
    """
    HRESULT VariantChangeType(
        VARIANTARG* pvargDest,
        const VARIANTARG* pvarSrc,
        USHORT wFlags,
        VARTYPE vt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvargDest", "pvarSrc", "wFlags", "vt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VariantChangeTypeEx(jitter):
    """
    HRESULT VariantChangeTypeEx(
        VARIANTARG* pvargDest,
        const VARIANTARG* pvarSrc,
        LCID lcid,
        USHORT wFlags,
        VARTYPE vt
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvargDest", "pvarSrc", "lcid", "wFlags", "vt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VariantClear(jitter):
    """
    HRESULT VariantClear(
        VARIANTARG* pvarg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VariantCopy(jitter):
    """
    HRESULT VariantCopy(
        VARIANTARG* pvargDest,
        const VARIANTARG* pvargSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvargDest", "pvargSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VariantCopyInd(jitter):
    """
    HRESULT VariantCopyInd(
        VARIANT* pvarDest,
        const VARIANTARG* pvargSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarDest", "pvargSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VariantInit(jitter):
    """
    void VariantInit(
        VARIANTARG* pvarg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_CreateDispTypeInfo(jitter):
    """
    HRESULT CreateDispTypeInfo(
        INTERFACEDATA* pidata,
        LCID lcid,
        ITypeInfo** pptinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pidata", "lcid", "pptinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_CreateStdDispatch(jitter):
    """
    HRESULT CreateStdDispatch(
        IUnknown* punkOuter,
        void* pvThis,
        ITypeInfo* ptinfo,
        IUnknown** ppunkStdDisp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punkOuter", "pvThis", "ptinfo", "ppunkStdDisp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_DispCallFunc(jitter):
    """
    HRESULT DispCallFunc(
        void* pvInstance,
        ULONG_PTR oVft,
        CALLCONV cc,
        VARTYPE vtReturn,
        UINT cActuals,
        VARTYPE* prgvt,
        VARIANTARG** prgpvarg,
        VARIANT* pvargResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvInstance", "oVft", "cc", "vtReturn", "cActuals", "prgvt", "prgpvarg", "pvargResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_DispGetIDsOfNames(jitter):
    """
    HRESULT DispGetIDsOfNames(
        ITypeInfo* ptinfo,
        OLECHAR** rgszNames,
        UINT cNames,
        DISPID* rgdispid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ptinfo", "rgszNames", "cNames", "rgdispid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_DispGetParam(jitter):
    """
    HRESULT DispGetParam(
        DISPPARAMS* pdispparams,
        UINT position,
        VARTYPE vtTarg,
        VARIANT* pvarResult,
        UINT* puArgErr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdispparams", "position", "vtTarg", "pvarResult", "puArgErr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_DispInvoke(jitter):
    """
    HRESULT DispInvoke(
        void* _this,
        ITypeInfo* ptinfo,
        DISPID dispidMember,
        WORD wFlags,
        DISPPARAMS* pparams,
        VARIANT* pvarResult,
        EXCEPINFO* pexcepinfo,
        UINT* puArgErr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["_this", "ptinfo", "dispidMember", "wFlags", "pparams", "pvarResult", "pexcepinfo", "puArgErr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_CreateErrorInfo(jitter):
    """
    HRESULT CreateErrorInfo(
        ICreateErrorInfo** pperrinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pperrinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_GetErrorInfo(jitter):
    """
    HRESULT GetErrorInfo(
        ULONG dwReserved,
        IErrorInfo** pperrinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved", "pperrinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_SetErrorInfo(jitter):
    """
    HRESULT SetErrorInfo(
        ULONG dwReserved,
        IErrorInfo* perrinfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReserved", "perrinfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarFormat(jitter):
    """
    HRESULT VarFormat(
        LPVARIANT pvarIn,
        LPOLESTR pstrFormat,
        int iFirstDay,
        int iFirstWeek,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "pstrFormat", "iFirstDay", "iFirstWeek", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarFormatCurrency(jitter):
    """
    HRESULT VarFormatCurrency(
        LPVARIANT pvarIn,
        int iNumDig,
        int iIncLead,
        int iUseParens,
        int iGroup,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "iNumDig", "iIncLead", "iUseParens", "iGroup", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarFormatDateTime(jitter):
    """
    HRESULT VarFormatDateTime(
        LPVARIANT pvarIn,
        int iNamedFormat,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "iNamedFormat", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarFormatFromTokens(jitter):
    """
    HRESULT VarFormatFromTokens(
        LPVARIANT pvarIn,
        LPOLESTR pstrFormat,
        LPBYTE pbTokCur,
        ULONG dwFlags,
        BSTR* pbstrOut,
        LCID lcid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "pstrFormat", "pbTokCur", "dwFlags", "pbstrOut", "lcid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarFormatNumber(jitter):
    """
    HRESULT VarFormatNumber(
        LPVARIANT pvarIn,
        int iNumDig,
        int iIncLead,
        int iUseParens,
        int iGroup,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "iNumDig", "iIncLead", "iUseParens", "iGroup", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarFormatPercent(jitter):
    """
    HRESULT VarFormatPercent(
        LPVARIANT pvarIn,
        int iNumDig,
        int iIncLead,
        int iUseParens,
        int iGroup,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pvarIn", "iNumDig", "iIncLead", "iUseParens", "iGroup", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarMonthName(jitter):
    """
    HRESULT VarMonthName(
        int iMonth,
        int fAbbrev,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iMonth", "fAbbrev", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarTokenizeFormatString(jitter):
    """
    HRESULT VarTokenizeFormatString(
        LPOLESTR pstrFormat,
        LPBYTE rgbTok,
        int cbTok,
        int iFirstDay,
        int iFirstWeek,
        LCID lcid,
        int* pcbActual
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstrFormat", "rgbTok", "cbTok", "iFirstDay", "iFirstWeek", "lcid", "pcbActual"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_VarWeekdayName(jitter):
    """
    HRESULT VarWeekdayName(
        int iWeekday,
        int fAbbrev,
        int iFirstDay,
        ULONG dwFlags,
        BSTR* pbstrOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["iWeekday", "fAbbrev", "iFirstDay", "dwFlags", "pbstrOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleLoadPictureFile(jitter):
    """
    HRESULT OleLoadPictureFile(
        VARIANT varFileName,
        LPDISPATCH* lplpdispPicture
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["varFileName", "lplpdispPicture"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleLoadPictureFileEx(jitter):
    """
    HRESULT OleLoadPictureFileEx(
        VARIANT varFileName,
        DWORD xSizeDesired,
        DWORD ySizeDesired,
        DWORD dwFlags,
        LPDISPATCH* lplpdispPicture
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["varFileName", "xSizeDesired", "ySizeDesired", "dwFlags", "lplpdispPicture"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OleSavePictureFile(jitter):
    """
    HRESULT OleSavePictureFile(
        LPDISPATCH lpdispPicture,
        BSTR bstrFileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpdispPicture", "bstrFileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_GetActiveObject(jitter):
    """
    HRESULT GetActiveObject(
        REFCLSID rclsid,
        void* pvReserved,
        IUnknown** ppunk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "pvReserved", "ppunk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_RegisterActiveObject(jitter):
    """
    HRESULT RegisterActiveObject(
        IUnknown* punk,
        REFCLSID rclsid,
        DWORD dwFlags,
        DWORD* pdwRegister
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["punk", "rclsid", "dwFlags", "pdwRegister"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_RevokeActiveObject(jitter):
    """
    HRESULT RevokeActiveObject(
        DWORD dwRegister,
        void* pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwRegister", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_CreateTypeLib(jitter):
    """
    HRESULT CreateTypeLib(
        SYSKIND syskind,
        LPCOLESTR szFile,
        ICreateTypeLib** ppctlib
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["syskind", "szFile", "ppctlib"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_CreateTypeLib2(jitter):
    """
    HRESULT CreateTypeLib2(
        SYSKIND syskind,
        LPCOLESTR szFile,
        ICreateTypeLib2** ppctlib
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["syskind", "szFile", "ppctlib"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OACreateTypeLib2(jitter):
    """
    HRESULT OACreateTypeLib2(
        SYSKIND syskind,
        LPCOLESTR szFile,
        ICreateTypeLib2** ppctlib
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["syskind", "szFile", "ppctlib"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OaBuildVersion(jitter):
    """
    ULONG OaBuildVersion()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LHashValOfNameSys(jitter):
    """
    ULONG LHashValOfNameSys(
        SYSKIND syskind,
        LCID lcid,
        const OLECHAR* szName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["syskind", "lcid", "szName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LHashValOfNameSysA(jitter):
    """
    ULONG LHashValOfNameSysA(
        SYSKIND syskind,
        LCID lcid,
        LPCSTR szName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["syskind", "lcid", "szName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LoadRegTypeLib(jitter):
    """
    HRESULT LoadRegTypeLib(
        REFGUID rguid,
        WORD wVerMajor,
        WORD wVerMinor,
        LCID lcid,
        ITypeLib** pptlib
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rguid", "wVerMajor", "wVerMinor", "lcid", "pptlib"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LoadTypeLib(jitter):
    """
    HRESULT LoadTypeLib(
        LPCOLESTR szFile,
        ITypeLib** pptlib
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFile", "pptlib"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_LoadTypeLibEx(jitter):
    """
    HRESULT LoadTypeLibEx(
        LPCOLESTR szFile,
        REGKIND regkind,
        ITypeLib** pptlib
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["szFile", "regkind", "pptlib"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_OaEnablePerUserTLibRegistration(jitter):
    """
    void OaEnablePerUserTLibRegistration()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_QueryPathOfRegTypeLib(jitter):
    """
    HRESULT QueryPathOfRegTypeLib(
        REFGUID guid,
        USHORT wMaj,
        USHORT wMin,
        LCID lcid,
        LPBSTR lpbstrPathName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["guid", "wMaj", "wMin", "lcid", "lpbstrPathName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_RegisterTypeLib(jitter):
    """
    HRESULT RegisterTypeLib(
        ITypeLib* ptlib,
        LPCOLESTR szFullPath,
        LPCOLESTR szHelpDir
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ptlib", "szFullPath", "szHelpDir"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_RegisterTypeLibForUser(jitter):
    """
    HRESULT RegisterTypeLibForUser(
        ITypeLib* ptlib,
        OLECHAR* szFullPath,
        OLECHAR* szHelpDir
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ptlib", "szFullPath", "szHelpDir"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_UnRegisterTypeLib(jitter):
    """
    HRESULT UnRegisterTypeLib(
        REFGUID libID,
        WORD wVerMajor,
        WORD wVerMinor,
        LCID lcid,
        SYSKIND syskind
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["libID", "wVerMajor", "wVerMinor", "lcid", "syskind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_UnRegisterTypeLibForUser(jitter):
    """
    HRESULT UnRegisterTypeLibForUser(
        REFGUID libID,
        WORD wMajorVerNum,
        WORD wMinorVerNum,
        LCID lcid,
        SYSKIND syskind
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["libID", "wMajorVerNum", "wMinorVerNum", "lcid", "syskind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_ClearCustData(jitter):
    """
    void ClearCustData(
        LPCUSTDATA pCustData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCustData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_GetRecordInfoFromGuids(jitter):
    """
    HRESULT GetRecordInfoFromGuids(
        REFGUID rGuidTypeLib,
        ULONG uVerMajor,
        ULONG uVerMinor,
        LCID lcid,
        REFGUID rGuidTypeInfo,
        IRecordInfo** ppRecInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rGuidTypeLib", "uVerMajor", "uVerMinor", "lcid", "rGuidTypeInfo", "ppRecInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def oleaut32_GetRecordInfoFromTypeInfo(jitter):
    """
    HRESULT GetRecordInfoFromTypeInfo(
        ITypeInfo* pTypeInfo,
        IRecordInfo** ppRecInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTypeInfo", "ppRecInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
