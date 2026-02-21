import adsk.core, adsk.fusion, traceback

def run(context):
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent

        # Create a sketch on the XY plane
        sketch = root.sketches.add(root.xYConstructionPlane)

        # Center point at origin
        center = adsk.core.Point3D.create(0, 0, 0)

        # Create a circle with radius = 5 mm (10 mm diameter)
        sketch.sketchCurves.sketchCircles.addByCenterRadius(
            center,
            5
        )

        sketch.name = "10mm Circle"

    except:
        if ui:
            ui.messageBox(traceback.format_exc())

def stop(context):
    pass
