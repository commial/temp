
def wldap32_cldap_open(jitter):
    """"
    [Wldap32.dll] LDAP* cldap_open(PSTR HostName, ULONG PortNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_cldap_open(jitter):
    """"
    [Wldap32.dll] LDAP* cldap_open(PTSTR HostName, ULONG PortNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_open(jitter):
    """"
    [Wldap32.dll] LDAP* ldap_open(PSTR HostName, ULONG PortNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_open(jitter):
    """"
    [Wldap32.dll] LDAP* ldap_open(PTSTR HostName, ULONG PortNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_bind(jitter):
    """"
    [Wldap32.dll] ULONG ldap_bind(LDAP* ld, PSTR dn, PCHAR cred, ULONG method)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "cred", "method"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_bind(jitter):
    """"
    [Wldap32.dll] ULONG ldap_bind(LDAP* ld, PTSTR dn, PTCHAR cred, ULONG method)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "cred", "method"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_bind_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_bind_s(LDAP* ld, PSTR dn, PCHAR cred, ULONG method)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "cred", "method"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_bind_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_bind_s(LDAP* ld, PTSTR dn, PTCHAR cred, ULONG method)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "cred", "method"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_simple_bind(jitter):
    """"
    [Wldap32.dll] ULONG ldap_simple_bind(LDAP* ld, PSTR dn, PSTR passwd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "passwd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_simple_bind(jitter):
    """"
    [Wldap32.dll] ULONG ldap_simple_bind(LDAP* ld, PTSTR dn, PTSTR passwd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "passwd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_simple_bind_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_simple_bind_s(LDAP* ld, PSTR dn, PSTR passwd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "passwd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_simple_bind_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_simple_bind_s(LDAP* ld, PTSTR dn, PTSTR passwd)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "passwd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_sasl_bind(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_sasl_bind(LDAP* ExternalHandle, const PCHAR DistName, const PCHAR AuthMechanism, const BERVAL* cred, PLDAPControl* ServerCtrls, PLDAPControl* ClientCtrls, int* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistName", "AuthMechanism", "cred", "ServerCtrls", "ClientCtrls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_sasl_bind_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_sasl_bind_s(LDAP* ExternalHandle, const PCHAR DistName, const PCHAR AuthMechanism, const BERVAL* cred, PLDAPControl* ServerCtrls, PLDAPControl* ClientCtrls, PBERVAL* ServerData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistName", "AuthMechanism", "cred", "ServerCtrls", "ClientCtrls", "ServerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_connect(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_connect(LDAP* ld, LDAP_TIMEVAL* timeout)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_init(jitter):
    """"
    [Wldap32.dll] LDAP* ldap_init(PSTR HostName, ULONG PortNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_init(jitter):
    """"
    [Wldap32.dll] LDAP* ldap_init(PTSTR HostName, ULONG PortNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_sslinit(jitter):
    """"
    [Wldap32.dll] LDAP* ldap_sslinit(PSTR HostName, ULONG PortNumber, int secure)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber", "secure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_sslinit(jitter):
    """"
    [Wldap32.dll] LDAP* ldap_sslinit(PTSTR HostName, ULONG PortNumber, int secure)
    """"
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber", "secure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_option(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_get_option(LDAP* ld, int option, void* outvalue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "option", "outvalue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_option(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_get_option(LDAP* ld, int option, void* outvalue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "option", "outvalue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_set_option(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_set_option(LDAP* ld, int option, void* invalue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "option", "invalue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_set_option(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_set_option(LDAP* ld, int option, void* invalue)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "option", "invalue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_abandon(jitter):
    """"
    [Wldap32.dll] ULONG ldap_abandon(LDAP* ld, ULONG msgid)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "msgid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_unbind(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_unbind(LDAP* ld)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_unbind_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_unbind_s(LDAP* ld)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add(jitter):
    """"
    [Wldap32.dll] ULONG ldap_add(LDAP* ld, PSTR dn, LDAPMod* [] attrs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add(jitter):
    """"
    [Wldap32.dll] ULONG ldap_add(LDAP* ld, PTSTR dn, LDAPMod* [] attrs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_add_ext(LDAP* ld, PSTR dn, LDAPMod* [] attrs, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_add_ext(LDAP* ld, PTSTR dn, LDAPMod* [] attrs, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_add_s(LDAP* ld, PSTR dn, LDAPMod* [] attrs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_add_s(LDAP* ld, PTSTR dn, LDAPMod* [] attrs)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_add_ext_s(LDAP* ld, PSTR dn, LDAPMod* [] attrs, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_add_ext_s(LDAP* ld, PTSTR dn, LDAPMod* [] attrs, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare(jitter):
    """"
    [Wldap32.dll] ULONG ldap_compare(LDAP* ld, PSTR dn, PSTR attr, PSTR value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attr", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare(jitter):
    """"
    [Wldap32.dll] ULONG ldap_compare(LDAP* ld, PTSTR dn, PTSTR attr, PTSTR value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attr", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_compare_ext(LDAP* ld, PSTR dn, PSTR Attr, PSTR Value, struct berval* Data, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "Attr", "Value", "Data", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_compare_ext(LDAP* ld, PTSTR dn, PTSTR Attr, PTSTR Value, struct berval* Data, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "Attr", "Value", "Data", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_compare_s(LDAP* ld, PSTR dn, PSTR attr, PSTR value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attr", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_compare_s(LDAP* ld, PTSTR dn, PTSTR attr, PTSTR value)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attr", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_compare_ext_s(LDAP* ld, PSTR dn, PSTR Attr, PSTR Value, struct berval* Data, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "Attr", "Value", "Data", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_compare_ext_s(LDAP* ld, PTSTR dn, PTSTR Attr, PTSTR Value, struct berval* Data, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "Attr", "Value", "Data", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete(jitter):
    """"
    [Wldap32.dll] ULONG ldap_delete(LDAP* ld, PSTR dn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete(jitter):
    """"
    [Wldap32.dll] ULONG ldap_delete(LDAP* ld, PTSTR dn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_delete_ext(LDAP* ld, PSTR dn, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_delete_ext(LDAP* ld, PTSTR dn, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_delete_s(LDAP* ld, PSTR dn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_delete_s(LDAP* ld, PTSTR dn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_delete_ext_s(LDAP* ld, PSTR dn, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_delete_ext_s(LDAP* ld, PTSTR dn, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_extended_operation_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_extended_operation_s(LDAP* ld, PSTR Oid, struct berval* Data, PLDAPControl* ServerControls, PLDAPControl* ClientControls, PCHAR* ReturnedOid, struct berval** ReturnedData)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "Oid", "Data", "ServerControls", "ClientControls", "ReturnedOid", "ReturnedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_extended_operation(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_extended_operation(LDAP* ld, PSTR Oid, struct berval* Data, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "Oid", "Data", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_extended_operation(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_extended_operation(LDAP* ld, PTSTR Oid, struct berval* Data, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "Oid", "Data", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_close_extended_op(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_close_extended_op(LDAP* ld, ULONG MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify(jitter):
    """"
    [Wldap32.dll] ULONG ldap_modify(LDAP* ld, PSTR dn, LDAPMod* [] mods)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify(jitter):
    """"
    [Wldap32.dll] ULONG ldap_modify(LDAP* ld, PTSTR dn, LDAPMod* [] mods)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_modify_ext(LDAP* ld, PSTR dn, LDAPMod* [] mods, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_modify_ext(LDAP* ld, PTSTR dn, LDAPMod* [] mods, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_modify_s(LDAP* ld, PSTR dn, LDAPMod* [] mods)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_modify_s(LDAP* ld, PTSTR dn, LDAPMod* [] mods)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_modify_ext_s(LDAP* ld, PSTR dn, LDAPMod* [] mods, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_modify_ext_s(LDAP* ld, PTSTR dn, LDAPMod* [] mods, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_check_filter(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_check_filter(LDAP* ld, PWCHAR SearchFilter)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "SearchFilter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_entries(jitter):
    """"
    [Wldap32.dll] ULONG ldap_count_entries(LDAP* ld, LDAPMessage* res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_references(jitter):
    """"
    [Wldap32.dll] ULONG ldap_count_references(LDAP* ld, LDAPMessage* res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_values(jitter):
    """"
    [Wldap32.dll] ULONG ldap_count_values(PCHAR* vals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_values(jitter):
    """"
    [Wldap32.dll] ULONG ldap_count_values(PTCHAR* vals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_values_len(jitter):
    """"
    [Wldap32.dll] ULONG ldap_count_values_len(struct berval** vals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_page_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_create_page_control(PLDAP ExternalHandle, ULONG PageSize, struct berval* Cookie, UCHAR IsCritical, PLDAPControl* Control)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "PageSize", "Cookie", "IsCritical", "Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_page_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_create_page_control(PLDAP ExternalHandle, ULONG PageSize, struct berval* Cookie, UCHAR IsCritical, PLDAPControl* Control)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "PageSize", "Cookie", "IsCritical", "Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_sort_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_create_sort_control(PLDAP ExternalHandle, PLDAPSortKey* SortKeys, UCHAR IsCritical, PLDAPControl* Control)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SortKeys", "IsCritical", "Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_sort_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_create_sort_control(PLDAP ExternalHandle, PLDAPSortKey* SortKeys, UCHAR IsCritical, PLDAPControl* Control)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SortKeys", "IsCritical", "Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_vlv_control(jitter):
    """"
    [Wldap32.dll] [LDAP_RETCODE_INT] ldap_create_vlv_control(LDAP* ld, LDAPVLVInfo* Vlvinfop, char IsCritical, LDAPControl** ctrlp)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "Vlvinfop", "IsCritical", "ctrlp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_encode_sort_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_encode_sort_control(PLDAP ExternalHandle, PLDAPSortKey* SortKeys, PLDAPControl Control, BOOLEAN IsCritical)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SortKeys", "Control", "IsCritical"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_escape_filter_element(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_escape_filter_element(PCHAR sourceFilterElement, ULONG sourceLength, PCHAR destFilterElement, ULONG destLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sourceFilterElement", "sourceLength", "destFilterElement", "destLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_escape_filter_element(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_escape_filter_element(PTCHAR sourceFilterElement, ULONG sourceLength, PCHAR destFilterElement, ULONG destLength)
    """"
    ret_ad, args = jitter.func_args_stdcall(["sourceFilterElement", "sourceLength", "destFilterElement", "destLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_first_attribute(jitter):
    """"
    [Wldap32.dll] PCHAR ldap_first_attribute(LDAP* ld, LDAPMessage* entry, BerElement** ptr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_first_attribute(jitter):
    """"
    [Wldap32.dll] PTCHAR ldap_first_attribute(LDAP* ld, LDAPMessage* entry, BerElement** ptr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_next_attribute(jitter):
    """"
    [Wldap32.dll] PCHAR ldap_next_attribute(LDAP* ld, LDAPMessage* entry, BerElement* ptr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_next_attribute(jitter):
    """"
    [Wldap32.dll] PTCHAR ldap_next_attribute(LDAP* ld, LDAPMessage* entry, BerElement* ptr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_first_entry(jitter):
    """"
    [Wldap32.dll] LDAPMessage* ldap_first_entry(LDAP* ld, LDAPMessage* res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_next_entry(jitter):
    """"
    [Wldap32.dll] LDAPMessage* ldap_next_entry(LDAP* ld, LDAPMessage* entry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_first_reference(jitter):
    """"
    [Wldap32.dll] LDAPMessage* ldap_first_reference(LDAP* ld, LDAPMessage* res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_next_reference(jitter):
    """"
    [Wldap32.dll] LDAPMessage* ldap_next_reference(LDAP* ld, LDAPMessage* entry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_next_page(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_get_next_page(PLDAP ExternalHandle, PLDAPSearch SearchHandle, ULONG PageSize, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SearchHandle", "PageSize", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_next_page_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_get_next_page_s(PLDAP ExternalHandle, PLDAPSearch SearchHandle, struct l_timeval* timeout, ULONG PageSize, ULONG* TotalCount, LDAPMessage** Results)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SearchHandle", "timeout", "PageSize", "TotalCount", "Results"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_paged_count(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_get_paged_count(PLDAP ExternalHandle, PLDAPSearch SearchBlock, ULONG* TotalCount, PLDAPMessage Results)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SearchBlock", "TotalCount", "Results"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_values(jitter):
    """"
    [Wldap32.dll] PCHAR* ldap_get_values(LDAP* ld, LDAPMessage* entry, PSTR attr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "attr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_values(jitter):
    """"
    [Wldap32.dll] PTCHAR* ldap_get_values(LDAP* ld, LDAPMessage* entry, PTSTR attr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "attr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_values_len(jitter):
    """"
    [Wldap32.dll] struct berval** ldap_get_values_len(LDAP* ExternalHandle, LDAPMessage* Message, PSTR attr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "Message", "attr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_values_len(jitter):
    """"
    [Wldap32.dll] struct berval** ldap_get_values_len(LDAP* ExternalHandle, LDAPMessage* Message, PTSTR attr)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "Message", "attr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_extended_result(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_extended_result(LDAP* Connection, LDAPMessage* ResultMessage, PCHAR* ResultOID, struct berval** ResultData, BOOLEAN Freeit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "ResultOID", "ResultData", "Freeit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_page_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_page_control(PLDAP ExternalHandle, PLDAPControl* ServerControls, ULONG* TotalCount, struct berval** Cookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "ServerControls", "TotalCount", "Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_page_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_page_control(PLDAP ExternalHandle, PLDAPControl* ServerControls, ULONG* TotalCount, struct berval** Cookie)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "ServerControls", "TotalCount", "Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_reference(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_reference(LDAP* Connection, LDAPMessage* ResultMessage, PCHAR** Referrals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "Referrals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_reference(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_reference(LDAP* Connection, LDAPMessage* ResultMessage, PTCHAR** Referrals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "Referrals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_result(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_result(LDAP* Connection, LDAPMessage* ResultMessage, ULONG* ReturnCode, PCHAR* MatchedDNs, PCHAR* ErrorMessage, PCHAR** Referrals, PLDAPControl** ServerControls, BOOLEAN Freeit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "ReturnCode", "MatchedDNs", "ErrorMessage", "Referrals", "ServerControls", "Freeit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_result(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_result(LDAP* Connection, LDAPMessage* ResultMessage, ULONG* ReturnCode, PTCHAR* MatchedDNs, PTCHAR* ErrorMessage, PTCHAR** Referrals, PLDAPControl** ServerControls, BOOLEAN Freeit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "ReturnCode", "MatchedDNs", "ErrorMessage", "Referrals", "ServerControls", "Freeit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_sort_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_sort_control(PLDAP ExternalHandle, PLDAPControl* Control, ULONG* Result, PCHAR* Attribute)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "Control", "Result", "Attribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_sort_control(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_parse_sort_control(PLDAP ExternalHandle, PLDAPControl* Control, ULONG* Result, PTCHAR* Attribute)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "Control", "Result", "Attribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_vlv_control(jitter):
    """"
    [Wldap32.dll] [LDAP_RETCODE_INT] ldap_parse_vlv_control(LDAP* ld, LDAPControl** ctrls, unsigned long* target_posp, unsigned long* list_countp, struct berval** contextp, int* errcodep)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "ctrls", "target_posp", "list_countp", "contextp", "errcodep"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_result(jitter):
    """"
    [Wldap32.dll] ULONG ldap_result(LDAP* ld, ULONG msgid, ULONG all, struct l_timeval* timeout, LDAPMessage** res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "msgid", "all", "timeout", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search(jitter):
    """"
    [Wldap32.dll] ULONG ldap_search(LDAP* ld, PCHAR base, ULONG scope, PCHAR filter, ULONG attrsonly)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search(jitter):
    """"
    [Wldap32.dll] ULONG ldap_search(LDAP* ld, PTCHAR base, ULONG scope, PTCHAR filter, ULONG attrsonly)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_s(LDAP* ld, PCHAR base, ULONG scope, PCHAR filter, ULONG attrsonly, LDAPMessage** res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_s(LDAP* ld, PTCHAR base, ULONG scope, PTCHAR filter, ULONG attrsonly, LDAPMessage** res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_st(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_st(LDAP* ld, PCHAR base, ULONG scope, PCHAR filter, ULONG attrsonly, struct l_timeval* timeout, LDAPMessage** res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "timeout", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_st(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_st(LDAP* ld, PTCHAR base, ULONG scope, PTCHAR filter, ULONG attrsonly, struct l_timeval* timeout, LDAPMessage** res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "timeout", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_ext(LDAP* ld, PCHAR base, ULONG scope, PCHAR filter, ULONG attrsonly, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG TimeLimit, ULONG SizeLimit, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "ServerControls", "ClientControls", "TimeLimit", "SizeLimit", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_ext(LDAP* ld, PTCHAR base, ULONG scope, PTCHAR filter, ULONG attrsonly, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG TimeLimit, ULONG SizeLimit, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "ServerControls", "ClientControls", "TimeLimit", "SizeLimit", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_ext_s(LDAP* ld, PCHAR base, ULONG scope, PCHAR filter, ULONG attrsonly, PLDAPControl* ServerControls, PLDAPControl* ClientControls, struct l_timeval* timeout, ULONG SizeLimit, LDAPMessage** res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "ServerControls", "ClientControls", "timeout", "SizeLimit", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_ext_s(LDAP* ld, PTCHAR base, ULONG scope, PTCHAR filter, ULONG attrsonly, PLDAPControl* ServerControls, PLDAPControl* ClientControls, struct l_timeval* timeout, ULONG SizeLimit, LDAPMessage** res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "ServerControls", "ClientControls", "timeout", "SizeLimit", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_init_page(jitter):
    """"
    [Wldap32.dll] PLDAPSearch ldap_search_init_page(PLDAP ExternalHandle, PCHAR DistinguishedName, ULONG ScopeOfSearch, PCHAR SearchFilter, ULONG AttributesOnly, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG PageTimeLimit, ULONG TotalSizeLimit, PLDAPSortKey* SortKeys)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "ScopeOfSearch", "SearchFilter", "AttributesOnly", "ServerControls", "ClientControls", "PageTimeLimit", "TotalSizeLimit", "SortKeys"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_init_page(jitter):
    """"
    [Wldap32.dll] PLDAPSearch ldap_search_init_page(PLDAP ExternalHandle, PTCHAR DistinguishedName, ULONG ScopeOfSearch, PTCHAR SearchFilter, ULONG AttributesOnly, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG PageTimeLimit, ULONG TotalSizeLimit, PLDAPSortKey* SortKeys)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "ScopeOfSearch", "SearchFilter", "AttributesOnly", "ServerControls", "ClientControls", "PageTimeLimit", "TotalSizeLimit", "SortKeys"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_abandon_page(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_search_abandon_page(PLDAP ExternalHandle, PLDAPSearch SearchBlock)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SearchBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_err2string(jitter):
    """"
    [Wldap32.dll] PCHAR ldap_err2string(ULONG err)
    """"
    ret_ad, args = jitter.func_args_stdcall(["err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_err2string(jitter):
    """"
    [Wldap32.dll] PTCHAR ldap_err2string(ULONG err)
    """"
    ret_ad, args = jitter.func_args_stdcall(["err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_LdapGetLastError(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE LdapGetLastError()
    """"
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_LdapMapErrorToWin32(jitter):
    """"
    [Wldap32.dll] [ERROR_CODE_ULONG] LdapMapErrorToWin32(LDAP_RETCODE LdapError)
    """"
    ret_ad, args = jitter.func_args_stdcall(["LdapError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_result2error(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_result2error(LDAP* ld, LDAPMessage* res, ULONG freeit)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "res", "freeit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_control_free(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_control_free(LDAPControl* Control)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_control_free(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_control_free(LDAPControl* Control)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_controls_free(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_controls_free(LDAPControl** Controls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Controls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_controls_free(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_controls_free(LDAPControl** Controls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Controls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_memfree(jitter):
    """"
    [Wldap32.dll] VOID ldap_memfree(PCHAR Block)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Block"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_memfree(jitter):
    """"
    [Wldap32.dll] VOID ldap_memfree(PTCHAR Block)
    """"
    ret_ad, args = jitter.func_args_stdcall(["Block"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_msgfree(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_msgfree(LDAPMessage* res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_value_free(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_value_free(PCHAR* vals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_value_free(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_value_free(PTCHAR* vals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_value_free_len(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_value_free_len(struct berval** vals)
    """"
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_dn2ufn(jitter):
    """"
    [Wldap32.dll] PCHAR ldap_dn2ufn(PSTR dn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_dn2ufn(jitter):
    """"
    [Wldap32.dll] PTCHAR ldap_dn2ufn(PTSTR dn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_ufn2dn(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_ufn2dn(PCHAR ufn, PCHAR* pDn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ufn", "pDn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_ufn2dn(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_ufn2dn(PTCHAR ufn, PTCHAR* pDn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ufn", "pDn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_explode_dn(jitter):
    """"
    [Wldap32.dll] PCHAR* ldap_explode_dn(PSTR dn, ULONG notypes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dn", "notypes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_explode_dn(jitter):
    """"
    [Wldap32.dll] PTCHAR* ldap_explode_dn(PTSTR dn, ULONG notypes)
    """"
    ret_ad, args = jitter.func_args_stdcall(["dn", "notypes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_dn(jitter):
    """"
    [Wldap32.dll] PCHAR ldap_get_dn(LDAP* ld, LDAPMessage* entry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_dn(jitter):
    """"
    [Wldap32.dll] PTCHAR ldap_get_dn(LDAP* ld, LDAPMessage* entry)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_conn_from_msg(jitter):
    """"
    [Wldap32.dll] LDAP* ldap_conn_from_msg(LDAP* PrimaryConn, LDAPMessage* res)
    """"
    ret_ad, args = jitter.func_args_stdcall(["PrimaryConn", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2(jitter):
    """"
    [Wldap32.dll] ULONG ldap_modrdn2(LDAP* ExternalHandle, PCHAR DistinguishedName, PCHAR NewDistinguishedName, INT DeleteOldRdn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "NewDistinguishedName", "DeleteOldRdn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2(jitter):
    """"
    [Wldap32.dll] ULONG ldap_modrdn2(LDAP* ExternalHandle, PTCHAR DistinguishedName, PTCHAR NewDistinguishedName, INT DeleteOldRdn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "NewDistinguishedName", "DeleteOldRdn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_modrdn2_s(LDAP* ExternalHandle, PCHAR DistinguishedName, PCHAR NewDistinguishedName, INT DeleteOldRdn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "NewDistinguishedName", "DeleteOldRdn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_modrdn2_s(LDAP* ExternalHandle, PTCHAR DistinguishedName, PTCHAR NewDistinguishedName, INT DeleteOldRdn)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "NewDistinguishedName", "DeleteOldRdn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_rename_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_rename_ext(LDAP* ld, PSTR dn, PSTR NewRDN, PSTR NewParent, INT DeleteOldRdn, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "NewRDN", "NewParent", "DeleteOldRdn", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_rename_ext(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_rename_ext(LDAP* ld, PTSTR dn, PTSTR NewRDN, PTSTR NewParent, INT DeleteOldRdn, PLDAPControl* ServerControls, PLDAPControl* ClientControls, ULONG* MessageNumber)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "NewRDN", "NewParent", "DeleteOldRdn", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_rename_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_rename_ext_s(LDAP* ld, PSTR dn, PSTR NewRDN, PSTR NewParent, INT DeleteOldRdn, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "NewRDN", "NewParent", "DeleteOldRdn", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_rename_ext_s(jitter):
    """"
    [Wldap32.dll] LDAP_RETCODE ldap_rename_ext_s(LDAP* ld, PTSTR dn, PTSTR NewRDN, PTSTR NewParent, INT DeleteOldRdn, PLDAPControl* ServerControls, PLDAPControl* ClientControls)
    """"
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "NewRDN", "NewParent", "DeleteOldRdn", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_LdapUnicodeToUTF8(jitter):
    """"
    [Wldap32.dll] int LdapUnicodeToUTF8(LPCWSTR lpSrcStr, int cchSrc, LPSTR lpDestStr, int cchDest)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSrcStr", "cchSrc", "lpDestStr", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_LdapUTF8ToUnicode(jitter):
    """"
    [Wldap32.dll] int LdapUTF8ToUnicode(LPCSTR lpSrcStr, int cchSrc, LPWSTR lpDestStr, int cchDest)
    """"
    ret_ad, args = jitter.func_args_stdcall(["lpSrcStr", "cchSrc", "lpDestStr", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_init(jitter):
    """"
    [Wldap32.dll] BerElement* ber_init(BERVAL* pBerVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_free(jitter):
    """"
    [Wldap32.dll] void ber_free(BerElement* pBerElement, INT fbuf)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "fbuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_bvfree(jitter):
    """"
    [Wldap32.dll] void ber_bvfree(BERVAL* pBerVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_bvecfree(jitter):
    """"
    [Wldap32.dll] void ber_bvecfree(PBERVAL* pBerVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_bvdup(jitter):
    """"
    [Wldap32.dll] BERVAL* ber_bvdup(BERVAL* pBerVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_alloc_t(jitter):
    """"
    [Wldap32.dll] BerElement* ber_alloc_t(INT options)
    """"
    ret_ad, args = jitter.func_args_stdcall(["options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_skip_tag(jitter):
    """"
    [Wldap32.dll] ULONG ber_skip_tag(BerElement* pBerElement, ULONG* pLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_peek_tag(jitter):
    """"
    [Wldap32.dll] ULONG ber_peek_tag(BerElement* pBerElement, ULONG* pLen)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_first_element(jitter):
    """"
    [Wldap32.dll] ULONG ber_first_element(BerElement* pBerElement, ULONG* pLen, CHAR** ppOpaque)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pLen", "ppOpaque"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_next_element(jitter):
    """"
    [Wldap32.dll] ULONG ber_next_element(BerElement* pBerElement, ULONG* pLen, CHAR* opaque)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pLen", "opaque"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_flatten(jitter):
    """"
    [Wldap32.dll] INT ber_flatten(BerElement* pBerElement, PBERVAL* pBerVal)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_printf(jitter):
    """"
    [Wldap32.dll] INT ber_printf(BerElement* pBerElement, PCHAR fmt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "fmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_scanf(jitter):
    """"
    [Wldap32.dll] INT ber_scanf(BerElement* pBerElement, PCHAR fmt)
    """"
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "fmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
