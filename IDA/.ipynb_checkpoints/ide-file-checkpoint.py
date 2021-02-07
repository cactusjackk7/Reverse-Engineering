import os
import idaapi


def find_changed_bytes():

    changed_bytes = list()

    for seg_start in Segments():
        for ea in range(seg_start, SegEnd(seg_start) ):
            if isLoaded(ea):
                byte = Byte(ea)
                original_byte = GetOriginalByte(ea)
                if byte != original_byte:
                    changed_bytes.append( (ea, byte, original_byte) )
            
    return changed_bytes



def patch_file(data, changed_bytes):
    
    for ea, byte, original_byte in changed_bytes:
        print '%08x: %02x original(%02x)' % (ea, byte, original_byte)
                
        file_offset = idaapi.get_fileregion_offset( ea )
        
        original_char = chr( original_byte )
        char = chr( byte )
        
        if data[ file_offset ] == original_char:
            data[ file_offset ] = char
    
    patched_file = idc.AskFile( 1, '*.*', 'Choose new file')
    if patched_file:
        with file(patched_file, 'wb') as f:
            f.write( ''.join( data ) )



def main():
    
    print 'Finding changed bytes...',
    changed_bytes = find_changed_bytes()
    print 'done. %d changed bytes found' % len(changed_bytes)
    
    if changed_bytes:
        original_file = GetInputFilePath()
        print original_file
    
        if not os.path.exists(original_file):
            original_file = idc.AskFile( 0, '*.*', 'Select original file to patch')
        
        if os.path.exists(original_file):

            with file(original_file, 'rb') as f:
                data = list( f.read() )

            patch_file(data, changed_bytes)
        
        else:
            print 'No valid file to patch provided'

    else:
        print 'No changes to patch'

        
print '---- Running IDA file patching script version %s ----' % __version__
main()
print '---- Script finished ----'