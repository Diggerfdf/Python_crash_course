def describe_city(name, country='Brasil'):
    print("\n{} is in {}".format(name, country))
    
describe_city('São Paulo')
describe_city('Curitiba')
describe_city('Tokyo', country='Japan')
describe_city('Nagoya', 'Japan')
