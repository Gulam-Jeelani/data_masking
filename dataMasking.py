import random as rand

# character mappings
def getSubstitute(c):
    return {
        "0":"7", "1":"9", "2":"5", "3":"1", "4":"8", "5":"6", "6":"4", "7":"3", "8":"0", "9":"2", "A":"Z", "B":"Y",
        "C":"X", "D":"W", "E":"V", "F":"U", "G":"T", "H":"S", "I":"R", "J":"Q", "K":"P", "L":"O", "M":"N", "N":"M",
        "O":"L", "P":"K", "Q":"J", "R":"I", "S":"H", "T":"G", "U":"F", "V":"E", "W":"D", "X":"C", "Y":"B", "Z":"A",
        "a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o",
        "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c",
        "y":"b", "z":"a"
    }.get(c, c)

# Below function susbtitue the actual data to some random data based on the above mapping
def substitution(text):
    cipher_text = ""
    if text is not None:
        for i in str(text):
           cipher_text += getSubstitute(i)
    return cipher_text

# This function scrambles data word by word
def scrambling(text):
    if text is not None:
        words = text.split()
        rand.shuffle(words)
        return " ".join(words)
    return ""

# In this function both substitution() and scrambling() functions are called
def two_layer_masking(text):
    layer1_txt = substitution(text)
    layer2_txt = scrambling(layer1_txt)
    return layer2_txt

# This method shuffles the rows based on the column list passed to it
def shuffle(df, col_list):
    for col in col_list:
        df[col] = df[col].sample(frac = 1).values
    return df
