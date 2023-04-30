###### Enums ######
COLORTYPE = {
    "COLOR_GRAY": 1,
    "COLOR_RGB": 2,
    "COLOR_XYZ": 3,
    "COLOR_Yxy": 4,
    "COLOR_Lab": 5,
    "COLOR_3_CHANNEL": 6,
    "COLOR_CMYK": 7,
    "COLOR_5_CHANNEL": 8,
    "COLOR_6_CHANNEL": 9,
    "COLOR_7_CHANNEL": 10,
    "COLOR_8_CHANNEL": 11,
    "COLOR_NAMED": 12,
}
COLORTYPE_INV = {
    1: "COLOR_GRAY",
    2: "COLOR_RGB",
    3: "COLOR_XYZ",
    4: "COLOR_Yxy",
    5: "COLOR_Lab",
    6: "COLOR_3_CHANNEL",
    7: "COLOR_CMYK",
    8: "COLOR_5_CHANNEL",
    9: "COLOR_6_CHANNEL",
    10: "COLOR_7_CHANNEL",
    11: "COLOR_8_CHANNEL",
    12: "COLOR_NAMED",
}
_CMS_DIRECTION_ = {
    "CMS_FORWARD": 0,
    "CMS_BACKWARD": 1,
}
_CMS_DIRECTION__INV = {
    0: "CMS_FORWARD",
    1: "CMS_BACKWARD",
}

###################

###### Types ######
HCMTRANSFORM = HANDLE
LPDEVCHARACTER = PVOID
COLORTYPE = UINT

class RGBTRIPLE(MemStruct):
    fields = [
        ("rgbtBlue", BYTE()),
        ("rgbtGreen", BYTE()),
        ("rgbtRed", BYTE()),
    ]

RGBTRIPLE_PTR = Ptr("<I", RGBTRIPLE())
_CMS_DIRECTION_ = DWORD

###################

###### Functions ######

