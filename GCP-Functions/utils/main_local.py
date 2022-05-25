from src.main import file_trigger

if __name__ == '__main__':
    
    event = {
        "project" : "",
        "bucket" : "",
        "name" : ""
    }
    
    context = Context(event_Id = 3345435,
                      timestamp = "20220523120065",
                      event_type = "google.storage.object.finalize",
                      resource = "storage")
    
    file_trigger(event, context)
