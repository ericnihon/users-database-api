from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID

from models import User, Gender, Role, UpdateUser

app = FastAPI()

db: List[User] = [
	User(
		id=UUID("e200490e-901f-493e-b810-689b81f61ede"),
		first_name="Kazuma",
		last_name="Oike",
		gender=Gender.male,
		roles=[Role.student]
		),
	User(
		id=UUID("37cc00e9-8f5e-4dc6-92ba-c752a98cda87"),
		first_name="Jeong",
		last_name="Kim",
		gender=Gender.other,
		roles=[Role.admin, Role.teacher]
		),
	User(
		id=UUID("9697e27f-3041-494c-9b90-7011166b76f3"),
		first_name="Karin",
		last_name="Fujiwara",
		middle_name="Mayu",
		gender=Gender.female,
		roles=[Role.assistant]
		)
]

@app.get("/")
async def fetch_users():
	return db


@app.post("/add")
async def register_user(user: User):
	db.append(user)
	return {"id": user.id}


@app.delete("/{user_id}")
async def delete_user(user_id: UUID):
	for user in db:
		if user.id == user_id:
			db.remove(user)
			return
	raise HTTPException(
		status_code=404,
		detail=f"user with id: {user_id} does not exist."
	)


@app.put("/{user_id}")
async def update_user(user_id: UUID, new_user_info: UpdateUser):
	for user in db:
		if user.id == user_id:
			if new_user_info.first_name:
				user.first_name = new_user_info.first_name
			if new_user_info.last_name:
				user.last_name = new_user_info.last_name
			if new_user_info.middle_name:
				user.middle_name = new_user_info.middle_name
			if new_user_info.gender:
				user.gender = new_user_info.gender
			if new_user_info.roles:
				user.roles = new_user_info.roles
			return
	raise HTTPException(
		status_code=404,
		detail=f"user with id: {user_id} does not exist."
	)
