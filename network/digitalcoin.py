
from clove.network.bitcoin import Bitcoin


class Digitalcoin(Bitcoin):
    """
    Class with all the necessary DGC network information based on
    http://www.github.com/lomtax/digitalcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'digitalcoin'
    symbols = ('DGC', )
    seeds = ('digitalcoin.co', 'game.digitalcoin.co', 'dev.digitalcoin.co', '178.62.28.81')
    port = 7999


class DigitalcoinTestNet(Digitalcoin):
    """
    Class with all the necessary DGC testing network information based on
    http://www.github.com/lomtax/digitalcoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-digitalcoin'
    seeds = ('seed3.digihash.co', 'seed4.love2hash.com', 'seed5.digiexplorer.info')
    port = 12025
