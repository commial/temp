
def snmpapi_SnmpSvcGetUptime(jitter):
    """
    DWORD SnmpSvcGetUptime()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpSvcSetLogLevel(jitter):
    """
    void SnmpSvcSetLogLevel(
        INT nLogLevel
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nLogLevel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpSvcSetLogType(jitter):
    """
    void SnmpSvcSetLogType(
        INT nLogType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nLogType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilAsnAnyCpy(jitter):
    """
    SNMPAPI SnmpUtilAsnAnyCpy(
        AsnAny* pAnyDst,
        AsnAny* pAnySrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAnyDst", "pAnySrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilAsnAnyFree(jitter):
    """
    void SnmpUtilAsnAnyFree(
        AsnAny* pAny
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilDbgPrint(jitter):
    """
    void SnmpUtilDbgPrint(
        INT nLogLevel,
        LPSTR szFormat
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nLogLevel", "szFormat"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilIdsToA(jitter):
    """
    LPSTR SnmpUtilIdsToA(
        UINT* Ids,
        UINT IdLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Ids", "IdLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilMemAlloc(jitter):
    """
    LPVOID SnmpUtilMemAlloc(
        UINT nBytes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilMemFree(jitter):
    """
    void SnmpUtilMemFree(
        LPVOID pMem
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMem"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilMemReAlloc(jitter):
    """
    LPVOID SnmpUtilMemReAlloc(
        LPVOID pMem,
        UINT nBytes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMem", "nBytes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOctetsCmp(jitter):
    """
    SNMPAPI SnmpUtilOctetsCmp(
        AsnOctetString* pOctets1,
        AsnOctetString* pOctets2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOctets1", "pOctets2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOctetsCpy(jitter):
    """
    SNMPAPI SnmpUtilOctetsCpy(
        AsnOctetString* pOctetsDst,
        AsnOctetString* pOctetsSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOctetsDst", "pOctetsSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOctetsFree(jitter):
    """
    void SnmpUtilOctetsFree(
        AsnOctetString* pOctets
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOctets"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOctetsNCmp(jitter):
    """
    SNMPAPI SnmpUtilOctetsNCmp(
        AsnOctetString* pOctets1,
        AsnOctetString* pOctets2,
        UINT nChars
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOctets1", "pOctets2", "nChars"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidAppend(jitter):
    """
    SNMPAPI SnmpUtilOidAppend(
        AsnObjectIdentifier* pOidDst,
        AsnObjectIdentifier* pOidSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOidDst", "pOidSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidCmp(jitter):
    """
    SNMPAPI SnmpUtilOidCmp(
        AsnObjectIdentifier* pOid1,
        AsnObjectIdentifier* pOid2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOid1", "pOid2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidCpy(jitter):
    """
    SNMPAPI SnmpUtilOidCpy(
        AsnObjectIdentifier* pOidDst,
        AsnObjectIdentifier* pOidSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOidDst", "pOidSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidFree(jitter):
    """
    void SnmpUtilOidFree(
        AsnObjectIdentifier* pOid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidNCmp(jitter):
    """
    SNMPAPI SnmpUtilOidNCmp(
        AsnObjectIdentifier* pOid1,
        AsnObjectIdentifier* pOid2,
        UINT nSubIds
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOid1", "pOid2", "nSubIds"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilOidToA(jitter):
    """
    LPSTR SnmpUtilOidToA(
        AsnObjectIdentifier* Oid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Oid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilPrintAsnAny(jitter):
    """
    void SnmpUtilPrintAsnAny(
        AsnAny* pAny
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAny"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilPrintOid(jitter):
    """
    void SnmpUtilPrintOid(
        AsnObjectIdentifier* Oid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Oid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilVarBindCpy(jitter):
    """
    SNMPAPI SnmpUtilVarBindCpy(
        SnmpVarBind* pVbDst,
        SnmpVarBind* pVbSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pVbDst", "pVbSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilVarBindListCpy(jitter):
    """
    SNMPAPI SnmpUtilVarBindListCpy(
        SnmpVarBindList* pVblDst,
        SnmpVarBindList* pVblSrc
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pVblDst", "pVblSrc"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilVarBindFree(jitter):
    """
    void SnmpUtilVarBindFree(
        SnmpVarBind* pVb
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pVb"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def snmpapi_SnmpUtilVarBindListFree(jitter):
    """
    void SnmpUtilVarBindListFree(
        SnmpVarBindList* pVbl
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pVbl"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
