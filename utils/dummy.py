import json

# party dummies
party = json.dumps(dict(
    id=1,
    name="Blue",
    hqAddress="Memphis",
    logoUrl="blue.img"
))

party_edit_data = json.dumps(dict(
    id=1,
    name="Red",
    hqAddress="Addis",
    logoUrl="red.img"
))

party_missing_name_key = json.dumps(dict(
    id=1,
    hqAddress="Addis",
    logoUrl="red.img"
))

party_blank_name = json.dumps(dict(
    id=1,
    name="",
    hqAddress="Belgrade",
    logoUrl="logo.png"
))

party_blank_hqAddress = json.dumps(dict(
    id=1,
    name="Jubilee",
    hqAddress="",
    logoUrl="logo.png"
))

party_blank_logoUrl = json.dumps(dict(
    id=1,
    name="Jubilee",
    hqAddress="Kent",
    logoUrl=""
))

party_non_string_name = json.dumps(dict(
    id=1,
    name=5,
    hqAddress="Kent",
    logoUrl="kent.png"
))

party_non_string_hqAddress = json.dumps(dict(
    id=1,
    name="Jubilee",
    hqAddress=7,
    logoUrl="kent.png"
))

empty_data_party = json.dumps(dict(

))

# office dummies
office = json.dumps(dict(
    id=1,
    officeType="National",
    name="Presidential"
))

office_missing_name_key = json.dumps(dict(
    id=1,
    officeType="National"
))
office_empty_body = json.dumps(dict(

))

office_empty_type = json.dumps(dict(
    id=1,
    officeType="",
    name="Presidential"
))

office_empty_name = json.dumps(dict(
    id=1,
    officeType="National",
    name=""
))

non_string_office_name = json.dumps(dict(
    id=1,
    officeType="National",
    name=5
))

non_string_office_type = json.dumps(dict(
    id=1,
    officeType=5,
    name="Presidential"
))


# user dummies

admin_user = json.dumps(dict(
    id=1,
    firstName='John',
    lastName='Doe',
    otherName='Laurient',
    email='doe@politico.com',
    phoneNumber='0765234234',
    passportUrl='image.png',
    password="admin123"
))

user = json.dumps(dict(
    id=2,
    firstName='Jane',
    lastName='Doe',
    otherName='Daniel',
    email='user@politico.com',
    phoneNumber='0798344456',
    passportUrl='user.png',
    password="user123"
))

admin_user_login=json.dumps(dict(
    email='admin@politico.com',
    password='admin123'
))

empty_body_login=json.dumps(dict(

))

wrong_password_login=json.dumps(dict(
    email='admin@politico.com',
    password='wrongpassword'
))

without_email_login=json.dumps(dict(
    password='admin123'
))

without_password_login=json.dumps(dict(
    email='admin@politico.com'
))

blank_password_login=json.dumps(dict(
    email='admin@politico.com',
    password=''
))

blank_email_login=json.dumps(dict(
    email='',
    password='admin123'
))

unregistered_login=json.dumps(dict(
    email='unregistered@politico.com',
    password='notme'
))

# dummy candidates

candidate=json.dumps(dict(
    id=1,
    office=1,
    party=1,
    candidate=1
))
