DNS_PROXY_INFORMATION_TYPE = {
    "DNS_PROXY_INFORMATION_DIRECT": 0,
    "DNS_PROXY_INFORMATION_DEFAULT_SETTINGS": 1,
    "DNS_PROXY_INFORMATION_PROXY_NAME": 2,
    "DNS_PROXY_INFORMATION_DOES_NOT_EXIST": 3,
}
DNS_FREE_TYPE = {
    "DnsFreeFlat": 0,
    "DnsFreeRecordList": 1,
    "DnsFreeParsedMessageFields": 2,
}
_DnsRecordType_ = {
    "DNS_TYPE_A": 0x0001,
    "DNS_TYPE_NS": 0x0002,
    "DNS_TYPE_MD": 0x0003,
    "DNS_TYPE_MF": 0x0004,
    "DNS_TYPE_CNAME": 0x0005,
    "DNS_TYPE_SOA": 0x0006,
    "DNS_TYPE_MB": 0x0007,
    "DNS_TYPE_MG": 0x0008,
    "DNS_TYPE_MR": 0x0009,
    "DNS_TYPE_NULL": 0x000a,
    "DNS_TYPE_WKS": 0x000b,
    "DNS_TYPE_PTR": 0x000c,
    "DNS_TYPE_HINFO": 0x000d,
    "DNS_TYPE_MINFO": 0x000e,
    "DNS_TYPE_MX": 0x000f,
    "DNS_TYPE_TEXT": 0x0010,
    "DNS_TYPE_RP": 0x0011,
    "DNS_TYPE_AFSDB": 0x0012,
    "DNS_TYPE_X25": 0x0013,
    "DNS_TYPE_ISDN": 0x0014,
    "DNS_TYPE_RT": 0x0015,
    "DNS_TYPE_NSAP": 0x0016,
    "DNS_TYPE_NSAPPTR": 0x0017,
    "DNS_TYPE_SIG": 0x0018,
    "DNS_TYPE_KEY": 0x0019,
    "DNS_TYPE_PX": 0x001a,
    "DNS_TYPE_GPOS": 0x001b,
    "DNS_TYPE_AAAA": 0x001c,
    "DNS_TYPE_LOC": 0x001d,
    "DNS_TYPE_NXT": 0x001e,
    "DNS_TYPE_EID": 0x001f,
    "DNS_TYPE_NIMLOC": 0x0020,
    "DNS_TYPE_SRV": 0x0021,
    "DNS_TYPE_ATMA": 0x0022,
    "DNS_TYPE_NAPTR": 0x0023,
    "DNS_TYPE_KX": 0x0024,
    "DNS_TYPE_CERT": 0x0025,
    "DNS_TYPE_A6": 0x0026,
    "DNS_TYPE_DNAME": 0x0027,
    "DNS_TYPE_SINK": 0x0028,
    "DNS_TYPE_OPT": 0x0029,
    "DNS_TYPE_UINFO": 0x0064,
    "DNS_TYPE_UID": 0x0065,
    "DNS_TYPE_GID": 0x0066,
    "DNS_TYPE_UNSPEC": 0x0067,
    "DNS_TYPE_ADDRS": 0x00f8,
    "DNS_TYPE_TKEY": 0x00f9,
    "DNS_TYPE_TSIG": 0x00fa,
    "DNS_TYPE_IXFR": 0x00fb,
    "DNS_TYPE_AXFR": 0x00fc,
    "DNS_TYPE_MAILB": 0x00fd,
    "DNS_TYPE_MAILA": 0x00fe,
    "DNS_TYPE_ALL": 0x00ff,
    "DNS_TYPE_ANY": 0x00ff,
    "DNS_TYPE_WINS": 0xff01,
    "DNS_TYPE_WINSR": 0xff02,
    "DNS_TYPE_NBSTAT": 0xff02,
}
DNS_NAME_FORMAT = {
    "DnsNameDomain": 0,
    "DnsNameDomainLabel": 1,
    "DnsNameHostnameFull": 2,
    "DnsNameHostnameLabel": 3,
    "DnsNameWildcard": 4,
    "DnsNameSrvRecord": 5,
    "DnsNameValidateTld": 6,
}
DNS_CONFIG_TYPE = {
    "DnsConfigPrimaryDomainName_W": 0,
    "DnsConfigPrimaryDomainName_A": 1,
    "DnsConfigPrimaryDomainName_UTF8": 2,
    "DnsConfigAdapterDomainName_W": 3,
    "DnsConfigAdapterDomainName_A": 4,
    "DnsConfigAdapterDomainName_UTF8": 5,
    "DnsConfigDnsServerList": 6,
    "DnsConfigSearchList": 7,
    "DnsConfigAdapterInfo": 8,
    "DnsConfigPrimaryHostNameRegistrationEnabled": 9,
    "DnsConfigAdapterHostNameRegistrationEnabled": 10,
    "DnsConfigAddressRegistrationMaxCount": 11,
    "DnsConfigHostName_W": 12,
    "DnsConfigHostName_A": 13,
    "DnsConfigHostName_UTF8": 14,
    "DnsConfigFullHostName_W": 15,
    "DnsConfigFullHostName_A": 16,
    "DnsConfigFullHostName_UTF8": 17,
}
DNS_CHARSET = {
    "DnsCharSetUnknown": 0,
    "DnsCharSetUnicode": 1,
    "DnsCharSetUtf8": 2,
    "DnsCharSetAnsi": 3,
}

