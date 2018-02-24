from clove.network.bitcoin import Bitcoin


class Electroneum(Bitcoin):
    """
    Class with all the necessary Electroneum (ETN) network information based on
    https://github.com/electroneum/electroneum/blob/master/src/p2p/net_node.inl
    (date of access: 02/23/2018)
    """
    name = 'electroneum'
    symbols = ('ETN', )
    seeds = ('13.125.37.208', 
			 '13.125.50.165',
			 '13.124.43.88',
			 '34.250.126.109',
			 '52.50.2.110',
			 '34.240.247.44',
			 '34.237.39.232',
			 '34.236.180.233',
			 '34.197.74.127')
    port = 26967

# no testnet
