import sender_stand_request
import data



def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    user_body = get_kit_body(name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["name"] == name

def negative_assert_no_name(name):
    user_body = get_kit_body(name)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400

def test_create_user_1_letter_in_name_get_success_response():
    positive_assert("a")

def test_create_user_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_user_0_letter_in_name_get_error_response():#EL NUMERO DE CARACTER ES CERO
    negative_assert_no_name("")

def test_create_user_512_letter_in_name_get_error_response():
    negative_assert_no_name("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_user_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")

def test_create_user_empty_in_name_get_success_response():
    positive_assert("A Aaa")

def test_create_user_has_number_in_name_get_success_response():
    positive_assert("123")

def test_create_user_no_name_get_error_response():#EL PARAMETRO NO SE PASA EN LA SOLICITUD Y SOLO DA ERROR 400
    kit_body_new = data.kit_body.copy()
    kit_body_new.pop("name")
    negative_assert_no_name(kit_body_new)

def test_create_user_number_type_name_get_error_response():#SE HA PASADO UN TIPO DE PARAMETRO DIFERENTE(NUMERO), ERROR 400
    kit_body_new = get_kit_body(12)
    response = sender_stand_request.post_new_user(kit_body_new)
    assert response.status_code == 400