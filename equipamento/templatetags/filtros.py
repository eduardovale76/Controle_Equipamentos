from datetime import date, datetime
from django import template

register = template.Library()

@register.filter
def mostra_duracao(value1, value2):
    #if isinstance(value1, datetime) and isinstance(value2, datetime): # Analisa a instancia dos dois valores. Se true realiza o calculo
    if all((isinstance(value1, date), isinstance(value2, date))):
        texto = (value1 - value2).days
        if texto == 1:
            return f'{texto} Dia.'
        else:
            return f'{texto} Dias.'
    else:
        return "Ainda não foi devolvido!"