def dnsapi_DnsAcquireContextHandle_(jitter, get_str, set_str):
    """
    DNS_STATUS DnsAcquireContextHandle_(
        BOOL CredentialFlags,
        PVOID Credentials,
        PHANDLE pContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["CredentialFlags", "Credentials", "pContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsAcquireContextHandle_A(jitter):
    dnsapi_DnsAcquireContextHandle_(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dnsapi_DnsAcquireContextHandle_W(jitter):
    dnsapi_DnsAcquireContextHandle_(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dnsapi_DnsExtractRecordsFromMessage_W(jitter):
    """
    DNS_STATUS DnsExtractRecordsFromMessage_W(
        PDNS_MESSAGE_BUFFER pDnsBuffer,
        WORD wMessageLength,
        PDNS_RECORD* ppRecord
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDnsBuffer", "wMessageLength", "ppRecord"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsFree(jitter):
    """
    void DnsFree(
        PVOID pData,
        DNS_FREE_TYPE FreeType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pData", "FreeType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsFreeProxyName(jitter):
    """
    void DnsFreeProxyName(
        PWSTR proxyName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["proxyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsGetProxyInformation(jitter):
    """
    DNS_STATUS DnsGetProxyInformation(
        PCWSTR hostName,
        DNS_PROXY_INFORMATION* proxyInformation,
        DNS_PROXY_INFORMATION* defaultProxyInformation,
        DNS_PROXY_COMPLETION_ROUTINE completionRoutine,
        void* completionContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hostName", "proxyInformation", "defaultProxyInformation", "completionRoutine", "completionContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsModifyRecordsInSet_(jitter, get_str, set_str):
    """
    DNS_STATUS DnsModifyRecordsInSet_(
        PDNS_RECORD pAddRecords,
        PDNS_RECORD pDeleteRecords,
        DWORD Options,
        HANDLE hContext,
        PVOID pExtraList,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAddRecords", "pDeleteRecords", "Options", "hContext", "pExtraList", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsModifyRecordsInSet_A(jitter):
    dnsapi_DnsModifyRecordsInSet_(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dnsapi_DnsModifyRecordsInSet_W(jitter):
    dnsapi_DnsModifyRecordsInSet_(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dnsapi_DnsNameCompare_(jitter, get_str, set_str):
    """
    BOOL DnsNameCompare_(
        PCTSTR pName1,
        PCTSTR pName2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pName1", "pName2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsNameCompare_A(jitter):
    dnsapi_DnsNameCompare_(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dnsapi_DnsNameCompare_W(jitter):
    dnsapi_DnsNameCompare_(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dnsapi_DnsQuery_(jitter, get_str, set_str):
    """
    DNS_STATUS DnsQuery_(
        PCTSTR lpstrName,
        [DnsRecordType] wType,
        [DnsQueryOptions] Options,
        PVOID pExtra,
        PDNS_RECORD* ppQueryResultsSet,
        PVOID* pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpstrName", "wType", "Options", "pExtra", "ppQueryResultsSet", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsQuery_A(jitter):
    dnsapi_DnsQuery_(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dnsapi_DnsQuery_W(jitter):
    dnsapi_DnsQuery_(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dnsapi_DnsQueryConfig(jitter):
    """
    DNS_STATUS DnsQueryConfig(
        DNS_CONFIG_TYPE Config,
        [DnsConfigFlags] Flag,
        PCWSTR pwsAdapterName,
        PVOID pReserved,
        PVOID pBuffer,
        PDWORD pBufferLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Config", "Flag", "pwsAdapterName", "pReserved", "pBuffer", "pBufferLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordCompare(jitter):
    """
    BOOL DnsRecordCompare(
        PDNS_RECORD pRecord1,
        PDNS_RECORD pRecord2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecord1", "pRecord2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordCopyEx(jitter):
    """
    PDNS_RECORD DnsRecordCopyEx(
        PDNS_RECORD pRecord,
        DNS_CHARSET CharSetIn,
        DNS_CHARSET CharSetOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecord", "CharSetIn", "CharSetOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordListFree(jitter):
    """
    void DnsRecordListFree(
        PDNS_RECORD pRecordList,
        DNS_FREE_TYPE FreeType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecordList", "FreeType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordSetCompare(jitter):
    """
    BOOL DnsRecordSetCompare(
        PDNS_RECORD pRR1,
        PDNS_RECORD pRR2,
        PDNS_RECORD* ppDiff1,
        PDNS_RECORD* ppDiff2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRR1", "pRR2", "ppDiff1", "ppDiff2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordSetCopyEx(jitter):
    """
    PDNS_RECORD DnsRecordSetCopyEx(
        PDNS_RECORD pRecordSet,
        DNS_CHARSET CharSetIn,
        DNS_CHARSET CharSetOut
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRecordSet", "CharSetIn", "CharSetOut"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsRecordSetDetach(jitter):
    """
    PDNS_RECORD DnsRecordSetDetach(
        PDNS_RECORD pRR
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRR"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsReleaseContextHandle(jitter):
    """
    void DnsReleaseContextHandle(
        HANDLE ContextHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ContextHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsReplaceRecordSet(jitter, get_str, set_str):
    """
    DNS_STATUS DnsReplaceRecordSet(
        PDNS_RECORD pNewSet,
        [DnsUpdateFlags] Options,
        HANDLE hContext,
        PVOID pExtraInfo,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pNewSet", "Options", "hContext", "pExtraInfo", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsReplaceRecordSetA(jitter):
    dnsapi_DnsReplaceRecordSet(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dnsapi_DnsReplaceRecordSetW(jitter):
    dnsapi_DnsReplaceRecordSet(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dnsapi_DnsValidateName_(jitter, get_str, set_str):
    """
    DNS_STATUS DnsValidateName_(
        PCTSTR pszName,
        DNS_NAME_FORMAT Format
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pszName", "Format"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsValidateName_A(jitter):
    dnsapi_DnsValidateName_(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def dnsapi_DnsValidateName_W(jitter):
    dnsapi_DnsValidateName_(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def dnsapi_DnsWriteQuestionToBuffer_W(jitter):
    """
    BOOL DnsWriteQuestionToBuffer_W(
        PDNS_MESSAGE_BUFFER pDnsBuffer,
        PDWORD pdwBufferSize,
        PCWSTR pszName,
        [DnsRecordType] wType,
        WORD Xid,
        BOOL fRecursionDesired
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDnsBuffer", "pdwBufferSize", "pszName", "wType", "Xid", "fRecursionDesired"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsCancelQuery(jitter):
    """
    DNS_STATUS DnsCancelQuery(
        PDNS_QUERY_CANCEL pCancelHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pCancelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def dnsapi_DnsQueryEx(jitter):
    """
    DNS_STATUS DnsQueryEx(
        PDNS_QUERY_REQUEST pQueryRequest,
        PDNS_QUERY_RESULT pQueryResults,
        PDNS_QUERY_CANCEL pCancelHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pQueryRequest", "pQueryResults", "pCancelHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
