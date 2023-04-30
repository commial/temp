###### Enums ######
NET_API_STATUS = {
    "NERR_Success": 0,
    "NERR_NetNotStarted": 2102,
    "NERR_UnknownServer": 2103,
    "NERR_ShareMem": 2104,
    "NERR_NoNetworkResource": 2105,
    "NERR_RemoteOnly": 2106,
    "NERR_DevNotRedirected": 2107,
    "NERR_ServerNotStarted": 2114,
    "NERR_ItemNotFound": 2115,
    "NERR_UnknownDevDir": 2116,
    "NERR_RedirectedPath": 2117,
    "NERR_DuplicateShare": 2118,
    "NERR_NoRoom": 2119,
    "NERR_TooManyItems": 2121,
    "NERR_InvalidMaxUsers": 2122,
    "NERR_BufTooSmall": 2123,
    "NERR_RemoteErr": 2127,
    "NERR_LanmanIniError": 2131,
    "NERR_NetworkError": 2136,
    "NERR_WkstaInconsistentState": 2137,
    "NERR_WkstaNotStarted": 2138,
    "NERR_BrowserNotStarted": 2139,
    "NERR_InternalError": 2140,
    "NERR_BadTransactConfig": 2141,
    "NERR_InvalidAPI": 2142,
    "NERR_BadEventName": 2143,
    "NERR_DupNameReboot": 2144,
    "NERR_CfgCompNotFound": 2146,
    "NERR_CfgParamNotFound": 2147,
    "NERR_LineTooLong": 2149,
    "NERR_QNotFound": 2150,
    "NERR_JobNotFound": 2151,
    "NERR_DestNotFound": 2152,
    "NERR_DestExists": 2153,
    "NERR_QExists": 2154,
    "NERR_QNoRoom": 2155,
    "NERR_JobNoRoom": 2156,
    "NERR_DestNoRoom": 2157,
    "NERR_DestIdle": 2158,
    "NERR_DestInvalidOp": 2159,
    "NERR_ProcNoRespond": 2160,
    "NERR_SpoolerNotLoaded": 2161,
    "NERR_DestInvalidState": 2162,
    "NERR_QInvalidState": 2163,
    "NERR_JobInvalidState": 2164,
    "NERR_SpoolNoMemory": 2165,
    "NERR_DriverNotFound": 2166,
    "NERR_DataTypeInvalid": 2167,
    "NERR_ProcNotFound": 2168,
    "NERR_ServiceTableLocked": 2180,
    "NERR_ServiceTableFull": 2181,
    "NERR_ServiceInstalled": 2182,
    "NERR_ServiceEntryLocked": 2183,
    "NERR_ServiceNotInstalled": 2184,
    "NERR_BadServiceName": 2185,
    "NERR_ServiceCtlTimeout": 2186,
    "NERR_ServiceCtlBusy": 2187,
    "NERR_BadServiceProgName": 2188,
    "NERR_ServiceNotCtrl": 2189,
    "NERR_ServiceKillProc": 2190,
    "NERR_ServiceCtlNotValid": 2191,
    "NERR_NotInDispatchTbl": 2192,
    "NERR_BadControlRecv": 2193,
    "NERR_ServiceNotStarting": 2194,
    "NERR_AlreadyLoggedOn": 2200,
    "NERR_NotLoggedOn": 2201,
    "NERR_BadUsername": 2202,
    "NERR_BadPassword": 2203,
    "NERR_UnableToAddName_W": 2204,
    "NERR_UnableToAddName_F": 2205,
    "NERR_UnableToDelName_W": 2206,
    "NERR_UnableToDelName_F": 2207,
    "NERR_LogonsPaused": 2209,
    "NERR_LogonServerConflict": 2210,
    "NERR_LogonNoUserPath": 2211,
    "NERR_LogonScriptError": 2212,
    "NERR_StandaloneLogon": 2214,
    "NERR_LogonServerNotFound": 2215,
    "NERR_LogonDomainExists": 2216,
    "NERR_NonValidatedLogon": 2217,
    "NERR_ACFNotFound": 2219,
    "NERR_GroupNotFound": 2220,
    "NERR_UserNotFound": 2221,
    "NERR_ResourceNotFound": 2222,
    "NERR_GroupExists": 2223,
    "NERR_UserExists": 2224,
    "NERR_ResourceExists": 2225,
    "NERR_NotPrimary": 2226,
    "NERR_ACFNotLoaded": 2227,
    "NERR_ACFNoRoom": 2228,
    "NERR_ACFFileIOFail": 2229,
    "NERR_ACFTooManyLists": 2230,
    "NERR_UserLogon": 2231,
    "NERR_ACFNoParent": 2232,
    "NERR_CanNotGrowSegment": 2233,
    "NERR_SpeGroupOp": 2234,
    "NERR_NotInCache": 2235,
    "NERR_UserInGroup": 2236,
    "NERR_UserNotInGroup": 2237,
    "NERR_AccountUndefined": 2238,
    "NERR_AccountExpired": 2239,
    "NERR_InvalidWorkstation": 2240,
    "NERR_InvalidLogonHours": 2241,
    "NERR_PasswordExpired": 2242,
    "NERR_PasswordCantChange": 2243,
    "NERR_PasswordHistConflict": 2244,
    "NERR_PasswordTooShort": 2245,
    "NERR_PasswordTooRecent": 2246,
    "NERR_InvalidDatabase": 2247,
    "NERR_DatabaseUpToDate": 2248,
    "NERR_SyncRequired": 2249,
    "NERR_UseNotFound": 2250,
    "NERR_BadAsgType": 2251,
    "NERR_DeviceIsShared": 2252,
    "NERR_SameAsComputerName": 2253,
    "NERR_NoComputerName": 2270,
    "NERR_MsgAlreadyStarted": 2271,
    "NERR_MsgInitFailed": 2272,
    "NERR_NameNotFound": 2273,
    "NERR_AlreadyForwarded": 2274,
    "NERR_AddForwarded": 2275,
    "NERR_AlreadyExists": 2276,
    "NERR_TooManyNames": 2277,
    "NERR_DelComputerName": 2278,
    "NERR_LocalForward": 2279,
    "NERR_GrpMsgProcessor": 2280,
    "NERR_PausedRemote": 2281,
    "NERR_BadReceive": 2282,
    "NERR_NameInUse": 2283,
    "NERR_MsgNotStarted": 2284,
    "NERR_NotLocalName": 2285,
    "NERR_NoForwardName": 2286,
    "NERR_RemoteFull": 2287,
    "NERR_NameNotForwarded": 2288,
    "NERR_TruncatedBroadcast": 2289,
    "NERR_InvalidDevice": 2294,
    "NERR_WriteFault": 2295,
    "NERR_DuplicateName": 2297,
    "NERR_DeleteLater": 2298,
    "NERR_IncompleteDel": 2299,
    "NERR_MultipleNets": 2300,
    "NERR_NetNameNotFound": 2310,
    "NERR_DeviceNotShared": 2311,
    "NERR_ClientNameNotFound": 2312,
    "NERR_FileIdNotFound": 2314,
    "NERR_ExecFailure": 2315,
    "NERR_TmpFile": 2316,
    "NERR_TooMuchData": 2317,
    "NERR_DeviceShareConflict": 2318,
    "NERR_BrowserTableIncomplete": 2319,
    "NERR_NotLocalDomain": 2320,
    "NERR_IsDfsShare": 2321,
    "NERR_DevInvalidOpCode": 2331,
    "NERR_DevNotFound": 2332,
    "NERR_DevNotOpen": 2333,
    "NERR_BadQueueDevString": 2334,
    "NERR_BadQueuePriority": 2335,
    "NERR_NoCommDevs": 2337,
    "NERR_QueueNotFound": 2338,
    "NERR_BadDevString": 2340,
    "NERR_BadDev": 2341,
    "NERR_InUseBySpooler": 2342,
    "NERR_CommDevInUse": 2343,
    "NERR_InvalidComputer": 2351,
    "NERR_MaxLenExceeded": 2354,
    "NERR_BadComponent": 2356,
    "NERR_CantType": 2357,
    "NERR_TooManyEntries": 2362,
    "NERR_ProfileFileTooBig": 2370,
    "NERR_ProfileOffset": 2371,
    "NERR_ProfileCleanup": 2372,
    "NERR_ProfileUnknownCmd": 2373,
    "NERR_ProfileLoadErr": 2374,
    "NERR_ProfileSaveErr": 2375,
    "NERR_LogOverflow": 2377,
    "NERR_LogFileChanged": 2378,
    "NERR_LogFileCorrupt": 2379,
    "NERR_SourceIsDir": 2380,
    "NERR_BadSource": 2381,
    "NERR_BadDest": 2382,
    "NERR_DifferentServers": 2383,
    "NERR_RunSrvPaused": 2385,
    "NERR_ErrCommRunSrv": 2389,
    "NERR_ErrorExecingGhost": 2391,
    "NERR_ShareNotFound": 2392,
    "NERR_InvalidLana": 2400,
    "NERR_OpenFiles": 2401,
    "NERR_ActiveConns": 2402,
    "NERR_BadPasswordCore": 2403,
    "NERR_DevInUse": 2404,
    "NERR_LocalDrive": 2405,
    "NERR_AlertExists": 2430,
    "NERR_TooManyAlerts": 2431,
    "NERR_NoSuchAlert": 2432,
    "NERR_BadRecipient": 2433,
    "NERR_AcctLimitExceeded": 2434,
    "NERR_InvalidLogSeek": 2440,
    "NERR_BadUasConfig": 2450,
    "NERR_InvalidUASOp": 2451,
    "NERR_LastAdmin": 2452,
    "NERR_DCNotFound": 2453,
    "NERR_LogonTrackingError": 2454,
    "NERR_NetlogonNotStarted": 2455,
    "NERR_CanNotGrowUASFile": 2456,
    "NERR_TimeDiffAtDC": 2457,
    "NERR_PasswordMismatch": 2458,
    "NERR_NoSuchServer": 2460,
    "NERR_NoSuchSession": 2461,
    "NERR_NoSuchConnection": 2462,
    "NERR_TooManyServers": 2463,
    "NERR_TooManySessions": 2464,
    "NERR_TooManyConnections": 2465,
    "NERR_TooManyFiles": 2466,
    "NERR_NoAlternateServers": 2467,
    "NERR_TryDownLevel": 2470,
    "NERR_UPSDriverNotStarted": 2480,
    "NERR_UPSInvalidConfig": 2481,
    "NERR_UPSInvalidCommPort": 2482,
    "NERR_UPSSignalAsserted": 2483,
    "NERR_UPSShutdownFailed": 2484,
    "NERR_BadDosRetCode": 2500,
    "NERR_ProgNeedsExtraMem": 2501,
    "NERR_BadDosFunction": 2502,
    "NERR_RemoteBootFailed": 2503,
    "NERR_BadFileCheckSum": 2504,
    "NERR_NoRplBootSystem": 2505,
    "NERR_RplLoadrNetBiosErr": 2506,
    "NERR_RplLoadrDiskErr": 2507,
    "NERR_ImageParamErr": 2508,
    "NERR_TooManyImageParams": 2509,
    "NERR_NonDosFloppyUsed": 2510,
    "NERR_RplBootRestart": 2511,
    "NERR_RplSrvrCallFailed": 2512,
    "NERR_CantConnectRplSrvr": 2513,
    "NERR_CantOpenImageFile": 2514,
    "NERR_CallingRplSrvr": 2515,
    "NERR_StartingRplBoot": 2516,
    "NERR_RplBootServiceTerm": 2517,
    "NERR_RplBootStartFailed": 2518,
    "NERR_RPL_CONNECTED": 2519,
    "NERR_BrowserConfiguredToNotRun": 2550,
    "NERR_RplNoAdaptersStarted": 2610,
    "NERR_RplBadRegistry": 2611,
    "NERR_RplBadDatabase": 2612,
    "NERR_RplRplfilesShare": 2613,
    "NERR_RplNotRplServer": 2614,
    "NERR_RplCannotEnum": 2615,
    "NERR_RplWkstaInfoCorrupted": 2616,
    "NERR_RplWkstaNotFound": 2617,
    "NERR_RplWkstaNameUnavailable": 2618,
    "NERR_RplProfileInfoCorrupted": 2619,
    "NERR_RplProfileNotFound": 2620,
    "NERR_RplProfileNameUnavailable": 2621,
    "NERR_RplProfileNotEmpty": 2622,
    "NERR_RplConfigInfoCorrupted": 2623,
    "NERR_RplConfigNotFound": 2624,
    "NERR_RplAdapterInfoCorrupted": 2625,
    "NERR_RplInternal": 2626,
    "NERR_RplVendorInfoCorrupted": 2627,
    "NERR_RplBootInfoCorrupted": 2628,
    "NERR_RplWkstaNeedsUserAcct": 2629,
    "NERR_RplNeedsRPLUSERAcct": 2630,
    "NERR_RplBootNotFound": 2631,
    "NERR_RplIncompatibleProfile": 2632,
    "NERR_RplAdapterNameUnavailable": 2633,
    "NERR_RplConfigNotEmpty": 2634,
    "NERR_RplBootInUse": 2635,
    "NERR_RplBackupDatabase": 2636,
    "NERR_RplAdapterNotFound": 2637,
    "NERR_RplVendorNotFound": 2638,
    "NERR_RplVendorNameUnavailable": 2639,
    "NERR_RplBootNameUnavailable": 2640,
    "NERR_RplConfigNameUnavailable": 2641,
    "NERR_DfsInternalCorruption": 2660,
    "NERR_DfsVolumeDataCorrupt": 2661,
    "NERR_DfsNoSuchVolume": 2662,
    "NERR_DfsVolumeAlreadyExists": 2663,
    "NERR_DfsAlreadyShared": 2664,
    "NERR_DfsNoSuchShare": 2665,
    "NERR_DfsNotALeafVolume": 2666,
    "NERR_DfsLeafVolume": 2667,
    "NERR_DfsVolumeHasMultipleServers": 2668,
    "NERR_DfsCantCreateJunctionPoint": 2669,
    "NERR_DfsServerNotDfsAware": 2670,
    "NERR_DfsBadRenamePath": 2671,
    "NERR_DfsVolumeIsOffline": 2672,
    "NERR_DfsNoSuchServer": 2673,
    "NERR_DfsCyclicalName": 2674,
    "NERR_DfsNotSupportedInServerDfs": 2675,
    "NERR_DfsDuplicateService": 2676,
    "NERR_DfsCantRemoveLastServerShare": 2677,
    "NERR_DfsVolumeIsInterDfs": 2678,
    "NERR_DfsInconsistent": 2679,
    "NERR_DfsServerUpgraded": 2680,
    "NERR_DfsDataIsIdentical": 2681,
    "NERR_DfsCantRemoveDfsRoot": 2682,
    "NERR_DfsChildOrParentInDfs": 2683,
    "NERR_DfsInternalError": 2690,
    "NERR_SetupAlreadyJoined": 2691,
    "NERR_SetupNotJoined": 2692,
    "NERR_SetupDomainController": 2693,
    "NERR_DefaultJoinRequired": 2694,
    "NERR_InvalidWorkgroupName": 2695,
    "NERR_NameUsesIncompatibleCodePage": 2696,
    "NERR_ComputerAccountNotFound": 2697,
    "NERR_PersonalSku": 2698,
    "NERR_SetupCheckDNSConfig": 2699,
    "NERR_PasswordMustChange": 2701,
    "NERR_AccountLockedOut": 2702,
    "NERR_PasswordTooLong": 2703,
    "NERR_PasswordNotComplexEnough": 2704,
    "NERR_PasswordFilterError": 2705,
    "NERR_NoOfflineJoinInfo": 2709,
    "NERR_BadOfflineJoinInfo": 2710,
    "NERR_CantCreateJoinInfo": 2711,
    "NERR_BadDomainJoinInfo": 2712,
    "NERR_JoinPerformedMustRestart": 2713,
    "NERR_NoJoinPending": 2714,
    "NERR_ValuesNotSet": 2715,
    "NERR_CantVerifyHostname": 2716,
    "NERR_CantLoadOfflineHive": 2717,
    "NERR_ConnectionInsecure": 2718,
    "NERR_ProvisioningBlobUnsupported": 2719,
    "NERR_DS8DCRequired": 2720,
    "NERR_LDAPCapableDCRequired": 2721,
    "NERR_DS8DCNotFound": 2722,
    "NERR_TargetVersionUnsupported": 2723,
    "ERROR_ACCESS_DENIED": 5,
    "ERROR_NOT_ENOUGH_MEMORY": 8,
    "ERROR_NOT_SUPPORTED": 50,
    "ERROR_DUP_NAME": 52,
    "ERROR_BAD_NETPATH": 53,
    "ERROR_INVALID_PASSWORD": 86,
    "ERROR_INVALID_PARAMETER": 87,
    "ERROR_INVALID_NAME": 123,
    "ERROR_INVALID_LEVEL": 124,
    "ERROR_MORE_DATA": 234,
    "ERROR_INVALID_DOMAIN_ROLE": 1354,
    "ERROR_NO_SUCH_DOMAIN": 1355,
    "ERROR_WRONG_TARGET_NAME": 1396,
    "RPC_S_PROTSEQ_NOT_SUPPORTED": 1703,
    "RPC_S_CALL_IN_PROGRESS": 1791,
    "ERROR_NO_BROWSER_SERVERS_FOUND": 6118,
}
NET_API_STATUS_INV = {
    0: "NERR_Success",
    2102: "NERR_NetNotStarted",
    2103: "NERR_UnknownServer",
    2104: "NERR_ShareMem",
    2105: "NERR_NoNetworkResource",
    2106: "NERR_RemoteOnly",
    2107: "NERR_DevNotRedirected",
    2114: "NERR_ServerNotStarted",
    2115: "NERR_ItemNotFound",
    2116: "NERR_UnknownDevDir",
    2117: "NERR_RedirectedPath",
    2118: "NERR_DuplicateShare",
    2119: "NERR_NoRoom",
    2121: "NERR_TooManyItems",
    2122: "NERR_InvalidMaxUsers",
    2123: "NERR_BufTooSmall",
    2127: "NERR_RemoteErr",
    2131: "NERR_LanmanIniError",
    2136: "NERR_NetworkError",
    2137: "NERR_WkstaInconsistentState",
    2138: "NERR_WkstaNotStarted",
    2139: "NERR_BrowserNotStarted",
    2140: "NERR_InternalError",
    2141: "NERR_BadTransactConfig",
    2142: "NERR_InvalidAPI",
    2143: "NERR_BadEventName",
    2144: "NERR_DupNameReboot",
    2146: "NERR_CfgCompNotFound",
    2147: "NERR_CfgParamNotFound",
    2149: "NERR_LineTooLong",
    2150: "NERR_QNotFound",
    2151: "NERR_JobNotFound",
    2152: "NERR_DestNotFound",
    2153: "NERR_DestExists",
    2154: "NERR_QExists",
    2155: "NERR_QNoRoom",
    2156: "NERR_JobNoRoom",
    2157: "NERR_DestNoRoom",
    2158: "NERR_DestIdle",
    2159: "NERR_DestInvalidOp",
    2160: "NERR_ProcNoRespond",
    2161: "NERR_SpoolerNotLoaded",
    2162: "NERR_DestInvalidState",
    2163: "NERR_QInvalidState",
    2164: "NERR_JobInvalidState",
    2165: "NERR_SpoolNoMemory",
    2166: "NERR_DriverNotFound",
    2167: "NERR_DataTypeInvalid",
    2168: "NERR_ProcNotFound",
    2180: "NERR_ServiceTableLocked",
    2181: "NERR_ServiceTableFull",
    2182: "NERR_ServiceInstalled",
    2183: "NERR_ServiceEntryLocked",
    2184: "NERR_ServiceNotInstalled",
    2185: "NERR_BadServiceName",
    2186: "NERR_ServiceCtlTimeout",
    2187: "NERR_ServiceCtlBusy",
    2188: "NERR_BadServiceProgName",
    2189: "NERR_ServiceNotCtrl",
    2190: "NERR_ServiceKillProc",
    2191: "NERR_ServiceCtlNotValid",
    2192: "NERR_NotInDispatchTbl",
    2193: "NERR_BadControlRecv",
    2194: "NERR_ServiceNotStarting",
    2200: "NERR_AlreadyLoggedOn",
    2201: "NERR_NotLoggedOn",
    2202: "NERR_BadUsername",
    2203: "NERR_BadPassword",
    2204: "NERR_UnableToAddName_W",
    2205: "NERR_UnableToAddName_F",
    2206: "NERR_UnableToDelName_W",
    2207: "NERR_UnableToDelName_F",
    2209: "NERR_LogonsPaused",
    2210: "NERR_LogonServerConflict",
    2211: "NERR_LogonNoUserPath",
    2212: "NERR_LogonScriptError",
    2214: "NERR_StandaloneLogon",
    2215: "NERR_LogonServerNotFound",
    2216: "NERR_LogonDomainExists",
    2217: "NERR_NonValidatedLogon",
    2219: "NERR_ACFNotFound",
    2220: "NERR_GroupNotFound",
    2221: "NERR_UserNotFound",
    2222: "NERR_ResourceNotFound",
    2223: "NERR_GroupExists",
    2224: "NERR_UserExists",
    2225: "NERR_ResourceExists",
    2226: "NERR_NotPrimary",
    2227: "NERR_ACFNotLoaded",
    2228: "NERR_ACFNoRoom",
    2229: "NERR_ACFFileIOFail",
    2230: "NERR_ACFTooManyLists",
    2231: "NERR_UserLogon",
    2232: "NERR_ACFNoParent",
    2233: "NERR_CanNotGrowSegment",
    2234: "NERR_SpeGroupOp",
    2235: "NERR_NotInCache",
    2236: "NERR_UserInGroup",
    2237: "NERR_UserNotInGroup",
    2238: "NERR_AccountUndefined",
    2239: "NERR_AccountExpired",
    2240: "NERR_InvalidWorkstation",
    2241: "NERR_InvalidLogonHours",
    2242: "NERR_PasswordExpired",
    2243: "NERR_PasswordCantChange",
    2244: "NERR_PasswordHistConflict",
    2245: "NERR_PasswordTooShort",
    2246: "NERR_PasswordTooRecent",
    2247: "NERR_InvalidDatabase",
    2248: "NERR_DatabaseUpToDate",
    2249: "NERR_SyncRequired",
    2250: "NERR_UseNotFound",
    2251: "NERR_BadAsgType",
    2252: "NERR_DeviceIsShared",
    2253: "NERR_SameAsComputerName",
    2270: "NERR_NoComputerName",
    2271: "NERR_MsgAlreadyStarted",
    2272: "NERR_MsgInitFailed",
    2273: "NERR_NameNotFound",
    2274: "NERR_AlreadyForwarded",
    2275: "NERR_AddForwarded",
    2276: "NERR_AlreadyExists",
    2277: "NERR_TooManyNames",
    2278: "NERR_DelComputerName",
    2279: "NERR_LocalForward",
    2280: "NERR_GrpMsgProcessor",
    2281: "NERR_PausedRemote",
    2282: "NERR_BadReceive",
    2283: "NERR_NameInUse",
    2284: "NERR_MsgNotStarted",
    2285: "NERR_NotLocalName",
    2286: "NERR_NoForwardName",
    2287: "NERR_RemoteFull",
    2288: "NERR_NameNotForwarded",
    2289: "NERR_TruncatedBroadcast",
    2294: "NERR_InvalidDevice",
    2295: "NERR_WriteFault",
    2297: "NERR_DuplicateName",
    2298: "NERR_DeleteLater",
    2299: "NERR_IncompleteDel",
    2300: "NERR_MultipleNets",
    2310: "NERR_NetNameNotFound",
    2311: "NERR_DeviceNotShared",
    2312: "NERR_ClientNameNotFound",
    2314: "NERR_FileIdNotFound",
    2315: "NERR_ExecFailure",
    2316: "NERR_TmpFile",
    2317: "NERR_TooMuchData",
    2318: "NERR_DeviceShareConflict",
    2319: "NERR_BrowserTableIncomplete",
    2320: "NERR_NotLocalDomain",
    2321: "NERR_IsDfsShare",
    2331: "NERR_DevInvalidOpCode",
    2332: "NERR_DevNotFound",
    2333: "NERR_DevNotOpen",
    2334: "NERR_BadQueueDevString",
    2335: "NERR_BadQueuePriority",
    2337: "NERR_NoCommDevs",
    2338: "NERR_QueueNotFound",
    2340: "NERR_BadDevString",
    2341: "NERR_BadDev",
    2342: "NERR_InUseBySpooler",
    2343: "NERR_CommDevInUse",
    2351: "NERR_InvalidComputer",
    2354: "NERR_MaxLenExceeded",
    2356: "NERR_BadComponent",
    2357: "NERR_CantType",
    2362: "NERR_TooManyEntries",
    2370: "NERR_ProfileFileTooBig",
    2371: "NERR_ProfileOffset",
    2372: "NERR_ProfileCleanup",
    2373: "NERR_ProfileUnknownCmd",
    2374: "NERR_ProfileLoadErr",
    2375: "NERR_ProfileSaveErr",
    2377: "NERR_LogOverflow",
    2378: "NERR_LogFileChanged",
    2379: "NERR_LogFileCorrupt",
    2380: "NERR_SourceIsDir",
    2381: "NERR_BadSource",
    2382: "NERR_BadDest",
    2383: "NERR_DifferentServers",
    2385: "NERR_RunSrvPaused",
    2389: "NERR_ErrCommRunSrv",
    2391: "NERR_ErrorExecingGhost",
    2392: "NERR_ShareNotFound",
    2400: "NERR_InvalidLana",
    2401: "NERR_OpenFiles",
    2402: "NERR_ActiveConns",
    2403: "NERR_BadPasswordCore",
    2404: "NERR_DevInUse",
    2405: "NERR_LocalDrive",
    2430: "NERR_AlertExists",
    2431: "NERR_TooManyAlerts",
    2432: "NERR_NoSuchAlert",
    2433: "NERR_BadRecipient",
    2434: "NERR_AcctLimitExceeded",
    2440: "NERR_InvalidLogSeek",
    2450: "NERR_BadUasConfig",
    2451: "NERR_InvalidUASOp",
    2452: "NERR_LastAdmin",
    2453: "NERR_DCNotFound",
    2454: "NERR_LogonTrackingError",
    2455: "NERR_NetlogonNotStarted",
    2456: "NERR_CanNotGrowUASFile",
    2457: "NERR_TimeDiffAtDC",
    2458: "NERR_PasswordMismatch",
    2460: "NERR_NoSuchServer",
    2461: "NERR_NoSuchSession",
    2462: "NERR_NoSuchConnection",
    2463: "NERR_TooManyServers",
    2464: "NERR_TooManySessions",
    2465: "NERR_TooManyConnections",
    2466: "NERR_TooManyFiles",
    2467: "NERR_NoAlternateServers",
    2470: "NERR_TryDownLevel",
    2480: "NERR_UPSDriverNotStarted",
    2481: "NERR_UPSInvalidConfig",
    2482: "NERR_UPSInvalidCommPort",
    2483: "NERR_UPSSignalAsserted",
    2484: "NERR_UPSShutdownFailed",
    2500: "NERR_BadDosRetCode",
    2501: "NERR_ProgNeedsExtraMem",
    2502: "NERR_BadDosFunction",
    2503: "NERR_RemoteBootFailed",
    2504: "NERR_BadFileCheckSum",
    2505: "NERR_NoRplBootSystem",
    2506: "NERR_RplLoadrNetBiosErr",
    2507: "NERR_RplLoadrDiskErr",
    2508: "NERR_ImageParamErr",
    2509: "NERR_TooManyImageParams",
    2510: "NERR_NonDosFloppyUsed",
    2511: "NERR_RplBootRestart",
    2512: "NERR_RplSrvrCallFailed",
    2513: "NERR_CantConnectRplSrvr",
    2514: "NERR_CantOpenImageFile",
    2515: "NERR_CallingRplSrvr",
    2516: "NERR_StartingRplBoot",
    2517: "NERR_RplBootServiceTerm",
    2518: "NERR_RplBootStartFailed",
    2519: "NERR_RPL_CONNECTED",
    2550: "NERR_BrowserConfiguredToNotRun",
    2610: "NERR_RplNoAdaptersStarted",
    2611: "NERR_RplBadRegistry",
    2612: "NERR_RplBadDatabase",
    2613: "NERR_RplRplfilesShare",
    2614: "NERR_RplNotRplServer",
    2615: "NERR_RplCannotEnum",
    2616: "NERR_RplWkstaInfoCorrupted",
    2617: "NERR_RplWkstaNotFound",
    2618: "NERR_RplWkstaNameUnavailable",
    2619: "NERR_RplProfileInfoCorrupted",
    2620: "NERR_RplProfileNotFound",
    2621: "NERR_RplProfileNameUnavailable",
    2622: "NERR_RplProfileNotEmpty",
    2623: "NERR_RplConfigInfoCorrupted",
    2624: "NERR_RplConfigNotFound",
    2625: "NERR_RplAdapterInfoCorrupted",
    2626: "NERR_RplInternal",
    2627: "NERR_RplVendorInfoCorrupted",
    2628: "NERR_RplBootInfoCorrupted",
    2629: "NERR_RplWkstaNeedsUserAcct",
    2630: "NERR_RplNeedsRPLUSERAcct",
    2631: "NERR_RplBootNotFound",
    2632: "NERR_RplIncompatibleProfile",
    2633: "NERR_RplAdapterNameUnavailable",
    2634: "NERR_RplConfigNotEmpty",
    2635: "NERR_RplBootInUse",
    2636: "NERR_RplBackupDatabase",
    2637: "NERR_RplAdapterNotFound",
    2638: "NERR_RplVendorNotFound",
    2639: "NERR_RplVendorNameUnavailable",
    2640: "NERR_RplBootNameUnavailable",
    2641: "NERR_RplConfigNameUnavailable",
    2660: "NERR_DfsInternalCorruption",
    2661: "NERR_DfsVolumeDataCorrupt",
    2662: "NERR_DfsNoSuchVolume",
    2663: "NERR_DfsVolumeAlreadyExists",
    2664: "NERR_DfsAlreadyShared",
    2665: "NERR_DfsNoSuchShare",
    2666: "NERR_DfsNotALeafVolume",
    2667: "NERR_DfsLeafVolume",
    2668: "NERR_DfsVolumeHasMultipleServers",
    2669: "NERR_DfsCantCreateJunctionPoint",
    2670: "NERR_DfsServerNotDfsAware",
    2671: "NERR_DfsBadRenamePath",
    2672: "NERR_DfsVolumeIsOffline",
    2673: "NERR_DfsNoSuchServer",
    2674: "NERR_DfsCyclicalName",
    2675: "NERR_DfsNotSupportedInServerDfs",
    2676: "NERR_DfsDuplicateService",
    2677: "NERR_DfsCantRemoveLastServerShare",
    2678: "NERR_DfsVolumeIsInterDfs",
    2679: "NERR_DfsInconsistent",
    2680: "NERR_DfsServerUpgraded",
    2681: "NERR_DfsDataIsIdentical",
    2682: "NERR_DfsCantRemoveDfsRoot",
    2683: "NERR_DfsChildOrParentInDfs",
    2690: "NERR_DfsInternalError",
    2691: "NERR_SetupAlreadyJoined",
    2692: "NERR_SetupNotJoined",
    2693: "NERR_SetupDomainController",
    2694: "NERR_DefaultJoinRequired",
    2695: "NERR_InvalidWorkgroupName",
    2696: "NERR_NameUsesIncompatibleCodePage",
    2697: "NERR_ComputerAccountNotFound",
    2698: "NERR_PersonalSku",
    2699: "NERR_SetupCheckDNSConfig",
    2701: "NERR_PasswordMustChange",
    2702: "NERR_AccountLockedOut",
    2703: "NERR_PasswordTooLong",
    2704: "NERR_PasswordNotComplexEnough",
    2705: "NERR_PasswordFilterError",
    2709: "NERR_NoOfflineJoinInfo",
    2710: "NERR_BadOfflineJoinInfo",
    2711: "NERR_CantCreateJoinInfo",
    2712: "NERR_BadDomainJoinInfo",
    2713: "NERR_JoinPerformedMustRestart",
    2714: "NERR_NoJoinPending",
    2715: "NERR_ValuesNotSet",
    2716: "NERR_CantVerifyHostname",
    2717: "NERR_CantLoadOfflineHive",
    2718: "NERR_ConnectionInsecure",
    2719: "NERR_ProvisioningBlobUnsupported",
    2720: "NERR_DS8DCRequired",
    2721: "NERR_LDAPCapableDCRequired",
    2722: "NERR_DS8DCNotFound",
    2723: "NERR_TargetVersionUnsupported",
    5: "ERROR_ACCESS_DENIED",
    8: "ERROR_NOT_ENOUGH_MEMORY",
    50: "ERROR_NOT_SUPPORTED",
    52: "ERROR_DUP_NAME",
    53: "ERROR_BAD_NETPATH",
    86: "ERROR_INVALID_PASSWORD",
    87: "ERROR_INVALID_PARAMETER",
    123: "ERROR_INVALID_NAME",
    124: "ERROR_INVALID_LEVEL",
    234: "ERROR_MORE_DATA",
    1354: "ERROR_INVALID_DOMAIN_ROLE",
    1355: "ERROR_NO_SUCH_DOMAIN",
    1396: "ERROR_WRONG_TARGET_NAME",
    1703: "RPC_S_PROTSEQ_NOT_SUPPORTED",
    1791: "RPC_S_CALL_IN_PROGRESS",
    6118: "ERROR_NO_BROWSER_SERVERS_FOUND",
}
NET_COMPUTER_NAME_TYPE = {
    "NetPrimaryComputerName": 0,
    "NetAlternateComputerNames": 1,
    "NetAllComputerNames": 2,
    "NetComputerNameTypeMax": 3,
}
NET_COMPUTER_NAME_TYPE_INV = {
    0: "NetPrimaryComputerName",
    1: "NetAlternateComputerNames",
    2: "NetAllComputerNames",
    3: "NetComputerNameTypeMax",
}
NETSETUP_NAME_TYPE = {
    "NetSetupUnknown": 0,
    "NetSetupMachine": 1,
    "NetSetupWorkgroup": 2,
    "NetSetupDomain": 3,
    "NetSetupNonExistentDomain": 4,
    "NetSetupDnsMachine": 5,
}
NETSETUP_NAME_TYPE_INV = {
    0: "NetSetupUnknown",
    1: "NetSetupMachine",
    2: "NetSetupWorkgroup",
    3: "NetSetupDomain",
    4: "NetSetupNonExistentDomain",
    5: "NetSetupDnsMachine",
}
NET_VALIDATE_PASSWORD_TYPE = {
    "NetValidateAuthentication": 1,
    "NetValidatePasswordChange": 2,
    "NetValidatePasswordReset": 3,
}
NET_VALIDATE_PASSWORD_TYPE_INV = {
    1: "NetValidateAuthentication",
    2: "NetValidatePasswordChange",
    3: "NetValidatePasswordReset",
}
DSROLE_PRIMARY_DOMAIN_INFO_LEVEL = {
    "DsRolePrimaryDomainInfoBasic": 1,
    "DsRoleUpgradeStatus": 2,
    "DsRoleOperationState": 3,
}
DSROLE_PRIMARY_DOMAIN_INFO_LEVEL_INV = {
    1: "DsRolePrimaryDomainInfoBasic",
    2: "DsRoleUpgradeStatus",
    3: "DsRoleOperationState",
}
_DFS_FLAG_ = {
    "DFS_ADD_VOLUME": 1,
    "DFS_RESTORE_VOLUME": 2,
}
_DFS_FLAG__INV = {
    1: "DFS_ADD_VOLUME",
    2: "DFS_RESTORE_VOLUME",
}
DFS_NAMESPACE_VERSION_ORIGIN = {
    "DFS_NAMESPACE_VERSION_ORIGIN_COMBINED": 0,
    "DFS_NAMESPACE_VERSION_ORIGIN_SERVER": 1,
    "DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN": 2,
}
DFS_NAMESPACE_VERSION_ORIGIN_INV = {
    0: "DFS_NAMESPACE_VERSION_ORIGIN_COMBINED",
    1: "DFS_NAMESPACE_VERSION_ORIGIN_SERVER",
    2: "DFS_NAMESPACE_VERSION_ORIGIN_DOMAIN",
}

