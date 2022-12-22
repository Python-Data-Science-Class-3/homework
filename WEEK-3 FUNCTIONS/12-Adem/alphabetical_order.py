#ALPHABETİCAL_ORDER
def alp_order():
    alp_order = (list(input("Enter elements with \"-\" sign between them.").split("-")))
    alp_order.sort()
    return ('-'.join(alp_order))
alp_order()