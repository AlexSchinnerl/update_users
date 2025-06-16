# Update User Roles
## Goal
We want to update the user roles in Alma via an API-call. On this way, we are able to roll out user profiles on multiple users without going to the process of open each user separately.
## How it works
The program uses the [keyring library](https://pypi.org/project/keyring/) to work with the [Alma API](https://developers.exlibrisgroup.com/console/) (Users and Fulfillment).

It uses the user_id (in our case AK-Number) to get the user details.

Afterwards it erases all user roles

In the next step the program reads input xml files that contain a set of new user roles and adds the new roles to the existing user details.

In the last step the newly created user xml ist updated in the Alma system via another API call.

**Note!** Some Fields are filled with features, specially tailored to meet the needs of the JKU and would need adaptation if used in a different university.

# How to run
## keyring preperations
* Store your API key in the keyring library.
* Change the content of the ```getAPIkey``` function to your own specifications.

## input files
There are two input files:
* The input_akNumbers.txt stores the user_id(s) you want to modify
* The input_roles

