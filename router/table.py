from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/table",
)


@router.put("/append/{entity}")
def append(entity: str):
    match entity:
        case "row":
            pass
        case _:
            return JSONResponse(content=f"Unknown entity '{entity}'", status_code=418)
    return JSONResponse(content=f"Successfully appended '{entity}'", status_code=200)
