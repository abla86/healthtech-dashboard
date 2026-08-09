from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal

app = FastAPI(
    title="HealthTech Device API",
    version="1.0.0",
    description="REST API for monitoring simulated healthcare technology devices."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Device(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=100)
    type: str = Field(min_length=2, max_length=100)
    status: Literal["Online", "Offline", "Maintenance"]
    battery: int = Field(ge=0, le=100)

class DeviceCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    type: str = Field(min_length=2, max_length=100)
    status: Literal["Online", "Offline", "Maintenance"] = "Online"
    battery: int = Field(ge=0, le=100)

devices = [
    Device(id=1, name="Vital Sensor 01", type="Sensor", status="Online", battery=87),
    Device(id=2, name="Home Monitor 02", type="Monitor", status="Offline", battery=34),
    Device(id=3, name="Gateway 01", type="Gateway", status="Online", battery=100),
    Device(id=4, name="Medication Hub", type="Medication", status="Maintenance", battery=61),
]

@app.get("/")
def root():
    return {
        "service": "HealthTech Device API",
        "status": "running",
        "docs": "/docs"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/devices", response_model=list[Device])
def get_devices():
    return devices

@app.get("/devices/{device_id}", response_model=Device)
def get_device(device_id: int):
    for device in devices:
        if device.id == device_id:
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.post("/devices", response_model=Device, status_code=201)
def create_device(device: DeviceCreate):
    new_id = max((item.id for item in devices), default=0) + 1
    new_device = Device(id=new_id, **device.model_dump())
    devices.append(new_device)
    return new_device

@app.delete("/devices/{device_id}", status_code=204)
def delete_device(device_id: int):
    for index, device in enumerate(devices):
        if device.id == device_id:
            devices.pop(index)
            return
    raise HTTPException(status_code=404, detail="Device not found")
