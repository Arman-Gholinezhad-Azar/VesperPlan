from enum import Enum

class TaskStatus(Enum):
    
    DONE = "done"
    PENDING = "pending"
    DELETED = "deleted" # recoverable