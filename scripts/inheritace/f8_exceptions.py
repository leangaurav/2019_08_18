class AppError(Exception):
    pass

class AError(AppError):
    pass
    
class BError(AppError):
    pass
    
class CError(AppError):
    pass
  
e = [AError, BError, CError]

for ex in e:
    try:
        print("Raising ", ex)
        raise ex
    except AError:
        print("Got AError")
    except BError:
        print("Got BError")
    except AppError:
        print("Got AppError")
    except Exception:
        print("Some Exception")
        