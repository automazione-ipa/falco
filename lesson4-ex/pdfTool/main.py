import sys
import pdf_utils

if len(sys.argv) == 2:
    pdf_path = sys.argv[1]
    file_out = open('./out.txt', 'w', encoding='utf-8')
    text_out = pdf_utils.extract_text_from_pdf(pdf_path)
    file_out.write(text_out)
    file_out.close()
    print('Text extracted successfully')
if len(sys.argv) == 4:
    if sys.argv[2] == '-t' and sys.argv[3] != '':
        result = pdf_utils.get_info_in_file_by_word(content_path=sys.argv[1], word_to_search=sys.argv[3])
        if result != '':
            print(result)
        else:
            print("No info was found")
    elif sys.argv[2] == '-p' and sys.argv[3] != '':
        text_content = pdf_utils.extract_text_from_pdf(sys.argv[1])
        result = pdf_utils.get_info_in_content_by_word(content=text_content, word_to_search=sys.argv[3])
        if result != '':
            print(result)
        else:
            print("No info was found")
    else:
        print('error')
