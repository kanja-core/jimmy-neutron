from .extra.typesEscavador import LawsuitsEscavador
from .types import Case, Lawsuits


class LawsuitFetcherMapper:
    @staticmethod
    def escavador(input: LawsuitsEscavador) -> Lawsuits:
        return Lawsuits(
            name=input.envolvido_encontrado.tipo_pessoa,
            type=input.envolvido_encontrado.tipo_pessoa,
            items=[
                Case(
                    amount=getattr(
                        getattr(
                            getattr(x.fontes[0], "capa", None), "valor_causa", None
                        ),
                        "valor",
                        None,
                    ),
                    cnj=x.numero_cnj,
                    area=getattr(
                        getattr(
                            getattr(x.fontes[0], "capa", None), "valor_causa", None
                        ),
                        "descricao",
                        None,
                    ),
                )
                for x in input.items
            ],
        )
