"""Local, synthetic-data patient intake demo. No API calls or file storage."""


def ask(prompt: str) -> str:
    answer = input(f"{prompt}: ").strip()
    return answer or "Not provided"


def main() -> None:
    print("PATIENT INTAKE DEMO — FICTIONAL ANSWERS ONLY")
    print("Do not enter real patient information. Nothing is saved or sent to an API.")
    print("This demo does not assess emergencies or provide medical advice.\n")

    case = {
        "Symptoms": ask("What symptoms are you feeling"),
        "Symptom start / duration": ask("When did they start, or how long have they lasted"),
        "Age": ask("Age"),
        "Sex / gender (if relevant)": ask("Sex or gender, as the patient describes it"),
        "Past conditions": ask("Past diseases or health conditions"),
        "Current medicines and doses": ask("Current medicines and dosage for each"),
        "Allergies": ask("Medicine or other allergies"),
        "Heart rate": ask("Heart rate and unit (for example, 88 bpm)"),
        "Blood pressure": ask("Blood pressure and unit (for example, 120/80 mmHg)"),
        "Glucose": ask("Glucose reading and unit (for example, 110 mg/dL)"),
        "Vitals source / time": ask("Monitor or report source and measurement time"),
    }

    print("\nCLINICIAN HANDOFF — FACTUAL INTAKE ONLY")
    for label, value in case.items():
        print(f"{label}: {value}")
    print("\nAssessment: Not performed by this demo.")
    print("Diagnosis / emergency status: Not assessed; clinician review required.")
    print("No information was saved or sent to Sarvam.")


if __name__ == "__main__":
    main()

