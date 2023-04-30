DOT11_BSS_TYPE = {
    "dot11_BSS_type_infrastructure": 1,
    "dot11_BSS_type_independent": 2,
    "dot11_BSS_type_any": 3,
}
DOT11_BSS_TYPE_INV = {
    1: "dot11_BSS_type_infrastructure",
    2: "dot11_BSS_type_independent",
    3: "dot11_BSS_type_any",
}
DOT11_PHY_TYPE = {
    "dot11_phy_type_unknown": 0,
    "dot11_phy_type_fhss": 1,
    "dot11_phy_type_dsss": 2,
    "dot11_phy_type_irbaseband": 3,
    "dot11_phy_type_ofdm": 4,
    "dot11_phy_type_hrdsss": 5,
    "dot11_phy_type_erp": 6,
    "dot11_phy_type_ht": 7,
}
DOT11_PHY_TYPE_INV = {
    0: "dot11_phy_type_unknown",
    1: "dot11_phy_type_fhss",
    2: "dot11_phy_type_dsss",
    3: "dot11_phy_type_irbaseband",
    4: "dot11_phy_type_ofdm",
    5: "dot11_phy_type_hrdsss",
    6: "dot11_phy_type_erp",
    7: "dot11_phy_type_ht",
}
DOT11_AUTH_ALGORITHM = {
    "DOT11_AUTH_ALGO_80211_OPEN": 1,
    "DOT11_AUTH_ALGO_80211_SHARED_KEY": 2,
    "DOT11_AUTH_ALGO_WPA": 3,
    "DOT11_AUTH_ALGO_WPA_PSK": 4,
    "DOT11_AUTH_ALGO_WPA_NONE": 5,
    "DOT11_AUTH_ALGO_RSNA": 6,
    "DOT11_AUTH_ALGO_RSNA_PSK": 7,
}
DOT11_AUTH_ALGORITHM_INV = {
    1: "DOT11_AUTH_ALGO_80211_OPEN",
    2: "DOT11_AUTH_ALGO_80211_SHARED_KEY",
    3: "DOT11_AUTH_ALGO_WPA",
    4: "DOT11_AUTH_ALGO_WPA_PSK",
    5: "DOT11_AUTH_ALGO_WPA_NONE",
    6: "DOT11_AUTH_ALGO_RSNA",
    7: "DOT11_AUTH_ALGO_RSNA_PSK",
}
DOT11_CIPHER_ALGORITHM = {
    "DOT11_CIPHER_ALGO_NONE": 0x00,
    "DOT11_CIPHER_ALGO_WEP40": 0x01,
    "DOT11_CIPHER_ALGO_TKIP": 0x02,
    "DOT11_CIPHER_ALGO_CCMP": 0x04,
    "DOT11_CIPHER_ALGO_WEP104": 0x05,
    "DOT11_CIPHER_ALGO_WPA_USE_GROUP": 0x100,
    "DOT11_CIPHER_ALGO_WEP": 0x101,
}
DOT11_CIPHER_ALGORITHM_INV = {
    0x00: "DOT11_CIPHER_ALGO_NONE",
    0x01: "DOT11_CIPHER_ALGO_WEP40",
    0x02: "DOT11_CIPHER_ALGO_TKIP",
    0x04: "DOT11_CIPHER_ALGO_CCMP",
    0x05: "DOT11_CIPHER_ALGO_WEP104",
    0x100: "DOT11_CIPHER_ALGO_WPA_USE_GROUP",
    0x101: "DOT11_CIPHER_ALGO_WEP",
}
_NDIS_OBJECT_TYPE_ = {
    "NDIS_OBJECT_TYPE_DEFAULT": 0x80,
    "NDIS_OBJECT_TYPE_MINIPORT_INIT_PARAMETERS": 0x81,
    "NDIS_OBJECT_TYPE_SG_DMA_DESCRIPTION": 0x83,
    "NDIS_OBJECT_TYPE_MINIPORT_INTERRUPT": 0x84,
    "NDIS_OBJECT_TYPE_DEVICE_OBJECT_ATTRIBUTES": 0x85,
    "NDIS_OBJECT_TYPE_BIND_PARAMETERS": 0x86,
    "NDIS_OBJECT_TYPE_OPEN_PARAMETERS": 0x87,
    "NDIS_OBJECT_TYPE_RSS_CAPABILITIES": 0x88,
    "NDIS_OBJECT_TYPE_RSS_PARAMETERS": 0x89,
    "NDIS_OBJECT_TYPE_MINIPORT_DRIVER_CHARACTERISTICS": 0x8A,
    "NDIS_OBJECT_TYPE_FILTER_DRIVER_CHARACTERISTICS": 0x8B,
    "NDIS_OBJECT_TYPE_FILTER_PARTIAL_CHARACTERISTICS": 0x8C,
    "NDIS_OBJECT_TYPE_FILTER_ATTRIBUTES": 0x8D,
    "NDIS_OBJECT_TYPE_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS": 0x8E,
    "NDIS_OBJECT_TYPE_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS": 0x8F,
    "NDIS_OBJECT_TYPE_CO_PROTOCOL_CHARACTERISTICS": 0x90,
    "NDIS_OBJECT_TYPE_CO_MINIPORT_CHARACTERISTICS": 0x91,
    "NDIS_OBJECT_TYPE_MINIPORT_PNP_CHARACTERISTICS": 0x92,
    "NDIS_OBJECT_TYPE_CLIENT_CHIMNEY_OFFLOAD_CHARACTERISTICS": 0x93,
    "NDIS_OBJECT_TYPE_PROVIDER_CHIMNEY_OFFLOAD_CHARACTERISTICS": 0x94,
    "NDIS_OBJECT_TYPE_PROTOCOL_DRIVER_CHARACTERISTICS": 0x95,
    "NDIS_OBJECT_TYPE_REQUEST_EX": 0x96,
    "NDIS_OBJECT_TYPE_OID_REQUEST": 0x96,
    "NDIS_OBJECT_TYPE_TIMER_CHARACTERISTICS": 0x97,
    "NDIS_OBJECT_TYPE_STATUS_INDICATION": 0x98,
    "NDIS_OBJECT_TYPE_FILTER_ATTACH_PARAMETERS": 0x99,
    "NDIS_OBJECT_TYPE_FILTER_PAUSE_PARAMETERS": 0x9A,
    "NDIS_OBJECT_TYPE_FILTER_RESTART_PARAMETERS": 0x9B,
    "NDIS_OBJECT_TYPE_PORT_CHARACTERISTICS": 0x9C,
    "NDIS_OBJECT_TYPE_PORT_STATE": 0x9D,
    "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES": 0x9E,
    "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES": 0x9F,
    "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES": 0xA0,
    "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES": 0xA1,
    "NDIS_OBJECT_TYPE_RESTART_GENERAL_ATTRIBUTES": 0xA2,
    "NDIS_OBJECT_TYPE_PROTOCOL_RESTART_PARAMETERS": 0xA3,
    "NDIS_OBJECT_TYPE_MINIPORT_ADD_DEVICE_REGISTRATION_ATTRIBUTES": 0xA4,
    "NDIS_OBJECT_TYPE_CO_CALL_MANAGER_OPTIONAL_HANDLERS": 0xA5,
    "NDIS_OBJECT_TYPE_CO_CLIENT_OPTIONAL_HANDLERS": 0xA6,
    "NDIS_OBJECT_TYPE_OFFLOAD": 0xA7,
    "NDIS_OBJECT_TYPE_OFFLOAD_ENCAPSULATION": 0xA8,
    "NDIS_OBJECT_TYPE_CONFIGURATION_OBJECT": 0xA9,
    "NDIS_OBJECT_TYPE_DRIVER_WRAPPER_OBJECT": 0xAA,
    "NDIS_OBJECT_TYPE_HD_SPLIT_ATTRIBUTES": 0xAB,
    "NDIS_OBJECT_TYPE_NSI_NETWORK_RW_STRUCT": 0xAC,
    "NDIS_OBJECT_TYPE_NSI_COMPARTMENT_RW_STRUCT": 0xAD,
    "NDIS_OBJECT_TYPE_NSI_INTERFACE_PERSIST_RW_STRUCT": 0xAE,
    "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES": 0xAF,
    "NDIS_OBJECT_TYPE_SHARED_MEMORY_PROVIDER_CHARACTERISTICS": 0xB0,
    "NDIS_OBJECT_TYPE_RSS_PROCESSOR_INFO": 0xB1,
}
_NDIS_OBJECT_TYPE__INV = {
    0x80: "NDIS_OBJECT_TYPE_DEFAULT",
    0x81: "NDIS_OBJECT_TYPE_MINIPORT_INIT_PARAMETERS",
    0x83: "NDIS_OBJECT_TYPE_SG_DMA_DESCRIPTION",
    0x84: "NDIS_OBJECT_TYPE_MINIPORT_INTERRUPT",
    0x85: "NDIS_OBJECT_TYPE_DEVICE_OBJECT_ATTRIBUTES",
    0x86: "NDIS_OBJECT_TYPE_BIND_PARAMETERS",
    0x87: "NDIS_OBJECT_TYPE_OPEN_PARAMETERS",
    0x88: "NDIS_OBJECT_TYPE_RSS_CAPABILITIES",
    0x89: "NDIS_OBJECT_TYPE_RSS_PARAMETERS",
    0x8A: "NDIS_OBJECT_TYPE_MINIPORT_DRIVER_CHARACTERISTICS",
    0x8B: "NDIS_OBJECT_TYPE_FILTER_DRIVER_CHARACTERISTICS",
    0x8C: "NDIS_OBJECT_TYPE_FILTER_PARTIAL_CHARACTERISTICS",
    0x8D: "NDIS_OBJECT_TYPE_FILTER_ATTRIBUTES",
    0x8E: "NDIS_OBJECT_TYPE_CLIENT_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS",
    0x8F: "NDIS_OBJECT_TYPE_PROVIDER_CHIMNEY_OFFLOAD_GENERIC_CHARACTERISTICS",
    0x90: "NDIS_OBJECT_TYPE_CO_PROTOCOL_CHARACTERISTICS",
    0x91: "NDIS_OBJECT_TYPE_CO_MINIPORT_CHARACTERISTICS",
    0x92: "NDIS_OBJECT_TYPE_MINIPORT_PNP_CHARACTERISTICS",
    0x93: "NDIS_OBJECT_TYPE_CLIENT_CHIMNEY_OFFLOAD_CHARACTERISTICS",
    0x94: "NDIS_OBJECT_TYPE_PROVIDER_CHIMNEY_OFFLOAD_CHARACTERISTICS",
    0x95: "NDIS_OBJECT_TYPE_PROTOCOL_DRIVER_CHARACTERISTICS",
    0x96: "NDIS_OBJECT_TYPE_REQUEST_EX",
    0x96: "NDIS_OBJECT_TYPE_OID_REQUEST",
    0x97: "NDIS_OBJECT_TYPE_TIMER_CHARACTERISTICS",
    0x98: "NDIS_OBJECT_TYPE_STATUS_INDICATION",
    0x99: "NDIS_OBJECT_TYPE_FILTER_ATTACH_PARAMETERS",
    0x9A: "NDIS_OBJECT_TYPE_FILTER_PAUSE_PARAMETERS",
    0x9B: "NDIS_OBJECT_TYPE_FILTER_RESTART_PARAMETERS",
    0x9C: "NDIS_OBJECT_TYPE_PORT_CHARACTERISTICS",
    0x9D: "NDIS_OBJECT_TYPE_PORT_STATE",
    0x9E: "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_REGISTRATION_ATTRIBUTES",
    0x9F: "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES",
    0xA0: "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_OFFLOAD_ATTRIBUTES",
    0xA1: "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_NATIVE_802_11_ATTRIBUTES",
    0xA2: "NDIS_OBJECT_TYPE_RESTART_GENERAL_ATTRIBUTES",
    0xA3: "NDIS_OBJECT_TYPE_PROTOCOL_RESTART_PARAMETERS",
    0xA4: "NDIS_OBJECT_TYPE_MINIPORT_ADD_DEVICE_REGISTRATION_ATTRIBUTES",
    0xA5: "NDIS_OBJECT_TYPE_CO_CALL_MANAGER_OPTIONAL_HANDLERS",
    0xA6: "NDIS_OBJECT_TYPE_CO_CLIENT_OPTIONAL_HANDLERS",
    0xA7: "NDIS_OBJECT_TYPE_OFFLOAD",
    0xA8: "NDIS_OBJECT_TYPE_OFFLOAD_ENCAPSULATION",
    0xA9: "NDIS_OBJECT_TYPE_CONFIGURATION_OBJECT",
    0xAA: "NDIS_OBJECT_TYPE_DRIVER_WRAPPER_OBJECT",
    0xAB: "NDIS_OBJECT_TYPE_HD_SPLIT_ATTRIBUTES",
    0xAC: "NDIS_OBJECT_TYPE_NSI_NETWORK_RW_STRUCT",
    0xAD: "NDIS_OBJECT_TYPE_NSI_COMPARTMENT_RW_STRUCT",
    0xAE: "NDIS_OBJECT_TYPE_NSI_INTERFACE_PERSIST_RW_STRUCT",
    0xAF: "NDIS_OBJECT_TYPE_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES",
    0xB0: "NDIS_OBJECT_TYPE_SHARED_MEMORY_PROVIDER_CHARACTERISTICS",
    0xB1: "NDIS_OBJECT_TYPE_RSS_PROCESSOR_INFO",
}
WLAN_INTERFACE_STATE = {
    "wlan_interface_state_not_ready": 0,
    "wlan_interface_state_connected": 1,
    "wlan_interface_state_ad_hoc_network_formed": 2,
    "wlan_interface_state_disconnecting": 3,
    "wlan_interface_state_disconnected": 4,
    "wlan_interface_state_associating": 5,
    "wlan_interface_state_discovering": 6,
    "wlan_interface_state_authenticating": 7,
}
WLAN_INTERFACE_STATE_INV = {
    0: "wlan_interface_state_not_ready",
    1: "wlan_interface_state_connected",
    2: "wlan_interface_state_ad_hoc_network_formed",
    3: "wlan_interface_state_disconnecting",
    4: "wlan_interface_state_disconnected",
    5: "wlan_interface_state_associating",
    6: "wlan_interface_state_discovering",
    7: "wlan_interface_state_authenticating",
}
WLAN_INTERFACE_TYPE = {
    "wlan_interface_type_emulated_802_11": 0,
    "wlan_interface_type_native_802_11": 1,
    "wlan_interface_type_invalid": 2,
}
WLAN_INTERFACE_TYPE_INV = {
    0: "wlan_interface_type_emulated_802_11",
    1: "wlan_interface_type_native_802_11",
    2: "wlan_interface_type_invalid",
}
WLAN_HOSTED_NETWORK_STATE = {
    "wlan_hosted_network_unavailable": 0,
    "wlan_hosted_network_idle": 1,
    "wlan_hosted_network_active": 2,
}
WLAN_HOSTED_NETWORK_STATE_INV = {
    0: "wlan_hosted_network_unavailable",
    1: "wlan_hosted_network_idle",
    2: "wlan_hosted_network_active",
}
WLAN_HOSTED_NETWORK_PEER_AUTH_STATE = {
    "wlan_hosted_network_peer_state_invalid": 0,
    "wlan_hosted_network_peer_state_authenticated": 1,
}
WLAN_HOSTED_NETWORK_PEER_AUTH_STATE_INV = {
    0: "wlan_hosted_network_peer_state_invalid",
    1: "wlan_hosted_network_peer_state_authenticated",
}
WLAN_CONNECTION_MODE = {
    "wlan_connection_mode_profile": 0,
    "wlan_connection_mode_temporary_profile": 1,
    "wlan_connection_mode_discovery_secure": 2,
    "wlan_connection_mode_discovery_unsecure": 3,
    "wlan_connection_mode_auto": 4,
    "wlan_connection_mode_invalid": 5,
}
WLAN_CONNECTION_MODE_INV = {
    0: "wlan_connection_mode_profile",
    1: "wlan_connection_mode_temporary_profile",
    2: "wlan_connection_mode_discovery_secure",
    3: "wlan_connection_mode_discovery_unsecure",
    4: "wlan_connection_mode_auto",
    5: "wlan_connection_mode_invalid",
}
WLAN_OPCODE_VALUE_TYPE = {
    "wlan_opcode_value_type_query_only": 0,
    "wlan_opcode_value_type_set_by_group_policy": 1,
    "wlan_opcode_value_type_set_by_user": 2,
    "wlan_opcode_value_type_invalid": 3,
}
WLAN_OPCODE_VALUE_TYPE_INV = {
    0: "wlan_opcode_value_type_query_only",
    1: "wlan_opcode_value_type_set_by_group_policy",
    2: "wlan_opcode_value_type_set_by_user",
    3: "wlan_opcode_value_type_invalid",
}
WLAN_FILTER_LIST_TYPE = {
    "wlan_filter_list_type_gp_permit": 0,
    "wlan_filter_list_type_gp_deny": 1,
    "wlan_filter_list_type_user_permit": 2,
    "wlan_filter_list_type_user_deny": 3,
}
WLAN_FILTER_LIST_TYPE_INV = {
    0: "wlan_filter_list_type_gp_permit",
    1: "wlan_filter_list_type_gp_deny",
    2: "wlan_filter_list_type_user_permit",
    3: "wlan_filter_list_type_user_deny",
}
WLAN_SECURABLE_OBJECT = {
    "wlan_secure_permit_list": 0,
    "wlan_secure_deny_list": 1,
    "wlan_secure_ac_enabled": 2,
    "wlan_secure_bc_scan_enabled": 3,
    "wlan_secure_bss_type": 4,
    "wlan_secure_show_denied": 5,
    "wlan_secure_interface_properties": 6,
    "wlan_secure_ihv_control": 7,
    "wlan_secure_all_user_profiles_order": 8,
    "wlan_secure_add_new_all_user_profiles": 9,
    "wlan_secure_add_new_per_user_profiles": 10,
    "wlan_secure_media_streaming_mode_enabled": 11,
    "wlan_secure_current_operation_mode": 12,
}
WLAN_SECURABLE_OBJECT_INV = {
    0: "wlan_secure_permit_list",
    1: "wlan_secure_deny_list",
    2: "wlan_secure_ac_enabled",
    3: "wlan_secure_bc_scan_enabled",
    4: "wlan_secure_bss_type",
    5: "wlan_secure_show_denied",
    6: "wlan_secure_interface_properties",
    7: "wlan_secure_ihv_control",
    8: "wlan_secure_all_user_profiles_order",
    9: "wlan_secure_add_new_all_user_profiles",
    10: "wlan_secure_add_new_per_user_profiles",
    11: "wlan_secure_media_streaming_mode_enabled",
    12: "wlan_secure_current_operation_mode",
}
WLAN_HOSTED_NETWORK_REASON = {
    "wlan_hosted_network_reason_success": 0,
    "wlan_hosted_network_reason_unspecified": 1,
    "wlan_hosted_network_reason_bad_parameters": 2,
    "wlan_hosted_network_reason_service_shutting_down": 3,
    "wlan_hosted_network_reason_insufficient_resources": 4,
    "wlan_hosted_network_reason_elevation_required": 5,
    "wlan_hosted_network_reason_read_only": 6,
    "wlan_hosted_network_reason_persistence_failed": 7,
    "wlan_hosted_network_reason_crypt_error": 8,
    "wlan_hosted_network_reason_impersonation": 9,
    "wlan_hosted_network_reason_stop_before_start": 10,
    "wlan_hosted_network_reason_interface_available": 11,
    "wlan_hosted_network_reason_interface_unavailable": 12,
    "wlan_hosted_network_reason_miniport_stopped": 13,
    "wlan_hosted_network_reason_miniport_started": 14,
    "wlan_hosted_network_reason_incompatible_connection_started": 15,
    "wlan_hosted_network_reason_incompatible_connection_stopped": 16,
    "wlan_hosted_network_reason_user_action": 17,
    "wlan_hosted_network_reason_client_abort": 18,
    "wlan_hosted_network_reason_ap_start_failed": 19,
    "wlan_hosted_network_reason_peer_arrived": 20,
    "wlan_hosted_network_reason_peer_departed": 21,
    "wlan_hosted_network_reason_peer_timeout": 22,
    "wlan_hosted_network_reason_gp_denied": 23,
    "wlan_hosted_network_reason_service_unavailable": 24,
    "wlan_hosted_network_reason_device_change": 25,
    "wlan_hosted_network_reason_properties_change": 26,
    "wlan_hosted_network_reason_virtual_station_blocking_use": 27,
    "wlan_hosted_network_reason_service_available_on_virtual_station": 28,
}
WLAN_HOSTED_NETWORK_REASON_INV = {
    0: "wlan_hosted_network_reason_success",
    1: "wlan_hosted_network_reason_unspecified",
    2: "wlan_hosted_network_reason_bad_parameters",
    3: "wlan_hosted_network_reason_service_shutting_down",
    4: "wlan_hosted_network_reason_insufficient_resources",
    5: "wlan_hosted_network_reason_elevation_required",
    6: "wlan_hosted_network_reason_read_only",
    7: "wlan_hosted_network_reason_persistence_failed",
    8: "wlan_hosted_network_reason_crypt_error",
    9: "wlan_hosted_network_reason_impersonation",
    10: "wlan_hosted_network_reason_stop_before_start",
    11: "wlan_hosted_network_reason_interface_available",
    12: "wlan_hosted_network_reason_interface_unavailable",
    13: "wlan_hosted_network_reason_miniport_stopped",
    14: "wlan_hosted_network_reason_miniport_started",
    15: "wlan_hosted_network_reason_incompatible_connection_started",
    16: "wlan_hosted_network_reason_incompatible_connection_stopped",
    17: "wlan_hosted_network_reason_user_action",
    18: "wlan_hosted_network_reason_client_abort",
    19: "wlan_hosted_network_reason_ap_start_failed",
    20: "wlan_hosted_network_reason_peer_arrived",
    21: "wlan_hosted_network_reason_peer_departed",
    22: "wlan_hosted_network_reason_peer_timeout",
    23: "wlan_hosted_network_reason_gp_denied",
    24: "wlan_hosted_network_reason_service_unavailable",
    25: "wlan_hosted_network_reason_device_change",
    26: "wlan_hosted_network_reason_properties_change",
    27: "wlan_hosted_network_reason_virtual_station_blocking_use",
    28: "wlan_hosted_network_reason_service_available_on_virtual_station",
}
WLAN_HOSTED_NETWORK_OPCODE = {
    "wlan_hosted_network_opcode_connection_settings": 0,
    "wlan_hosted_network_opcode_security_settings": 1,
    "wlan_hosted_network_opcode_station_profile": 2,
    "wlan_hosted_network_opcode_enable": 3,
}
WLAN_HOSTED_NETWORK_OPCODE_INV = {
    0: "wlan_hosted_network_opcode_connection_settings",
    1: "wlan_hosted_network_opcode_security_settings",
    2: "wlan_hosted_network_opcode_station_profile",
    3: "wlan_hosted_network_opcode_enable",
}
WLAN_IHV_CONTROL_TYPE = {
    "wlan_ihv_control_type_service": 0,
    "wlan_ihv_control_type_driver": 1,
}
WLAN_IHV_CONTROL_TYPE_INV = {
    0: "wlan_ihv_control_type_service",
    1: "wlan_ihv_control_type_driver",
}
WLAN_AUTOCONF_OPCODE = {
    "wlan_autoconf_opcode_start": 0,
    "wlan_autoconf_opcode_show_denied_networks": 1,
    "wlan_autoconf_opcode_power_setting": 2,
    "wlan_autoconf_opcode_only_use_gp_profiles_for_allowed_networks": 3,
    "wlan_autoconf_opcode_allow_explicit_creds": 4,
    "wlan_autoconf_opcode_block_period": 5,
    "wlan_autoconf_opcode_allow_virtual_station_extensibility": 6,
    "wlan_autoconf_opcode_end": 7,
}
WLAN_AUTOCONF_OPCODE_INV = {
    0: "wlan_autoconf_opcode_start",
    1: "wlan_autoconf_opcode_show_denied_networks",
    2: "wlan_autoconf_opcode_power_setting",
    3: "wlan_autoconf_opcode_only_use_gp_profiles_for_allowed_networks",
    4: "wlan_autoconf_opcode_allow_explicit_creds",
    5: "wlan_autoconf_opcode_block_period",
    6: "wlan_autoconf_opcode_allow_virtual_station_extensibility",
    7: "wlan_autoconf_opcode_end",
}
WLAN_INTF_OPCODE = {
    "wlan_intf_opcode_autoconf_enabled": 1,
    "wlan_intf_opcode_background_scan_enabled": 2,
    "wlan_intf_opcode_media_streaming_mode": 3,
    "wlan_intf_opcode_radio_state": 4,
    "wlan_intf_opcode_bss_type": 5,
    "wlan_intf_opcode_interface_state": 6,
    "wlan_intf_opcode_current_connection": 7,
    "wlan_intf_opcode_channel_number": 8,
    "wlan_intf_opcode_supported_infrastructure_auth_cipher_pairs": 9,
    "wlan_intf_opcode_supported_adhoc_auth_cipher_pairs": 10,
    "wlan_intf_opcode_supported_country_or_region_string_list": 11,
    "wlan_intf_opcode_current_operation_mode": 12,
    "wlan_intf_opcode_supported_safe_mode": 13,
    "wlan_intf_opcode_certified_safe_mode": 14,
    "wlan_intf_opcode_hosted_network_capable": 15,
    "wlan_intf_opcode_statistics": 0x10000101,
    "wlan_intf_opcode_rssi": 0x10000102,
}
WLAN_INTF_OPCODE_INV = {
    1: "wlan_intf_opcode_autoconf_enabled",
    2: "wlan_intf_opcode_background_scan_enabled",
    3: "wlan_intf_opcode_media_streaming_mode",
    4: "wlan_intf_opcode_radio_state",
    5: "wlan_intf_opcode_bss_type",
    6: "wlan_intf_opcode_interface_state",
    7: "wlan_intf_opcode_current_connection",
    8: "wlan_intf_opcode_channel_number",
    9: "wlan_intf_opcode_supported_infrastructure_auth_cipher_pairs",
    10: "wlan_intf_opcode_supported_adhoc_auth_cipher_pairs",
    11: "wlan_intf_opcode_supported_country_or_region_string_list",
    12: "wlan_intf_opcode_current_operation_mode",
    13: "wlan_intf_opcode_supported_safe_mode",
    14: "wlan_intf_opcode_certified_safe_mode",
    15: "wlan_intf_opcode_hosted_network_capable",
    0x10000101: "wlan_intf_opcode_statistics",
    0x10000102: "wlan_intf_opcode_rssi",
}

