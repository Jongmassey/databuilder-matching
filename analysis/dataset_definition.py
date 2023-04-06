from databuilder.ehrql import Dataset
from databuilder.query_language import table_from_file, PatientFrame, Series
from databuilder.tables.beta.tpp import patients, practice_registrations
from datetime import date


@table_from_file("output/matched_cases_stp.csv")
class matched_cases(PatientFrame):
    patient_id = Series(int)
    n = Series(int)
    text = Series(str)


dataset = Dataset()
registration = practice_registrations

dataset.define_population(
    (patients.age_on(date.today()) >= 18)
    & registration.exists_for_patient()
    & matched_cases.exists_for_patient()
)
