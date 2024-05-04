import re

def extract_digits(text):
    pattern = r'\b\d{1,3}(?:,\d{3})*(?:,\d+)?(?:\.\d+)?\b'

    digits = re.findall(pattern, text)

    digits = [float(digit.replace(',', '.')) for digit in digits]

    return digits

def word_to_number(text):
    number_mapping = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    pattern = r'\b(?:' + '|'.join(number_mapping.keys()) + r')\b'
    return [number_mapping[word] for word in re.findall(pattern, text)]

def words_after_numbers_except_kilos(text):
    pattern = r'\b(?:zero|one|two|three|four|five|six|seven|eight|nine)\s+(\w+)\b'

    matches = re.findall(pattern, text)

    result_words = []

    for match in matches:
        word = match
        if word.lower() == 'kilo':
            split_parts= text.split('kilo',1)
            text =split_parts[1].strip()
            index_of_of = text.find("of")
            if index_of_of != -1:
                substring_after_of = text[index_of_of + len("of"):].strip()

                match_after_of = re.search(r'\b(\w+)\b', substring_after_of)
                if match_after_of:
                    result_words.append(match_after_of.group(1))
        elif word.lower() == 'kilos':
            split_parts= text.split('kilos',1)
            text =split_parts[1].strip()
            index_of_of = text.find("of")
            if index_of_of != -1:
                substring_after_of = text[index_of_of + len("of"):].strip()

                match_after_of = re.search(r'\b(\w+)\b', substring_after_of)
                if match_after_of:
                    result_words.append(match_after_of.group(1))
        else:
            result_words.append(word)

    return result_words

def process_text():
    sentence =input('write a text to generate the bill: ')
    digit_list = extract_digits(sentence)
    number_list = word_to_number(sentence)
    words_list = words_after_numbers_except_kilos(sentence)

    total_price_list = [digit_list[i] * number_list[i] for i in range(0, len(digit_list))]

    print("Product\t\tQuantity\tUnit Price\tTotal Price")
    for i in range(len(words_list)):
        print("{:<16}\t{:>8}\t{:>10}\t{:>11}".format(words_list[i], number_list[i], digit_list[i],
                                                     total_price_list[i]))

process_text()