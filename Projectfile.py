import json

class TherapySession:
    def __init__(self, session_id, athlete_id, date, duration):
        self.session_id = session_id
        self.athlete_id = athlete_id
        self.date = date
        self.duration = duration

    def _str_(self):
        return f"Session ID: {self.session_id}, Athlete ID: {self.athlete_id}, Date: {self.date}, Duration: {self.duration} minutes"

class TherapyScheduler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sessions = self.load_sessions()

    def load_sessions(self):
        try:
            with open(self.file_path, 'r') as file:
                sessions_data = json.load(file)
                return [TherapySession(**data) for data in sessions_data]
        except FileNotFoundError:
            return []

    def save_sessions(self):
        sessions_data = [{'session_id': session.session_id,
                          'athlete_id': session.athlete_id,
                          'date': session.date,
                          'duration': session.duration} for session in self.sessions]
        with open(self.file_path, 'w') as file:
            json.dump(sessions_data, file)

    def create_session(self, athlete_id, date, duration):
        session_id = len(self.sessions) + 1
        session = TherapySession(session_id, athlete_id, date, duration)
        self.sessions.append(session)
        self.save_sessions()
        return session

    def update_session(self, session_id, new_date, new_duration):
        for session in self.sessions:
            if session.session_id == session_id:
                session.date = new_date
                session.duration = new_duration
                self.save_sessions()
                return True
        return False

    def delete_session(self, session_id):
        self.sessions = [session for session in self.sessions if session.session_id != session_id]
        self.save_sessions()

    def display_sessions(self):
        if not self.sessions:
            print("No sessions scheduled.")
        else:
            print("Scheduled Sessions:")
            for session in self.sessions:
                print(session)

class OutcomeTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.outcomes = self.load_outcomes()

    def load_outcomes(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_outcomes(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.outcomes, file)

    def track_therapy_outcomes(self, session_id, outcome_data):
        self.outcomes[session_id] = outcome_data
        self.save_outcomes()

    def get_outcome(self, session_id):
        return self.outcomes.get(session_id, None)

if __name__ == '__main__':
    scheduler = TherapyScheduler("sessions.json")
    tracker = OutcomeTracker("outcomes.json")
    
    while True:
        print("\n1. Schedule a therapy session")
        print("2. Update a therapy session")
        print("3. Delete a therapy session")
        print("4. View scheduled sessions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            athlete_id = int(input("Enter athlete ID: "))
            date = input("Enter session date (YYYY-MM-DD): ")
            duration = int(input("Enter session duration (minutes): "))
            scheduler.create_session(athlete_id, date, duration)
            print("Session scheduled successfully.")

        elif choice == "2":
            session_id = int(input("Enter session ID to update: "))
            new_date = input("Enter new date (YYYY-MM-DD): ")
            new_duration = int(input("Enter new duration (minutes): "))
            if scheduler.update_session(session_id, new_date, new_duration):
                print("Session updated successfully.")
            else:
                print("Session not found.")

        elif choice == "3":
            session_id = int(input("Enter session ID to delete: "))
            if scheduler.delete_session(session_id):
                print("Session deleted successfully.")
            else:
                print("Session not found.")

        elif choice == "4":
            scheduler.display_sessions()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")