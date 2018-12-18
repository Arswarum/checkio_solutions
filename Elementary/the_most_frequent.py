#!/usr/local/bin/checkio --domain=py run the-most-frequent

# https://py.checkio.org/mission/the-most-frequent/

# You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
# 
# Input:a list of strings.
# 
# Output:a string.
# 
# 
# END_DESC

def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    m_f = None
    qty_m_f = 0
    for item in data:
        qty = data.count(item)
        if qty > qty_m_f:
            qty_m_f = qty
            m_f = item


    return m_f

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]))
    
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')