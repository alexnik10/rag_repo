import uuid

def generate-unique-id():
  return str(uuid.uuid4())[:8]

def format-task(task):
  return f"[{task['id']}] {task['title']} - {task['description']}"