###################

###### Types ######
PZPWSTR_PTR = Ptr("<I", PWSTR())
LMSTR = LPWSTR
LMSTR___ = Ptr("<I", LMSTR())
_DsDomainFlags_ = ULONG

class DS_DOMAIN_TRUSTS(MemStruct):
    fields = [
        ("NetbiosDomainName", LPTSTR()),
        ("DnsDomainName", LPTSTR()),
        ("Flags", _DsDomainFlags_()),
        ("ParentIndex", ULONG()),
        ("TrustType", ULONG()),
        ("TrustAttributes", ULONG()),
        ("DomainSid", PSID()),
        ("DomainGuid", GUID()),
    ]

PDS_DOMAIN_TRUSTS = Ptr("<I", DS_DOMAIN_TRUSTS())
PDS_DOMAIN_TRUSTS_PTR = Ptr("<I", PDS_DOMAIN_TRUSTS())

class DOMAIN_CONTROLLER_INFO(MemStruct):
    fields = [
        ("DomainControllerName", LPTSTR()),
        ("DomainControllerAddress", LPTSTR()),
        ("DomainControllerAddressType", ULONG()),
        ("DomainGuid", GUID()),
        ("DomainName", LPTSTR()),
        ("DnsForestName", LPTSTR()),
        ("Flags", ULONG()),
        ("DcSiteName", LPTSTR()),
        ("ClientSiteName", LPTSTR()),
    ]

