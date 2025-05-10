#Challenge 4: Email verifier

from typing import List
import re

#user_input = input("Enter an email: ")
test_emails: List[str] = ["test@email.com", "test_email@email.com", "nomail.com", "a@a.A", "abcdefg@mail", "donut", "aaa@aaa.aaa", ".asdfi_+saf@email.com", "user@mail.com.com.com"]
reg_ex: str = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"

for mail in test_emails:
    if re.fullmatch(reg_ex, mail.lower()):
        print(f"\'{mail}\': valid")
    else:
        print(f"\'{mail}\': not valid")