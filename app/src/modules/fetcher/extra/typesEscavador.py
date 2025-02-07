from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


@dataclass
class Estado:
    nome: str
    sigla: str


@dataclass
class Tribunal:
    id: int
    nome: str
    sigla: str
    categoria: Optional[str] = None
    estados: List[Estado] = field(default_factory=list)


@dataclass
class Oab:
    numero: int
    uf: str
    tipo: str


@dataclass
class InvolvedEscavador:
    nome: str
    tipo_pessoa: str
    quantidade_processos: int = field()
    # cpfs_com_esse_nome: int = field(default=0)
    # last_valid_cursor: Optional[str] = field(default="")


@dataclass
class Envolvido:
    nome: Optional[str]
    tipo: Optional[str]
    tipo_normalizado: str
    tipo_pessoa: str
    quantidade_processos: int
    polo: str
    prefixo: Optional[str] = None
    sufixo: Optional[str] = None
    cpf: Optional[str] = None
    cnpj: Optional[str] = None
    oabs: List[Oab] = field(default_factory=list)
    advogados: List["Envolvido"] = field(default_factory=list)
    last_valid_cursor: str = field(default="")


@dataclass
class TipoEnvolvidoPesquisado:
    id: int
    tipo: str
    tipo_normalizado: str
    polo: str


# Enums
class Ordem(str, Enum):
    ASC = "asc"
    DESC = "desc"


class CriterioOrdenacao(str, Enum):
    ULTIMA_MOVIMENTACAO = "data_ultima_movimentacao"
    INICIO = "data_inicio"


class SiglaTribunal(str, Enum):
    STF = "STF"
    CNJ = "CNJ"
    STJ = "STJ"
    CJF = "CJF"
    TRF1 = "TRF1"
    TRF2 = "TRF2"
    TRF3 = "TRF3"
    TRF4 = "TRF4"
    TRF5 = "TRF5"
    TRF6 = "TRF6"
    TST = "TST"
    CSJT = "CSJT"
    # (... mais tribunais ...)
    TJTO = "TJTO"
    TJMEMG = "TJME-MG"
    TJMERS = "TJME-RS"
    TJMESP = "TJME-SP"


# Dataclasses
@dataclass(frozen=True)
class SolicitacaoAtualizacao:
    id: int
    status: str
    criado_em: str
    numero_cnj: str
    concluido_em: Optional[str] = None


@dataclass
class StatusAtualizacao:
    numero_cnj: str
    data_ultima_verificacao: str
    tempo_desde_ultima_verificacao: str
    ultima_verificacao: Optional[SolicitacaoAtualizacao]


@dataclass
class MatchFontes:
    tribunal: bool
    diario_oficial: bool


@dataclass
class InformacaoComplementar:
    tipo: str
    valor: str


@dataclass
class Assunto:
    id: int
    nome: str
    nome_com_pai: str
    path_completo: str


@dataclass
class ValorCausa:
    valor: float
    moeda: str
    valor_formatado: str


@dataclass
class CapaProcessoTribunal:
    assunto_principal_normalizado: Optional[Assunto] = None
    assuntos_normalizados: List[Assunto] = field(default_factory=list)
    classe: Optional[str] = None
    assunto: Optional[str] = None
    area: Optional[str] = None
    orgao_julgador: Optional[str] = None
    data_distribuicao: Optional[str] = None
    data_arquivamento: Optional[str] = None
    valor_causa: Optional[ValorCausa] = None
    informacoes_complementares: List[InformacaoComplementar] = field(
        default_factory=list
    )


@dataclass
class FonteProcesso:
    id: int
    processo_fonte_id: int
    descricao: str
    nome: str
    sigla: str
    tipo: str
    grau: int
    grau_formatado: str
    data_inicio: str
    data_ultima_movimentacao: str
    fisico: bool
    sistema: str
    quantidade_movimentacoes: int
    quantidade_envolvidos: int
    segredo_justica: Optional[bool] = None
    arquivado: Optional[bool] = None
    status_predito: Optional[str] = None
    tipos_envolvido_pesquisado: List[TipoEnvolvidoPesquisado] = field(
        default_factory=list
    )
    match_documento_por: Optional[str] = None
    url: Optional[str] = None
    caderno: Optional[str] = None
    data_ultima_verificacao: Optional[str] = None
    tribunal: Optional[Tribunal] = None
    capa: Optional[CapaProcessoTribunal] = None
    envolvidos: List[Envolvido] = field(default_factory=list)


@dataclass
class CaseEscavador:
    numero_cnj: str
    quantidade_movimentacoes: int
    fontes_tribunais_estao_arquivadas: bool
    ano_inicio: int
    data_ultima_verificacao: str
    tempo_desde_ultima_verificacao: str
    data_ultima_movimentacao: str
    match_fontes: MatchFontes
    titulo_polo_ativo: Optional[str] = None
    titulo_polo_passivo: Optional[str] = None
    data_inicio: Optional[str] = None
    tipo_match: Optional[str] = None
    fontes: List[FonteProcesso] = field(default_factory=list)
    last_valid_cursor: str = field(default="", repr=False)


@dataclass
class LawsuitsEscavador:
    envolvido_encontrado: InvolvedEscavador
    items: List[CaseEscavador]
