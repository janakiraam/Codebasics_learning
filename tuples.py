'''
contact =[('raam',1),('janaki',2),('ravi',3)]
for contacts in contact:
    if contacts[0]=='janaki':
        print(contacts[1])
        '''

# nested dictionary

appl_revenues = {
    "USA" : {
        "iphone" : 20,
        "ipdaa"  : 30,
        "macbook" : 8
    },
    "china": {
        "iphone":40,
        "ipad" : 20,
        "mac" : 400,

    }
}

for country in appl_revenues:
    print(country) # print only keys

for country,product in appl_revenues.items():
    for product_datra, rev in product.items():
        print(f"{country} {product_datra} revnue: {rev} $million dollars") 