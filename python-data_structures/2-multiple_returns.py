def multiple_returns(sentence):
    length=(len(sentence),)    
    if len(sentence) != 0:
        # length=(len(sentence),)    
        first=sentence[0]
    else:
        first=None
    return length[0], first

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))