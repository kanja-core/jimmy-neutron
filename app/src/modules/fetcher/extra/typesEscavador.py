from typing import List, Optional
from pydantic import BaseModel


# ✅ Define simple structures using Pydantic
class Estado(BaseModel):
    nome: str
    sigla: str


class Tribunal(BaseModel):
    id: int
    nome: str
    sigla: str
    categoria: Optional[str] = None
    estados: List[Estado] = []


class Oab(BaseModel):
    numero: int
    uf: str
    tipo: str


class InvolvedEscavador(BaseModel):
    nome: str
    tipo_pessoa: str
    quantidade_processos: int


class Envolvido(BaseModel):
    nome: Optional[str] = None
    tipo: Optional[str] = None
    tipo_normalizado: str
    tipo_pessoa: str
    quantidade_processos: int
    polo: str
    prefixo: Optional[str] = None
    sufixo: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    oabs: List[Oab] = []
    advogados: List["Envolvido"] = []
    last_valid_cursor: str = ""


class TipoEnvolvidoPesquisado(BaseModel):
    id: int
    tipo: str
    tipo_normalizado: str
    polo: str


# ✅ Define the Case Structure
class MatchFontes(BaseModel):
    tribunal: Optional[bool]
    diario_oficial: Optional[bool]


class InformacaoComplementar(BaseModel):
    tipo: str
    valor: str


class Assunto(BaseModel):
    id: int
    nome: str
    nome_com_pai: str
    path_completo: str


class ValorCausa(BaseModel):
    valor: Optional[float] = None
    moeda: Optional[str] = None
    valor_formatado: Optional[str] = None


class CapaProcessoTribunal(BaseModel):
    assunto_principal_normalizado: Optional[Assunto] = None
    assuntos_normalizados: List[Assunto] = []
    classe: Optional[str] = None
    assunto: Optional[str] = None
    area: Optional[str] = None
    orgao_julgador: Optional[str] = None
    data_distribuicao: Optional[str] = None
    data_arquivamento: Optional[str] = None
    valor_causa: Optional[ValorCausa] = None
    informacoes_complementares: Optional[List[InformacaoComplementar]] = []


class FonteProcesso(BaseModel):
    id: int
    processo_fonte_id: int
    descricao: str
    nome: str
    sigla: str
    tipo: str
    grau: int
    grau_formatado: str
    data_inicio: Optional[str] = None
    data_ultima_movimentacao: Optional[str] = None
    fisico: Optional[bool]
    sistema: str
    quantidade_movimentacoes: int
    quantidade_envolvidos: int
    segredo_justica: Optional[bool] = None
    arquivado: Optional[bool] = None
    status_predito: Optional[str] = None
    tipos_envolvido_pesquisado: List[TipoEnvolvidoPesquisado] = []
    match_documento_por: Optional[str] = None
    url: Optional[str] = None
    caderno: Optional[str] = None
    data_ultima_verificacao: Optional[str] = None
    tribunal: Optional[Tribunal] = None
    capa: Optional[CapaProcessoTribunal] = None
    envolvidos: List[Envolvido] = []


class CaseEscavador(BaseModel):
    numero_cnj: str
    quantidade_movimentacoes: int
    fontes_tribunais_estao_arquivadas: Optional[bool]
    ano_inicio: int
    data_ultima_verificacao: str
    tempo_desde_ultima_verificacao: str
    data_ultima_movimentacao: str
    match_fontes: MatchFontes
    titulo_polo_ativo: Optional[str] = None
    titulo_polo_passivo: Optional[str] = None
    data_inicio: Optional[str] = None
    tipo_match: Optional[str] = None
    fontes: List[FonteProcesso] = []
    last_valid_cursor: str = ""


# ✅ Final Structure Using Pydantic
class LawsuitsEscavador(BaseModel):
    envolvido_encontrado: InvolvedEscavador
    items: List[CaseEscavador]


# from __future__ import annotations
# from dataclasses import dataclass, field
# from typing import List, Optional
# from enum import Enum
# from ..helpers.decorators import filter_unexpected_fields


# @filter_unexpected_fields
# @dataclass
# class Estado:
#     nome: str
#     sigla: str


# @filter_unexpected_fields
# @dataclass
# class Tribunal:
#     id: int
#     nome: str
#     sigla: str
#     categoria: Optional[str] = None
#     estados: List[Estado] = field(default_factory=list)


# @filter_unexpected_fields
# @dataclass
# class Oab:
#     numero: int
#     uf: str
#     tipo: str


