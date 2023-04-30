_USB_DESCRIPTOR_TYPE_ = {
    "USB_DEVICE_DESCRIPTOR_TYPE": 0x01,
    "USB_CONFIGURATION_DESCRIPTOR_TYPE": 0x02,
    "USB_STRING_DESCRIPTOR_TYPE": 0x03,
    "USB_INTERFACE_DESCRIPTOR_TYPE": 0x04,
    "USB_ENDPOINT_DESCRIPTOR_TYPE": 0x05,
    "USB_DEVICE_QUALIFIER_DESCRIPTOR_TYPE": 0x06,
    "USB_OTHER_SPEED_CONFIGURATION_DESCRIPTOR_TYPE": 0x07,
    "USB_INTERFACE_POWER_DESCRIPTOR_TYPE": 0x08,
    "USB_OTG_DESCRIPTOR_TYPE": 0x09,
    "USB_DEBUG_DESCRIPTOR_TYPE": 0x0A,
    "USB_INTERFACE_ASSOCIATION_DESCRIPTOR_TYPE": 0x0B,
    "USB_BOS_DESCRIPTOR_TYPE": 0x0F,
    "USB_DEVICE_CAPABILITY_DESCRIPTOR_TYPE": 0x10,
    "USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR_TYPE": 0x30,
}
_USB_DESCRIPTOR_TYPE__INV = {
    0x01: "USB_DEVICE_DESCRIPTOR_TYPE",
    0x02: "USB_CONFIGURATION_DESCRIPTOR_TYPE",
    0x03: "USB_STRING_DESCRIPTOR_TYPE",
    0x04: "USB_INTERFACE_DESCRIPTOR_TYPE",
    0x05: "USB_ENDPOINT_DESCRIPTOR_TYPE",
    0x06: "USB_DEVICE_QUALIFIER_DESCRIPTOR_TYPE",
    0x07: "USB_OTHER_SPEED_CONFIGURATION_DESCRIPTOR_TYPE",
    0x08: "USB_INTERFACE_POWER_DESCRIPTOR_TYPE",
    0x09: "USB_OTG_DESCRIPTOR_TYPE",
    0x0A: "USB_DEBUG_DESCRIPTOR_TYPE",
    0x0B: "USB_INTERFACE_ASSOCIATION_DESCRIPTOR_TYPE",
    0x0F: "USB_BOS_DESCRIPTOR_TYPE",
    0x10: "USB_DEVICE_CAPABILITY_DESCRIPTOR_TYPE",
    0x30: "USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR_TYPE",
}
_USB_PIPE_POLICY_TYPE_ = {
    "SHORT_PACKET_TERMINATE": 0x01,
    "AUTO_CLEAR_STALL": 0x02,
    "PIPE_TRANSFER_TIMEOUT": 0x03,
    "IGNORE_SHORT_PACKETS": 0x04,
    "ALLOW_PARTIAL_READS": 0x05,
    "AUTO_FLUSH": 0x06,
    "RAW_IO": 0x07,
    "MAXIMUM_TRANSFER_SIZE": 0x08,
    "RESET_PIPE_ON_RESUME": 0x09,
}
_USB_PIPE_POLICY_TYPE__INV = {
    0x01: "SHORT_PACKET_TERMINATE",
    0x02: "AUTO_CLEAR_STALL",
    0x03: "PIPE_TRANSFER_TIMEOUT",
    0x04: "IGNORE_SHORT_PACKETS",
    0x05: "ALLOW_PARTIAL_READS",
    0x06: "AUTO_FLUSH",
    0x07: "RAW_IO",
    0x08: "MAXIMUM_TRANSFER_SIZE",
    0x09: "RESET_PIPE_ON_RESUME",
}
_USB_POWER_POLICY_TYPE_ = {
    "AUTO_SUSPEND": 0x81,
    "SUSPEND_DELAY": 0x83,
}
_USB_POWER_POLICY_TYPE__INV = {
    0x81: "AUTO_SUSPEND",
    0x83: "SUSPEND_DELAY",
}
_USB_INFORMATION_TYPE_ = {
    "DEVICE_SPEED": 0x01,
}
_USB_INFORMATION_TYPE__INV = {
    0x01: "DEVICE_SPEED",
}
_USB_REQUEST_ = {
    "USB_REQUEST_GET_STATUS": 0x00,
    "USB_REQUEST_CLEAR_FEATURE": 0x01,
    "USB_REQUEST_SET_FEATURE": 0x03,
    "USB_REQUEST_SET_ADDRESS": 0x05,
    "USB_REQUEST_GET_DESCRIPTOR": 0x06,
    "USB_REQUEST_SET_DESCRIPTOR": 0x07,
    "USB_REQUEST_GET_CONFIGURATION": 0x08,
    "USB_REQUEST_SET_CONFIGURATION": 0x09,
    "USB_REQUEST_GET_INTERFACE": 0x0A,
    "USB_REQUEST_SET_INTERFACE": 0x0B,
    "USB_REQUEST_SYNC_FRAME": 0x0C,
    "USB_REQUEST_SET_SEL": 0x30,
    "USB_REQUEST_ISOCH_DELAY": 0x31,
}
_USB_REQUEST__INV = {
    0x00: "USB_REQUEST_GET_STATUS",
    0x01: "USB_REQUEST_CLEAR_FEATURE",
    0x03: "USB_REQUEST_SET_FEATURE",
    0x05: "USB_REQUEST_SET_ADDRESS",
    0x06: "USB_REQUEST_GET_DESCRIPTOR",
    0x07: "USB_REQUEST_SET_DESCRIPTOR",
    0x08: "USB_REQUEST_GET_CONFIGURATION",
    0x09: "USB_REQUEST_SET_CONFIGURATION",
    0x0A: "USB_REQUEST_GET_INTERFACE",
    0x0B: "USB_REQUEST_SET_INTERFACE",
    0x0C: "USB_REQUEST_SYNC_FRAME",
    0x30: "USB_REQUEST_SET_SEL",
    0x31: "USB_REQUEST_ISOCH_DELAY",
}
_USB_DEVICE_CLASS_ = {
    "USB_DEVICE_CLASS_RESERVED": 0x00,
    "USB_DEVICE_CLASS_AUDIO": 0x01,
    "USB_DEVICE_CLASS_COMMUNICATIONS": 0x02,
    "USB_DEVICE_CLASS_HUMAN_INTERFACE": 0x03,
    "USB_DEVICE_CLASS_MONITOR": 0x04,
    "USB_DEVICE_CLASS_PHYSICAL_INTERFACE": 0x05,
    "USB_DEVICE_CLASS_POWER": 0x06,
    "USB_DEVICE_CLASS_IMAGE": 0x06,
    "USB_DEVICE_CLASS_PRINTER": 0x07,
    "USB_DEVICE_CLASS_STORAGE": 0x08,
    "USB_DEVICE_CLASS_HUB": 0x09,
    "USB_DEVICE_CLASS_CDC_DATA": 0x0A,
    "USB_DEVICE_CLASS_SMART_CARD": 0x0B,
    "USB_DEVICE_CLASS_CONTENT_SECURITY": 0x0D,
    "USB_DEVICE_CLASS_VIDEO": 0x0E,
    "USB_DEVICE_CLASS_PERSONAL_HEALTHCARE": 0x0F,
    "USB_DEVICE_CLASS_DIAGNOSTIC_DEVICE": 0xDC,
    "USB_DEVICE_CLASS_WIRELESS_CONTROLLER": 0xE0,
    "USB_DEVICE_CLASS_MISCELLANEOUS": 0xEF,
    "USB_DEVICE_CLASS_APPLICATION_SPECIFIC": 0xFE,
    "USB_DEVICE_CLASS_VENDOR_SPECIFIC": 0xFF,
}
_USB_DEVICE_CLASS__INV = {
    0x00: "USB_DEVICE_CLASS_RESERVED",
    0x01: "USB_DEVICE_CLASS_AUDIO",
    0x02: "USB_DEVICE_CLASS_COMMUNICATIONS",
    0x03: "USB_DEVICE_CLASS_HUMAN_INTERFACE",
    0x04: "USB_DEVICE_CLASS_MONITOR",
    0x05: "USB_DEVICE_CLASS_PHYSICAL_INTERFACE",
    0x06: "USB_DEVICE_CLASS_POWER",
    0x06: "USB_DEVICE_CLASS_IMAGE",
    0x07: "USB_DEVICE_CLASS_PRINTER",
    0x08: "USB_DEVICE_CLASS_STORAGE",
    0x09: "USB_DEVICE_CLASS_HUB",
    0x0A: "USB_DEVICE_CLASS_CDC_DATA",
    0x0B: "USB_DEVICE_CLASS_SMART_CARD",
    0x0D: "USB_DEVICE_CLASS_CONTENT_SECURITY",
    0x0E: "USB_DEVICE_CLASS_VIDEO",
    0x0F: "USB_DEVICE_CLASS_PERSONAL_HEALTHCARE",
    0xDC: "USB_DEVICE_CLASS_DIAGNOSTIC_DEVICE",
    0xE0: "USB_DEVICE_CLASS_WIRELESS_CONTROLLER",
    0xEF: "USB_DEVICE_CLASS_MISCELLANEOUS",
    0xFE: "USB_DEVICE_CLASS_APPLICATION_SPECIFIC",
    0xFF: "USB_DEVICE_CLASS_VENDOR_SPECIFIC",
}
USBD_PIPE_TYPE = {
    "UsbdPipeTypeControl": 0,
    "UsbdPipeTypeIsochronous": 1,
    "UsbdPipeTypeBulk": 2,
    "UsbdPipeTypeInterrupt": 3,
}
USBD_PIPE_TYPE_INV = {
    0: "UsbdPipeTypeControl",
    1: "UsbdPipeTypeIsochronous",
    2: "UsbdPipeTypeBulk",
    3: "UsbdPipeTypeInterrupt",
}

