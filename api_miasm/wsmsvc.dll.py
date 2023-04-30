WSManShellFlag = {
    "WSMAN_FLAG_NO_COMPRESSION": 0x1,
    "WSMAN_FLAG_DELETE_SERVER_SESSION": 0x2,
    "WSMAN_FLAG_SERVER_BUFFERING_MODE_DROP": 0x4,
    "WSMAN_FLAG_SERVER_BUFFERING_MODE_BLOCK": 0x8,
    "WSMAN_FLAG_RECEIVE_DELAY_OUTPUT_STREAM": 0X10,
}
WSManShellFlag_INV = {
    0x1: "WSMAN_FLAG_NO_COMPRESSION",
    0x2: "WSMAN_FLAG_DELETE_SERVER_SESSION",
    0x4: "WSMAN_FLAG_SERVER_BUFFERING_MODE_DROP",
    0x8: "WSMAN_FLAG_SERVER_BUFFERING_MODE_BLOCK",
    0X10: "WSMAN_FLAG_RECEIVE_DELAY_OUTPUT_STREAM",
}
_WSMAN_FLAG_REQUESTED_API_VERSION_ = {
    "WSMAN_FLAG_REQUESTED_API_VERSION_1_0": 0x0,
    "WSMAN_FLAG_REQUESTED_API_VERSION_1_1": 0x1,
}
_WSMAN_FLAG_REQUESTED_API_VERSION__INV = {
    0x0: "WSMAN_FLAG_REQUESTED_API_VERSION_1_0",
    0x1: "WSMAN_FLAG_REQUESTED_API_VERSION_1_1",
}
WSManAuthenticationFlags = {
    "WSMAN_FLAG_DEFAULT_AUTHENTICATION": 0x0,
    "WSMAN_FLAG_NO_AUTHENTICATION": 0x1,
    "WSMAN_FLAG_AUTH_DIGEST": 0x2,
    "WSMAN_FLAG_AUTH_NEGOTIATE": 0x4,
    "WSMAN_FLAG_AUTH_BASIC": 0x8,
    "WSMAN_FLAG_AUTH_KERBEROS": 0x10,
    "WSMAN_FLAG_AUTH_CREDSSP": 0x80,
    "WSMAN_FLAG_AUTH_CLIENT_CERTIFICATE": 0x20,
}
WSManAuthenticationFlags_INV = {
    0x0: "WSMAN_FLAG_DEFAULT_AUTHENTICATION",
    0x1: "WSMAN_FLAG_NO_AUTHENTICATION",
    0x2: "WSMAN_FLAG_AUTH_DIGEST",
    0x4: "WSMAN_FLAG_AUTH_NEGOTIATE",
    0x8: "WSMAN_FLAG_AUTH_BASIC",
    0x10: "WSMAN_FLAG_AUTH_KERBEROS",
    0x80: "WSMAN_FLAG_AUTH_CREDSSP",
    0x20: "WSMAN_FLAG_AUTH_CLIENT_CERTIFICATE",
}
WSManSessionOption = {
    "WSMAN_OPTION_DEFAULT_OPERATION_TIMEOUTMS": 1,
    "WSMAN_OPTION_MAX_RETRY_TIME": 11,
    "WSMAN_OPTION_TIMEOUTMS_CREATE_SHELL": 12,
    "WSMAN_OPTION_TIMEOUTMS_RUN_SHELL_COMMAND": 13,
    "WSMAN_OPTION_TIMEOUTMS_RECEIVE_SHELL_OUTPUT": 14,
    "WSMAN_OPTION_TIMEOUTMS_SEND_SHELL_INPUT": 15,
    "WSMAN_OPTION_TIMEOUTMS_SIGNAL_SHELL": 16,
    "WSMAN_OPTION_TIMEOUTMS_CLOSE_SHELL": 17,
    "WSMAN_OPTION_SKIP_CA_CHECK": 18,
    "WSMAN_OPTION_SKIP_CN_CHECK": 19,
    "WSMAN_OPTION_UNENCRYPTED_MESSAGES": 20,
    "WSMAN_OPTION_UTF16": 21,
    "WSMAN_OPTION_ENABLE_SPN_SERVER_PORT": 22,
    "WSMAN_OPTION_MACHINE_ID": 23,
    "WSMAN_OPTION_LOCALE": 25,
    "WSMAN_OPTION_UI_LANGUAGE": 26,
    "WSMAN_OPTION_MAX_ENVELOPE_SIZE_KB": 28,
    "WSMAN_OPTION_SHELL_MAX_DATA_SIZE_PER_MESSAGE_KB": 29,
    "WSMAN_OPTION_REDIRECT_LOCATION": 30,
    "WSMAN_OPTION_SKIP_REVOCATION_CHECK": 31,
    "WSMAN_OPTION_ALLOW_NEGOTIATE_IMPLICIT_CREDENTIALS": 32,
    "WSMAN_OPTION_USE_SSL": 33,
    "WSMAN_OPTION_USE_INTEARACTIVE_TOKEN": 34,
}
WSManSessionOption_INV = {
    1: "WSMAN_OPTION_DEFAULT_OPERATION_TIMEOUTMS",
    11: "WSMAN_OPTION_MAX_RETRY_TIME",
    12: "WSMAN_OPTION_TIMEOUTMS_CREATE_SHELL",
    13: "WSMAN_OPTION_TIMEOUTMS_RUN_SHELL_COMMAND",
    14: "WSMAN_OPTION_TIMEOUTMS_RECEIVE_SHELL_OUTPUT",
    15: "WSMAN_OPTION_TIMEOUTMS_SEND_SHELL_INPUT",
    16: "WSMAN_OPTION_TIMEOUTMS_SIGNAL_SHELL",
    17: "WSMAN_OPTION_TIMEOUTMS_CLOSE_SHELL",
    18: "WSMAN_OPTION_SKIP_CA_CHECK",
    19: "WSMAN_OPTION_SKIP_CN_CHECK",
    20: "WSMAN_OPTION_UNENCRYPTED_MESSAGES",
    21: "WSMAN_OPTION_UTF16",
    22: "WSMAN_OPTION_ENABLE_SPN_SERVER_PORT",
    23: "WSMAN_OPTION_MACHINE_ID",
    25: "WSMAN_OPTION_LOCALE",
    26: "WSMAN_OPTION_UI_LANGUAGE",
    28: "WSMAN_OPTION_MAX_ENVELOPE_SIZE_KB",
    29: "WSMAN_OPTION_SHELL_MAX_DATA_SIZE_PER_MESSAGE_KB",
    30: "WSMAN_OPTION_REDIRECT_LOCATION",
    31: "WSMAN_OPTION_SKIP_REVOCATION_CHECK",
    32: "WSMAN_OPTION_ALLOW_NEGOTIATE_IMPLICIT_CREDENTIALS",
    33: "WSMAN_OPTION_USE_SSL",
    34: "WSMAN_OPTION_USE_INTEARACTIVE_TOKEN",
}
WSManDataType = {
    "WSMAN_DATA_NONE": 0,
    "WSMAN_DATA_TYPE_TEXT": 1,
    "WSMAN_DATA_TYPE_BINARY": 2,
    "WSMAN_DATA_TYPE_DWORD": 4,
}
WSManDataType_INV = {
    0: "WSMAN_DATA_NONE",
    1: "WSMAN_DATA_TYPE_TEXT",
    2: "WSMAN_DATA_TYPE_BINARY",
    4: "WSMAN_DATA_TYPE_DWORD",
}
WSManProxyAccessType = {
    "WSMAN_OPTION_PROXY_IE_PROXY_CONFIG": 1,
    "WSMAN_OPTION_PROXY_WINHTTP_PROXY_CONFIG": 2,
    "WSMAN_OPTION_PROXY_AUTO_DETECT": 4,
    "WSMAN_OPTION_PROXY_NO_PROXY_SERVER": 8,
}
WSManProxyAccessType_INV = {
    1: "WSMAN_OPTION_PROXY_IE_PROXY_CONFIG",
    2: "WSMAN_OPTION_PROXY_WINHTTP_PROXY_CONFIG",
    4: "WSMAN_OPTION_PROXY_AUTO_DETECT",
    8: "WSMAN_OPTION_PROXY_NO_PROXY_SERVER",
}

