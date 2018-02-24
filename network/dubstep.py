from clove.network.bitcoin import Bitcoin


class Dubstep(Bitcoin):
    """
    Class with all the necessary Dubstep (DUB) network information based on
    https://github.com/dubsteproject/basscreator/blob/master/src/net.cpp
    (date of access: 02/23/2018)
    """
    name = 'dubstep'
    symbols = ('DUB', )
    seeds = ('52.26.103.164')
    port = 5494

# no testnet
