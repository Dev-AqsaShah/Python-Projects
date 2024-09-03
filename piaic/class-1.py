# print("hello Python")

#! 45 STRING METHODS

#! 1
# text: str = "hello"
# print(text.capitalize())

#! 2
# text1: str = "aqSA"
# text2: str = "AQsa"
# print(text1.casefold())
# print(text2.casefold())

#! 3
# text: str = "aqsa"
# print(text.center(30, "."))

#! 4
# text: str = "aqsa_aqsa_aqsa_aqsa"
# print(text.count("a"))

#! 5
# text: str = "aqsa shah"
# print(text.encode(encoding="utf-8"))  #?The b prefix indicates that the string has been encoded as a bytes object. (bytes means can not change)

#! 6
# text: str = "Apple"
# print(text.endswith('e'))

#! 7
# text: str = 'syed\taqsa\tshah'
# print(text.expandtabs(10))

#! 8
# text: str = "hey im aqsa shah here from nausharo feroz"
# position: int = text.find('from')
# print(position)
# print(text[position:])

#! 9
# text: str = '{subject} is doing: {action}.'
# print(text.format(subject='Cat', action='meow'))
# # or
# text1: str = '{} is doing: {}. '
# print(text1.format('Cat', 'meow'))

#! 10
# coordinates: dict = {'x' : 10, 'y' : -5}
# text: str = 'Coordinates: ({x}, {y})'
# print(text.format_map(coordinates))

#! 11
# text: str = 'hey im student of generative ai'
# position: int = text.index('ai')
# print(position)
# print(text[position:])

#! 12
# text: str = 'heyaqsa120'
# print(text.isalnum())

#! 13
# text: str = 'aqsa'
# print(text.isalpha())

#! 14
# text: str = 'hello'
# print(text.isascii())

#! 15
# text: str = '12345'
# print(text.isdecimal())

#! 16
# text: str = '12334'
# print(text.isdigit())

#! 17
# text: str = '13'
# print(text.isnumeric())

#! 18
# text: str = 'aqsa_shah'
# print(text.isidentifier())

#! 19
# text: str = 'aqsu'
# print(text.islower())

#! 20
# text: str = 'text\n'   # false
# text: str = 'text'  # true
# print(text.isprintable())

#! 21
# text: str = '   '
# print(text.isspace())

#! 22
# text: str = 'Aqsa Shah'
# print(text.istitle())

#! 23
# text: str = 'AQSA'
# print(text.isupper())

#! 24 
# text: str = '-'
# print(text.join(['syed', 'aqsa', 'shah']))

#! 25
# text: str = 'aqsu'
# print(text.ljust(20, '_'))

#! 26
# text: str = 'aqsa'
# print(text.islower())

#! 27
# text: str = 'aqsu shah'
# print(text.lstrip('aqsu'))

#! 28, 29
# text: str = 'That is Baby.'
# table = text.maketrans('B', '😍')

# print(table)
# print(text.translate(table))

#! 30 
# text: str =  'a+b=c'
# print(text.partition('='))

#! 31
# text: str = 'unimportant'
# print(text.removeprefix('un'))

#! 32
# text: str = 'whatsapp'
# print(text.removesuffix('app'))

#! 33
# text: str = 'hey hello aqsa how are you'
# print(text.replace('aqsa', 'aqsu'))

#! 34
# text: str = 'A: Some text. A'
# position = text.rfind('asfgh')
# print(position)

#! 35
# text: str = 'B: hello aqsa. B'
# position = text.rindex('B') #? if not found raises error
# print(position)

#! 36
# text: str = 'text'
# print(text.rjust(20, '_'))

#! 37
# text: str = 'text2=text1=text3'
# print(text.rpartition('='))

#! 38 39
# text: str = 'this is some special stuff'
# print(text.rsplit(maxsplit=2))

# text1: str = 'www.website.com'
# print(text.rsplit(sep='.'))

# text2: str =  'this is some special stuff'
# print(text.split(maxsplit=2))

#! 40
# text: str = 'Her name is Aqsa Aqsa'
# print(text.rstrip('Aqsa'))

#! 41
# text: str = 'Remember to read \nor else...\n'
# print(text.splitlines())

#! 42
# text: str = 'Aqsu'
# print(text.startswith('A'))

#! 43
# text: str = 'syed aqsa shah'
# print(text.strip('syed'))

#! 44
# text: str = 'halwa has pasta.'
# print(text.swapcase())

#! 45
# text: str = 'title'
# print(text.title())

#! 46
# text: str = 'hello aqsa'
# print(text.upper())

#! 47
# text: str = 'hello'
# print(text.zfill(10))




