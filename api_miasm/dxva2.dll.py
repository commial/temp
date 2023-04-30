MC_COLOR_TEMPERATURE = {
    "MC_COLOR_TEMPERATURE_UNKNOWN": 0,
    "MC_COLOR_TEMPERATURE_4000K": 1,
    "MC_COLOR_TEMPERATURE_5000K": 2,
    "MC_COLOR_TEMPERATURE_6500K": 3,
    "MC_COLOR_TEMPERATURE_7500K": 4,
    "MC_COLOR_TEMPERATURE_8200K": 5,
    "MC_COLOR_TEMPERATURE_9300K": 6,
    "MC_COLOR_TEMPERATURE_10000K": 7,
    "MC_COLOR_TEMPERATURE_11500K": 8,
}
MC_COLOR_TEMPERATURE_INV = {
    0: "MC_COLOR_TEMPERATURE_UNKNOWN",
    1: "MC_COLOR_TEMPERATURE_4000K",
    2: "MC_COLOR_TEMPERATURE_5000K",
    3: "MC_COLOR_TEMPERATURE_6500K",
    4: "MC_COLOR_TEMPERATURE_7500K",
    5: "MC_COLOR_TEMPERATURE_8200K",
    6: "MC_COLOR_TEMPERATURE_9300K",
    7: "MC_COLOR_TEMPERATURE_10000K",
    8: "MC_COLOR_TEMPERATURE_11500K",
}
MC_POSITION_TYPE = {
    "MC_HORIZONTAL_POSITION": 0,
    "MC_VERTICAL_POSITION": 1,
}
MC_POSITION_TYPE_INV = {
    0: "MC_HORIZONTAL_POSITION",
    1: "MC_VERTICAL_POSITION",
}
MC_SIZE_TYPE = {
    "MC_WIDTH": 0,
    "MC_HEIGHT": 1,
}
MC_SIZE_TYPE_INV = {
    0: "MC_WIDTH",
    1: "MC_HEIGHT",
}
MC_DRIVE_TYPE = {
    "MC_RED_DRIVE": 0,
    "MC_GREEN_DRIVE": 1,
    "MC_BLUE_DRIVE": 2,
}
MC_DRIVE_TYPE_INV = {
    0: "MC_RED_DRIVE",
    1: "MC_GREEN_DRIVE",
    2: "MC_BLUE_DRIVE",
}
MC_GAIN_TYPE = {
    "MC_RED_GAIN": 0,
    "MC_GREEN_GAIN": 1,
    "MC_BLUE_GAIN": 2,
}
MC_GAIN_TYPE_INV = {
    0: "MC_RED_GAIN",
    1: "MC_GREEN_GAIN",
    2: "MC_BLUE_GAIN",
}
MC_DISPLAY_TECHNOLOGY_TYPE = {
    "MC_SHADOW_MASK_CATHODE_RAY_TUBE": 0,
    "MC_APERTURE_GRILL_CATHODE_RAY_TUBE": 1,
    "MC_THIN_FILM_TRANSISTOR": 2,
    "MC_LIQUID_CRYSTAL_ON_SILICON": 3,
    "MC_PLASMA": 4,
    "MC_ORGANIC_LIGHT_EMITTING_DIODE": 5,
    "MC_ELECTROLUMINESCENT": 6,
    "MC_MICROELECTROMECHANICAL": 7,
    "MC_FIELD_EMISSION_DEVICE": 8,
}
MC_DISPLAY_TECHNOLOGY_TYPE_INV = {
    0: "MC_SHADOW_MASK_CATHODE_RAY_TUBE",
    1: "MC_APERTURE_GRILL_CATHODE_RAY_TUBE",
    2: "MC_THIN_FILM_TRANSISTOR",
    3: "MC_LIQUID_CRYSTAL_ON_SILICON",
    4: "MC_PLASMA",
    5: "MC_ORGANIC_LIGHT_EMITTING_DIODE",
    6: "MC_ELECTROLUMINESCENT",
    7: "MC_MICROELECTROMECHANICAL",
    8: "MC_FIELD_EMISSION_DEVICE",
}
MC_VCP_CODE_TYPE = {
    "MC_MOMENTARY": 0,
    "MC_SET_PARAMETER": 1,
}
MC_VCP_CODE_TYPE_INV = {
    0: "MC_MOMENTARY",
    1: "MC_SET_PARAMETER",
}

