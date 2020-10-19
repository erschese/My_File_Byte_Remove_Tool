import codecs
import subprocess


def test_bytekit():
    return 'Bytekit'


def split_bytes(bytes_, i_):
    return [bytes_[i:i + i_] for i in range(0, len(bytes_), i_)]


def remove_sensitive_bytes_from_text(encoding_, decoding_, text_, remove_bytes_list_):
    result_text = ''
    no_byte_found_dummy = True
    found_dummy = False
    text_b = text_.encode(encoding_, errors='strict')
    text_bytes_as_array = split_bytes(text_b, 1)
    for text_byte in text_bytes_as_array:
        for remove_byte in remove_bytes_list_:
            if text_byte == remove_byte:
                no_byte_found_dummy = False
                found_dummy = True
        if no_byte_found_dummy:
            result_text = result_text + text_byte.decode(decoding_, errors='strict')
            no_byte_found_dummy = True
        else:
            no_byte_found_dummy = True
    # print text with findings
    if found_dummy:
        print('\nfinding in: ', text_)
        print('changed to: ', result_text)
    # return text with removals
    if result_text is None or result_text == '':
        return "\n"
    else:
        return result_text


def encode_my_file_and_remove_bytes(source_file_, output_file_, output_decoding_, remove_bytes_list_):
    print('\n%%%%%%%%%%%\nSTART FILE ENCODING\n%%%%%%%%%%%')
    print('...')
    file_encoding = subprocess.getoutput('file -b --mime-encoding %s' % source_file_)
    print('file format of file ' + source_file_ + ' is ' + file_encoding)
    source_stream = codecs.open(source_file_, 'r', file_encoding)
    output_stream = codecs.open(output_file_, 'w', output_decoding_)

    for l_ in source_stream:
        l_remove_bytes = remove_sensitive_bytes_from_text(file_encoding, output_decoding_, l_, remove_bytes_list_)
        output_stream.write(l_remove_bytes)

    source_stream.close()
    output_stream.close()
    print('...done!')


def println_file(source_file_, linenumber_):
    print('\n%%%%%%%%%%%\nSTART PRINTLN FROM FILE\n%%%%%%%%%%%')
    print('...')
    file_encoding = subprocess.getoutput('file -b --mime-encoding %s' % source_file_)
    print(source_file_, 'has format', file_encoding)
    source_stream = codecs.open(source_file_, 'r', file_encoding)
    linecounter = 0
    for l_ in source_stream:
        if linecounter == linenumber_:
            print(l_, '\n')
            print('...done!')
            return
        else:
            linecounter = linecounter + 1
    print('...done!')


def test_remove_sensitive_bytes_from_text(encoding_, decoding_, text_, search_bytes_as_array_):
    print('\n%%%%%%%%%%%\n(TEST) REMOVING BYTES FROM TEXT\n%%%%%%%%%%%')
    print('...')
    remove_sensitive_bytes_from_text(encoding_, decoding_, text_, search_bytes_as_array_)
    print('...done!')


def encode_my_file(source_file_, output_file_, output_encoding_):
    print('\n%%%%%%%%%%%\nSTART FILE ENCODING\n%%%%%%%%%%%')
    print('...')
    file_encoding = subprocess.getoutput('file -b --mime-encoding %s' % source_file_)
    print('file format of file ' + source_file_ + ' is ' + file_encoding)
    source_stream = codecs.open(source_file_, 'r', file_encoding)
    output_stream = codecs.open(output_file_, 'w', output_encoding_)

    for l_ in source_stream:
        output_stream.write(l_)

    source_stream.close()
    output_stream.close()
    print('...done!')


def change_xml_header(source_file_, output_file_, header_text_):
    print('\n%%%%%%%%%%%\nCHANGING FILE HEADER\n%%%%%%%%%%%')
    print('...')
    file_encoding = subprocess.getoutput('file -b --mime-encoding %s' % source_file_)
    source_stream = codecs.open(source_file_, 'r', file_encoding)
    output_stream = codecs.open(output_file_, 'w', file_encoding)
    isfirstline = True
    for l_ in source_stream:
        if isfirstline:
            output_stream.write(header_text_)
            isfirstline = False
        else:
            output_stream.write(l_)
    print('...done!')


def generate_file_with_ecoding(encoding_, outputfile_, text_):
    print('\n%%%%%%%%%%%\nGENERATING FILE\n%%%%%%%%%%%')
    print('...')
    with codecs.open(outputfile_, "w", encoding_) as f_:
        f_.write(text_)
    print('...done!')
