DB_NAME = 'streaming_server.db'

CREATE_TABLE_QUERY = '''
    CREATE TABLE IF NOT EXISTS video (
        id INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        video_format VARCHAR(10) NOT NULL,
        views INTEGER NOT NULL DEFAULT 0,
        uploaded_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
'''

INSERT_QUERY = '''
    INSERT INTO video (name, video_format) VALUES (?, ?);
'''

DELETE_QUERY = '''
    DELETE FROM video WHERE id = ?
'''
