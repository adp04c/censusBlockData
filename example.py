from census import censusData

#initiate
a = censusData(28.35975,-81.421988)

#get all data
a.data()

#get census FIPS block number
a.block()

#get adjacent block numbers
a.intersection()

#get state 
a.state()

#get county
a.county()
