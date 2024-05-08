from warranty_man.warranty import Certificate, CertificateTypeEnum, Warranty, WarrantyTypeEnum

def test_certificate_id():
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
    assert isinstance(w.id, int) is True
    assert w.id == 1


def test_certificate_name():
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

    assert isinstance(w.name, str) is True
    assert w.name == 'fan'


def test_certificate_start_date():
    time_len = 86400.0 * 5
    c = Certificate(
        location='kitchen',
        certificate_type=CertificateTypeEnum.RECEIPT
    )
    w = Warranty(
        id = 1,
        name = 'fan',
        start_date=time_len,
        certificate=c,
        time_len_day=30,
        warrantype=WarrantyTypeEnum.LIMITED,
    )
    assert isinstance(w.start_date, float) is True
    assert w.start_date == time_len

def test_certificate_certificate():
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
    assert isinstance(w.certificate, Certificate) is True
    assert w.certificate.certificate_type == CertificateTypeEnum.RECEIPT
    assert w.certificate.location == 'kitchen'


def test_certificate_time_len_day():
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
    assert isinstance(w.time_len_day, int) is True
    assert w.time_len_day == 30

def test_certificate_warrantype():
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
    assert isinstance(w.warrantype, WarrantyTypeEnum) is True
    assert w.warrantype == WarrantyTypeEnum.LIMITED