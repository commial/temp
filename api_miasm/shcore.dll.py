
def shcore_CreateRandomAccessStreamOnFile(jitter):
    """
    HRESULT CreateRandomAccessStreamOnFile(
        PCWSTR filePath,
        FileAccessMode accessMode,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["filePath", "accessMode", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shcore_CreateRandomAccessStreamOverStream(jitter):
    """
    HRESULT CreateRandomAccessStreamOverStream(
        IStream* stream,
        BSOS_OPTIONS options,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["stream", "options", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shcore_CreateStreamOverRandomAccessStream(jitter):
    """
    HRESULT CreateStreamOverRandomAccessStream(
        IUnknown* randomAccessStream,
        REFIID riid,
        void** ppv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["randomAccessStream", "riid", "ppv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shcore_GetScaleFactorForDevice(jitter):
    """
    DEVICE_SCALE_FACTOR GetScaleFactorForDevice(
        DISPLAY_DEVICE_TYPE deviceType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["deviceType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shcore_RegisterScaleChangeNotifications(jitter):
    """
    STDAPI RegisterScaleChangeNotifications(
        DISPLAY_DEVICE_TYPE displayDevice,
        HWND hwndNotify,
        UINT uMsgNotify,
        DWORD* pdwCookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["displayDevice", "hwndNotify", "uMsgNotify", "pdwCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def shcore_RevokeScaleChangeNotifications(jitter):
    """
    STDAPI RevokeScaleChangeNotifications(
        DISPLAY_DEVICE_TYPE displayDevice,
        DWORD dwCookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["displayDevice", "dwCookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
