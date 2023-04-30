
def mydocs_PerUserInit(jitter):
    """"
    [mydocs.dll] void PerUserInit()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
