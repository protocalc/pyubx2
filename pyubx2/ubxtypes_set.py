# pylint: disable=unused-import
'''
UBX Protocol Input payload definitions

THESE ARE THE PAYLOAD DEFINITIONS FOR _SET_ MESSAGES _TO_ THE RECEIVER

NB: Attribute names must be unique within each message class/id

NB: Repeating groups must be defined as a tuple thus:
    'group': ('numr', {dict})
    where
    - 'numr' is the name of the preceding attribute containing the number
       of repeats, or 'None' if there isn't one
    - {dict} is the nested dictionary containing the repeating attributes

Created on 27 Sep 2020

@author: semuadmin
'''
# pylint: disable=unused-import, too-many-lines, line-too-long

from pyubx2.ubxtypes_core import U1, I1, X1, U2, I2, X2, U3, U4, I4, U5, \
                                 X4, R4, U6, U40, U64, X6, R8, C2, C6, C10, \
                                 C30, C32, CH

UBX_PAYLOADS_SET = {
# AssistNow Aiding Messages: i.e. Ephemeris, Almanac, other A-GPS data input.
# Messages in the AID class are used to send GPS aiding data to the receiver
# AID messages are deprecated in favour of MGA messages in >=Gen8
'AID-ALM': {
'svid': U4,
'week': U4,
'optBlock': ('None', {
'dwrd': U4
})},
'AID-AOP' : {
'gnssId': U1,
'svId': U1,
'reserved1': U2,
'data': U64
},
'AID-EPH' : {
'svid': U1,
'how': U4,
'optBlock': ('None', {
'sf1d1': U4,
'sf1d2': U4,
'sf1d3': U4,
'sf1d4': U4,
'sf1d5': U4,
'sf1d6': U4,
'sf1d7': U4,
'sf1d8': U4,
'sf2d1': U4,
'sf2d2': U4,
'sf2d3': U4,
'sf2d4': U4,
'sf2d5': U4,
'sf2d6': U4,
'sf2d7': U4,
'sf2d8': U4,
'sf3d1': U4,
'sf3d2': U4,
'sf3d3': U4,
'sf3d4': U4,
'sf3d5': U4,
'sf3d6': U4,
'sf3d7': U4,
'sf3d8': U4,
})},
'AID-HUI': {
'health': X4,
'utcA0': R8,
'utcA1': R8,
'utcTOW': I4,
'utcWNT': I2,
'utcLS': I2,
'utcWNF': I2,
'utcDNs': I2,
'utcLSF': I2,
'utcSpare': I2,
'klobA0': R4,
'klobA1': R4,
'klobA2': R4,
'klobA3': R4,
'klobB0': R4,
'klobB1': R4,
'klobB2': R4,
'klobB3': R4,
'flags': X4
},
'AID-INI': {
'ecefXOrLat': I4,
'ecefYOrLon': I4,
'ecefZOrAlt': I4,
'posAcc': U4,
'tmCfg': X2,
'wn': U2,
'tow': U4,
'towNs': I4,
'tAccMs': U4,
'tAccNs': U4,
'clkDOrFreq': I4,
'clkDAccOrFreqAcc': U4,
'flags': X4
},
# ********************************************************************
# Configuration Input Messages: i.e. Set Dynamic Model, Set DOP Mask, Set Baud Rate, etc..
# Messages in the CFG class are used to configure the receiver and read out current configuration values. Any
# messages in the CFG class sent to the receiver are either acknowledged (with message UBX-ACK-ACK) if
# processed successfully or rejected (with message UBX-ACK-NAK) if processing unsuccessfully.
'CFG-ANT': {
'flags': X2,
'pins': X2
},
'CFG-CFG': {
'clearMask': X4,
'saveMask' : X4,
'loadMask': X4,
'deviceMask': X1
},
'CFG-DAT':{
'datumNum': U2,
'datumName': C6,
'majA': R8,
'flat': R8,
'dX': R4,
'dY': R4,
'dZ': R4,
'rotX': R4,
'rotY': R4,
'rotZ': R4,
'scale': R4
},
'CFG-DOSC': {
'version': U1,
'numOsc': U1,
'reserved1': U2,
'group': ('numOsc', {  # repeating group * numOsc
'oscId': U1,
'reserved2': U1,
'flags': X2,
'freq': U4,
'phaseOffset': I4,
'withTemp': U4,
'withAge': U4,
'timeToTemp': U2,
'reserved3': U2,
'gainVco': I4,
'gainUncertainty': U1,
'reserved4': U3
})},
'CFG-DYNSEED': {
'version': U1,
'reserved1': U3,
'seedHi': U4,
'seedLo': U4
},
'CFG-ESRC': {
'version': U1,
'numSources': U1,
'reserved1': U2,
'group': ('numSources', {  # repeating group * numSources
'extInt': U1,
'flags': X2,
'freq': U4,
'reserved2': U4,
'withTemp': U4,
'withAge': U4,
'timeToTemp': U2,
'maxDevLifeTim': U2,
'offset': I4,
'offsetUncertainty': U4,
'jitter': U4
})},
'CFG-FIXSEED': {
'version': U1,
'length': U1,
'reserved1': U2,
'seedHi': U4,
'seedLo': U4,
'group': ('length', {  # repeating group * length
'classId': U1,
'msgId': U1
})},
'CFG-GEOFENCE': {
'version': U1,
'numFences': U1,
'confLvl': U1,
'reserved1': U1,
'pioEnabled': U1,
'pinPolarity': U1,
'pin': U1,
'reserved2': U1,
'group': ('numFences', {  # repeating group * numFences
'lat': I4,
'lon': I4,
'radius': U4
})},
'CFG-GNSS': {
'msgVer': U1,
'numTrkChHw': U1,
'numTrkChUse': U1,
'numConfigBlocks': U1,
'group': ('numConfigBlocks', {  # repeating group * numConfigBlocks
'gnssId': U1,
'resTrkCh': U1,
'maxTrkCh': U1,
'reserved1': U1,
'flags': X4
})},
'CFG-INF': {
'protocolID': U1,
'reserved1': U3,
'infMsgMaskDDC': X1,
'infMsgMaskUART1': X1,
'infMsgMaskUART2': X1,
'infMsgMaskUSB': X1,
'infMsgMaskSPI': X1,
'reserved2': X1
},
'CFG-ITFM': {
'config': X4,
'config2': X4
},
'CFG-LOGFILTER': {
'version': U1,
'flags': X1,
'minInterval': U2,
'timeThreshold': U2,
'speedThreshold': U2,
'positionThreshold': U4
},
'CFG-MSG': {
'msgClass': U1,
'msgID': U1,
'rateDDC': U1,
'rateUART1': U1,
'rateUART2': U1,
'rateUSB': U1,
'rateSPI': U1,
'reserved': U1
},
'CFG-NAV5': {
'mask': X2,
'dynModel': U1,
'fixMode': U1,
'fixedAlt': I4,
'fixedAltVar': U4,
'minElev': I1,
'drLimit': U1,
'pDop': U2,
'tDop': U2,
'pAcc': U2,
'tAcc': U2,
'staticHoldThresh': U1,
'dgpsTimeOut': U1,
'reserved2': U4,
'reserved3': U4,
'reserved4': U4
},
'CFG-NAVX5': {
'mask1': X2,
'reserved0': U4,
'reserved1': U1,
'reserved2': U1,
'minSVs': U1,
'maxSVs': U1,
'minCNO': U1,
'reserved5': U1,
'iniFix3D': U1,
'reserved6': U1,
'reserved7': U1,
'reserved8': U1,
'wknRollover': U2,
'reserved9': U1,
'reserved10': U1,
'reserved11': U1,
'usePPP': U1,
'useAOP': U1,
'reserved12': U1,
'reserved13': U1,
'aopOrbMaxErr': U2,
'reserved3': U4,
'reserved4': U4
},
'CFG-NMEAvX': {  # deprecated length 4
'filter': X1,
'nmeaVersion': U1,
'numSV': U1,
'flags': X1
},
'CFG-NMEAv0': {  # v0 deprecated length 12
'filter': X1,
'nmeaVersion': U1,
'numSV': U1,
'flags': X1,
'gnssToFilter': X4,
'svNumbering': U1,
'mainTalkerId': U1,
'gsvTalkerId': U1,
'version': U1
},
'CFG-NMEA': {  # preferred version length 20
'filter': X1,
'nmeaVersion': U1,
'numSV': U1,
'flags': X1,
'gnssToFilter': X4,
'svNumbering': U1,
'mainTalkerId': U1,
'gsvTalkerId': U1,
'version': U1,
'bdsTalkerId': C2,
'reserved1': U6
},
'CFG-ODO': {
'version': U1,
'reserved1': U3,
'flags': U1,
'odoCfg': X1,
'reserved2': U6,
'cogMaxSpeed': U1,
'cogMaxPosAcc': U1,
'reserved3': U2,
'velLpGain': U1,
'cogLpGain': U1,
'reserved4': U2
},
'CFG-PM2': {
'version': U1,
'reserved1': U1,
'reserved2': U1,
'reserved3': U1,
'flags': X4,
'updatePeriod': U4,
'searchPeriod': U4,
'gridOffset': U4,
'onTime': U2,
'minAcqTime': U2,
'reserved4': U2,
'reserved5': U2,
'reserved6': U4,
'reserved7': U4,
'reserved8': U1,
'reserved9': U1,
'reserved10': U2,
'reserved11': U4
},
'CFG-PMS': {
'version': U1,
'powerSetupValue': U1,
'period': U2,
'onTime': U2,
'reserved1': U2
},
'CFG-PRT': {
'portID': U1,
'reserved0': U1,
'txReady': X2,
'mode': X4,
'baudRate': U4,
'inProtoMask': X2,
'outProtoMask': X2,
'reserved4': U2,
'reserved5': U2
},
'CFG-PWR': {
'version': U1,
'reserved1': U3,
'state': U4
},
'CFG-RATE': {
'measRate': U2,
'navRate': U2,
'timeRef': U2
},
'CFG-RINV': {
'flags': X1,
'group': ('None', {  # repeating group
'data': U1
})},
'CFG-RST': {
'navBbrMask': X2,
'resetMode': U1,
'reserved1': U1
},
'CFG-RXM': {
'reserved1': U1,
'lpMode': U1
},
'CFG-SBAS': {
'mode': X1,
'usage': X1,
'maxSBAS': U1,
'scanmode2': X1,
'scanmode1': X4
},
'CFG-SMGR': {
'minGNSSFix' : U1,
'maxFreqChange': U2,
'maxPhaseCorrRate': U2,
'reserved1': U2,
'freqTolerance' : U2,
'timeTolerance': U2,
'messageCfg': X2,
'maxSlewRate': U2,
'flags': X4
},
'CFG-TMODE2': {
'timeMode': U1,
'reserved1': U1,
'flags': X2,
'ecefXOrLat': I4,
'ecefYOrLon': I4,
'ecefZOrAlt': I4,
'fixedPosAcc': U4,
'svinMinDur': U4,
'svinAccLimit': U4
},
'CFG-TP5': {
'tpIdx': U1,
'reserved0': U1,
'reserved1': U2,
'antCableDelay': I2,
'rfGroupDelay': I2,
'freqPeriod': U4,
'freqPeriodLock': U4,
'pulseLenRatio': U4,
'pulseLenRatioLock': U4,
'userConfigDelay': I4,
'flags': X4
},
'CFG-TXSLOT': {
'version': U1,
'enable': X1,
'refTp': U1,
'reserved1': U1,
'end1': U4,
'end2': U4,
'end3': U4
},
'CFG-USB': {
'vendorID': U2,
'productID': U2,
'reserved1': U2,
'reserved2': U2,
'powerConsumpt': U2,
'flags': X2,
'vendorString': C32,
'productString': C32,
'serialNumber': C32
},
# ********************************************************************
# Logging Messages: i.e. Log creation, deletion, info and retrieval.
# Messages in the LOG class are used to configure and report status information of the logging feature.
'LOG-ERASE': {
},
'LOG-RETRIEVE': {
'startNumber': U4,
'entryCount': U4,
'version': U1,
'reserved': U3
},
'LOG-STRING': {
'group': ('None', {  # repeating group
'bytes': U1
})},
# ********************************************************************
# Multiple GNSS Assistance Messages: i.e. Assistance data for various GNSS.
# Messages in the MGA class are used for GNSS aiding information from and to the receiver.
'MGA-ANO': {
'type': U1,
'version': U1,
'svId': U1,
'gnssId': U1,
'year': U1,
'month': U1,
'day': U1,
'reserved1': U1,
'data': U64,
'reserved2': U4,
},
'MGA-BDS-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'SatH1': U1,
'IODC': U1,
'a2': I2,
'a1': I4,
'a0': I4,
'toc': U4,
'TGD1': I2,
'URAI': U1,
'IODE': U1,
'toe': U4,
'sqrtA': U4,
'e': U4,
'omega': I4,
'Deltan': I2,
'IDOT': I2,
'M0': I4,
'Omega0': I4,
'OmegaDot': I4,
'i0': I4,
'Cuc': I4,
'Cus': I4,
'Crc': I4,
'Crs': I4,
'Cic': I4,
'Cis': I4,
'reserved2': U4
},
'MGA-BDS-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'Wna': U1,
'toa': U1,
'deltaI': I2,
'sqrtA': U4,
'e': U4,
'omega': I4,
'M0': I4,
'Omega0': I4,
'omegaDot': I4,
'a0': I2,
'a1': I2,
'reserved2': U4
},
'MGA-BDS-HEALTH': {
'type': U1,  # 0x04
'version': U1,
'reserved1': U2,
'healthCode01': U2,
'healthCode02': U2,
'healthCode03': U2,
'healthCode04': U2,
'healthCode05': U2,
'healthCode06': U2,
'healthCode07': U2,
'healthCode08': U2,
'healthCode09': U2,
'healthCode10': U2,
'healthCode11': U2,
'healthCode12': U2,
'healthCode13': U2,
'healthCode14': U2,
'healthCode15': U2,
'healthCode16': U2,
'healthCode17': U2,
'healthCode18': U2,
'healthCode19': U2,
'healthCode20': U2,
'healthCode21': U2,
'healthCode22': U2,
'healthCode23': U2,
'healthCode24': U2,
'healthCode25': U2,
'healthCode26': U2,
'healthCode27': U2,
'healthCode28': U2,
'healthCode29': U2,
'healthCode30': U2,
'reserved2': U4
},
'MGA-BDS-UTC': {
'type': U1,
'version': U1,
'reserved1': U2,
'a0UTC': I4,
'a1UTC': I4,
'dtLS': I1,
'reserved2': U1,
'wnRec': U1,
'wnLSF': U1,
'dN': U1,
'dtLSF': I1,
'reserved3': U2
},
'MGA-BDS-IONO': {
'type': U1,
'version': U1,
'reserved1': U2,
'alpha0': I1,
'alpha1': I1,
'alpha2': I1,
'alpha3': I1,
'beta0': I1,
'beta1': I1,
'beta2': I1,
'beta3': I1,
'reserved2': U4
},
'MGA-FLASH-DATA': {
'type': U1,
'version': U1,
'sequence': U2,
'size': U2,
'group': ('size', {  # repeating group * size
'data': U1
})},
'MGA-FLASH-STOP': {
'type': U1,
'version': U1
},
'MGA-GAL-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'iodNav': U2,
'deltaN': I2,
'm0': I4,
'e': U4,
'sqrtA': U4,
'omega0': I4,
'i0': I4,
'omega': I4,
'omegaDot': I4,
'iDot': I2,
'cuc': I2,
'cus': I2,
'crc': I2,
'crs': I2,
'cic': I2,
'cis': I2,
'toe': U2,
'af0': I4,
'af1': I4,
'af2': I1,
'sisaIndexE1E5b': U1,
'toc': U2,
'bgdE1E5b': I2,
'reserved2': U2,
'healthE1B': U1,
'dataValidityE1B': U1,
'healthE5b': U1,
'dataValidityE5b': U1,
'reserved3': U4
},
'MGA-GAL-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'ioda': U1,
'almWNa': U1,
'toa': U2,
'deltaSqrtA': I2,
'e': U2,
'deltaI': I2,
'omega0': I2,
'omegaDot': I2,
'omega': I2,
'm0': I2,
'af0': I2,
'af1': I2,
'healthE1B': U1,
'healthE5b': U1,
'reserved2': U4
},
'MGA-GAL-TIMEOFFSET': {
'type': U1,
'version': U1,
'reserved1': U2,
'a0G': I2,
'a1G': I2,
't0G': U1,
'wn0G': U1,
'reserved2': U2
},
'MGA-GAL-UTC': {
'type': U1,
'version': U1,
'reserved1': U2,
'a0': I4,
'a1': I4,
'dtLS': I1,
'tot': U1,
'wnt': U1,
'wnLSF': U1,
'dN': U1,
'dTLSF': I1,
'reserved2': U2
},
'MGA-GLO-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'FT': U1,
'B': U1,
'M': U1,
'H': I1,
'x': I4,
'y': I4,
'z': I4,
'dx': I4,
'dy': I4,
'dz': I4,
'ddx': I1,
'ddy': I1,
'ddz': I1,
'tb': U1,
'gamma': I2,
'E': U1,
'deltaTau': I1,
'tau': I4,
'reserved2': U4
},
'MGA-GLO-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'N': U2,
'M': U1,
'C': U1,
'tau': I2,
'epsilon': U2,
'lambda': I4,
'deltaI': I4,
'tLambda': U4,
'deltaT': I4,
'deltaDT': I1,
'H': I1,
'omega': I2,
'reserved2': U4
},
'MGA-GLO-TIMEOFFSET': {
'type': U1,
'version': U1,
'N': U2,
'tauC': I4,
'tauGps': I4,
'B1': I2,
'B2': I2,
'reserved1': U4
},
'MGA-GPS-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'fitInterval': U1,
'uraIndex': U1,
'svHealth': U1,
'tgd': I1,
'iodc': U2,
'toc': U2,
'reserved2': U1,
'af2': I1,
'af1': I2,
'af0': I4,
'crs': I2,
'deltaN': I2,
'm0': I4,
'cuc': I2,
'cus': I2,
'e': U4,
'sqrtA': U4,
'toe': U2,
'cic': I2,
'omega0': I4,
'cis': I2,
'crc': I2,
'i0': I4,
'omega': I4,
'omegaDot': I4,
'idot': I2,
'reserved3': U4
},
'MGA-GPS-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'svHealth': U1,
'e': U2,
'almWNa': U1,
'toa': U1,
'deltaI': I2,
'omegaDot': I2,
'sqrtA': U4,
'omega0': I4,
'omega': I4,
'm0': I4,
'af0': I2,
'af1': I2,
'reserved1': U4
},
'MGA-GPS-HEALTH': {
'type': U1,
'version': U1,
'reserved1': U2,
'healthCode01': U1,
'healthCode02': U1,
'healthCode03': U1,
'healthCode04': U1,
'healthCode05': U1,
'healthCode06': U1,
'healthCode07': U1,
'healthCode08': U1,
'healthCode09': U1,
'healthCode10': U1,
'healthCode11': U1,
'healthCode12': U1,
'healthCode13': U1,
'healthCode14': U1,
'healthCode15': U1,
'healthCode16': U1,
'healthCode17': U1,
'healthCode18': U1,
'healthCode19': U1,
'healthCode20': U1,
'healthCode21': U1,
'healthCode22': U1,
'healthCode23': U1,
'healthCode24': U1,
'healthCode25': U1,
'healthCode26': U1,
'healthCode27': U1,
'healthCode28': U1,
'healthCode29': U1,
'healthCode30': U1,
'healthCode31': U1,
'healthCode32': U1,
'reserved': U4,
},
'MGA-GPS-UTC': {
'type': U1,
'version': U1,
'reserved1': U2,
'utcA0': I4,
'utcA1': I4,
'utcDtLS': I1,
'utcTot': U1,
'utcWNt': U1,
'utcWNlsf': U1,
'utcDn': U1,
'utcDtLSF': I1,
'reserved2': U2
},
'MGA-GPS-IONO': {
'type': U1,
'version': U1,
'reserved1': U2,
'ionoAlpha0': I1,
'ionoAlpha1': I1,
'ionoAlpha2': I1,
'ionoAlpha3': I1,
'ionoBeta0': I1,
'ionoBeta1': I1,
'ionoBeta2': I1,
'ionoBeta3': I1,
'reserved2': U4
},
'MGA-INI-POS_XYZ': {
'type': U1,
'version': U1,
'reserved1': U2,
'ecefX': I4,
'ecefY': I4,
'ecefZ': I4,
'posAcc': U4
},
'MGA-INI-POS_LLH': {
'type': U1,
'version': U1,
'reserved1': U2,
'lat': I4,
'lon': I4,
'alt': I4,
'posAcc': U4
},
'MGA-INI-TIME_UTC': {
'type': U1,
'version': U1,
'ref': X1,
'leapSecs': I1,
'year': U2,
'month': U1,
'day': U1,
'hour': U1,
'minute': U1,
'second': U1,
'reserved1': U1,
'ns': U4,
'tAccS': U2,
'reserved2': U2,
'tAccNs': U4
},
'MGA-INI-TIME_GNSS': {
'type': U1,
'version': U1,
'ref': X1,
'gnssId': U1,
'reserved1': U2,
'week': U2,
'tow': U4,
'ns': U4,
'tAccS': U2,
'reserved2': U2,
'tAccNs': U4
},
'MGA-INI-CLKD': {
'type': U1,
'version': U1,
'reserved1': U2,
'clkD': I4,
'clkDAcc': U4
},
'MGA-INI-FREQ': {
'type': U1,
'version': U1,
'reserved1': U1,
'flags': X1,
'freq': I4,
'freqAcc': U4
},
'MGA-INI-EOP': {
'type': U1,
'version': U1,
'reserved1': U2,
'd2kRef': U2,
'd2kMax': U2,
'xpP0': I4,
'xpP1': I4,
'ypP0': I4,
'ypP1': I4,
'dUT1': I4,
'ddUT1': I4,
'reserved2': U40
},
'MGA-QZSS-EPH': {
'type': U1,
'version': U1,
'svId': U1,
'reserved1': U1,
'fitInterval': U1,
'uraIndex': U1,
'svHealth': U1,
'tgd': I1,
'iodc': U2,
'toc': U2,
'reserved2': U1,
'af2': I1,
'af1': I2,
'af0': I4,
'crs': I2,
'deltaN': I2,
'm0': I4,
'cuc': I2,
'cus': I2,
'e': U4,
'sqrtA': U4,
'toe': U2,
'cic': I2,
'omega0': I4,
'cis': I2,
'crc': I2,
'i0': I4,
'omega': I4,
'omegaDot': I4,
'idot': I2,
'reserved3': U2
},
'MGA-QZSS-ALM': {
'type': U1,
'version': U1,
'svId': U1,
'svHealth': U1,
'e': U2,
'almWNa': U1,
'toa': U1,
'deltaI': I2,
'omegaDot': I2,
'sqrtA': U4,
'omega0': I4,
'omega': I4,
'm0': I4,
'af0': I2,
'af1': I2,
'reserved1': U4
},
'MGA-QZSS-HEALTH': {
'type': U1,
'version': U1,
'reserved1': U2,
'healthCode1': U1,
'healthCode2': U1,
'healthCode3': U1,
'healthCode4': U1,
'healthCode5': U1,
'reserved2': U3
},
# ********************************************************************
# Navigation Results Messages: i.e. Position, Speed, Time, Acceleration, Heading, DOP, SVs used.
# Messages in the NAV class are used to output navigation data such as position, altitude and velocity in a
# number of formats. Additionally, status flags and accuracy figures are output. The messages are generated with
# the configured navigation/measurement rate.
'NAV-RESETODO': {
},
# ********************************************************************
# Receiver Manager Messages: i.e. Satellite Status, RTC Status.
# Messages in the RXM class are used to output status and result data from the Receiver Manager. The output
# rate is not bound to the navigation/measurement rate and messages can also be generated on events.
'RXM-PMREQ': {
'duration': U4,
'flags': X4
},
# ********************************************************************
# Timing Messages: i.e. Time Pulse Output, Time Mark Results.
# Messages in the TIM class are used to output timing information from the receiver, like Time Pulse and Time
# Mark measurements.
'TIM-HOC': {
'version': U1,
'oscId': U1,
'flags': U1,
'reserved1': U1,
'value': I4
},
'TIM-VCOCAL': {
'type': U1,
'version': U1,
'oscId': U1,
'reserved1': U3,
'gainUncertainty': U2,
'gainVco': I4,
},
# ********************************************************************
# Firmware Update Messages: i.e. Memory/Flash erase/write, Reboot, Flash identification, etc..
# Messages in the UPD class are used to update the firmware and identify any attached flash device.
'UPD-SOS': {  # Create or clear backup in flash
'cmd': U1,
'reserved1': U3
}
}