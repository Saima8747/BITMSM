class TherapySession:
    def __init__(self, session_id, athlete_id, date, duration):
        self.session_id = session_id
        self.athlete_id = athlete_id
        self.date = date
        self.duration = duration
    def __str__(self):
        return f"Session ID: {self.session_id}, Athlete ID: {self.athlete_id}, Date: {self.date}, Duration: {self.duration} minutes"   

class TherapyScheduler:
    def __init__(self):
        self.sessions = []

    def create_session(self, session_id, athlete_id, date, duration):
        session = TherapySession(session_id, athlete_id, date, duration)
        self.sessions.append(session)

    def read_sessions(self):
        return self.sessions

    def update_session(self, session_id, new_date, new_duration):
        for session in self.sessions:
            if session.session_id == session_id:
                session.date = new_date
                session.duration = new_duration

    def delete_session(self, session_id):
        self.sessions = [session for session in self.sessions if session.session_id != session_id]
    
    def schedule_physical_therapy(self, athlete_id):
        # Implementation of scheduling logic
        pass

class OutcomeTracker:
    def __init__(self):
        self.outcome_data = {}

    def track_therapy_outcomes(self, outcome_data):
        # Implementation of tracking outcomes logic
        pass

# Example usage:
scheduler = TherapyScheduler()

# Creating sessions
scheduler.create_session(1, 101, "2024-05-01", 60)
scheduler.create_session(2, 102, "2024-05-03", 45)

# Reading sessions
#print("Sessions:", scheduler.read_sessions())

# Updating session
scheduler.update_session(1, "2024-05-02", 75)
#print("Updated Sessions:", scheduler.read_sessions())

# Deleting session
scheduler.delete_session(2)
#print("Sessions after deletion:", scheduler.read_sessions())
import unittest

class TherapySession:
    def __init__(self, session_id, athlete_id, date, duration):
        self.session_id = session_id
        self.athlete_id = athlete_id
        self.date = date
        self.duration = duration

class TherapyScheduler:
    def __init__(self):
        self.sessions = []

    def schedule_physical_therapy(self, athlete_id, date, duration):
        session_id = len(self.sessions) + 1
        session = TherapySession(session_id, athlete_id, date, duration)
        self.sessions.append(session)
        return session

    def delete_session(self, session_id):
        for session in self.sessions:
            if session.session_id == session_id:
                self.sessions.remove(session)
                return True
        return False

class OutcomeTracker:
    def __init__(self):
        self.outcomes = {}

    def track_therapy_outcomes(self, session_id, outcome_data):
        self.outcomes[session_id] = outcome_data

    def get_outcome(self, session_id):
        return self.outcomes.get(session_id, None)

class TestTherapySystem(unittest.TestCase):
    def setUp(self):
        self.scheduler = TherapyScheduler()
        self.tracker = OutcomeTracker()

    def test_schedule_session(self):
        session = self.scheduler.schedule_physical_therapy(1, "2024-04-30", 60)
        self.assertEqual(session.athlete_id, 1)
        self.assertEqual(session.date, "2024-04-30")
        self.assertEqual(session.duration, 60)

    def test_delete_session(self):
        session = self.scheduler.schedule_physical_therapy(1, "2024-04-30", 60)
        self.assertTrue(self.scheduler.delete_session(session.session_id))

    def test_track_outcome(self):
        session = self.scheduler.schedule_physical_therapy(1, "2024-04-30", 60)
        self.tracker.track_therapy_outcomes(session.session_id, "Good progress")
        outcome = self.tracker.get_outcome(session.session_id)
        self.assertEqual(outcome, "Good progress")

if __name__ == '__main__':
    unittest.main(verbosity=4)