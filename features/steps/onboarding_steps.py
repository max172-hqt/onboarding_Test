from behave import *
from pom.pages.onboarding_page.onboarding_page import OnboardingPage
from pom.pages.subject_test_page.subject_test_page import SubjectTestPage


@when('I "pass" Policy Test')
def step_impl(context):
    onboarding_page = OnboardingPage(context.driver_wrapper)
    onboarding_page.start_onboarding_test()
    onboarding_page.pass_policy_test()
    context.onboarding_page = onboarding_page


@then('I am on Subject Test page')
def step_impl(context):
    subject_test_page = SubjectTestPage(context.driver_wrapper)
    subject_test_page.is_displayed()
    context.subject_test_page = subject_test_page


@when('I "{action}" Core Excel Test')
def step_impl(context, action):
    subject_test_page: SubjectTestPage = context.subject_test_page
    onboarding_page: OnboardingPage = context.onboarding_page
    subject_test_page.start_excel_core()
    if action == 'pass':
        onboarding_page.perform_excel_core_test()
    else:
        onboarding_page.perform_excel_core_test(passing=False)


@then('I am on "{result}" page')
def step_impl(context, result):
    onboarding_page: OnboardingPage = context.onboarding_page
    subject_test_page: SubjectTestPage = context.subject_test_page
    if result == 'Success':
        subject_test_page.is_displayed()
    else:
        onboarding_page.is_fail_page_displayed()




