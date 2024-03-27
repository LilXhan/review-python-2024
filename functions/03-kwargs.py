# keyword arguments

def get_product(**data):
    print(data['id'])
    print(data['name'])
    print(data['descp'])

get_product(id=1,
            name='Iphone',
            descp='This is a iphone')