PDOMAIN_CONTROLLER_INFO = Ptr("<I", DOMAIN_CONTROLLER_INFO())
PDOMAIN_CONTROLLER_INFO_PTR = Ptr("<I", PDOMAIN_CONTROLLER_INFO())
NET_API_STATUS = DWORD
NET_COMPUTER_NAME_TYPE = UINT
NETSETUP_NAME_TYPE = UINT
NET_VALIDATE_PASSWORD_TYPE = LPVOID
DSROLE_PRIMARY_DOMAIN_INFO_LEVEL = UINT
_ServerType_ = DWORD
NETSETUP_JOIN_STATUS = UINT
PNETSETUP_JOIN_STATUS = Ptr("<I", NETSETUP_JOIN_STATUS())
_NetUserGetLocalGroupsFlags_ = DWORD
_DsGetDcNameFlags_ = ULONG
_NETSETUP_PROVISION_OPTIONS_ = DWORD

class NETSETUP_PROVISIONING_PARAMS(MemStruct):
    fields = [
        ("dwVersion", DWORD()),
        ("lpDomain", LPCWSTR()),
        ("lpMachineName", LPCWSTR()),
        ("lpMachineAccountOU", LPCWSTR()),
        ("lpDcName", LPCWSTR()),
        ("dwProvisionOptions", _NETSETUP_PROVISION_OPTIONS_()),
        ("aCertTemplateNames", LPCWSTR_PTR()),
        ("cCertTemplateNames", DWORD()),
        ("aMachinePolicyNames", LPCWSTR_PTR()),
        ("cMachinePolicyNames", DWORD()),
        ("aMachinePolicyPaths", LPCWSTR_PTR()),
        ("cMachinePolicyPaths", DWORD()),
    ]

