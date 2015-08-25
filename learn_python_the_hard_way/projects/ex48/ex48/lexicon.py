directions = ['north', 'south', 'east', 'west', 'down',
              'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
numbers = ['0', '1', '2', '3', '4', '5',
           '6', '7', '8', '9']

def scan(text):
    tokens = text.split()
    results = []

    for token in tokens:
        token_type = 'error'
        if token in directions:
            token_type = 'direction'
        elif token in verbs:
            token_type = 'verb'
        elif token in stops:
            token_type = 'stop'
        elif token in nouns:
            token_type = 'noun'
        else:
            try:
                token_type = 'number'
                value = int(token)
                token = value
            except ValueError:
                token_type = 'error'

        results.append((token_type, token))

    return results
        
                

            
