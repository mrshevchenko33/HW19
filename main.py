def is_palindrome(text):
    new_text = ''.join(i.lower() for i in text if i.isalnum())
    return new_text == new_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")