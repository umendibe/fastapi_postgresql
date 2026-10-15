import psycopg
from psycopg.rows import dict_row

from schemas import schemas

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

def get_all_participants():
    with psycopg.connect(DATABASE_URL, row_factory=dict_row) as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name, surname, age FROM participants")
        return cur.fetchall()


def get_participant_id(id: int):
    with psycopg.connect(DATABASE_URL, row_factory=dict_row) as conn, conn.cursor() as cur:
        cur.execute("""
                    SELECT id, name, surname, age FROM participants
                    WHERE id = %s
                    """,
                    (id,))
        return cur.fetchone()


def post_participant(participant: schemas.CreateParticipant):
    with psycopg.connect(DATABASE_URL, row_factory=dict_row) as conn, conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO participants (name, surname, age)
                    VALUES (%s, %s, %s)
                    RETURNING id, name, surname, age
                    """,
                    (participant.name, participant.surname, participant.age))
        return cur.fetchone()
