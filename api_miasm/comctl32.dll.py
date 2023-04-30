_WSB_Prop_ = {
    "WSB_PROP_CYVSCROLL": 0x00000001,
    "WSB_PROP_CXHSCROLL": 0x00000002,
    "WSB_PROP_CYHSCROLL": 0x00000004,
    "WSB_PROP_CXVSCROLL": 0x00000008,
    "WSB_PROP_CXHTHUMB": 0x00000010,
    "WSB_PROP_CYVTHUMB": 0x00000020,
    "WSB_PROP_VBKGCOLOR": 0x00000040,
    "WSB_PROP_HBKGCOLOR": 0x00000080,
    "WSB_PROP_VSTYLE": 0x00000100,
    "WSB_PROP_HSTYLE": 0x00000200,
    "WSB_PROP_WINSTYLE": 0x00000400,
    "WSB_PROP_PALETTE": 0x00000800,
    "WSB_PROP_MASK": 0x00000FFF,
}
_WSB_Prop__INV = {
    0x00000001: "WSB_PROP_CYVSCROLL",
    0x00000002: "WSB_PROP_CXHSCROLL",
    0x00000004: "WSB_PROP_CYHSCROLL",
    0x00000008: "WSB_PROP_CXVSCROLL",
    0x00000010: "WSB_PROP_CXHTHUMB",
    0x00000020: "WSB_PROP_CYVTHUMB",
    0x00000040: "WSB_PROP_VBKGCOLOR",
    0x00000080: "WSB_PROP_HBKGCOLOR",
    0x00000100: "WSB_PROP_VSTYLE",
    0x00000200: "WSB_PROP_HSTYLE",
    0x00000400: "WSB_PROP_WINSTYLE",
    0x00000800: "WSB_PROP_PALETTE",
    0x00000FFF: "WSB_PROP_MASK",
}
_ILP_Flags_ = {
    "ILP_NORMAL": 0,
    "ILP_DOWNLEVEL": 1,
}
_ILP_Flags__INV = {
    0: "ILP_NORMAL",
    1: "ILP_DOWNLEVEL",
}

