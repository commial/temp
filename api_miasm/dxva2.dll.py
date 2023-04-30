
def dxva2_DegaussMonitor(jitter):
    """
    [dxva2.dll] BOOL DegaussMonitor(HANDLE hMonitor)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorBrightness(jitter):
    """
    [dxva2.dll] BOOL GetMonitorBrightness(HANDLE hMonitor, LPDWORD pdwMinimumBrightness, LPDWORD pdwCurrentBrightness, LPDWORD pdwMaximumBrightness)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwMinimumBrightness", "pdwCurrentBrightness", "pdwMaximumBrightness"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorCapabilities(jitter):
    """
    [dxva2.dll] BOOL GetMonitorCapabilities(HANDLE hMonitor, LPDWORD pdwMonitorCapabilities, LPDWORD pdwSupportedColorTemperatures)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwMonitorCapabilities", "pdwSupportedColorTemperatures"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorColorTemperature(jitter):
    """
    [dxva2.dll] BOOL GetMonitorColorTemperature(HANDLE hMonitor, LPMC_COLOR_TEMPERATURE pctCurrentColorTemperature)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pctCurrentColorTemperature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorContrast(jitter):
    """
    [dxva2.dll] BOOL GetMonitorContrast(HANDLE hMonitor, LPDWORD pdwMinimumContrast, LPDWORD pdwCurrentContrast, LPDWORD pdwMaximumContrast)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwMinimumContrast", "pdwCurrentContrast", "pdwMaximumContrast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorDisplayAreaPosition(jitter):
    """
    [dxva2.dll] BOOL GetMonitorDisplayAreaPosition(HANDLE hMonitor, MC_POSITION_TYPE ptPositionType, LPDWORD pdwMinimumPosition, LPDWORD pdwCurrentPosition, LPDWORD pdwMaximumPosition)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "ptPositionType", "pdwMinimumPosition", "pdwCurrentPosition", "pdwMaximumPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorDisplayAreaSize(jitter):
    """
    [dxva2.dll] BOOL GetMonitorDisplayAreaSize(HANDLE hMonitor, MC_SIZE_TYPE stSizeType, LPDWORD pdwMinimumWidthOrHeight, LPDWORD pdwCurrentWidthOrHeight, LPDWORD pdwMaximumWidthOrHeight)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "stSizeType", "pdwMinimumWidthOrHeight", "pdwCurrentWidthOrHeight", "pdwMaximumWidthOrHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorRedGreenOrBlueDrive(jitter):
    """
    [dxva2.dll] BOOL GetMonitorRedGreenOrBlueDrive(HANDLE hMonitor, MC_DRIVE_TYPE dtDriveType, LPDWORD pdwMinimumDrive, LPDWORD pdwCurrentDrive, LPDWORD pdwMaximumDrive)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dtDriveType", "pdwMinimumDrive", "pdwCurrentDrive", "pdwMaximumDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorRedGreenOrBlueGain(jitter):
    """
    [dxva2.dll] BOOL GetMonitorRedGreenOrBlueGain(HANDLE hMonitor, MC_GAIN_TYPE gtGainType, LPDWORD pdwMinimumGain, LPDWORD pdwCurrentGain, LPDWORD pdwMaximumGain)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "gtGainType", "pdwMinimumGain", "pdwCurrentGain", "pdwMaximumGain"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorTechnologyType(jitter):
    """
    [dxva2.dll] BOOL GetMonitorTechnologyType(HANDLE hMonitor, LPMC_DISPLAY_TECHNOLOGY_TYPE pdtyDisplayTechnologyType)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdtyDisplayTechnologyType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_RestoreMonitorFactoryColorDefaults(jitter):
    """
    [dxva2.dll] BOOL RestoreMonitorFactoryColorDefaults(HANDLE hMonitor)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_RestoreMonitorFactoryDefaults(jitter):
    """
    [dxva2.dll] BOOL RestoreMonitorFactoryDefaults(HANDLE hMonitor)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SaveCurrentMonitorSettings(jitter):
    """
    [dxva2.dll] BOOL SaveCurrentMonitorSettings(HANDLE hMonitor)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorBrightness(jitter):
    """
    [dxva2.dll] BOOL SetMonitorBrightness(HANDLE hMonitor, DWORD dwNewBrightness)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dwNewBrightness"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorColorTemperature(jitter):
    """
    [dxva2.dll] BOOL SetMonitorColorTemperature(HANDLE hMonitor, MC_COLOR_TEMPERATURE ctCurrentColorTemperature)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "ctCurrentColorTemperature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorContrast(jitter):
    """
    [dxva2.dll] BOOL SetMonitorContrast(HANDLE hMonitor, DWORD dwNewContrast)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dwNewContrast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorDisplayAreaPosition(jitter):
    """
    [dxva2.dll] BOOL SetMonitorDisplayAreaPosition(HANDLE hMonitor, MC_POSITION_TYPE ptPositionType, DWORD dwNewPosition)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "ptPositionType", "dwNewPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorDisplayAreaSize(jitter):
    """
    [dxva2.dll] BOOL SetMonitorDisplayAreaSize(HANDLE hMonitor, MC_SIZE_TYPE stSizeType, DWORD dwNewDisplayAreaWidthOrHeight)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "stSizeType", "dwNewDisplayAreaWidthOrHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorRedGreenOrBlueDrive(jitter):
    """
    [dxva2.dll] BOOL SetMonitorRedGreenOrBlueDrive(HANDLE hMonitor, MC_DRIVE_TYPE dtDriveType, DWORD dwNewDrive)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dtDriveType", "dwNewDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorRedGreenOrBlueGain(jitter):
    """
    [dxva2.dll] BOOL SetMonitorRedGreenOrBlueGain(HANDLE hMonitor, MC_GAIN_TYPE gtGainType, DWORD dwNewGain)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "gtGainType", "dwNewGain"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_CapabilitiesRequestAndCapabilitiesReply(jitter):
    """
    [dxva2.dll] BOOL CapabilitiesRequestAndCapabilitiesReply(HANDLE hMonitor, LPSTR pszASCIICapabilitiesString, DWORD dwCapabilitiesStringLengthInCharacters)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pszASCIICapabilitiesString", "dwCapabilitiesStringLengthInCharacters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetCapabilitiesStringLength(jitter):
    """
    [dxva2.dll] BOOL GetCapabilitiesStringLength(HANDLE hMonitor, LPDWORD pdwCapabilitiesStringLengthInCharacters)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwCapabilitiesStringLengthInCharacters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetTimingReport(jitter):
    """
    [dxva2.dll] BOOL GetTimingReport(HANDLE hMonitor, LPMC_TIMING_REPORT pmtrMonitorTimingReport)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pmtrMonitorTimingReport"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetVCPFeatureAndVCPFeatureReply(jitter):
    """
    [dxva2.dll] BOOL GetVCPFeatureAndVCPFeatureReply(HANDLE hMonitor, BYTE bVCPCode, LPMC_VCP_CODE_TYPE pvct, LPDWORD pdwCurrentValue, LPDWORD pdwMaximumValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "bVCPCode", "pvct", "pdwCurrentValue", "pdwMaximumValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SaveCurrentSettings(jitter):
    """
    [dxva2.dll] BOOL SaveCurrentSettings(HANDLE hMonitor)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetVCPFeature(jitter):
    """
    [dxva2.dll] BOOL SetVCPFeature(HANDLE hMonitor, BYTE bVCPCode, DWORD dwNewValue)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "bVCPCode", "dwNewValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DestroyPhysicalMonitor(jitter):
    """
    [dxva2.dll] BOOL DestroyPhysicalMonitor(HANDLE hMonitor)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DestroyPhysicalMonitors(jitter):
    """
    [dxva2.dll] BOOL DestroyPhysicalMonitors(DWORD dwPhysicalMonitorArraySize, LPPHYSICAL_MONITOR pPhysicalMonitorArray)
    """
    ret_ad, args = jitter.func_args_stdcall(["dwPhysicalMonitorArraySize", "pPhysicalMonitorArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetNumberOfPhysicalMonitorsFromHMONITOR(jitter):
    """
    [dxva2.dll] BOOL GetNumberOfPhysicalMonitorsFromHMONITOR(HMONITOR hMonitor, LPDWORD pdwNumberOfPhysicalMonitors)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwNumberOfPhysicalMonitors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetNumberOfPhysicalMonitorsFromIDirect3DDevice9(jitter):
    """
    [dxva2.dll] BOOL GetNumberOfPhysicalMonitorsFromIDirect3DDevice9(IDirect3DDevice9* pDirect3DDevice9, LPDWORD pdwNumberOfPhysicalMonitors)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDirect3DDevice9", "pdwNumberOfPhysicalMonitors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetPhysicalMonitorsFromHMONITOR(jitter):
    """
    [dxva2.dll] BOOL GetPhysicalMonitorsFromHMONITOR(HMONITOR hMonitor, DWORD dwPhysicalMonitorArraySize, LPPHYSICAL_MONITOR pPhysicalMonitorArray)
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dwPhysicalMonitorArraySize", "pPhysicalMonitorArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetPhysicalMonitorsFromIDirect3DDevice9(jitter):
    """
    [dxva2.dll] BOOL GetPhysicalMonitorsFromIDirect3DDevice9(IDirect3DDevice9* pDirect3DDevice9, DWORD dwPhysicalMonitorArraySize, LPPHYSICAL_MONITOR pPhysicalMonitorArray)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDirect3DDevice9", "dwPhysicalMonitorArraySize", "pPhysicalMonitorArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DXVA2CreateDirect3DDeviceManager9(jitter):
    """
    [dxva2.dll] HRESULT DXVA2CreateDirect3DDeviceManager9(UINT* pResetToken, IDirect3DDeviceManager9** ppDXVAManager)
    """
    ret_ad, args = jitter.func_args_stdcall(["pResetToken", "ppDXVAManager"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DXVA2CreateVideoService(jitter):
    """
    [dxva2.dll] HRESULT DXVA2CreateVideoService(IDirect3DDevice9* pDD, REFIID riid, void** ppService)
    """
    ret_ad, args = jitter.func_args_stdcall(["pDD", "riid", "ppService"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DXVAHD_CreateDevice(jitter):
    """
    [dxva2.dll] HRESULT DXVAHD_CreateDevice(IDirect3DDevice9Ex* pD3DDevice, const DXVAHD_CONTENT_DESC* pContentDesc, DXVAHD_DEVICE_USAGE Usage, PDXVAHDSW_Plugin pPlugin, IDXVAHD_Device** ppDevice)
    """
    ret_ad, args = jitter.func_args_stdcall(["pD3DDevice", "pContentDesc", "Usage", "pPlugin", "ppDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
