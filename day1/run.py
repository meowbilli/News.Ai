import os
from flaskblog import app

port = int(os.environ.get('PORT', 8080))  # use Railway's PORT if available
app.run(host='0.0.0.0', port=port)
