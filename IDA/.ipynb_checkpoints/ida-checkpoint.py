import pefile
import peutils

peid_db_URL = 'http://reverse-engineering-scripts.googlecode.com/files/UserDB.TXT'

def main():
   inf = idaapi.get_inf_structure()

   #find the null char of the string (if any)
   null_idxv = inf.procName.find(ch(0))
   if null_idx > 0:
        processor_name = inf.procName[:null_idx]
   else:
         processor_name = inf.procName

             if 'metapc' not in processor_name:
                print 'This script can only handle x86 (metapc) and [%s] has been found' % processor_name
             return
                                   
             print 'Found [%s] architecture, loading signatures...' % processor_name

             try:
                 signatures = peutils.SignatureDatabase( peid_db_URL )
            except Exception as excp:
                  print 'Unable to load PEiD signature databases'
                  print str(excp)
           return

       ep_count = GetEntryPointQty()
           if ep_count == 0:
              print 'The script could not find any entry points in the IDB'
              print 'The signatures will be checked at the locations of entry points.'
              print 'You can add entry points using the AddEntryPoint() function:'
              print 'Documentation for AddEntryPoint():'
              print '---------------------------------------------------------------'
              print AddEntryPoint.__doc__
              print '---------------------------------------------------------------'
              return
                                                                                   
                                  
        for ep_idx in range( ep_count ) :
             ep_ord = GetEntryOrdinal( ep_idx )
             ep = GetEntryPoint( ep_ord )                                                                    print 'Analyzing entry-point [%08x], %d of %d' % (ep, ep_idx+1, ep_count                        data_length = 128
             data = GetManyBytes(ep, data_length, 0)
            if data is None or len(data) != data_length:
                    print 'Unable to read %d bytes at [%08x]' % (data_length, ep)
            continue
           matches = signatures.match_data( data, ep_only = True )
        if matches:
        print 'Signatures matched at [%08x]: %s' % (ep, '; '.join( x[0] for x in matches[1] ))
        print '---- Running IDA PEiD script version %s ----' % __version__
        main()
                                                                                                                                                                                                   print '---- Script finished ----'
