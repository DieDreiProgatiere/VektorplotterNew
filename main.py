
from vector3Dclass import Vector3D
try:
    from pointclass import Point
except Exception:
    pass
from lineclass import Line
from planeclass import Plane
from colorAssignclass import ColorAssign
from nameAssignclass import NameAssign
from listclass import ObjectLists
from solvers import Solvers

VecList = []
PoiList = []
LinList = []
PlaList = []

running = True

while running:
    for element in ObjectLists.getObjDict():
        print(" --- "+str(element))
    UserInput = input(
        """Nächste Operation [NewVec;AddVec;ScalMultVec;VecMultVecScal;VecMultVecCro;NewPoi;NewLin;NewPla;ConvertPlaToHess;X]: """
        )
    
    if UserInput == "NewVec":
        VecList.append(Vector3D(input("x = "), input("y = "), input("z = "), input("Name = ")))
        print(str(VecList[-1]))
    elif UserInput == "AddVec":
        Vec1 = Vector3D(input("x = "), input("y = "), input("z = "), input("Name = "))
        Vec2 = Vector3D(input("x = "), input("y = "), input("z = "), input("Name = "))
        print("Ergebnis: " + str(Vec1.add(Vec2)))
    elif UserInput == "ScalMultVec":
        Vec1 = Vector3D(input("x = "), input("y = "), input("z = "), input("Name = "))
        scal = float(input("Scalar: "))
        print("Ergebnis: " + str(Vec1.scalarMultiplication(scal)))
    elif UserInput == "VecMultVecScal":
        Vec1 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        Vec2 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        print("Ergebnis: " + str(Vec1.scalarProduct(Vec2)))
    elif UserInput == "VecMultVecCro":
        Vec1 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        Vec2 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        print("Ergebnis: " + str(Vec1.vectorProduct(Vec2)))
    elif UserInput == "NewPoi":
        PoiList.append(Point(input("x = "),input("y = "),input("z = "),input("Name = ")))
        print(str(PoiList[-1]))
    elif UserInput == "NewLin":
        print("Position Vector: ")
        Vec1 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        print("Direction Vector: ")
        Vec2 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        name = input("Name: ")
        LinList.append(Line(Vec1, Vec2, name, (0, 0, 0)))
        print(str(LinList[-1]))
    elif UserInput == "NewPla":
        print("Position Vector: ")
        Vec1 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        print("Direction Vector One: ")
        Vec2 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        print("Direction Vector Two: ")
        Vec3 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        name = input("Name: ")
        PlaList.append(Plane.parameterForm(Vec1, Vec2, Vec3, name, (0, 0, 0)))
        print(str(PlaList[-1]))
    elif UserInput == "ConvertPlaToHess":
        print("Position Vector: ")
        Vec1 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        print("Direction Vector One: ")
        Vec2 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        print("Direction Vector Two: ")
        Vec3 = Vector3D(input("x = "),input("y = "),input("z = "),input("Name = "))
        name = input("Name: ")
        PlaList.append(Plane.parameterForm(Vec1, Vec2, Vec3, name, (0, 0, 0)))
        print(str(PlaList[-1].convertToHessianNormalForm()))
    elif UserInput == "Schnittgerade":
        ebene1 = Plane.coordinateForm(Vector3D(-2,1,-3),7)
        ebene = Plane.coordinateForm(Vector3D(3,-2,1),4)
        print(Solvers.schnittgerade(ebene,ebene1))
    elif UserInput == "X":
        running = False
    else:
        print("Uberprüfen Sie bitte ihre Eingabe!")
        print("")

plane3 = Plane.normalForm(Vector3D(3,3,3),Vector3D(5,6,7))
plane4 = Plane.parameterForm(Vector3D(3,3,3),Vector3D(5,6,7),Vector3D(24,3,2))
