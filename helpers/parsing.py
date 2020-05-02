def check_file_extension(allowed_extensions, filename):
    extension = '.' + filename.split('.')[-1]
    return extension in allowed_extensions


def extract_header_and_body(file):
    body_part = False
    header, body = '', ''
    for line in file:
        if line == '\n':
            body_part = True
        if not body_part:
            header += line
        else:
            body += line
    return header, body


def get_content_type(header):
    """
    Content-Type: text/plain;
    """
    header = header.split('\n')
    content_type_line = list(filter(lambda x: 'content-type' in x.lower(), header))
    if not content_type_line:
        return None
    else:
        content_type_line = content_type_line[0]
    if ':' in content_type_line:
        content_type = content_type_line.split(':')[1]
    else:
        return None
    return content_type.split(';')[0]


def process_content_type(content_type):
    if isinstance(content_type, str):
        return content_type.lower().strip()
    else:
        return None
