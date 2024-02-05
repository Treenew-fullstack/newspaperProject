from django import template


register = template.Library()

bad_words = ['6ля', '6лядь', '6лять', 'b3ъeб', 'cock', 'cunt', 'e6aль', 'ebal', 'eblan', 'eбaл', 'eбaть', 'eбyч', 'eбать', 'eбёт', 'eблантий',
             'fuck', 'fucker', 'fucking', 'xyёв', 'xyй', 'xyя', 'xуе','xуй', 'xую', 'zaeb', 'zaebal', 'zaebali', 'zaebat', 'архипиздрит', 'ахуел, ']



@register.filter()
def censor(text):
    for word in bad_words:
        text = text.replace(word[1:], '*' * len(word[1:]))
    return text
