'''This code checks if any word in the sentence is in all 
uppercase letters, if any word is a digit, and if the sentence
ends with a proper punctuation mark (., !, or ?). If any of these 
conditions are met,the function returns True to indicate that an 
error has been detected.'''

def error_detection(sentence):
    words = sentence.split()
    error = False
    
    # Check if any word is in all uppercase
    for word in words:
        if word.isupper():
            error = True
            break
    
    # Check if any word is a digit
    for word in words:
        if word.isdigit():
            error = True
            break
    
    # Check if the sentence ends with a punctuation
    if sentence[-1] not in ['?', '!', '.']:
        error = True
        
    return error

sentence = "THIS IS A TEST SENTENCE1"
if error_detection(sentence):
    print("Error detected in sentence.")
else:
    print("No error detected in sentence.")
