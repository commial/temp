LDAP_RETCODE = {
    "LDAP_SUCCESS": 0x00,
    "LDAP_OPERATIONS_ERROR": 0x01,
    "LDAP_PROTOCOL_ERROR": 0x02,
    "LDAP_TIMELIMIT_EXCEEDED": 0x03,
    "LDAP_SIZELIMIT_EXCEEDED": 0x04,
    "LDAP_COMPARE_FALSE": 0x05,
    "LDAP_COMPARE_TRUE": 0x06,
    "LDAP_AUTH_METHOD_NOT_SUPPORTED": 0x07,
    "LDAP_STRONG_AUTH_REQUIRED": 0x08,
    "LDAP_REFERRAL_V2": 0x09,
    "LDAP_PARTIAL_RESULTS": 0x09,
    "LDAP_REFERRAL": 0x0a,
    "LDAP_ADMIN_LIMIT_EXCEEDED": 0x0b,
    "LDAP_UNAVAILABLE_CRIT_EXTENSION": 0x0c,
    "LDAP_CONFIDENTIALITY_REQUIRED": 0x0d,
    "LDAP_SASL_BIND_IN_PROGRESS": 0x0e,
    "LDAP_NO_SUCH_ATTRIBUTE": 0x10,
    "LDAP_UNDEFINED_TYPE": 0x11,
    "LDAP_INAPPROPRIATE_MATCHING": 0x12,
    "LDAP_CONSTRAINT_VIOLATION": 0x13,
    "LDAP_ATTRIBUTE_OR_VALUE_EXISTS": 0x14,
    "LDAP_INVALID_SYNTAX": 0x15,
    "LDAP_NO_SUCH_OBJECT": 0x20,
    "LDAP_ALIAS_PROBLEM": 0x21,
    "LDAP_INVALID_DN_SYNTAX": 0x22,
    "LDAP_IS_LEAF": 0x23,
    "LDAP_ALIAS_DEREF_PROBLEM": 0x24,
    "LDAP_INAPPROPRIATE_AUTH": 0x30,
    "LDAP_INVALID_CREDENTIALS": 0x31,
    "LDAP_INSUFFICIENT_RIGHTS": 0x32,
    "LDAP_BUSY": 0x33,
    "LDAP_UNAVAILABLE": 0x34,
    "LDAP_UNWILLING_TO_PERFORM": 0x35,
    "LDAP_LOOP_DETECT": 0x36,
    "LDAP_SORT_CONTROL_MISSING": 0x3C,
    "LDAP_OFFSET_RANGE_ERROR": 0x3D,
    "LDAP_NAMING_VIOLATION": 0x40,
    "LDAP_OBJECT_CLASS_VIOLATION": 0x41,
    "LDAP_NOT_ALLOWED_ON_NONLEAF": 0x42,
    "LDAP_NOT_ALLOWED_ON_RDN": 0x43,
    "LDAP_ALREADY_EXISTS": 0x44,
    "LDAP_NO_OBJECT_CLASS_MODS": 0x45,
    "LDAP_RESULTS_TOO_LARGE": 0x46,
    "LDAP_AFFECTS_MULTIPLE_DSAS": 0x47,
    "LDAP_VIRTUAL_LIST_VIEW_ERROR": 0x4c,
    "LDAP_OTHER": 0x50,
    "LDAP_SERVER_DOWN": 0x51,
    "LDAP_LOCAL_ERROR": 0x52,
    "LDAP_ENCODING_ERROR": 0x53,
    "LDAP_DECODING_ERROR": 0x54,
    "LDAP_TIMEOUT": 0x55,
    "LDAP_AUTH_UNKNOWN": 0x56,
    "LDAP_FILTER_ERROR": 0x57,
    "LDAP_USER_CANCELLED": 0x58,
    "LDAP_PARAM_ERROR": 0x59,
    "LDAP_NO_MEMORY": 0x5a,
    "LDAP_CONNECT_ERROR": 0x5b,
    "LDAP_NOT_SUPPORTED": 0x5c,
    "LDAP_NO_RESULTS_RETURNED": 0x5e,
    "LDAP_CONTROL_NOT_FOUND": 0x5d,
    "LDAP_MORE_RESULTS_TO_RETURN": 0x5f,
    "LDAP_CLIENT_LOOP": 0x60,
    "LDAP_REFERRAL_LIMIT_EXCEEDED": 0x61,
}