def dxva2_DegaussMonitor(jitter):
    """
    BOOL DegaussMonitor(
        HANDLE hMonitor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorBrightness(jitter):
    """
    BOOL GetMonitorBrightness(
        HANDLE hMonitor,
        LPDWORD pdwMinimumBrightness,
        LPDWORD pdwCurrentBrightness,
        LPDWORD pdwMaximumBrightness
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwMinimumBrightness", "pdwCurrentBrightness", "pdwMaximumBrightness"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorCapabilities(jitter):
    """
    BOOL GetMonitorCapabilities(
        HANDLE hMonitor,
        LPDWORD pdwMonitorCapabilities,
        LPDWORD pdwSupportedColorTemperatures
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwMonitorCapabilities", "pdwSupportedColorTemperatures"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorColorTemperature(jitter):
    """
    BOOL GetMonitorColorTemperature(
        HANDLE hMonitor,
        LPMC_COLOR_TEMPERATURE pctCurrentColorTemperature
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pctCurrentColorTemperature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorContrast(jitter):
    """
    BOOL GetMonitorContrast(
        HANDLE hMonitor,
        LPDWORD pdwMinimumContrast,
        LPDWORD pdwCurrentContrast,
        LPDWORD pdwMaximumContrast
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwMinimumContrast", "pdwCurrentContrast", "pdwMaximumContrast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorDisplayAreaPosition(jitter):
    """
    BOOL GetMonitorDisplayAreaPosition(
        HANDLE hMonitor,
        MC_POSITION_TYPE ptPositionType,
        LPDWORD pdwMinimumPosition,
        LPDWORD pdwCurrentPosition,
        LPDWORD pdwMaximumPosition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "ptPositionType", "pdwMinimumPosition", "pdwCurrentPosition", "pdwMaximumPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorDisplayAreaSize(jitter):
    """
    BOOL GetMonitorDisplayAreaSize(
        HANDLE hMonitor,
        MC_SIZE_TYPE stSizeType,
        LPDWORD pdwMinimumWidthOrHeight,
        LPDWORD pdwCurrentWidthOrHeight,
        LPDWORD pdwMaximumWidthOrHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "stSizeType", "pdwMinimumWidthOrHeight", "pdwCurrentWidthOrHeight", "pdwMaximumWidthOrHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorRedGreenOrBlueDrive(jitter):
    """
    BOOL GetMonitorRedGreenOrBlueDrive(
        HANDLE hMonitor,
        MC_DRIVE_TYPE dtDriveType,
        LPDWORD pdwMinimumDrive,
        LPDWORD pdwCurrentDrive,
        LPDWORD pdwMaximumDrive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dtDriveType", "pdwMinimumDrive", "pdwCurrentDrive", "pdwMaximumDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorRedGreenOrBlueGain(jitter):
    """
    BOOL GetMonitorRedGreenOrBlueGain(
        HANDLE hMonitor,
        MC_GAIN_TYPE gtGainType,
        LPDWORD pdwMinimumGain,
        LPDWORD pdwCurrentGain,
        LPDWORD pdwMaximumGain
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "gtGainType", "pdwMinimumGain", "pdwCurrentGain", "pdwMaximumGain"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetMonitorTechnologyType(jitter):
    """
    BOOL GetMonitorTechnologyType(
        HANDLE hMonitor,
        LPMC_DISPLAY_TECHNOLOGY_TYPE pdtyDisplayTechnologyType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdtyDisplayTechnologyType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_RestoreMonitorFactoryColorDefaults(jitter):
    """
    BOOL RestoreMonitorFactoryColorDefaults(
        HANDLE hMonitor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_RestoreMonitorFactoryDefaults(jitter):
    """
    BOOL RestoreMonitorFactoryDefaults(
        HANDLE hMonitor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SaveCurrentMonitorSettings(jitter):
    """
    BOOL SaveCurrentMonitorSettings(
        HANDLE hMonitor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorBrightness(jitter):
    """
    BOOL SetMonitorBrightness(
        HANDLE hMonitor,
        DWORD dwNewBrightness
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dwNewBrightness"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorColorTemperature(jitter):
    """
    BOOL SetMonitorColorTemperature(
        HANDLE hMonitor,
        MC_COLOR_TEMPERATURE ctCurrentColorTemperature
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "ctCurrentColorTemperature"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorContrast(jitter):
    """
    BOOL SetMonitorContrast(
        HANDLE hMonitor,
        DWORD dwNewContrast
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dwNewContrast"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorDisplayAreaPosition(jitter):
    """
    BOOL SetMonitorDisplayAreaPosition(
        HANDLE hMonitor,
        MC_POSITION_TYPE ptPositionType,
        DWORD dwNewPosition
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "ptPositionType", "dwNewPosition"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorDisplayAreaSize(jitter):
    """
    BOOL SetMonitorDisplayAreaSize(
        HANDLE hMonitor,
        MC_SIZE_TYPE stSizeType,
        DWORD dwNewDisplayAreaWidthOrHeight
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "stSizeType", "dwNewDisplayAreaWidthOrHeight"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorRedGreenOrBlueDrive(jitter):
    """
    BOOL SetMonitorRedGreenOrBlueDrive(
        HANDLE hMonitor,
        MC_DRIVE_TYPE dtDriveType,
        DWORD dwNewDrive
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dtDriveType", "dwNewDrive"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetMonitorRedGreenOrBlueGain(jitter):
    """
    BOOL SetMonitorRedGreenOrBlueGain(
        HANDLE hMonitor,
        MC_GAIN_TYPE gtGainType,
        DWORD dwNewGain
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "gtGainType", "dwNewGain"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_CapabilitiesRequestAndCapabilitiesReply(jitter):
    """
    BOOL CapabilitiesRequestAndCapabilitiesReply(
        HANDLE hMonitor,
        LPSTR pszASCIICapabilitiesString,
        DWORD dwCapabilitiesStringLengthInCharacters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pszASCIICapabilitiesString", "dwCapabilitiesStringLengthInCharacters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetCapabilitiesStringLength(jitter):
    """
    BOOL GetCapabilitiesStringLength(
        HANDLE hMonitor,
        LPDWORD pdwCapabilitiesStringLengthInCharacters
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwCapabilitiesStringLengthInCharacters"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetTimingReport(jitter):
    """
    BOOL GetTimingReport(
        HANDLE hMonitor,
        LPMC_TIMING_REPORT pmtrMonitorTimingReport
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pmtrMonitorTimingReport"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetVCPFeatureAndVCPFeatureReply(jitter):
    """
    BOOL GetVCPFeatureAndVCPFeatureReply(
        HANDLE hMonitor,
        BYTE bVCPCode,
        LPMC_VCP_CODE_TYPE pvct,
        LPDWORD pdwCurrentValue,
        LPDWORD pdwMaximumValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "bVCPCode", "pvct", "pdwCurrentValue", "pdwMaximumValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SaveCurrentSettings(jitter):
    """
    BOOL SaveCurrentSettings(
        HANDLE hMonitor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_SetVCPFeature(jitter):
    """
    BOOL SetVCPFeature(
        HANDLE hMonitor,
        BYTE bVCPCode,
        DWORD dwNewValue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "bVCPCode", "dwNewValue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DestroyPhysicalMonitor(jitter):
    """
    BOOL DestroyPhysicalMonitor(
        HANDLE hMonitor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DestroyPhysicalMonitors(jitter):
    """
    BOOL DestroyPhysicalMonitors(
        DWORD dwPhysicalMonitorArraySize,
        LPPHYSICAL_MONITOR pPhysicalMonitorArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwPhysicalMonitorArraySize", "pPhysicalMonitorArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetNumberOfPhysicalMonitorsFromHMONITOR(jitter):
    """
    BOOL GetNumberOfPhysicalMonitorsFromHMONITOR(
        HMONITOR hMonitor,
        LPDWORD pdwNumberOfPhysicalMonitors
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "pdwNumberOfPhysicalMonitors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetNumberOfPhysicalMonitorsFromIDirect3DDevice9(jitter):
    """
    BOOL GetNumberOfPhysicalMonitorsFromIDirect3DDevice9(
        IDirect3DDevice9* pDirect3DDevice9,
        LPDWORD pdwNumberOfPhysicalMonitors
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDirect3DDevice9", "pdwNumberOfPhysicalMonitors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetPhysicalMonitorsFromHMONITOR(jitter):
    """
    BOOL GetPhysicalMonitorsFromHMONITOR(
        HMONITOR hMonitor,
        DWORD dwPhysicalMonitorArraySize,
        LPPHYSICAL_MONITOR pPhysicalMonitorArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hMonitor", "dwPhysicalMonitorArraySize", "pPhysicalMonitorArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_GetPhysicalMonitorsFromIDirect3DDevice9(jitter):
    """
    BOOL GetPhysicalMonitorsFromIDirect3DDevice9(
        IDirect3DDevice9* pDirect3DDevice9,
        DWORD dwPhysicalMonitorArraySize,
        LPPHYSICAL_MONITOR pPhysicalMonitorArray
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDirect3DDevice9", "dwPhysicalMonitorArraySize", "pPhysicalMonitorArray"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DXVA2CreateDirect3DDeviceManager9(jitter):
    """
    HRESULT DXVA2CreateDirect3DDeviceManager9(
        UINT* pResetToken,
        IDirect3DDeviceManager9** ppDXVAManager
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pResetToken", "ppDXVAManager"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DXVA2CreateVideoService(jitter):
    """
    HRESULT DXVA2CreateVideoService(
        IDirect3DDevice9* pDD,
        REFIID riid,
        void** ppService
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDD", "riid", "ppService"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dxva2_DXVAHD_CreateDevice(jitter):
    """
    HRESULT DXVAHD_CreateDevice(
        IDirect3DDevice9Ex* pD3DDevice,
        const DXVAHD_CONTENT_DESC* pContentDesc,
        DXVAHD_DEVICE_USAGE Usage,
        PDXVAHDSW_Plugin pPlugin,
        IDXVAHD_Device** ppDevice
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pD3DDevice", "pContentDesc", "Usage", "pPlugin", "ppDevice"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
