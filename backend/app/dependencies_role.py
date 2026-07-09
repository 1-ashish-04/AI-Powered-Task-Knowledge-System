from fastapi import Depends, HTTPException

from app.dependencies import get_current_user


def admin_required(current_user=Depends(get_current_user)):

    if current_user.role.role_name != "Admin":
        raise HTTPException(
            status_code=403,
            detail="Only Admin allowed."
        )

    return current_user