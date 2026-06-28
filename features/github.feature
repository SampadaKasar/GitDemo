Feature: GitHub API validation

  Scenario: Session management check
    Given I have github auth credentials
    When I hit getRepo API of github
    Then status code of response should be 200