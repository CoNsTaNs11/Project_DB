from .events_crud import (
    create_event,
    get_events,
    get_event,
    update_event,
    delete_event
)
from .reports_crud import (
    create_report,
    get_reports,
    get_report,
    update_report,
    delete_report
)
from .correspondents_crud import (
    create_correspondent,
    get_correspondents,
    get_correspondent,
    update_correspondent,
    delete_correspondent
)

__all__ = [
    "create_event", "get_events", "get_event", "update_event", "delete_event",
    "create_report", "get_reports", "get_report", "update_report", "delete_report",
    "create_correspondent", "get_correspondents", "get_correspondent",
    "update_correspondent", "delete_correspondent"
]
