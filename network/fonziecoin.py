from clove.network.bitcoin import Bitcoin


class Fonziecoin(Bitcoin):
    """
    Class with all the necessary Fonziecoin (FONZ) network information based on
    https://github.com/fonziecoin/fonzie/blob/master/src/net.cpp
    (date of access: 02/23/2018)
    """
    name = 'fonziecoin'
    symbols = ('FONZ', )
    seeds = ('66.172.12.80', '69.172.229.219')
    port = 1974

# no testnet
