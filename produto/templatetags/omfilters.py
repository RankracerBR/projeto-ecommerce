from django.template import Library
from utils import utils

register = Library()


@register.filter
def formata_preco(val):
    return utils.formata_preco

@register.filter
def cart_total_qtd(carinho):
    return utils.cart_total_qtd(carinho)

@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)