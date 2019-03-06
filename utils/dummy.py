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

party_edit_invalid_logo = json.dumps(dict(
    id=1,
    name="Red",
    hqAddress="Addis",
    logoUrl="red"
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

party_invalid_logoUrl = json.dumps(dict(
    id=1,
    name="Jubilee",
    hqAddress="Kent",
    logoUrl="invalid"
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
    password="admin@123",
    isAdmin=True
))

user = json.dumps(dict(
    firstName='Wayne',
    lastName='Rooney',
    otherName='Timothy',
    email='user@politico.com',
    phoneNumber='0798344456',
    passportUrl='user.png',
    password="User@123"
))

weak_password_user = json.dumps(dict(
    firstName='Wayne',
    lastName='Rooney',
    otherName='Timothy',
    email='user@politico.com',
    phoneNumber='0798344456',
    passportUrl='user.png',
    password="user123"
))

blank_user = json.dumps(dict(
    firstName='',
    lastName='Rooney',
    otherName='Timothy',
    email='user@politico.com',
    phoneNumber='0798344456',
    passportUrl='user.png',
    password="User@123"
))

user1 = json.dumps(dict(
    firstName='George',
    lastName='Harrison',
    otherName='Herbert',
    email='user1@politico.com',
    phoneNumber='0798344456',
    passportUrl='user.png',
    password="User@123"
))

int_user = json.dumps(dict(
    firstName=8,
    lastName='Harrison',
    otherName='Herbert',
    email='user1@politico.com',
    phoneNumber='0798344456',
    passportUrl='user.png',
    password="User@123"
))

invalid_image_user = json.dumps(dict(
    firstName='George',
    lastName='Harrison',
    otherName='Herbert',
    email='user1@politico.com',
    phoneNumber='0798344456',
    passportUrl='user',
    password="User@123"
))

invalid_email_user = json.dumps(dict(
    firstName='George',
    lastName='Harrison',
    otherName='Herbert',
    email='politico.com',
    phoneNumber='0798344456',
    passportUrl='user.png',
    password="User@123"
))

missing_key_user = json.dumps(dict(
    lastName='Harrison',
    otherName='Herbert',
    email='user4@politico.com',
    phoneNumber='0798344456',
    passportUrl='user.png',
    password="User@123"
))

admin_user_login = json.dumps(dict(
    email='admin@politico.com',
    password='admin@123'
))

empty_body_login = json.dumps(dict(

))

wrong_password_login = json.dumps(dict(
    email='admin@politico.com',
    password='Admin@12345'
))

without_email_login = json.dumps(dict(
    password='Admin@123'
))

without_password_login = json.dumps(dict(
    email='admin@politico.com'
))

blank_password_login = json.dumps(dict(
    email='admin@politico.com',
    password=''
))

blank_email_login = json.dumps(dict(
    email='',
    password='Admin@123'
))

invalid_email_login = json.dumps(dict(
    email='email',
    password='Admin@123'
))

unregistered_login = json.dumps(dict(
    email='unregistered@politico.com',
    password='Admin@12356'
))

# dummy candidates
candidate = json.dumps(dict(
    office=1,
    party=1,
    user=2
))

string_candidate = json.dumps(dict(
    office=1,
    party="democrat",
    user=2
))

candidate_blank = json.dumps(dict(
    office="",
    party=1,
    user=2
))

candidate1 = json.dumps(dict(
    office=1,
    party=1,
    user=3
))

# vote

ballot = json.dumps(dict(
    office=1,
    candidate=2,
    voter=2
))

no_office_ballot = json.dumps(dict(
    office=3,
    candidate=2,
    voter=2
))

no_candidate_ballot = json.dumps(dict(
    office=1,
    candidate=5,
    voter=2
))
