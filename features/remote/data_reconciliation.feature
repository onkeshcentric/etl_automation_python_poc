@remote
Feature: ETL Tests Data Reconciliation on Remote DB
  Sample tests for ETL testing POC

    Background:
        Given I connect to the remote source and destination databases

  Scenario: Check count between source and destination
    Then I fetch count for "members" table from "source" database
    Then I fetch count for "stateclaims" table from "destination" database
    Then I validate the count between tables "members" and "stateclaims"