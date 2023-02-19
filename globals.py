import modal
Globals = {
    "VOLUME": modal.SharedVolume().persist("model-cache-vol"),
    "OPENAPI_SECRET":"my-openai-secret",
    "CACHE_DIR": "/internal",
    "FAISS_PKL":"./faiss_store.pkl",
    "INDEX":"./docs.index",
    # "INDEX":"/internal/docs.index",
    # "FAISS_PKL":"/internal/faiss_store.pkl",
    "CORES":14.0,
    "MEMORY":32768
}