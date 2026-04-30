import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("q", False),
        ("12345678", False),
        ("Password", False),
        ("P@ssw0rd", True),
        ("P@s1", False),
        ("P@ssw0rd123", True),
        ("p@ssw0rd", False),
        ("Passw@wrdpasswordpassword", False),
        ("abcdefgh", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
