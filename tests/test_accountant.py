import pytest
from warranty_man.accountant import Accountant
from warranty_man.warranty import Certificate, CertificateTypeEnum, Warranty, WarrantyTypeEnum

def test_accountant_property():
    a = Accountant()
    assert isinstance(a.vault, list) is True

def test_accountant_store():
    a = Accountant()
    c = Certificate(
        location='kitchen',
        certificate_type=CertificateTypeEnum.RECEIPT
    )
    w = Warranty(
        id = 1,
        name = 'fan',
        start_date=86400.0 * 5,
        certificate=c,
        time_len_day=30,
        warrantype=WarrantyTypeEnum.LIMITED,
    )

    a.store_warranty(w)

    assert len(a.vault) == 1
    assert a.vault[0] == w

def test_get_valid_warranty_by_date():
    a = Accountant()
    c = Certificate(
        location='kitchen',
        certificate_type=CertificateTypeEnum.RECEIPT
    )
    w_due = Warranty(
        id = 1,
        name = 'fan',
        start_date=86400.0 * 5,
        certificate=c,
        time_len_day=30,
        warrantype=WarrantyTypeEnum.LIMITED,
    )
    
    w_valid = Warranty(
        id = 2,
        name = 'fridge',
        start_date=86400.0 * 6,
        certificate=c,
        time_len_day=365,
        warrantype=WarrantyTypeEnum.LIMITED,
    )

    a.store_warranty(w_due)
    a.store_warranty(w_valid)
    check_date = 86400.0 * 200
    valid_list = a.get_valid_warranty_by_date(check_date)

    assert len(valid_list) == 1
    assert valid_list[0] == w_valid

def test_get_warranty_by_id():
    a = Accountant()
    c = Certificate(
        location='kitchen',
        certificate_type=CertificateTypeEnum.RECEIPT
    )
    w_due = Warranty(
        id = 1,
        name = 'fan',
        start_date=86400.0 * 5,
        certificate=c,
        time_len_day=30,
        warrantype=WarrantyTypeEnum.LIMITED,
    )
    
    w_valid = Warranty(
        id = 2,
        name = 'fridge',
        start_date=86400.0 * 6,
        certificate=c,
        time_len_day=365,
        warrantype=WarrantyTypeEnum.LIMITED,
    )

    a.store_warranty(w_due)
    a.store_warranty(w_valid)
    found_w = a.get_warranty_by_id(1)

    assert found_w == w_due

    with pytest.raises(Exception) as excinfo:
        a.get_warranty_by_id(3)

    assert str(excinfo.value)  == 'No warranty found with id: 3'    