PNETSETUP_PROVISIONING_PARAMS = Ptr("<I", NETSETUP_PROVISIONING_PARAMS())
_DFS_FLAG_ = DWORD
_DFS_MOVE_FLAG_ = ULONG
_DFS_REMOVE_FLAG_ = ULONG
DFS_NAMESPACE_VERSION_ORIGIN = UINT
_DFS_NAMESPACE_CAPABILITY_FLAG_ = ULONGLONG

class DFS_SUPPORTED_NAMESPACE_VERSION_INFO(MemStruct):
    fields = [
        ("DomainDfsMajorVersion", ULONG()),
        ("DomainDfsMinorVersion", ULONG()),
        ("DomainDfsCapabilities", _DFS_NAMESPACE_CAPABILITY_FLAG_()),
        ("StandaloneDfsMajorVersion", ULONG()),
        ("StandaloneDfsMinorVersion", ULONG()),
        ("StandaloneDfsCapabilities", _DFS_NAMESPACE_CAPABILITY_FLAG_()),
    ]

PDFS_SUPPORTED_NAMESPACE_VERSION_INFO = Ptr("<I", DFS_SUPPORTED_NAMESPACE_VERSION_INFO())
PDFS_SUPPORTED_NAMESPACE_VERSION_INFO_PTR = Ptr("<I", PDFS_SUPPORTED_NAMESPACE_VERSION_INFO())

class HLOG(MemStruct):
    fields = [
        ("time", DWORD()),
        ("last_flags", DWORD()),
        ("offset", DWORD()),
        ("rec_offset", DWORD()),
    ]

LPHLOG = Ptr("<I", HLOG())

###################

###### Functions ######

