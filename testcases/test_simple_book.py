from http.client import responses

import pytest
import requests
from api.simple_book_api import SimpleBookAPI
from faker import Faker
import time

api = SimpleBookAPI()

@pytest.mark.smoke
def test_order_flow():
    #获取api状态
    response = api.get_status()
    print("获取接口状态")
    print(response.status_code)
    print(response.json())
    assert response.json()["status"] == "OK","Check status"

    #注册一个token
    email = f"pytest_{int(time.time())}@gmail.com"
    response = api.post_register_api_clients(
        client_email=email,
        client_name="luke"
    )
    print("注册一个token")
    print(response.status_code)
    token = response.json().get("accessToken")
    print(token)

    #获取non-fiction的书本第一本available的书的id
    response = api.get_books(params={"type": "non-fiction"})
    print("查找书本列表")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    for book in response.json():
        if book["available"] is True:
            book_id = book["id"]
            break
    print(book_id)
    for book in response.json():
        if book["id"] == book_id:
            assert book["type"] == "non-fiction"

    #获取单本书的信息
    response = api.get_book_by_id(book_id)
    print("用id获取书本")
    print(response.status_code)
    print(response.json())
    #assert response.json()["id"] == book_id
    assert response.json()["current-stock"] >= 1

    #预定一本书
    fake = Faker()
    name = fake.name()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = api.post_order(headers=headers,book_id=book_id,customer_name= name)
    print("Body:", response.request.body)
    print("预定书本")
    print(response.status_code)
    print(response.json())
    order_id = response.json().get("orderId")

    #查询单个order
    response = api.get_order_by_orderId(headers = headers,order_id = order_id)
    print("查询一个订单详情")
    print(response.status_code)
    print(response.json())
    assert response.json()["id"] == order_id

    #修改一个name
    new_name = "Luke Huang"
    response = api.patch_an_order(headers = headers,order_id = order_id,customer_name = new_name)
    print("修改订单名称")
    print(response.status_code)
    response = api.get_order_by_orderId(headers = headers,order_id = order_id)
    print("查询一个订单详情")
    print(response.status_code)
    print(response.json())
    assert response.json()["customerName"] == new_name

    #删除订单
    response = api.delete_an_order(headers = headers,order_id = order_id)
    print("删除订单")
    print(response.status_code)
    response = api.get_order_by_orderId(headers = headers,order_id = order_id)
    print("查询一个订单详情")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 404

    # 定义时间格式：年-月-日 时:分:秒
    time_format = "%Y-%m-%d %H:%M:%S"
    # 获取当前时间戳并格式化为指定字符串
    current_time_str = time.strftime(time_format)
    print("execute one" + current_time_str)


def test_delete_an_order():
    headers = {
        "Authorization": f"Bearer 6d5331c3f6fc4915a4c32a516b01ccd3f840b4f9f2b0a06d12a2b0af79456638"
    }
    order_id = "AUXgxAlAzd1cHT-PLPG0s"
    response = api.delete_an_order(headers = headers,order_id = order_id)
    print(response.status_code)
    #print(response.json())
    #assert response.json()["id"] == order_id

def test_patch_an_order():
    fake = Faker()
    name = fake.name()
    headers = {
        "Authorization": f"Bearer 6d5331c3f6fc4915a4c32a516b01ccd3f840b4f9f2b0a06d12a2b0af79456638"
    }
    order_id = "AUXgxAlAzd1cHT-PLPG0s"
    customer_name = name
    response = api.patch_an_order(headers = headers,order_id = order_id,customer_name = customer_name)
    print(response.status_code)
    #print(response.json())
    #assert response.json()["id"] == order_id

def test_get_an_order():
    headers = {
        "Authorization": f"Bearer 6d5331c3f6fc4915a4c32a516b01ccd3f840b4f9f2b0a06d12a2b0af79456638"
    }
    order_id = "AUXgxAlAzd1cHT-PLPG0s"
    response = api.get_order_by_orderId(headers = headers,order_id = order_id)
    print(response.status_code)
    print(response.json())
    assert response.json()["id"] == order_id

def test_get_all_orders():

    headers = {
        "Authorization": f"Bearer 6d5331c3f6fc4915a4c32a516b01ccd3f840b4f9f2b0a06d12a2b0af79456638"
    }
    response = api.get_all_orders(headers=headers)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


def test_post_orders(token):
    fake = Faker()
    name = fake.name()
    #headers = {
    #    "Authorization": f"Bearer {token}"
    #}
    headers = {
        "Authorization": f"Bearer 6d5331c3f6fc4915a4c32a516b01ccd3f840b4f9f2b0a06d12a2b0af79456638"
    }
    response = api.post_order(headers=headers,book_id=3,customer_name= name)
    print("Body:", response.request.body)
    print(response.status_code)
    print(response.json())
    #assert response.status_code == 200

def test_get_book_by_id():
    book_id = 2
    response = api.get_book_by_id(book_id)
    print(response.status_code)
    print(response.json())
    assert response.json()["id"] == book_id

def test_get_fiction_books():
    response = api.get_books(params={"type": "fiction","limit": 2})
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    # 可以加断言检查返回内容
    for book in response.json():
        assert book["type"] == "fiction"

def test_get_books():
    response = api.get_books()
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200




def test_get_status():
    response = api.get_status()
    # 打印返回结果
    print(response.status_code)
    print(response.json())
    assert response.json()["status"] == "OK","Check status"
    # 断言
    assert response.status_code == 200
    #assert response.json()["id"] == 1