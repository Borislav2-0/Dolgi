def introspection_info(obj):
    info = {}
    info['Type'] = type(obj).__name__
    info['Attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['Methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['Module'] = obj.__class__.__module__

    if isinstance(obj, dict):
        info['Keys'] = [key for key in obj.keys()]
        info['Values'] = [value for value in obj.values()]

    return info


number_info = introspection_info(42)
print(number_info)
