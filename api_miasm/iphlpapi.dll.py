###### Enums ######
IFTYPE = {
    "IF_TYPE_OTHER": 1,
    "IF_TYPE_REGULAR_1822": 2,
    "IF_TYPE_HDH_1822": 3,
    "IF_TYPE_DDN_X25": 4,
    "IF_TYPE_RFC877_X25": 5,
    "IF_TYPE_ETHERNET_CSMACD": 6,
    "IF_TYPE_IS088023_CSMACD": 7,
    "IF_TYPE_ISO88024_TOKENBUS": 8,
    "IF_TYPE_ISO88025_TOKENRING": 9,
    "IF_TYPE_ISO88026_MAN": 10,
    "IF_TYPE_STARLAN": 11,
    "IF_TYPE_PROTEON_10MBIT": 12,
    "IF_TYPE_PROTEON_80MBIT": 13,
    "IF_TYPE_HYPERCHANNEL": 14,
    "IF_TYPE_FDDI": 15,
    "IF_TYPE_LAP_B": 16,
    "IF_TYPE_SDLC": 17,
    "IF_TYPE_DS1": 18,
    "IF_TYPE_E1": 19,
    "IF_TYPE_BASIC_ISDN": 20,
    "IF_TYPE_PRIMARY_ISDN": 21,
    "IF_TYPE_PROP_POINT2POINT_SERIAL": 22,
    "IF_TYPE_PPP": 23,
    "IF_TYPE_SOFTWARE_LOOPBACK": 24,
    "IF_TYPE_EON": 25,
    "IF_TYPE_ETHERNET_3MBIT": 26,
    "IF_TYPE_NSIP": 27,
    "IF_TYPE_SLIP": 28,
    "IF_TYPE_ULTRA": 29,
    "IF_TYPE_DS3": 30,
    "IF_TYPE_SIP": 31,
    "IF_TYPE_FRAMERELAY": 32,
    "IF_TYPE_RS232": 33,
    "IF_TYPE_PARA": 34,
    "IF_TYPE_ARCNET": 35,
    "IF_TYPE_ARCNET_PLUS": 36,
    "IF_TYPE_ATM": 37,
    "IF_TYPE_MIO_X25": 38,
    "IF_TYPE_SONET": 39,
    "IF_TYPE_X25_PLE": 40,
    "IF_TYPE_ISO88022_LLC": 41,
    "IF_TYPE_LOCALTALK": 42,
    "IF_TYPE_SMDS_DXI": 43,
    "IF_TYPE_FRAMERELAY_SERVICE": 44,
    "IF_TYPE_V35": 45,
    "IF_TYPE_HSSI": 46,
    "IF_TYPE_HIPPI": 47,
    "IF_TYPE_MODEM": 48,
    "IF_TYPE_AAL5": 49,
    "IF_TYPE_SONET_PATH": 50,
    "IF_TYPE_SONET_VT": 51,
    "IF_TYPE_SMDS_ICIP": 52,
    "IF_TYPE_PROP_VIRTUAL": 53,
    "IF_TYPE_PROP_MULTIPLEXOR": 54,
    "IF_TYPE_IEEE80212": 55,
    "IF_TYPE_FIBRECHANNEL": 56,
    "IF_TYPE_HIPPIINTERFACE": 57,
    "IF_TYPE_FRAMERELAY_INTERCONNECT": 58,
    "IF_TYPE_AFLANE_8023": 59,
    "IF_TYPE_AFLANE_8025": 60,
    "IF_TYPE_CCTEMUL": 61,
    "IF_TYPE_FASTETHER": 62,
    "IF_TYPE_ISDN": 63,
    "IF_TYPE_V11": 64,
    "IF_TYPE_V36": 65,
    "IF_TYPE_G703_64K": 66,
    "IF_TYPE_G703_2MB": 67,
    "IF_TYPE_QLLC": 68,
    "IF_TYPE_FASTETHER_FX": 69,
    "IF_TYPE_CHANNEL": 70,
    "IF_TYPE_IEEE80211": 71,
    "IF_TYPE_IBM370PARCHAN": 72,
    "IF_TYPE_ESCON": 73,
    "IF_TYPE_DLSW": 74,
    "IF_TYPE_ISDN_S": 75,
    "IF_TYPE_ISDN_U": 76,
    "IF_TYPE_LAP_D": 77,
    "IF_TYPE_IPSWITCH": 78,
    "IF_TYPE_RSRB": 79,
    "IF_TYPE_ATM_LOGICAL": 80,
    "IF_TYPE_DS0": 81,
    "IF_TYPE_DS0_BUNDLE": 82,
    "IF_TYPE_BSC": 83,
    "IF_TYPE_ASYNC": 84,
    "IF_TYPE_CNR": 85,
    "IF_TYPE_ISO88025R_DTR": 86,
    "IF_TYPE_EPLRS": 87,
    "IF_TYPE_ARAP": 88,
    "IF_TYPE_PROP_CNLS": 89,
    "IF_TYPE_HOSTPAD": 90,
    "IF_TYPE_TERMPAD": 91,
    "IF_TYPE_FRAMERELAY_MPI": 92,
    "IF_TYPE_X213": 93,
    "IF_TYPE_ADSL": 94,
    "IF_TYPE_RADSL": 95,
    "IF_TYPE_SDSL": 96,
    "IF_TYPE_VDSL": 97,
    "IF_TYPE_ISO88025_CRFPRINT": 98,
    "IF_TYPE_MYRINET": 99,
    "IF_TYPE_VOICE_EM": 100,
    "IF_TYPE_VOICE_FXO": 101,
    "IF_TYPE_VOICE_FXS": 102,
    "IF_TYPE_VOICE_ENCAP": 103,
    "IF_TYPE_VOICE_OVERIP": 104,
    "IF_TYPE_ATM_DXI": 105,
    "IF_TYPE_ATM_FUNI": 106,
    "IF_TYPE_ATM_IMA": 107,
    "IF_TYPE_PPPMULTILINKBUNDLE": 108,
    "IF_TYPE_IPOVER_CDLC": 109,
    "IF_TYPE_IPOVER_CLAW": 110,
    "IF_TYPE_STACKTOSTACK": 111,
    "IF_TYPE_VIRTUALIPADDRESS": 112,
    "IF_TYPE_MPC": 113,
    "IF_TYPE_IPOVER_ATM": 114,
    "IF_TYPE_ISO88025_FIBER": 115,
    "IF_TYPE_TDLC": 116,
    "IF_TYPE_GIGABITETHERNET": 117,
    "IF_TYPE_HDLC": 118,
    "IF_TYPE_LAP_F": 119,
    "IF_TYPE_V37": 120,
    "IF_TYPE_X25_MLP": 121,
    "IF_TYPE_X25_HUNTGROUP": 122,
    "IF_TYPE_TRANSPHDLC": 123,
    "IF_TYPE_INTERLEAVE": 124,
    "IF_TYPE_FAST": 125,
    "IF_TYPE_IP": 126,
    "IF_TYPE_DOCSCABLE_MACLAYER": 127,
    "IF_TYPE_DOCSCABLE_DOWNSTREAM": 128,
    "IF_TYPE_DOCSCABLE_UPSTREAM": 129,
    "IF_TYPE_A12MPPSWITCH": 130,
    "IF_TYPE_TUNNEL": 131,
    "IF_TYPE_COFFEE": 132,
    "IF_TYPE_CES": 133,
    "IF_TYPE_ATM_SUBINTERFACE": 134,
    "IF_TYPE_L2_VLAN": 135,
    "IF_TYPE_L3_IPVLAN": 136,
    "IF_TYPE_L3_IPXVLAN": 137,
    "IF_TYPE_DIGITALPOWERLINE": 138,
    "IF_TYPE_MEDIAMAILOVERIP": 139,
    "IF_TYPE_DTM": 140,
    "IF_TYPE_DCN": 141,
    "IF_TYPE_IPFORWARD": 142,
    "IF_TYPE_MSDSL": 143,
    "IF_TYPE_IEEE1394": 144,
    "IF_TYPE_IF_GSN": 145,
    "IF_TYPE_DVBRCC_MACLAYER": 146,
    "IF_TYPE_DVBRCC_DOWNSTREAM": 147,
    "IF_TYPE_DVBRCC_UPSTREAM": 148,
    "IF_TYPE_ATM_VIRTUAL": 149,
    "IF_TYPE_MPLS_TUNNEL": 150,
    "IF_TYPE_SRP": 151,
    "IF_TYPE_VOICEOVERATM": 152,
    "IF_TYPE_VOICEOVERFRAMERELAY": 153,
    "IF_TYPE_IDSL": 154,
    "IF_TYPE_COMPOSITELINK": 155,
    "IF_TYPE_SS7_SIGLINK": 156,
    "IF_TYPE_PROP_WIRELESS_P2P": 157,
    "IF_TYPE_FR_FORWARD": 158,
    "IF_TYPE_RFC1483": 159,
    "IF_TYPE_USB": 160,
    "IF_TYPE_IEEE8023AD_LAG": 161,
    "IF_TYPE_BGP_POLICY_ACCOUNTING": 162,
    "IF_TYPE_FRF16_MFR_BUNDLE": 163,
    "IF_TYPE_H323_GATEKEEPER": 164,
    "IF_TYPE_H323_PROXY": 165,
    "IF_TYPE_MPLS": 166,
    "IF_TYPE_MF_SIGLINK": 167,
    "IF_TYPE_HDSL2": 168,
    "IF_TYPE_SHDSL": 169,
    "IF_TYPE_DS1_FDL": 170,
    "IF_TYPE_POS": 171,
    "IF_TYPE_DVB_ASI_IN": 172,
    "IF_TYPE_DVB_ASI_OUT": 173,
    "IF_TYPE_PLC": 174,
    "IF_TYPE_NFAS": 175,
    "IF_TYPE_TR008": 176,
    "IF_TYPE_GR303_RDT": 177,
    "IF_TYPE_GR303_IDT": 178,
    "IF_TYPE_ISUP": 179,
    "IF_TYPE_PROP_DOCS_WIRELESS_MACLAYER": 180,
    "IF_TYPE_PROP_DOCS_WIRELESS_DOWNSTREAM": 181,
    "IF_TYPE_PROP_DOCS_WIRELESS_UPSTREAM": 182,
    "IF_TYPE_HIPERLAN2": 183,
    "IF_TYPE_PROP_BWA_P2MP": 184,
    "IF_TYPE_SONET_OVERHEAD_CHANNEL": 185,
    "IF_TYPE_DIGITAL_WRAPPER_OVERHEAD_CHANNEL": 186,
    "IF_TYPE_AAL2": 187,
    "IF_TYPE_RADIO_MAC": 188,
    "IF_TYPE_ATM_RADIO": 189,
    "IF_TYPE_IMT": 190,
    "IF_TYPE_MVL": 191,
    "IF_TYPE_REACH_DSL": 192,
    "IF_TYPE_FR_DLCI_ENDPT": 193,
    "IF_TYPE_ATM_VCI_ENDPT": 194,
    "IF_TYPE_OPTICAL_CHANNEL": 195,
    "IF_TYPE_OPTICAL_TRANSPORT": 196,
    "IF_TYPE_IEEE80216_WMAN": 237,
    "IF_TYPE_WWANPP": 243,
    "IF_TYPE_WWANPP2": 244,
}
IFTYPE_INV = {
    1: "IF_TYPE_OTHER",
    2: "IF_TYPE_REGULAR_1822",
    3: "IF_TYPE_HDH_1822",
    4: "IF_TYPE_DDN_X25",
    5: "IF_TYPE_RFC877_X25",
    6: "IF_TYPE_ETHERNET_CSMACD",
    7: "IF_TYPE_IS088023_CSMACD",
    8: "IF_TYPE_ISO88024_TOKENBUS",
    9: "IF_TYPE_ISO88025_TOKENRING",
    10: "IF_TYPE_ISO88026_MAN",
    11: "IF_TYPE_STARLAN",
    12: "IF_TYPE_PROTEON_10MBIT",
    13: "IF_TYPE_PROTEON_80MBIT",
    14: "IF_TYPE_HYPERCHANNEL",
    15: "IF_TYPE_FDDI",
    16: "IF_TYPE_LAP_B",
    17: "IF_TYPE_SDLC",
    18: "IF_TYPE_DS1",
    19: "IF_TYPE_E1",
    20: "IF_TYPE_BASIC_ISDN",
    21: "IF_TYPE_PRIMARY_ISDN",
    22: "IF_TYPE_PROP_POINT2POINT_SERIAL",
    23: "IF_TYPE_PPP",
    24: "IF_TYPE_SOFTWARE_LOOPBACK",
    25: "IF_TYPE_EON",
    26: "IF_TYPE_ETHERNET_3MBIT",
    27: "IF_TYPE_NSIP",
    28: "IF_TYPE_SLIP",
    29: "IF_TYPE_ULTRA",
    30: "IF_TYPE_DS3",
    31: "IF_TYPE_SIP",
    32: "IF_TYPE_FRAMERELAY",
    33: "IF_TYPE_RS232",
    34: "IF_TYPE_PARA",
    35: "IF_TYPE_ARCNET",
    36: "IF_TYPE_ARCNET_PLUS",
    37: "IF_TYPE_ATM",
    38: "IF_TYPE_MIO_X25",
    39: "IF_TYPE_SONET",
    40: "IF_TYPE_X25_PLE",
    41: "IF_TYPE_ISO88022_LLC",
    42: "IF_TYPE_LOCALTALK",
    43: "IF_TYPE_SMDS_DXI",
    44: "IF_TYPE_FRAMERELAY_SERVICE",
    45: "IF_TYPE_V35",
    46: "IF_TYPE_HSSI",
    47: "IF_TYPE_HIPPI",
    48: "IF_TYPE_MODEM",
    49: "IF_TYPE_AAL5",
    50: "IF_TYPE_SONET_PATH",
    51: "IF_TYPE_SONET_VT",
    52: "IF_TYPE_SMDS_ICIP",
    53: "IF_TYPE_PROP_VIRTUAL",
    54: "IF_TYPE_PROP_MULTIPLEXOR",
    55: "IF_TYPE_IEEE80212",
    56: "IF_TYPE_FIBRECHANNEL",
    57: "IF_TYPE_HIPPIINTERFACE",
    58: "IF_TYPE_FRAMERELAY_INTERCONNECT",
    59: "IF_TYPE_AFLANE_8023",
    60: "IF_TYPE_AFLANE_8025",
    61: "IF_TYPE_CCTEMUL",
    62: "IF_TYPE_FASTETHER",
    63: "IF_TYPE_ISDN",
    64: "IF_TYPE_V11",
    65: "IF_TYPE_V36",
    66: "IF_TYPE_G703_64K",
    67: "IF_TYPE_G703_2MB",
    68: "IF_TYPE_QLLC",
    69: "IF_TYPE_FASTETHER_FX",
    70: "IF_TYPE_CHANNEL",
    71: "IF_TYPE_IEEE80211",
    72: "IF_TYPE_IBM370PARCHAN",
    73: "IF_TYPE_ESCON",
    74: "IF_TYPE_DLSW",
    75: "IF_TYPE_ISDN_S",
    76: "IF_TYPE_ISDN_U",
    77: "IF_TYPE_LAP_D",
    78: "IF_TYPE_IPSWITCH",
    79: "IF_TYPE_RSRB",
    80: "IF_TYPE_ATM_LOGICAL",
    81: "IF_TYPE_DS0",
    82: "IF_TYPE_DS0_BUNDLE",
    83: "IF_TYPE_BSC",
    84: "IF_TYPE_ASYNC",
    85: "IF_TYPE_CNR",
    86: "IF_TYPE_ISO88025R_DTR",
    87: "IF_TYPE_EPLRS",
    88: "IF_TYPE_ARAP",
    89: "IF_TYPE_PROP_CNLS",
    90: "IF_TYPE_HOSTPAD",
    91: "IF_TYPE_TERMPAD",
    92: "IF_TYPE_FRAMERELAY_MPI",
    93: "IF_TYPE_X213",
    94: "IF_TYPE_ADSL",
    95: "IF_TYPE_RADSL",
    96: "IF_TYPE_SDSL",
    97: "IF_TYPE_VDSL",
    98: "IF_TYPE_ISO88025_CRFPRINT",
    99: "IF_TYPE_MYRINET",
    100: "IF_TYPE_VOICE_EM",
    101: "IF_TYPE_VOICE_FXO",
    102: "IF_TYPE_VOICE_FXS",
    103: "IF_TYPE_VOICE_ENCAP",
    104: "IF_TYPE_VOICE_OVERIP",
    105: "IF_TYPE_ATM_DXI",
    106: "IF_TYPE_ATM_FUNI",
    107: "IF_TYPE_ATM_IMA",
    108: "IF_TYPE_PPPMULTILINKBUNDLE",
    109: "IF_TYPE_IPOVER_CDLC",
    110: "IF_TYPE_IPOVER_CLAW",
    111: "IF_TYPE_STACKTOSTACK",
    112: "IF_TYPE_VIRTUALIPADDRESS",
    113: "IF_TYPE_MPC",
    114: "IF_TYPE_IPOVER_ATM",
    115: "IF_TYPE_ISO88025_FIBER",
    116: "IF_TYPE_TDLC",
    117: "IF_TYPE_GIGABITETHERNET",
    118: "IF_TYPE_HDLC",
    119: "IF_TYPE_LAP_F",
    120: "IF_TYPE_V37",
    121: "IF_TYPE_X25_MLP",
    122: "IF_TYPE_X25_HUNTGROUP",
    123: "IF_TYPE_TRANSPHDLC",
    124: "IF_TYPE_INTERLEAVE",
    125: "IF_TYPE_FAST",
    126: "IF_TYPE_IP",
    127: "IF_TYPE_DOCSCABLE_MACLAYER",
    128: "IF_TYPE_DOCSCABLE_DOWNSTREAM",
    129: "IF_TYPE_DOCSCABLE_UPSTREAM",
    130: "IF_TYPE_A12MPPSWITCH",
    131: "IF_TYPE_TUNNEL",
    132: "IF_TYPE_COFFEE",
    133: "IF_TYPE_CES",
    134: "IF_TYPE_ATM_SUBINTERFACE",
    135: "IF_TYPE_L2_VLAN",
    136: "IF_TYPE_L3_IPVLAN",
    137: "IF_TYPE_L3_IPXVLAN",
    138: "IF_TYPE_DIGITALPOWERLINE",
    139: "IF_TYPE_MEDIAMAILOVERIP",
    140: "IF_TYPE_DTM",
    141: "IF_TYPE_DCN",
    142: "IF_TYPE_IPFORWARD",
    143: "IF_TYPE_MSDSL",
    144: "IF_TYPE_IEEE1394",
    145: "IF_TYPE_IF_GSN",
    146: "IF_TYPE_DVBRCC_MACLAYER",
    147: "IF_TYPE_DVBRCC_DOWNSTREAM",
    148: "IF_TYPE_DVBRCC_UPSTREAM",
    149: "IF_TYPE_ATM_VIRTUAL",
    150: "IF_TYPE_MPLS_TUNNEL",
    151: "IF_TYPE_SRP",
    152: "IF_TYPE_VOICEOVERATM",
    153: "IF_TYPE_VOICEOVERFRAMERELAY",
    154: "IF_TYPE_IDSL",
    155: "IF_TYPE_COMPOSITELINK",
    156: "IF_TYPE_SS7_SIGLINK",
    157: "IF_TYPE_PROP_WIRELESS_P2P",
    158: "IF_TYPE_FR_FORWARD",
    159: "IF_TYPE_RFC1483",
    160: "IF_TYPE_USB",
    161: "IF_TYPE_IEEE8023AD_LAG",
    162: "IF_TYPE_BGP_POLICY_ACCOUNTING",
    163: "IF_TYPE_FRF16_MFR_BUNDLE",
    164: "IF_TYPE_H323_GATEKEEPER",
    165: "IF_TYPE_H323_PROXY",
    166: "IF_TYPE_MPLS",
    167: "IF_TYPE_MF_SIGLINK",
    168: "IF_TYPE_HDSL2",
    169: "IF_TYPE_SHDSL",
    170: "IF_TYPE_DS1_FDL",
    171: "IF_TYPE_POS",
    172: "IF_TYPE_DVB_ASI_IN",
    173: "IF_TYPE_DVB_ASI_OUT",
    174: "IF_TYPE_PLC",
    175: "IF_TYPE_NFAS",
    176: "IF_TYPE_TR008",
    177: "IF_TYPE_GR303_RDT",
    178: "IF_TYPE_GR303_IDT",
    179: "IF_TYPE_ISUP",
    180: "IF_TYPE_PROP_DOCS_WIRELESS_MACLAYER",
    181: "IF_TYPE_PROP_DOCS_WIRELESS_DOWNSTREAM",
    182: "IF_TYPE_PROP_DOCS_WIRELESS_UPSTREAM",
    183: "IF_TYPE_HIPERLAN2",
    184: "IF_TYPE_PROP_BWA_P2MP",
    185: "IF_TYPE_SONET_OVERHEAD_CHANNEL",
    186: "IF_TYPE_DIGITAL_WRAPPER_OVERHEAD_CHANNEL",
    187: "IF_TYPE_AAL2",
    188: "IF_TYPE_RADIO_MAC",
    189: "IF_TYPE_ATM_RADIO",
    190: "IF_TYPE_IMT",
    191: "IF_TYPE_MVL",
    192: "IF_TYPE_REACH_DSL",
    193: "IF_TYPE_FR_DLCI_ENDPT",
    194: "IF_TYPE_ATM_VCI_ENDPT",
    195: "IF_TYPE_OPTICAL_CHANNEL",
    196: "IF_TYPE_OPTICAL_TRANSPORT",
    237: "IF_TYPE_IEEE80216_WMAN",
    243: "IF_TYPE_WWANPP",
    244: "IF_TYPE_WWANPP2",
}
MIB_TCP_STATE = {
    "MIB_TCP_STATE_CLOSED": 1,
    "MIB_TCP_STATE_LISTEN": 2,
    "MIB_TCP_STATE_SYN_SENT": 3,
    "MIB_TCP_STATE_SYN_RCVD": 4,
    "MIB_TCP_STATE_ESTAB": 5,
    "MIB_TCP_STATE_FIN_WAIT1": 6,
    "MIB_TCP_STATE_FIN_WAIT2": 7,
    "MIB_TCP_STATE_CLOSE_WAIT": 8,
    "MIB_TCP_STATE_CLOSING": 9,
    "MIB_TCP_STATE_LAST_ACK": 10,
    "MIB_TCP_STATE_TIME_WAIT": 11,
    "MIB_TCP_STATE_DELETE_TCB": 12,
}
MIB_TCP_STATE_INV = {
    1: "MIB_TCP_STATE_CLOSED",
    2: "MIB_TCP_STATE_LISTEN",
    3: "MIB_TCP_STATE_SYN_SENT",
    4: "MIB_TCP_STATE_SYN_RCVD",
    5: "MIB_TCP_STATE_ESTAB",
    6: "MIB_TCP_STATE_FIN_WAIT1",
    7: "MIB_TCP_STATE_FIN_WAIT2",
    8: "MIB_TCP_STATE_CLOSE_WAIT",
    9: "MIB_TCP_STATE_CLOSING",
    10: "MIB_TCP_STATE_LAST_ACK",
    11: "MIB_TCP_STATE_TIME_WAIT",
    12: "MIB_TCP_STATE_DELETE_TCB",
}
TCP_CONNECTION_OFFLOAD_STATE = {
    "TcpConnectionOffloadStateInHost": 0,
    "TcpConnectionOffloadStateOffloading": 1,
    "TcpConnectionOffloadStateOffloaded": 2,
    "TcpConnectionOffloadStateUploading": 3,
}
TCP_CONNECTION_OFFLOAD_STATE_INV = {
    0: "TcpConnectionOffloadStateInHost",
    1: "TcpConnectionOffloadStateOffloading",
    2: "TcpConnectionOffloadStateOffloaded",
    3: "TcpConnectionOffloadStateUploading",
}
NL_ROUTE_PROTOCOL = {
    "MIB_IPPROTO_OTHER": 1,
    "MIB_IPPROTO_LOCAL": 2,
    "MIB_IPPROTO_NETMGMT": 3,
    "MIB_IPPROTO_ICMP": 4,
    "MIB_IPPROTO_EGP": 5,
    "MIB_IPPROTO_GGP": 6,
    "MIB_IPPROTO_HELLO": 7,
    "MIB_IPPROTO_RIP": 8,
    "MIB_IPPROTO_IS_IS": 9,
    "MIB_IPPROTO_ES_IS": 10,
    "MIB_IPPROTO_CISCO": 11,
    "MIB_IPPROTO_BBN": 12,
    "MIB_IPPROTO_OSPF": 13,
    "MIB_IPPROTO_BGP": 14,
    "MIB_IPPROTO_NT_AUTOSTATIC": 10002,
    "MIB_IPPROTO_NT_STATIC": 10006,
    "MIB_IPPROTO_NT_STATIC_NON_DOD": 10007,
}
NL_ROUTE_PROTOCOL_INV = {
    1: "MIB_IPPROTO_OTHER",
    2: "MIB_IPPROTO_LOCAL",
    3: "MIB_IPPROTO_NETMGMT",
    4: "MIB_IPPROTO_ICMP",
    5: "MIB_IPPROTO_EGP",
    6: "MIB_IPPROTO_GGP",
    7: "MIB_IPPROTO_HELLO",
    8: "MIB_IPPROTO_RIP",
    9: "MIB_IPPROTO_IS_IS",
    10: "MIB_IPPROTO_ES_IS",
    11: "MIB_IPPROTO_CISCO",
    12: "MIB_IPPROTO_BBN",
    13: "MIB_IPPROTO_OSPF",
    14: "MIB_IPPROTO_BGP",
    10002: "MIB_IPPROTO_NT_AUTOSTATIC",
    10006: "MIB_IPPROTO_NT_STATIC",
    10007: "MIB_IPPROTO_NT_STATIC_NON_DOD",
}
NL_ROUTE_ORIGIN = {
    "NlroManual": 0,
    "NlroWellKnown": 1,
    "NlroDHCP": 2,
    "NlroRouterAdvertisement": 3,
    "Nlro6to4": 4,
}
NL_ROUTE_ORIGIN_INV = {
    0: "NlroManual",
    1: "NlroWellKnown",
    2: "NlroDHCP",
    3: "NlroRouterAdvertisement",
    4: "Nlro6to4",
}
MIB_IPNET_TYPE = {
    "MIB_IPNET_TYPE_OTHER": 1,
    "MIB_IPNET_TYPE_INVALID": 2,
    "MIB_IPNET_TYPE_DYNAMIC": 3,
    "MIB_IPNET_TYPE_STATIC": 4,
}
MIB_IPNET_TYPE_INV = {
    1: "MIB_IPNET_TYPE_OTHER",
    2: "MIB_IPNET_TYPE_INVALID",
    3: "MIB_IPNET_TYPE_DYNAMIC",
    4: "MIB_IPNET_TYPE_STATIC",
}
INTERNAL_IF_OPER_STATUS = {
    "IF_OPER_STATUS_NON_OPERATIONAL": 0,
    "IF_OPER_STATUS_UNREACHABLE": 1,
    "IF_OPER_STATUS_DISCONNECTED": 2,
    "IF_OPER_STATUS_CONNECTING": 3,
    "IF_OPER_STATUS_CONNECTED": 4,
    "IF_OPER_STATUS_OPERATIONAL": 5,
}
INTERNAL_IF_OPER_STATUS_INV = {
    0: "IF_OPER_STATUS_NON_OPERATIONAL",
    1: "IF_OPER_STATUS_UNREACHABLE",
    2: "IF_OPER_STATUS_DISCONNECTED",
    3: "IF_OPER_STATUS_CONNECTING",
    4: "IF_OPER_STATUS_CONNECTED",
    5: "IF_OPER_STATUS_OPERATIONAL",
}
TUNNEL_TYPE = {
    "TUNNEL_TYPE_NONE": 0,
    "TUNNEL_TYPE_OTHER": 1,
    "TUNNEL_TYPE_DIRECT": 2,
    "TUNNEL_TYPE_6TO4": 11,
    "TUNNEL_TYPE_ISATAP": 13,
    "TUNNEL_TYPE_TEREDO": 14,
    "TUNNEL_TYPE_IPHTTPS": 15,
}
TUNNEL_TYPE_INV = {
    0: "TUNNEL_TYPE_NONE",
    1: "TUNNEL_TYPE_OTHER",
    2: "TUNNEL_TYPE_DIRECT",
    11: "TUNNEL_TYPE_6TO4",
    13: "TUNNEL_TYPE_ISATAP",
    14: "TUNNEL_TYPE_TEREDO",
    15: "TUNNEL_TYPE_IPHTTPS",
}
NDIS_MEDIUM = {
    "NdisMedium802_3": 0,
    "NdisMedium802_5": 1,
    "NdisMediumFddi": 2,
    "NdisMediumWan": 3,
    "NdisMediumLocalTalk": 4,
    "NdisMediumDix": 5,
    "NdisMediumArcnetRaw": 6,
    "NdisMediumArcnet878_2": 7,
    "NdisMediumAtm": 8,
    "NdisMediumWirelessWan": 9,
    "NdisMediumIrda": 10,
    "NdisMediumBpc": 11,
    "NdisMediumCoWan": 12,
    "NdisMedium1394": 13,
    "NdisMediumInfiniBand": 14,
    "NdisMediumTunnel": 15,
    "NdisMediumNative802_11": 16,
    "NdisMediumLoopback": 17,
    "NdisMediumWiMAX": 18,
    "NdisMediumIP": 19,
}
NDIS_MEDIUM_INV = {
    0: "NdisMedium802_3",
    1: "NdisMedium802_5",
    2: "NdisMediumFddi",
    3: "NdisMediumWan",
    4: "NdisMediumLocalTalk",
    5: "NdisMediumDix",
    6: "NdisMediumArcnetRaw",
    7: "NdisMediumArcnet878_2",
    8: "NdisMediumAtm",
    9: "NdisMediumWirelessWan",
    10: "NdisMediumIrda",
    11: "NdisMediumBpc",
    12: "NdisMediumCoWan",
    13: "NdisMedium1394",
    14: "NdisMediumInfiniBand",
    15: "NdisMediumTunnel",
    16: "NdisMediumNative802_11",
    17: "NdisMediumLoopback",
    18: "NdisMediumWiMAX",
    19: "NdisMediumIP",
}
NDIS_PHYSICAL_MEDIUM = {
    "NdisPhysicalMediumUnspecified": 0,
    "NdisPhysicalMediumWirelessLan": 1,
    "NdisPhysicalMediumCableModem": 2,
    "NdisPhysicalMediumPhoneLine": 3,
    "NdisPhysicalMediumPowerLine": 4,
    "NdisPhysicalMediumDSL": 5,
    "NdisPhysicalMediumFibreChannel": 6,
    "NdisPhysicalMedium1394": 7,
    "NdisPhysicalMediumWirelessWan": 8,
    "NdisPhysicalMediumNative802_11": 9,
    "NdisPhysicalMediumBluetooth": 10,
    "NdisPhysicalMediumInfiniband": 11,
    "NdisPhysicalMediumWiMax": 12,
    "NdisPhysicalMediumUWB": 13,
    "NdisPhysicalMedium802_3": 14,
    "NdisPhysicalMedium802_5": 15,
    "NdisPhysicalMediumIrda": 16,
    "NdisPhysicalMediumWiredWAN": 17,
    "NdisPhysicalMediumWiredCoWan": 18,
    "NdisPhysicalMediumOther": 19,
}
NDIS_PHYSICAL_MEDIUM_INV = {
    0: "NdisPhysicalMediumUnspecified",
    1: "NdisPhysicalMediumWirelessLan",
    2: "NdisPhysicalMediumCableModem",
    3: "NdisPhysicalMediumPhoneLine",
    4: "NdisPhysicalMediumPowerLine",
    5: "NdisPhysicalMediumDSL",
    6: "NdisPhysicalMediumFibreChannel",
    7: "NdisPhysicalMedium1394",
    8: "NdisPhysicalMediumWirelessWan",
    9: "NdisPhysicalMediumNative802_11",
    10: "NdisPhysicalMediumBluetooth",
    11: "NdisPhysicalMediumInfiniband",
    12: "NdisPhysicalMediumWiMax",
    13: "NdisPhysicalMediumUWB",
    14: "NdisPhysicalMedium802_3",
    15: "NdisPhysicalMedium802_5",
    16: "NdisPhysicalMediumIrda",
    17: "NdisPhysicalMediumWiredWAN",
    18: "NdisPhysicalMediumWiredCoWan",
    19: "NdisPhysicalMediumOther",
}
NET_IF_ACCESS_TYPE = {
    "NET_IF_ACCESS_LOOPBACK": 1,
    "NET_IF_ACCESS_BROADCAST": 2,
    "NET_IF_ACCESS_POINT_TO_POINT": 3,
    "NET_IF_ACCESS_POINT_TO_MULTI_POINT": 4,
    "NET_IF_ACCESS_MAXIMUM": 5,
}
NET_IF_ACCESS_TYPE_INV = {
    1: "NET_IF_ACCESS_LOOPBACK",
    2: "NET_IF_ACCESS_BROADCAST",
    3: "NET_IF_ACCESS_POINT_TO_POINT",
    4: "NET_IF_ACCESS_POINT_TO_MULTI_POINT",
    5: "NET_IF_ACCESS_MAXIMUM",
}
NET_IF_DIRECTION_TYPE = {
    "NET_IF_DIRECTION_SENDRECEIVE": 0,
    "NET_IF_DIRECTION_SENDONLY": 1,
    "NET_IF_DIRECTION_RECEIVEONLY": 2,
}
NET_IF_DIRECTION_TYPE_INV = {
    0: "NET_IF_DIRECTION_SENDRECEIVE",
    1: "NET_IF_DIRECTION_SENDONLY",
    2: "NET_IF_DIRECTION_RECEIVEONLY",
}
IF_OPER_STATUS = {
    "IfOperStatusUp": 1,
    "IfOperStatusDown": 2,
    "IfOperStatusTesting": 3,
    "IfOperStatusUnknown": 4,
    "IfOperStatusDormant": 5,
    "IfOperStatusNotPresent": 6,
    "IfOperStatusLowerLayerDown": 7,
}
IF_OPER_STATUS_INV = {
    1: "IfOperStatusUp",
    2: "IfOperStatusDown",
    3: "IfOperStatusTesting",
    4: "IfOperStatusUnknown",
    5: "IfOperStatusDormant",
    6: "IfOperStatusNotPresent",
    7: "IfOperStatusLowerLayerDown",
}
NET_IF_ADMIN_STATUS = {
    "NET_IF_ADMIN_STATUS_UP": 1,
    "NET_IF_ADMIN_STATUS_DOWN": 2,
    "NET_IF_ADMIN_STATUS_TESTING": 3,
}
NET_IF_ADMIN_STATUS_INV = {
    1: "NET_IF_ADMIN_STATUS_UP",
    2: "NET_IF_ADMIN_STATUS_DOWN",
    3: "NET_IF_ADMIN_STATUS_TESTING",
}
NET_IF_MEDIA_CONNECT_STATE = {
    "MediaConnectStateUnknown": 0,
    "MediaConnectStateConnected": 1,
    "MediaConnectStateDisconnected": 2,
}
NET_IF_MEDIA_CONNECT_STATE_INV = {
    0: "MediaConnectStateUnknown",
    1: "MediaConnectStateConnected",
    2: "MediaConnectStateDisconnected",
}
NET_IF_CONNECTION_TYPE = {
    "NET_IF_CONNECTION_DEDICATED": 1,
    "NET_IF_CONNECTION_PASSIVE": 2,
    "NET_IF_CONNECTION_DEMAND": 3,
    "NET_IF_CONNECTION_MAXIMUM": 4,
}
NET_IF_CONNECTION_TYPE_INV = {
    1: "NET_IF_CONNECTION_DEDICATED",
    2: "NET_IF_CONNECTION_PASSIVE",
    3: "NET_IF_CONNECTION_DEMAND",
    4: "NET_IF_CONNECTION_MAXIMUM",
}
NL_ROUTER_DISCOVERY_BEHAVIOR = {
    "RouterDiscoveryDisabled": 0,
    "RouterDiscoveryEnabled": 1,
    "RouterDiscoveryDhcp": 2,
    "RouterDiscoveryUnchanged": -1,
}
NL_ROUTER_DISCOVERY_BEHAVIOR_INV = {
    0: "RouterDiscoveryDisabled",
    1: "RouterDiscoveryEnabled",
    2: "RouterDiscoveryDhcp",
    -1: "RouterDiscoveryUnchanged",
}
NL_LINK_LOCAL_ADDRESS_BEHAVIOR = {
    "LinkLocalAlwaysOff": 0,
    "LinkLocalDelayed": 1,
    "LinkLocalAlwaysOn": 2,
    "LinkLocalUnchanged": -1,
}
NL_LINK_LOCAL_ADDRESS_BEHAVIOR_INV = {
    0: "LinkLocalAlwaysOff",
    1: "LinkLocalDelayed",
    2: "LinkLocalAlwaysOn",
    -1: "LinkLocalUnchanged",
}
MIB_IPSTATS_FORWARDING = {
    "MIB_IP_FORWARDING": 1,
    "MIB_IP_NOT_FORWARDING": 2,
}
MIB_IPSTATS_FORWARDING_INV = {
    1: "MIB_IP_FORWARDING",
    2: "MIB_IP_NOT_FORWARDING",
}
NL_PREFIX_ORIGIN = {
    "IpPrefixOriginOther": 0,
    "IpPrefixOriginManual": 1,
    "IpPrefixOriginWellKnown": 2,
    "IpPrefixOriginDhcp": 3,
    "IpPrefixOriginRouterAdvertisement": 4,
    "IpPrefixOriginUnchanged": 0x10,
}
NL_PREFIX_ORIGIN_INV = {
    0: "IpPrefixOriginOther",
    1: "IpPrefixOriginManual",
    2: "IpPrefixOriginWellKnown",
    3: "IpPrefixOriginDhcp",
    4: "IpPrefixOriginRouterAdvertisement",
    0x10: "IpPrefixOriginUnchanged",
}
NL_SUFFIX_ORIGIN = {
    "IpSuffixOriginOther": 0,
    "IpSuffixOriginManual": 1,
    "IpSuffixOriginWellKnown": 2,
    "IpSuffixOriginDhcp": 3,
    "IpSuffixOriginLinkLayerAddress": 4,
    "IpSuffixOriginRandom": 5,
    "IpSuffixOriginUnchanged": 0x10,
}
NL_SUFFIX_ORIGIN_INV = {
    0: "IpSuffixOriginOther",
    1: "IpSuffixOriginManual",
    2: "IpSuffixOriginWellKnown",
    3: "IpSuffixOriginDhcp",
    4: "IpSuffixOriginLinkLayerAddress",
    5: "IpSuffixOriginRandom",
    0x10: "IpSuffixOriginUnchanged",
}
NL_DAD_STATE = {
    "IpDadStateInvalid": 0,
    "IpDadStateTentative": 1,
    "IpDadStateDuplicate": 2,
    "IpDadStateDeprecated": 3,
    "IpDadStatePreferred": 4,
}
NL_DAD_STATE_INV = {
    0: "IpDadStateInvalid",
    1: "IpDadStateTentative",
    2: "IpDadStateDuplicate",
    3: "IpDadStateDeprecated",
    4: "IpDadStatePreferred",
}
NL_NEIGHBOR_STATE = {
    "NlnsUnreachable": 0,
    "NlnsIncomplete": 1,
    "NlnsProbe": 2,
    "NlnsDelay": 3,
    "NlnsStale": 4,
    "NlnsReachable": 5,
    "NlnsPermanent": 6,
    "NlnsMaximum": 7,
}
NL_NEIGHBOR_STATE_INV = {
    0: "NlnsUnreachable",
    1: "NlnsIncomplete",
    2: "NlnsProbe",
    3: "NlnsDelay",
    4: "NlnsStale",
    5: "NlnsReachable",
    6: "NlnsPermanent",
    7: "NlnsMaximum",
}
MIB_IPFORWARD_TYPE = {
    "MIB_IPROUTE_TYPE_OTHER": 1,
    "MIB_IPROUTE_TYPE_INVALID": 2,
    "MIB_IPROUTE_TYPE_DIRECT": 3,
    "MIB_IPROUTE_TYPE_INDIRECT": 4,
}
MIB_IPFORWARD_TYPE_INV = {
    1: "MIB_IPROUTE_TYPE_OTHER",
    2: "MIB_IPROUTE_TYPE_INVALID",
    3: "MIB_IPROUTE_TYPE_DIRECT",
    4: "MIB_IPROUTE_TYPE_INDIRECT",
}
NET_ADDRESS_FORMAT = {
    "NET_ADDRESS_FORMAT_UNSPECIFIED": 0,
    "NET_ADDRESS_DNS_NAME": 1,
    "NET_ADDRESS_IPV4": 2,
    "NET_ADDRESS_IPV6": 3,
}
NET_ADDRESS_FORMAT_INV = {
    0: "NET_ADDRESS_FORMAT_UNSPECIFIED",
    1: "NET_ADDRESS_DNS_NAME",
    2: "NET_ADDRESS_IPV4",
    3: "NET_ADDRESS_IPV6",
}
_FIXED_INFO_NODETYPE_ = {
    "BROADCAST_NODETYPE": 1,
    "PEER_TO_PEER_NODETYPE": 2,
    "MIXED_NODETYPE": 4,
    "HYBRID_NODETYPE": 8,
}
_FIXED_INFO_NODETYPE__INV = {
    1: "BROADCAST_NODETYPE",
    2: "PEER_TO_PEER_NODETYPE",
    4: "MIXED_NODETYPE",
    8: "HYBRID_NODETYPE",
}
TCP_RTO_ALGORITHM = {
    "MIB_TCP_RTO_OTHER": 1,
    "MIB_TCP_RTO_CONSTANT": 2,
    "MIB_TCP_RTO_RSRE": 3,
    "MIB_TCP_RTO_VANJ": 4,
}
TCP_RTO_ALGORITHM_INV = {
    1: "MIB_TCP_RTO_OTHER",
    2: "MIB_TCP_RTO_CONSTANT",
    3: "MIB_TCP_RTO_RSRE",
    4: "MIB_TCP_RTO_VANJ",
}
TCPIP_OWNER_MODULE_INFO_CLASS = {
    "TCPIP_OWNER_MODULE_INFO_BASIC": 0,
}
TCPIP_OWNER_MODULE_INFO_CLASS_INV = {
    0: "TCPIP_OWNER_MODULE_INFO_BASIC",
}
TCP_ESTATS_TYPE = {
    "TcpConnectionEstatsSynOpts": 0,
    "TcpConnectionEstatsData": 1,
    "TcpConnectionEstatsSndCong": 2,
    "TcpConnectionEstatsPath": 3,
    "TcpConnectionEstatsSendBuff": 4,
    "TcpConnectionEstatsRec": 5,
    "TcpConnectionEstatsObsRec": 6,
    "TcpConnectionEstatsBandwidth": 7,
    "TcpConnectionEstatsFineRtt": 8,
    "TcpConnectionEstatsMaximum": 9,
}
TCP_ESTATS_TYPE_INV = {
    0: "TcpConnectionEstatsSynOpts",
    1: "TcpConnectionEstatsData",
    2: "TcpConnectionEstatsSndCong",
    3: "TcpConnectionEstatsPath",
    4: "TcpConnectionEstatsSendBuff",
    5: "TcpConnectionEstatsRec",
    6: "TcpConnectionEstatsObsRec",
    7: "TcpConnectionEstatsBandwidth",
    8: "TcpConnectionEstatsFineRtt",
    9: "TcpConnectionEstatsMaximum",
}
MIB_IF_TABLE_LEVEL = {
    "MibIfTableNormal": 0,
    "MibIfTableRaw": 1,
}
MIB_IF_TABLE_LEVEL_INV = {
    0: "MibIfTableNormal",
    1: "MibIfTableRaw",
}
TCP_TABLE_CLASS = {
    "TCP_TABLE_BASIC_LISTENER": 0,
    "TCP_TABLE_BASIC_CONNECTIONS": 1,
    "TCP_TABLE_BASIC_ALL": 2,
    "TCP_TABLE_OWNER_PID_LISTENER": 3,
    "TCP_TABLE_OWNER_PID_CONNECTIONS": 4,
    "TCP_TABLE_OWNER_PID_ALL": 5,
    "TCP_TABLE_OWNER_MODULE_LISTENER": 6,
    "TCP_TABLE_OWNER_MODULE_CONNECTIONS": 7,
    "TCP_TABLE_OWNER_MODULE_ALL": 8,
}
TCP_TABLE_CLASS_INV = {
    0: "TCP_TABLE_BASIC_LISTENER",
    1: "TCP_TABLE_BASIC_CONNECTIONS",
    2: "TCP_TABLE_BASIC_ALL",
    3: "TCP_TABLE_OWNER_PID_LISTENER",
    4: "TCP_TABLE_OWNER_PID_CONNECTIONS",
    5: "TCP_TABLE_OWNER_PID_ALL",
    6: "TCP_TABLE_OWNER_MODULE_LISTENER",
    7: "TCP_TABLE_OWNER_MODULE_CONNECTIONS",
    8: "TCP_TABLE_OWNER_MODULE_ALL",
}
UDP_TABLE_CLASS = {
    "UDP_TABLE_BASIC": 0,
    "UDP_TABLE_OWNER_PID": 1,
    "UDP_TABLE_OWNER_MODULE": 2,
}
UDP_TABLE_CLASS_INV = {
    0: "UDP_TABLE_BASIC",
    1: "UDP_TABLE_OWNER_PID",
    2: "UDP_TABLE_OWNER_MODULE",
}

