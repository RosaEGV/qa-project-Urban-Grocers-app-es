import sender_stand_request
import data
from data import kit_body


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    user_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_client_kit(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["name"] == name

def negative_assert_no_name(name):
    user_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400

def test_create_user_1_letter_in_name_get_success_response():
    positive_assert(data.kit_body_1)

def test_create_user_511_letter_in_name_get_success_response():
    positive_assert(data.kit_body_2)

def test_create_user_0_letter_in_name_get_error_response():
    negative_assert_no_name(data.kit_body_3)

def test_create_user_512_letter_in_name_get_error_response():
    negative_assert_no_name(data.kit_body_4)

def test_create_user_has_special_symbol_in_name_get_success_response():
    positive_assert(data.kit_body_5)

def test_create_user_empty_in_name_get_success_response():
    positive_assert(data.kit_body_6)

def test_create_user_has_number_in_name_get_success_response():
    positive_assert(data.kit_body_7)

def test_create_user_no_name_get_error_response():
    negative_assert_no_name(data.kit_body_8)

def test_create_user_number_type_name_get_error_response():
    negative_assert_no_name(data.kit_body_9)