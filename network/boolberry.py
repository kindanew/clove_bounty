from clove.network.bitcoin import Bitcoin


class Boolberry(Bitcoin):
    """
    Class with all the necessary Boolberry (BBR) network information based on
    https://github.com/cryptozoidberg/boolberry/blob/master/src/p2p/net_node.inl
    (date of access: 02/23/2018)
    """
    name = 'boolberry'
    symbols = ('BBR', )
    seeds = ('88.99.193.104', '138.201.126.98')
    port = 10101

# no testnet