###################

###### Types ######
PIP_ADAPTER_ADDRESSES = LPVOID
NET_IFINDEX = ULONG
PNET_IFINDEX = Ptr("<I", NET_IFINDEX())
IF_INDEX = NET_IFINDEX
IPMask = ULONG
const_CHAR_PTR = CHAR_PTR
PTEREDO_PORT_CHANGE_CALLBACK = LPVOID
PUNICAST_IPADDRESS_CHANGE_CALLBACK = LPVOID
PIPFORWARD_CHANGE_CALLBACK = LPVOID
PIPINTERFACE_CHANGE_CALLBACK = LPVOID
PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK = LPVOID
NET_IF_NETWORK_GUID = GUID
NETIO_STATUS = _ERROR_CODE_
NETIOAPI_API = NETIO_STATUS
IP_STATUS = ULONG
char__16_ = Array(char, 16)
char__MAX_HOSTNAME_LEN_+_4_ = Array(char, 132)
char__MAX_DOMAIN_NAME_LEN_+_4_ = Array(char, 132)
char__MAX_SCOPE_ID_LEN_+_4_ = Array(char, 260)
char__MAX_ADAPTER_NAME_LENGTH_+_4_ = Array(char, 260)
char__MAX_ADAPTER_DESCRIPTION_LENGTH_+_4_ = Array(char, 132)
CHAR__8_ = Array(CHAR, 8)
WCHAR__6_ = Array(WCHAR, 6)
WCHAR__MAX_ADAPTER_NAME_ = Array(WCHAR, 128)
WCHAR__IF_MAX_STRING_SIZE_+_1_ = Array(WCHAR, 257)
WCHAR__DNS_MAX_NAME_BUFFER_LENGTH_ = Array(WCHAR, 256)
WCHAR__MAX_INTERFACE_NAME_LEN_ = Array(WCHAR, 256)
UCHAR__MAXLEN_PHYSADDR_ = Array(UCHAR, 8)
UCHAR__MAXLEN_IFDESCR_ = Array(UCHAR, 256)
UCHAR__IF_MAX_PHYS_ADDRESS_LENGTH_ = Array(UCHAR, 32)
BYTE__MAX_ADAPTER_ADDRESS_LENGTH_ = Array(BYTE, 8)
ULONG__ScopeLevelCount_ = Array(ULONG, 16)
DWORD__256_ = Array(DWORD, 256)
ULONGLONG__TCPIP_OWNING_MODULE_SIZE_ = Array(ULONGLONG, 16)
IFTYPE = ULONG

