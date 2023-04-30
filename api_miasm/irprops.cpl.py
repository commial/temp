
def irprops_BluetoothAuthenticateDevice(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothAuthenticateDevice(HWND hwndParent, HANDLE hRadio, BLUETOOTH_DEVICE_INFO* pbtdi, PWCHAR pszPasskey, ULONG ulPasskeyLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hRadio", "pbtdi", "pszPasskey", "ulPasskeyLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothAuthenticateMultipleDevices(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothAuthenticateMultipleDevices(HWND hwndParent, HANDLE hRadio, DWORD cDevices, BLUETOOTH_DEVICE_INFO* pbtdi)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hRadio", "cDevices", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothDisplayDeviceProperties(jitter):
    """
    [irprops.cpl] BOOL BluetoothDisplayDeviceProperties(HWND hwndParent, BLUETOOTH_DEVICE_INFO* pbtdi)
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothEnableDiscovery(jitter):
    """
    [irprops.cpl] BOOL BluetoothEnableDiscovery(HANDLE hRadio, BOOL fEnabled)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "fEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothEnableIncomingConnections(jitter):
    """
    [irprops.cpl] BOOL BluetoothEnableIncomingConnections(HANDLE hRadio, BOOL fEnabled)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "fEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothEnumerateInstalledServices(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothEnumerateInstalledServices(HANDLE hRadio, BLUETOOTH_DEVICE_INFO* pbtdi, DWORD* pcServices, GUID* pGuidServices)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pbtdi", "pcServices", "pGuidServices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothFindDeviceClose(jitter):
    """
    [irprops.cpl] BOOL BluetoothFindDeviceClose(HBLUETOOTH_DEVICE_FIND hFind)
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothFindFirstDevice(jitter):
    """
    [irprops.cpl] HBLUETOOTH_DEVICE_FIND BluetoothFindFirstDevice(BLUETOOTH_DEVICE_SEARCH_PARAMS* pbtsp, BLUETOOTH_DEVICE_INFO* pbtdi)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtsp", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothFindFirstRadio(jitter):
    """
    [irprops.cpl] HBLUETOOTH_RADIO_FIND BluetoothFindFirstRadio(BLUETOOTH_FIND_RADIO_PARAMS* pbtfrp, HANDLE* phRadio)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtfrp", "phRadio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothFindNextDevice(jitter):
    """
    [irprops.cpl] BOOL BluetoothFindNextDevice(HBLUETOOTH_DEVICE_FIND hFind, BLUETOOTH_DEVICE_INFO* pbtdi)
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothFindNextRadio(jitter):
    """
    [irprops.cpl] BOOL BluetoothFindNextRadio(HBLUETOOTH_RADIO_FIND hFind, HANDLE* phRadio)
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind", "phRadio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothFindRadioClose(jitter):
    """
    [irprops.cpl] BOOL BluetoothFindRadioClose(HBLUETOOTH_RADIO_FIND hFind)
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothGetDeviceInfo(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothGetDeviceInfo(HANDLE hRadio, BLUETOOTH_DEVICE_INFO* pbtdi)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothGetRadioInfo(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothGetRadioInfo(HANDLE hRadio, PBLUETOOTH_RADIO_INFO pRadioInfo)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pRadioInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothIsConnectable(jitter):
    """
    [irprops.cpl] BOOL BluetoothIsConnectable(HANDLE hRadio)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothIsDiscoverable(jitter):
    """
    [irprops.cpl] BOOL BluetoothIsDiscoverable(HANDLE hRadio)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothRegisterForAuthentication(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothRegisterForAuthentication(BLUETOOTH_DEVICE_INFO* pbtdi, HBLUETOOTH_AUTHENTICATION_REGISTRATION* phRegHandle, PFN_AUTHENTICATION_CALLBACK pfnCallback, PVOID pvParam)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtdi", "phRegHandle", "pfnCallback", "pvParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothRemoveDevice(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothRemoveDevice(BLUETOOTH_ADDRESS* pAddress)
    """
    ret_ad, args = jitter.func_args_stdcall(["pAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSdpEnumAttributes(jitter):
    """
    [irprops.cpl] BOOL BluetoothSdpEnumAttributes(LPBYTE pSDPStream, ULONG cbStreamSize, PFN_BLUETOOTH_ENUM_ATTRIBUTES_CALLBACK pfnCallback, LPVOID pvParam)
    """
    ret_ad, args = jitter.func_args_stdcall(["pSDPStream", "cbStreamSize", "pfnCallback", "pvParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSdpGetAttributeValue(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothSdpGetAttributeValue(LPBYTE pRecordStream, ULONG cbRecordLength, USHORT usAttributeId, PSDP_ELEMENT_DATA pAttributeData)
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecordStream", "cbRecordLength", "usAttributeId", "pAttributeData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSdpGetContainerElementData(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothSdpGetContainerElementData(LPBYTE pContainerStream, ULONG cbContainerLength, HBLUETOOTH_CONTAINER_ELEMENT* pElement, PSDP_ELEMENT_DATA pData)
    """
    ret_ad, args = jitter.func_args_stdcall(["pContainerStream", "cbContainerLength", "pElement", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSdpGetElementData(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothSdpGetElementData(LPBYTE pSdpStream, ULONG cbSpdStreamLength, PSDP_ELEMENT_DATA pData)
    """
    ret_ad, args = jitter.func_args_stdcall(["pSdpStream", "cbSpdStreamLength", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSdpGetString(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothSdpGetString(LPBYTE pRecordStream, ULONG cbRecordLength, PSDP_STRING_TYPE_DATA pStringData, USHORT usStringOffset, PWCHAR pszString, PULONG pcchStringLength)
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecordStream", "cbRecordLength", "pStringData", "usStringOffset", "pszString", "pcchStringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSelectDevices(jitter):
    """
    [irprops.cpl] BOOL BluetoothSelectDevices(BLUETOOTH_SELECT_DEVICE_PARAMS* pbtsdp)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtsdp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSelectDevicesFree(jitter):
    """
    [irprops.cpl] BOOL BluetoothSelectDevicesFree(BLUETOOTH_SELECT_DEVICE_PARAMS* pbtsdp)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtsdp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSendAuthenticationResponse(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothSendAuthenticationResponse(HANDLE hRadio, BLUETOOTH_DEVICE_INFO* pbtdi, LPWSTR pszPasskey)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pbtdi", "pszPasskey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothSetServiceState(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothSetServiceState(HANDLE hRadio, BLUETOOTH_DEVICE_INFO* pbtdi, GUID* pGuidService, DWORD dwServiceFlags)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pbtdi", "pGuidService", "dwServiceFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothUnregisterAuthentication(jitter):
    """
    [irprops.cpl] BOOL BluetoothUnregisterAuthentication(HBLUETOOTH_AUTHENTICATION_REGISTRATION hRegHandle)
    """
    ret_ad, args = jitter.func_args_stdcall(["hRegHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def irprops_BluetoothUpdateDeviceRecord(jitter):
    """
    [irprops.cpl] [ERROR_CODE] BluetoothUpdateDeviceRecord(BLUETOOTH_DEVICE_INFO* pbtdi)
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
