
def dwmapi_DwmAttachMilContent(jitter):
    """
    HRESULT DwmAttachMilContent(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmDefWindowProc(jitter):
    """
    BOOL DwmDefWindowProc(
        HWND hwnd,
        [WinMsg] msg,
        WPARAM wParam,
        LPARAM lParam,
        LRESULT* plResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "msg", "wParam", "lParam", "plResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmDetachMilContent(jitter):
    """
    HRESULT DwmDetachMilContent(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmEnableBlurBehindWindow(jitter):
    """
    HRESULT DwmEnableBlurBehindWindow(
        HWND hWnd,
        const DWM_BLURBEHIND* pBlurBehind
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pBlurBehind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmEnableComposition(jitter):
    """
    HRESULT DwmEnableComposition(
        UINT uCompositionAction
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uCompositionAction"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmEnableMMCSS(jitter):
    """
    HRESULT DwmEnableMMCSS(
        BOOL fEnableMMCSS
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["fEnableMMCSS"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmExtendFrameIntoClientArea(jitter):
    """
    HRESULT DwmExtendFrameIntoClientArea(
        HWND hWnd,
        const MARGINS* pMarInset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pMarInset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmFlush(jitter):
    """
    HRESULT DwmFlush()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmGetColorizationColor(jitter):
    """
    HRESULT DwmGetColorizationColor(
        DWORD* pcrColorization,
        BOOL* pfOpaqueBlend
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pcrColorization", "pfOpaqueBlend"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmGetCompositionTimingInfo(jitter):
    """
    HRESULT DwmGetCompositionTimingInfo(
        HWND hwnd,
        DWM_TIMING_INFO* pTimingInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pTimingInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmGetGraphicsStreamClient(jitter):
    """
    HRESULT DwmGetGraphicsStreamClient(
        UINT uIndex,
        UUID* pClientUuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uIndex", "pClientUuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmGetGraphicsStreamTransformHint(jitter):
    """
    HRESULT DwmGetGraphicsStreamTransformHint(
        UINT uIndex,
        MilMatrix3x2D* pTransform
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["uIndex", "pTransform"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmGetTransportAttributes(jitter):
    """
    HRESULT DwmGetTransportAttributes(
        BOOL* pfIsRemoting,
        BOOL* pfIsConnected,
        DWORD* pDwGeneration
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfIsRemoting", "pfIsConnected", "pDwGeneration"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmGetWindowAttribute(jitter):
    """
    HRESULT DwmGetWindowAttribute(
        HWND hwnd,
        [DwmWindowAttr] dwAttribute,
        PVOID pvAttribute,
        DWORD cbAttribute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwAttribute", "pvAttribute", "cbAttribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmInvalidateIconicBitmaps(jitter):
    """
    HRESULT DwmInvalidateIconicBitmaps(
        HWND hwnd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmIsCompositionEnabled(jitter):
    """
    HRESULT DwmIsCompositionEnabled(
        BOOL* pfEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pfEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmModifyPreviousDxFrameDuration(jitter):
    """
    HRESULT DwmModifyPreviousDxFrameDuration(
        HWND hwnd,
        INT cRefreshes,
        BOOL fRelative
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "cRefreshes", "fRelative"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmQueryThumbnailSourceSize(jitter):
    """
    HRESULT DwmQueryThumbnailSourceSize(
        HTHUMBNAIL hThumbnail,
        PSIZE pSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hThumbnail", "pSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmRenderGesture(jitter):
    """
    HRESULT DwmRenderGesture(
        GESTURE_TYPE gt,
        UINT cContacts,
        DWORD* pdwPointerID,
        POINT* pPoints
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["gt", "cContacts", "pdwPointerID", "pPoints"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmSetDxFrameDuration(jitter):
    """
    HRESULT DwmSetDxFrameDuration(
        HWND hwnd,
        INT cRefreshes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "cRefreshes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmSetIconicLivePreviewBitmap(jitter):
    """
    HRESULT DwmSetIconicLivePreviewBitmap(
        HWND hwnd,
        HBITMAP hbmp,
        POINT* pptClient,
        DWORD dwSITFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hbmp", "pptClient", "dwSITFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmSetIconicThumbnail(jitter):
    """
    HRESULT DwmSetIconicThumbnail(
        HWND hwnd,
        HBITMAP hbmp,
        DWORD dwSITFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "hbmp", "dwSITFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmSetPresentParameters(jitter):
    """
    HRESULT DwmSetPresentParameters(
        HWND hwnd,
        DWM_PRESENT_PARAMETERS* pPresentParams
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "pPresentParams"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmSetWindowAttribute(jitter):
    """
    HRESULT DwmSetWindowAttribute(
        HWND hwnd,
        [DwmWindowAttr] dwAttribute,
        LPCVOID pvAttribute,
        DWORD cbAttribute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "dwAttribute", "pvAttribute", "cbAttribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmShowContact(jitter):
    """
    HRESULT DwmShowContact(
        DWORD dwPointerID,
        DWM_SHOWCONTACT eShowContact
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwPointerID", "eShowContact"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmTetherContact(jitter):
    """
    HRESULT DwmTetherContact(
        DWORD dwPointerID,
        BOOL fEnable,
        POINT ptTether
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwPointerID", "fEnable", "ptTether"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmTransitionOwnedWindow(jitter):
    """
    HRESULT DwmTransitionOwnedWindow(
        HWND hwnd,
        DWMTRANSITION_OWNEDWINDOW_TARGET target
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "target"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmUnregisterThumbnail(jitter):
    """
    HRESULT DwmUnregisterThumbnail(
        HTHUMBNAIL hThumbnailId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hThumbnailId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmRegisterThumbnail(jitter):
    """
    HRESULT DwmRegisterThumbnail(
        HWND hwndDestination,
        HWND* hwndSource,
        PHTHUMBNAIL phThumbnailId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndDestination", "hwndSource", "phThumbnailId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dwmapi_DwmUpdateThumbnailProperties(jitter):
    """
    HRESULT DwmUpdateThumbnailProperties(
        HTHUMBNAIL hThumbnailId,
        const DWM_THUMBNAIL_PROPERTIES* ptnProperties
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hThumbnailId", "ptnProperties"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