class SCOPE_ID(MemStruct):
    fields = [
        ("Value", ULONG()),
    ]

MIB_TCP_STATE = UINT
TCP_CONNECTION_OFFLOAD_STATE = UINT

class SOCKADDR_IN(MemStruct):
    fields = [
        ("sin_family", ADDRESS_FAMILY()),
        ("sin_port", USHORT()),
        ("sin_addr", IN_ADDR()),
        ("sin_zero", CHAR__8_()),
    ]


class struct_sockaddr_in6(MemStruct):
    fields = [
        ("sin6_family", ADDRESS_FAMILY()),
        ("sin6_port", USHORT()),
        ("sin6_flowinfo", ULONG()),
        ("sin6_addr", IN6_ADDR()),
        ("sin6_scope_id", ULONG()),
    ]

struct_sockaddr_in6_PTR = Ptr("<I", struct_sockaddr_in6())
SOCKADDR_IN6 = struct_sockaddr_in6
PSOCKADDR_IN6 = Ptr("<I", SOCKADDR_IN6())
const_PSOCKADDR_IN6 = Ptr("<I", SOCKADDR_IN6())
NET_LUID = Union([
    ("Value", ULONG64),
])
NET_LUID_PTR = Ptr("<I", NET_LUID())
PNET_LUID = Ptr("<I", NET_LUID())
const_NET_LUID_PTR = Ptr("<I", NET_LUID())

