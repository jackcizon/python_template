import os
import asyncio

import pytest

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.core.config import Settings


test_settings = Settings("test")