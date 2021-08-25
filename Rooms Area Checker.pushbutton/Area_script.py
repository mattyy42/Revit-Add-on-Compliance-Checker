from Autodesk.Revit.DB import FilteredElementCollector,BuiltInCategory
__title__='Rooms \n Area Cheker'
doc= __revit__.ActiveUIDocument.Document
collector=FilteredElementCollector(doc)
collector.OfCategory(BuiltInCategory.OST_Rooms)
collector.WhereElementIsNotElementType()
print('Checking Areas of all available rooms, All rooms have to have a minimum of 6 meter square area size')
for rooms in collector:
	Room_area=rooms.LookupParameter('Area')
	Room_area_to_Double=Room_area.AsDouble()
	if (Room_area_to_Double > 6.0):	
		print(rooms)
		print(str(Room_area_to_Double)+ "  feet Square Parameter Check Pass")
	else:
		print (rooms)
		print(str(Room_area_to_Double)+ "  feet Square Parameter Check Fail for the Room Above")
#Done by Michael Matwose
