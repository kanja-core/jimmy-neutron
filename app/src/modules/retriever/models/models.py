from typing import Optional, Literal
from pydantic import BaseModel, Field
from datetime import datetime


class ID(BaseModel):
    """Information extracted from a Brazilian ID document (RG - Registro Geral)."""

    first_name: Optional[str] = Field(
        default=None,
        description="""
            The person's first name as it appears on the ID.
            If not sure, leave blank.
        """,
    )

    last_name: Optional[str] = Field(
        default=None,
        description="""
            The person's complete last name as it appears on the ID.
            Should include all middle names and family names in capital letters.
            If not sure, leave blank.
        """,
    )

    rg: Optional[str] = Field(
        default=None,
        description="""
            The RG number in format XX.XXX.XXX-X.
            Should only contain numbers from 0-9 or the letter X.\
            Look for "Registro Geral", "RG".
            If not sure, leave blank.
        """,
    )

    cpf: Optional[str] = Field(
        default=None,
        description="""
            The CPF number in format XXX.XXX.XXX/XX.
            Should only contain numbers from 0-9.
            If not sure, leave blank.
        """,
    )

    issuance_date: Optional[str] = Field(
        default=None,
        description="""
            The date when the ID was issued in format DD/MM/YYYY.
            Look for 'Data de Expedição' or similar phrases.
            If not sure, leave blank.
        """,
    )

    date_of_birth: Optional[str] = Field(
        default=None,
        description="""
            The person's date of birth in format DD/MM/YYYY.
            Look for 'Data de Nascimento' or similar phrases.
            If not sure, leave blank.
        """,
    )

    expiration_date: Optional[str] = Field(
        default=None,
        description="""
            The expiration date of the ID in format DD/MM/YYYY.
            Validity rules based on age:
            * 5 years for people under 12 years old
            * 10 years for people between 12 and 59 years old
            * No expiration (leave blank) for people 60 years or older
            Example: If issued on 01/04/2023:
            - For a 7-year-old: expires 01/04/2028 (5 years)
            - For a 39-year-old: expires 01/04/2033 (10 years)
            - For a 61-year-old: leave blank (no expiration)
            If not sure, leave blank.
        """,
    )

    @staticmethod
    def parse_date(date_str: Optional[str]) -> Optional[str]:
        """Parses a string in DD/MM/YYYY format and validates it."""
        if date_str:
            try:
                parsed_date = datetime.strptime(date_str, "%d/%m/%Y")
                return parsed_date.strftime("%d/%m/%Y")
            except ValueError:
                return None
        return None

    def __init__(self, **data):
        if "issuance_date" in data:
            data["issuance_date"] = self.parse_date(data.get("issuance_date"))
        if "expiration_date" in data:
            data["expiration_date"] = self.parse_date(data.get("expiration_date"))
        super().__init__(**data)


class TaxCertificate(BaseModel):
    """Information extracted from a Brazil (national, state, municipal) tax certificate (Certidão de Débitos)."""

    cpf: Optional[str] = Field(
        default=None,
        description="""
            The CPF number in format XXX.XXX.XXX/XX.
            It should only contain numbers from 0-9 or the letter X
            If not Sure, leave blank
        """,
    )
    debt_exists: Optional[Literal["negative", "positive", "positive_suspended"]] = (
        Field(
            default=None,
            description="""
            Extract if there are any debts, looking for:
            * positive: ('constam débitos', positiva);
            * negative: ('não constam débitos', negativa);
            * positive_suspended: (positiva mas com efeito de negativa).
            FILL WITH one of the above options.
            IF NOT SURE, leave blank
        """,
        )
    )
    issuance_date: Optional[str] = Field(
        default=None,
        description="""
            The date when the certificate was issued in format DD/MM/YYYY.
            Look for 'Data e hora da emissão' or similar phrases.
            IF NOT SURE, leave blank
        """,
    )
    expiration_date: Optional[str] = Field(
        default=None,
        description="""
            The expiration date of the certificate in format DD/MM/YYYY.
            This can be either explicitly stated in the document or calculated by adding
            the expiration period to the issuance date. For example, if issued on 10/08/2010
            with expiration of 8 months, the expiration date would be 10/04/2011.
            IF NOT SURE, leave blank
        """,
    )
    certificate_number: Optional[str] = Field(
        default=None,
        description="""
            The certificate number (número da certidão).
            It should only contain numbers from 0-9, and a maximun of one dash ('-') caracter.
            IF NOT SURE, leave blank
        """,
    )

    @staticmethod
    def parse_date(date_str: Optional[str]) -> Optional[str]:
        """Parses a string in DD/MM/YYYY format and validates it."""
        if date_str:
            try:
                # Ensure the date is valid and properly formatted
                parsed_date = datetime.strptime(date_str, "%d/%m/%Y")
                return parsed_date.strftime("%d/%m/%Y")
            except ValueError:
                return None
        return None

    def __init__(self, **data):
        if "issuance_date" in data:
            data["issuance_date"] = self.parse_date(data.get("issuance_date"))
        if "expiration_date" in data:
            data["expiration_date"] = self.parse_date(data.get("expiration_date"))
        super().__init__(**data)
