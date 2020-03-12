def rotate(text, key):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''
    for character in text:
        if character.lower() in abc:
            pos = abc.index(character.lower()) + key
            if pos > 25: pos -= 26

            if character.islower(): new_text += abc[pos]
            else: new_text += abc[pos].upper()
        else:
            new_text += character 
    return new_text

