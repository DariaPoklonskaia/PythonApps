from unittest.loader import VALID_MODULE_NAME
import model_dev as model_dev
import model_mult
import view 

def buttun_click_dev():
    global value_a
    global value_b
    value_a = view.get_value()
    value_b = view.get_value()
    model_dev.init(value_a, value_b)
    result = model_dev.do_dev()
    view.view_data(result, "result_dev")

def buttun_click_mult():
    # value_a = view.get_value()
    # value_b = view.get_value()
    model_mult.init(value_a, value_b)
    result = model_mult.do_mult()
    view.view_data(result, "result_mult")