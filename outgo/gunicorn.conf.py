import multiprocessing
import os

port = os.environ.get("PORT", 8000)
WORKERS_PER_CPU = multiprocessing.cpu_count() * int(
    os.environ.get("WORKERS_PER_CPU", 1)
)


bind = f"0.0.0.0:{port}"
workers = int(os.environ.get("NUM_WORKERS", WORKERS_PER_CPU))
