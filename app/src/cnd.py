from typing import Optional, Literal
from pydantic import BaseModel, Field
from datetime import datetime

class CND(BaseModel):
    """Information extracted from a São Paulo state tax certificate (Certidão de Débitos)."""

    cpf: Optional[str] = Field(
        default=None, 
        description="""
            The CPF number in format XXX.XXX.XXX-XX.
            It should only contain numbers from 0-9 or the letter X
            If not Sure, leave blank
        """
    )
    debt_exists: Optional[Literal["negative", "positive", "positive_suspended"]] = Field(
        default=None, 
        description="""
            Extract if there are any debts, looking for:
            * positive: ('constam débitos', positiva);
            * negative: ('não constam débitos', negativa);
            * positive_suspended: (positiva mas com efeito de negativa).
            FILL WITH one of the above options.
            IF NOT SURE, leave blank
        """
    )
    issuance_date: Optional[str] = Field(
        default=None,
        description="""
            The date when the certificate was issued in format DD/MM/YYYY.
            Look for 'Data e hora da emissão' or similar phrases.
            IF NOT SURE, leave blank
        """
    )
    validity_date: Optional[str] = Field(
        default=None,
        description="""
            The expiration date of the certificate in format DD/MM/YYYY.
            This can be either explicitly stated in the document or calculated by adding
            the validity period to the issuance date. For example, if issued on 10/08/2010
            with validity of 8 months, the validity date would be 10/04/2011.
            IF NOT SURE, leave blank
        """
    )
    certificate_number: Optional[str] = Field(
        default=None, 
        description="""
            The certificate number (número da certidão).
            It should only contain numbers from 0-9, and a maximun of one dash ('-') caracter.
            IF NOT SURE, leave blank
        """
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
        if 'issuance_date' in data:
            data['issuance_date'] = self.parse_date(data.get('issuance_date'))
        if 'validity_date' in data:
            data['validity_date'] = self.parse_date(data.get('validity_date'))
        super().__init__(**data)