class IP_ADDRESS_STRING(MemStruct):
    fields = [
        ("String", char__16_()),
    ]

IP_MASK_STRING = IP_ADDRESS_STRING

class IP_ADDR_STRING(MemStruct):
    fields = [
        ("Next", LPVOID()),
        ("IpAddress", IP_ADDRESS_STRING()),
        ("IpMask", IP_MASK_STRING()),
        ("Context", DWORD()),
    ]

PIP_ADDR_STRING = Ptr("<I", IP_ADDR_STRING())
NL_ROUTE_PROTOCOL = UINT
MIB_IPFORWARD_PROTO = NL_ROUTE_PROTOCOL
NL_ROUTE_ORIGIN = UINT
SOCKADDR_INET = Union([
    ("Ipv4", SOCKADDR_IN),
    ("Ipv6", SOCKADDR_IN6),
    ("si_family", ADDRESS_FAMILY),
])
SOCKADDR_INET_PTR = Ptr("<I", SOCKADDR_INET())
const_SOCKADDR_INET_PTR = Ptr("<I", SOCKADDR_INET())

class IP_ADDRESS_PREFIX(MemStruct):
    fields = [
        ("Prefix", SOCKADDR_INET()),
        ("PrefixLength", UINT8()),
    ]

_MIB_IF_TYPE_ = IFTYPE

class IP_ADAPTER_INFO(MemStruct):
    fields = [
        ("Next", LPVOID()),
        ("ComboIndex", DWORD()),
        ("AdapterName", char__MAX_ADAPTER_NAME_LENGTH_+_4_()),
        ("Description", char__MAX_ADAPTER_DESCRIPTION_LENGTH_+_4_()),
        ("AddressLength", UINT()),
        ("Address", BYTE__MAX_ADAPTER_ADDRESS_LENGTH_()),
        ("Index", DWORD()),
        ("Type", _MIB_IF_TYPE_()),
        ("DhcpEnabled", UINT()),
        ("CurrentIpAddress", PIP_ADDR_STRING()),
        ("IpAddressList", IP_ADDR_STRING()),
        ("GatewayList", IP_ADDR_STRING()),
        ("DhcpServer", IP_ADDR_STRING()),
        ("HaveWins", BOOL()),
        ("PrimaryWinsServer", IP_ADDR_STRING()),
        ("SecondaryWinsServer", IP_ADDR_STRING()),
        ("LeaseObtained", time_t()),
        ("LeaseExpires", time_t()),
    ]

PIP_ADAPTER_INFO = Ptr("<I", IP_ADAPTER_INFO())

class IP_PER_ADAPTER_INFO(MemStruct):
    fields = [
        ("AutoconfigEnabled", UINT()),
        ("AutoconfigActive", UINT()),
        ("CurrentDnsServer", PIP_ADDR_STRING()),
        ("DnsServerList", IP_ADDR_STRING()),
    ]

PIP_PER_ADAPTER_INFO = Ptr("<I", IP_PER_ADAPTER_INFO())

class IP_UNIDIRECTIONAL_ADAPTER_ADDRESS(MemStruct):
    fields = [
        ("NumAdapters", ULONG()),
        ("Address", IPAddr__1_()),
    ]

PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS = Ptr("<I", IP_UNIDIRECTIONAL_ADAPTER_ADDRESS())
MIB_IPNET_TYPE = UINT

class MIB_IPNETROW(MemStruct):
    fields = [
        ("dwIndex", IF_INDEX()),
        ("dwPhysAddrLen", DWORD()),
        ("bPhysAddr", UCHAR__MAXLEN_PHYSADDR_()),
        ("dwAddr", DWORD()),
        ("Type", MIB_IPNET_TYPE()),
    ]

PMIB_IPNETROW = Ptr("<I", MIB_IPNETROW())
MIB_IPNETROW__ANY_SIZE_ = Array(MIB_IPNETROW, 1)

class MIB_IPNETTABLE(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_IPNETROW__ANY_SIZE_()),
    ]

PMIB_IPNETTABLE = Ptr("<I", MIB_IPNETTABLE())

class MIB_IFSTACK_ROW(MemStruct):
    fields = [
        ("HigherLayerInterfaceIndex", NET_IFINDEX()),
        ("LowerLayerInterfaceIndex", NET_IFINDEX()),
    ]

MIB_IFSTACK_ROW__ANY_SIZE_ = Array(MIB_IFSTACK_ROW, 1)

class MIB_IFSTACK_TABLE(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_IFSTACK_ROW__ANY_SIZE_()),
    ]

PMIB_IFSTACK_TABLE = Ptr("<I", MIB_IFSTACK_TABLE())
PMIB_IFSTACK_TABLE_PTR = Ptr("<I", PMIB_IFSTACK_TABLE())
INTERNAL_IF_OPER_STATUS = UINT

class MIB_IFROW(MemStruct):
    fields = [
        ("wszName", WCHAR__MAX_INTERFACE_NAME_LEN_()),
        ("dwIndex", IF_INDEX()),
        ("dwType", IFTYPE()),
        ("dwMtu", DWORD()),
        ("dwSpeed", DWORD()),
        ("dwPhysAddrLen", DWORD()),
        ("bPhysAddr", UCHAR__MAXLEN_PHYSADDR_()),
        ("dwAdminStatus", DWORD()),
        ("dwOperStatus", INTERNAL_IF_OPER_STATUS()),
        ("dwLastChange", DWORD()),
        ("dwInOctets", DWORD()),
        ("dwInUcastPkts", DWORD()),
        ("dwInNUcastPkts", DWORD()),
        ("dwInDiscards", DWORD()),
        ("dwInErrors", DWORD()),
        ("dwInUnknownProtos", DWORD()),
        ("dwOutOctets", DWORD()),
        ("dwOutUcastPkts", DWORD()),
        ("dwOutNUcastPkts", DWORD()),
        ("dwOutDiscards", DWORD()),
        ("dwOutErrors", DWORD()),
        ("dwOutQLen", DWORD()),
        ("dwDescrLen", DWORD()),
        ("bDescr", UCHAR__MAXLEN_IFDESCR_()),
    ]

PMIB_IFROW = Ptr("<I", MIB_IFROW())
MIB_IFROW__ANY_SIZE_ = Array(MIB_IFROW, 1)

class MIB_IFTABLE(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_IFROW__ANY_SIZE_()),
    ]

PMIB_IFTABLE = Ptr("<I", MIB_IFTABLE())

class _MIB_IF_ROW2_s_(MemStruct):
    fields = [
        ("Flags", BOOLEAN()),
    ]

TUNNEL_TYPE = UINT
NDIS_MEDIUM = UINT
NDIS_PHYSICAL_MEDIUM = UINT
NET_IF_ACCESS_TYPE = UINT
NET_IF_DIRECTION_TYPE = UINT
IF_OPER_STATUS = UINT
NET_IF_ADMIN_STATUS = UINT
NET_IF_MEDIA_CONNECT_STATE = UINT
NET_IF_CONNECTION_TYPE = UINT

class MIB_IF_ROW2(MemStruct):
    fields = [
        ("InterfaceLuid", NET_LUID()),
        ("InterfaceIndex", NET_IFINDEX()),
        ("InterfaceGuid", GUID()),
        ("Alias", WCHAR__IF_MAX_STRING_SIZE_+_1_()),
        ("Description", WCHAR__IF_MAX_STRING_SIZE_+_1_()),
        ("PhysicalAddressLength", ULONG()),
        ("PhysicalAddress", UCHAR__IF_MAX_PHYS_ADDRESS_LENGTH_()),
        ("PermanentPhysicalAddress", UCHAR__IF_MAX_PHYS_ADDRESS_LENGTH_()),
        ("Mtu", ULONG()),
        ("Type", IFTYPE()),
        ("TunnelType", TUNNEL_TYPE()),
        ("MediaType", NDIS_MEDIUM()),
        ("PhysicalMediumType", NDIS_PHYSICAL_MEDIUM()),
        ("AccessType", NET_IF_ACCESS_TYPE()),
        ("DirectionType", NET_IF_DIRECTION_TYPE()),
        ("InterfaceAndOperStatusFlags", _MIB_IF_ROW2_s_()),
        ("OperStatus", IF_OPER_STATUS()),
        ("AdminStatus", NET_IF_ADMIN_STATUS()),
        ("MediaConnectState", NET_IF_MEDIA_CONNECT_STATE()),
        ("NetworkGuid", NET_IF_NETWORK_GUID()),
        ("ConnectionType", NET_IF_CONNECTION_TYPE()),
        ("TransmitLinkSpeed", ULONG64()),
        ("ReceiveLinkSpeed", ULONG64()),
        ("InOctets", ULONG64()),
        ("InUcastPkts", ULONG64()),
        ("InNUcastPkts", ULONG64()),
        ("InDiscards", ULONG64()),
        ("InErrors", ULONG64()),
        ("InUnknownProtos", ULONG64()),
        ("InUcastOctets", ULONG64()),
        ("InMulticastOctets", ULONG64()),
        ("InBroadcastOctets", ULONG64()),
        ("OutOctets", ULONG64()),
        ("OutUcastPkts", ULONG64()),
        ("OutNUcastPkts", ULONG64()),
        ("OutDiscards", ULONG64()),
        ("OutErrors", ULONG64()),
        ("OutUcastOctets", ULONG64()),
        ("OutMulticastOctets", ULONG64()),
        ("OutBroadcastOctets", ULONG64()),
        ("OutQLen", ULONG64()),
    ]

PMIB_IF_ROW2 = Ptr("<I", MIB_IF_ROW2())
MIB_IF_ROW2__ANY_SIZE_ = Array(MIB_IF_ROW2, 1)

class MIB_IF_TABLE2(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_IF_ROW2__ANY_SIZE_()),
    ]

PMIB_IF_TABLE2 = Ptr("<I", MIB_IF_TABLE2())
PMIB_IF_TABLE2_PTR = Ptr("<I", PMIB_IF_TABLE2())

class IP_ADAPTER_INDEX_MAP(MemStruct):
    fields = [
        ("Index", ULONG()),
        ("Name", WCHAR__MAX_ADAPTER_NAME_()),
    ]

PIP_ADAPTER_INDEX_MAP = Ptr("<I", IP_ADAPTER_INDEX_MAP())
IP_ADAPTER_INDEX_MAP__1_ = Array(IP_ADAPTER_INDEX_MAP, 1)

class IP_INTERFACE_INFO(MemStruct):
    fields = [
        ("NumAdapters", LONG()),
        ("Adapter", IP_ADAPTER_INDEX_MAP__1_()),
    ]

PIP_INTERFACE_INFO = Ptr("<I", IP_INTERFACE_INFO())

class MIB_INVERTEDIFSTACK_ROW(MemStruct):
    fields = [
        ("LowerLayerInterfaceIndex", NET_IFINDEX()),
        ("HigherLayerInterfaceIndex", NET_IFINDEX()),
    ]

MIB_INVERTEDIFSTACK_ROW__ANY_SIZE_ = Array(MIB_INVERTEDIFSTACK_ROW, 1)

