###### Enums ######

###################

###### Types ######

###################

###### Functions ######

def mgmtapi_SnmpMgrClose(jitter):
    """
    BOOL SnmpMgrClose(
        LPSNMP_MGR_SESSION session
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mgmtapi_SnmpMgrCtl(jitter):
    """
    BOOL SnmpMgrCtl(
        LPSNMP_MGR_SESSION session,
        DWORD dwCtlCode,
        LPVOID lpvInBuffer,
        DWORD cbInBuffer,
        LPVOID lpvOutBuffer,
        DWORD cbOutBuffer,
        LPDWORD lpcbBytesReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "dwCtlCode", "lpvInBuffer", "cbInBuffer", "lpvOutBuffer", "cbOutBuffer", "lpcbBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mgmtapi_SnmpMgrGetTrap(jitter):
    """
    BOOL SnmpMgrGetTrap(
        AsnObjectIdentifier* enterprise,
        AsnNetworkAddress* IPAddress,
        AsnInteger* genericTrap,
        AsnInteger* specificTrap,
        AsnTimeticks* timeStamp,
        SnmpVarBindList* variableBindings
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["enterprise", "IPAddress", "genericTrap", "specificTrap", "timeStamp", "variableBindings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mgmtapi_SnmpMgrGetTrapEx(jitter):
    """
    BOOL SnmpMgrGetTrapEx(
        AsnObjectIdentifier* enterprise,
        AsnNetworkAddress* agentAddress,
        AsnNetworkAddress* sourceAddress,
        AsnInteger* genericTrap,
        AsnInteger* specificTrap,
        AsnOctetString* community,
        AsnTimeticks* timeStamp,
        SnmpVarBindList* variableBindings
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["enterprise", "agentAddress", "sourceAddress", "genericTrap", "specificTrap", "community", "timeStamp", "variableBindings"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mgmtapi_SnmpMgrOidToStr(jitter):
    """
    BOOL SnmpMgrOidToStr(
        AsnObjectIdentifier* oid,
        LPSTR* string
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["oid", "string"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mgmtapi_SnmpMgrOpen(jitter):
    """
    LPSNMP_MGR_SESSION SnmpMgrOpen(
        LPSTR lpAgentAddress,
        LPSTR lpAgentCommunity,
        INT nTimeOut,
        INT nRetries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpAgentAddress", "lpAgentCommunity", "nTimeOut", "nRetries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mgmtapi_SnmpMgrRequest(jitter):
    """
    SNMPAPI SnmpMgrRequest(
        LPSNMP_MGR_SESSION session,
        BYTE requestType,
        SnmpVarBindList* variableBindings,
        AsnInteger* errorStatus,
        AsnInteger* errorIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["session", "requestType", "variableBindings", "errorStatus", "errorIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mgmtapi_SnmpMgrStrToOid(jitter):
    """
    BOOL SnmpMgrStrToOid(
        LPSTR string,
        AsnObjectIdentifier* oid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["string", "oid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def mgmtapi_SnmpMgrTrapListen(jitter):
    """
    BOOL SnmpMgrTrapListen(
        HANDLE* phTrapAvailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["phTrapAvailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
