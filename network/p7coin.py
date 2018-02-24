from clove.network.bitcoin import Bitcoin


class P7Coin(Bitcoin):
    """
    Class with all the necessary P7Coin (DTC) network information based on
    https://github.com/p7coin/source/blob/master/src/net.cpp
    (date of access: 02/23/2018)
    """
    name = 'p7coin'
    symbols = ('P7C', )
    seeds = ('225.149.199.33', '49.211.161.66')
    port = 3954

# no testnet