class MIB_INVERTEDIFSTACK_TABLE(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_INVERTEDIFSTACK_ROW__ANY_SIZE_()),
    ]

PMIB_INVERTEDIFSTACK_TABLE = Ptr("<I", MIB_INVERTEDIFSTACK_TABLE())
PMIB_INVERTEDIFSTACK_TABLE_PTR = Ptr("<I", PMIB_INVERTEDIFSTACK_TABLE())
NL_ROUTER_DISCOVERY_BEHAVIOR = UINT
NL_LINK_LOCAL_ADDRESS_BEHAVIOR = UINT

class NL_INTERFACE_OFFLOAD_ROD(MemStruct):
    fields = [
        ("Value", BOOLEAN()),
    ]


class MIB_IPINTERFACE_ROW(MemStruct):
    fields = [
        ("Family", ADDRESS_FAMILY()),
        ("InterfaceLuid", NET_LUID()),
        ("InterfaceIndex", NET_IFINDEX()),
        ("MaxReassemblySize", ULONG()),
        ("InterfaceIdentifier", ULONG64()),
        ("MinRouterAdvertisementInterval", ULONG()),
        ("MaxRouterAdvertisementInterval", ULONG()),
        ("AdvertisingEnabled", BOOLEAN()),
        ("ForwardingEnabled", BOOLEAN()),
        ("WeakHostSend", BOOLEAN()),
        ("WeakHostReceive", BOOLEAN()),
        ("UseAutomaticMetric", BOOLEAN()),
        ("UseNeighborUnreachabilityDetection", BOOLEAN()),
        ("ManagedAddressConfigurationSupported", BOOLEAN()),
        ("OtherStatefulConfigurationSupported", BOOLEAN()),
        ("AdvertiseDefaultRoute", BOOLEAN()),
        ("RouterDiscoveryBehavior", NL_ROUTER_DISCOVERY_BEHAVIOR()),
        ("DadTransmits", ULONG()),
        ("BaseReachableTime", ULONG()),
        ("RetransmitTime", ULONG()),
        ("PathMtuDiscoveryTimeout", ULONG()),
        ("LinkLocalAddressBehavior", NL_LINK_LOCAL_ADDRESS_BEHAVIOR()),
        ("LinkLocalAddressTimeout", ULONG()),
        ("ZoneIndices", ULONG__ScopeLevelCount_()),
        ("SitePrefixLength", ULONG()),
        ("Metric", ULONG()),
        ("NlMtu", ULONG()),
        ("Connected", BOOLEAN()),
        ("SupportsWakeUpPatterns", BOOLEAN()),
        ("SupportsNeighborDiscovery", BOOLEAN()),
        ("SupportsRouterDiscovery", BOOLEAN()),
        ("ReachableTime", ULONG()),
        ("TransmitOffload", NL_INTERFACE_OFFLOAD_ROD()),
        ("ReceiveOffload", NL_INTERFACE_OFFLOAD_ROD()),
        ("DisableDefaultRoutes", BOOLEAN()),
    ]

PMIB_IPINTERFACE_ROW = Ptr("<I", MIB_IPINTERFACE_ROW())
MIB_IPINTERFACE_ROW__ANY_SIZE_ = Array(MIB_IPINTERFACE_ROW, 1)

class MIB_IPINTERFACE_TABLE(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_IPINTERFACE_ROW__ANY_SIZE_()),
    ]

PMIB_IPINTERFACE_TABLE = Ptr("<I", MIB_IPINTERFACE_TABLE())
PMIB_IPINTERFACE_TABLE_PTR = Ptr("<I", PMIB_IPINTERFACE_TABLE())

class MIBICMPSTATS(MemStruct):
    fields = [
        ("dwMsgs", DWORD()),
        ("dwErrors", DWORD()),
        ("dwDestUnreachs", DWORD()),
        ("dwTimeExcds", DWORD()),
        ("dwParmProbs", DWORD()),
        ("dwSrcQuenchs", DWORD()),
        ("dwRedirects", DWORD()),
        ("dwEchos", DWORD()),
        ("dwEchoReps", DWORD()),
        ("dwTimestamps", DWORD()),
        ("dwTimestampReps", DWORD()),
        ("dwAddrMasks", DWORD()),
        ("dwAddrMaskReps", DWORD()),
    ]


class MIBICMPINFO(MemStruct):
    fields = [
        ("icmpInStats", MIBICMPSTATS()),
        ("icmpOutStats", MIBICMPSTATS()),
    ]


class MIB_ICMP(MemStruct):
    fields = [
        ("stats", MIBICMPINFO()),
    ]

PMIB_ICMP = Ptr("<I", MIB_ICMP())
MIB_IPSTATS_FORWARDING = UINT

class MIB_IPSTATS(MemStruct):
    fields = [
        ("Forwarding", MIB_IPSTATS_FORWARDING()),
        ("dwDefaultTTL", DWORD()),
        ("dwInReceives", DWORD()),
        ("dwInHdrErrors", DWORD()),
        ("dwInAddrErrors", DWORD()),
        ("dwForwDatagrams", DWORD()),
        ("dwInUnknownProtos", DWORD()),
        ("dwInDiscards", DWORD()),
        ("dwInDelivers", DWORD()),
        ("dwOutRequests", DWORD()),
        ("dwRoutingDiscards", DWORD()),
        ("dwOutDiscards", DWORD()),
        ("dwOutNoRoutes", DWORD()),
        ("dwReasmTimeout", DWORD()),
        ("dwReasmReqds", DWORD()),
        ("dwReasmOks", DWORD()),
        ("dwReasmFails", DWORD()),
        ("dwFragOks", DWORD()),
        ("dwFragFails", DWORD()),
        ("dwFragCreates", DWORD()),
        ("dwNumIf", DWORD()),
        ("dwNumAddr", DWORD()),
        ("dwNumRoutes", DWORD()),
    ]

PMIB_IPSTATS = Ptr("<I", MIB_IPSTATS())

class MIB_ANYCASTIPADDRESS_ROW(MemStruct):
    fields = [
        ("Address", SOCKADDR_INET()),
        ("InterfaceLuid", NET_LUID()),
        ("InterfaceIndex", NET_IFINDEX()),
        ("ScopeId", SCOPE_ID()),
    ]

PMIB_ANYCASTIPADDRESS_ROW = Ptr("<I", MIB_ANYCASTIPADDRESS_ROW())
const_MIB_ANYCASTIPADDRESS_ROW_PTR = Ptr("<I", MIB_ANYCASTIPADDRESS_ROW())
MIB_ANYCASTIPADDRESS_ROW__ANY_SIZE_ = Array(MIB_ANYCASTIPADDRESS_ROW, 1)

class MIB_ANYCASTIPADDRESS_TABLE(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_ANYCASTIPADDRESS_ROW__ANY_SIZE_()),
    ]

PMIB_ANYCASTIPADDRESS_TABLE = Ptr("<I", MIB_ANYCASTIPADDRESS_TABLE())
PMIB_ANYCASTIPADDRESS_TABLE_PTR = Ptr("<I", PMIB_ANYCASTIPADDRESS_TABLE())
_MIB_IPADDR_TYPE_ = unsigned_short

class MIB_IPADDRROW(MemStruct):
    fields = [
        ("dwAddr", DWORD()),
        ("dwIndex", IF_INDEX()),
        ("dwMask", DWORD()),
        ("dwBCastAddr", DWORD()),
        ("dwReasmSize", DWORD()),
        ("unused1", unsigned_short()),
        ("wType", _MIB_IPADDR_TYPE_()),
    ]

MIB_IPADDRROW__ANY_SIZE_ = Array(MIB_IPADDRROW, 1)

class MIB_IPADDRTABLE(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_IPADDRROW__ANY_SIZE_()),
    ]

PMIB_IPADDRTABLE = Ptr("<I", MIB_IPADDRTABLE())

class MIB_MULTICASTIPADDRESS_ROW(MemStruct):
    fields = [
        ("Address", SOCKADDR_INET()),
        ("InterfaceIndex", NET_IFINDEX()),
        ("InterfaceLuid", NET_LUID()),
        ("ScopeId", SCOPE_ID()),
    ]

PMIB_MULTICASTIPADDRESS_ROW = Ptr("<I", MIB_MULTICASTIPADDRESS_ROW())
MIB_MULTICASTIPADDRESS_ROW__ANY_SIZE_ = Array(MIB_MULTICASTIPADDRESS_ROW, 1)

class MIB_MULTICASTIPADDRESS_TABLE(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_MULTICASTIPADDRESS_ROW__ANY_SIZE_()),
    ]

PMIB_MULTICASTIPADDRESS_TABLE = Ptr("<I", MIB_MULTICASTIPADDRESS_TABLE())
PMIB_MULTICASTIPADDRESS_TABLE_PTR = Ptr("<I", PMIB_MULTICASTIPADDRESS_TABLE())
NL_PREFIX_ORIGIN = UINT
NL_SUFFIX_ORIGIN = UINT
NL_DAD_STATE = UINT

class MIB_UNICASTIPADDRESS_ROW(MemStruct):
    fields = [
        ("Address", SOCKADDR_INET()),
        ("InterfaceLuid", NET_LUID()),
        ("InterfaceIndex", NET_IFINDEX()),
        ("PrefixOrigin", NL_PREFIX_ORIGIN()),
        ("SuffixOrigin", NL_SUFFIX_ORIGIN()),
        ("ValidLifetime", ULONG()),
        ("PreferredLifetime", ULONG()),
        ("OnLinkPrefixLength", UINT8()),
        ("SkipAsSource", BOOLEAN()),
        ("DadState", NL_DAD_STATE()),
        ("ScopeId", SCOPE_ID()),
        ("CreationTimeStamp", LARGE_INTEGER()),
    ]

PMIB_UNICASTIPADDRESS_ROW = Ptr("<I", MIB_UNICASTIPADDRESS_ROW())
const_MIB_UNICASTIPADDRESS_ROW_PTR = Ptr("<I", MIB_UNICASTIPADDRESS_ROW())
MIB_UNICASTIPADDRESS_ROW__ANY_SIZE_ = Array(MIB_UNICASTIPADDRESS_ROW, 1)

class MIB_UNICASTIPADDRESS_TABLE(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_UNICASTIPADDRESS_ROW__ANY_SIZE_()),
    ]

PMIB_UNICASTIPADDRESS_TABLE = Ptr("<I", MIB_UNICASTIPADDRESS_TABLE())
PMIB_UNICASTIPADDRESS_TABLE_PTR = Ptr("<I", PMIB_UNICASTIPADDRESS_TABLE())
_MIB_ReachabilityTime_ = Union([
    ("LastReachable", ULONG),
    ("LastUnreachable", ULONG),
])
NL_NEIGHBOR_STATE = UINT

class MIB_IPNET_ROW2(MemStruct):
    fields = [
        ("Address", SOCKADDR_INET()),
        ("InterfaceIndex", NET_IFINDEX()),
        ("InterfaceLuid", NET_LUID()),
        ("PhysicalAddress", UCHAR__IF_MAX_PHYS_ADDRESS_LENGTH_()),
        ("PhysicalAddressLength", ULONG()),
        ("State", NL_NEIGHBOR_STATE()),
        ("Flags", UCHAR()),
        ("ReachabilityTime", _MIB_ReachabilityTime_()),
    ]

const_MIB_IPNET_ROW2_PTR = Ptr("<I", MIB_IPNET_ROW2())
PMIB_IPNET_ROW2 = Ptr("<I", MIB_IPNET_ROW2())
MIB_IPNET_ROW2__ANY_SIZE_ = Array(MIB_IPNET_ROW2, 1)

class MIB_IPNET_TABLE2(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_IPNET_ROW2__ANY_SIZE_()),
    ]

PMIB_IPNET_TABLE2 = Ptr("<I", MIB_IPNET_TABLE2())
PMIB_IPNET_TABLE2_PTR = Ptr("<I", PMIB_IPNET_TABLE2())

class MIB_IPPATH_ROW(MemStruct):
    fields = [
        ("Source", SOCKADDR_INET()),
        ("Destination", SOCKADDR_INET()),
        ("InterfaceLuid", NET_LUID()),
        ("InterfaceIndex", NET_IFINDEX()),
        ("CurrentNextHop", SOCKADDR_INET()),
        ("PathMtu", ULONG()),
        ("RttMean", ULONG()),
        ("RttDeviation", ULONG()),
        (None, _MIB_ReachabilityTime_()),
        ("IsReachable", BOOLEAN()),
        ("LinkTransmitSpeed", ULONG64()),
        ("LinkReceiveSpeed", ULONG64()),
    ]

PMIB_IPPATH_ROW = Ptr("<I", MIB_IPPATH_ROW())
MIB_IPPATH_ROW__ANY_SIZE_ = Array(MIB_IPPATH_ROW, 1)

class MIB_IPPATH_TABLE(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_IPPATH_ROW__ANY_SIZE_()),
    ]

MIB_IPPATH_TABLE_PTR = Ptr("<I", MIB_IPPATH_TABLE())
MIB_IPFORWARD_TYPE = UINT

class MIB_IPFORWARDROW(MemStruct):
    fields = [
        ("dwForwardDest", DWORD()),
        ("dwForwardMask", DWORD()),
        ("dwForwardPolicy", DWORD()),
        ("dwForwardNextHop", DWORD()),
        ("dwForwardIfIndex", IF_INDEX()),
        ("ForwardType", MIB_IPFORWARD_TYPE()),
        ("ForwardProto", MIB_IPFORWARD_PROTO()),
        ("dwForwardAge", DWORD()),
        ("dwForwardNextHopAS", DWORD()),
        ("dwForwardMetric1", DWORD()),
        ("dwForwardMetric2", DWORD()),
        ("dwForwardMetric3", DWORD()),
        ("dwForwardMetric4", DWORD()),
        ("dwForwardMetric5", DWORD()),
    ]

PMIB_IPFORWARDROW = Ptr("<I", MIB_IPFORWARDROW())
MIB_IPFORWARDROW__ANY_SIZE_ = Array(MIB_IPFORWARDROW, 1)

class MIB_IPFORWARDTABLE(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_IPFORWARDROW__ANY_SIZE_()),
    ]

PMIB_IPFORWARDTABLE = Ptr("<I", MIB_IPFORWARDTABLE())

class MIB_IPFORWARD_ROW2(MemStruct):
    fields = [
        ("InterfaceLuid", NET_LUID()),
        ("InterfaceIndex", NET_IFINDEX()),
        ("DestinationPrefix", IP_ADDRESS_PREFIX()),
        ("NextHop", SOCKADDR_INET()),
        ("SitePrefixLength", UCHAR()),
        ("ValidLifetime", ULONG()),
        ("PreferredLifetime", ULONG()),
        ("Metric", ULONG()),
        ("Protocol", NL_ROUTE_PROTOCOL()),
        ("Loopback", BOOLEAN()),
        ("AutoconfigureAddress", BOOLEAN()),
        ("Publish", BOOLEAN()),
        ("Immortal", BOOLEAN()),
        ("Age", ULONG()),
        ("Origin", NL_ROUTE_ORIGIN()),
    ]

PMIB_IPFORWARD_ROW2 = Ptr("<I", MIB_IPFORWARD_ROW2())
const_MIB_IPFORWARD_ROW2_PTR = Ptr("<I", MIB_IPFORWARD_ROW2())
MIB_IPFORWARD_ROW2__ANY_SIZE_ = Array(MIB_IPFORWARD_ROW2, 1)

