import pytest
from src import query_trino

class DummyCursor:
    def __init__(self):
        self.data = [(1,)]
    def execute(self, sql):
        pass
    def fetchall(self):
        return self.data
    def close(self):
        pass

class DummyConn:
    def __init__(self):
        self.cursor_obj = DummyCursor()
    def cursor(self):
        return self.cursor_obj
    def close(self):
        pass

def dummy_connect(*args, **kwargs):
    return DummyConn()

def test_query_one_row(monkeypatch):
    monkeypatch.setattr(query_trino, "connect", dummy_connect)
    rows = query_trino.query_one_row("SELECT 1")
    assert rows == [(1,)]