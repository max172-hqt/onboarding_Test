from behave.fixture import use_fixture_by_tag, use_fixture
from features.fixtures import browser_setup, testing_email_setup, question_pools_setup
from custom_config import Config


fixture_registry = {
    "fixture.setup.browser": browser_setup,
    "fixture.setup.email": testing_email_setup,
    "fixture.setup.question_pool": question_pools_setup
}


def before_tag(context, tag):
    if tag.startswith("fixture."):
        use_fixture_by_tag(tag, context, fixture_registry)


def before_step(context, step):
    context.step = step


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        context.driver_wrapper.screen_shot(
            Config.get_current_date_time(),
            scenario.name,
            context.step.name
        )

# def before_feature(context, feature):
#     if feature.name == 'ExcelChat expert onboarding flow':
#         use_fixture(browser_setup, context)
