# "Database code" for the DB Forum.

import psycopg2



def get_posts():
  """Return all posts from the 'database', most recent first."""
  query = """
	select time, content from posts order by time desc
  """
  db = psycopg2.connect("dbname=forum")
  c = db.cursor()
  c.execute(query)
  posts = ({str(row[0]), str(row[1])} for row in c.fetchall())
  db.close()
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect("dbname=forum")
  c = db.cursor()
  c.execute("insert into posts (content) values (%s)" , (content,))
  db.commit()
  db.close()




