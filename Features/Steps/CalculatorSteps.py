import time

from behave import *

use_step_matcher("parse")


@given('User is on "{current_page}" homepage')
def user_is_on_current_page(context, current_page):
    print(f"User is on {current_page} home page")
    # time.sleep(5)


@when('User clicks on "{number}"')
def user_clicks_on_number(context, number):
    context.android.tap_number(number)


@when('User clicks on operator "{opt}"')
def user_clicks_on_operator(context, opt):
    context.android.tap_operator(opt)


@then('User verifies answer is "{ans}"')
def user_verifies_answer(context, ans):
    context.android.verify_answer(ans)
