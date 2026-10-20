"""
Entry point into the application.
"""

from fastapi import FastAPI

from configs import settings

app = FastAPI(debug=settings.debug)
