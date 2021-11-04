from mytodo.views import *
from mytodo.models import *
from mytodo import app

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
