def notas(*n, sit=False):
    r = {}
    r ["total"] = len(n)
    r ["menor"] = min(n)
    r ["maior"] = max(n)
    r ["media"] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r ['situação'] = "Boa!"
        elif r ['media'] >= 5:
            r ["situação"] = "Razoavél"
        else:
            r ["situação"] = 'Ruim'
    return r


resp = notas(5, 6, 8, 9,sit=True)
print(resp)
