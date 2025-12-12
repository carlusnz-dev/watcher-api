import uuid
from extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Text, ForeignKey, Uuid

class Monitor(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(String(80))
  url: Mapped[str] = mapped_column(String(255), unique=True)
  frequency: Mapped[int] = mapped_column(Integer, nullable=True)
  status: Mapped[int] = mapped_column(Integer, nullable=True)
  description: Mapped[str] = mapped_column(Text, nullable=True)
  
class Log(db.Model):
  id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4, unique=True)
  log: Mapped[str] = mapped_column(Text, nullable=True)
  monitor_id: Mapped[int] = mapped_column(ForeignKey("monitor.id"))
  status: Mapped[int] = mapped_column(Integer, nullable=True)