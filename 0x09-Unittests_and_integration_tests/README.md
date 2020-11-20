# 0x09. Unittests and Integration Tests

## Resources:books:
Read or watch:
* [unittest — Unit testing framework](https://intranet.hbtn.io/rltoken/CZk1PZz753_Dz-0IoyGiyA)
* [unittest.mock — mock object library](https://intranet.hbtn.io/rltoken/QEQFuhCQnu--N3p-K2jL2Q)
* [How to mock a readonly property with mock?](https://intranet.hbtn.io/rltoken/jPX7moqAyFOKcP-Es1R5LQ)
* [parametrized](https://intranet.hbtn.io/rltoken/GkU3bOnYHUtRWGSKmuSQyg)
* [Memoization](https://intranet.hbtn.io/rltoken/bdcbwegwwMOr1QZJIwAMsw)

---
## Learning Objectives:bulb:
What you should learn from this project:
* The difference between unit and integration tests.
* Common testing patterns such as mocking, parametrizations and fixtures

---

### [0. Parameterize a unit test](./test_utils.py)
* Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.


### [1. Parameterize a unit test](./test_utils.py)
* Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parametrized.expand):


### [2. Mock HTTP calls](./test_utils.py)
* Familiarize yourself with the utils.get_json function.


### [3. Parameterize and patch](./test_utils.py)
* Read about memoization and familiarize yourself with the utils.memoize decorator.


### [4. Parameterize and patch as decorators](./test_client.py)
* Familiarize yourself with the client.GithubOrgClient class.


### [5.  Mocking a property](./test_client.py)
* memoize turns methods into properties. Read up on how to mock a property (see resource).


### [6. More patching](./test_client.py)
* Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.


### [7. Parameterize](./test_client.py)
* Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.


### [8. Integration test: fixtures](./test_client.py)
* We want to test the GithubOrgClient.public_repos method in an integration test. That means that we will only mock code that sends external requests.


### [9. Integration tests](./test_client.py)
* Implement the test_public_repos method to test GithubOrgClient.public_repos.

---

## Author
* **Brent Muha** - [bmuha1](github.com/bmuha1)