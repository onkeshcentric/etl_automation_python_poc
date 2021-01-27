# ETL Automation POC using Python
ETL Automation POC using Python

## BDD Approach
Implemented using behave
To execute all the BDD scenarios in the framework, simply use the command: `behave`

To execute specific feature file, use the command: 

`behave <relative path to feature file>:<scenario line number>`

### ETL Scenarios categories implemented
- Data Conformance
- Data Reconciliation
- Data Transformation

### Executing Specific Scenarios
Behave has support for custom cucumber tags and anyone can execute any specific test using the command 

`behave -t <tag_name>`

For example, user can execute the following command to run on both local and remote DB tests: 

`behave -t @local,@remote`

### Reporting

Current reporting is being done using allure reports.
The execution command changes into: 

`behave -f allure_behave.formatter:AllureFormatter -o reports ./features`

To view the reports, execute the following command: `allure serve reports`