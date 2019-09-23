from behave import *
from pom.pages.landing_page.landing_page import LandingPage
from pom.pages.onboarding_page.onboarding_page import OnboardingPage
from pom.modals.email_verification_modal import EmailVerificationModal
from pom.modals.term_and_condition_modal import TermAndConditionModal


@given('I am on Expert Landing page')
def step_impl(context):
    landing_page = LandingPage(context.driver_wrapper)
    landing_page.open()
    landing_page.is_displayed()
    landing_page.click_login()
    context.landing_page = landing_page


@when("I sign up")
def step_impl(context):
    landing_page = context.landing_page
    landing_page.sign_up(
        context.test_email,
        context.config.userdata['test_password']
    )


@then('I am on Email Verification modal')
def step_impl(context):
    email_verification = EmailVerificationModal(context.driver_wrapper)
    email_verification.is_displayed()
    context.email_verification = email_verification


@when('I verify my email')
def step_impl(context):
    context.email_verification.verify_email()


@when('I accept Terms and Conditions')
def step_impl(context):
    term_and_condition = TermAndConditionModal(context.driver_wrapper)
    term_and_condition.is_displayed()
    term_and_condition.click_next()


@then('I am on Welcome page')
def step_impl(context):
    onboarding = OnboardingPage(context.driver_wrapper)
    # onboarding.is_displayed()

