def extract_bold_texts(html):
    bold_list = []
    if "</b>" in html:
        words = html.split("</b>")
        
        for word in words:
            if "<b>" in word:
                bold_word = word.split("<b>")
                bold_list.append(bold_word[1].strip())

        return bold_list
    else:
        return []