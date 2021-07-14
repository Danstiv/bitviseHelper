import appModuleHandler
import NVDAObjects.IAccessible.sysListView32
class AppModule(appModuleHandler.AppModule):
	def event_NVDAObject_init(self, obj):
		if isinstance(obj, NVDAObjects.IAccessible.sysListView32.List) and obj.name=='List1':
			obj.name = obj.parent.next.name
