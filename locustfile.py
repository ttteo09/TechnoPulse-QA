import random
from locust import HttpUser, task, between

class TechnoPulseUser(HttpUser):
    # Fiecare utilizator simulat va aștepta între 1 și 3 secunde între acțiuni
    wait_time = between(1, 3)

    @task(3)
    def stream_track(self):
        """
        Simulează ascultarea unui stream techno.
        Ponderea (3) înseamnă că această acțiune este de 3 ori mai frecventă.
        """
        track_id = random.randint(100, 999)
        self.client.get(f"/v1/tracks/stream/{track_id}", name="/v1/tracks/stream/[id]")

    @task(1)
    def analyze_bpm(self):
        """
        Simulează trimiterea unei cereri de calculare BPM.
        """
        payload = {
            "track_name": f"techno_set_{random.randint(1, 50)}.wav",
            "bpm_target": 140
        }
        self.client.post("/v1/audio/analyze", json=payload, name="/v1/audio/analyze")