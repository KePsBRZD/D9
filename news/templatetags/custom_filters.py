from django import template

register = template.Library()


@register.filter()
def censor(value):
    swear_words = ('редиска', 'редиску', 'Бля', 'бля', 'Бля.', '.Бля', 'Бля,', 'Бля?', 'Бля!', '.бля', 'бля.', 'бля?', 'бля!', 'бля,', 'Бля:')

    if not isinstance(value, str):
        raise TypeError(f"unresolved type '{type(value)}' expected  type 'str'")

    for word in value.split():
        if word.lower() in swear_words:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 2)}{word[-1]}")
    return value



#{% load custom_filters %} в news.html  и |censor