
def msctfmonitor_InitLocalMsCtfMonitor(jitter):
    """
    HRESULT InitLocalMsCtfMonitor(
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def msctfmonitor_UninitLocalMsCtfMonitor(jitter):
    """
    HRESULT UninitLocalMsCtfMonitor()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
