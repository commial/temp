
def winusb_WinUsb_AbortPipe(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_AbortPipe(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR PipeID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ControlTransfer(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_ControlTransfer(WINUSB_INTERFACE_HANDLE InterfaceHandle, WINUSB_SETUP_PACKET SetupPacket, PUCHAR Buffer, ULONG BufferLength, PULONG LengthTransferred, LPOVERLAPPED Overlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "SetupPacket", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_FlushPipe(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_FlushPipe(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR PipeID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_Free(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_Free(WINUSB_INTERFACE_HANDLE InterfaceHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetAssociatedInterface(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_GetAssociatedInterface(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR AssociatedInterfaceIndex, PWINUSB_INTERFACE_HANDLE AssociatedInterfaceHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AssociatedInterfaceIndex", "AssociatedInterfaceHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetCurrentAlternateSetting(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_GetCurrentAlternateSetting(WINUSB_INTERFACE_HANDLE InterfaceHandle, PUCHAR AlternateSetting)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AlternateSetting"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetDescriptor(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_GetDescriptor(WINUSB_INTERFACE_HANDLE InterfaceHandle, [USB_DESCRIPTOR_TYPE] DescriptorType, UCHAR Index, USHORT LanguageID, PUCHAR Buffer, ULONG BufferLength, PULONG LengthTransferred)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "DescriptorType", "Index", "LanguageID", "Buffer", "BufferLength", "LengthTransferred"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetOverlappedResult(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_GetOverlappedResult(WINUSB_INTERFACE_HANDLE InterfaceHandle, LPOVERLAPPED lpOverlapped, LPDWORD lpNumberOfBytesTransferred, BOOL bWait)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "lpOverlapped", "lpNumberOfBytesTransferred", "bWait"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetPipePolicy(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_GetPipePolicy(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR PipeID, [USB_PIPE_POLICY_TYPE] PolicyType, PULONG ValueLength, PVOID Value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID", "PolicyType", "ValueLength", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_GetPowerPolicy(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_GetPowerPolicy(WINUSB_INTERFACE_HANDLE InterfaceHandle, [USB_POWER_POLICY_TYPE] PolicyType, PULONG ValueLength, PVOID Value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PolicyType", "ValueLength", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_Initialize(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_Initialize(HANDLE DeviceHandle, PWINUSB_INTERFACE_HANDLE InterfaceHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DeviceHandle", "InterfaceHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_QueryDeviceInformation(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_QueryDeviceInformation(WINUSB_INTERFACE_HANDLE InterfaceHandle, [USB_INFORMATION_TYPE] InformationType, PULONG BufferLength, PVOID Buffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "InformationType", "BufferLength", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_QueryInterfaceSettings(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_QueryInterfaceSettings(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR AlternateSettingNumber, PUSB_INTERFACE_DESCRIPTOR UsbAltInterfaceDescriptor)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AlternateSettingNumber", "UsbAltInterfaceDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_QueryPipe(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_QueryPipe(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR AlternateInterfaceNumber, UCHAR PipeIndex, PWINUSB_PIPE_INFORMATION PipeInformation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AlternateInterfaceNumber", "PipeIndex", "PipeInformation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ReadPipe(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_ReadPipe(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR PipeID, PUCHAR Buffer, ULONG BufferLength, PULONG LengthTransferred, LPOVERLAPPED Overlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ResetPipe(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_ResetPipe(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR PipeID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_SetCurrentAlternateSetting(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_SetCurrentAlternateSetting(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR AlternateSetting)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "AlternateSetting"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_SetPipePolicy(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_SetPipePolicy(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR PipeID, [USB_PIPE_POLICY_TYPE] PolicyType, ULONG ValueLength, PVOID Value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID", "PolicyType", "ValueLength", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_SetPowerPolicy(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_SetPowerPolicy(WINUSB_INTERFACE_HANDLE InterfaceHandle, [USB_POWER_POLICY_TYPE] PolicyType, ULONG ValueLength, PVOID Value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PolicyType", "ValueLength", "Value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_WritePipe(jitter):
    """"
    [WinUsb.dll] BOOL WinUsb_WritePipe(WINUSB_INTERFACE_HANDLE InterfaceHandle, UCHAR PipeID, PUCHAR Buffer, ULONG BufferLength, PULONG LengthTransferred, LPOVERLAPPED Overlapped)
    """"
    ret_ad, args = jitter.func_args_stdcall(["InterfaceHandle", "PipeID", "Buffer", "BufferLength", "LengthTransferred", "Overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ParseDescriptors(jitter):
    """"
    [WinUsb.dll] PUSB_COMMON_DESCRIPTOR WinUsb_ParseDescriptors(PVOID DescriptorBuffer, ULONG TotalLength, PVOID StartPosition, LONG DescriptorType)
    """"
    ret_ad, args = jitter.func_args_stdcall(["DescriptorBuffer", "TotalLength", "StartPosition", "DescriptorType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winusb_WinUsb_ParseConfigurationDescriptor(jitter):
    """"
    [WinUsb.dll] PUSB_INTERFACE_DESCRIPTOR WinUsb_ParseConfigurationDescriptor(PUSB_CONFIGURATION_DESCRIPTOR ConfigurationDescriptor, PVOID StartPosition, LONG InterfaceNumber, LONG AlternateSetting, LONG InterfaceClass, LONG InterfaceSubClass, LONG InterfaceProtocol)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ConfigurationDescriptor", "StartPosition", "InterfaceNumber", "AlternateSetting", "InterfaceClass", "InterfaceSubClass", "InterfaceProtocol"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
