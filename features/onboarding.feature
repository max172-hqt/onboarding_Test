Feature: ExcelChat expert onboarding flow
  """
  Precondition
  - Set up mocking pre-exist pool using API requests to Admin Panel
  """

  @fixture.setup.question_pool
  @fixture.setup.browser
  @fixture.setup.email
  Scenario Outline: User Signup and onboarding
    Given I am on Expert Landing page
    When I sign up
    Then I am on Email Verification modal
    When I verify my email
    And I accept Terms and Conditions
    Then I am on Welcome page
    When I "pass" Policy Test
    Then I am on Subject Test page
    When I "<action>" Core Excel Test
#    Then I am on "<result>" page

    Examples:
      | action | result   |
      | pass   | Success  |
      | fail   | Failed   |
