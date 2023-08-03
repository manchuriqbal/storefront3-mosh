from locust import HttpUser, task, between
from random import randint


class WebsiteTest(HttpUser):
    wait_time= between(1,5)
    # View products
    @task(2)
    def view_products(self):
        collection_id = randint(2,6)
        self.client.get(
            f'/store/products/?collection_id{collection_id}/', 
            name= '/store/products'
            )
        
    # View Product deatils
    @task(4)
    def view_product(self):
        product_id = randint(1, 1000)
        self.client.get(
            f'/store/products/{product_id}',
            name = '/store/products/:id'
            )
        
    # add to cart
    @task(1)
    def add_to_cart(self):
        product_id =randint(1, 10)
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name = '/store/carts/items',
            json= {'product_id': product_id, 'quantity': 1}
            )
    
    @task 
    def say_hello(self):
        self.client.get('/playground/hello/')

    def on_start(self):
        respons = self.client.post('/store/carts/')
        result = respons.json()
        self.cart_id = result['id']