def icm32_CMCheckColors(jitter):
    """
    BOOL CMCheckColors(
        HCMTRANSFORM hcmTransform,
        LPCOLOR lpaInputColors,
        DWORD nColors,
        COLORTYPE ctInput,
        LPBYTE lpaResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcmTransform", "lpaInputColors", "nColors", "ctInput", "lpaResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMCheckColorsInGamut(jitter):
    """
    BOOL CMCheckColorsInGamut(
        HCMTRANSFORM hcmTransform,
        RGBTRIPLE* lpaRGBTriple,
        LPBYTE lpaResult,
        UINT nCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcmTransform", "lpaRGBTriple", "lpaResult", "nCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMCheckRGBs(jitter):
    """
    BOOL CMCheckRGBs(
        HCMTRANSFORM hcmTransform,
        LPVOID lpSrcBits,
        BMFORMAT bmInput,
        DWORD dwWidth,
        DWORD dwHeight,
        DWORD dwStride,
        LPBYTE lpaResult,
        PBMCALLBACKFN pfnCallback,
        ULONG ulCallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcmTransform", "lpSrcBits", "bmInput", "dwWidth", "dwHeight", "dwStride", "lpaResult", "pfnCallback", "ulCallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMConvertColorNameToIndex(jitter):
    """
    BOOL CMConvertColorNameToIndex(
        HPROFILE hProfile,
        PCOLOR_NAME paColorName,
        PDWORD paIndex,
        DWORD dwCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "paColorName", "paIndex", "dwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMConvertIndexToColorName(jitter):
    """
    BOOL CMConvertIndexToColorName(
        HPROFILE hProfile,
        PDWORD paIndex,
        PCOLOR_NAME paColorName,
        DWORD dwCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "paIndex", "paColorName", "dwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMCreateDeviceLinkProfile(jitter):
    """
    BOOL CMCreateDeviceLinkProfile(
        PHPROFILE lpahProfiles,
        DWORD nProfiles,
        [RENDERING_INTENT*] padwIntents,
        DWORD nIntents,
        [CCT_FLAGS] dwFlags,
        LPBYTE* lpProfileData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpahProfiles", "nProfiles", "padwIntents", "nIntents", "dwFlags", "lpProfileData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMCreateMultiProfileTransform(jitter):
    """
    HCMTRANSFORM CMCreateMultiProfileTransform(
        PHPROFILE lpahProfiles,
        DWORD nProfiles,
        [RENDERING_INTENT*] padwIntents,
        DWORD nIntents,
        [CCT_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpahProfiles", "nProfiles", "padwIntents", "nIntents", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMCreateProfile(jitter, get_str, set_str):
    """
    BOOL CMCreateProfile(
        LPLOGCOLORSPACE lpColorSpace,
        LPBYTE* lpProfileData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpColorSpace", "lpProfileData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMCreateProfileA(jitter):
    icm32_CMCreateProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def icm32_CMCreateProfileW(jitter):
    icm32_CMCreateProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def icm32_CMCreateTransformExt(jitter, get_str, set_str):
    """
    HCMTRANSFORM CMCreateTransformExt(
        LPLOGCOLORSPACE lpColorSpace,
        LPDEVCHARACTER lpDevCharacter,
        LPDEVCHARACTER lpTargetDevCharacter,
        [CCT_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpColorSpace", "lpDevCharacter", "lpTargetDevCharacter", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMCreateTransformExtA(jitter):
    icm32_CMCreateTransformExt(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def icm32_CMCreateTransformExtW(jitter):
    icm32_CMCreateTransformExt(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def icm32_CMDeleteTransform(jitter):
    """
    BOOL CMDeleteTransform(
        HCMTRANSFORM hcmTransform
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcmTransform"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMGetInfo(jitter):
    """
    DWORD CMGetInfo(
        [CMM_INFO] dwInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMGetNamedProfileInfo(jitter):
    """
    BOOL CMGetNamedProfileInfo(
        HPROFILE hProfile,
        PNAMED_PROFILE_INFO pNamedProfileInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "pNamedProfileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMGetPS2ColorRenderingDictionary(jitter):
    """
    BOOL CMGetPS2ColorRenderingDictionary(
        HPROFILE hProfile,
        [RENDERING_INTENT] dwIntent,
        LPBYTE lpBuffer,
        LPDWORD lpcbSize,
        LPBOOL lpbBinary
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "dwIntent", "lpBuffer", "lpcbSize", "lpbBinary"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMGetPS2ColorRenderingIntent(jitter):
    """
    BOOL CMGetPS2ColorRenderingIntent(
        HPROFILE hProfile,
        [RENDERING_INTENT] dwIntent,
        LPBYTE lpBuffer,
        LPDWORD lpcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "dwIntent", "lpBuffer", "lpcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMGetPS2ColorSpaceArray(jitter):
    """
    BOOL CMGetPS2ColorSpaceArray(
        HPROFILE hProfile,
        [RENDERING_INTENT] dwIntent,
        DWORD dwCSAType,
        LPBYTE lpBuffer,
        LPDWORD lpcbSize,
        LPBOOL lpbBinary
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "dwIntent", "dwCSAType", "lpBuffer", "lpcbSize", "lpbBinary"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMIsProfileValid(jitter):
    """
    BOOL CMIsProfileValid(
        HPROFILE hProfile,
        LPBOOL lpbValid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "lpbValid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMTranslateColors(jitter):
    """
    BOOL CMTranslateColors(
        HCMTRANSFORM hcmTransform,
        LPCOLOR lpaInputColors,
        DWORD nColors,
        COLORTYPE ctInput,
        LPCOLOR lpaOutputColors,
        COLORTYPE ctOutput
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcmTransform", "lpaInputColors", "nColors", "ctInput", "lpaOutputColors", "ctOutput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMTranslateRGB(jitter):
    """
    BOOL CMTranslateRGB(
        HCMTRANSFORM hcmTransform,
        COLORREF ColorRef,
        LPCOLORREF lpColorRef,
        [CMS_DIRECTION] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcmTransform", "ColorRef", "lpColorRef", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMTranslateRGBs(jitter):
    """
    BOOL CMTranslateRGBs(
        HCMTRANSFORM hcmTransform,
        LPVOID lpSrcBits,
        BMFORMAT bmInput,
        DWORD dwWidth,
        DWORD dwHeight,
        DWORD dwStride,
        LPVOID lpDestBits,
        BMFORMAT bmOutput,
        [CMS_DIRECTION] dwTranslateDirection
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcmTransform", "lpSrcBits", "bmInput", "dwWidth", "dwHeight", "dwStride", "lpDestBits", "bmOutput", "dwTranslateDirection"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def icm32_CMTranslateRGBsExt(jitter):
    """
    BOOL CMTranslateRGBsExt(
        HCMTRANSFORM hcmTransform,
        LPVOID lpSrcBits,
        BMFORMAT bmInput,
        DWORD dwWidth,
        DWORD dwHeight,
        DWORD dwInputStride,
        LPVOID lpDestBits,
        BMFORMAT bmOutput,
        DWORD dwOutputStride,
        LPBMCALLBACKFN lpfnCallback,
        ULONG ulCallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hcmTransform", "lpSrcBits", "bmInput", "dwWidth", "dwHeight", "dwInputStride", "lpDestBits", "bmOutput", "dwOutputStride", "lpfnCallback", "ulCallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
