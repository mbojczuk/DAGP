# Workflows testing framework

The idea is you just expand as many tests in the wrapper as you want and then on a PR it will print out errors to users

If you wanna change the tests then in the workflow yaml.

line 42: python "${TEST_WRAPPER_DIR}/${MAIN_RUNNER}" > "${LOG_PATH}" 2>&1 || true
the main test also expects test names in a list so

python "${TEST_WRAPPER_DIR}/${MAIN_RUNNER}" --tests hello,some_name,whatever > "${LOG_PATH}" 2>&1 || true