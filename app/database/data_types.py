from app.database import get_db


def output_formatter(results):
  out = []
  for result in results:
    entry = {
      "id": result[0],
      "name": result[1],
      "summary": result[2],
      "description": result[3]
    }
    out.append(entry)
    return out

def scan():
  statement = "SELECT * FROM data_type"
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute(statement, ())
  out = cursor.fetchall()
  cursor.close()
  return output_formatter(out)
  