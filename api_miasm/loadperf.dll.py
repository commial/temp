
def loadperf_LoadPerfCounterTextStrings(jitter, get_str, set_str):
    """
    [Loadperf.dll] [ERROR_CODE] LoadPerfCounterTextStrings(LPCTSTR commandLine, BOOL bQuietModeArg)
    """
    ret_ad, args = jitter.func_args_stdcall(["commandLine", "bQuietModeArg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def loadperf_LoadPerfCounterTextStringsA(jitter):
    loadperf_LoadPerfCounterTextStrings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def loadperf_LoadPerfCounterTextStringsW(jitter):
    loadperf_LoadPerfCounterTextStrings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def loadperf_UnloadPerfCounterTextStrings(jitter, get_str, set_str):
    """
    [Loadperf.dll] [ERROR_CODE] UnloadPerfCounterTextStrings(LPCTSTR commandLine, BOOL bQuietModeArg)
    """
    ret_ad, args = jitter.func_args_stdcall(["commandLine", "bQuietModeArg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def loadperf_UnloadPerfCounterTextStringsA(jitter):
    loadperf_UnloadPerfCounterTextStrings(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def loadperf_UnloadPerfCounterTextStringsW(jitter):
    loadperf_UnloadPerfCounterTextStrings(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))
