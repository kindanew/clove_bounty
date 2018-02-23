from clove.network.bitcoin import Bitcoin


class DarkLisk(Bitcoin):
    """
    Class with all the necessary DarkLisk (DISK) network information based on
    https://github.com/diskdev/disk/blob/master/src/net.cpp
    (date of access: 02/23/2018)
    """
    name = 'darklisk'
    symbols = ('DISK', )
    seeds = ('223.75.211.121',
			 '121.52.210.155',
			 '38.188.2.173',
			 '122.183.67.173',
			 '10.179.167.188',
			 '55.90.181.188',
			 '201.11.22.23',
			 '83.82.253.23',
			 '94.252.108.24',
			 '204.220.125.24',
			 '68.61.145.24',
			 '132.3.27.24',
			 '52.124.30.24',
			 '134.81.36.24',
			 '252.254.144.49',
			 '219.94.185.54',
			 '239.141.46.58',
			 '207.81.242.60',
			 '24.171.102.62',
			 '54.224.223.64',
			 '222.72.182.65',
			 '173.62.78.65',
			 '208.243.43.68',
			 '9.115.59.68',
			 '106.81.245.69',
			 '229.147.239.72',
			 '197.245.239.72',
			 '150.244.241.72',
			 '211.84.211.74',
			 '54.32.111.76',
			 '206.239.233.83',
			 '80.70.140.85',
			 '137.211.141.85',
			 '101.230.26.90',
			 '22.177.185.93',
			 '112.43.19.94',
			 '15.87.36.94',
			 '218.171.95.95',
			 '186.21.239.99')
    port = 7612

# no testnet