class MIB_IPFORWARD_TABLE2(MemStruct):
    fields = [
        ("NumEntries", ULONG()),
        ("Table", MIB_IPFORWARD_ROW2__ANY_SIZE_()),
    ]

PMIB_IPFORWARD_TABLE2 = Ptr("<I", MIB_IPFORWARD_TABLE2())
PMIB_IPFORWARD_TABLE2_PTR = Ptr("<I", PMIB_IPFORWARD_TABLE2())

class SOCKADDR_IN6_PAIR(MemStruct):
    fields = [
        ("SourceAddress", PSOCKADDR_IN6()),
        ("DestinationAddress", PSOCKADDR_IN6()),
    ]

PSOCKADDR_IN6_PAIR = Ptr("<I", SOCKADDR_IN6_PAIR())
PSOCKADDR_IN6_PAIR_PTR = Ptr("<I", PSOCKADDR_IN6_PAIR())
NET_ADDRESS_FORMAT = UINT

class _NET_ADDRESS_INFO_u_s_(MemStruct):
    fields = [
        ("Address", WCHAR__DNS_MAX_NAME_BUFFER_LENGTH_()),
        ("Port", WCHAR__6_()),
    ]

_NET_ADDRESS_INFO_u_ = Union([
    ("NamedAddress", _NET_ADDRESS_INFO_u_s_),
    ("Ipv4Address", SOCKADDR_IN),
    ("Ipv6Address", SOCKADDR_IN6),
    ("IpAddress", SOCKADDR),
])

class NET_ADDRESS_INFO(MemStruct):
    fields = [
        ("Format", NET_ADDRESS_FORMAT()),
        (None, _NET_ADDRESS_INFO_u_()),
    ]

PNET_ADDRESS_INFO = Ptr("<I", NET_ADDRESS_INFO())
_FIXED_INFO_NODETYPE_ = UINT

class FIXED_INFO(MemStruct):
    fields = [
        ("HostName", char__MAX_HOSTNAME_LEN_+_4_()),
        ("DomainName", char__MAX_DOMAIN_NAME_LEN_+_4_()),
        ("CurrentDnsServer", PIP_ADDR_STRING()),
        ("DnsServerList", IP_ADDR_STRING()),
        ("NodeType", _FIXED_INFO_NODETYPE_()),
        ("ScopeId", char__MAX_SCOPE_ID_LEN_+_4_()),
        ("EnableRouting", UINT()),
        ("EnableProxy", UINT()),
        ("EnableDns", UINT()),
    ]

PFIXED_INFO = Ptr("<I", FIXED_INFO())

class MIB_TCP6ROW_OWNER_MODULE(MemStruct):
    fields = [
        ("ucLocalAddr", UCHAR__16_()),
        ("dwLocalScopeId", DWORD()),
        ("dwLocalPort", DWORD()),
        ("ucRemoteAddr", UCHAR__16_()),
        ("dwRemoteScopeId", DWORD()),
        ("dwRemotePort", DWORD()),
        ("dwState", MIB_TCP_STATE()),
        ("dwOwningPid", DWORD()),
        ("liCreateTimestamp", LARGE_INTEGER()),
        ("OwningModuleInfo", ULONGLONG__TCPIP_OWNING_MODULE_SIZE_()),
    ]

PMIB_TCP6ROW_OWNER_MODULE = Ptr("<I", MIB_TCP6ROW_OWNER_MODULE())

class MIB_TCPROW_OWNER_MODULE(MemStruct):
    fields = [
        ("dwState", MIB_TCP_STATE()),
        ("dwLocalAddr", DWORD()),
        ("dwLocalPort", DWORD()),
        ("dwRemoteAddr", DWORD()),
        ("dwRemotePort", DWORD()),
        ("dwOwningPid", DWORD()),
        ("liCreateTimestamp", LARGE_INTEGER()),
        ("OwningModuleInfo", ULONGLONG__TCPIP_OWNING_MODULE_SIZE_()),
    ]

PMIB_TCPROW_OWNER_MODULE = Ptr("<I", MIB_TCPROW_OWNER_MODULE())

class MIB_UDP6ROW_OWNER_MODULE(MemStruct):
    fields = [
        ("ucLocalAddr", UCHAR__16_()),
        ("dwLocalScopeId", DWORD()),
        ("dwLocalPort", DWORD()),
        ("dwOwningPid", DWORD()),
        ("liCreateTimestamp", LARGE_INTEGER()),
        ("dwFlags", int()),
        ("OwningModuleInfo", ULONGLONG__TCPIP_OWNING_MODULE_SIZE_()),
    ]

PMIB_UDP6ROW_OWNER_MODULE = Ptr("<I", MIB_UDP6ROW_OWNER_MODULE())

class MIB_UDPROW_OWNER_MODULE(MemStruct):
    fields = [
        ("dwLocalAddr", DWORD()),
        ("dwLocalPort", DWORD()),
        ("dwOwningPid", DWORD()),
        ("liCreateTimestamp", LARGE_INTEGER()),
        ("dwFlags", int()),
        ("OwningModuleInfo", ULONGLONG__TCPIP_OWNING_MODULE_SIZE_()),
    ]

PMIB_UDPROW_OWNER_MODULE = Ptr("<I", MIB_UDPROW_OWNER_MODULE())
TCP_RTO_ALGORITHM = UINT

class MIB_TCPSTATS(MemStruct):
    fields = [
        ("RtoAlgorithm", TCP_RTO_ALGORITHM()),
        ("dwRtoMin", DWORD()),
        ("dwRtoMax", DWORD()),
        ("dwMaxConn", DWORD()),
        ("dwActiveOpens", DWORD()),
        ("dwPassiveOpens", DWORD()),
        ("dwAttemptFails", DWORD()),
        ("dwEstabResets", DWORD()),
        ("dwCurrEstab", DWORD()),
        ("dwInSegs", DWORD()),
        ("dwOutSegs", DWORD()),
        ("dwRetransSegs", DWORD()),
        ("dwInErrs", DWORD()),
        ("dwOutRsts", DWORD()),
        ("dwNumConns", DWORD()),
    ]

PMIB_TCPSTATS = Ptr("<I", MIB_TCPSTATS())

class MIB_TCP6ROW(MemStruct):
    fields = [
        ("State", MIB_TCP_STATE()),
        ("LocalAddr", IN6_ADDR()),
        ("dwLocalScopeId", DWORD()),
        ("dwLocalPort", DWORD()),
        ("RemoteAddr", IN6_ADDR()),
        ("dwRemoteScopeId", DWORD()),
        ("dwRemotePort", DWORD()),
    ]

PMIB_TCP6ROW = Ptr("<I", MIB_TCP6ROW())
MIB_TCP6ROW__ANY_SIZE_ = Array(MIB_TCP6ROW, 1)

class MIB_TCP6TABLE(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_TCP6ROW__ANY_SIZE_()),
    ]

PMIB_TCP6TABLE = Ptr("<I", MIB_TCP6TABLE())

class MIB_TCP6ROW2(MemStruct):
    fields = [
        ("LocalAddr", IN6_ADDR()),
        ("dwLocalScopeId", DWORD()),
        ("dwLocalPort", DWORD()),
        ("RemoteAddr", IN6_ADDR()),
        ("dwRemoteScopeId", DWORD()),
        ("dwRemotePort", DWORD()),
        ("State", MIB_TCP_STATE()),
        ("dwOwningPid", DWORD()),
        ("dwOffloadState", TCP_CONNECTION_OFFLOAD_STATE()),
    ]

MIB_TCP6ROW2__ANY_SIZE_ = Array(MIB_TCP6ROW2, 1)

class MIB_TCP6TABLE2(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_TCP6ROW2__ANY_SIZE_()),
    ]

PMIB_TCP6TABLE2 = Ptr("<I", MIB_TCP6TABLE2())

class MIB_TCPROW(MemStruct):
    fields = [
        ("State", MIB_TCP_STATE()),
        ("dwLocalAddr", DWORD()),
        ("dwLocalPort", DWORD()),
        ("dwRemoteAddr", DWORD()),
        ("dwRemotePort", DWORD()),
    ]

PMIB_TCPROW = Ptr("<I", MIB_TCPROW())
MIB_TCPROW__ANY_SIZE_ = Array(MIB_TCPROW, 1)

class MIB_TCPTABLE(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_TCPROW__ANY_SIZE_()),
    ]

PMIB_TCPTABLE = Ptr("<I", MIB_TCPTABLE())

class MIB_TCPROW2(MemStruct):
    fields = [
        ("dwState", MIB_TCP_STATE()),
        ("dwLocalAddr", DWORD()),
        ("dwLocalPort", DWORD()),
        ("dwRemoteAddr", DWORD()),
        ("dwRemotePort", DWORD()),
        ("dwOwningPid", DWORD()),
        ("dwOffloadState", TCP_CONNECTION_OFFLOAD_STATE()),
    ]

MIB_TCPROW2__ANY_SIZE_ = Array(MIB_TCPROW2, 1)

class MIB_TCPTABLE2(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_TCPROW2__ANY_SIZE_()),
    ]

PMIB_TCPTABLE2 = Ptr("<I", MIB_TCPTABLE2())

class MIB_UDP6ROW(MemStruct):
    fields = [
        ("dwLocalAddr", IN6_ADDR()),
        ("dwLocalScopeId", DWORD()),
        ("dwLocalPort", DWORD()),
    ]

MIB_UDP6ROW__ANY_SIZE_ = Array(MIB_UDP6ROW, 1)

class MIB_UDP6TABLE(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_UDP6ROW__ANY_SIZE_()),
    ]

PMIB_UDP6TABLE = Ptr("<I", MIB_UDP6TABLE())

class MIB_UDPSTATS(MemStruct):
    fields = [
        ("dwInDatagrams", DWORD()),
        ("dwNoPorts", DWORD()),
        ("dwInErrors", DWORD()),
        ("dwOutDatagrams", DWORD()),
        ("dwNumAddrs", DWORD()),
    ]

PMIB_UDPSTATS = Ptr("<I", MIB_UDPSTATS())

class MIB_UDPROW(MemStruct):
    fields = [
        ("dwLocalAddr", DWORD()),
        ("dwLocalPort", DWORD()),
    ]

MIB_UDPROW__ANY_SIZE_ = Array(MIB_UDPROW, 1)

class MIB_UDPTABLE(MemStruct):
    fields = [
        ("dwNumEntries", DWORD()),
        ("table", MIB_UDPROW__ANY_SIZE_()),
    ]

PMIB_UDPTABLE = Ptr("<I", MIB_UDPTABLE())
TCPIP_OWNER_MODULE_INFO_CLASS = UINT
TCP_ESTATS_TYPE = UINT
MIB_IF_TABLE_LEVEL = UINT
TCP_TABLE_CLASS = UINT
UDP_TABLE_CLASS = UINT
_GetAdaptersAddressesFlags_ = ULONG

class NL_BANDWIDTH_INFORMATION(MemStruct):
    fields = [
        ("Bandwidth", ULONG64()),
        ("Instability", ULONG64()),
        ("BandwidthPeaked", BOOLEAN()),
    ]


class MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES(MemStruct):
    fields = [
        ("InboundBandwidthInformation", NL_BANDWIDTH_INFORMATION()),
        ("OutboundBandwidthInformation", NL_BANDWIDTH_INFORMATION()),
    ]

PMIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES = Ptr("<I", MIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES())

class IP_ADAPTER_ORDER_MAP(MemStruct):
    fields = [
        ("NumAdapters", ULONG()),
        ("AdapterOrder", ULONG__1_()),
    ]

PIP_ADAPTER_ORDER_MAP = Ptr("<I", IP_ADAPTER_ORDER_MAP())

class IP_INTERFACE_NAME_INFO(MemStruct):
    fields = [
        ("Index", ULONG()),
        ("MediaType", ULONG()),
        ("ConnectionType", UCHAR()),
        ("AccessType", UCHAR()),
        ("DeviceGuid", GUID()),
        ("InterfaceGuid", GUID()),
    ]

IP_INTERFACE_NAME_INFO_PTR = Ptr("<I", IP_INTERFACE_NAME_INFO())
IP_INTERFACE_NAME_INFO_PTR_PTR = Ptr("<I", IP_INTERFACE_NAME_INFO_PTR())

class MIBICMPSTATS_EX(MemStruct):
    fields = [
        ("dwMsgs", DWORD()),
        ("dwErrors", DWORD()),
        ("rgdwTypeCount", DWORD__256_()),
    ]


class MIB_ICMP_EX(MemStruct):
    fields = [
        ("icmpInStats", MIBICMPSTATS_EX()),
        ("icmpOutStats", MIBICMPSTATS_EX()),
    ]

PMIB_ICMP_EX = Ptr("<I", MIB_ICMP_EX())

###################

###### Functions ######

