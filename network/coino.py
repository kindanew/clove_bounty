from clove.network.bitcoin import Bitcoin


class CoinO(Bitcoin):
    """
    Class with all the necessary CoinO (CNO) network information based on
    https://github.com/scriptRack003756/coino/blob/master/src/net.cpp
    (date of access: 02/23/2018)
    """
    name = 'coino'
    symbols = ('CNO', )
    seeds = ('159.203.71.86')
    port = 29293

# no testnet
