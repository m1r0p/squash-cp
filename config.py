###### settings
##### old squash settings
OLD_SQUASH_BASE_URL="http://<ip_or_name>:8030/squash"
OLD_SQUASH_PROJECTS_URL = OLD_SQUASH_BASE_URL + '/administration/projects'
OLD_SQUASH_USERS_URL = OLD_SQUASH_BASE_URL + '/administration/users/list'
OLD_SQUASH_REQ_URL = OLD_SQUASH_BASE_URL + '/requirement-workspace'
OLD_SQUASH_CASES_URL = OLD_SQUASH_BASE_URL + '/test-case-workspace'
OLD_SQUASH_CAMP_URL = OLD_SQUASH_BASE_URL + '/campaign-workspace'

OLD_SQUASH_USER="<user1>"
OLD_SQUASH_PASS="<pass1>"
DOMAIN = "<domain>"
#OLD_SQUASH_CASES_URL = 'http://' +  OLD_SQUASH_USER + ':' + OLD_SQUASH_PASS + '@' + DOMAIN + ':8030/squash/test-case-workspace'
OLD_SQUASH_REQ_LIB = 'RequirementLibrary-'
OLD_SQUASH_REQ_FOL = 'RequirementFolder-'
OLD_SQUASH_CASES_LIB = 'TestCaseLibrary-'
OLD_SQUASH_CASES_FOL = 'TestCaseFolder-'
OLD_SQUASH_CAMP_LIB = 'RequirementLibrary-'
OLD_SQUASH_CAMP_FOL = 'RequirementFolder-'

##### new squash settings
NEW_SQUASH_BASE_URL="http://<ip_or_name>:8080/squash"
NEW_SQUASH_PROJECTS_URL = NEW_SQUASH_BASE_URL + '/api/rest/latest/projects'
NEW_SQUASH_GET_PR_URL = NEW_SQUASH_PROJECTS_URL + '?page=0&size=100'
NEW_SQUASH_USER="<user2>"
NEW_SQUASH_PASS="<pass2>"

