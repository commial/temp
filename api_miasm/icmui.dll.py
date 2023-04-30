
def icmui_SetupColorMatching(jitter):
    """"
    [Icmui.dll] BOOL SetupColorMatching(PCOLORMATCHSETUP pcms)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pcms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
