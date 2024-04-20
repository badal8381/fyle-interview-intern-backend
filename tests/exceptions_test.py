from core.libs.exceptions import FyleError

def test_fyle_error():
    message = "Test Fyle Error"
    status_code = 400
    error = FyleError(status_code, message)
    
    # Check if the error object is initialized correctly
    assert error.message == message
    assert error.status_code == status_code
    

def test_fyle_error_to_dict():
    message = "Test Fyle Error"
    status_code = 400
    error = FyleError(status_code, message)
    fyle_dict = error.to_dict()
    assert fyle_dict['message'] == message