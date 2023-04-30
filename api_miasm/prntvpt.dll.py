
def prntvpt_PTConvertPrintTicketToDevMode(jitter):
    """"
    [Prntvpt.dll] HRESULT PTConvertPrintTicketToDevMode(HPTPROVIDER hProvider, IStream* pPrintTicket, EDefaultDevmodeType baseDevmodeType, EPrintTicketScope scope, ULONG* pcbDevmode, PDEVMODE* ppDevmode, BSTR* pbstrErrorMessage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pPrintTicket", "baseDevmodeType", "scope", "pcbDevmode", "ppDevmode", "pbstrErrorMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def prntvpt_PTConvertDevModeToPrintTicket(jitter):
    """"
    [Prntvpt.dll] HRESULT PTConvertDevModeToPrintTicket(HPTPROVIDER hProvider, ULONG cbDevmode, PDEVMODE pDevmode, EPrintTicketScope scope, IStream* pPrintTicket)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "cbDevmode", "pDevmode", "scope", "pPrintTicket"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def prntvpt_PTReleaseMemory(jitter):
    """"
    [Prntvpt.dll] HRESULT PTReleaseMemory(PVOID pBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def prntvpt_PTMergeAndValidatePrintTicket(jitter):
    """"
    [Prntvpt.dll] HRESULT PTMergeAndValidatePrintTicket(HPTPROVIDER hProvider, IStream* pBaseTicket, IStream* pDeltaTicket, EPrintTicketScope scope, IStream* pResultTicket, BSTR* pbstrErrorMessage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pBaseTicket", "pDeltaTicket", "scope", "pResultTicket", "pbstrErrorMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def prntvpt_PTGetPrintCapabilities(jitter):
    """"
    [Prntvpt.dll] HRESULT PTGetPrintCapabilities(HPTPROVIDER hProvider, IStream* pPrintTicket, IStream* pCapabilities, BSTR* pbstrErrorMessage)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider", "pPrintTicket", "pCapabilities", "pbstrErrorMessage"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def prntvpt_PTOpenProvider(jitter):
    """"
    [Prntvpt.dll] HRESULT PTOpenProvider(PCWSTR pszPrinterName, DWORD version, HPTPROVIDER* phProvider)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPrinterName", "version", "phProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def prntvpt_PTOpenProviderEx(jitter):
    """"
    [Prntvpt.dll] HRESULT PTOpenProviderEx(PCWSTR pszPrinterName, DWORD maxVersion, DWORD prefVersion, HPTPROVIDER* phProvider, DWORD* usedVersion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPrinterName", "maxVersion", "prefVersion", "phProvider", "usedVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def prntvpt_PTCloseProvider(jitter):
    """"
    [Prntvpt.dll] HRESULT PTCloseProvider(HPTPROVIDER hProvider)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hProvider"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def prntvpt_PTQuerySchemaVersionSupport(jitter):
    """"
    [Prntvpt.dll] HRESULT PTQuerySchemaVersionSupport(PCWSTR pszPrinterName, DWORD* pMaxVersion)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPrinterName", "pMaxVersion"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
