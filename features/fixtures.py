from behave import fixture
from custom_config import Config
from manager.driver_factory import get_browser_wrapper
from admin_api_request.question_pool import QuestionPool
import time
import os


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


@fixture(name="fixture.clean.screenshot_dir")
def clean_screenshot_dir(context):
    screenshot_dir = Config.SCREEN_SHOT_DIR
    for the_file in os.listdir(screenshot_dir):
        file_path = os.path.join(screenshot_dir, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def _generate_email(context):
    current_timestamp = time.time()
    return context.config.userdata['test_email_format'].format(current_timestamp)
