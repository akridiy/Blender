import bpy

def toggle_render_visibility():
    """
    Toggles render visibility for objects and collections that are hidden in viewport
    """
    objects_affected = 0
    collections_affected = 0
    
    # Process objects in scene
    for obj in bpy.context.scene.objects:
        if obj.hide_get():
            obj.hide_render = True
            objects_affected += 1
            print(f"Object {obj.name} - hidden in render")
    
    # Process collections using view_layer
    def process_layer_collection(layer_collection):
        nonlocal collections_affected
        
        # Check if collection is hidden in viewport
        if layer_collection.hide_viewport:
            # Get the actual collection
            collection = layer_collection.collection
            collection.hide_render = True
            collections_affected += 1
            print(f"Collection {collection.name} - hidden in render")
        
        # Process child collections
        for child in layer_collection.children:
            process_layer_collection(child)
    
    # Start with the main layer collection
    view_layer = bpy.context.view_layer
    process_layer_collection(view_layer.layer_collection)
    
    print(f"\nTotal affected:")
    print(f"Objects: {objects_affected}")
    print(f"Collections: {collections_affected}")

# Run the function
toggle_render_visibility()