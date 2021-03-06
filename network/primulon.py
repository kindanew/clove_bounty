from clove.network.bitcoin import Bitcoin


class Primulon(Bitcoin):
    """
    Class with all the necessary Primulon network information based on
    https://github.com/primulondev2/primu2/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'primulon'
    symbols = ('PRIMU', )
    seeds = ("198.136.28.100")
    port = 19667


# Has no testnet