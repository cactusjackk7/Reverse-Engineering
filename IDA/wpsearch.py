import idc 
import idaapi
import idautils

class WPSearch(object):
   '''
   Sea Searches for immediate values commonly founds in MIPS WPS checksum implementations.
   May be applicable to other architectures as well.
   '''

   IMMEDIATES = {
                  0x6B5FCA6B : set(),
                  0x431BDE83 : set(),
                  0x0A7C5AC5 : set(),
                  0x10624DD3 : set(),
                  0x51EB851F : set(),
                  0xCCCCCCCD : set(),
                  0xD1B71759 : set(),
   }
