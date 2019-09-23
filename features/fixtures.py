from behave import fixture
from manager.driver_factory import get_browser_wrapper
from admin_api_request.question_pool import QuestionPool
import time


@fixture(name="fixture.setup.browser")
def browser_setup(context):
    context.driver_wrapper = get_browser_wrapper(context.config.userdata['browser'])
    yield context.driver_wrapper
    context.driver_wrapper.shutdown()


@fixture(name="fixture.setup.email")
def testing_email_setup(context):
    context.test_email = _generate_email(context)
    yield context.test_email


@fixture(name="fixture.setup.question_pool")
def question_pools_setup(context):
    context.question_pool = QuestionPool()
    context.question_pool.update_all_tests()
    yield context.question_pool
    context.question_pool.reset_all_tests()


def _generate_email(context):
    current_timestamp = time.time()
    return context.config.userdata['test_email_format'].format(current_timestamp)
