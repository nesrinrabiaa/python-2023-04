# 1.PLUSSA


# Skapa ett program med en ny metod. Metoden skall ta emot två inparametrar av 
# typen string och slå ihop dom till en sträng och returnera det nya värdet. 
# Anropa den nya metoden från Main och skriv ut resultatet på skärmen.
def concatenate_strings(str1: str, str2: str) -> str:
    """
    # Takes two string parameters and concatenates them into a new string.

    # Args:
    # str1 (str): First string to concatenate.
    # str2 (str): Second string to concatenate.

    # Returns:
    # str: A new string consisting of the concatenation of str1 and str2.
    # """
    return str1 + str2

# Test the new method by calling it with two strings and printing the result
result = concatenate_strings("Hello ", "world!")
print(result)