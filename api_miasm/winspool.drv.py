
def winspool_AddJob(jitter):
    """"
    [Winspool.drv] BOOL AddJob(HANDLE hPrinter, DWORD Level, LPBYTE pData, DWORD cbBuf, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pData", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddMonitor(jitter):
    """"
    [Winspool.drv] BOOL AddMonitor(LPTSTR pName, DWORD Level, LPBYTE pMonitors)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pMonitors"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinter(jitter):
    """"
    [Winspool.drv] HANDLE AddPrinter(LPTSTR* pName, DWORD Level, LPBYTE pPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterConnection(jitter):
    """"
    [Winspool.drv] BOOL AddPrinterConnection(LPTSTR pName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterConnection2(jitter):
    """"
    [Winspool.drv] BOOL AddPrinterConnection2(HWND hWnd, LPCTSTR pszName, DWORD dwLevel, PVOID pConnectionInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "pszName", "dwLevel", "pConnectionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterDriver(jitter):
    """"
    [Winspool.drv] BOOL AddPrinterDriver(LPTSTR pName, DWORD Level, LPBYTE pDriverInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pDriverInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrinterDriverEx(jitter):
    """"
    [Winspool.drv] BOOL AddPrinterDriverEx(LPTSTR pName, DWORD Level, LPBYTE pDriverInfo, DWORD dwFileCopyFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pDriverInfo", "dwFileCopyFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrintProcessor(jitter):
    """"
    [Winspool.drv] BOOL AddPrintProcessor(LPTSTR pName, LPTSTR pEnvironment, LPTSTR pPathName, LPTSTR pPrintProcessorName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pPathName", "pPrintProcessorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPrintProvidor(jitter):
    """"
    [Winspool.drv] BOOL AddPrintProvidor(LPTSTR pName, DWORD Level, LPBYTE pProviderInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pProviderInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ConfigurePort(jitter):
    """"
    [Winspool.drv] BOOL ConfigurePort(LPTSTR pName, HWND hWnd, LPTSTR pPortName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "hWnd", "pPortName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeleteForm(jitter):
    """"
    [Winspool.drv] BOOL DeleteForm(HANDLE hPrinter, LPTSTR pFormName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pFormName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeleteMonitor(jitter):
    """"
    [Winspool.drv] BOOL DeleteMonitor(LPTSTR pName, LPTSTR pEnvironment, LPTSTR pMonitorName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pMonitorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePort(jitter):
    """"
    [Winspool.drv] BOOL DeletePort(LPTSTR pName, HWND hWnd, LPTSTR pPortName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "hWnd", "pPortName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterConnection(jitter):
    """"
    [Winspool.drv] BOOL DeletePrinterConnection(LPTSTR pName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterData(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] DeletePrinterData(HANDLE hPrinter, LPTSTR pValueName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pValueName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDataEx(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] DeletePrinterDataEx(HANDLE hPrinter, LPCTSTR pKeyName, LPCTSTR pValueName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pValueName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDriver(jitter):
    """"
    [Winspool.drv] BOOL DeletePrinterDriver(LPTSTR pName, LPTSTR pEnvironment, LPTSTR pDriverName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pDriverName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDriverEx(jitter):
    """"
    [Winspool.drv] BOOL DeletePrinterDriverEx(LPTSTR pName, LPTSTR pEnvironment, LPTSTR pDriverName, DWORD dwDeleteFlag, DWORD dwVersionFlag)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pDriverName", "dwDeleteFlag", "dwVersionFlag"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterKey(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] DeletePrinterKey(HANDLE hPrinter, LPCTSTR pKeyName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrintProcessor(jitter):
    """"
    [Winspool.drv] BOOL DeletePrintProcessor(LPTSTR pName, LPTSTR pEnvironment, LPTSTR pPrintProcessorName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pPrintProcessorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrintProvidor(jitter):
    """"
    [Winspool.drv] BOOL DeletePrintProvidor(LPTSTR pName, LPTSTR pEnvironment, LPTSTR pPrintProviderName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "pPrintProviderName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumForms(jitter):
    """"
    [Winspool.drv] BOOL EnumForms(HANDLE hPrinter, DWORD Level, LPBYTE pForm, DWORD cbBuf, LPDWORD pcbNeeded, LPDWORD pcReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pForm", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumJobs(jitter):
    """"
    [Winspool.drv] BOOL EnumJobs(HANDLE hPrinter, DWORD FirstJob, DWORD NoJobs, DWORD Level, LPBYTE pJob, DWORD cbBuf, LPDWORD pcbNeeded, LPDWORD pcReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "FirstJob", "NoJobs", "Level", "pJob", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumMonitors(jitter):
    """"
    [Winspool.drv] BOOL EnumMonitors(LPTSTR pName, DWORD Level, LPBYTE pMonitors, DWORD cbBuf, LPDWORD pcbNeeded, LPDWORD pcReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pMonitors", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPorts(jitter):
    """"
    [Winspool.drv] BOOL EnumPorts(LPTSTR pName, DWORD Level, LPBYTE pPorts, DWORD cbBuf, LPDWORD pcbNeeded, LPDWORD pcReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "Level", "pPorts", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinterData(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] EnumPrinterData(HANDLE hPrinter, DWORD dwIndex, LPTSTR pValueName, DWORD cbValueName, LPDWORD pcbValueName, LPDWORD pType, LPBYTE pData, DWORD cbData, LPDWORD pcbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "dwIndex", "pValueName", "cbValueName", "pcbValueName", "pType", "pData", "cbData", "pcbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinterDataEx(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] EnumPrinterDataEx(HANDLE hPrinter, LPCTSTR pKeyName, LPBYTE pEnumValues, DWORD cbEnumValues, LPDWORD pcbEnumValues, LPDWORD pnEnumValues)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pEnumValues", "cbEnumValues", "pcbEnumValues", "pnEnumValues"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinterDrivers(jitter):
    """"
    [Winspool.drv] BOOL EnumPrinterDrivers(LPTSTR pName, LPTSTR pEnvironment, DWORD Level, LPBYTE pDriverInfo, DWORD cbBuf, LPDWORD pcbNeeded, LPDWORD pcReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "Level", "pDriverInfo", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinterKey(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] EnumPrinterKey(HANDLE hPrinter, LPCTSTR pKeyName, LPTSTR pSubkey, DWORD cbSubkey, LPDWORD pcbSubkey)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pSubkey", "cbSubkey", "pcbSubkey"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrinters(jitter):
    """"
    [Winspool.drv] BOOL EnumPrinters([EnumPrintersFlags] Flags, LPTSTR Name, DWORD Level, LPBYTE pPrinterEnum, DWORD cbBuf, LPDWORD pcbNeeded, LPDWORD pcReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Flags", "Name", "Level", "pPrinterEnum", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrintProcessorDatatypes(jitter):
    """"
    [Winspool.drv] BOOL EnumPrintProcessorDatatypes(LPTSTR pName, LPTSTR pPrintProcessorName, DWORD Level, LPBYTE pDatatypes, DWORD cbBuf, LPDWORD pcbNeeded, LPDWORD pcReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pPrintProcessorName", "Level", "pDatatypes", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EnumPrintProcessors(jitter):
    """"
    [Winspool.drv] BOOL EnumPrintProcessors(LPTSTR pName, LPTSTR pEnvironment, DWORD Level, LPBYTE pPrintProcessorInfo, DWORD cbBuf, LPDWORD pcbNeeded, LPDWORD pcReturned)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "Level", "pPrintProcessorInfo", "cbBuf", "pcbNeeded", "pcReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FlushPrinter(jitter):
    """"
    [Winspool.drv] BOOL FlushPrinter(HANDLE hPrinter, LPVOID pBuf, DWORD cbBuf, LPDWORD pcWritten, DWORD cSleep)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pBuf", "cbBuf", "pcWritten", "cSleep"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetForm(jitter):
    """"
    [Winspool.drv] BOOL GetForm(HANDLE hPrinter, LPTSTR pFormName, DWORD Level, LPBYTE pForm, DWORD cbBuf, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pFormName", "Level", "pForm", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetJob(jitter):
    """"
    [Winspool.drv] BOOL GetJob(HANDLE hPrinter, DWORD JobId, DWORD Level, LPBYTE pJob, DWORD cbBuf, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "JobId", "Level", "pJob", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinter(jitter):
    """"
    [Winspool.drv] BOOL GetPrinter(HANDLE hPrinter, DWORD Level, LPBYTE pPrinter, DWORD cbBuf, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pPrinter", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterData(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] GetPrinterData(HANDLE hPrinter, LPTSTR pValueName, [RegType*] pType, LPBYTE pData, DWORD nSize, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pValueName", "pType", "pData", "nSize", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDataEx(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] GetPrinterDataEx(HANDLE hPrinter, LPCTSTR pKeyName, LPCTSTR pValueName, [RegType*] pType, LPBYTE pData, DWORD nSize, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pValueName", "pType", "pData", "nSize", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDriver(jitter):
    """"
    [Winspool.drv] BOOL GetPrinterDriver(HANDLE hPrinter, LPTSTR pEnvironment, DWORD Level, LPBYTE pDriverInfo, DWORD cbBuf, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pEnvironment", "Level", "pDriverInfo", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDriverDirectory(jitter):
    """"
    [Winspool.drv] BOOL GetPrinterDriverDirectory(LPTSTR pName, LPTSTR pEnvironment, DWORD Level, LPWSTR pDriverDirectory, DWORD cbBuf, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "Level", "pDriverDirectory", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrintProcessorDirectory(jitter):
    """"
    [Winspool.drv] BOOL GetPrintProcessorDirectory(LPTSTR pName, LPTSTR pEnvironment, DWORD Level, LPBYTE pPrintProcessorInfo, DWORD cbBuf, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pEnvironment", "Level", "pPrintProcessorInfo", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_OpenPrinter(jitter):
    """"
    [Winspool.drv] BOOL OpenPrinter(LPTSTR pPrinterName, LPHANDLE phPrinter, LPPRINTER_DEFAULTS pDefault)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPrinterName", "phPrinter", "pDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ResetPrinter(jitter):
    """"
    [Winspool.drv] BOOL ResetPrinter(HANDLE hPrinter, LPPRINTER_DEFAULTS pDefault)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pDefault"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_StartDocPrinter(jitter):
    """"
    [Winspool.drv] DWORD StartDocPrinter(HANDLE hPrinter, DWORD Level, LPBYTE pDocInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pDocInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetForm(jitter):
    """"
    [Winspool.drv] BOOL SetForm(HANDLE hPrinter, LPTSTR pFormName, DWORD Level, LPTSTR pForm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pFormName", "Level", "pForm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetJob(jitter):
    """"
    [Winspool.drv] BOOL SetJob(HANDLE hPrinter, DWORD JobId, DWORD Level, LPBYTE pJob, [JobControl] Command)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "JobId", "Level", "pJob", "Command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetPort(jitter):
    """"
    [Winspool.drv] BOOL SetPort(LPTSTR pName, LPTSTR pPortName, DWORD dwLevel, LPBYTE pPortInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pPortName", "dwLevel", "pPortInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetPrinter(jitter):
    """"
    [Winspool.drv] BOOL SetPrinter(HANDLE hPrinter, DWORD Level, LPBYTE pPrinter, [PrinterControl] Command)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pPrinter", "Command"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetPrinterData(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] SetPrinterData(HANDLE hPrinter, LPTSTR pValueName, [RegType] Type, LPBYTE pData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pValueName", "Type", "pData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetPrinterDataEx(jitter):
    """"
    [Winspool.drv] [ERROR_CODE] SetPrinterDataEx(HANDLE hPrinter, LPCTSTR pKeyName, LPCTSTR pValueName, [RegType] Type, LPBYTE pData, DWORD cbData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pKeyName", "pValueName", "Type", "pData", "cbData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeviceCapabilities(jitter):
    """"
    [Winspool.drv] DWORD DeviceCapabilities(LPCTSTR pDevice, LPCTSTR pPort, [DeviceCapability] fwCapability, LPTSTR pOutput, const DEVMODE* pDevMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pDevice", "pPort", "fwCapability", "pOutput", "pDevMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_CorePrinterDriverInstalled(jitter):
    """"
    [Winspool.drv] HRESULT CorePrinterDriverInstalled(LPCTSTR pszServer, LPCTSTR pszEnvironment, GUID CoreDriverGUID, FILETIME ftDriverDate, DWORDLONG dwlDriverVersion, BOOL* pbDriverInstalled)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszEnvironment", "CoreDriverGUID", "ftDriverDate", "dwlDriverVersion", "pbDriverInstalled"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinterDriverPackage(jitter):
    """"
    [Winspool.drv] HRESULT DeletePrinterDriverPackage(LPCTSTR pszServer, LPCTSTR pszInfPath, LPCTSTR pszEnvironment)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszInfPath", "pszEnvironment"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetCorePrinterDrivers(jitter):
    """"
    [Winspool.drv] HRESULT GetCorePrinterDrivers(LPCTSTR pszServer, LPCTSTR pszEnvironment, LPCTSTR pszzCoreDriverDependencies, DWORD cCorePrinterDrivers, PCORE_PRINTER_DRIVER pCorePrinterDrivers)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszEnvironment", "pszzCoreDriverDependencies", "cCorePrinterDrivers", "pCorePrinterDrivers"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDriverPackagePath(jitter):
    """"
    [Winspool.drv] HRESULT GetPrinterDriverPackagePath(LPCTSTR pszServer, LPCTSTR pszEnvironment, LPCTSTR pszLanguage, LPCTSTR pszPackageID, LPTSTR pszDriverPackageCab, DWORD cchDriverPackageCab, LPDWORD pcchRequiredSize)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszEnvironment", "pszLanguage", "pszPackageID", "pszDriverPackageCab", "cchDriverPackageCab", "pcchRequiredSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_InstallPrinterDriverFromPackage(jitter):
    """"
    [Winspool.drv] HRESULT InstallPrinterDriverFromPackage(LPCTSTR pszServer, LPCTSTR pszInfPath, LPCTSTR pszDriverName, LPCTSTR pszEnvironment, DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszInfPath", "pszDriverName", "pszEnvironment", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_UploadPrinterDriverPackage(jitter):
    """"
    [Winspool.drv] HRESULT UploadPrinterDriverPackage(LPCTSTR pszServer, LPCTSTR pszInfPath, LPCTSTR pszEnvironment, DWORD dwFlags, HWND hwnd, LPTSTR pszDestInfPath, PULONG pcchDestInfPath)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszServer", "pszInfPath", "pszEnvironment", "dwFlags", "hwnd", "pszDestInfPath", "pcchDestInfPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AbortPrinter(jitter):
    """"
    [Winspool.drv] BOOL AbortPrinter(HANDLE hPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddForm(jitter):
    """"
    [Winspool.drv] BOOL AddForm(HANDLE hPrinter, DWORD Level, LPBYTE pForm)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "Level", "pForm"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AddPort(jitter):
    """"
    [Winspool.drv] BOOL AddPort(LPTSTR pName, HWND hWnd, LPTSTR pMonitorName)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "hWnd", "pMonitorName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_AdvancedDocumentProperties(jitter):
    """"
    [Winspool.drv] LONG AdvancedDocumentProperties(HWND hWnd, HANDLE hPrinter, LPTSTR pDeviceName, PDEVMODE pDevModeOutput, PDEVMODE pDevModeInput)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hPrinter", "pDeviceName", "pDevModeOutput", "pDevModeInput"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ClosePrinter(jitter):
    """"
    [Winspool.drv] BOOL ClosePrinter(HANDLE hPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ConnectToPrinterDlg(jitter):
    """"
    [Winspool.drv] HANDLE ConnectToPrinterDlg(HWND hwnd, DWORD Flags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hwnd", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_CreatePrintAsyncNotifyChannel(jitter):
    """"
    [Winspool.drv] HRESULT CreatePrintAsyncNotifyChannel(LPCWSTR pName, PrintAsyncNotificationType* pSchema, PrintAsyncNotifyUserFilter filter, PrintAsyncNotifyConversationStyle directionality, IPrintAsyncNotifyCallback* pCallback, IPrintAsyncNotifyChannel** ppChannel)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pSchema", "filter", "directionality", "pCallback", "ppChannel"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DeletePrinter(jitter):
    """"
    [Winspool.drv] BOOL DeletePrinter(HANDLE hPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_DocumentProperties(jitter):
    """"
    [Winspool.drv] LONG DocumentProperties(HWND hWnd, HANDLE hPrinter, LPTSTR pDeviceName, PDEVMODE pDevModeOutput, PDEVMODE pDevModeInput, [DocumentMode] fMode)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hPrinter", "pDeviceName", "pDevModeOutput", "pDevModeInput", "fMode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EndDocPrinter(jitter):
    """"
    [Winspool.drv] BOOL EndDocPrinter(HANDLE hPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_EndPagePrinter(jitter):
    """"
    [Winspool.drv] BOOL EndPagePrinter(HANDLE hPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FindClosePrinterChangeNotification(jitter):
    """"
    [Winspool.drv] BOOL FindClosePrinterChangeNotification(HANDLE hChange)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChange"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FindFirstPrinterChangeNotification(jitter):
    """"
    [Winspool.drv] HANDLE FindFirstPrinterChangeNotification(HANDLE hPrinter, [PrinterChangeFlags] fdwFilter, DWORD fdwOptions, PPRINTER_NOTIFY_OPTIONS pPrinterNotifyOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "fdwFilter", "fdwOptions", "pPrinterNotifyOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FindNextPrinterChangeNotification(jitter):
    """"
    [Winspool.drv] BOOL FindNextPrinterChangeNotification(HANDLE hChange, [PrinterChangeFlags*] pdwChange, PPRINTER_NOTIFY_OPTIONS pPrinterNotifyOptions, LPVOID* ppPrinterNotifyInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hChange", "pdwChange", "pPrinterNotifyOptions", "ppPrinterNotifyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_FreePrinterNotifyInfo(jitter):
    """"
    [Winspool.drv] BOOL FreePrinterNotifyInfo(PPRINTER_NOTIFY_INFO pPrinterNotifyInfo)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPrinterNotifyInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetDefaultPrinter(jitter):
    """"
    [Winspool.drv] BOOL GetDefaultPrinter(LPTSTR pszBuffer, LPDWORD pcchBuffer)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszBuffer", "pcchBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_GetPrinterDriver2(jitter):
    """"
    [Winspool.drv] BOOL GetPrinterDriver2(HWND hWnd, HANDLE hPrinter, LPTSTR pEnvironment, DWORD Level, LPBYTE pDriverInfo, DWORD cbBuf, LPDWORD pcbNeeded)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hPrinter", "pEnvironment", "Level", "pDriverInfo", "cbBuf", "pcbNeeded"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_OpenPrinter2(jitter):
    """"
    [Winspool.drv] BOOL OpenPrinter2(LPCTSTR pPrinterName, LPHANDLE phPrinter, LPPRINTER_DEFAULTS pDefault, PPRINTER_OPTIONS pOptions)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPrinterName", "phPrinter", "pDefault", "pOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_PrinterProperties(jitter):
    """"
    [Winspool.drv] BOOL PrinterProperties(HWND hWnd, HANDLE hPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hWnd", "hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ReadPrinter(jitter):
    """"
    [Winspool.drv] BOOL ReadPrinter(HANDLE hPrinter, LPVOID pBuf, DWORD cbBuf, LPDWORD pNoBytesRead)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pBuf", "cbBuf", "pNoBytesRead"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_RegisterForPrintAsyncNotifications(jitter):
    """"
    [Winspool.drv] HRESULT RegisterForPrintAsyncNotifications(LPCWSTR pName, PrintAsyncNotificationType* pSchema, PrintAsyncNotifyUserFilter filter, PrintAsyncNotifyConversationStyle directionality, IPrintAsyncNotifyCallback* pCallback, HANDLE* pRegistrationHandler)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pName", "pSchema", "filter", "directionality", "pCallback", "pRegistrationHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ReportJobProcessingProgress(jitter):
    """"
    [Winspool.drv] HRESULT ReportJobProcessingProgress(HANDLE printerHandle, ULONG jobId, EPrintXPSJobOperation jobOperation, EPrintXPSJobProgress jobProgress)
    """"
    ret_ad, args = jitter.func_args_stdcall(["printerHandle", "jobId", "jobOperation", "jobProgress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_ScheduleJob(jitter):
    """"
    [Winspool.drv] BOOL ScheduleJob(HANDLE hPrinter, DWORD dwJobID)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "dwJobID"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_SetDefaultPrinter(jitter):
    """"
    [Winspool.drv] BOOL SetDefaultPrinter(LPCTSTR pszPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pszPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_StartPagePrinter(jitter):
    """"
    [Winspool.drv] BOOL StartPagePrinter(HANDLE hPrinter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_UnRegisterForPrintAsyncNotifications(jitter):
    """"
    [Winspool.drv] HRESULT UnRegisterForPrintAsyncNotifications(HANDLE hRegistrationHandler)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hRegistrationHandler"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def winspool_WritePrinter(jitter):
    """"
    [Winspool.drv] BOOL WritePrinter(HANDLE hPrinter, LPVOID pBuf, DWORD cbBuf, LPDWORD pcWritten)
    """"
    ret_ad, args = jitter.func_args_stdcall(["hPrinter", "pBuf", "cbBuf", "pcWritten"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
