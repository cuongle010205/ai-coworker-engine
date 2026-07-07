from typing import Dict, List
import sqlite3
import json


class MemoryManager:

    def __init__(self, db_path="memory.db"):

        self.conn = sqlite3.connect(
            db_path,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_tables()


    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS conversations(

            session_id TEXT PRIMARY KEY,

            history TEXT,

            relationship INTEGER,

            progress INTEGER,

            summary TEXT

        )

        """)

        self.conn.commit()


    def load(self, session_id):

        self.cursor.execute(

            "SELECT history FROM conversations WHERE session_id=?",

            (session_id,)

        )

        row = self.cursor.fetchone()

        if row is None:

            return []

        return json.loads(row[0])


    def save(self, session_id, history):

        relationship = self.relationship(session_id)
        progress = self.progress(session_id)
        summary = self.summary(history)

        history_json = json.dumps(history)

        self.cursor.execute(
        """
        INSERT INTO conversations
        (session_id, history, relationship, progress, summary)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(session_id)
        DO UPDATE SET
            history = excluded.history,
            relationship = excluded.relationship,
            progress = excluded.progress,
            summary = excluded.summary
        """,
        (
            session_id,
            history_json,
            relationship,
            progress,
            summary
        )
    )

        self.conn.commit()


    def relationship(self, session_id):

        self.cursor.execute(

            "SELECT relationship FROM conversations WHERE session_id=?",

            (session_id,)

        )

        row = self.cursor.fetchone()

        if row is None:

            return 50

        return row[0]


    def update_relationship(

        self,

        session_id,

        delta

    ):

        value = self.relationship(session_id)

        value += delta

        value = max(

            0,

            min(

                100,

                value

            )

        )

        self.cursor.execute("""

        UPDATE conversations

        SET relationship=?

        WHERE session_id=?

        """,

        (

            value,

            session_id

        ))

        self.conn.commit()


    def progress(self, session_id):

        self.cursor.execute(

            "SELECT progress FROM conversations WHERE session_id=?",

            (session_id,)

        )

        row = self.cursor.fetchone()

        if row is None:

            return 0

        return row[0]


    def update_progress(

        self,

        session_id,

        value

    ):

        self.cursor.execute("""

        UPDATE conversations

        SET progress=?

        WHERE session_id=?

        """,

        (

            value,

            session_id

        ))

        self.conn.commit()


    def summary(

        self,

        history

    ):

        if len(history) == 0:

            return ""

        recent = history[-5:]

        text = ""

        for turn in recent:

            text += f"""

User:

{turn["user"]}

Assistant:

{turn["assistant"]}

"""

        return text