
def mscms_CheckBitmapBits(jitter):
    """
    BOOL CheckBitmapBits(
        HTRANSFORM hColorTransform,
        PVOID pSrcBits,
        BMFORMAT bmInput,
        DWORD dwWidth,
        DWORD dwHeight,
        DWORD dwStride,
        PBYTE paResult,
        PBMCALLBACKFN pfnCallback,
        LPARAM lpCallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorTransform", "pSrcBits", "bmInput", "dwWidth", "dwHeight", "dwStride", "paResult", "pfnCallback", "lpCallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_CheckColors(jitter):
    """
    BOOL CheckColors(
        HTRANSFORM hColorTransform,
        PCOLOR paInputColors,
        DWORD nColors,
        COLORTYPE ctInput,
        PBYTE paResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorTransform", "paInputColors", "nColors", "ctInput", "paResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_ConvertColorNameToIndex(jitter):
    """
    BOOL ConvertColorNameToIndex(
        HPROFILE hProfile,
        PCOLOR_NAME paColorName,
        PDWORD paIndex,
        DWORD dwCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "paColorName", "paIndex", "dwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_ConvertIndexToColorName(jitter):
    """
    BOOL ConvertIndexToColorName(
        HPROFILE hProfile,
        PDWORD paIndex,
        PCOLOR_NAME paColorName,
        DWORD dwCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "paIndex", "paColorName", "dwCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_CreateColorTransform(jitter, get_str, set_str):
    """
    HTRANSFORM CreateColorTransform(
        LPLOGCOLORSPACE pLogColorSpace,
        HPROFILE hDestProfile,
        HPROFILE hTargetProfile,
        [CCT_FLAGS] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pLogColorSpace", "hDestProfile", "hTargetProfile", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_CreateColorTransformA(jitter):
    mscms_CreateColorTransform(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_CreateColorTransformW(jitter):
    mscms_CreateColorTransform(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_CreateMultiProfileTransform(jitter):
    """
    HTRANSFORM CreateMultiProfileTransform(
        PHPROFILE pahProfiles,
        DWORD nProfiles,
        [RENDERING_INTENT*] padwIntent,
        DWORD nIntents,
        [CCT_FLAGS] dwFlags,
        DWORD indexPreferredCMM
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pahProfiles", "nProfiles", "padwIntent", "nIntents", "dwFlags", "indexPreferredCMM"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_DeleteColorTransform(jitter):
    """
    BOOL DeleteColorTransform(
        HTRANSFORM hColorTransform
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorTransform"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetCMMInfo(jitter):
    """
    DWORD GetCMMInfo(
        HTRANSFORM hColorTransform,
        [CMM_INFO] dwInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorTransform", "dwInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetNamedProfileInfo(jitter):
    """
    BOOL GetNamedProfileInfo(
        HPROFILE hProfile,
        PNAMED_PROFILE_INFO pNamedProfileInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "pNamedProfileInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_SelectCMM(jitter):
    """
    BOOL SelectCMM(
        DWORD cmmID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["cmmID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_TranslateBitmapBits(jitter):
    """
    BOOL TranslateBitmapBits(
        HTRANSFORM hColorTransform,
        PVOID pSrcBits,
        BMFORMAT bmInput,
        DWORD dwWidth,
        DWORD dwHeight,
        DWORD dwInputStride,
        PVOID pDestBits,
        BMFORMAT bmOutput,
        DWORD dwOutputStride,
        PBMCALLBACKFN pfnCallback,
        LPARAM ulCallbackData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorTransform", "pSrcBits", "bmInput", "dwWidth", "dwHeight", "dwInputStride", "pDestBits", "bmOutput", "dwOutputStride", "pfnCallback", "ulCallbackData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_TranslateColors(jitter):
    """
    BOOL TranslateColors(
        HTRANSFORM hColorTransform,
        PCOLOR paInputColors,
        DWORD nColors,
        COLORTYPE ctInput,
        PCOLOR paOutputColors,
        COLORTYPE ctOutput
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorTransform", "paInputColors", "nColors", "ctInput", "paOutputColors", "ctOutput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsCheckColors(jitter):
    """
    BOOL WcsCheckColors(
        HTRANSFORM hColorTransform,
        DWORD nColors,
        DWORD nInputChannels,
        COLORDATATYPE cdtInput,
        DWORD cbInput,
        PVOID pInputData,
        PBYTE paResult
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorTransform", "nColors", "nInputChannels", "cdtInput", "cbInput", "pInputData", "paResult"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsTranslateColors(jitter):
    """
    BOOL WcsTranslateColors(
        HTRANSFORM hColorTransform,
        DWORD nColors,
        DWORD nInputChannels,
        COLORDATATYPE cdtInput,
        DWORD cbInput,
        PVOID pInputData,
        DWORD nOutputChannels,
        COLORDATATYPE cdtOutput,
        DWORD cbOutput,
        PVOID pOutputData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hColorTransform", "nColors", "nInputChannels", "cdtInput", "cbInput", "pInputData", "nOutputChannels", "cdtOutput", "cbOutput", "pOutputData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_CloseColorProfile(jitter):
    """
    BOOL CloseColorProfile(
        HPROFILE hProfile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_CreateDeviceLinkProfile(jitter, get_str, set_str):
    """
    BOOL CreateDeviceLinkProfile(
        PHPROFILE pahProfiles,
        DWORD nProfiles,
        [RENDERING_INTENT*] padwIntent,
        DWORD nIntents,
        [CCT_FLAGS] dwFlags,
        PBYTE pProfileData,
        DWORD indexPreferredCMM
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pahProfiles", "nProfiles", "padwIntent", "nIntents", "dwFlags", "pProfileData", "indexPreferredCMM"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_CreateDeviceLinkProfileA(jitter):
    mscms_CreateDeviceLinkProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_CreateDeviceLinkProfileW(jitter):
    mscms_CreateDeviceLinkProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_GetColorProfileElement(jitter):
    """
    BOOL GetColorProfileElement(
        HPROFILE hProfile,
        TAGTYPE tag,
        DWORD dwOffset,
        PDWORD pcbSize,
        PVOID pBuffer,
        PBOOL pbReference
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "tag", "dwOffset", "pcbSize", "pBuffer", "pbReference"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetColorProfileElementTag(jitter):
    """
    BOOL GetColorProfileElementTag(
        HPROFILE hProfile,
        DWORD dwIndex,
        PTAGTYPE pTag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "dwIndex", "pTag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetColorProfileFromHandle(jitter):
    """
    BOOL GetColorProfileFromHandle(
        HPROFILE hProfile,
        PBYTE pBuffer,
        PDWORD pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "pBuffer", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetColorProfileHeader(jitter):
    """
    BOOL GetColorProfileHeader(
        HPROFILE hProfile,
        PPROFILEHEADER pHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "pHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetCountColorProfileElements(jitter):
    """
    BOOL GetCountColorProfileElements(
        HPROFILE hProfile,
        PDWORD pnCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "pnCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetPS2ColorRenderingDictionary(jitter):
    """
    BOOL GetPS2ColorRenderingDictionary(
        HPROFILE hProfile,
        [RENDERING_INTENT] dwIntent,
        PBYTE pBuffer,
        PDWORD pcbSize,
        PBOOL pbBinary
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "dwIntent", "pBuffer", "pcbSize", "pbBinary"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetPS2ColorRenderingIntent(jitter):
    """
    BOOL GetPS2ColorRenderingIntent(
        HPROFILE hProfile,
        [RENDERING_INTENT] dwIntent,
        PBYTE pBuffer,
        PDWORD pcbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "dwIntent", "pBuffer", "pcbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetPS2ColorSpaceArray(jitter):
    """
    BOOL GetPS2ColorSpaceArray(
        HPROFILE hProfile,
        [RENDERING_INTENT] dwIntent,
        DWORD dwCSAType,
        PBYTE pBuffer,
        PDWORD pcbSize,
        PBOOL pbBinary
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "dwIntent", "dwCSAType", "pBuffer", "pcbSize", "pbBinary"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_IsColorProfileTagPresent(jitter):
    """
    BOOL IsColorProfileTagPresent(
        HPROFILE hProfile,
        TAGTYPE tag,
        PBOOL pbPresent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "tag", "pbPresent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_IsColorProfileValid(jitter):
    """
    BOOL IsColorProfileValid(
        HPROFILE hProfile,
        PBOOL pbValid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "pbValid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_OpenColorProfile(jitter, get_str, set_str):
    """
    HPROFILE OpenColorProfile(
        PPROFILE pProfile,
        [PROFILE_ACCESS] dwDesiredAccess,
        [FILE_SHARE_MODE] dwShareMode,
        [CreationDisposition] dwCreationMode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProfile", "dwDesiredAccess", "dwShareMode", "dwCreationMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_OpenColorProfileA(jitter):
    mscms_OpenColorProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_OpenColorProfileW(jitter):
    mscms_OpenColorProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_SetColorProfileElement(jitter):
    """
    BOOL SetColorProfileElement(
        HPROFILE hProfile,
        TAGTYPE tag,
        DWORD dwOffset,
        PDWORD pcbSize,
        PVOID pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "tag", "dwOffset", "pcbSize", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_SetColorProfileElementReference(jitter):
    """
    BOOL SetColorProfileElementReference(
        HPROFILE hProfile,
        TAGTYPE newTag,
        TAGTYPE refTag
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "newTag", "refTag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_SetColorProfileElementSize(jitter):
    """
    BOOL SetColorProfileElementSize(
        HPROFILE hProfile,
        TAGTYPE tag,
        DWORD cbSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "tag", "cbSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_SetColorProfileHeader(jitter):
    """
    BOOL SetColorProfileHeader(
        HPROFILE hProfile,
        PPROFILEHEADER pHeader
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hProfile", "pHeader"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsGetCalibrationManagementState(jitter):
    """
    BOOL WcsGetCalibrationManagementState(
        BOOL* pbIsEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbIsEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsSetCalibrationManagementState(jitter):
    """
    BOOL WcsSetCalibrationManagementState(
        BOOL bIsEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["bIsEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_AssociateColorProfileWithDevice(jitter, get_str, set_str):
    """
    BOOL AssociateColorProfileWithDevice(
        PCTSTR pMachineName,
        PCTSTR pProfileName,
        PCTSTR pDeviceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pProfileName", "pDeviceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_AssociateColorProfileWithDeviceA(jitter):
    mscms_AssociateColorProfileWithDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_AssociateColorProfileWithDeviceW(jitter):
    mscms_AssociateColorProfileWithDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_CreateProfileFromLogColorSpace(jitter, get_str, set_str):
    """
    BOOL CreateProfileFromLogColorSpace(
        LPLOGCOLORSPACE pLogColorSpace,
        PBYTE* pBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pLogColorSpace", "pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_CreateProfileFromLogColorSpaceA(jitter):
    mscms_CreateProfileFromLogColorSpace(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_CreateProfileFromLogColorSpaceW(jitter):
    mscms_CreateProfileFromLogColorSpace(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_DisassociateColorProfileFromDevice(jitter, get_str, set_str):
    """
    BOOL DisassociateColorProfileFromDevice(
        PCTSTR pMachineName,
        PCTSTR pProfileName,
        PCTSTR pDeviceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pProfileName", "pDeviceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_DisassociateColorProfileFromDeviceA(jitter):
    mscms_DisassociateColorProfileFromDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_DisassociateColorProfileFromDeviceW(jitter):
    mscms_DisassociateColorProfileFromDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_EnumColorProfiles(jitter, get_str, set_str):
    """
    BOOL EnumColorProfiles(
        PCTSTR pMachineName,
        PENUMTYPE pEnumRecord,
        PBYTE pBuffer,
        PDWORD pdwSize,
        PDWORD pnProfiles
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pEnumRecord", "pBuffer", "pdwSize", "pnProfiles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_EnumColorProfilesA(jitter):
    mscms_EnumColorProfiles(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_EnumColorProfilesW(jitter):
    mscms_EnumColorProfiles(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_GetColorDirectory(jitter, get_str, set_str):
    """
    BOOL GetColorDirectory(
        PCTSTR pMachineName,
        PTSTR pBuffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pBuffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetColorDirectoryA(jitter):
    mscms_GetColorDirectory(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_GetColorDirectoryW(jitter):
    mscms_GetColorDirectory(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_GetStandardColorSpaceProfile(jitter, get_str, set_str):
    """
    BOOL GetStandardColorSpaceProfile(
        PCTSTR pMachineName,
        [LCSCSTYPE_DWORD] dwProfileID,
        PTSTR pProfileName,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "dwProfileID", "pProfileName", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_GetStandardColorSpaceProfileA(jitter):
    mscms_GetStandardColorSpaceProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_GetStandardColorSpaceProfileW(jitter):
    mscms_GetStandardColorSpaceProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_InstallColorProfile(jitter, get_str, set_str):
    """
    BOOL InstallColorProfile(
        PCTSTR pMachineName,
        PCTSTR pProfileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pProfileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_InstallColorProfileA(jitter):
    mscms_InstallColorProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_InstallColorProfileW(jitter):
    mscms_InstallColorProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_RegisterCMM(jitter, get_str, set_str):
    """
    BOOL RegisterCMM(
        PCTSTR pMachineName,
        DWORD cmmID,
        PCTSTR pCMMdll
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "cmmID", "pCMMdll"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_RegisterCMMA(jitter):
    mscms_RegisterCMM(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_RegisterCMMW(jitter):
    mscms_RegisterCMM(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_SetStandardColorSpaceProfile(jitter, get_str, set_str):
    """
    BOOL SetStandardColorSpaceProfile(
        PCTSTR pMachineName,
        [LCSCSTYPE_DWORD] dwProfileID,
        PCSTR pProfilename
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "dwProfileID", "pProfilename"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_SetStandardColorSpaceProfileA(jitter):
    mscms_SetStandardColorSpaceProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_SetStandardColorSpaceProfileW(jitter):
    mscms_SetStandardColorSpaceProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_UninstallColorProfile(jitter, get_str, set_str):
    """
    BOOL UninstallColorProfile(
        PCTSTR pMachineName,
        PCTSTR pProfileName,
        BOOL bDelete
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "pProfileName", "bDelete"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_UninstallColorProfileA(jitter):
    mscms_UninstallColorProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_UninstallColorProfileW(jitter):
    mscms_UninstallColorProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_UnregisterCMM(jitter, get_str, set_str):
    """
    BOOL UnregisterCMM(
        PCTSTR pMachineName,
        DWORD cmmID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMachineName", "cmmID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_UnregisterCMMA(jitter):
    mscms_UnregisterCMM(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_UnregisterCMMW(jitter):
    mscms_UnregisterCMM(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_WcsAssociateColorProfileWithDevice(jitter, get_str, set_str):
    """
    BOOL WcsAssociateColorProfileWithDevice(
        WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
        PCWSTR pProfileName,
        PCWSTR pDeviceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["profileManagementScope", "pProfileName", "pDeviceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsAssociateColorProfileWithDeviceA(jitter):
    mscms_WcsAssociateColorProfileWithDevice(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_WcsAssociateColorProfileWithDeviceW(jitter):
    mscms_WcsAssociateColorProfileWithDevice(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_WcsCreateIccProfile(jitter):
    """
    HPROFILE WcsCreateIccProfile(
        HPROFILE hWcsProfile,
        DWORD dwOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hWcsProfile", "dwOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsDisassociateColorProfileFromDevice(jitter):
    """
    BOOL WcsDisassociateColorProfileFromDevice(
        WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
        PCWSTR pProfileName,
        PCWSTR pDeviceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["profileManagementScope", "pProfileName", "pDeviceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsEnumColorProfiles(jitter):
    """
    BOOL WcsEnumColorProfiles(
        WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
        PENUMTYPEW pEnumRecord,
        PBYTE pBuffer,
        DWORD dwSize,
        PDWORD pnProfiles
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["profileManagementScope", "pEnumRecord", "pBuffer", "dwSize", "pnProfiles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsEnumColorProfilesSize(jitter):
    """
    BOOL WcsEnumColorProfilesSize(
        WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
        PENUMTYPEW pEnumRecord,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["profileManagementScope", "pEnumRecord", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsGetDefaultColorProfile(jitter):
    """
    BOOL WcsGetDefaultColorProfile(
        WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
        PCWSTR pDeviceName,
        COLORPROFILETYPE cptColorProfileType,
        COLORPROFILESUBTYPE cpstColorProfileSubType,
        [LCSCSTYPE_DWORD] dwProfileID,
        DWORD cbProfileName,
        LPWSTR pProfileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["profileManagementScope", "pDeviceName", "cptColorProfileType", "cpstColorProfileSubType", "dwProfileID", "cbProfileName", "pProfileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsGetDefaultColorProfileSize(jitter):
    """
    BOOL WcsGetDefaultColorProfileSize(
        WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
        PCWSTR pDeviceName,
        COLORPROFILETYPE cptColorProfileType,
        COLORPROFILESUBTYPE cpstColorProfileSubType,
        [LCSCSTYPE_DWORD] dwProfileID,
        PDWORD pcbProfileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["profileManagementScope", "pDeviceName", "cptColorProfileType", "cpstColorProfileSubType", "dwProfileID", "pcbProfileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsGetDefaultRenderingIntent(jitter):
    """
    BOOL WcsGetDefaultRenderingIntent(
        WCS_PROFILE_MANAGEMENT_SCOPE scope,
        [RENDERING_INTENT*] pdwRenderingIntent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["scope", "pdwRenderingIntent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsGetUsePerUserProfiles(jitter):
    """
    BOOL WcsGetUsePerUserProfiles(
        LPCWSTR pDeviceName,
        [DEVICE_CLASS] dwDeviceClass,
        BOOL* pUsePerUserProfiles
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceName", "dwDeviceClass", "pUsePerUserProfiles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsOpenColorProfile(jitter, get_str, set_str):
    """
    HPROFILE WcsOpenColorProfile(
        PPROFILE pCDMPProfile,
        PPROFILE pCAMPProfile,
        PPROFILE pGMMPProfile,
        [PROFILE_ACCESS] dwDesiredAccess,
        [FILE_SHARE_MODE] dwShareMode,
        [CreationDisposition] dwCreationMode,
        [WCS_OPEN_PROFILE_FLAG] dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCDMPProfile", "pCAMPProfile", "pGMMPProfile", "dwDesiredAccess", "dwShareMode", "dwCreationMode", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsOpenColorProfileA(jitter):
    mscms_WcsOpenColorProfile(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def mscms_WcsOpenColorProfileW(jitter):
    mscms_WcsOpenColorProfile(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def mscms_WcsSetDefaultColorProfile(jitter):
    """
    BOOL WcsSetDefaultColorProfile(
        WCS_PROFILE_MANAGEMENT_SCOPE profileManagementScope,
        PCWSTR pDeviceName,
        COLORPROFILETYPE cptColorProfileType,
        COLORPROFILESUBTYPE cpstColorProfileSubType,
        [LCSCSTYPE_DWORD] dwProfileID,
        LPCWSTR pProfileName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["profileManagementScope", "pDeviceName", "cptColorProfileType", "cpstColorProfileSubType", "dwProfileID", "pProfileName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsSetDefaultRenderingIntent(jitter):
    """
    BOOL WcsSetDefaultRenderingIntent(
        WCS_PROFILE_MANAGEMENT_SCOPE scope,
        [RENDERING_INTENT] dwRenderingIntent
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["scope", "dwRenderingIntent"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mscms_WcsSetUsePerUserProfiles(jitter):
    """
    BOOL WcsSetUsePerUserProfiles(
        LPCWSTR pDeviceName,
        [DEVICE_CLASS] dwDeviceClass,
        BOOL usePerUserProfiles
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceName", "dwDeviceClass", "usePerUserProfiles"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
