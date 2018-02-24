from clove.network.bitcoin import Bitcoin


class Avoncoin(Bitcoin):
    """
    Class with all the necessary Avoncoin (ACN) network information based on
    https://github.com/acncoin/Avoncoin-Project/blob/master/src/net.cpp
    (date of access: 02/23/2018)
    """
    name = 'avoncoin'
    symbols = ('ACN', )
    seeds = ('68.65.120.48')
    port = 5797

# no testnet
