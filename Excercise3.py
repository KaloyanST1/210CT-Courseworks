def RemoveVowels(Maybestring):
    if not Maybestring: # empty string
        return Maybestring
    elif Maybestring[0] in "aeiou": # first character is vowel #is Y a vowel?!
        
        return RemoveVowels(Maybestring[1:]) # skip first character and process rest
    return Maybestring[0] + RemoveVowels(Maybestring[1:])