def netapi32_DsAddressToSiteNames(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsAddressToSiteNames(
        LPCTSTR ComputerName,
        DWORD EntryCount,
        PSOCKET_ADDRESS SocketAddresses,
        LPTSTR** SiteNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerName", "EntryCount", "SocketAddresses", "SiteNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsAddressToSiteNamesA(jitter):
    netapi32_DsAddressToSiteNames(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsAddressToSiteNamesW(jitter):
    netapi32_DsAddressToSiteNames(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsAddressToSiteNamesEx(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsAddressToSiteNamesEx(
        LPCTSTR ComputerName,
        DWORD EntryCount,
        PSOCKET_ADDRESS SocketAddresses,
        LPTSTR** SiteNames,
        LPTSTR** SubnetNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerName", "EntryCount", "SocketAddresses", "SiteNames", "SubnetNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsAddressToSiteNamesExA(jitter):
    netapi32_DsAddressToSiteNamesEx(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsAddressToSiteNamesExW(jitter):
    netapi32_DsAddressToSiteNamesEx(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsDeregisterDnsHostRecords(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsDeregisterDnsHostRecords(
        LPTSTR ServerName,
        LPTSTR DnsDomainName,
        GUID* DomainGuid,
        GUID* DsaGuid,
        LPTSTR DnsHostName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "DnsDomainName", "DomainGuid", "DsaGuid", "DnsHostName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsDeregisterDnsHostRecordsA(jitter):
    netapi32_DsDeregisterDnsHostRecords(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsDeregisterDnsHostRecordsW(jitter):
    netapi32_DsDeregisterDnsHostRecords(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsEnumerateDomainTrusts(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsEnumerateDomainTrusts(
        LPTSTR ServerName,
        ULONG Flags,
        PDS_DOMAIN_TRUSTS* Domains,
        PULONG DomainCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Flags", "Domains", "DomainCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsEnumerateDomainTrustsA(jitter):
    netapi32_DsEnumerateDomainTrusts(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsEnumerateDomainTrustsW(jitter):
    netapi32_DsEnumerateDomainTrusts(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetDcCloseW(jitter):
    """
    void DsGetDcCloseW(
        HANDLE GetDcContextHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["GetDcContextHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcName(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDcName(
        LPCTSTR ComputerName,
        LPCTSTR DomainName,
        GUID* DomainGuid,
        LPCTSTR SiteName,
        [DsGetDcNameFlags] Flags,
        PDOMAIN_CONTROLLER_INFO* DomainControllerInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerName", "DomainName", "DomainGuid", "SiteName", "Flags", "DomainControllerInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcNameA(jitter):
    netapi32_DsGetDcName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetDcNameW(jitter):
    netapi32_DsGetDcName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetDcNext(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDcNext(
        HANDLE GetDcContextHandle,
        PULONG SockAddressCount,
        LPSOCKET_ADDRESS* SockAddresses,
        LPTSTR* DnsHostName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["GetDcContextHandle", "SockAddressCount", "SockAddresses", "DnsHostName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcNextA(jitter):
    netapi32_DsGetDcNext(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetDcNextW(jitter):
    netapi32_DsGetDcNext(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetDcOpen(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDcOpen(
        LPCTSTR DnsName,
        ULONG OptionFlags,
        LPCTSTR SiteName,
        GUID* DomainGuid,
        LPCTSTR DnsForestName,
        ULONG DcFlags,
        PHANDLE RetGetDcContext
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DnsName", "OptionFlags", "SiteName", "DomainGuid", "DnsForestName", "DcFlags", "RetGetDcContext"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcOpenA(jitter):
    netapi32_DsGetDcOpen(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetDcOpenW(jitter):
    netapi32_DsGetDcOpen(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetDcSiteCoverage(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetDcSiteCoverage(
        LPCTSTR ServerName,
        PULONG EntryCount,
        LPTSTR** SiteNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "EntryCount", "SiteNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetDcSiteCoverageA(jitter):
    netapi32_DsGetDcSiteCoverage(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetDcSiteCoverageW(jitter):
    netapi32_DsGetDcSiteCoverage(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsGetForestTrustInformationW(jitter):
    """
    [ERROR_CODE] DsGetForestTrustInformationW(
        LPCWSTR ServerName,
        LPCWSTR TrustedDomainName,
        DWORD Flags,
        PLSA_FOREST_TRUST_INFORMATION* ForestTrustInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "TrustedDomainName", "Flags", "ForestTrustInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetSiteName(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsGetSiteName(
        LPCTSTR ComputerName,
        LPTSTR* SiteName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ComputerName", "SiteName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsGetSiteNameA(jitter):
    netapi32_DsGetSiteName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsGetSiteNameW(jitter):
    netapi32_DsGetSiteName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_DsMergeForestTrustInformationW(jitter):
    """
    void DsMergeForestTrustInformationW(
        LPCWSTR DomainName,
        PLSA_FOREST_TRUST_INFORMATION NewForestTrustInfo,
        PLSA_FOREST_TRUST_INFORMATION OldForestTrustInfo,
        PLSA_FOREST_TRUST_INFORMATION* ForestTrustInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainName", "NewForestTrustInfo", "OldForestTrustInfo", "ForestTrustInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsRoleFreeMemory(jitter):
    """
    void DsRoleFreeMemory(
        PVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsRoleGetPrimaryDomainInformation(jitter):
    """
    [ERROR_CODE] DsRoleGetPrimaryDomainInformation(
        LPCWSTR lpServer,
        DSROLE_PRIMARY_DOMAIN_INFO_LEVEL InfoLevel,
        PBYTE* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "InfoLevel", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsValidateSubnetName(jitter, get_str, set_str):
    """
    [ERROR_CODE] DsValidateSubnetName(
        LPCTSTR SubnetName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["SubnetName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DsValidateSubnetNameA(jitter):
    netapi32_DsValidateSubnetName(jitter, lambda addr:get_win_str_a(jitter, addr), lambda addr,value: set_win_str_a(jitter, addr, value))

def netapi32_DsValidateSubnetNameW(jitter):
    netapi32_DsValidateSubnetName(jitter, lambda addr:get_win_str_w(jitter, addr), lambda addr,value: set_win_str_w(jitter, addr, value))

def netapi32_NetAlertRaise(jitter):
    """
    NET_API_STATUS NetAlertRaise(
        LPCWSTR AlertEventName,
        LPVOID Buffer,
        DWORD BufferSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AlertEventName", "Buffer", "BufferSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAlertRaiseEx(jitter):
    """
    NET_API_STATUS NetAlertRaiseEx(
        LPCWSTR AlertEventName,
        LPVOID VariableInfo,
        DWORD VariableInfoSize,
        LPCWSTR ServiceName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["AlertEventName", "VariableInfo", "VariableInfoSize", "ServiceName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetapipBufferAllocate(jitter):
    """
    NET_API_STATUS NetapipBufferAllocate(
        DWORD ByteCount,
        LPVOID* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ByteCount", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetApiBufferAllocate(jitter):
    """
    NET_API_STATUS NetApiBufferAllocate(
        DWORD ByteCount,
        LPVOID* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ByteCount", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetApiBufferFree(jitter):
    """
    NET_API_STATUS NetApiBufferFree(
        LPVOID Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetApiBufferReallocate(jitter):
    """
    NET_API_STATUS NetApiBufferReallocate(
        LPVOID OldBuffer,
        DWORD NewByteCount,
        LPVOID* NewBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OldBuffer", "NewByteCount", "NewBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetApiBufferSize(jitter):
    """
    NET_API_STATUS NetApiBufferSize(
        LPVOID Buffer,
        LPDWORD ByteCount
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Buffer", "ByteCount"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAddAlternateComputerName(jitter):
    """
    NET_API_STATUS NetAddAlternateComputerName(
        LPCWSTR Server,
        LPCWSTR AlternateName,
        LPCWSTR DomainAccount,
        LPCWSTR DomainAccountPassword,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Server", "AlternateName", "DomainAccount", "DomainAccountPassword", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetEnumerateComputerNames(jitter):
    """
    NET_API_STATUS NetEnumerateComputerNames(
        LPCWSTR Server,
        NET_COMPUTER_NAME_TYPE NameType,
        ULONG Reserved,
        PDWORD EntryCount,
        LPWSTR** ComputerNames
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Server", "NameType", "Reserved", "EntryCount", "ComputerNames"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetJoinableOUs(jitter):
    """
    NET_API_STATUS NetGetJoinableOUs(
        LPCWSTR lpServer,
        LPCWSTR lpDomain,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        DWORD* OUCount,
        LPWSTR** OUs
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpDomain", "lpAccount", "lpPassword", "OUCount", "OUs"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetJoinInformation(jitter):
    """
    NET_API_STATUS NetGetJoinInformation(
        LPCWSTR lpServer,
        LPWSTR* lpNameBuffer,
        PNETSETUP_JOIN_STATUS BufferType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpNameBuffer", "BufferType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetJoinDomain(jitter):
    """
    NET_API_STATUS NetJoinDomain(
        LPCWSTR lpServer,
        LPCWSTR lpDomain,
        LPCWSTR lpAccountOU,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        DWORD fJoinOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpDomain", "lpAccountOU", "lpAccount", "lpPassword", "fJoinOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLogonSetServiceBits(jitter):
    """
    NET_API_STATUS NetLogonSetServiceBits(
        LPWSTR ServerName,
        DWORD ServiceBitsOfInterest,
        DWORD ServiceBits
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "ServiceBitsOfInterest", "ServiceBits"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetProvisionComputerAccount(jitter):
    """
    NET_API_STATUS NetProvisionComputerAccount(
        LPCWSTR lpDomain,
        LPCWSTR lpMachineName,
        LPCWSTR lpMachineAccountOU,
        LPCWSTR lpDcName,
        [NETSETUP_PROVISION_OPTIONS] dwOptions,
        PBYTE pProvisionBinData,
        DWORD pdwProvisionBinDataSize,
        LPWSTR pProvisionTextData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpDomain", "lpMachineName", "lpMachineAccountOU", "lpDcName", "dwOptions", "pProvisionBinData", "pdwProvisionBinDataSize", "pProvisionTextData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRemoveAlternateComputerName(jitter):
    """
    NET_API_STATUS NetRemoveAlternateComputerName(
        LPCWSTR Server,
        LPCWSTR AlternateName,
        LPCWSTR DomainAccount,
        LPCWSTR DomainAccountPassword,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Server", "AlternateName", "DomainAccount", "DomainAccountPassword", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRenameMachineInDomain(jitter):
    """
    NET_API_STATUS NetRenameMachineInDomain(
        LPCWSTR lpServer,
        LPCWSTR lpNewMachineName,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        DWORD fRenameOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpNewMachineName", "lpAccount", "lpPassword", "fRenameOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRequestOfflineDomainJoin(jitter):
    """
    NET_API_STATUS NetRequestOfflineDomainJoin(
        BYTE* pProvisionBinData,
        DWORD cbProvisionBinDataSize,
        DWORD dwOptions,
        LPCWSTR lpWindowsPath
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProvisionBinData", "cbProvisionBinDataSize", "dwOptions", "lpWindowsPath"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetSetPrimaryComputerName(jitter):
    """
    NET_API_STATUS NetSetPrimaryComputerName(
        LPCWSTR Server,
        LPCWSTR PrimaryName,
        LPCWSTR DomainAccount,
        LPCWSTR DomainAccountPassword,
        ULONG Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Server", "PrimaryName", "DomainAccount", "DomainAccountPassword", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUnjoinDomain(jitter):
    """
    NET_API_STATUS NetUnjoinDomain(
        LPCWSTR lpServer,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        DWORD fUnjoinOptions
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpAccount", "lpPassword", "fUnjoinOptions"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetValidateName(jitter):
    """
    NET_API_STATUS NetValidateName(
        LPCWSTR lpServer,
        LPCWSTR lpName,
        LPCWSTR lpAccount,
        LPCWSTR lpPassword,
        NETSETUP_NAME_TYPE NameType
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["lpServer", "lpName", "lpAccount", "lpPassword", "NameType"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetCreateProvisioningPackage(jitter):
    """
    NET_API_STATUS NetCreateProvisioningPackage(
        PNETSETUP_PROVISIONING_PARAMS pProvisioningParams,
        PBYTE* pPackageBinData,
        DWORD* pdwPackageBinDataSize,
        LPWSTR* pPackageTextData
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pProvisioningParams", "pPackageBinData", "pdwPackageBinDataSize", "pPackageTextData"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRequestProvisioningPackageInstall(jitter):
    """
    NET_API_STATUS NetRequestProvisioningPackageInstall(
        BYTE* pPackageBinData,
        DWORD dwPackageBinDataSize,
        DWORD dwProvisionOptions,
        LPCWSTR lpWindowsPath,
        PVOID pvReserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pPackageBinData", "dwPackageBinDataSize", "dwProvisionOptions", "lpWindowsPath", "pvReserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetAnyDCName(jitter):
    """
    NET_API_STATUS NetGetAnyDCName(
        LPCWSTR servername,
        LPCWSTR domainname,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "domainname", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetDCName(jitter):
    """
    NET_API_STATUS NetGetDCName(
        LPCWSTR servername,
        LPCWSTR domainname,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "domainname", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGetDisplayInformationIndex(jitter):
    """
    NET_API_STATUS NetGetDisplayInformationIndex(
        LPCWSTR ServerName,
        DWORD Level,
        LPCWSTR Prefix,
        LPDWORD Index
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Level", "Prefix", "Index"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetQueryDisplayInformation(jitter):
    """
    NET_API_STATUS NetQueryDisplayInformation(
        LPCWSTR ServerName,
        DWORD Level,
        DWORD Index,
        DWORD EntriesRequested,
        DWORD PreferredMaximumLength,
        LPDWORD ReturnedEntryCount,
        PVOID* SortedBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Level", "Index", "EntriesRequested", "PreferredMaximumLength", "ReturnedEntryCount", "SortedBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupAdd(jitter):
    """
    NET_API_STATUS NetGroupAdd(
        LPCWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupAddUser(jitter):
    """
    NET_API_STATUS NetGroupAddUser(
        LPCWSTR servername,
        LPCWSTR GroupName,
        LPCWSTR username
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "GroupName", "username"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupDel(jitter):
    """
    NET_API_STATUS NetGroupDel(
        LPCWSTR servername,
        LPCWSTR groupname
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupDelUser(jitter):
    """
    NET_API_STATUS NetGroupDelUser(
        LPCWSTR servername,
        LPCWSTR GroupName,
        LPCWSTR Username
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "GroupName", "Username"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupEnum(jitter):
    """
    NET_API_STATUS NetGroupEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupGetInfo(jitter):
    """
    NET_API_STATUS NetGroupGetInfo(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupGetUsers(jitter):
    """
    NET_API_STATUS NetGroupGetUsers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR ResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "ResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupSetInfo(jitter):
    """
    NET_API_STATUS NetGroupSetInfo(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetGroupSetUsers(jitter):
    """
    NET_API_STATUS NetGroupSetUsers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        DWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupAdd(jitter):
    """
    NET_API_STATUS NetLocalGroupAdd(
        LPCWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupAddMembers(jitter):
    """
    NET_API_STATUS NetLocalGroupAddMembers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        DWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupDel(jitter):
    """
    NET_API_STATUS NetLocalGroupDel(
        LPCWSTR servername,
        LPCWSTR groupname
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupDelMembers(jitter):
    """
    NET_API_STATUS NetLocalGroupDelMembers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        DWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupEnum(jitter):
    """
    NET_API_STATUS NetLocalGroupEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupGetInfo(jitter):
    """
    NET_API_STATUS NetLocalGroupGetInfo(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupGetMembers(jitter):
    """
    NET_API_STATUS NetLocalGroupGetMembers(
        LPCWSTR servername,
        LPCWSTR localgroupname,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "localgroupname", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupSetInfo(jitter):
    """
    NET_API_STATUS NetLocalGroupSetInfo(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupSetMembers(jitter):
    """
    NET_API_STATUS NetLocalGroupSetMembers(
        LPCWSTR servername,
        LPCWSTR groupname,
        DWORD level,
        LPBYTE buf,
        DWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "level", "buf", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageBufferSend(jitter):
    """
    NET_API_STATUS NetMessageBufferSend(
        LPCWSTR servername,
        LPCWSTR msgname,
        LPCWSTR fromname,
        LPBYTE buf,
        DWORD buflen
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "msgname", "fromname", "buf", "buflen"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageNameAdd(jitter):
    """
    NET_API_STATUS NetMessageNameAdd(
        LPCWSTR servername,
        LPCWSTR msgname
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "msgname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageNameDel(jitter):
    """
    NET_API_STATUS NetMessageNameDel(
        LPCWSTR servername,
        LPCWSTR msgname
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "msgname"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageNameEnum(jitter):
    """
    NET_API_STATUS NetMessageNameEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetMessageNameGetInfo(jitter):
    """
    NET_API_STATUS NetMessageNameGetInfo(
        LPCWSTR servername,
        LPCWSTR msgname,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "msgname", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRemoteComputerSupports(jitter):
    """
    NET_API_STATUS NetRemoteComputerSupports(
        LPCWSTR UncServerName,
        DWORD OptionsWanted,
        LPDWORD OptionsSupported
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "OptionsWanted", "OptionsSupported"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRemoteTOD(jitter):
    """
    NET_API_STATUS NetRemoteTOD(
        LPCWSTR UncServerName,
        LPBYTE* BufferPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "BufferPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetScheduleJobAdd(jitter):
    """
    NET_API_STATUS NetScheduleJobAdd(
        LPCWSTR Servername,
        LPBYTE Buffer,
        LPDWORD JobId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Servername", "Buffer", "JobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetScheduleJobDel(jitter):
    """
    NET_API_STATUS NetScheduleJobDel(
        LPCWSTR Servername,
        DWORD MinJobId,
        DWORD MaxJobId
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Servername", "MinJobId", "MaxJobId"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetScheduleJobEnum(jitter):
    """
    NET_API_STATUS NetScheduleJobEnum(
        LPCWSTR Servername,
        LPBYTE* PointerToBuffer,
        DWORD PreferredMaximumLength,
        LPDWORD EntriesRead,
        LPDWORD TotalEntries,
        LPDWORD ResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Servername", "PointerToBuffer", "PreferredMaximumLength", "EntriesRead", "TotalEntries", "ResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetScheduleJobGetInfo(jitter):
    """
    NET_API_STATUS NetScheduleJobGetInfo(
        LPCWSTR Servername,
        DWORD JobId,
        LPBYTE* PointerToBuffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Servername", "JobId", "PointerToBuffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerDiskEnum(jitter):
    """
    NET_API_STATUS NetServerDiskEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerEnum(jitter):
    """
    NET_API_STATUS NetServerEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        [ServerType] servertype,
        LPCWSTR domain,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "servertype", "domain", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerEnumEx(jitter):
    """
    NET_API_STATUS NetServerEnumEx(
        LPCWSTR ServerName,
        DWORD Level,
        LPBYTE* Bufptr,
        DWORD PrefMaxlen,
        LPDWORD EntriesRead,
        LPDWORD totalentries,
        [ServerType] servertype,
        LPCWSTR domain,
        LPCWSTR FirstNameToReturn
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Level", "Bufptr", "PrefMaxlen", "EntriesRead", "totalentries", "servertype", "domain", "FirstNameToReturn"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerGetInfo(jitter):
    """
    NET_API_STATUS NetServerGetInfo(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerSetInfo(jitter):
    """
    NET_API_STATUS NetServerSetInfo(
        LPWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD ParmError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "ParmError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerSetInfoCommandLine(jitter):
    """
    NET_API_STATUS NetServerSetInfoCommandLine(
        WORD argc,
        LMSTR [] argv
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["argc", "argv"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerComputerNameAdd(jitter):
    """
    NET_API_STATUS NetServerComputerNameAdd(
        LPWSTR ServerName,
        LPWSTR EmulatedDomainName,
        LPWSTR EmulatedServerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "EmulatedDomainName", "EmulatedServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerComputerNameDel(jitter):
    """
    NET_API_STATUS NetServerComputerNameDel(
        LPWSTR ServerName,
        LPWSTR EmulatedServerName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "EmulatedServerName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerTransportAdd(jitter):
    """
    NET_API_STATUS NetServerTransportAdd(
        LPWSTR servername,
        DWORD level,
        LPBYTE bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerTransportAddEx(jitter):
    """
    NET_API_STATUS NetServerTransportAddEx(
        LPWSTR servername,
        DWORD level,
        LPBYTE bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerTransportDel(jitter):
    """
    NET_API_STATUS NetServerTransportDel(
        LPWSTR servername,
        DWORD level,
        LPBYTE bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerTransportEnum(jitter):
    """
    NET_API_STATUS NetServerTransportEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaTransportEnum(jitter):
    """
    NET_API_STATUS NetWkstaTransportEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUseAdd(jitter):
    """
    NET_API_STATUS NetUseAdd(
        LMSTR UncServerName,
        DWORD Level,
        LPBYTE Buf,
        LPDWORD ParmError
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "Level", "Buf", "ParmError"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUseDel(jitter):
    """
    NET_API_STATUS NetUseDel(
        LMSTR UncServerName,
        LMSTR UseName,
        DWORD ForceCond
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "UseName", "ForceCond"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUseEnum(jitter):
    """
    NET_API_STATUS NetUseEnum(
        LMSTR UncServerName,
        DWORD Level,
        LPBYTE* BufPtr,
        DWORD PreferedMaximumSize,
        LPDWORD EntriesRead,
        LPDWORD TotalEntries,
        LPDWORD ResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "Level", "BufPtr", "PreferedMaximumSize", "EntriesRead", "TotalEntries", "ResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUseGetInfo(jitter):
    """
    NET_API_STATUS NetUseGetInfo(
        LMSTR UncServerName,
        LMSTR UseName,
        DWORD Level,
        LPBYTE* BufPtr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "UseName", "Level", "BufPtr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserAdd(jitter):
    """
    NET_API_STATUS NetUserAdd(
        LMSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserChangePassword(jitter):
    """
    NET_API_STATUS NetUserChangePassword(
        LPCWSTR domainname,
        LPCWSTR username,
        LPCWSTR oldpassword,
        LPCWSTR newpassword
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["domainname", "username", "oldpassword", "newpassword"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserDel(jitter):
    """
    NET_API_STATUS NetUserDel(
        LPCWSTR servername,
        LPCWSTR username
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserEnum(jitter):
    """
    NET_API_STATUS NetUserEnum(
        LPCWSTR servername,
        DWORD level,
        DWORD filter,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "filter", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserGetGroups(jitter):
    """
    NET_API_STATUS NetUserGetGroups(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserGetInfo(jitter):
    """
    NET_API_STATUS NetUserGetInfo(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserGetLocalGroups(jitter):
    """
    NET_API_STATUS NetUserGetLocalGroups(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        [NetUserGetLocalGroupsFlags] flags,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "flags", "bufptr", "prefmaxlen", "entriesread", "totalentries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserSetGroups(jitter):
    """
    NET_API_STATUS NetUserSetGroups(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        LPBYTE buf,
        DWORD num_entries
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "buf", "num_entries"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserSetInfo(jitter):
    """
    NET_API_STATUS NetUserSetInfo(
        LPCWSTR servername,
        LPCWSTR username,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "username", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserModalsGet(jitter):
    """
    NET_API_STATUS NetUserModalsGet(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetUserModalsSet(jitter):
    """
    NET_API_STATUS NetUserModalsSet(
        LPCWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetValidatePasswordPolicyFree(jitter):
    """
    NET_API_STATUS NetValidatePasswordPolicyFree(
        LPVOID* OutputArg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["OutputArg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetValidatePasswordPolicy(jitter):
    """
    NET_API_STATUS NetValidatePasswordPolicy(
        LPCWSTR ServerName,
        LPVOID Qualifier,
        NET_VALIDATE_PASSWORD_TYPE ValidationType,
        LPVOID InputArg,
        LPVOID OutputArg
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Qualifier", "ValidationType", "InputArg", "OutputArg"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaGetInfo(jitter):
    """
    NET_API_STATUS NetWkstaGetInfo(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaSetInfo(jitter):
    """
    NET_API_STATUS NetWkstaSetInfo(
        LPWSTR servername,
        DWORD level,
        LPBYTE buffer,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buffer", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaUserEnum(jitter):
    """
    NET_API_STATUS NetWkstaUserEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaUserGetInfo(jitter):
    """
    NET_API_STATUS NetWkstaUserGetInfo(
        LPWSTR reserved,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaUserSetInfo(jitter):
    """
    NET_API_STATUS NetWkstaUserSetInfo(
        LPWSTR reserved,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAddServiceAccount(jitter):
    """
    NTSTATUS NetAddServiceAccount(
        LPWSTR ServerName,
        LPWSTR AccountName,
        LPWSTR Reserved,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "AccountName", "Reserved", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetEnumerateServiceAccounts(jitter):
    """
    NTSTATUS NetEnumerateServiceAccounts(
        LPWSTR ServerName,
        DWORD Flags,
        DWORD* AccountsCount,
        PZPWSTR* Accounts
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Flags", "AccountsCount", "Accounts"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetIsServiceAccount(jitter):
    """
    NTSTATUS NetIsServiceAccount(
        LPWSTR ServerName,
        LPWSTR AccountName,
        BOOL* IsService
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "AccountName", "IsService"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetRemoveServiceAccount(jitter):
    """
    NTSTATUS NetRemoveServiceAccount(
        LPWSTR ServerName,
        LPWSTR AccountName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "AccountName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavAddConnection(jitter):
    """
    [ERROR_CODE] DavAddConnection(
        HANDLE* ConnectionHandle,
        LPCWSTR RemoteName,
        LPCWSTR UserName,
        LPCWSTR Password,
        PBYTE ClientCert,
        DWORD CertSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle", "RemoteName", "UserName", "Password", "ClientCert", "CertSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavDeleteConnection(jitter):
    """
    [ERROR_CODE] DavDeleteConnection(
        HANDLE ConnectionHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ConnectionHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavFlushFile(jitter):
    """
    [ERROR_CODE] DavFlushFile(
        HANDLE hFile
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavGetExtendedError(jitter):
    """
    [ERROR_CODE] DavGetExtendedError(
        HANDLE hFile,
        DWORD* ExtError,
        LPWSTR ExtErrorString,
        DWORD* cChSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["hFile", "ExtError", "ExtErrorString", "cChSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavGetHTTPFromUNCPath(jitter):
    """
    [ERROR_CODE] DavGetHTTPFromUNCPath(
        LPCWSTR UncPath,
        LPWSTR HttpPath,
        LPDWORD lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncPath", "HttpPath", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_DavGetUNCFromHTTPPath(jitter):
    """
    [ERROR_CODE] DavGetUNCFromHTTPPath(
        LPCWSTR HttpPath,
        LPWSTR UncPath,
        LPDWORD lpSize
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["HttpPath", "UncPath", "lpSize"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetFileClose(jitter):
    """
    NET_API_STATUS NetFileClose(
        LMSTR servername,
        DWORD fileid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "fileid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetFileEnum(jitter):
    """
    NET_API_STATUS NetFileEnum(
        LMSTR servername,
        LMSTR basepath,
        LMSTR username,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        PDWORD_PTR resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "basepath", "username", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetFileGetInfo(jitter):
    """
    NET_API_STATUS NetFileGetInfo(
        LMSTR servername,
        DWORD fileid,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "fileid", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetSessionDel(jitter):
    """
    NET_API_STATUS NetSessionDel(
        LPWSTR servername,
        LPWSTR UncClientName,
        LPWSTR username
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "UncClientName", "username"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetSessionEnum(jitter):
    """
    NET_API_STATUS NetSessionEnum(
        LPWSTR servername,
        LPWSTR UncClientName,
        LPWSTR username,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "UncClientName", "username", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetSessionGetInfo(jitter):
    """
    NET_API_STATUS NetSessionGetInfo(
        LPWSTR servername,
        LPWSTR UncClientName,
        LPWSTR username,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "UncClientName", "username", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetConnectionEnum(jitter):
    """
    NET_API_STATUS NetConnectionEnum(
        LMSTR servername,
        LMSTR qualifier,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "qualifier", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareAdd(jitter):
    """
    NET_API_STATUS NetShareAdd(
        LPWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareCheck(jitter):
    """
    NET_API_STATUS NetShareCheck(
        LPWSTR servername,
        LPWSTR device,
        LPDWORD type
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "device", "type"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareDel(jitter):
    """
    NET_API_STATUS NetShareDel(
        LMSTR servername,
        LMSTR netname,
        DWORD reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "netname", "reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareDelSticky(jitter):
    """
    NET_API_STATUS NetShareDelSticky(
        LMSTR servername,
        LMSTR netname,
        DWORD reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "netname", "reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareDelEx(jitter):
    """
    NET_API_STATUS NetShareDelEx(
        LMSTR servername,
        DWORD level,
        LPBYTE buf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareEnum(jitter):
    """
    NET_API_STATUS NetShareEnum(
        LPWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareEnumSticky(jitter):
    """
    NET_API_STATUS NetShareEnumSticky(
        LMSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareGetInfo(jitter):
    """
    NET_API_STATUS NetShareGetInfo(
        LPWSTR servername,
        LPWSTR netname,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "netname", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetShareSetInfo(jitter):
    """
    NET_API_STATUS NetShareSetInfo(
        LPWSTR servername,
        LPWSTR netname,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "netname", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetStatisticsGet(jitter):
    """
    NET_API_STATUS NetStatisticsGet(
        LPWSTR server,
        LPWSTR service,
        DWORD level,
        DWORD options,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "service", "level", "options", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessAdd(jitter):
    """
    NET_API_STATUS NetAccessAdd(
        LPCWSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessCheck(jitter):
    """
    NET_API_STATUS NetAccessCheck(
        LPCWSTR reserved,
        LPCWSTR userName,
        LPCWSTR resource,
        DWORD operation,
        LPDWORD result
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["reserved", "userName", "resource", "operation", "result"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessDel(jitter):
    """
    NET_API_STATUS NetAccessDel(
        LPCWSTR servername,
        LPCWSTR resource
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "resource"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessEnum(jitter):
    """
    NET_API_STATUS NetAccessEnum(
        LPCWSTR servername,
        LPCWSTR BasePath,
        DWORD Recursive,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "BasePath", "Recursive", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessGetInfo(jitter):
    """
    NET_API_STATUS NetAccessGetInfo(
        LPCWSTR servername,
        LPCWSTR resource,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "resource", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessGetUserPerms(jitter):
    """
    NET_API_STATUS NetAccessGetUserPerms(
        LPCWSTR servername,
        LPCWSTR UGname,
        LPCWSTR resource,
        LPDWORD Perms
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "UGname", "resource", "Perms"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAccessSetInfo(jitter):
    """
    NET_API_STATUS NetAccessSetInfo(
        LPCWSTR servername,
        LPCWSTR resource,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "resource", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAuditClear(jitter):
    """
    NET_API_STATUS NetAuditClear(
        LPCWSTR server,
        LPCWSTR backupfile,
        LPCWSTR service
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "backupfile", "service"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAuditRead(jitter):
    """
    NET_API_STATUS NetAuditRead(
        LPCWSTR server,
        LPCWSTR service,
        LPHLOG auditloghandle,
        DWORD offset,
        LPDWORD reserved1,
        DWORD reserved2,
        DWORD offsetflag,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD bytesread,
        LPDWORD totalavailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "service", "auditloghandle", "offset", "reserved1", "reserved2", "offsetflag", "bufptr", "prefmaxlen", "bytesread", "totalavailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetAuditWrite(jitter):
    """
    NET_API_STATUS NetAuditWrite(
        DWORD type,
        LPBYTE buf,
        DWORD numbytes,
        LPCWSTR service,
        LPBYTE reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["type", "buf", "numbytes", "service", "reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetConfigGet(jitter):
    """
    NET_API_STATUS NetConfigGet(
        LPCWSTR server,
        LPCWSTR component,
        LPCWSTR parameter,
        LPBYTE* bufptr,
        LPDWORD totalavailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "component", "parameter", "bufptr", "totalavailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetConfigGetAll(jitter):
    """
    NET_API_STATUS NetConfigGetAll(
        LPCWSTR server,
        LPCWSTR component,
        LPBYTE* bufptr,
        LPDWORD totalavailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "component", "bufptr", "totalavailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetConfigSet(jitter):
    """
    NET_API_STATUS NetConfigSet(
        LPCWSTR server,
        LPCWSTR reserved1,
        LPCWSTR component,
        DWORD level,
        DWORD reserved2,
        LPBYTE buf,
        DWORD reserved3
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["server", "reserved1", "component", "level", "reserved2", "buf", "reserved3"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetErrorLogClear(jitter):
    """
    NET_API_STATUS NetErrorLogClear(
        LPCWSTR UncServerName,
        LPCWSTR BackupFile,
        LPBYTE Reserved
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "BackupFile", "Reserved"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetErrorLogRead(jitter):
    """
    NET_API_STATUS NetErrorLogRead(
        LPCWSTR UncServerName,
        LPWSTR Reserved1,
        LPHLOG ErrorLogHandle,
        DWORD Offset,
        LPDWORD Reserved2,
        DWORD Reserved3,
        DWORD OffsetFlag,
        LPBYTE* BufPtr,
        DWORD PrefMaxSize,
        LPDWORD BytesRead,
        LPDWORD TotalAvailable
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["UncServerName", "Reserved1", "ErrorLogHandle", "Offset", "Reserved2", "Reserved3", "OffsetFlag", "BufPtr", "PrefMaxSize", "BytesRead", "TotalAvailable"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetErrorLogWrite(jitter):
    """
    NET_API_STATUS NetErrorLogWrite(
        LPBYTE Reserved1,
        DWORD Code,
        LPCWSTR Component,
        LPBYTE Buffer,
        DWORD NumBytes,
        LPBYTE MsgBuf,
        DWORD StrCount,
        LPBYTE Reserved2
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Reserved1", "Code", "Component", "Buffer", "NumBytes", "MsgBuf", "StrCount", "Reserved2"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupAddMember(jitter):
    """
    NET_API_STATUS NetLocalGroupAddMember(
        LPCWSTR servername,
        LPCWSTR groupname,
        PSID membersid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "membersid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetLocalGroupDelMember(jitter):
    """
    NET_API_STATUS NetLocalGroupDelMember(
        LPCWSTR servername,
        LPCWSTR groupname,
        PSID membersid
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "groupname", "membersid"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServiceControl(jitter):
    """
    NET_API_STATUS NetServiceControl(
        LPCWSTR servername,
        LPCWSTR service,
        DWORD opcode,
        DWORD arg,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "service", "opcode", "arg", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServiceEnum(jitter):
    """
    NET_API_STATUS NetServiceEnum(
        LPCWSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resume_handle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resume_handle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServiceGetInfo(jitter):
    """
    NET_API_STATUS NetServiceGetInfo(
        LPCWSTR servername,
        LPCWSTR service,
        DWORD level,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "service", "level", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServiceInstall(jitter):
    """
    NET_API_STATUS NetServiceInstall(
        LPCWSTR servername,
        LPCWSTR service,
        DWORD argc,
        LPCWSTR [] argv,
        LPBYTE* bufptr
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "service", "argc", "argv", "bufptr"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaTransportAdd(jitter):
    """
    NET_API_STATUS NetWkstaTransportAdd(
        LMSTR servername,
        DWORD level,
        LPBYTE buf,
        LPDWORD parm_err
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf", "parm_err"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetWkstaTransportDel(jitter):
    """
    NET_API_STATUS NetWkstaTransportDel(
        LMSTR servername,
        LMSTR transportname,
        DWORD ucond
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "transportname", "ucond"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAdd(jitter):
    """
    NET_API_STATUS NetDfsAdd(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR PathName,
        LPWSTR Comment,
        [DFS_FLAG] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "PathName", "Comment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAddFtRoot(jitter):
    """
    NET_API_STATUS NetDfsAddFtRoot(
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR FtDfsName,
        LPWSTR Comment,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "FtDfsName", "Comment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAddRootTarget(jitter):
    """
    NET_API_STATUS NetDfsAddRootTarget(
        LPWSTR pDfsPath,
        LPWSTR pTargetPath,
        ULONG MajorVersion,
        LPWSTR pComment,
        ULONG Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDfsPath", "pTargetPath", "MajorVersion", "pComment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAddStdRoot(jitter):
    """
    NET_API_STATUS NetDfsAddStdRoot(
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR Comment,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "Comment", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsAddStdRootForced(jitter):
    """
    NET_API_STATUS NetDfsAddStdRootForced(
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR Comment,
        LPWSTR Store
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "Comment", "Store"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsEnum(jitter):
    """
    NET_API_STATUS NetDfsEnum(
        LPWSTR DfsName,
        DWORD Level,
        DWORD PrefMaxLen,
        LPBYTE* Buffer,
        LPDWORD EntriesRead,
        LPDWORD ResumeHandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsName", "Level", "PrefMaxLen", "Buffer", "EntriesRead", "ResumeHandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetClientInfo(jitter):
    """
    NET_API_STATUS NetDfsGetClientInfo(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName,
        DWORD Level,
        LPBYTE* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName", "Level", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetFtContainerSecurity(jitter):
    """
    NET_API_STATUS NetDfsGetFtContainerSecurity(
        LPWSTR DomainName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR* ppSecurityDescriptor,
        LPDWORD lpcbSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainName", "SecurityInformation", "ppSecurityDescriptor", "lpcbSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetInfo(jitter):
    """
    NET_API_STATUS NetDfsGetInfo(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName,
        DWORD Level,
        LPBYTE* Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName", "Level", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetSecurity(jitter):
    """
    NET_API_STATUS NetDfsGetSecurity(
        LPWSTR DfsEntryPath,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR* ppSecurityDescriptor,
        LPDWORD lpcbSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "SecurityInformation", "ppSecurityDescriptor", "lpcbSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetStdContainerSecurity(jitter):
    """
    NET_API_STATUS NetDfsGetStdContainerSecurity(
        LPWSTR MachineName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR* ppSecurityDescriptor,
        LPDWORD lpcbSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MachineName", "SecurityInformation", "ppSecurityDescriptor", "lpcbSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsGetSupportedNamespaceVersion(jitter):
    """
    NET_API_STATUS NetDfsGetSupportedNamespaceVersion(
        DFS_NAMESPACE_VERSION_ORIGIN Origin,
        PWSTR pName,
        PDFS_SUPPORTED_NAMESPACE_VERSION_INFO* ppVersionInfo
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Origin", "pName", "ppVersionInfo"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsManagerInitialize(jitter):
    """
    NET_API_STATUS NetDfsManagerInitialize(
        LPWSTR ServerName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsMove(jitter):
    """
    NET_API_STATUS NetDfsMove(
        LPWSTR Path,
        LPWSTR NewPath,
        [DFS_MOVE_FLAG] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["Path", "NewPath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemove(jitter):
    """
    NET_API_STATUS NetDfsRemove(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemoveFtRoot(jitter):
    """
    NET_API_STATUS NetDfsRemoveFtRoot(
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR FtDfsName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "FtDfsName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemoveFtRootForced(jitter):
    """
    NET_API_STATUS NetDfsRemoveFtRootForced(
        LPWSTR DomainName,
        LPWSTR ServerName,
        LPWSTR RootShare,
        LPWSTR FtDfsName,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainName", "ServerName", "RootShare", "FtDfsName", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemoveRootTarget(jitter):
    """
    NET_API_STATUS NetDfsRemoveRootTarget(
        LPWSTR pDfsPath,
        LPWSTR pTargetPath,
        [DFS_REMOVE_FLAG] Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["pDfsPath", "pTargetPath", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsRemoveStdRoot(jitter):
    """
    NET_API_STATUS NetDfsRemoveStdRoot(
        LPWSTR ServerName,
        LPWSTR RootShare,
        DWORD Flags
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["ServerName", "RootShare", "Flags"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetClientInfo(jitter):
    """
    NET_API_STATUS NetDfsSetClientInfo(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName,
        DWORD Level,
        LPBYTE Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName", "Level", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetFtContainerSecurity(jitter):
    """
    NET_API_STATUS NetDfsSetFtContainerSecurity(
        LPWSTR DomainName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DomainName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetInfo(jitter):
    """
    NET_API_STATUS NetDfsSetInfo(
        LPWSTR DfsEntryPath,
        LPWSTR ServerName,
        LPWSTR ShareName,
        DWORD Level,
        LPBYTE Buffer
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "ServerName", "ShareName", "Level", "Buffer"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetSecurity(jitter):
    """
    NET_API_STATUS NetDfsSetSecurity(
        LPWSTR DfsEntryPath,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["DfsEntryPath", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetDfsSetStdContainerSecurity(jitter):
    """
    NET_API_STATUS NetDfsSetStdContainerSecurity(
        LPWSTR MachineName,
        SECURITY_INFORMATION SecurityInformation,
        PSECURITY_DESCRIPTOR pSecurityDescriptor
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["MachineName", "SecurityInformation", "pSecurityDescriptor"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerAliasAdd(jitter):
    """
    NET_API_STATUS NetServerAliasAdd(
        LMSTR servername,
        DWORD level,
        LPBYTE buf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerAliasDel(jitter):
    """
    NET_API_STATUS NetServerAliasDel(
        LMSTR servername,
        DWORD level,
        LPBYTE buf
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "buf"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)

def netapi32_NetServerAliasEnum(jitter):
    """
    NET_API_STATUS NetServerAliasEnum(
        LMSTR servername,
        DWORD level,
        LPBYTE* bufptr,
        DWORD prefmaxlen,
        LPDWORD entriesread,
        LPDWORD totalentries,
        LPDWORD resumehandle
    )
    """
    ret_ad, args = jitter.func_args_stdcall(["servername", "level", "bufptr", "prefmaxlen", "entriesread", "totalentries", "resumehandle"])
    raise RuntimeError('API not implemented')
    jitter.func_ret_stdcall(ret_ad, ret_value)
