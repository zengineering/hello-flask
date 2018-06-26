import sqlite3
import pytest
from flaskr.db import get_db


def test_get_close_db(app):
    '''
    reuse db if opened

    fail when db is closed
    '''
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute("SELECT 1")

    assert 'closed' in str(e)


def test_init_db_command(runner, monkeypatch):
    '''
    call db.init_db from cli command
    '''
    class Recorder():
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr("flaskr.db.init_db", fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert "Initialized" in result.output
    assert Recorder.called