def iphlpapi_GetAdapterIndex(jitter):
    """
    [ERROR_CODE] GetAdapterIndex(
        LPWSTR AdapterName,
        PULONG IfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AdapterName", "IfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAdaptersAddresses(jitter):
    """
    [ERROR_CODE_ULONG] GetAdaptersAddresses(
        ADDRESS_FAMILY Family,
        [GetAdaptersAddressesFlags] Flags,
        PVOID Reserved,
        PIP_ADAPTER_ADDRESSES AdapterAddresses,
        PULONG SizePointer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Flags", "Reserved", "AdapterAddresses", "SizePointer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAdaptersInfo(jitter):
    """
    [ERROR_CODE] GetAdaptersInfo(
        PIP_ADAPTER_INFO pAdapterInfo,
        PULONG pOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pAdapterInfo", "pOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetPerAdapterInfo(jitter):
    """
    [ERROR_CODE] GetPerAdapterInfo(
        ULONG IfIndex,
        PIP_PER_ADAPTER_INFO pPerAdapterInfo,
        PULONG pOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfIndex", "pPerAdapterInfo", "pOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUniDirectionalAdapterInfo(jitter):
    """
    [ERROR_CODE] GetUniDirectionalAdapterInfo(
        PIP_UNIDIRECTIONAL_ADAPTER_ADDRESS pIPIfInfo,
        PULONG dwOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIPIfInfo", "dwOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateIpNetEntry(jitter):
    """
    [ERROR_CODE] CreateIpNetEntry(
        PMIB_IPNETROW pArpEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pArpEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateProxyArpEntry(jitter):
    """
    [ERROR_CODE] CreateProxyArpEntry(
        DWORD dwAddress,
        DWORD dwMask,
        DWORD dwIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwAddress", "dwMask", "dwIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIpNetEntry(jitter):
    """
    [ERROR_CODE] DeleteIpNetEntry(
        PMIB_IPNETROW pArpEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pArpEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteProxyArpEntry(jitter):
    """
    [ERROR_CODE] DeleteProxyArpEntry(
        DWORD dwAddress,
        DWORD dwMask,
        DWORD dwIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwAddress", "dwMask", "dwIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_FlushIpNetTable(jitter):
    """
    [ERROR_CODE] FlushIpNetTable(
        DWORD dwIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpNetTable(jitter):
    """
    [ERROR_CODE] GetIpNetTable(
        PMIB_IPNETTABLE pIpNetTable,
        PULONG pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpNetTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SendARP(jitter):
    """
    [ERROR_CODE] SendARP(
        IPAddr DestIP,
        IPAddr SrcIP,
        PULONG pMacAddr,
        PULONG PhyAddrLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestIP", "SrcIP", "pMacAddr", "PhyAddrLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpNetEntry(jitter):
    """
    [ERROR_CODE] SetIpNetEntry(
        PMIB_IPNETROW pArpEntry
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pArpEntry"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceAliasToLuid(jitter):
    """
    NETIO_STATUS ConvertInterfaceAliasToLuid(
        const WCHAR* InterfaceAlias,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceAlias", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceGuidToLuid(jitter):
    """
    NETIO_STATUS ConvertInterfaceGuidToLuid(
        const GUID* InterfaceGuid,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceGuid", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceIndexToLuid(jitter):
    """
    NETIO_STATUS ConvertInterfaceIndexToLuid(
        NET_IFINDEX InterfaceIndex,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceIndex", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToAlias(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToAlias(
        const NET_LUID* InterfaceLuid,
        PWSTR InterfaceAlias,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceAlias", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToGuid(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToGuid(
        const NET_LUID* InterfaceLuid,
        GUID* InterfaceGuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceGuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToIndex(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToIndex(
        const NET_LUID* InterfaceLuid,
        PNET_IFINDEX InterfaceIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToNameA(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToNameA(
        const NET_LUID* InterfaceLuid,
        PSTR InterfaceName,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceName", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceLuidToNameW(jitter):
    """
    NETIO_STATUS ConvertInterfaceLuidToNameW(
        const NET_LUID* InterfaceLuid,
        PWSTR InterfaceName,
        SIZE_T Length
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceName", "Length"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceNameToLuidA(jitter):
    """
    NETIO_STATUS ConvertInterfaceNameToLuidA(
        const CHAR* InterfaceName,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceName", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertInterfaceNameToLuidW(jitter):
    """
    NETIO_STATUS ConvertInterfaceNameToLuidW(
        const WCHAR* InterfaceName,
        PNET_LUID InterfaceLuid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceName", "InterfaceLuid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_if_indextoname(jitter):
    """
    PCHAR if_indextoname(
        NET_IFINDEX InterfaceIndex,
        PCHAR InterfaceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceIndex", "InterfaceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_if_nametoindex(jitter):
    """
    NET_IFINDEX if_nametoindex(
        PCSTR InterfaceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetFriendlyIfIndex(jitter):
    """
    [ERROR_CODE] GetFriendlyIfIndex(
        DWORD IfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfEntry(jitter):
    """
    [ERROR_CODE] GetIfEntry(
        PMIB_IFROW pIfRow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIfRow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfEntry2(jitter):
    """
    NETIOAPI_API GetIfEntry2(
        PMIB_IF_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfStackTable(jitter):
    """
    NETIOAPI_API GetIfStackTable(
        PMIB_IFSTACK_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfTable(jitter):
    """
    [ERROR_CODE] GetIfTable(
        PMIB_IFTABLE pIfTable,
        PULONG pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIfTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfTable2(jitter):
    """
    NETIOAPI_API GetIfTable2(
        PMIB_IF_TABLE2* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIfTable2Ex(jitter):
    """
    NETIOAPI_API GetIfTable2Ex(
        MIB_IF_TABLE_LEVEL Level,
        PMIB_IF_TABLE2* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Level", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetInterfaceInfo(jitter):
    """
    [ERROR_CODE] GetInterfaceInfo(
        PIP_INTERFACE_INFO pIfTable,
        PULONG dwOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIfTable", "dwOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetInvertedIfStackTable(jitter):
    """
    NETIOAPI_API GetInvertedIfStackTable(
        PMIB_INVERTEDIFSTACK_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpInterfaceEntry(jitter):
    """
    NETIOAPI_API GetIpInterfaceEntry(
        PMIB_IPINTERFACE_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpInterfaceTable(jitter):
    """
    NETIOAPI_API GetIpInterfaceTable(
        ADDRESS_FAMILY Family,
        PMIB_IPINTERFACE_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetNumberOfInterfaces(jitter):
    """
    [ERROR_CODE] GetNumberOfInterfaces(
        PDWORD pdwNumIf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pdwNumIf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_InitializeIpInterfaceEntry(jitter):
    """
    VOID InitializeIpInterfaceEntry(
        PMIB_IPINTERFACE_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIfEntry(jitter):
    """
    [ERROR_CODE] SetIfEntry(
        PMIB_IFROW pIfRow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIfRow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpInterfaceEntry(jitter):
    """
    NETIOAPI_API SetIpInterfaceEntry(
        PMIB_IPINTERFACE_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIcmpStatistics(jitter):
    """
    [ERROR_CODE] GetIcmpStatistics(
        PMIB_ICMP pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpStatistics(jitter):
    """
    [ERROR_CODE] GetIpStatistics(
        PMIB_IPSTATS pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_Icmp6CreateFile(jitter):
    """
    [FILE_HANDLE] Icmp6CreateFile()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_Icmp6ParseReplies(jitter):
    """
    [ERROR_CODE] Icmp6ParseReplies(
        LPVOID ReplyBuffer,
        DWORD ReplySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReplyBuffer", "ReplySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_Icmp6SendEcho2(jitter):
    """
    [ERROR_CODE] Icmp6SendEcho2(
        HANDLE IcmpHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        struct sockaddr_in6* SourceAddress,
        struct sockaddr_in6* DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "Event", "ApcRoutine", "ApcContext", "SourceAddress", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpSendEcho2Ex(jitter):
    """
    [ERROR_CODE] IcmpSendEcho2Ex(
        HANDLE IcmpHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        IPAddr SourceAddress,
        IPAddr DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "Event", "ApcRoutine", "ApcContext", "SourceAddress", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpTTL(jitter):
    """
    [ERROR_CODE] SetIpTTL(
        UINT nTTL
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["nTTL"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_AddIPAddress(jitter):
    """
    [ERROR_CODE] AddIPAddress(
        IPAddr Address,
        IPMask IpMask,
        DWORD IfIndex,
        PULONG NTEContext,
        PULONG NTEInstance
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Address", "IpMask", "IfIndex", "NTEContext", "NTEInstance"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateAnycastIpAddressEntry(jitter):
    """
    NETIOAPI_API CreateAnycastIpAddressEntry(
        const MIB_ANYCASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateUnicastIpAddressEntry(jitter):
    """
    NETIOAPI_API CreateUnicastIpAddressEntry(
        const MIB_UNICASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIPAddress(jitter):
    """
    [ERROR_CODE] DeleteIPAddress(
        ULONG NTEContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NTEContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteAnycastIpAddressEntry(jitter):
    """
    NETIOAPI_API DeleteAnycastIpAddressEntry(
        const MIB_ANYCASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteUnicastIpAddressEntry(jitter):
    """
    NETIOAPI_API DeleteUnicastIpAddressEntry(
        const MIB_UNICASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAnycastIpAddressEntry(jitter):
    """
    NETIOAPI_API GetAnycastIpAddressEntry(
        PMIB_ANYCASTIPADDRESS_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAnycastIpAddressTable(jitter):
    """
    NETIOAPI_API GetAnycastIpAddressTable(
        ADDRESS_FAMILY Family,
        PMIB_ANYCASTIPADDRESS_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpAddrTable(jitter):
    """
    [ERROR_CODE] GetIpAddrTable(
        PMIB_IPADDRTABLE pIpAddrTable,
        PULONG pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpAddrTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetMulticastIpAddressEntry(jitter):
    """
    NETIOAPI_API GetMulticastIpAddressEntry(
        PMIB_MULTICASTIPADDRESS_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetMulticastIpAddressTable(jitter):
    """
    NETIOAPI_API GetMulticastIpAddressTable(
        ADDRESS_FAMILY Family,
        PMIB_MULTICASTIPADDRESS_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUnicastIpAddressEntry(jitter):
    """
    NETIOAPI_API GetUnicastIpAddressEntry(
        PMIB_UNICASTIPADDRESS_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUnicastIpAddressTable(jitter):
    """
    NETIOAPI_API GetUnicastIpAddressTable(
        ADDRESS_FAMILY Family,
        PMIB_UNICASTIPADDRESS_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_InitializeUnicastIpAddressEntry(jitter):
    """
    VOID InitializeUnicastIpAddressEntry(
        PMIB_UNICASTIPADDRESS_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IpReleaseAddress(jitter):
    """
    [ERROR_CODE] IpReleaseAddress(
        PIP_ADAPTER_INDEX_MAP AdapterInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AdapterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IpRenewAddress(jitter):
    """
    [ERROR_CODE] IpRenewAddress(
        PIP_ADAPTER_INDEX_MAP AdapterInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AdapterInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyStableUnicastIpAddressTable(jitter):
    """
    NETIOAPI_API NotifyStableUnicastIpAddressTable(
        ADDRESS_FAMILY Family,
        PMIB_UNICASTIPADDRESS_TABLE* Table,
        PSTABLE_UNICAST_IPADDRESS_TABLE_CALLBACK CallerCallback,
        PVOID CallerContext,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table", "CallerCallback", "CallerContext", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetUnicastIpAddressEntry(jitter):
    """
    NETIOAPI_API SetUnicastIpAddressEntry(
        const MIB_UNICASTIPADDRESS_ROW* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateIpNetEntry2(jitter):
    """
    NETIOAPI_API CreateIpNetEntry2(
        const MIB_IPNET_ROW2* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIpNetEntry2(jitter):
    """
    NETIOAPI_API DeleteIpNetEntry2(
        const MIB_IPNET_ROW2* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_FlushIpNetTable2(jitter):
    """
    NETIOAPI_API FlushIpNetTable2(
        ADDRESS_FAMILY Family,
        NET_IFINDEX InterfaceIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "InterfaceIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpNetEntry2(jitter):
    """
    NETIOAPI_API GetIpNetEntry2(
        PMIB_IPNET_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpNetTable2(jitter):
    """
    NETIOAPI_API GetIpNetTable2(
        ADDRESS_FAMILY Family,
        PMIB_IPNET_TABLE2* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ResolveIpNetEntry2(jitter):
    """
    NETIOAPI_API ResolveIpNetEntry2(
        PMIB_IPNET_ROW2 Row,
        const SOCKADDR_INET* SourceAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "SourceAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ResolveNeighbor(jitter):
    """
    [ERROR_CODE_ULONG] ResolveNeighbor(
        SOCKADDR* NetworkAddress,
        PVOID PhysicalAddress,
        PULONG PhysicalAddressLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NetworkAddress", "PhysicalAddress", "PhysicalAddressLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpNetEntry2(jitter):
    """
    NETIOAPI_API SetIpNetEntry2(
        PMIB_IPNET_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_FlushIpPathTable(jitter):
    """
    NETIOAPI_API FlushIpPathTable(
        ADDRESS_FAMILY Family
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpPathEntry(jitter):
    """
    NETIOAPI_API GetIpPathEntry(
        PMIB_IPPATH_ROW Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpPathTable(jitter):
    """
    NETIOAPI_API GetIpPathTable(
        ADDRESS_FAMILY Family,
        MIB_IPPATH_TABLE* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateIpForwardEntry(jitter):
    """
    [ERROR_CODE] CreateIpForwardEntry(
        PMIB_IPFORWARDROW pRoute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRoute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateIpForwardEntry2(jitter):
    """
    NETIOAPI_API CreateIpForwardEntry2(
        const MIB_IPFORWARD_ROW2* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIpForwardEntry(jitter):
    """
    [ERROR_CODE] DeleteIpForwardEntry(
        PMIB_IPFORWARDROW pRoute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRoute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeleteIpForwardEntry2(jitter):
    """
    NETIOAPI_API DeleteIpForwardEntry2(
        const MIB_IPFORWARD_ROW2* Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_EnableRouter(jitter):
    """
    [ERROR_CODE] EnableRouter(
        HANDLE* pHandle,
        OVERLAPPED* pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pHandle", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetBestInterface(jitter):
    """
    [ERROR_CODE] GetBestInterface(
        IPAddr dwDestAddr,
        PDWORD pdwBestIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDestAddr", "pdwBestIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetBestInterfaceEx(jitter):
    """
    [ERROR_CODE] GetBestInterfaceEx(
        struct sockaddr* pDestAddr,
        PDWORD pdwBestIfIndex
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDestAddr", "pdwBestIfIndex"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetBestRoute(jitter):
    """
    [ERROR_CODE] GetBestRoute(
        DWORD dwDestAddr,
        DWORD dwSourceAddr,
        PMIB_IPFORWARDROW pBestRoute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["dwDestAddr", "dwSourceAddr", "pBestRoute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetBestRoute2(jitter):
    """
    NETIOAPI_API GetBestRoute2(
        NET_LUID* InterfaceLuid,
        NET_IFINDEX InterfaceIndex,
        const SOCKADDR_INET* SourceAddress,
        const SOCKADDR_INET* DestinationAddress,
        ULONG AddressSortOptions,
        PMIB_IPFORWARD_ROW2 BestRoute,
        SOCKADDR_INET* BestSourceAddress
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceLuid", "InterfaceIndex", "SourceAddress", "DestinationAddress", "AddressSortOptions", "BestRoute", "BestSourceAddress"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpForwardEntry2(jitter):
    """
    NETIOAPI_API GetIpForwardEntry2(
        PMIB_IPFORWARD_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpForwardTable(jitter):
    """
    [ERROR_CODE] GetIpForwardTable(
        PMIB_IPFORWARDTABLE pIpForwardTable,
        PULONG pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpForwardTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpForwardTable2(jitter):
    """
    NETIOAPI_API GetIpForwardTable2(
        ADDRESS_FAMILY Family,
        PMIB_IPFORWARD_TABLE2* Table
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Table"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetRTTAndHopCount(jitter):
    """
    BOOL GetRTTAndHopCount(
        IPAddr DestIpAddress,
        PULONG HopCount,
        ULONG MaxHops,
        PULONG RTT
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DestIpAddress", "HopCount", "MaxHops", "RTT"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_InitializeIpForwardEntry(jitter):
    """
    VOID InitializeIpForwardEntry(
        PMIB_IPFORWARD_ROW2 Row
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpForwardEntry(jitter):
    """
    [ERROR_CODE] SetIpForwardEntry(
        PMIB_IPFORWARDROW pRoute
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pRoute"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpForwardEntry2(jitter):
    """
    NETIOAPI_API SetIpForwardEntry2(
        const MIB_IPFORWARD_ROW2* Route
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Route"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpStatistics(jitter):
    """
    [ERROR_CODE] SetIpStatistics(
        PMIB_IPSTATS pIpStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetIpStatisticsEx(jitter):
    """
    [ERROR_CODE] SetIpStatisticsEx(
        PMIB_IPSTATS pIpStats,
        ULONG Family
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pIpStats", "Family"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_UnenableRouter(jitter):
    """
    [ERROR_CODE] UnenableRouter(
        OVERLAPPED* pOverlapped,
        LPDWORD lpdwEnableCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOverlapped", "lpdwEnableCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_FreeMibTable(jitter):
    """
    VOID FreeMibTable(
        PVOID Memory
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Memory"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertIpv4MaskToLength(jitter):
    """
    NETIO_STATUS ConvertIpv4MaskToLength(
        ULONG Mask,
        PUINT8 MaskLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Mask", "MaskLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ConvertLengthToIpv4Mask(jitter):
    """
    NETIO_STATUS ConvertLengthToIpv4Mask(
        ULONG MaskLength,
        PULONG Mask
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MaskLength", "Mask"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreateSortedAddressPairs(jitter):
    """
    NETIOAPI_API CreateSortedAddressPairs(
        const PSOCKADDR_IN6 SourceAddressList,
        ULONG SourceAddressCount,
        const PSOCKADDR_IN6 DestinationAddressList,
        ULONG DestinationAddressCount,
        ULONG AddressSortOptions,
        PSOCKADDR_IN6_PAIR* SortedAddressPairList,
        ULONG* SortedAddressPairCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SourceAddressList", "SourceAddressCount", "DestinationAddressList", "DestinationAddressCount", "AddressSortOptions", "SortedAddressPairList", "SortedAddressPairCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_ParseNetworkString(jitter):
    """
    [ERROR_CODE] ParseNetworkString(
        const WCHAR* NetworkString,
        DWORD Types,
        PNET_ADDRESS_INFO AddressInfo,
        USHORT* PortNumber,
        BYTE* PrefixLength
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NetworkString", "Types", "AddressInfo", "PortNumber", "PrefixLength"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetNetworkParams(jitter):
    """
    [ERROR_CODE] GetNetworkParams(
        PFIXED_INFO pFixedInfo,
        PULONG pOutBufLen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pFixedInfo", "pOutBufLen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CancelMibChangeNotify2(jitter):
    """
    NETIOAPI_API CancelMibChangeNotify2(
        HANDLE NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyAddrChange(jitter):
    """
    [ERROR_CODE] NotifyAddrChange(
        PHANDLE Handle,
        LPOVERLAPPED overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyIpInterfaceChange(jitter):
    """
    NETIOAPI_API NotifyIpInterfaceChange(
        ADDRESS_FAMILY Family,
        PIPINTERFACE_CHANGE_CALLBACK Callback,
        PVOID CallerContext,
        BOOLEAN InitialNotification,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Callback", "CallerContext", "InitialNotification", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyRouteChange(jitter):
    """
    [ERROR_CODE] NotifyRouteChange(
        PHANDLE Handle,
        LPOVERLAPPED overlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Handle", "overlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyRouteChange2(jitter):
    """
    NETIOAPI_API NotifyRouteChange2(
        ADDRESS_FAMILY Family,
        PIPFORWARD_CHANGE_CALLBACK Callback,
        PVOID CallerContext,
        BOOLEAN InitialNotification,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Callback", "CallerContext", "InitialNotification", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyUnicastIpAddressChange(jitter):
    """
    NETIOAPI_API NotifyUnicastIpAddressChange(
        ADDRESS_FAMILY Family,
        PUNICAST_IPADDRESS_CHANGE_CALLBACK Callback,
        PVOID CallerContext,
        BOOLEAN InitialNotification,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Family", "Callback", "CallerContext", "InitialNotification", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CancelSecurityHealthChangeNotify(jitter):
    """
    BOOL CancelSecurityHealthChangeNotify(
        LPOVERLAPPED notifyOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["notifyOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifySecurityHealthChange(jitter):
    """
    [ERROR_CODE] NotifySecurityHealthChange(
        PHANDLE pHandle,
        LPOVERLAPPED pOverLapped,
        PULONG SecurityHealthFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pHandle", "pOverLapped", "SecurityHealthFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTeredoPort(jitter):
    """
    NETIOAPI_API GetTeredoPort(
        USHORT* Port
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Port"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NotifyTeredoPortChange(jitter):
    """
    NETIOAPI_API NotifyTeredoPortChange(
        PTEREDO_PORT_CHANGE_CALLBACK Callback,
        PVOID CallerContext,
        BOOLEAN InitialNotification,
        HANDLE* NotificationHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Callback", "CallerContext", "InitialNotification", "NotificationHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetExtendedTcpTable(jitter):
    """
    [ERROR_CODE] GetExtendedTcpTable(
        PVOID pTcpTable,
        PDWORD pdwSize,
        BOOL bOrder,
        ADDRESS_FAMILY ulAf,
        TCP_TABLE_CLASS TableClass,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpTable", "pdwSize", "bOrder", "ulAf", "TableClass", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetExtendedUdpTable(jitter):
    """
    [ERROR_CODE] GetExtendedUdpTable(
        PVOID pUdpTable,
        PDWORD pdwSize,
        BOOL bOrder,
        ADDRESS_FAMILY ulAf,
        UDP_TABLE_CLASS TableClass,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUdpTable", "pdwSize", "bOrder", "ulAf", "TableClass", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetOwnerModuleFromTcp6Entry(jitter):
    """
    [ERROR_CODE] GetOwnerModuleFromTcp6Entry(
        PMIB_TCP6ROW_OWNER_MODULE pTcpEntry,
        TCPIP_OWNER_MODULE_INFO_CLASS Class,
        PVOID Buffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpEntry", "Class", "Buffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetOwnerModuleFromTcpEntry(jitter):
    """
    [ERROR_CODE] GetOwnerModuleFromTcpEntry(
        PMIB_TCPROW_OWNER_MODULE pTcpEntry,
        TCPIP_OWNER_MODULE_INFO_CLASS Class,
        PVOID Buffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpEntry", "Class", "Buffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetOwnerModuleFromUdp6Entry(jitter):
    """
    [ERROR_CODE] GetOwnerModuleFromUdp6Entry(
        PMIB_UDP6ROW_OWNER_MODULE pUdpEntry,
        TCPIP_OWNER_MODULE_INFO_CLASS Class,
        PVOID Buffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUdpEntry", "Class", "Buffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetOwnerModuleFromUdpEntry(jitter):
    """
    [ERROR_CODE] GetOwnerModuleFromUdpEntry(
        PMIB_UDPROW_OWNER_MODULE pUdpEntry,
        TCPIP_OWNER_MODULE_INFO_CLASS Class,
        PVOID Buffer,
        PDWORD pdwSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUdpEntry", "Class", "Buffer", "pdwSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetPerTcp6ConnectionEStats(jitter):
    """
    [ERROR_CODE_ULONG] GetPerTcp6ConnectionEStats(
        PMIB_TCP6ROW Row,
        TCP_ESTATS_TYPE EstatsType,
        PUCHAR Rw,
        ULONG RwVersion,
        ULONG RwSize,
        PUCHAR Ros,
        ULONG RosVersion,
        ULONG RosSize,
        PUCHAR Rod,
        ULONG RodVersion,
        ULONG RodSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "EstatsType", "Rw", "RwVersion", "RwSize", "Ros", "RosVersion", "RosSize", "Rod", "RodVersion", "RodSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetPerTcpConnectionEStats(jitter):
    """
    [ERROR_CODE_ULONG] GetPerTcpConnectionEStats(
        PMIB_TCPROW Row,
        TCP_ESTATS_TYPE EstatsType,
        PUCHAR Rw,
        ULONG RwVersion,
        ULONG RwSize,
        PUCHAR Ros,
        ULONG RosVersion,
        ULONG RosSize,
        PUCHAR Rod,
        ULONG RodVersion,
        ULONG RodSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "EstatsType", "Rw", "RwVersion", "RwSize", "Ros", "RosVersion", "RosSize", "Rod", "RodVersion", "RodSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcpStatistics(jitter):
    """
    [ERROR_CODE] GetTcpStatistics(
        PMIB_TCPSTATS pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcpStatisticsEx(jitter):
    """
    [ERROR_CODE] GetTcpStatisticsEx(
        PMIB_TCPSTATS pStats,
        ADDRESS_FAMILY dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcp6Table(jitter):
    """
    [ERROR_CODE_ULONG] GetTcp6Table(
        PMIB_TCP6TABLE TcpTable,
        PULONG SizePointer,
        BOOL Order
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TcpTable", "SizePointer", "Order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcp6Table2(jitter):
    """
    [ERROR_CODE_ULONG] GetTcp6Table2(
        PMIB_TCP6TABLE2 TcpTable,
        PULONG SizePointer,
        BOOL Order
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TcpTable", "SizePointer", "Order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcpTable(jitter):
    """
    [ERROR_CODE] GetTcpTable(
        PMIB_TCPTABLE pTcpTable,
        PDWORD pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetTcpTable2(jitter):
    """
    [ERROR_CODE_ULONG] GetTcpTable2(
        PMIB_TCPTABLE2 TcpTable,
        PULONG SizePointer,
        BOOL Order
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["TcpTable", "SizePointer", "Order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetPerTcp6ConnectionEStats(jitter):
    """
    [ERROR_CODE_ULONG] SetPerTcp6ConnectionEStats(
        PMIB_TCP6ROW Row,
        TCP_ESTATS_TYPE EstatsType,
        PUCHAR Rw,
        ULONG RwVersion,
        ULONG RwSize,
        ULONG Offset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "EstatsType", "Rw", "RwVersion", "RwSize", "Offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetPerTcpConnectionEStats(jitter):
    """
    [ERROR_CODE_ULONG] SetPerTcpConnectionEStats(
        PMIB_TCP6ROW Row,
        TCP_ESTATS_TYPE EstatsType,
        PUCHAR Rw,
        ULONG RwVersion,
        ULONG RwSize,
        ULONG Offset
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Row", "EstatsType", "Rw", "RwVersion", "RwSize", "Offset"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_SetTcpEntry(jitter):
    """
    [ERROR_CODE] SetTcpEntry(
        PMIB_TCPROW pTcpRow
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pTcpRow"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUdp6Table(jitter):
    """
    [ERROR_CODE_ULONG] GetUdp6Table(
        PMIB_UDP6TABLE Udp6Table,
        PULONG SizePointer,
        BOOL Order
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Udp6Table", "SizePointer", "Order"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUdpStatistics(jitter):
    """
    [ERROR_CODE] GetUdpStatistics(
        PMIB_UDPSTATS pStats
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUdpStatisticsEx(jitter):
    """
    [ERROR_CODE] GetUdpStatisticsEx(
        PMIB_UDPSTATS pStats,
        ADDRESS_FAMILY dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetUdpTable(jitter):
    """
    [ERROR_CODE] GetUdpTable(
        PMIB_UDPTABLE pUdpTable,
        PDWORD pdwSize,
        BOOL bOrder
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pUdpTable", "pdwSize", "bOrder"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_AllocateAndGetTcpExTableFromStack(jitter):
    """
    [ERROR_CODE] AllocateAndGetTcpExTableFromStack(
        PVOID* ppTcpTable,
        BOOL bOrder,
        HANDLE hHeap,
        DWORD dwFlags,
        ADDRESS_FAMILY dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppTcpTable", "bOrder", "hHeap", "dwFlags", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_AllocateAndGetUdpExTableFromStack(jitter):
    """
    [ERROR_CODE] AllocateAndGetUdpExTableFromStack(
        PVOID* ppUDPTable,
        BOOL bOrder,
        HANDLE hHeap,
        DWORD dwFlags,
        ADDRESS_FAMILY dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppUDPTable", "bOrder", "hHeap", "dwFlags", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpCloseHandle(jitter):
    """
    BOOL IcmpCloseHandle(
        HANDLE IcmpHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpCreateFile(jitter):
    """
    [FILE_HANDLE] IcmpCreateFile()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpParseReplies(jitter):
    """
    DWORD IcmpParseReplies(
        LPVOID ReplyBuffer,
        DWORD ReplySize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ReplyBuffer", "ReplySize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpSendEcho(jitter):
    """
    [ERROR_CODE] IcmpSendEcho(
        HANDLE IcmpHandle,
        IPAddr DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_IcmpSendEcho2(jitter):
    """
    [ERROR_CODE] IcmpSendEcho2(
        HANDLE IcmpHandle,
        HANDLE Event,
        PIO_APC_ROUTINE ApcRoutine,
        PVOID ApcContext,
        IPAddr DestinationAddress,
        LPVOID RequestData,
        WORD RequestSize,
        PIP_OPTION_INFORMATION RequestOptions,
        LPVOID ReplyBuffer,
        DWORD ReplySize,
        DWORD Timeout
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["IcmpHandle", "Event", "ApcRoutine", "ApcContext", "DestinationAddress", "RequestData", "RequestSize", "RequestOptions", "ReplyBuffer", "ReplySize", "Timeout"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpNetworkConnectionBandwidthEstimates(jitter):
    """
    NETIOAPI_API GetIpNetworkConnectionBandwidthEstimates(
        NET_IFINDEX InterfaceIndex,
        ADDRESS_FAMILY AddressFamily,
        PMIB_IP_NETWORK_CONNECTION_BANDWIDTH_ESTIMATES BandwidthEstimates
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["InterfaceIndex", "AddressFamily", "BandwidthEstimates"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CancelIPChangeNotify(jitter):
    """
    BOOL CancelIPChangeNotify(
        LPOVERLAPPED notifyOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["notifyOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreatePersistentTcpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] CreatePersistentTcpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts,
        PULONG64 Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_CreatePersistentUdpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] CreatePersistentUdpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts,
        PULONG64 Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeletePersistentTcpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] DeletePersistentTcpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DeletePersistentUdpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] DeletePersistentUdpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_DisableMediaSense(jitter):
    """
    [ERROR_CODE] DisableMediaSense(
        HANDLE* pHandle,
        OVERLAPPED* pOverlapped
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pHandle", "pOverlapped"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetAdapterOrderMap(jitter):
    """
    PIP_ADAPTER_ORDER_MAP GetAdapterOrderMap()
    """
    ret_ad, args = jitter.func_args_stdcall([])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIcmpStatisticsEx(jitter):
    """
    [ERROR_CODE] GetIcmpStatisticsEx(
        PMIB_ICMP_EX pStats,
        DWORD dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpErrorString(jitter):
    """
    [ERROR_CODE] GetIpErrorString(
        IP_STATUS ErrorCode,
        PWCHAR Buffer,
        PDWORD Size
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ErrorCode", "Buffer", "Size"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_GetIpStatisticsEx(jitter):
    """
    [ERROR_CODE] GetIpStatisticsEx(
        PMIB_IPSTATS pStats,
        DWORD dwFamily
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pStats", "dwFamily"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_LookupPersistentTcpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] LookupPersistentTcpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts,
        PULONG64 Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_LookupPersistentUdpPortReservation(jitter):
    """
    [ERROR_CODE_ULONG] LookupPersistentUdpPortReservation(
        USHORT StartPort,
        USHORT NumberOfPorts,
        PULONG64 Token
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["StartPort", "NumberOfPorts", "Token"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_NhpAllocateAndGetInterfaceInfoFromStack(jitter):
    """
    [ERROR_CODE] NhpAllocateAndGetInterfaceInfoFromStack(
        IP_INTERFACE_NAME_INFO** ppTable,
        PDWORD pdwCount,
        BOOL bOrder,
        HANDLE hHeap,
        DWORD dwFlags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ppTable", "pdwCount", "bOrder", "hHeap", "dwFlags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def iphlpapi_RestoreMediaSense(jitter):
    """
    [ERROR_CODE] RestoreMediaSense(
        OVERLAPPED* pOverlapped,
        LPDWORD lpdwEnableCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pOverlapped", "lpdwEnableCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
