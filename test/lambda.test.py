from app.src.modules.graph.factory import BuilderFactory

builder = BuilderFactory.test_lambda_flow()
graph = builder.exec()
