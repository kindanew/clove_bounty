from clove.network.bitcoin import Bitcoin


class Ecoin(Bitcoin):
    """
    Class with all the necessary ECN network information based on
    https://github.com/ecoinclub/ecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'ecoin'
    symbols = ('ECN', )
    seeds = (
        '138.68.164.92',
        'ecnblockchain.com',
        '72.52.156.4',
        '72.52.156.87',
    )
    port = 18741


class EcoinTestNet(Ecoin):
    """
    Class with all the necessary ECN testing network information based on
    https://github.com/ecoinclub/ecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-ecoin'
    seeds = ()
    port = 17778
