from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from pydantic import BaseModel
from models import Student, StudentUpdate

router = APIRouter()
class Id(BaseModel):
    id: str 

@router.get("/",response_description="An API to find a list of students.", response_model=List[Student])
async def get_Students(req: Request, response: Response, age: str | None = None, country : str | None = None):
    q= {}
    if country:
        q["address.country"]={"$eq": country}
    if age is not None:
        q["age"]={"$eq": int(age)}
    print(age , country)
    students = list(req.app.database["students"].find(q))
    return students

@router.get("/{id}", response_description="Get a single student by id", response_model=Student)
async def find_student(id: str, req: Request):
    if (student := req.app.database["students"].find_one({"_id": id})) is not None:
        return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")

@router.put("/{id}", response_description="Update a Student", response_model=Student)
async def update_student(id: str, req: Request, student: StudentUpdate = Body(...)):
    student = {k: v for k, v in student.dict().items() if v is not None}
    if any(not v for v in student.values()):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Empty values are not allowed")
    existingStudent = req.app.database["students"].find_one({"_id": id})
    if(existingStudent is None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")
    if len(student) >= 1:
        update_result = req.app.database["students"].update_one(
            {"_id": id}, {"$set": student}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")

    if (
        existing_student := req.app.database["students"].find_one({"_id": id})
    ) is not None:
        return existing_student




@router.post("/",response_description="API to create a student in the system.", status_code=status.HTTP_201_CREATED, response_model=Id)
async def create_Student(req: Request, res: Response, student: Student = Body(...)):
    student = jsonable_encoder(student)
    new_student = req.app.database["students"].insert_one(student)
    createdStudent = req.app.database["students"].find_one({"_id": new_student.inserted_id})
    return {"id": str(createdStudent["_id"])}

@router.delete('/', response_description="API to delete a student in the system")
async def delete_student(req: Request, res: Response):
    result = req.app.database["students"].delele_one({"_id", id})
    
    if result.deleted_count == 1:    
        res.status_code = status.HTTP_204_NO_CONTENT
        return res

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")