def comctl32__TrackMouseEvent(jitter):
    """
    BOOL _TrackMouseEvent(
        LPTRACKMOUSEEVENT lpEventTrack
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpEventTrack"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_AddMRUStringW(jitter):
    """
    int AddMRUStringW(
        HANDLE hMRU,
        LPCTSTR szString
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMRU", "szString"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_CreateMRUListW(jitter):
    """
    int CreateMRUListW(
        LPMRUINFO lpmi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpmi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DefSubclassProc(jitter):
    """
    LRESULT DefSubclassProc(
        HWND hWnd,
        [WinMsg] uMsg,
        WPARAM WPARAM,
        LPARAM LPARAM
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uMsg", "WPARAM", "LPARAM"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_EnumMRUListW(jitter):
    """
    int EnumMRUListW(
        HANDLE hMRU,
        int nItem,
        void* lpData,
        UINT uLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMRU", "nItem", "lpData", "uLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FreeMRUList(jitter):
    """
    int FreeMRUList(
        HANDLE hMRU
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMRU"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_GetWindowSubclass(jitter):
    """
    BOOL GetWindowSubclass(
        HWND hWnd,
        SUBCLASSPROC pfnSubclass,
        UINT_PTR uIdSubclass,
        DWORD_PTR* pdwRefData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pfnSubclass", "uIdSubclass", "pdwRefData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_RemoveWindowSubclass(jitter):
    """
    BOOL RemoveWindowSubclass(
        HWND hWnd,
        SUBCLASSPROC pfnSubclass,
        UINT_PTR uIdSubclass
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pfnSubclass", "uIdSubclass"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_SetWindowSubclass(jitter):
    """
    BOOL SetWindowSubclass(
        HWND hWnd,
        SUBCLASSPROC pfnSubclass,
        UINT_PTR uIdSubclass,
        DWORD_PTR dwRefData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pfnSubclass", "uIdSubclass", "dwRefData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_CreateMappedBitmap(jitter):
    """
    HBITMAP CreateMappedBitmap(
        HINSTANCE hInstance,
        INT_PTR idBitmap,
        UINT wFlags,
        LPCOLORMAP lpColorMap,
        int iNumMaps
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hInstance", "idBitmap", "wFlags", "lpColorMap", "iNumMaps"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_CreateToolbarEx(jitter):
    """
    HWND CreateToolbarEx(
        HWND hwnd,
        [TBStyle] ws,
        UINT wID,
        int nBitmaps,
        HINSTANCE hBMInst,
        UINT_PTR wBMID,
        LPCTBBUTTON lpButtons,
        int iNumButtons,
        int dxButton,
        int dyButton,
        int dxBitmap,
        int dyBitmap,
        UINT uStructSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "ws", "wID", "nBitmaps", "hBMInst", "wBMID", "lpButtons", "iNumButtons", "dxButton", "dyButton", "dxBitmap", "dyBitmap", "uStructSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_CreatePropertySheetPage(jitter, get_str, set_str):
    """
    HPROPSHEETPAGE CreatePropertySheetPage(
        LPCPROPSHEETPAGE lppsp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppsp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_CreatePropertySheetPageA(jitter):
    comctl32_CreatePropertySheetPage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comctl32_CreatePropertySheetPageW(jitter):
    comctl32_CreatePropertySheetPage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comctl32_DestroyPropertySheetPage(jitter):
    """
    BOOL DestroyPropertySheetPage(
        HPROPSHEETPAGE hPSPage
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hPSPage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_PropertySheet(jitter, get_str, set_str):
    """
    INT_PTR PropertySheet(
        LPCPROPSHEETHEADER lppsph
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lppsph"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_PropertySheetA(jitter):
    comctl32_PropertySheet(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comctl32_PropertySheetW(jitter):
    comctl32_PropertySheet(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comctl32_CreateStatusWindow(jitter, get_str, set_str):
    """
    HWND CreateStatusWindow(
        LONG style,
        LPCTSTR lpszText,
        HWND hwndParent,
        UINT wID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["style", "lpszText", "hwndParent", "wID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_CreateStatusWindowA(jitter):
    comctl32_CreateStatusWindow(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comctl32_CreateStatusWindowW(jitter):
    comctl32_CreateStatusWindow(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comctl32_DrawStatusText(jitter, get_str, set_str):
    """
    void DrawStatusText(
        HDC hdc,
        LPCRECT lprc,
        LPCTSTR pszText,
        UINT uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lprc", "pszText", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DrawStatusTextA(jitter):
    comctl32_DrawStatusText(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comctl32_DrawStatusTextW(jitter):
    comctl32_DrawStatusText(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comctl32_MenuHelp(jitter):
    """
    void MenuHelp(
        [WinMsg] uMsg,
        WPARAM wParam,
        LPARAM lParam,
        HMENU hMainMenu,
        HINSTANCE hInst,
        HWND hwndStatus,
        LPUINT lpwIDs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uMsg", "wParam", "lParam", "hMainMenu", "hInst", "hwndStatus", "lpwIDs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_CreateUpDownControl(jitter):
    """
    HWND CreateUpDownControl(
        [UDStyle] dwStyle,
        int x,
        int y,
        int cx,
        int cy,
        HWND hParent,
        int nID,
        HINSTANCE hInst,
        HWND hBuddy,
        int nUpper,
        int nLower,
        int nPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwStyle", "x", "y", "cx", "cy", "hParent", "nID", "hInst", "hBuddy", "nUpper", "nLower", "nPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DoReaderMode(jitter):
    """
    void DoReaderMode(
        PREADERMODEINFO prmi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["prmi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_Clone(jitter):
    """
    HDPA DPA_Clone(
        const HDPA hdpaSource,
        HDPA hdpaNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdpaSource", "hdpaNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_Create(jitter):
    """
    HDPA DPA_Create(
        int cpGrow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cpGrow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_CreateEx(jitter):
    """
    HDPA DPA_CreateEx(
        int cpGrow,
        HANDLE hheap
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cpGrow", "hheap"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_DeleteAllPtrs(jitter):
    """
    BOOL DPA_DeleteAllPtrs(
        HDPA pdpa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_DeletePtr(jitter):
    """
    void* DPA_DeletePtr(
        HDPA pdpa,
        int index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_Destroy(jitter):
    """
    BOOL DPA_Destroy(
        HDPA pdpa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_DestroyCallback(jitter):
    """
    void DPA_DestroyCallback(
        HDPA pdpa,
        PFNDPAENUMCALLBACK pfnCB,
        void* pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "pfnCB", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_EnumCallback(jitter):
    """
    void DPA_EnumCallback(
        HDPA pdpa,
        PFNDPAENUMCALLBACK pfnCB,
        void* pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "pfnCB", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_GetPtr(jitter):
    """
    void* DPA_GetPtr(
        HDPA pdpa,
        int index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_GetPtrIndex(jitter):
    """
    int DPA_GetPtrIndex(
        HDPA hdpa,
        const void* pvoid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdpa", "pvoid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_GetSize(jitter):
    """
    ULONGLONG DPA_GetSize(
        HDPA pdpa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_Grow(jitter):
    """
    BOOL DPA_Grow(
        HDPA hdpa,
        int cp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdpa", "cp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_InsertPtr(jitter):
    """
    int DPA_InsertPtr(
        HDPA pdpa,
        int index,
        void* p
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "index", "p"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_LoadStream(jitter):
    """
    HRESULT DPA_LoadStream(
        HDPA* ppdpa,
        PFNDPASTREAM pfn,
        IStream* pstm,
        void* pvInstData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppdpa", "pfn", "pstm", "pvInstData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_Merge(jitter):
    """
    BOOL DPA_Merge(
        HDPA hdpaDest,
        HDPA hdpaSrc,
        DWORD dwFlags,
        PFNDPACOMPARE pfnCompare,
        PFNDPAMERGE pfnMerge,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdpaDest", "hdpaSrc", "dwFlags", "pfnCompare", "pfnMerge", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_SaveStream(jitter):
    """
    HRESULT DPA_SaveStream(
        HDPA pdpa,
        PFNDPASTREAM pfn,
        IStream* pstm,
        void* pvInstData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "pfn", "pstm", "pvInstData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_Search(jitter):
    """
    int DPA_Search(
        HDPA pdpa,
        void* pFind,
        int iStart,
        PFNDPACOMPARE pfnCmp,
        LPARAM lParam,
        UINT options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "pFind", "iStart", "pfnCmp", "lParam", "options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_SetPtr(jitter):
    """
    BOOL DPA_SetPtr(
        HDPA pdpa,
        int index,
        void* p
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "index", "p"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DPA_Sort(jitter):
    """
    BOOL DPA_Sort(
        HDPA pdpa,
        PFNDPACOMPARE pfnCmp,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdpa", "pfnCmp", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DrawShadowText(jitter):
    """
    int DrawShadowText(
        HDC hdc,
        LPCWSTR pszText,
        UINT cch,
        const RECT* pRect,
        DWORD dwFlags,
        COLORREF crText,
        COLORREF crShadow,
        int ixOffset,
        int iyOffset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "pszText", "cch", "pRect", "dwFlags", "crText", "crShadow", "ixOffset", "iyOffset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DrawTextExPrivWrap(jitter):
    """
    int DrawTextExPrivWrap(
        HDC hdc,
        LPTSTR lpchText,
        int cchText,
        LPRECT lprc,
        UINT dwDTFormat,
        LPDRAWTEXTPARAMS lpDTParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpchText", "cchText", "lprc", "dwDTFormat", "lpDTParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DrawTextWrap(jitter):
    """
    int DrawTextWrap(
        HDC hdc,
        LPCTSTR lpString,
        int nCount,
        LPRECT lpRect,
        UINT uFormat,
        LPDRAWTEXTPARAMS lpDTParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpString", "nCount", "lpRect", "uFormat", "lpDTParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_Clone(jitter):
    """
    HDSA DSA_Clone(
        HDSA hdsa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_Create(jitter):
    """
    HDSA DSA_Create(
        int cbItem,
        int cbItemGrow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cbItem", "cbItemGrow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_DeleteAllItems(jitter):
    """
    BOOL DSA_DeleteAllItems(
        HDSA hdsa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_DeleteItem(jitter):
    """
    BOOL DSA_DeleteItem(
        HDSA hdsa,
        int nPosition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdsa", "nPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_Destroy(jitter):
    """
    BOOL DSA_Destroy(
        HDSA pdsa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_DestroyCallback(jitter):
    """
    void DSA_DestroyCallback(
        HDSA pdsa,
        PFNDSAENUMCALLBACK pfnCB,
        void* pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdsa", "pfnCB", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_EnumCallback(jitter):
    """
    void DSA_EnumCallback(
        HDSA hdsa,
        PFNDAENUMCALLBACK* pfnCB,
        void* pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdsa", "pfnCB", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_GetItem(jitter):
    """
    BOOL DSA_GetItem(
        HDSA pdsa,
        int index,
        void* pitem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdsa", "index", "pitem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_GetItemPtr(jitter):
    """
    void* DSA_GetItemPtr(
        HDSA pdsa,
        int index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdsa", "index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_GetSize(jitter):
    """
    ULONGLONG DSA_GetSize(
        HDSA hdsa
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdsa"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_InsertItem(jitter):
    """
    int DSA_InsertItem(
        HDSA pdsa,
        int index,
        void* pItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdsa", "index", "pItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_SetItem(jitter):
    """
    BOOL DSA_SetItem(
        HDSA hdsa,
        int index,
        void* pItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdsa", "index", "pItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_DSA_Sort(jitter):
    """
    BOOL DSA_Sort(
        HDSA pdsa,
        PFNDACOMPARE pfnCompare,
        LPARAM lParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdsa", "pfnCompare", "lParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ExtTextOutWrap(jitter):
    """
    BOOL ExtTextOutWrap(
        HDC hdc,
        int X,
        int Y,
        UINT uOptions,
        const RECT* lprc,
        LPCTSTR lpString,
        UINT cbCount,
        const INT* lpDx
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "X", "Y", "uOptions", "lprc", "lpString", "cbCount", "lpDx"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_GetEffectiveClientRect(jitter):
    """
    void GetEffectiveClientRect(
        HWND hWnd,
        LPRECT lprc,
        const INT* lpInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "lprc", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_GetMUILanguage(jitter):
    """
    LANGID GetMUILanguage()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_GetTextExtentPoint32Wrap(jitter):
    """
    BOOL GetTextExtentPoint32Wrap(
        HDC hdc,
        LPCTSTR lpString,
        UINT cbCount,
        LPSIZE lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hdc", "lpString", "cbCount", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_InitCommonControls(jitter):
    """
    void InitCommonControls()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_InitCommonControlsEx(jitter):
    """
    BOOL InitCommonControlsEx(
        const LPINITCOMMONCONTROLSEX lpInitCtrls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpInitCtrls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_InitMUILanguage(jitter):
    """
    VOID InitMUILanguage(
        LANGID uiLang
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uiLang"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_LoadIconMetric(jitter):
    """
    HRESULT LoadIconMetric(
        HINSTANCE hinst,
        PCWSTR pszName,
        int lims,
        HICON* phico
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hinst", "pszName", "lims", "phico"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_LoadIconWithScaleDown(jitter):
    """
    HRESULT LoadIconWithScaleDown(
        HINSTANCE hinst,
        PCWSTR pszName,
        int cx,
        int cy,
        HICON* phico
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hinst", "pszName", "cx", "cy", "phico"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_MirrorIcon(jitter):
    """
    BOOL MirrorIcon(
        HICON* phIconSmall,
        HICON* phIconLarge
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phIconSmall", "phIconLarge"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ShowHideMenuCtl(jitter):
    """
    BOOL ShowHideMenuCtl(
        HWND hWnd,
        UINT_PTR uFlags,
        LPINT lpInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "uFlags", "lpInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_Str_GetPtr(jitter, get_str, set_str):
    """
    int Str_GetPtr(
        LPCTSTR pszSource,
        LPCSTR pszDest,
        int cchDest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszSource", "pszDest", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_Str_GetPtrA(jitter):
    comctl32_Str_GetPtr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comctl32_Str_GetPtrW(jitter):
    comctl32_Str_GetPtr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comctl32_Str_SetPtr(jitter, get_str, set_str):
    """
    BOOL Str_SetPtr(
        LPTSTR* ppszCurrent,
        LPCTSTR pszNew
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppszCurrent", "pszNew"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_Str_SetPtrA(jitter):
    comctl32_Str_SetPtr(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comctl32_Str_SetPtrW(jitter):
    comctl32_Str_SetPtr(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comctl32_DrawInsert(jitter):
    """
    void DrawInsert(
        HWND handParent,
        HWND hLB,
        int nItem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["handParent", "hLB", "nItem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_LBItemFromPt(jitter):
    """
    int LBItemFromPt(
        HWND hLB,
        POINT pt,
        BOOL bAutoScroll
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLB", "pt", "bAutoScroll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_MakeDragList(jitter):
    """
    BOOL MakeDragList(
        HWND hLB
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hLB"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_EnableScrollBar(jitter):
    """
    BOOL FlatSB_EnableScrollBar(
        HWND hwnd,
        int wSBflags,
        UINT wArrows
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "wSBflags", "wArrows"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_GetScrollInfo(jitter):
    """
    BOOL FlatSB_GetScrollInfo(
        HWND hwnd,
        [SBType] fnBar,
        LPSCROLLINFO lpsi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fnBar", "lpsi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_GetScrollPos(jitter):
    """
    int FlatSB_GetScrollPos(
        HWND hwnd,
        [SBType] code
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "code"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_GetScrollProp(jitter):
    """
    BOOL FlatSB_GetScrollProp(
        HWND hwnd,
        [WSB_Prop] index,
        LPINT pValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "index", "pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_GetScrollPropPtr(jitter):
    """
    BOOL FlatSB_GetScrollPropPtr(
        HWND hwnd,
        [WSB_Prop] index,
        LPINT pValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "index", "pValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_GetScrollRange(jitter):
    """
    BOOL FlatSB_GetScrollRange(
        HWND hwnd,
        int code,
        LPINT lpMinPos,
        LPINT lpMaxPos
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "code", "lpMinPos", "lpMaxPos"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_SetScrollInfo(jitter):
    """
    int FlatSB_SetScrollInfo(
        HWND hwnd,
        [SBType] fnBar,
        LPSCROLLINFO lpsi,
        BOOL fRedraw
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "fnBar", "lpsi", "fRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_SetScrollPos(jitter):
    """
    int FlatSB_SetScrollPos(
        HWND hwnd,
        int code,
        int nPos,
        BOOL fRedraw
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "code", "nPos", "fRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_SetScrollProp(jitter):
    """
    BOOL FlatSB_SetScrollProp(
        HWND hwnd,
        [WSB_Prop] index,
        INT_PTR newValue,
        BOOL fRedraw
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "index", "newValue", "fRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_SetScrollRange(jitter):
    """
    int FlatSB_SetScrollRange(
        HWND hwnd,
        int code,
        int nMinPos,
        int nMaxPos,
        BOOL fRedraw
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "code", "nMinPos", "nMaxPos", "fRedraw"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_FlatSB_ShowScrollBar(jitter):
    """
    BOOL FlatSB_ShowScrollBar(
        HWND hwnd,
        int code,
        BOOL fShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "code", "fShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_InitializeFlatSB(jitter):
    """
    BOOL InitializeFlatSB(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_UninitializeFlatSB(jitter):
    """
    HRESULT UninitializeFlatSB(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_HIMAGELIST_QueryInterface(jitter):
    """
    HRESULT HIMAGELIST_QueryInterface(
        HIMAGELIST himl,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Add(jitter):
    """
    int ImageList_Add(
        HIMAGELIST himl,
        HBITMAP hbmImage,
        HBITMAP hbmMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "hbmImage", "hbmMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_AddMasked(jitter):
    """
    int ImageList_AddMasked(
        HIMAGELIST himl,
        HBITMAP hbmImage,
        COLORREF crMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "hbmImage", "crMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_BeginDrag(jitter):
    """
    BOOL ImageList_BeginDrag(
        HIMAGELIST himlTrack,
        int iTrack,
        int dxHotspot,
        int dyHotspot
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himlTrack", "iTrack", "dxHotspot", "dyHotspot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_CoCreateInstance(jitter):
    """
    HRESULT ImageList_CoCreateInstance(
        REFCLSID rclsid,
        const IUnknown* punkOuter,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["rclsid", "punkOuter", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Copy(jitter):
    """
    BOOL ImageList_Copy(
        HIMAGELIST himlDst,
        int iDst,
        HIMAGELIST himlSrc,
        int iSrc,
        UINT uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himlDst", "iDst", "himlSrc", "iSrc", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Create(jitter):
    """
    HIMAGELIST ImageList_Create(
        int cx,
        int cy,
        [ILC_Flags] flags,
        int cInitial,
        int cGrow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cx", "cy", "flags", "cInitial", "cGrow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Destroy(jitter):
    """
    BOOL ImageList_Destroy(
        HIMAGELIST himl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_DragEnter(jitter):
    """
    BOOL ImageList_DragEnter(
        HWND hwndLock,
        int x,
        int y
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndLock", "x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_DragLeave(jitter):
    """
    BOOL ImageList_DragLeave(
        HWND hwndLock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndLock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_DragMove(jitter):
    """
    BOOL ImageList_DragMove(
        int x,
        int y
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["x", "y"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_DragShowNolock(jitter):
    """
    BOOL ImageList_DragShowNolock(
        BOOL fShow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fShow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Draw(jitter):
    """
    BOOL ImageList_Draw(
        HIMAGELIST himl,
        int i,
        HDC hdcDst,
        int x,
        int y,
        [ILD_Flags] fStyle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "i", "hdcDst", "x", "y", "fStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_DrawEx(jitter):
    """
    BOOL ImageList_DrawEx(
        HIMAGELIST himl,
        int i,
        HDC hdcDst,
        int x,
        int y,
        int dx,
        int dy,
        COLORREF rgbBk,
        COLORREF rgbFg,
        [ILD_Flags] fStyle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "i", "hdcDst", "x", "y", "dx", "dy", "rgbBk", "rgbFg", "fStyle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_DrawIndirect(jitter):
    """
    BOOL ImageList_DrawIndirect(
        IMAGELISTDRAWPARAMS* pimldp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pimldp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Duplicate(jitter):
    """
    HIMAGELIST ImageList_Duplicate(
        HIMAGELIST himl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_EndDrag(jitter):
    """
    VOID ImageList_EndDrag()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_GetBkColor(jitter):
    """
    COLORREF ImageList_GetBkColor(
        HIMAGELIST himl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_GetDragImage(jitter):
    """
    HIMAGELIST ImageList_GetDragImage(
        POINT* ppt,
        POINT* pptHotspot
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppt", "pptHotspot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_GetIcon(jitter):
    """
    HICON ImageList_GetIcon(
        HIMAGELIST himl,
        int i,
        [ILD_Flags] flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "i", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_GetIconSize(jitter):
    """
    BOOL ImageList_GetIconSize(
        HIMAGELIST himl,
        int* cx,
        int* cy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "cx", "cy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_GetImageCount(jitter):
    """
    int ImageList_GetImageCount(
        HIMAGELIST himl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_GetImageInfo(jitter):
    """
    BOOL ImageList_GetImageInfo(
        HIMAGELIST himl,
        int i,
        IMAGEINFO* pImageInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "i", "pImageInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_LoadImage(jitter, get_str, set_str):
    """
    HIMAGELIST ImageList_LoadImage(
        HINSTANCE hi,
        LPCTSTR lpbmp,
        int cx,
        int cGrow,
        COLORREF crMask,
        [ImageType] uType,
        [LRFlags] uFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hi", "lpbmp", "cx", "cGrow", "crMask", "uType", "uFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_LoadImageA(jitter):
    comctl32_ImageList_LoadImage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def comctl32_ImageList_LoadImageW(jitter):
    comctl32_ImageList_LoadImage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def comctl32_ImageList_Merge(jitter):
    """
    HIMAGELIST ImageList_Merge(
        HIMAGELIST himl1,
        int i1,
        HIMAGELIST himl2,
        int i2,
        int dx,
        int dy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl1", "i1", "himl2", "i2", "dx", "dy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Read(jitter):
    """
    HIMAGELIST ImageList_Read(
        LPSTREAM pstm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_ReadEx(jitter):
    """
    HRESULT ImageList_ReadEx(
        [ILP_Flags] dwFlags,
        LPSTREAM pstm,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags", "pstm", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Remove(jitter):
    """
    BOOL ImageList_Remove(
        HIMAGELIST himl,
        int i
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "i"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Replace(jitter):
    """
    BOOL ImageList_Replace(
        HIMAGELIST himl,
        int i,
        HBITMAP hbmImage,
        HBITMAP hbmMask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "i", "hbmImage", "hbmMask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_ReplaceIcon(jitter):
    """
    int ImageList_ReplaceIcon(
        HIMAGELIST himl,
        int i,
        HICON hicon
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "i", "hicon"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_SetBkColor(jitter):
    """
    COLORREF ImageList_SetBkColor(
        HIMAGELIST himl,
        COLORREF clrBk
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "clrBk"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_SetColorTable(jitter):
    """
    int ImageList_SetColorTable(
        HIMAGELIST himl,
        int start,
        int len,
        RGBQUAD* prgb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "start", "len", "prgb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_SetDragCursorImage(jitter):
    """
    BOOL ImageList_SetDragCursorImage(
        HIMAGELIST himlDrag,
        int iDrag,
        int dxHotspot,
        int dyHotspot
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himlDrag", "iDrag", "dxHotspot", "dyHotspot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_SetIconSize(jitter):
    """
    BOOL ImageList_SetIconSize(
        HIMAGELIST himl,
        int cx,
        int cy
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "cx", "cy"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_SetImageCount(jitter):
    """
    BOOL ImageList_SetImageCount(
        HIMAGELIST himl,
        UINT uNewCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "uNewCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_SetOverlayImage(jitter):
    """
    BOOL ImageList_SetOverlayImage(
        HIMAGELIST himl,
        int iImage,
        int iOverlay
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "iImage", "iOverlay"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_Write(jitter):
    """
    BOOL ImageList_Write(
        HIMAGELIST himl,
        LPSTREAM pstm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "pstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_ImageList_WriteEx(jitter):
    """
    HRESULT ImageList_WriteEx(
        HIMAGELIST himl,
        [ILP_Flags] dwFlags,
        LPSTREAM pstm
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["himl", "dwFlags", "pstm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_TaskDialog(jitter):
    """
    HRESULT TaskDialog(
        HWND hWndParent,
        HINSTANCE hInstance,
        PCWSTR pszWindowTitle,
        PCWSTR pszMainInstruction,
        PCWSTR pszContent,
        TASKDIALOG_COMMON_BUTTON_FLAGS dwCommonButtons,
        PCWSTR pszIcon,
        int* pnButton
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWndParent", "hInstance", "pszWindowTitle", "pszMainInstruction", "pszContent", "dwCommonButtons", "pszIcon", "pnButton"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def comctl32_TaskDialogIndirect(jitter):
    """
    HRESULT TaskDialogIndirect(
        const TASKDIALOGCONFIG* pTaskConfig,
        int* pnButton,
        int* pnRadioButton,
        BOOL* pfVerificationFlagChecked
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTaskConfig", "pnButton", "pnRadioButton", "pfVerificationFlagChecked"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
