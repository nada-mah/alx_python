def multiple_returns(sentence):
    length=(len(sentence),)    
    if len(sentence) != 0:
        # length=(len(sentence),)    
        first=sentence[0]
    else:
        first=None
    return length[0], first
