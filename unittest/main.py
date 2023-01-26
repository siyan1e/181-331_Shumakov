
def replace_base_symbols(text: str) -> str:
    """Функция для единообразного преобразования входного текста (пословицы)

    Parameters
    ----------
    text : str
        Исходный текст (пословица).

    Example
    -------
        >>> replace_base_symbols('абв где, ёжз. -ийк')
        абвпрблгдезптпрблёжзтчкпрблтиреийк

    Returns
    -------
    str
        Преобразованная строка

    Notes
    -----
    Список замены:
        * 'ё' -> 'е'
        * ',' -> 'зпт'
        * '.' -> 'тчк'
        * '-' -> 'тире'
        * ' ' -> 'прбл'
    """
    text = text.replace('ё', 'е')
    text = text.replace(',', 'зпт')
    text = text.replace('.', 'тчк')
    text = text.replace('-', 'тире')
    text = text.replace(' ', 'прбл')
    return text.lower()

def reverse_replace_base_symbols(text: str) -> str:
    """Функция для единообразного преобразования входного текста (пословицы)

        Parameters
        ----------
        text : str
            Исходный текст (пословица).

        Example
        -------
            >>> replace_base_symbols('абвпрблгдезптпрблёжзтчкпрблтиреийк')
            абв где, ёжз. -ийк

        Returns
        -------
        str
            Преобразованная строка

        Notes
        -----
        Список замены:
            * 'зпт' -> ','
            * 'тчк' -> '.'
            * 'тире' -> '-'
            * 'прбл' -> ' '
        """
    text = text.replace('зпт', ',')
    text = text.replace('тчк', '.')
    text = text.replace('тире', '-')
    text = text.replace('прбл', ' ')
    return text


# Функция шифрования
def encrypt(text, shift):
    text = replace_base_symbols(text)
    result = ""
    for i in range(len(text)):
        result += chr((ord(text[i]) + shift - 1072) % 32 + 1072) # Применение сдвига к символам текста
    return result

# Функция расшифрования
def decrypt(encText, shift):
    result = ""
    for i in range(len(encText)):
        result += chr(((ord(encText[i]) - shift - 1072) % 32) + 1072) # Применение сдвига к символам текста
    return reverse_replace_base_symbols(result)

print(encrypt('съешь ещё этих мягких французских булок, да выпей чаю',3))