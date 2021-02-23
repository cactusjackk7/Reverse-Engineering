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
   
   def __init__(self):
      self.cksums = set()
   
   def checksum(self):
       '''
       Search for WPS checksum functions.

       Return a set of functions EAs.
       '''
       self.search_for_immediates()

       self.cksums = self.IMMEDIATES.values()[0]
       for i in range(1, len(self.IMMEDIATES).values())):
            self.cksums = self.cksums & self.IMMEDIATES.values()[i]
        
        return self.cksums 
    def xrefs(self):
         '''
        Identify functions that reference the WPS checksum functions and resolve their string xrefs.
        Returns a dictionary of function EAs and a list of their string xrefs.
        '''
        self._generate_checksum_xrefs_table()

        for string in idautils.String()
            for xref in idautils.XrefsTo(string.ea):
                func = idaapi.get_func(xref.frm)
                if func and self.funcs.has_key(func.startEA):
                     self.funcs[func.startEA].add(str(string))

         return self.funcs

    def _search_for_immediates(self):
         for immediate in self..IMMEDIATES.keys():
            ea = 0
            while ea != idc.BADADDR:
               (ea, n) = idc.FindImmediate(ea, idc.SEARCH_DOWN, self._twos_compliment(immediate))
               if ea != idc.BADADDR:
                  func = idaapi.get_func(ea)
                  if func:
                     self.IMMEDIATES[immediate].add(func.startEA)

     def _twos_compliment
