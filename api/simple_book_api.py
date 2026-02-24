from distutils.sysconfig import BASE_PREFIX

import requests
from common.config_reader import load_config

config = load_config()
BASE_URL = config["BASE_URL"]

class SimpleBookAPI:
    def delete_an_order(self, headers,order_id):
        url = f"{BASE_URL}/orders/{order_id}"
        return requests.delete(url,headers=headers)

    def patch_an_order(self, headers,order_id,customer_name):
        url = f"{BASE_URL}/orders/{order_id}"
        payload = {
              "customerName": customer_name
        }
        return requests.patch(url,headers=headers,json=payload)

    def get_order_by_orderId(self, headers,order_id):
        url = f"{BASE_URL}/orders/{order_id}"
        return requests.get(url,headers=headers)

    def post_register_api_clients(self, client_name, client_email):
        url = f"{BASE_URL}/api-clients"
        payload = {
            "clientName": client_name,
            "clientEmail": client_email
        }
        return requests.post(url, json=payload)

    def get_all_orders(self,headers):
        url = f"{BASE_URL}/orders"
        return requests.get(url, headers=headers)

    def post_order(self,headers, book_id, customer_name):
        url = f"{BASE_URL}/orders"
        payload = {
            "bookId": book_id,
            "customerName": customer_name
        }
        return requests.post(url,headers=headers,json=payload)


    def get_book_by_id(self, book_id):
        url = f"{BASE_URL}/books/{book_id}"
        return requests.get(url)

    def get_books(self, params = None):
        """
        params: dict 可选参数, 会被requests自动转换成query string
        例如: {"type": "fiction", "author": "Tom"}
        """
        url = f"{BASE_URL}/books"
        return requests.get(url, params=params)

    def get_status(self):
        url = f"{BASE_URL}/status"
        return requests.get(url)