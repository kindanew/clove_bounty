from clove.network.bitcoin import Bitcoin


class Datacoin(Bitcoin):
    """
    Class with all the necessary Datacoin (DTC) network information based on
    https://github.com/foo1inge/datacoin-hp/blob/master/src/net.cpp
    (date of access: 02/23/2018)
    """
    name = 'datacoin'
    symbols = ('DTC', )
    seeds = ('87.247.9.5', '80.57.61.108')
    port = 4777

# no testnet
