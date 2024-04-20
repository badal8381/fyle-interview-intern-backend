from core.libs.exceptions import FyleError
from core.libs.assertions import assert_auth, assert_found, assert_valid, assert_true, base_assert

def test_base_assert():
    try:
        base_assert(500, 'Test Base Assertion')
    except FyleError as e:
        assert e.status_code == 500
        assert e.message == 'Test Base Assertion'

def test_assert_auth():
    try:
        assert_auth(False, 'UNAUTHORIZED')
    except FyleError as e:
        assert e.status_code == 401
        assert e.message == 'UNAUTHORIZED'

def test_assert_found():
    try:
        assert_found(None, 'NOT_FOUND')
    except FyleError as e:
        assert e.status_code == 404
        assert e.message == 'NOT_FOUND'

def test_assert_valid():
    try:
        assert_valid(False, 'BAD_REQUEST')
    except FyleError as e:
        assert e.status_code == 400
        assert e.message == 'BAD_REQUEST'

def test_assert_true():
    try:
        assert_true(False, 'FORBIDDEN')
    except FyleError as e:
        assert e.status_code == 403
        assert e.message == 'FORBIDDEN'