def winusb_WinUsb_AbortPipe(jitter):
    """
    BOOL WinUsb_AbortPipe(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR PipeID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ControlTransfer(jitter):
    """
    BOOL WinUsb_ControlTransfer(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        WINUSB_SETUP_PACKET SetupPacket,
        PUCHAR Buffer,
        ULONG BufferLength,
        PULONG LengthTransferred,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "SetupPacket", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_FlushPipe(jitter):
    """
    BOOL WinUsb_FlushPipe(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR PipeID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_Free(jitter):
    """
    BOOL WinUsb_Free(
        WINUSB_INTERFACE_HANDLE InterfaceHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetAssociatedInterface(jitter):
    """
    BOOL WinUsb_GetAssociatedInterface(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR AssociatedInterfaceIndex,
        PWINUSB_INTERFACE_HANDLE AssociatedInterfaceHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AssociatedInterfaceIndex", "AssociatedInterfaceHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetCurrentAlternateSetting(jitter):
    """
    BOOL WinUsb_GetCurrentAlternateSetting(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        PUCHAR AlternateSetting
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AlternateSetting"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetDescriptor(jitter):
    """
    BOOL WinUsb_GetDescriptor(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        [USB_DESCRIPTOR_TYPE] DescriptorType,
        UCHAR Index,
        USHORT LanguageID,
        PUCHAR Buffer,
        ULONG BufferLength,
        PULONG LengthTransferred
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "DescriptorType", "Index", "LanguageID", "Buffer", "BufferLength", "LengthTransferred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetOverlappedResult(jitter):
    """
    BOOL WinUsb_GetOverlappedResult(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        LPOVERLAPPED lpOverlapped,
        LPDWORD lpNumberOfBytesTransferred,
        BOOL bWait
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "lpOverlapped", "lpNumberOfBytesTransferred", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetPipePolicy(jitter):
    """
    BOOL WinUsb_GetPipePolicy(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR PipeID,
        [USB_PIPE_POLICY_TYPE] PolicyType,
        PULONG ValueLength,
        PVOID Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID", "PolicyType", "ValueLength", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetPowerPolicy(jitter):
    """
    BOOL WinUsb_GetPowerPolicy(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        [USB_POWER_POLICY_TYPE] PolicyType,
        PULONG ValueLength,
        PVOID Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PolicyType", "ValueLength", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_Initialize(jitter):
    """
    BOOL WinUsb_Initialize(
        HANDLE DeviceHandle,
        PWINUSB_INTERFACE_HANDLE InterfaceHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DeviceHandle", "InterfaceHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_QueryDeviceInformation(jitter):
    """
    BOOL WinUsb_QueryDeviceInformation(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        [USB_INFORMATION_TYPE] InformationType,
        PULONG BufferLength,
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "InformationType", "BufferLength", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_QueryInterfaceSettings(jitter):
    """
    BOOL WinUsb_QueryInterfaceSettings(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR AlternateSettingNumber,
        PUSB_INTERFACE_DESCRIPTOR UsbAltInterfaceDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AlternateSettingNumber", "UsbAltInterfaceDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_QueryPipe(jitter):
    """
    BOOL WinUsb_QueryPipe(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR AlternateInterfaceNumber,
        UCHAR PipeIndex,
        PWINUSB_PIPE_INFORMATION PipeInformation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AlternateInterfaceNumber", "PipeIndex", "PipeInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ReadPipe(jitter):
    """
    BOOL WinUsb_ReadPipe(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR PipeID,
        PUCHAR Buffer,
        ULONG BufferLength,
        PULONG LengthTransferred,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ResetPipe(jitter):
    """
    BOOL WinUsb_ResetPipe(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR PipeID
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_SetCurrentAlternateSetting(jitter):
    """
    BOOL WinUsb_SetCurrentAlternateSetting(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR AlternateSetting
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AlternateSetting"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_SetPipePolicy(jitter):
    """
    BOOL WinUsb_SetPipePolicy(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR PipeID,
        [USB_PIPE_POLICY_TYPE] PolicyType,
        ULONG ValueLength,
        PVOID Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID", "PolicyType", "ValueLength", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_SetPowerPolicy(jitter):
    """
    BOOL WinUsb_SetPowerPolicy(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        [USB_POWER_POLICY_TYPE] PolicyType,
        ULONG ValueLength,
        PVOID Value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PolicyType", "ValueLength", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_WritePipe(jitter):
    """
    BOOL WinUsb_WritePipe(
        WINUSB_INTERFACE_HANDLE InterfaceHandle,
        UCHAR PipeID,
        PUCHAR Buffer,
        ULONG BufferLength,
        PULONG LengthTransferred,
        LPOVERLAPPED Overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ParseDescriptors(jitter):
    """
    PUSB_COMMON_DESCRIPTOR WinUsb_ParseDescriptors(
        PVOID DescriptorBuffer,
        ULONG TotalLength,
        PVOID StartPosition,
        LONG DescriptorType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DescriptorBuffer", "TotalLength", "StartPosition", "DescriptorType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ParseConfigurationDescriptor(jitter):
    """
    PUSB_INTERFACE_DESCRIPTOR WinUsb_ParseConfigurationDescriptor(
        PUSB_CONFIGURATION_DESCRIPTOR ConfigurationDescriptor,
        PVOID StartPosition,
        LONG InterfaceNumber,
        LONG AlternateSetting,
        LONG InterfaceClass,
        LONG InterfaceSubClass,
        LONG InterfaceProtocol
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConfigurationDescriptor", "StartPosition", "InterfaceNumber", "AlternateSetting", "InterfaceClass", "InterfaceSubClass", "InterfaceProtocol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