def wsmsvc_WSManCloseCommand(jitter):
    """
    void WSManCloseCommand(
        WSMAN_COMMAND_HANDLE commandHandle,
        DWORD flags,
        WSMAN_SHELL_ASYNC* async
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["commandHandle", "flags", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCloseOperation(jitter):
    """
    [ERROR_CODE] WSManCloseOperation(
        WSMAN_OPERATION_HANDLE operationHandle,
        DWORD flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["operationHandle", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCloseSession(jitter):
    """
    [ERROR_CODE] WSManCloseSession(
        WSMAN_SESSION_HANDLE session,
        DWORD flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCloseShell(jitter):
    """
    void WSManCloseShell(
        WSMAN_SHELL_HANDLE shellHandle,
        DWORD flags,
        WSMAN_SHELL_ASYNC* async
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shellHandle", "flags", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManConnectShell(jitter):
    """
    void WSManConnectShell(
        WSMAN_SESSION_HANDLE session,
        DWORD flags,
        PCWSTR resourceUri,
        PCWSTR shellID,
        WSMAN_OPTION_SET* options,
        WSMAN_DATA* connectXml,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_SHELL_HANDLE* shell
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "flags", "resourceUri", "shellID", "options", "connectXml", "async", "shell"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManConnectShellCommand(jitter):
    """
    void WSManConnectShellCommand(
        WSMAN_SHELL_HANDLE shell,
        DWORD flags,
        PCWSTR commandID,
        WSMAN_OPTION_SET* options,
        WSMAN_DATA* connectXml,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_SHELL_HANDLE* command
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "commandID", "options", "connectXml", "async", "command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCreateSession(jitter):
    """
    [ERROR_CODE] WSManCreateSession(
        WSMAN_API_HANDLE apiHandle,
        PCWSTR connection,
        DWORD flags,
        WSMAN_AUTHENTICATION_CREDENTIALS* serverAuthenticationCredentials,
        WSMAN_PROXY_INFO* proxyInfo,
        WSMAN_SESSION_HANDLE* session
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["apiHandle", "connection", "flags", "serverAuthenticationCredentials", "proxyInfo", "session"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCreateShell(jitter):
    """
    void WSManCreateShell(
        WSMAN_SESSION_HANDLE session,
        DWORD flags,
        PCWSTR resourceUri,
        WSMAN_SHELL_STARTUP_INFO* startupInfo,
        WSMAN_OPTION_SET* options,
        WSMAN_DATA* createXml,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_SHELL_HANDLE* shell
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "flags", "resourceUri", "startupInfo", "options", "createXml", "async", "shell"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManCreateShellEx(jitter):
    """
    void WSManCreateShellEx(
        WSMAN_SESSION_HANDLE session,
        DWORD flags,
        PCWSTR resourceUri,
        PCWSTR ShellID,
        WSMAN_SHELL_STARTUP_INFO* startupInfo,
        WSMAN_OPTION_SET* options,
        WSMAN_DATA* createXml,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_SHELL_HANDLE* shell
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "flags", "resourceUri", "ShellID", "startupInfo", "options", "createXml", "async", "shell"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManDeinitialize(jitter):
    """
    [ERROR_CODE] WSManDeinitialize(
        WSMAN_API_HANDLE apiHandle,
        DWORD flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["apiHandle", "flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManDisconnectShell(jitter):
    """
    void WSManDisconnectShell(
        WSMAN_SHELL_HANDLE shell,
        WSManShellFlag flags,
        WSMAN_SHELL_DISCONNECT_INFO* disconnectInfo,
        WSMAN_SHELL_ASYNC* async
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "disconnectInfo", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManInitialize(jitter):
    """
    [ERROR_CODE] WSManInitialize(
        [WSMAN_FLAG_REQUESTED_API_VERSION] flags,
        WSMAN_API_HANDLE* apiHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["flags", "apiHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManReceiveShellOutput(jitter):
    """
    void WSManReceiveShellOutput(
        WSMAN_SHELL_HANDLE shell,
        WSMAN_COMMAND_HANDLE command,
        DWORD flags,
        WSMAN_STREAM_ID_SET* desiredStreamSet,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_OPERATION_HANDLE* receiveOperation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shell", "command", "flags", "desiredStreamSet", "async", "receiveOperation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManReconnectShell(jitter):
    """
    void WSManReconnectShell(
        WSMAN_SHELL_HANDLE shell,
        DWORD flags,
        WSMAN_SHELL_ASYNC* async
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManReconnectShellCommand(jitter):
    """
    void WSManReconnectShellCommand(
        WSMAN_COMMAND_HANDLE commandHandle,
        DWORD flags,
        WSMAN_SHELL_ASYNC* async
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["commandHandle", "flags", "async"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManRunShellCommand(jitter):
    """
    void WSManRunShellCommand(
        WSMAN_SHELL_HANDLE shell,
        DWORD flags,
        PCWSTR commandLine,
        WSMAN_COMMAND_ARG_SET* args,
        WSMAN_OPTION_SET* options,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_COMMAND_HANDLE* command
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "commandLine", "args", "options", "async", "command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManRunShellCommandEx(jitter):
    """
    void WSManRunShellCommandEx(
        WSMAN_SHELL_HANDLE shell,
        DWORD flags,
        PCWSTR commandID,
        PCWSTR commandLine,
        WSMAN_COMMAND_ARG_SET* args,
        WSMAN_OPTION_SET* options,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_COMMAND_HANDLE* command
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shell", "flags", "commandID", "commandLine", "args", "options", "async", "command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManSendShellInput(jitter):
    """
    void WSManSendShellInput(
        WSMAN_SHELL_HANDLE shell,
        WSMAN_COMMAND_HANDLE command,
        DWORD flags,
        PCWSTR streamId,
        WSMAN_DATA* streamData,
        BOOL endOfStream,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_OPERATION_HANDLE* sendOperation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shell", "command", "flags", "streamId", "streamData", "endOfStream", "async", "sendOperation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManSignalShell(jitter):
    """
    void WSManSignalShell(
        WSMAN_SHELL_HANDLE shell,
        WSMAN_COMMAND_HANDLE command,
        DWORD flags,
        PCWSTR code,
        WSMAN_SHELL_ASYNC* async,
        WSMAN_OPERATION_HANDLE* signalOperation
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["shell", "command", "flags", "code", "async", "signalOperation"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManGetErrorMessage(jitter):
    """
    [ERROR_CODE] WSManGetErrorMessage(
        WSMAN_API_HANDLE apiHandle,
        DWORD flags,
        PCWSTR languageCode,
        DWORD errorCode,
        DWORD messageLength,
        PWSTR message,
        DWORD* messageLengthUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["apiHandle", "flags", "languageCode", "errorCode", "messageLength", "message", "messageLengthUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManGetSessionOptionAsDword(jitter):
    """
    [ERROR_CODE] WSManGetSessionOptionAsDword(
        WSMAN_SESSION_HANDLE session,
        WSManSessionOption option,
        DWORD* value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "option", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManGetSessionOptionAsString(jitter):
    """
    [ERROR_CODE] WSManGetSessionOptionAsString(
        WSMAN_SESSION_HANDLE session,
        WSManSessionOption option,
        DWORD stringLength,
        PWSTR string,
        DWORD* stringLengthUsed
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "option", "stringLength", "string", "stringLengthUsed"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wsmsvc_WSManSetSessionOption(jitter):
    """
    [ERROR_CODE] WSManSetSessionOption(
        WSMAN_SESSION_HANDLE session,
        WSManSessionOption option,
        WSMAN_DATA* data
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "option", "data"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
