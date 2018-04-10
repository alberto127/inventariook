from personas.models import Usuario
from table import Table
from table.columns import Column
 
class PostTable(Table):
	nombre = Column(field='nombre', header=u'nombre')
	departamento = Column(field='departamento', header=u'departamento')
	email = Column(field='email', header=u'email')
	fuera_convenio = Column(field='fuera_convenio', header=u'fuera_convenio')
	class Meta:
		model = Usuario