# @filter_unexpected_fields
# @dataclass
# class InvolvedEscavador:
#     nome: str
#     tipo_pessoa: str
#     quantidade_processos: int = field()
#     # cpfs_com_esse_nome: int = field(default=0)
#     # last_valid_cursor: Optional[str] = field(default="")


# @filter_unexpected_fields
# @dataclass
# class Envolvido:
#     nome: Optional[str]
#     tipo: Optional[str]
#     tipo_normalizado: str
#     tipo_pessoa: str
#     quantidade_processos: int
#     polo: str
#     prefixo: Optional[str] = None
#     sufixo: Optional[str] = None
#     cpf: Optional[str] = None
#     cnpj: Optional[str] = None
#     oabs: List[Oab] = field(default_factory=list)
#     advogados: List["Envolvido"] = field(default_factory=list)
#     last_valid_cursor: str = field(default="")


# @filter_unexpected_fields
# @dataclass
# class TipoEnvolvidoPesquisado:
#     id: int
#     tipo: str
#     tipo_normalizado: str
#     polo: str


# # Enums
# class Ordem(str, Enum):
#     ASC = "asc"
#     DESC = "desc"


# class CriterioOrdenacao(str, Enum):
#     ULTIMA_MOVIMENTACAO = "data_ultima_movimentacao"
#     INICIO = "data_inicio"


# class SiglaTribunal(str, Enum):
#     STF = "STF"
#     CNJ = "CNJ"
#     STJ = "STJ"
#     CJF = "CJF"
#     TRF1 = "TRF1"
#     TRF2 = "TRF2"
#     TRF3 = "TRF3"
#     TRF4 = "TRF4"
#     TRF5 = "TRF5"
#     TRF6 = "TRF6"
#     TST = "TST"
#     CSJT = "CSJT"
#     TRT1 = "TRT-1"
#     TRT2 = "TRT-2"
#     TRT3 = "TRT-3"
#     TRT4 = "TRT-4"
#     TRT5 = "TRT-5"
#     TRT6 = "TRT-6"
#     TRT7 = "TRT-7"
#     TRT8 = "TRT-8"
#     TRT9 = "TRT-9"
#     TRT10 = "TRT-10"
#     TRT11 = "TRT-11"
#     TRT12 = "TRT-12"
#     TRT13 = "TRT-13"
#     TRT14 = "TRT-14"
#     TRT15 = "TRT-15"
#     TRT16 = "TRT-16"
#     TRT17 = "TRT-17"
#     TRT18 = "TRT-18"
#     TRT19 = "TRT-19"
#     TRT20 = "TRT-20"
#     TRT21 = "TRT-21"
#     TRT22 = "TRT-22"
#     TRT23 = "TRT-23"
#     TRT24 = "TRT-24"
#     TSE = "TSE"
#     TREAC = "TRE-AC"
#     TREAL = "TRE-AL"
#     TREAP = "TRE-AP"
#     TREAM = "TRE-AM"
#     TREBA = "TRE-BA"
#     TRECE = "TRE-CE"
#     TREDF = "TRE-DF"
#     TREES = "TRE-ES"
#     TREGO = "TRE-GO"
#     TREMA = "TRE-MA"
#     TREMT = "TRE-MT"
#     TREMS = "TRE-MS"
#     TREMG = "TRE-MG"
#     TREPA = "TRE-PA"
#     TREPB = "TRE-PB"
#     TREPR = "TRE-PR"
#     TREPE = "TRE-PE"
#     TREPI = "TRE-PI"
#     TRERJ = "TRE-RJ"
#     TRERN = "TRE-RN"
#     TRERS = "TRE-RS"
#     TRERO = "TRE-RO"
#     TRERR = "TRE-RR"
#     TRESC = "TRE-SC"
#     TRESE = "TRE-SE"
#     TRESP = "TRE-SP"
#     TRETO = "TRE-TO"
#     STM = "STM"
#     # CJM1 = "1-CJM"
#     # CJM2 = "2-CJM"
#     # CJM3 = "3-CJM"
#     # CJM4 = "4-CJM"
#     # CJM5 = "5-CJM"
#     # CJM6 = "6-CJM"
#     # CJM7 = "7-CJM"
#     # CJM8 = "8-CJM"
#     # CJM9 = "9-CJM"
#     # CJM10 = "10-CJM"
#     # CJM11 = "11-CJM"
#     # CJM12 = "12-CJM"
#     TJAC = "TJAC"
#     TJAL = "TJAL"
#     TJAP = "TJAP"
#     TJAM = "TJAM"
#     TJBA = "TJBA"
#     TJCE = "TJCE"
#     TJDF = "TJDF"
#     TJES = "TJES"
#     TJGO = "TJGO"
#     TJMA = "TJMA"
#     TJMT = "TJMT"
#     TJMS = "TJMS"
#     TJMG = "TJMG"
#     TJPA = "TJPA"
#     TJPB = "TJPB"
#     TJPR = "TJPR"
#     TJPE = "TJPE"
#     TJPI = "TJPI"
#     TJRJ = "TJRJ"
#     TJRN = "TJRN"
#     TJRS = "TJRS"
#     TJRO = "TJRO"
#     TJRR = "TJRR"
#     TJSC = "TJSC"
#     TJSE = "TJSE"
#     TJSP = "TJSP"
#     TJTO = "TJTO"
#     TJMEMG = "TJME-MG"
#     TJMERS = "TJME-RS"
#     TJMESP = "TJME-SP"


