from sqlalchemy import Column, Integer, Text, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

Base = declarative_base()

class Person(Model):
    person_id = Column(Integer, nullable=False, primary_key=True)
    year_of_birth = Column(Integer, nullable=False)
    month_of_birth = Column(Integer)
    day_of_birth = Column(Integer)
    death_date =Column(Integer)
    gender_value = Column(String(50))
    rave_value = Column(String(50))
    ethnicity_value = Column(String(50))


class Visit_occurrence(Model):
    visit_occurrence_id = Column(Integer, nullable=False, primary_key=True)
    person_id = relationship("person", 
                        backref=backref('visit_person_id', cascade='all, delete-orphan'))
    visit_start_date = Column(Date)
    care_site_nm = Column(Text)
    visit_type_value = Column(String(50))


class Drug_exposure(Model):
    drug_exposure_id = Column(Integer, nullable=False, primary_key=True)
    person_id = relationship("person", 
                        backref=backref('drug_person_id', cascade='all, delete-orphan'))
    drug_exposure_start_date = Column(Date, nullable=False)
    drug_value = Column(Text)
    route_value = Column(String(50))
    dose_value = Column(String(50))
    unit_value = Column(String(50))
    visit_occurrence_id = relationship("drug_visit_occurrence",
                                    backref=backref('drug_person_id', cascade='all, delete-orphan'))
    

class Condition_occurrence(Model):
    condition_occurrence_id = Column(Integer, nullable=False, primary_key=True)
    person_id = relationship("person", 
                        backref=backref('condition_person_id', cascade='all, delete-orphan'))
    condition_start_date = Column(Date, nullable=False)
    condition_value = Column(Text)
    visit_occurrence_id = relationship("condition_visit_occurrence",
                                    backref=backref('drug_person_id', cascade='all, delete-orphan'))
    
    