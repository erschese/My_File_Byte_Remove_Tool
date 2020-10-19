import bytekit as bk

if __name__ == '__main__':
    # Search for sensitive bytes in file
    # ------------------------------------------------------------------------------------------------------------------
    search_b = b'\xA4\xA6\xA8\xB4\xB8\xBC\xBD\xBE'
    decoding = 'iso-8859-1'
    text = '-DÜRER-ABC´XYZ-¤-'

    # test remove_sensitive_bytes_from_text
    search_bytes_as_array = bk.split_bytes(search_b, 1)
    # bk.test_remove_sensitive_bytes_from_text('iso-8859-1', decoding, text, search_bytes_as_array)

    # remove bytes from file
    source_filepath_3 = '/home/b22263/Schreibtisch/Partner/2020-08-31_A360_Entlade_Person.xml'
    output_filepath_3 = '/home/b22263/Schreibtisch/Partner/2020-08-31_A360_Entlade_Person_REMOVE1.xml'
    bk.encode_my_file_and_remove_bytes(source_filepath_3, output_filepath_3, decoding, search_bytes_as_array)