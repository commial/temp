
def newdev_InstallNewDevice(jitter):
    """"
    [Newdev.dll] BOOL InstallNewDevice(HWND hwndParent, LPGUID ClassGuid, PDWORD pReboot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "ClassGuid", "pReboot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def newdev_DiInstallDevice(jitter):
    """"
    [Newdev.dll] BOOL DiInstallDevice(HWND hwndParent, HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, PSP_DRVINFO_DATA DriverInfoData, DWORD Flags, PBOOL NeedReboot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DeviceInfoSet", "DeviceInfoData", "DriverInfoData", "Flags", "NeedReboot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def newdev_DiInstallDriver(jitter):
    """"
    [Newdev.dll] BOOL DiInstallDriver(HWND hwndParent, LPCTSTR FullInfPath, DWORD Flags, PBOOL NeedReboot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "FullInfPath", "Flags", "NeedReboot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def newdev_DiRollbackDriver(jitter):
    """"
    [Newdev.dll] BOOL DiRollbackDriver(HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, HWND hwndParent, DWORD Flags, PBOOL NeedReboot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceInfoSet", "DeviceInfoData", "hwndParent", "Flags", "NeedReboot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def newdev_DiShowUpdateDevice(jitter):
    """"
    [Newdev.dll] BOOL DiShowUpdateDevice(HWND hwndParent, HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, DWORD Flags, PBOOL NeedReboot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DeviceInfoSet", "DeviceInfoData", "Flags", "NeedReboot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def newdev_DiUninstallDevice(jitter):
    """"
    [Newdev.dll] BOOL DiUninstallDevice(HWND hwndParent, HDEVINFO DeviceInfoSet, PSP_DEVINFO_DATA DeviceInfoData, DWORD Flags, PBOOL NeedReboot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DeviceInfoSet", "DeviceInfoData", "Flags", "NeedReboot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def newdev_UpdateDriverForPlugAndPlayDevices(jitter):
    """"
    [Newdev.dll] BOOL UpdateDriverForPlugAndPlayDevices(HWND hwndParent, LPCTSTR HardwareId, LPCTSTR FullInfPath, DWORD InstallFlags, PBOOL bRebootRequired)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "HardwareId", "FullInfPath", "InstallFlags", "bRebootRequired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def newdev_InstallSelectedDriver(jitter):
    """"
    [Newdev.dll] BOOL InstallSelectedDriver(HWND hwndParent, HDEVINFO DeviceInfoSet, LPCTSTR Reserved, BOOL Backup, PDWORD bReboot)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "DeviceInfoSet", "Reserved", "Backup", "bReboot"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
