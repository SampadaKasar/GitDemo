#In BDD workflow, we first write requirements in Gherkin inside feature files using Given-When-Then.
#Then we map those steps to Python step definitions in Behave. We use context to share data across steps, hooks in environment.py for setup and teardown,
# execute tests using Behave, and finally generate reports using tools like Allure.

#1. What is BDD?

# BDD (Behavior Driven Development) is a testing approach where requirements are written in business-readable language using Gherkin (Given/When/Then).
# It improves collaboration between QA, developers, and business teams.
#It focuses on describing software behavior in plain English using Gherkin:
#=====================================================================================
#2. Why use BDD for API testing?

# Better readability
# Non-technical stakeholders can understand tests
# Reusable step definitions
# Easier maintenance

# Instead of raw Python:
# response = requests.get(url)
# assert response.status_code == 200

# BDD:
# When I send GET request
# Then status code should be 200
#=====================================================================================
#3. What is a feature file?
#feature file contains scenarios written in Gherkin syntax.
# Example keywords:
# Feature
# Scenario
# Given
# When
# Then
# And
# But
#=====================================================================================
# 4. What are step definitions?

# Step definitions map Gherkin steps to Python functions using Behave decorators.

# @given('user id is {id}')
# def step_impl(context, id):
#     context.user_id = id
#=====================================================================================
#5. What is context in Behave?

# context is a shared object used to pass data between steps during scenario execution. To share data across steps inside a scenario
# context.response = response
#=====================================================================================

# 6. What is environment.py? Basically hooks
# for Setup/teardown, DB connections, auth tokens, reporting.
# It contains hooks executed before/after features or scenarios.
# Common hooks:
# before_all
# before_feature
# before_scenario
# after_scenario
# after_all

# def before_scenario(context, scenario):
#     context.base_url = "https://api.example.com"
#=====================================================================================

# 7. What are tags?

# Tags help run selective tests.
# behave --tags=smoke
#=====================================================================================

# 8. What is Scenario Outline? (Parameterization )-  Running same scenario with different inputs.
# Used for data-driven testing. Avoid duplicate scenarios.
# Scenario Outline: Validate users
#    Given user id is <id>
#    When I send request
#    Then status code should be 200
# Examples:
# | id |
# | 1  |
# | 2  |