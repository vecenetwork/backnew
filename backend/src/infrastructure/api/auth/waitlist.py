from fastapi import APIRouter, BackgroundTasks, status

from app.exceptions import ApiException
from app.schema.waitlist import WaitlistData
from infrastructure.api.dependencies import waitlist_service_dep

router = APIRouter()


@router.post("/waitlist", status_code=status.HTTP_204_NO_CONTENT)
async def join_waitlist(
    waitlist_service: waitlist_service_dep,
    background_tasks: BackgroundTasks,
    waitlist_data: WaitlistData,
):
    try:
        await waitlist_service.join_waitlist(waitlist_data)
    except ApiException as e:
        e.raise_http_exception()

    background_tasks.add_task(
        waitlist_service.send_verification_email, waitlist_data.email,
    )
