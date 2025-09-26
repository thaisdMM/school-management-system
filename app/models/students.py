"""
Student model for the school management system.
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Student(Base):
    """
    Represents a student in the school management system.

    Attributes:
        id (int): Unique identifier for the student
        name (str): Student's full name
        registration_number (int): Unique registration number for the student
        created_at (datetime): Timestamp when the student was created
        updated_at (datetime): Timestamp when the student was last updated
    """

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    registration_number = Column(Integer, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship
    enrollments = relationship("Enrollment", back_populates="student")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', registration_number={self.registration_number})>"

    def __str__(self):
        return f"Student: {self.name} (ID: {self.id}, Registration: {self.registration_number})"
