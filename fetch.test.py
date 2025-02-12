from app.src.modules.graph.factory import BuilderFactory

builder = BuilderFactory.test_fetch()
graph = builder.exec()
