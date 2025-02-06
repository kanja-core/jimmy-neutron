from app.src.modules.graph.factory import BuilderFactory

# from app.src.settings.main import settings
# from app.src.modules.node.types import NodePassInOutput
# import asyncio

# Ensure BuilderFactory returns an async-compatible graph
builder = BuilderFactory.test_1()
graph = builder.exec()

# # Ensure NodePassInOutput is correctly instantiated with a string type
# in_ = NodePassInOutput[str](data="app/pdf/sp/cnd_fazenda.pdf")


# # Run the async function properly
# async def run_graph():
#     result = await graph.ainvoke(in_)
#     print("Graph Output:", result)


# # Execute the async function
# asyncio.run(run_graph())
