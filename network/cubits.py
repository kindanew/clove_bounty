from clove.network.bitcoin import Bitcoin


class Cubits(Bitcoin):
    """
    Class with all the necessary Cubits (QBT) network information based on
    https://github.com/scificrypto/cubitsv3/blob/master/src/net.cpp
    (date of access: 02/23/2018)
    """
    name = 'cubits'
    symbols = ('QBT', )
    seeds = ('88.9.157.217')
    port = 17433

# no testnet
