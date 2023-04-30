
def msctfmonitor_InitLocalMsCtfMonitor(jitter):
    """"
    [MsCtfMonitor.dll] HRESULT InitLocalMsCtfMonitor(DWORD dwFlags)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctfmonitor_UninitLocalMsCtfMonitor(jitter):
    """"
    [MsCtfMonitor.dll] HRESULT UninitLocalMsCtfMonitor()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
