
def windows.ui.xaml_CreateXamlUIPresenter(jitter):
    """"
    [Windows.UI.Xaml.dll] HRESULT CreateXamlUIPresenter(IViewObjectPresentNotifySite* pPresentSite, Windows::UI::Xaml::Hosting::IXamlUIPresenter** ppPresenter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pPresentSite", "ppPresenter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