# # Dataclasses
# @filter_unexpected_fields
# @dataclass(frozen=True)
# class SolicitacaoAtualizacao:
#     id: int
#     status: str
#     criado_em: str
#     numero_cnj: str
#     concluido_em: Optional[str] = None


# @filter_unexpected_fields
# @dataclass
# class StatusAtualizacao:
#     numero_cnj: str
#     data_ultima_verificacao: str
#     tempo_desde_ultima_verificacao: str
#     ultima_verificacao: Optional[SolicitacaoAtualizacao]


# @filter_unexpected_fields
# @dataclass
# class MatchFontes:
#     tribunal: bool
#     diario_oficial: bool


# @filter_unexpected_fields
# @dataclass
# class InformacaoComplementar:
#     tipo: str
#     valor: str


# @filter_unexpected_fields
# @dataclass
# class Assunto:
#     id: int
#     nome: str
#     nome_com_pai: str
#     path_completo: str


# @filter_unexpected_fields
# @dataclass
# class ValorCausa:
#     valor: float
#     moeda: str
#     valor_formatado: str


# @filter_unexpected_fields
# @dataclass
# class CapaProcessoTribunal:
#     assunto_principal_normalizado: Optional[Assunto] = None
#     assuntos_normalizados: List[Assunto] = field(default_factory=list)
#     classe: Optional[str] = None
#     assunto: Optional[str] = None
#     area: Optional[str] = None
#     orgao_julgador: Optional[str] = None
#     data_distribuicao: Optional[str] = None
#     data_arquivamento: Optional[str] = None
#     valor_causa: Optional[ValorCausa] = None
#     informacoes_complementares: List[InformacaoComplementar] = field(
#         default_factory=list
#     )


# @filter_unexpected_fields
# @dataclass
# class FonteProcesso:
#     id: int
#     processo_fonte_id: int
#     descricao: str
#     nome: str
#     sigla: str
#     tipo: str
#     grau: int
#     grau_formatado: str
#     data_inicio: str
#     data_ultima_movimentacao: str
#     fisico: bool
#     sistema: str
#     quantidade_movimentacoes: int
#     quantidade_envolvidos: int
#     segredo_justica: Optional[bool] = None
#     arquivado: Optional[bool] = None
#     status_predito: Optional[str] = None
#     tipos_envolvido_pesquisado: List[TipoEnvolvidoPesquisado] = field(
#         default_factory=list
#     )
#     match_documento_por: Optional[str] = None
#     url: Optional[str] = None
#     caderno: Optional[str] = None
#     data_ultima_verificacao: Optional[str] = None
#     tribunal: Optional[Tribunal] = None
#     capa: Optional[CapaProcessoTribunal] = None
#     envolvidos: List[Envolvido] = field(default_factory=list)


# @filter_unexpected_fields
# @dataclass
# class CaseEscavador:
#     numero_cnj: str
#     quantidade_movimentacoes: int
#     fontes_tribunais_estao_arquivadas: bool
#     ano_inicio: int
#     data_ultima_verificacao: str
#     tempo_desde_ultima_verificacao: str
#     data_ultima_movimentacao: str
#     match_fontes: MatchFontes
#     titulo_polo_ativo: Optional[str] = None
#     titulo_polo_passivo: Optional[str] = None
#     data_inicio: Optional[str] = None
#     tipo_match: Optional[str] = None
#     fontes: List[FonteProcesso] = field(default_factory=list)
#     last_valid_cursor: str = field(default="", repr=False)


# @filter_unexpected_fields
# @dataclass
# class LawsuitsEscavador:
#     envolvido_encontrado: InvolvedEscavador
#     items: List[CaseEscavador]