def wldap32_cldap_open(jitter):
    """
    LDAP* cldap_open(
        PSTR HostName,
        ULONG PortNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_cldap_open(jitter, get_str, set_str):
    """
    LDAP* cldap_open(
        PTSTR HostName,
        ULONG PortNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_cldap_openA(jitter):
    wldap32_cldap_open(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_cldap_openW(jitter):
    wldap32_cldap_open(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_open(jitter):
    """
    LDAP* ldap_open(
        PSTR HostName,
        ULONG PortNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_open(jitter, get_str, set_str):
    """
    LDAP* ldap_open(
        PTSTR HostName,
        ULONG PortNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_openA(jitter):
    wldap32_ldap_open(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_openW(jitter):
    wldap32_ldap_open(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_bind(jitter):
    """
    ULONG ldap_bind(
        LDAP* ld,
        PSTR dn,
        PCHAR cred,
        ULONG method
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "cred", "method"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_bind(jitter, get_str, set_str):
    """
    ULONG ldap_bind(
        LDAP* ld,
        PTSTR dn,
        PTCHAR cred,
        ULONG method
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "cred", "method"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_bindA(jitter):
    wldap32_ldap_bind(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_bindW(jitter):
    wldap32_ldap_bind(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_bind_s(jitter):
    """
    LDAP_RETCODE ldap_bind_s(
        LDAP* ld,
        PSTR dn,
        PCHAR cred,
        ULONG method
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "cred", "method"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_bind_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_bind_s(
        LDAP* ld,
        PTSTR dn,
        PTCHAR cred,
        ULONG method
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "cred", "method"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_bind_sA(jitter):
    wldap32_ldap_bind_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_bind_sW(jitter):
    wldap32_ldap_bind_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_simple_bind(jitter):
    """
    ULONG ldap_simple_bind(
        LDAP* ld,
        PSTR dn,
        PSTR passwd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "passwd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_simple_bind(jitter, get_str, set_str):
    """
    ULONG ldap_simple_bind(
        LDAP* ld,
        PTSTR dn,
        PTSTR passwd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "passwd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_simple_bindA(jitter):
    wldap32_ldap_simple_bind(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_simple_bindW(jitter):
    wldap32_ldap_simple_bind(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_simple_bind_s(jitter):
    """
    LDAP_RETCODE ldap_simple_bind_s(
        LDAP* ld,
        PSTR dn,
        PSTR passwd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "passwd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_simple_bind_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_simple_bind_s(
        LDAP* ld,
        PTSTR dn,
        PTSTR passwd
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "passwd"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_simple_bind_sA(jitter):
    wldap32_ldap_simple_bind_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_simple_bind_sW(jitter):
    wldap32_ldap_simple_bind_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_sasl_bind(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_sasl_bind(
        LDAP* ExternalHandle,
        const PCHAR DistName,
        const PCHAR AuthMechanism,
        const BERVAL* cred,
        PLDAPControl* ServerCtrls,
        PLDAPControl* ClientCtrls,
        int* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistName", "AuthMechanism", "cred", "ServerCtrls", "ClientCtrls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_sasl_bindA(jitter):
    wldap32_ldap_sasl_bind(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_sasl_bindW(jitter):
    wldap32_ldap_sasl_bind(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_sasl_bind_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_sasl_bind_s(
        LDAP* ExternalHandle,
        const PCHAR DistName,
        const PCHAR AuthMechanism,
        const BERVAL* cred,
        PLDAPControl* ServerCtrls,
        PLDAPControl* ClientCtrls,
        PBERVAL* ServerData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistName", "AuthMechanism", "cred", "ServerCtrls", "ClientCtrls", "ServerData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_sasl_bind_sA(jitter):
    wldap32_ldap_sasl_bind_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_sasl_bind_sW(jitter):
    wldap32_ldap_sasl_bind_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_connect(jitter):
    """
    LDAP_RETCODE ldap_connect(
        LDAP* ld,
        LDAP_TIMEVAL* timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_init(jitter):
    """
    LDAP* ldap_init(
        PSTR HostName,
        ULONG PortNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_init(jitter, get_str, set_str):
    """
    LDAP* ldap_init(
        PTSTR HostName,
        ULONG PortNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_initA(jitter):
    wldap32_ldap_init(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_initW(jitter):
    wldap32_ldap_init(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_sslinit(jitter):
    """
    LDAP* ldap_sslinit(
        PSTR HostName,
        ULONG PortNumber,
        int secure
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber", "secure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_sslinit(jitter, get_str, set_str):
    """
    LDAP* ldap_sslinit(
        PTSTR HostName,
        ULONG PortNumber,
        int secure
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HostName", "PortNumber", "secure"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_sslinitA(jitter):
    wldap32_ldap_sslinit(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_sslinitW(jitter):
    wldap32_ldap_sslinit(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_get_option(jitter):
    """
    LDAP_RETCODE ldap_get_option(
        LDAP* ld,
        int option,
        void* outvalue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "option", "outvalue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_option(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_get_option(
        LDAP* ld,
        int option,
        void* outvalue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "option", "outvalue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_optionA(jitter):
    wldap32_ldap_get_option(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_get_optionW(jitter):
    wldap32_ldap_get_option(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_set_option(jitter):
    """
    LDAP_RETCODE ldap_set_option(
        LDAP* ld,
        int option,
        void* invalue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "option", "invalue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_set_option(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_set_option(
        LDAP* ld,
        int option,
        void* invalue
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "option", "invalue"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_set_optionA(jitter):
    wldap32_ldap_set_option(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_set_optionW(jitter):
    wldap32_ldap_set_option(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_abandon(jitter):
    """
    ULONG ldap_abandon(
        LDAP* ld,
        ULONG msgid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "msgid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_unbind(jitter):
    """
    LDAP_RETCODE ldap_unbind(
        LDAP* ld
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_unbind_s(jitter):
    """
    LDAP_RETCODE ldap_unbind_s(
        LDAP* ld
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add(jitter):
    """
    ULONG ldap_add(
        LDAP* ld,
        PSTR dn,
        LDAPMod* [] attrs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add(jitter, get_str, set_str):
    """
    ULONG ldap_add(
        LDAP* ld,
        PTSTR dn,
        LDAPMod* [] attrs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_addA(jitter):
    wldap32_ldap_add(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_addW(jitter):
    wldap32_ldap_add(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_add_ext(jitter):
    """
    LDAP_RETCODE ldap_add_ext(
        LDAP* ld,
        PSTR dn,
        LDAPMod* [] attrs,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_ext(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_add_ext(
        LDAP* ld,
        PTSTR dn,
        LDAPMod* [] attrs,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_extA(jitter):
    wldap32_ldap_add_ext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_add_extW(jitter):
    wldap32_ldap_add_ext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_add_s(jitter):
    """
    LDAP_RETCODE ldap_add_s(
        LDAP* ld,
        PSTR dn,
        LDAPMod* [] attrs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_add_s(
        LDAP* ld,
        PTSTR dn,
        LDAPMod* [] attrs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_sA(jitter):
    wldap32_ldap_add_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_add_sW(jitter):
    wldap32_ldap_add_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_add_ext_s(jitter):
    """
    LDAP_RETCODE ldap_add_ext_s(
        LDAP* ld,
        PSTR dn,
        LDAPMod* [] attrs,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_ext_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_add_ext_s(
        LDAP* ld,
        PTSTR dn,
        LDAPMod* [] attrs,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attrs", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_add_ext_sA(jitter):
    wldap32_ldap_add_ext_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_add_ext_sW(jitter):
    wldap32_ldap_add_ext_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_compare(jitter):
    """
    ULONG ldap_compare(
        LDAP* ld,
        PSTR dn,
        PSTR attr,
        PSTR value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attr", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare(jitter, get_str, set_str):
    """
    ULONG ldap_compare(
        LDAP* ld,
        PTSTR dn,
        PTSTR attr,
        PTSTR value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attr", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compareA(jitter):
    wldap32_ldap_compare(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_compareW(jitter):
    wldap32_ldap_compare(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_compare_ext(jitter):
    """
    LDAP_RETCODE ldap_compare_ext(
        LDAP* ld,
        PSTR dn,
        PSTR Attr,
        PSTR Value,
        struct berval* Data,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "Attr", "Value", "Data", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_ext(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_compare_ext(
        LDAP* ld,
        PTSTR dn,
        PTSTR Attr,
        PTSTR Value,
        struct berval* Data,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "Attr", "Value", "Data", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_extA(jitter):
    wldap32_ldap_compare_ext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_compare_extW(jitter):
    wldap32_ldap_compare_ext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_compare_s(jitter):
    """
    LDAP_RETCODE ldap_compare_s(
        LDAP* ld,
        PSTR dn,
        PSTR attr,
        PSTR value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attr", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_compare_s(
        LDAP* ld,
        PTSTR dn,
        PTSTR attr,
        PTSTR value
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "attr", "value"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_sA(jitter):
    wldap32_ldap_compare_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_compare_sW(jitter):
    wldap32_ldap_compare_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_compare_ext_s(jitter):
    """
    LDAP_RETCODE ldap_compare_ext_s(
        LDAP* ld,
        PSTR dn,
        PSTR Attr,
        PSTR Value,
        struct berval* Data,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "Attr", "Value", "Data", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_ext_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_compare_ext_s(
        LDAP* ld,
        PTSTR dn,
        PTSTR Attr,
        PTSTR Value,
        struct berval* Data,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "Attr", "Value", "Data", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_compare_ext_sA(jitter):
    wldap32_ldap_compare_ext_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_compare_ext_sW(jitter):
    wldap32_ldap_compare_ext_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_delete(jitter):
    """
    ULONG ldap_delete(
        LDAP* ld,
        PSTR dn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete(jitter, get_str, set_str):
    """
    ULONG ldap_delete(
        LDAP* ld,
        PTSTR dn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_deleteA(jitter):
    wldap32_ldap_delete(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_deleteW(jitter):
    wldap32_ldap_delete(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_delete_ext(jitter):
    """
    LDAP_RETCODE ldap_delete_ext(
        LDAP* ld,
        PSTR dn,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_ext(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_delete_ext(
        LDAP* ld,
        PTSTR dn,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_extA(jitter):
    wldap32_ldap_delete_ext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_delete_extW(jitter):
    wldap32_ldap_delete_ext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_delete_s(jitter):
    """
    LDAP_RETCODE ldap_delete_s(
        LDAP* ld,
        PSTR dn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_delete_s(
        LDAP* ld,
        PTSTR dn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_sA(jitter):
    wldap32_ldap_delete_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_delete_sW(jitter):
    wldap32_ldap_delete_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_delete_ext_s(jitter):
    """
    LDAP_RETCODE ldap_delete_ext_s(
        LDAP* ld,
        PSTR dn,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_ext_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_delete_ext_s(
        LDAP* ld,
        PTSTR dn,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_delete_ext_sA(jitter):
    wldap32_ldap_delete_ext_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_delete_ext_sW(jitter):
    wldap32_ldap_delete_ext_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_extended_operation_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_extended_operation_s(
        LDAP* ld,
        PSTR Oid,
        struct berval* Data,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        PCHAR* ReturnedOid,
        struct berval** ReturnedData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "Oid", "Data", "ServerControls", "ClientControls", "ReturnedOid", "ReturnedData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_extended_operation_sA(jitter):
    wldap32_ldap_extended_operation_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_extended_operation_sW(jitter):
    wldap32_ldap_extended_operation_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_extended_operation(jitter):
    """
    LDAP_RETCODE ldap_extended_operation(
        LDAP* ld,
        PSTR Oid,
        struct berval* Data,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "Oid", "Data", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_extended_operation(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_extended_operation(
        LDAP* ld,
        PTSTR Oid,
        struct berval* Data,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "Oid", "Data", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_extended_operationA(jitter):
    wldap32_ldap_extended_operation(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_extended_operationW(jitter):
    wldap32_ldap_extended_operation(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_close_extended_op(jitter):
    """
    LDAP_RETCODE ldap_close_extended_op(
        LDAP* ld,
        ULONG MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify(jitter):
    """
    ULONG ldap_modify(
        LDAP* ld,
        PSTR dn,
        LDAPMod* [] mods
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify(jitter, get_str, set_str):
    """
    ULONG ldap_modify(
        LDAP* ld,
        PTSTR dn,
        LDAPMod* [] mods
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modifyA(jitter):
    wldap32_ldap_modify(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_modifyW(jitter):
    wldap32_ldap_modify(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_modify_ext(jitter):
    """
    LDAP_RETCODE ldap_modify_ext(
        LDAP* ld,
        PSTR dn,
        LDAPMod* [] mods,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_ext(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_modify_ext(
        LDAP* ld,
        PTSTR dn,
        LDAPMod* [] mods,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_extA(jitter):
    wldap32_ldap_modify_ext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_modify_extW(jitter):
    wldap32_ldap_modify_ext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_modify_s(jitter):
    """
    LDAP_RETCODE ldap_modify_s(
        LDAP* ld,
        PSTR dn,
        LDAPMod* [] mods
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_modify_s(
        LDAP* ld,
        PTSTR dn,
        LDAPMod* [] mods
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_sA(jitter):
    wldap32_ldap_modify_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_modify_sW(jitter):
    wldap32_ldap_modify_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_modify_ext_s(jitter):
    """
    LDAP_RETCODE ldap_modify_ext_s(
        LDAP* ld,
        PSTR dn,
        LDAPMod* [] mods,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_ext_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_modify_ext_s(
        LDAP* ld,
        PTSTR dn,
        LDAPMod* [] mods,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "mods", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modify_ext_sA(jitter):
    wldap32_ldap_modify_ext_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_modify_ext_sW(jitter):
    wldap32_ldap_modify_ext_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_check_filter(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_check_filter(
        LDAP* ld,
        PWCHAR SearchFilter
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "SearchFilter"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_check_filterA(jitter):
    wldap32_ldap_check_filter(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_check_filterW(jitter):
    wldap32_ldap_check_filter(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_count_entries(jitter):
    """
    ULONG ldap_count_entries(
        LDAP* ld,
        LDAPMessage* res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_references(jitter):
    """
    ULONG ldap_count_references(
        LDAP* ld,
        LDAPMessage* res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_values(jitter):
    """
    ULONG ldap_count_values(
        PCHAR* vals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_values(jitter, get_str, set_str):
    """
    ULONG ldap_count_values(
        PTCHAR* vals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_count_valuesA(jitter):
    wldap32_ldap_count_values(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_count_valuesW(jitter):
    wldap32_ldap_count_values(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_count_values_len(jitter):
    """
    ULONG ldap_count_values_len(
        struct berval** vals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_page_control(jitter):
    """
    LDAP_RETCODE ldap_create_page_control(
        PLDAP ExternalHandle,
        ULONG PageSize,
        struct berval* Cookie,
        UCHAR IsCritical,
        PLDAPControl* Control
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "PageSize", "Cookie", "IsCritical", "Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_page_control(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_create_page_control(
        PLDAP ExternalHandle,
        ULONG PageSize,
        struct berval* Cookie,
        UCHAR IsCritical,
        PLDAPControl* Control
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "PageSize", "Cookie", "IsCritical", "Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_page_controlA(jitter):
    wldap32_ldap_create_page_control(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_create_page_controlW(jitter):
    wldap32_ldap_create_page_control(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_create_sort_control(jitter):
    """
    LDAP_RETCODE ldap_create_sort_control(
        PLDAP ExternalHandle,
        PLDAPSortKey* SortKeys,
        UCHAR IsCritical,
        PLDAPControl* Control
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SortKeys", "IsCritical", "Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_sort_control(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_create_sort_control(
        PLDAP ExternalHandle,
        PLDAPSortKey* SortKeys,
        UCHAR IsCritical,
        PLDAPControl* Control
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SortKeys", "IsCritical", "Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_sort_controlA(jitter):
    wldap32_ldap_create_sort_control(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_create_sort_controlW(jitter):
    wldap32_ldap_create_sort_control(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_create_vlv_control(jitter, get_str, set_str):
    """
    [LDAP_RETCODE_INT] ldap_create_vlv_control(
        LDAP* ld,
        LDAPVLVInfo* Vlvinfop,
        char IsCritical,
        LDAPControl** ctrlp
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "Vlvinfop", "IsCritical", "ctrlp"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_create_vlv_controlA(jitter):
    wldap32_ldap_create_vlv_control(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_create_vlv_controlW(jitter):
    wldap32_ldap_create_vlv_control(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_encode_sort_control(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_encode_sort_control(
        PLDAP ExternalHandle,
        PLDAPSortKey* SortKeys,
        PLDAPControl Control,
        BOOLEAN IsCritical
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SortKeys", "Control", "IsCritical"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_encode_sort_controlA(jitter):
    wldap32_ldap_encode_sort_control(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_encode_sort_controlW(jitter):
    wldap32_ldap_encode_sort_control(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_escape_filter_element(jitter):
    """
    LDAP_RETCODE ldap_escape_filter_element(
        PCHAR sourceFilterElement,
        ULONG sourceLength,
        PCHAR destFilterElement,
        ULONG destLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sourceFilterElement", "sourceLength", "destFilterElement", "destLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_escape_filter_element(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_escape_filter_element(
        PTCHAR sourceFilterElement,
        ULONG sourceLength,
        PCHAR destFilterElement,
        ULONG destLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["sourceFilterElement", "sourceLength", "destFilterElement", "destLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_escape_filter_elementA(jitter):
    wldap32_ldap_escape_filter_element(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_escape_filter_elementW(jitter):
    wldap32_ldap_escape_filter_element(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_first_attribute(jitter):
    """
    PCHAR ldap_first_attribute(
        LDAP* ld,
        LDAPMessage* entry,
        BerElement** ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_first_attribute(jitter, get_str, set_str):
    """
    PTCHAR ldap_first_attribute(
        LDAP* ld,
        LDAPMessage* entry,
        BerElement** ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_first_attributeA(jitter):
    wldap32_ldap_first_attribute(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_first_attributeW(jitter):
    wldap32_ldap_first_attribute(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_next_attribute(jitter):
    """
    PCHAR ldap_next_attribute(
        LDAP* ld,
        LDAPMessage* entry,
        BerElement* ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_next_attribute(jitter, get_str, set_str):
    """
    PTCHAR ldap_next_attribute(
        LDAP* ld,
        LDAPMessage* entry,
        BerElement* ptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "ptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_next_attributeA(jitter):
    wldap32_ldap_next_attribute(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_next_attributeW(jitter):
    wldap32_ldap_next_attribute(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_first_entry(jitter):
    """
    LDAPMessage* ldap_first_entry(
        LDAP* ld,
        LDAPMessage* res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_next_entry(jitter):
    """
    LDAPMessage* ldap_next_entry(
        LDAP* ld,
        LDAPMessage* entry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_first_reference(jitter):
    """
    LDAPMessage* ldap_first_reference(
        LDAP* ld,
        LDAPMessage* res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_next_reference(jitter):
    """
    LDAPMessage* ldap_next_reference(
        LDAP* ld,
        LDAPMessage* entry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_next_page(jitter):
    """
    LDAP_RETCODE ldap_get_next_page(
        PLDAP ExternalHandle,
        PLDAPSearch SearchHandle,
        ULONG PageSize,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SearchHandle", "PageSize", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_next_page_s(jitter):
    """
    LDAP_RETCODE ldap_get_next_page_s(
        PLDAP ExternalHandle,
        PLDAPSearch SearchHandle,
        struct l_timeval* timeout,
        ULONG PageSize,
        ULONG* TotalCount,
        LDAPMessage** Results
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SearchHandle", "timeout", "PageSize", "TotalCount", "Results"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_paged_count(jitter):
    """
    LDAP_RETCODE ldap_get_paged_count(
        PLDAP ExternalHandle,
        PLDAPSearch SearchBlock,
        ULONG* TotalCount,
        PLDAPMessage Results
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SearchBlock", "TotalCount", "Results"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_values(jitter):
    """
    PCHAR* ldap_get_values(
        LDAP* ld,
        LDAPMessage* entry,
        PSTR attr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "attr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_values(jitter, get_str, set_str):
    """
    PTCHAR* ldap_get_values(
        LDAP* ld,
        LDAPMessage* entry,
        PTSTR attr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry", "attr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_valuesA(jitter):
    wldap32_ldap_get_values(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_get_valuesW(jitter):
    wldap32_ldap_get_values(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_get_values_len(jitter):
    """
    struct berval** ldap_get_values_len(
        LDAP* ExternalHandle,
        LDAPMessage* Message,
        PSTR attr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "Message", "attr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_values_len(jitter, get_str, set_str):
    """
    struct berval** ldap_get_values_len(
        LDAP* ExternalHandle,
        LDAPMessage* Message,
        PTSTR attr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "Message", "attr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_values_lenA(jitter):
    wldap32_ldap_get_values_len(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_get_values_lenW(jitter):
    wldap32_ldap_get_values_len(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_parse_extended_result(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_parse_extended_result(
        LDAP* Connection,
        LDAPMessage* ResultMessage,
        PCHAR* ResultOID,
        struct berval** ResultData,
        BOOLEAN Freeit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "ResultOID", "ResultData", "Freeit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_extended_resultA(jitter):
    wldap32_ldap_parse_extended_result(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_parse_extended_resultW(jitter):
    wldap32_ldap_parse_extended_result(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_parse_page_control(jitter):
    """
    LDAP_RETCODE ldap_parse_page_control(
        PLDAP ExternalHandle,
        PLDAPControl* ServerControls,
        ULONG* TotalCount,
        struct berval** Cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "ServerControls", "TotalCount", "Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_page_control(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_parse_page_control(
        PLDAP ExternalHandle,
        PLDAPControl* ServerControls,
        ULONG* TotalCount,
        struct berval** Cookie
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "ServerControls", "TotalCount", "Cookie"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_page_controlA(jitter):
    wldap32_ldap_parse_page_control(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_parse_page_controlW(jitter):
    wldap32_ldap_parse_page_control(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_parse_reference(jitter):
    """
    LDAP_RETCODE ldap_parse_reference(
        LDAP* Connection,
        LDAPMessage* ResultMessage,
        PCHAR** Referrals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "Referrals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_reference(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_parse_reference(
        LDAP* Connection,
        LDAPMessage* ResultMessage,
        PTCHAR** Referrals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "Referrals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_referenceA(jitter):
    wldap32_ldap_parse_reference(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_parse_referenceW(jitter):
    wldap32_ldap_parse_reference(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_parse_result(jitter):
    """
    LDAP_RETCODE ldap_parse_result(
        LDAP* Connection,
        LDAPMessage* ResultMessage,
        ULONG* ReturnCode,
        PCHAR* MatchedDNs,
        PCHAR* ErrorMessage,
        PCHAR** Referrals,
        PLDAPControl** ServerControls,
        BOOLEAN Freeit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "ReturnCode", "MatchedDNs", "ErrorMessage", "Referrals", "ServerControls", "Freeit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_result(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_parse_result(
        LDAP* Connection,
        LDAPMessage* ResultMessage,
        ULONG* ReturnCode,
        PTCHAR* MatchedDNs,
        PTCHAR* ErrorMessage,
        PTCHAR** Referrals,
        PLDAPControl** ServerControls,
        BOOLEAN Freeit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Connection", "ResultMessage", "ReturnCode", "MatchedDNs", "ErrorMessage", "Referrals", "ServerControls", "Freeit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_resultA(jitter):
    wldap32_ldap_parse_result(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_parse_resultW(jitter):
    wldap32_ldap_parse_result(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_parse_sort_control(jitter):
    """
    LDAP_RETCODE ldap_parse_sort_control(
        PLDAP ExternalHandle,
        PLDAPControl* Control,
        ULONG* Result,
        PCHAR* Attribute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "Control", "Result", "Attribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_sort_control(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_parse_sort_control(
        PLDAP ExternalHandle,
        PLDAPControl* Control,
        ULONG* Result,
        PTCHAR* Attribute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "Control", "Result", "Attribute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_sort_controlA(jitter):
    wldap32_ldap_parse_sort_control(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_parse_sort_controlW(jitter):
    wldap32_ldap_parse_sort_control(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_parse_vlv_control(jitter, get_str, set_str):
    """
    [LDAP_RETCODE_INT] ldap_parse_vlv_control(
        LDAP* ld,
        LDAPControl** ctrls,
        unsigned long* target_posp,
        unsigned long* list_countp,
        struct berval** contextp,
        int* errcodep
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "ctrls", "target_posp", "list_countp", "contextp", "errcodep"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_parse_vlv_controlA(jitter):
    wldap32_ldap_parse_vlv_control(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_parse_vlv_controlW(jitter):
    wldap32_ldap_parse_vlv_control(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_result(jitter):
    """
    ULONG ldap_result(
        LDAP* ld,
        ULONG msgid,
        ULONG all,
        struct l_timeval* timeout,
        LDAPMessage** res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "msgid", "all", "timeout", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search(jitter):
    """
    ULONG ldap_search(
        LDAP* ld,
        PCHAR base,
        ULONG scope,
        PCHAR filter,
        ULONG attrsonly
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search(jitter, get_str, set_str):
    """
    ULONG ldap_search(
        LDAP* ld,
        PTCHAR base,
        ULONG scope,
        PTCHAR filter,
        ULONG attrsonly
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_searchA(jitter):
    wldap32_ldap_search(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_searchW(jitter):
    wldap32_ldap_search(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_search_s(jitter):
    """
    LDAP_RETCODE ldap_search_s(
        LDAP* ld,
        PCHAR base,
        ULONG scope,
        PCHAR filter,
        ULONG attrsonly,
        LDAPMessage** res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_search_s(
        LDAP* ld,
        PTCHAR base,
        ULONG scope,
        PTCHAR filter,
        ULONG attrsonly,
        LDAPMessage** res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_sA(jitter):
    wldap32_ldap_search_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_search_sW(jitter):
    wldap32_ldap_search_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_search_st(jitter):
    """
    LDAP_RETCODE ldap_search_st(
        LDAP* ld,
        PCHAR base,
        ULONG scope,
        PCHAR filter,
        ULONG attrsonly,
        struct l_timeval* timeout,
        LDAPMessage** res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "timeout", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_st(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_search_st(
        LDAP* ld,
        PTCHAR base,
        ULONG scope,
        PTCHAR filter,
        ULONG attrsonly,
        struct l_timeval* timeout,
        LDAPMessage** res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "timeout", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_stA(jitter):
    wldap32_ldap_search_st(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_search_stW(jitter):
    wldap32_ldap_search_st(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_search_ext(jitter):
    """
    LDAP_RETCODE ldap_search_ext(
        LDAP* ld,
        PCHAR base,
        ULONG scope,
        PCHAR filter,
        ULONG attrsonly,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG TimeLimit,
        ULONG SizeLimit,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "ServerControls", "ClientControls", "TimeLimit", "SizeLimit", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_ext(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_search_ext(
        LDAP* ld,
        PTCHAR base,
        ULONG scope,
        PTCHAR filter,
        ULONG attrsonly,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG TimeLimit,
        ULONG SizeLimit,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "ServerControls", "ClientControls", "TimeLimit", "SizeLimit", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_extA(jitter):
    wldap32_ldap_search_ext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_search_extW(jitter):
    wldap32_ldap_search_ext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_search_ext_s(jitter):
    """
    LDAP_RETCODE ldap_search_ext_s(
        LDAP* ld,
        PCHAR base,
        ULONG scope,
        PCHAR filter,
        ULONG attrsonly,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        struct l_timeval* timeout,
        ULONG SizeLimit,
        LDAPMessage** res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "ServerControls", "ClientControls", "timeout", "SizeLimit", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_ext_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_search_ext_s(
        LDAP* ld,
        PTCHAR base,
        ULONG scope,
        PTCHAR filter,
        ULONG attrsonly,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        struct l_timeval* timeout,
        ULONG SizeLimit,
        LDAPMessage** res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "base", "scope", "filter", "attrsonly", "ServerControls", "ClientControls", "timeout", "SizeLimit", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_ext_sA(jitter):
    wldap32_ldap_search_ext_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_search_ext_sW(jitter):
    wldap32_ldap_search_ext_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_search_init_page(jitter):
    """
    PLDAPSearch ldap_search_init_page(
        PLDAP ExternalHandle,
        PCHAR DistinguishedName,
        ULONG ScopeOfSearch,
        PCHAR SearchFilter,
        ULONG AttributesOnly,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG PageTimeLimit,
        ULONG TotalSizeLimit,
        PLDAPSortKey* SortKeys
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "ScopeOfSearch", "SearchFilter", "AttributesOnly", "ServerControls", "ClientControls", "PageTimeLimit", "TotalSizeLimit", "SortKeys"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_init_page(jitter, get_str, set_str):
    """
    PLDAPSearch ldap_search_init_page(
        PLDAP ExternalHandle,
        PTCHAR DistinguishedName,
        ULONG ScopeOfSearch,
        PTCHAR SearchFilter,
        ULONG AttributesOnly,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG PageTimeLimit,
        ULONG TotalSizeLimit,
        PLDAPSortKey* SortKeys
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "ScopeOfSearch", "SearchFilter", "AttributesOnly", "ServerControls", "ClientControls", "PageTimeLimit", "TotalSizeLimit", "SortKeys"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_search_init_pageA(jitter):
    wldap32_ldap_search_init_page(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_search_init_pageW(jitter):
    wldap32_ldap_search_init_page(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_search_abandon_page(jitter):
    """
    LDAP_RETCODE ldap_search_abandon_page(
        PLDAP ExternalHandle,
        PLDAPSearch SearchBlock
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "SearchBlock"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_err2string(jitter):
    """
    PCHAR ldap_err2string(
        ULONG err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_err2string(jitter, get_str, set_str):
    """
    PTCHAR ldap_err2string(
        ULONG err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_err2stringA(jitter):
    wldap32_ldap_err2string(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_err2stringW(jitter):
    wldap32_ldap_err2string(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_LdapGetLastError(jitter):
    """
    LDAP_RETCODE LdapGetLastError()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_LdapMapErrorToWin32(jitter):
    """
    [ERROR_CODE_ULONG] LdapMapErrorToWin32(
        LDAP_RETCODE LdapError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["LdapError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_result2error(jitter):
    """
    LDAP_RETCODE ldap_result2error(
        LDAP* ld,
        LDAPMessage* res,
        ULONG freeit
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "res", "freeit"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_control_free(jitter):
    """
    LDAP_RETCODE ldap_control_free(
        LDAPControl* Control
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_control_free(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_control_free(
        LDAPControl* Control
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Control"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_control_freeA(jitter):
    wldap32_ldap_control_free(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_control_freeW(jitter):
    wldap32_ldap_control_free(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_controls_free(jitter):
    """
    LDAP_RETCODE ldap_controls_free(
        LDAPControl** Controls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Controls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_controls_free(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_controls_free(
        LDAPControl** Controls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Controls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_controls_freeA(jitter):
    wldap32_ldap_controls_free(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_controls_freeW(jitter):
    wldap32_ldap_controls_free(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_memfree(jitter):
    """
    VOID ldap_memfree(
        PCHAR Block
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Block"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_memfree(jitter, get_str, set_str):
    """
    VOID ldap_memfree(
        PTCHAR Block
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Block"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_memfreeA(jitter):
    wldap32_ldap_memfree(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_memfreeW(jitter):
    wldap32_ldap_memfree(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_msgfree(jitter):
    """
    LDAP_RETCODE ldap_msgfree(
        LDAPMessage* res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_value_free(jitter):
    """
    LDAP_RETCODE ldap_value_free(
        PCHAR* vals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_value_free(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_value_free(
        PTCHAR* vals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_value_freeA(jitter):
    wldap32_ldap_value_free(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_value_freeW(jitter):
    wldap32_ldap_value_free(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_value_free_len(jitter):
    """
    LDAP_RETCODE ldap_value_free_len(
        struct berval** vals
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["vals"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_dn2ufn(jitter):
    """
    PCHAR ldap_dn2ufn(
        PSTR dn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_dn2ufn(jitter, get_str, set_str):
    """
    PTCHAR ldap_dn2ufn(
        PTSTR dn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_dn2ufnA(jitter):
    wldap32_ldap_dn2ufn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_dn2ufnW(jitter):
    wldap32_ldap_dn2ufn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_ufn2dn(jitter):
    """
    LDAP_RETCODE ldap_ufn2dn(
        PCHAR ufn,
        PCHAR* pDn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ufn", "pDn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_ufn2dn(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_ufn2dn(
        PTCHAR ufn,
        PTCHAR* pDn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ufn", "pDn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_ufn2dnA(jitter):
    wldap32_ldap_ufn2dn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_ufn2dnW(jitter):
    wldap32_ldap_ufn2dn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_explode_dn(jitter):
    """
    PCHAR* ldap_explode_dn(
        PSTR dn,
        ULONG notypes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dn", "notypes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_explode_dn(jitter, get_str, set_str):
    """
    PTCHAR* ldap_explode_dn(
        PTSTR dn,
        ULONG notypes
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dn", "notypes"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_explode_dnA(jitter):
    wldap32_ldap_explode_dn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_explode_dnW(jitter):
    wldap32_ldap_explode_dn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_get_dn(jitter):
    """
    PCHAR ldap_get_dn(
        LDAP* ld,
        LDAPMessage* entry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_dn(jitter, get_str, set_str):
    """
    PTCHAR ldap_get_dn(
        LDAP* ld,
        LDAPMessage* entry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "entry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_get_dnA(jitter):
    wldap32_ldap_get_dn(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_get_dnW(jitter):
    wldap32_ldap_get_dn(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_conn_from_msg(jitter):
    """
    LDAP* ldap_conn_from_msg(
        LDAP* PrimaryConn,
        LDAPMessage* res
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["PrimaryConn", "res"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2(jitter):
    """
    ULONG ldap_modrdn2(
        LDAP* ExternalHandle,
        PCHAR DistinguishedName,
        PCHAR NewDistinguishedName,
        INT DeleteOldRdn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "NewDistinguishedName", "DeleteOldRdn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2(jitter, get_str, set_str):
    """
    ULONG ldap_modrdn2(
        LDAP* ExternalHandle,
        PTCHAR DistinguishedName,
        PTCHAR NewDistinguishedName,
        INT DeleteOldRdn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "NewDistinguishedName", "DeleteOldRdn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2A(jitter):
    wldap32_ldap_modrdn2(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_modrdn2W(jitter):
    wldap32_ldap_modrdn2(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_modrdn2_s(jitter):
    """
    LDAP_RETCODE ldap_modrdn2_s(
        LDAP* ExternalHandle,
        PCHAR DistinguishedName,
        PCHAR NewDistinguishedName,
        INT DeleteOldRdn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "NewDistinguishedName", "DeleteOldRdn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_modrdn2_s(
        LDAP* ExternalHandle,
        PTCHAR DistinguishedName,
        PTCHAR NewDistinguishedName,
        INT DeleteOldRdn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ExternalHandle", "DistinguishedName", "NewDistinguishedName", "DeleteOldRdn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_modrdn2_sA(jitter):
    wldap32_ldap_modrdn2_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_modrdn2_sW(jitter):
    wldap32_ldap_modrdn2_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_rename_ext(jitter):
    """
    LDAP_RETCODE ldap_rename_ext(
        LDAP* ld,
        PSTR dn,
        PSTR NewRDN,
        PSTR NewParent,
        INT DeleteOldRdn,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "NewRDN", "NewParent", "DeleteOldRdn", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_rename_ext(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_rename_ext(
        LDAP* ld,
        PTSTR dn,
        PTSTR NewRDN,
        PTSTR NewParent,
        INT DeleteOldRdn,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls,
        ULONG* MessageNumber
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "NewRDN", "NewParent", "DeleteOldRdn", "ServerControls", "ClientControls", "MessageNumber"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_rename_extA(jitter):
    wldap32_ldap_rename_ext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_rename_extW(jitter):
    wldap32_ldap_rename_ext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_ldap_rename_ext_s(jitter):
    """
    LDAP_RETCODE ldap_rename_ext_s(
        LDAP* ld,
        PSTR dn,
        PSTR NewRDN,
        PSTR NewParent,
        INT DeleteOldRdn,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "NewRDN", "NewParent", "DeleteOldRdn", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_rename_ext_s(jitter, get_str, set_str):
    """
    LDAP_RETCODE ldap_rename_ext_s(
        LDAP* ld,
        PTSTR dn,
        PTSTR NewRDN,
        PTSTR NewParent,
        INT DeleteOldRdn,
        PLDAPControl* ServerControls,
        PLDAPControl* ClientControls
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ld", "dn", "NewRDN", "NewParent", "DeleteOldRdn", "ServerControls", "ClientControls"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ldap_rename_ext_sA(jitter):
    wldap32_ldap_rename_ext_s(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def wldap32_ldap_rename_ext_sW(jitter):
    wldap32_ldap_rename_ext_s(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def wldap32_LdapUnicodeToUTF8(jitter):
    """
    int LdapUnicodeToUTF8(
        LPCWSTR lpSrcStr,
        int cchSrc,
        LPSTR lpDestStr,
        int cchDest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSrcStr", "cchSrc", "lpDestStr", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_LdapUTF8ToUnicode(jitter):
    """
    int LdapUTF8ToUnicode(
        LPCSTR lpSrcStr,
        int cchSrc,
        LPWSTR lpDestStr,
        int cchDest
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpSrcStr", "cchSrc", "lpDestStr", "cchDest"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_init(jitter):
    """
    BerElement* ber_init(
        BERVAL* pBerVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_free(jitter):
    """
    void ber_free(
        BerElement* pBerElement,
        INT fbuf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "fbuf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_bvfree(jitter):
    """
    void ber_bvfree(
        BERVAL* pBerVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_bvecfree(jitter):
    """
    void ber_bvecfree(
        PBERVAL* pBerVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_bvdup(jitter):
    """
    BERVAL* ber_bvdup(
        BERVAL* pBerVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_alloc_t(jitter):
    """
    BerElement* ber_alloc_t(
        INT options
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["options"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_skip_tag(jitter):
    """
    ULONG ber_skip_tag(
        BerElement* pBerElement,
        ULONG* pLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_peek_tag(jitter):
    """
    ULONG ber_peek_tag(
        BerElement* pBerElement,
        ULONG* pLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_first_element(jitter):
    """
    ULONG ber_first_element(
        BerElement* pBerElement,
        ULONG* pLen,
        CHAR** ppOpaque
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pLen", "ppOpaque"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_next_element(jitter):
    """
    ULONG ber_next_element(
        BerElement* pBerElement,
        ULONG* pLen,
        CHAR* opaque
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pLen", "opaque"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_flatten(jitter):
    """
    INT ber_flatten(
        BerElement* pBerElement,
        PBERVAL* pBerVal
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "pBerVal"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_printf(jitter):
    """
    INT ber_printf(
        BerElement* pBerElement,
        PCHAR fmt,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "fmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wldap32_ber_scanf(jitter):
    """
    INT ber_scanf(
        BerElement* pBerElement,
        PCHAR fmt,
        ...
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pBerElement", "fmt"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
