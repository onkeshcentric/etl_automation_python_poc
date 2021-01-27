@local
Feature: ETL Tests Data Conformance
  Sample tests for ETL testing POC

  Background:
        Given I connect to source and destination databases

  Scenario: Check distinct count
    Then I fetch distinct count for "ID" in "members" table from "source" database
    Then I fetch distinct count for "ID" in "reports" table from "destination" database
    Then I validate the distinct count between tables "members" and "reports"

  @test
  Scenario: Check SSN
    Then I fetch all "SSN" in "members" table from "source" database
    Then I fetch all "SSN" in "reports" table from "destination" database
    Then I validate the column data between tables "members" and "reports"



