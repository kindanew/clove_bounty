from clove.network.bitcoin import Bitcoin


class TAGRcoin(Bitcoin):
    """
    Class with all the necessary TAGRcoin network information based on
    https://github.com/tagrdev/tagrcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'tagrcoin'
    symbols = ('TAGR', )
    seeds = ("195.34.100.2", "212.91.189.164")
    port = 18885


# Has no testnet