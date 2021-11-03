from fastapi import FastAPI
import uvicorn
from routes.routes import blog_router
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from grpc import ssl_channel_credentials

blog = FastAPI(
    debug=True,
    title="Blog",
    version="0.1.0",
)
my_blog = blog_router()
blog.include_router(my_blog)


# settings for observability
blog_resource = Resource(attributes={
    "service.name": "MyBlog"
})

blog_trace_provider = TracerProvider(resource=blog_resource)

otlp_exporter = OTLPSpanExporter(
    endpoint="api.honeycomb.io:443",
    insecure=False,
    credentials=ssl_channel_credentials(),
    headers=(
        ("x-honeycomb-team", "6e34d5a6fac444ef36f23d2e765b01a7"),
    )
)

# register exporter with provider
blog_trace_provider.add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

# register trace provider
trace.set_tracer_provider(blog_trace_provider)


if __name__ == "__main__":
    uvicorn.run(app=blog)
