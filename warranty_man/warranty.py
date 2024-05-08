import enum
import dataclasses


class CertificateTypeEnum(enum.Enum):
    OTHER = 0
    RECEIPT = 1
    BOX = 2


class WarrantyTypeEnum(enum.Enum):
    UNLIMIT = 0
    LIMITED = 1


@dataclasses.dataclass
class Certificate:
    location: str
    certificate_type: CertificateTypeEnum = CertificateTypeEnum.RECEIPT


@dataclasses.dataclass
class Warranty:
    id: int
    name: str
    start_date: float
    certificate: Certificate
    time_len_day: int = 0
    warrantype: WarrantyTypeEnum = WarrantyTypeEnum.LIMITED
