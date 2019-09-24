from behave import *
from custom_config import Config
from libs.account_kit import background_run

from pom.sign_up.landing_page import LandingPage
from pom.sign_up.signin_modal import SigninComponent

from pom.onboarding.subject_test_page import SubjectTestPage
from pom.onboarding.question_page import QuestionPage
from pom.onboarding.video_page import VideoPage
from pom.onboarding.pass_test_page import PassTestPage
from pom.onboarding.fail_test_page import FailTestPage
from pom.onboarding.welcome_page import WelcomePage

from pom.sign_up.email_verification_modal import EmailVerificationModal
from pom.sign_up.term_and_condition_modal import TermAndConditionModal


@given('I am on Expert Landing page')
def step_impl(context):
    context.driver_wrapper.open(Config.BASE_EXPERT_URL)
    landing_page = LandingPage(context.driver_wrapper)
    landing_page.open_login_modal()


@when("I sign up")
def step_impl(context):
    signin_modal = SigninComponent(context.driver_wrapper)
    signin_modal.sign_up(
        context.test_email,
        context.config.userdata['test_password']
    )


@then('I am on Email Verification modal')
def step_impl(context):
    email_verification = EmailVerificationModal(context.driver_wrapper)
    email_verification.send_email_verification()


@when('I verify my email')
def step_impl(context):
    background_run()


@when('I accept Terms and Conditions')
def step_impl(context):
    term_and_condition = TermAndConditionModal(context.driver_wrapper)
    term_and_condition.click_next()


@then('I am on Welcome page')
def step_impl(context):
    welcome_page = WelcomePage(context.driver_wrapper)
    welcome_page.start_onboarding_test()


@when('I "pass" Policy Test')
def step_impl(context):
    video_page = VideoPage(context.driver_wrapper, check_is_displayed=False)
    question_page = QuestionPage(context.driver_wrapper, check_is_displayed=False)
    pass_page = PassTestPage(context.driver_wrapper, check_is_displayed=False)

    for i in range(Config.NUM_MINI_POLICY_TESTS):
        video_page.is_displayed()
        video_page.watch_video()

        question_page.is_displayed()
        question_page.answer_test()

        pass_page.is_displayed()
        pass_page.click_continue()


@then('I am on Subject Test page')
def step_impl(context):
    subject_test_page = SubjectTestPage(context.driver_wrapper)
    subject_test_page.start_excel_core()


@when('I "{action}" Core Excel Test')
def step_impl(context, action):
    question_page = QuestionPage(context.driver_wrapper, check_is_displayed=False)

    if action == 'pass':
        question_page.answer_test(answer_correct=True)
    else:
        question_page.answer_test(answer_correct=False)


@then('I am on "{result}" page')
def step_impl(context, result):
    pass_page = PassTestPage(context.driver_wrapper, check_is_displayed=False)
    fail_page = FailTestPage(context.driver_wrapper, check_is_displayed=False)

    if result == 'Success':
        pass_page.is_displayed()
    else:
        fail_page.is_displayed()


