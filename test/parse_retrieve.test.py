from app.src.modules.graph.factory import BuilderFactory

builder = BuilderFactory.test_parse_retrieve()
graph = builder.exec()
