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


@when('I am on Email Verification modal')
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


@then('I should see Welcome page')
def step_impl(context):
    welcome_page = WelcomePage(context.driver_wrapper)
    assert welcome_page.is_displayed()


@when('I click next')
def step_impl(context):
    welcome_page = WelcomePage(context.driver_wrapper)
    welcome_page.start_onboarding_test()


@when('I "pass" Policy Test')
def step_impl(context):
    for i in range(Config.NUM_MINI_POLICY_TESTS):
        video_page = VideoPage(context.driver_wrapper)
        video_page.watch_video()

        question_page = QuestionPage(context.driver_wrapper)
        question_page.answer_test()

        pass_page = PassTestPage(context.driver_wrapper)
        pass_page.click_continue()


@then('I should see Subject Test page')
def step_impl(context):
    subject_test_page = SubjectTestPage(context.driver_wrapper)
    assert subject_test_page.is_displayed()


@when(u'I start Core Excel Test')
def step_impl(context):
    subject_test_page = SubjectTestPage(context.driver_wrapper)
    subject_test_page.start_excel_core()


@when('I start Excel Core Test')
def step_impl(context):
    subject_test_page = SubjectTestPage(context.driver_wrapper)
    subject_test_page.start_excel_core()


@when('I "{action}" Core Excel Test')
def step_impl(context, action):
    question_page = QuestionPage(context.driver_wrapper)

    if action == 'pass':
        question_page.answer_test(answer_correct=True)
    elif action == 'fail':
        question_page.answer_test(answer_correct=False)
    else:
        assert False, "Action not valid"


@then('I should see "{result}" page')
def step_impl(context, result):
    if result == 'Success':
        pass_page = PassTestPage(context.driver_wrapper)
        assert pass_page.is_displayed()
    elif result == 'Failed':
        fail_page = FailTestPage(context.driver_wrapper)
        assert fail_page.is_displayed()
    else:
        assert False, "Page name is invalid"



