_BLUETOOTH_SERVICE_FLAGS_ = {
    "BLUETOOTH_SERVICE_DISABLE": 0x00,
    "BLUETOOTH_SERVICE_ENABLE": 0x01,
}
_BLUETOOTH_SERVICE_FLAGS__INV = {
    0x00: "BLUETOOTH_SERVICE_DISABLE",
    0x01: "BLUETOOTH_SERVICE_ENABLE",
}

def bthprops_BluetoothAuthenticateDevice(jitter):
    """
    [ERROR_CODE] BluetoothAuthenticateDevice(
        HWND hwndParent,
        HANDLE hRadio,
        BLUETOOTH_DEVICE_INFO* pbtdi,
        PWCHAR pszPasskey,
        ULONG ulPasskeyLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hRadio", "pbtdi", "pszPasskey", "ulPasskeyLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothAuthenticateDeviceEx(jitter):
    """
    [ERROR_CODE] BluetoothAuthenticateDeviceEx(
        HWND hwndParentIn,
        HANDLE hRadioIn,
        BLUETOOTH_DEVICE_INFO* pbtdilInOut,
        PBLUETOOTH_OOB_DATA_INFO pbtdilInOut,
        BLUETOOTH_AUTHENTICATION_REQUIREMENTS authenticationRequirement
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParentIn", "hRadioIn", "pbtdilInOut", "pbtdilInOut", "authenticationRequirement"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothAuthenticateMultipleDevices(jitter):
    """
    [ERROR_CODE] BluetoothAuthenticateMultipleDevices(
        HWND hwndParent,
        HANDLE hRadio,
        DWORD cDevices,
        BLUETOOTH_DEVICE_INFO* pbtdi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "hRadio", "cDevices", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothDisplayDeviceProperties(jitter):
    """
    BOOL BluetoothDisplayDeviceProperties(
        HWND hwndParent,
        BLUETOOTH_DEVICE_INFO* pbtdi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hwndParent", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothEnableDiscovery(jitter):
    """
    BOOL BluetoothEnableDiscovery(
        HANDLE hRadio,
        BOOL fEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "fEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothEnableIncomingConnections(jitter):
    """
    BOOL BluetoothEnableIncomingConnections(
        HANDLE hRadio,
        BOOL fEnabled
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "fEnabled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothEnumerateInstalledServices(jitter):
    """
    [ERROR_CODE] BluetoothEnumerateInstalledServices(
        HANDLE hRadio,
        BLUETOOTH_DEVICE_INFO* pbtdi,
        DWORD* pcServices,
        GUID* pGuidServices
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pbtdi", "pcServices", "pGuidServices"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothFindDeviceClose(jitter):
    """
    BOOL BluetoothFindDeviceClose(
        HBLUETOOTH_DEVICE_FIND hFind
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothFindFirstDevice(jitter):
    """
    HBLUETOOTH_DEVICE_FIND BluetoothFindFirstDevice(
        BLUETOOTH_DEVICE_SEARCH_PARAMS* pbtsp,
        BLUETOOTH_DEVICE_INFO* pbtdi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtsp", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothFindFirstRadio(jitter):
    """
    HBLUETOOTH_RADIO_FIND BluetoothFindFirstRadio(
        BLUETOOTH_FIND_RADIO_PARAMS* pbtfrp,
        HANDLE* phRadio
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtfrp", "phRadio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothFindNextDevice(jitter):
    """
    BOOL BluetoothFindNextDevice(
        HBLUETOOTH_DEVICE_FIND hFind,
        BLUETOOTH_DEVICE_INFO* pbtdi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothFindNextRadio(jitter):
    """
    BOOL BluetoothFindNextRadio(
        HBLUETOOTH_RADIO_FIND hFind,
        HANDLE* phRadio
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind", "phRadio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothFindRadioClose(jitter):
    """
    BOOL BluetoothFindRadioClose(
        HBLUETOOTH_RADIO_FIND hFind
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFind"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothGetDeviceInfo(jitter):
    """
    [ERROR_CODE] BluetoothGetDeviceInfo(
        HANDLE hRadio,
        BLUETOOTH_DEVICE_INFO* pbtdi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothGetRadioInfo(jitter):
    """
    [ERROR_CODE] BluetoothGetRadioInfo(
        HANDLE hRadio,
        PBLUETOOTH_RADIO_INFO pRadioInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pRadioInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothIsConnectable(jitter):
    """
    BOOL BluetoothIsConnectable(
        HANDLE hRadio
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothIsDiscoverable(jitter):
    """
    BOOL BluetoothIsDiscoverable(
        HANDLE hRadio
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothIsVersionAvailable(jitter):
    """
    BOOL BluetoothIsVersionAvailable(
        UCHAR MajorVersion,
        UCHAR MinorVersion
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MajorVersion", "MinorVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothRegisterForAuthentication(jitter):
    """
    [ERROR_CODE] BluetoothRegisterForAuthentication(
        BLUETOOTH_DEVICE_INFO* pbtdi,
        HBLUETOOTH_AUTHENTICATION_REGISTRATION* phRegHandle,
        PFN_AUTHENTICATION_CALLBACK pfnCallback,
        PVOID pvParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtdi", "phRegHandle", "pfnCallback", "pvParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothRegisterForAuthenticationEx(jitter):
    """
    [ERROR_CODE] BluetoothRegisterForAuthenticationEx(
        const BLUETOOTH_DEVICE_INFO* pbtdiln,
        HBLUETOOTH_AUTHENTICATION_REGISTRATION* phRegHandleOut,
        PFN_AUTHENTICATION_CALLBACK_EX pfnCallbackIn,
        PVOID pvParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtdiln", "phRegHandleOut", "pfnCallbackIn", "pvParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothRemoveDevice(jitter):
    """
    [ERROR_CODE] BluetoothRemoveDevice(
        BLUETOOTH_ADDRESS* pAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSdpEnumAttributes(jitter):
    """
    BOOL BluetoothSdpEnumAttributes(
        LPBYTE pSDPStream,
        ULONG cbStreamSize,
        PFN_BLUETOOTH_ENUM_ATTRIBUTES_CALLBACK pfnCallback,
        LPVOID pvParam
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSDPStream", "cbStreamSize", "pfnCallback", "pvParam"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSdpGetAttributeValue(jitter):
    """
    [ERROR_CODE] BluetoothSdpGetAttributeValue(
        LPBYTE pRecordStream,
        ULONG cbRecordLength,
        USHORT usAttributeId,
        PSDP_ELEMENT_DATA pAttributeData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecordStream", "cbRecordLength", "usAttributeId", "pAttributeData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSdpGetContainerElementData(jitter):
    """
    [ERROR_CODE] BluetoothSdpGetContainerElementData(
        LPBYTE pContainerStream,
        ULONG cbContainerLength,
        HBLUETOOTH_CONTAINER_ELEMENT* pElement,
        PSDP_ELEMENT_DATA pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pContainerStream", "cbContainerLength", "pElement", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSdpGetElementData(jitter):
    """
    [ERROR_CODE] BluetoothSdpGetElementData(
        LPBYTE pSdpStream,
        ULONG cbSpdStreamLength,
        PSDP_ELEMENT_DATA pData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pSdpStream", "cbSpdStreamLength", "pData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSdpGetString(jitter):
    """
    [ERROR_CODE] BluetoothSdpGetString(
        LPBYTE pRecordStream,
        ULONG cbRecordLength,
        PSDP_STRING_TYPE_DATA pStringData,
        USHORT usStringOffset,
        PWCHAR pszString,
        PULONG pcchStringLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecordStream", "cbRecordLength", "pStringData", "usStringOffset", "pszString", "pcchStringLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSelectDevices(jitter):
    """
    BOOL BluetoothSelectDevices(
        BLUETOOTH_SELECT_DEVICE_PARAMS* pbtsdp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtsdp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSelectDevicesFree(jitter):
    """
    BOOL BluetoothSelectDevicesFree(
        BLUETOOTH_SELECT_DEVICE_PARAMS* pbtsdp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtsdp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSendAuthenticationResponse(jitter):
    """
    [ERROR_CODE] BluetoothSendAuthenticationResponse(
        HANDLE hRadio,
        BLUETOOTH_DEVICE_INFO* pbtdi,
        LPWSTR pszPasskey
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pbtdi", "pszPasskey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSendAuthenticationResponseEx(jitter):
    """
    [ERROR_CODE] BluetoothSendAuthenticationResponseEx(
        HANDLE hRadioIn,
        PBLUETOOTH_AUTHENTICATE_RESPONSE pauthResponse
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadioIn", "pauthResponse"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSetLocalServiceInfo(jitter):
    """
    [ERROR_CODE] BluetoothSetLocalServiceInfo(
        HANDLE hRadioIn,
        const GUID* pClassGuid,
        ULONG ulInstance,
        const BLUETOOTH_LOCAL_SERVICE_INFO* pServiceInfoIn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadioIn", "pClassGuid", "ulInstance", "pServiceInfoIn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothSetServiceState(jitter):
    """
    [ERROR_CODE] BluetoothSetServiceState(
        HANDLE hRadio,
        BLUETOOTH_DEVICE_INFO* pbtdi,
        GUID* pGuidService,
        [BLUETOOTH_SERVICE_FLAGS] dwServiceFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRadio", "pbtdi", "pGuidService", "dwServiceFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothUnregisterAuthentication(jitter):
    """
    BOOL BluetoothUnregisterAuthentication(
        HBLUETOOTH_AUTHENTICATION_REGISTRATION hRegHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hRegHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def bthprops_BluetoothUpdateDeviceRecord(jitter):
    """
    [ERROR_CODE] BluetoothUpdateDeviceRecord(
        BLUETOOTH_DEVICE_INFO* pbtdi
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pbtdi"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
