from math import log2, ceil

def sfe(prob):
    syms = list(prob.keys())

    def mcf(i):
        a = sum(prob[k] for k in syms[:i])
        b = prob[syms[i]] / 2
        return a + b

    def len(symbol):
        p = prob[symbol]
        return ceil(-log2(p)) + 1

    def code(x, n):
        x = round(x, 8)
        assert(0 <= x <= 1)
        if x == 1:
            return '0' * n

        z = ''
        for i in range(1, n+1):
            if x >= pow(2, -i):
                x -= pow(2, -i)
                z += '1'
            else:
                z += '0'
        return z

    return {symbol: code(mcf(i), len(symbol)) for i, symbol in enumerate(syms)}
