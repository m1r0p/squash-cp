###### settings
##### old squash settings
OLD_SQUASH_BASE_URL="http://devx.kiev.ua:8030/squash"
OLD_SQUASH_PROJECTS_URL = OLD_SQUASH_BASE_URL + '/administration/projects'
OLD_SQUASH_CASES_URL = OLD_SQUASH_BASE_URL + '/test-case-workspace' 
OLD_SQUASH_USER="igor.matveyev"
OLD_SQUASH_PASS="q123456_"
#OLD_SQUASH_CASES_URL = 'http://' +  OLD_SQUASH_USER + ':' + OLD_SQUASH_PASS + '@' + 'devx.kiev.ua:8030/squash/test-case-workspace' 

##### new squash settings
NEW_SQUASH_BASE_URL="http://192.168.10.65:8080/squash"
#NEW_SQUASH_PROJECTS_URL = NEW_SQUASH_BASE_URL + '/administration-workspace/projects'
NEW_SQUASH_PROJECTS_URL = NEW_SQUASH_BASE_URL + '/api/rest/latest/projects?page=0&size=3 HTTP/1.1'
#OLD_SQUASH_CASES_URL = OLD_SQUASH_BASE_URL + '/test-case-workspace' 
NEW_SQUASH_USER="admin"
NEW_SQUASH_PASS="q123456_"