def wlanapi_WlanAllocateMemory(jitter):
    """
    PVOID WlanAllocateMemory(
        DWORD dwMemorySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwMemorySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanCloseHandle(jitter):
    """
    [ERROR_CODE] WlanCloseHandle(
        HANDLE hClientHandle,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanConnect(jitter):
    """
    [ERROR_CODE] WlanConnect(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        const PWLAN_CONNECTION_PARAMETERS pConnectionParameters,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pConnectionParameters", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanDeleteProfile(jitter):
    """
    [ERROR_CODE] WlanDeleteProfile(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        LPCWSTR strProfileName,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanDisconnect(jitter):
    """
    [ERROR_CODE] WlanDisconnect(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanEnumInterfaces(jitter):
    """
    [ERROR_CODE] WlanEnumInterfaces(
        HANDLE hClientHandle,
        PVOID pReserved,
        PWLAN_INTERFACE_INFO_LIST* ppInterfaceList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pReserved", "ppInterfaceList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanExtractPsdIEDataList(jitter):
    """
    [ERROR_CODE] WlanExtractPsdIEDataList(
        HANDLE hClientHandle,
        DWORD dwIeDataSize,
        const PBYTE pRawIeData,
        LPCWSTR strFormat,
        PVOID pReserved,
        PWLAN_RAW_DATA_LIST* ppPsdIEDataList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "dwIeDataSize", "pRawIeData", "strFormat", "pReserved", "ppPsdIEDataList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanFreeMemory(jitter):
    """
    VOID WlanFreeMemory(
        PVOID pMemory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pMemory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetAvailableNetworkList(jitter):
    """
    [ERROR_CODE] WlanGetAvailableNetworkList(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        [WlanAvailableFlags] dwFlags,
        PVOID pReserved,
        PWLAN_AVAILABLE_NETWORK_LIST* ppAvailableNetworkList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "dwFlags", "pReserved", "ppAvailableNetworkList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetFilterList(jitter):
    """
    [ERROR_CODE] WlanGetFilterList(
        HANDLE hClientHandle,
        WLAN_FILTER_LIST_TYPE wlanFilterListType,
        PVOID pReserved,
        PDOT11_NETWORK_LIST* ppNetworkList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "wlanFilterListType", "pReserved", "ppNetworkList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetInterfaceCapability(jitter):
    """
    [ERROR_CODE] WlanGetInterfaceCapability(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        PVOID pReserved,
        PWLAN_INTERFACE_CAPABILITY* ppCapability
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pReserved", "ppCapability"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetNetworkBssList(jitter):
    """
    [ERROR_CODE] WlanGetNetworkBssList(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        const PDOT11_SSID pDot11Ssid,
        DOT11_BSS_TYPE dot11BssType,
        BOOL bSecurityEnabled,
        PVOID pReserved,
        PWLAN_BSS_LIST* ppWlanBssList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pDot11Ssid", "dot11BssType", "bSecurityEnabled", "pReserved", "ppWlanBssList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetProfile(jitter):
    """
    [ERROR_CODE] WlanGetProfile(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        LPCWSTR strProfileName,
        PVOID pReserved,
        LPWSTR* pstrProfileXml,
        [WlanProfileFlags*] pdwFlags,
        [WlanAccess*] pdwGrantedAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "pReserved", "pstrProfileXml", "pdwFlags", "pdwGrantedAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetProfileCustomUserData(jitter):
    """
    [ERROR_CODE] WlanGetProfileCustomUserData(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        LPCWSTR strProfileName,
        PVOID pReserved,
        DWORD* pdwDataSize,
        PBYTE* ppData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "pReserved", "pdwDataSize", "ppData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetProfileList(jitter):
    """
    [ERROR_CODE] WlanGetProfileList(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        PVOID pReserved,
        PWLAN_PROFILE_INFO_LIST* ppProfileList
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pReserved", "ppProfileList"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanGetSecuritySettings(jitter):
    """
    [ERROR_CODE] WlanGetSecuritySettings(
        HANDLE hClientHandle,
        WLAN_SECURABLE_OBJECT SecurableObject,
        PWLAN_OPCODE_VALUE_TYPE pValueType,
        LPWSTR* pstrCurrentSDDL,
        [WlanAccess*] pdwGrantedAccess
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "SecurableObject", "pValueType", "pstrCurrentSDDL", "pdwGrantedAccess"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanIhvControl(jitter):
    """
    [ERROR_CODE] WlanIhvControl(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        WLAN_IHV_CONTROL_TYPE Type,
        DWORD dwInBufferSize,
        PVOID pInBuffer,
        DWORD dwOutBufferSize,
        PVOID pOutBuffer,
        PDWORD pdwBytesReturned
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "Type", "dwInBufferSize", "pInBuffer", "dwOutBufferSize", "pOutBuffer", "pdwBytesReturned"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanOpenHandle(jitter):
    """
    [ERROR_CODE] WlanOpenHandle(
        DWORD dwClientVersion,
        PVOID pReserved,
        PDWORD pdwNegotiatedVersion,
        PHANDLE phClientHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwClientVersion", "pReserved", "pdwNegotiatedVersion", "phClientHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanQueryAutoConfigParameter(jitter):
    """
    [ERROR_CODE] WlanQueryAutoConfigParameter(
        HANDLE hClientHandle,
        WLAN_AUTOCONF_OPCODE OpCode,
        PVOID pReserved,
        PDWORD pdwDataSize,
        PVOID ppData,
        PWLAN_OPCODE_VALUE_TYPE pWlanOpcodeValueType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "OpCode", "pReserved", "pdwDataSize", "ppData", "pWlanOpcodeValueType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanQueryInterface(jitter):
    """
    [ERROR_CODE] WlanQueryInterface(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        WLAN_INTF_OPCODE OpCode,
        PVOID pReserved,
        PDWORD pdwDataSize,
        PVOID* ppData,
        PWLAN_OPCODE_VALUE_TYPE pWlanOpcodeValueType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "OpCode", "pReserved", "pdwDataSize", "ppData", "pWlanOpcodeValueType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanReasonCodeToString(jitter):
    """
    [ERROR_CODE] WlanReasonCodeToString(
        DWORD dwReasonCode,
        DWORD dwBufferSize,
        PWCHAR pStringBuffer,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwReasonCode", "dwBufferSize", "pStringBuffer", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanRegisterNotification(jitter):
    """
    [ERROR_CODE] WlanRegisterNotification(
        HANDLE hClientHandle,
        [WlanNotificationSource] dwNotifSource,
        BOOL bIgnoreDuplicate,
        WLAN_NOTIFICATION_CALLBACK funcCallback,
        PVOID pCallbackContext,
        PVOID pReserved,
        [WlanNotificationSource*] pdwPrevNotifSource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "dwNotifSource", "bIgnoreDuplicate", "funcCallback", "pCallbackContext", "pReserved", "pdwPrevNotifSource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanRenameProfile(jitter):
    """
    [ERROR_CODE] WlanRenameProfile(
        HANDLE hClientHandle,
        CONST GUID* pInterfaceGuid,
        LPCWSTR strOldProfileName,
        LPCWSTR strNewProfileName,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strOldProfileName", "strNewProfileName", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSaveTemporaryProfile(jitter):
    """
    [ERROR_CODE] WlanSaveTemporaryProfile(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        LPCWSTR strProfileName,
        LPCWSTR strAllUserProfileSecurity,
        [WlanProfileFlags] dwFlags,
        BOOL bOverWrite,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "strAllUserProfileSecurity", "dwFlags", "bOverWrite", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanScan(jitter):
    """
    [ERROR_CODE] WlanScan(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        const PDOT11_SSID pDot11Ssid,
        const PWLAN_RAW_DATA pIeData,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "pDot11Ssid", "pIeData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetAutoConfigParameter(jitter):
    """
    [ERROR_CODE] WlanSetAutoConfigParameter(
        HANDLE hClientHandle,
        WLAN_AUTOCONF_OPCODE OpCode,
        DWORD dwDataSize,
        const PVOID pData,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "OpCode", "dwDataSize", "pData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetFilterList(jitter):
    """
    [ERROR_CODE] WlanSetFilterList(
        HANDLE hClientHandle,
        WLAN_FILTER_LIST_TYPE wlanFilterListType,
        const PDOT11_NETWORK_LIST pNetworkList,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "wlanFilterListType", "pNetworkList", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetInterface(jitter):
    """
    [ERROR_CODE] WlanSetInterface(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        WLAN_INTF_OPCODE OpCode,
        DWORD dwDataSize,
        const PVOID pData,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "OpCode", "dwDataSize", "pData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfile(jitter):
    """
    [ERROR_CODE] WlanSetProfile(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        DWORD dwFlags,
        LPCWSTR strProfileXml,
        LPCWSTR strAllUserProfileSecurity,
        BOOL bOverwrite,
        PVOID pReserved,
        DWORD* pdwReasonCode
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "dwFlags", "strProfileXml", "strAllUserProfileSecurity", "bOverwrite", "pReserved", "pdwReasonCode"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfileCustomUserData(jitter):
    """
    [ERROR_CODE] WlanSetProfileCustomUserData(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        LPCWSTR strProfileName,
        DWORD dwDataSize,
        const PBYTE pData,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "dwDataSize", "pData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfileEapUserData(jitter):
    """
    [ERROR_CODE] WlanSetProfileEapUserData(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        LPCWSTR strProfileName,
        EAP_METHOD_TYPE eapType,
        DWORD dwFlags,
        DWORD dwEapUserDataSize,
        const LPBYTE pbEapUserData,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "eapType", "dwFlags", "dwEapUserDataSize", "pbEapUserData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfileEapXmlUserData(jitter):
    """
    [ERROR_CODE] WlanSetProfileEapXmlUserData(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        LPCWSTR strProfileName,
        DWORD dwFlags,
        LPCWSTR strEapXmlUserData,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "dwFlags", "strEapXmlUserData", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfileList(jitter):
    """
    [ERROR_CODE] WlanSetProfileList(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        DWORD dwItems,
        LPCWSTR* strProfileNames,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "dwItems", "strProfileNames", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetProfilePosition(jitter):
    """
    [ERROR_CODE] WlanSetProfilePosition(
        HANDLE hClientHandle,
        const GUID* pInterfaceGuid,
        LPCWSTR strProfileName,
        DWORD dwPosition,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pInterfaceGuid", "strProfileName", "dwPosition", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetPsdIEDataList(jitter):
    """
    [ERROR_CODE] WlanSetPsdIEDataList(
        HANDLE hClientHandle,
        LPCWSTR strFormat,
        const PWLAN_RAW_DATA_LIST pPsdIEDataList,
        PVOID pReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "strFormat", "pPsdIEDataList", "pReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanSetSecuritySettings(jitter):
    """
    [ERROR_CODE] WlanSetSecuritySettings(
        HANDLE hClientHandle,
        WLAN_SECURABLE_OBJECT SecurableObject,
        LPCWSTR strModifiedSDDL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "SecurableObject", "strModifiedSDDL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDCancelOpenSession(jitter):
    """
    [ERROR_CODE] WFDCancelOpenSession(
        PHANDLE hSessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDCloseHandle(jitter):
    """
    [ERROR_CODE] WFDCloseHandle(
        HANDLE hClientHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDCloseSession(jitter):
    """
    [ERROR_CODE] WFDCloseSession(
        PHANDLE hSessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDOpenHandle(jitter):
    """
    [ERROR_CODE] WFDOpenHandle(
        DWORD dwClientVersion,
        PDWORD pdwNegotiatedVersion,
        PHANDLE phClientHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwClientVersion", "pdwNegotiatedVersion", "phClientHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDOpenLegacySession(jitter):
    """
    [ERROR_CODE] WFDOpenLegacySession(
        HANDLE hClientHandle,
        PDOT11_MAC_ADDRESS pLegacyMacAddress,
        HANDLE phSessionHandle,
        GUID pGuidSessionInterface
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pLegacyMacAddress", "phSessionHandle", "pGuidSessionInterface"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDStartOpenSession(jitter):
    """
    [ERROR_CODE] WFDStartOpenSession(
        HANDLE hClientHandle,
        PDOT11_MAC_ADDRESS pDeviceAddress,
        PVOID pvContext,
        WFD_OPEN_SESSION_COMPLETE_CALLBACK pfnCallback,
        PHANDLE phSessionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pDeviceAddress", "pvContext", "pfnCallback", "phSessionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WFDUpdateDeviceVisibility(jitter):
    """
    [ERROR_CODE] WFDUpdateDeviceVisibility(
        PDOT11_MAC_ADDRESS pDeviceAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDeviceAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkForceStart(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkForceStart(
        HANDLE hClientHandle,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkForceStop(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkForceStop(
        HANDLE hClientHandle,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkInitSettings(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkInitSettings(
        HANDLE hClientHandle,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkQueryProperty(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkQueryProperty(
        HANDLE hClientHandle,
        WLAN_HOSTED_NETWORK_OPCODE OpCode,
        PDWORD pdwDataSize,
        PVOID* ppvData,
        PWLAN_OPCODE_VALUE_TYPE* pWlanOpcodeValueType,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "OpCode", "pdwDataSize", "ppvData", "pWlanOpcodeValueType", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkQuerySecondaryKey(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkQuerySecondaryKey(
        HANDLE hClientHandle,
        DWORD pdwKeyLength,
        PUCHAR* ppucKeyData,
        PBOOL pbIsPassPhrase,
        PBOOL pbPersistent,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pdwKeyLength", "ppucKeyData", "pbIsPassPhrase", "pbPersistent", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkQueryStatus(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkQueryStatus(
        HANDLE hClientHandle,
        PWLAN_HOSTED_NETWORK_STATUS* ppWlanHostedNetworkStatus,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "ppWlanHostedNetworkStatus", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkRefreshSecuritySettings(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkRefreshSecuritySettings(
        HANDLE hClientHandle,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkSetProperty(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkSetProperty(
        HANDLE hClientHandle,
        WLAN_HOSTED_NETWORK_OPCODE OpCode,
        DWORD dwDataSize,
        PVOID pvData,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "OpCode", "dwDataSize", "pvData", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkSetSecondaryKey(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkSetSecondaryKey(
        HANDLE hClientHandle,
        DWORD dwKeyLength,
        PUCHAR pucKeyData,
        BOOL bIsPassPhrase,
        BOOL bPersistent,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "dwKeyLength", "pucKeyData", "bIsPassPhrase", "bPersistent", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkStartUsing(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkStartUsing(
        HANDLE hClientHandle,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanHostedNetworkStopUsing(jitter):
    """
    [ERROR_CODE] WlanHostedNetworkStopUsing(
        HANDLE hClientHandle,
        PWLAN_HOSTED_NETWORK_REASON pFailReason,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "pFailReason", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def wlanapi_WlanRegisterVirtualStationNotification(jitter):
    """
    [ERROR_CODE] WlanRegisterVirtualStationNotification(
        HANDLE hClientHandle,
        BOOL bRegister,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hClientHandle", "bRegister", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
