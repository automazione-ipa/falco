import pypdf


def extract_text_from_pdf(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    reader = pypdf.PdfReader(pdf_file)
    text_out = ''.join(str(page.extract_text(0)) for page in reader.pages)
    reader.close()
    return text_out


def get_info_in_file_by_word(content_path, word_to_search):
    text_file = open(content_path, 'r')
    content = text_file.read()
    splitted_content = content.split('\n')
    for row in splitted_content:
        if word_to_search in row:
            return row
    return ''


def get_info_in_content_by_word(content, word_to_search):
    splitted_content = content.split('\n')
    for row in splitted_content:
        if word_to_search in row:
            return row
    return ''