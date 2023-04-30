
def wsmsvc_WSManCloseCommand(jitter):
    """"
    [Wsmsvc.dll] void WSManCloseCommand(WSMAN_COMMAND_HANDLE commandHandle, DWORD flags, WSMAN_SHELL_ASYNC* async)
    """"
    ret_ad, args = jitter.func_args_stdcall(["commandHandle", "flags", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCloseOperation(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManCloseOperation(WSMAN_OPERATION_HANDLE operationHandle, DWORD flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["operationHandle", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCloseSession(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManCloseSession(WSMAN_SESSION_HANDLE session, DWORD flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["session", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCloseShell(jitter):
    """"
    [Wsmsvc.dll] void WSManCloseShell(WSMAN_SHELL_HANDLE shellHandle, DWORD flags, WSMAN_SHELL_ASYNC* async)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shellHandle", "flags", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManConnectShell(jitter):
    """"
    [Wsmsvc.dll] void WSManConnectShell(WSMAN_SESSION_HANDLE session, DWORD flags, PCWSTR resourceUri, PCWSTR shellID, WSMAN_OPTION_SET* options, WSMAN_DATA* connectXml, WSMAN_SHELL_ASYNC* async, WSMAN_SHELL_HANDLE* shell)
    """"
    ret_ad, args = jitter.func_args_stdcall(["session", "flags", "resourceUri", "shellID", "options", "connectXml", "async", "shell"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManConnectShellCommand(jitter):
    """"
    [Wsmsvc.dll] void WSManConnectShellCommand(WSMAN_SHELL_HANDLE shell, DWORD flags, PCWSTR commandID, WSMAN_OPTION_SET* options, WSMAN_DATA* connectXml, WSMAN_SHELL_ASYNC* async, WSMAN_SHELL_HANDLE* command)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "commandID", "options", "connectXml", "async", "command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCreateSession(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManCreateSession(WSMAN_API_HANDLE apiHandle, PCWSTR connection, DWORD flags, WSMAN_AUTHENTICATION_CREDENTIALS* serverAuthenticationCredentials, WSMAN_PROXY_INFO* proxyInfo, WSMAN_SESSION_HANDLE* session)
    """"
    ret_ad, args = jitter.func_args_stdcall(["apiHandle", "connection", "flags", "serverAuthenticationCredentials", "proxyInfo", "session"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCreateShell(jitter):
    """"
    [Wsmsvc.dll] void WSManCreateShell(WSMAN_SESSION_HANDLE session, DWORD flags, PCWSTR resourceUri, WSMAN_SHELL_STARTUP_INFO* startupInfo, WSMAN_OPTION_SET* options, WSMAN_DATA* createXml, WSMAN_SHELL_ASYNC* async, WSMAN_SHELL_HANDLE* shell)
    """"
    ret_ad, args = jitter.func_args_stdcall(["session", "flags", "resourceUri", "startupInfo", "options", "createXml", "async", "shell"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCreateShellEx(jitter):
    """"
    [Wsmsvc.dll] void WSManCreateShellEx(WSMAN_SESSION_HANDLE session, DWORD flags, PCWSTR resourceUri, PCWSTR ShellID, WSMAN_SHELL_STARTUP_INFO* startupInfo, WSMAN_OPTION_SET* options, WSMAN_DATA* createXml, WSMAN_SHELL_ASYNC* async, WSMAN_SHELL_HANDLE* shell)
    """"
    ret_ad, args = jitter.func_args_stdcall(["session", "flags", "resourceUri", "ShellID", "startupInfo", "options", "createXml", "async", "shell"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManDeinitialize(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManDeinitialize(WSMAN_API_HANDLE apiHandle, DWORD flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["apiHandle", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManDisconnectShell(jitter):
    """"
    [Wsmsvc.dll] void WSManDisconnectShell(WSMAN_SHELL_HANDLE shell, WSManShellFlag flags, WSMAN_SHELL_DISCONNECT_INFO* disconnectInfo, WSMAN_SHELL_ASYNC* async)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "disconnectInfo", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManInitialize(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManInitialize([WSMAN_FLAG_REQUESTED_API_VERSION] flags, WSMAN_API_HANDLE* apiHandle)
    """"
    ret_ad, args = jitter.func_args_stdcall(["flags", "apiHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManReceiveShellOutput(jitter):
    """"
    [Wsmsvc.dll] void WSManReceiveShellOutput(WSMAN_SHELL_HANDLE shell, WSMAN_COMMAND_HANDLE command, DWORD flags, WSMAN_STREAM_ID_SET* desiredStreamSet, WSMAN_SHELL_ASYNC* async, WSMAN_OPERATION_HANDLE* receiveOperation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shell", "command", "flags", "desiredStreamSet", "async", "receiveOperation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManReconnectShell(jitter):
    """"
    [Wsmsvc.dll] void WSManReconnectShell(WSMAN_SHELL_HANDLE shell, DWORD flags, WSMAN_SHELL_ASYNC* async)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManReconnectShellCommand(jitter):
    """"
    [Wsmsvc.dll] void WSManReconnectShellCommand(WSMAN_COMMAND_HANDLE commandHandle, DWORD flags, WSMAN_SHELL_ASYNC* async)
    """"
    ret_ad, args = jitter.func_args_stdcall(["commandHandle", "flags", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManRunShellCommand(jitter):
    """"
    [Wsmsvc.dll] void WSManRunShellCommand(WSMAN_SHELL_HANDLE shell, DWORD flags, PCWSTR commandLine, WSMAN_COMMAND_ARG_SET* args, WSMAN_OPTION_SET* options, WSMAN_SHELL_ASYNC* async, WSMAN_COMMAND_HANDLE* command)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "commandLine", "args", "options", "async", "command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManRunShellCommandEx(jitter):
    """"
    [Wsmsvc.dll] void WSManRunShellCommandEx(WSMAN_SHELL_HANDLE shell, DWORD flags, PCWSTR commandID, PCWSTR commandLine, WSMAN_COMMAND_ARG_SET* args, WSMAN_OPTION_SET* options, WSMAN_SHELL_ASYNC* async, WSMAN_COMMAND_HANDLE* command)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "commandID", "commandLine", "args", "options", "async", "command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManSendShellInput(jitter):
    """"
    [Wsmsvc.dll] void WSManSendShellInput(WSMAN_SHELL_HANDLE shell, WSMAN_COMMAND_HANDLE command, DWORD flags, PCWSTR streamId, WSMAN_DATA* streamData, BOOL endOfStream, WSMAN_SHELL_ASYNC* async, WSMAN_OPERATION_HANDLE* sendOperation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shell", "command", "flags", "streamId", "streamData", "endOfStream", "async", "sendOperation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManSignalShell(jitter):
    """"
    [Wsmsvc.dll] void WSManSignalShell(WSMAN_SHELL_HANDLE shell, WSMAN_COMMAND_HANDLE command, DWORD flags, PCWSTR code, WSMAN_SHELL_ASYNC* async, WSMAN_OPERATION_HANDLE* signalOperation)
    """"
    ret_ad, args = jitter.func_args_stdcall(["shell", "command", "flags", "code", "async", "signalOperation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManGetErrorMessage(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManGetErrorMessage(WSMAN_API_HANDLE apiHandle, DWORD flags, PCWSTR languageCode, DWORD errorCode, DWORD messageLength, PWSTR message, DWORD* messageLengthUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["apiHandle", "flags", "languageCode", "errorCode", "messageLength", "message", "messageLengthUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManGetSessionOptionAsDword(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManGetSessionOptionAsDword(WSMAN_SESSION_HANDLE session, WSManSessionOption option, DWORD* value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["session", "option", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManGetSessionOptionAsString(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManGetSessionOptionAsString(WSMAN_SESSION_HANDLE session, WSManSessionOption option, DWORD stringLength, PWSTR string, DWORD* stringLengthUsed)
    """"
    ret_ad, args = jitter.func_args_stdcall(["session", "option", "stringLength", "string", "stringLengthUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManSetSessionOption(jitter):
    """"
    [Wsmsvc.dll] [ERROR_CODE] WSManSetSessionOption(WSMAN_SESSION_HANDLE session, WSManSessionOption option, WSMAN_DATA* data)
    """"
    ret_ad, args = jitter.func_args_stdcall(["session", "option", "data"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
