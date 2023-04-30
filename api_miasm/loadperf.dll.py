
def loadperf_LoadPerfCounterTextStrings(jitter):
    """"
    [Loadperf.dll] [ERROR_CODE] LoadPerfCounterTextStrings(LPCTSTR commandLine, BOOL bQuietModeArg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["commandLine", "bQuietModeArg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def loadperf_UnloadPerfCounterTextStrings(jitter):
    """"
    [Loadperf.dll] [ERROR_CODE] UnloadPerfCounterTextStrings(LPCTSTR commandLine, BOOL bQuietModeArg)
    """"
    ret_ad, args = jitter.func_args_stdcall(["commandLine", "bQuietModeArg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
