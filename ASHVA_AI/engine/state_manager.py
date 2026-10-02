from schemas.episode import Episode


class StateManager:

    def __init__(self, episode: Episode):
        self.episode = episode

    def validate_scene_continuity(self, previous_scene, current_scene):

        if previous_scene is None:
            return True

        previous_end = previous_scene.end_state
        current_start = current_scene.start_state

        if previous_end != current_start:
            raise ValueError(
                f"Continuity violation between "
                f"Scene {previous_scene.scene_id} and "
                f"Scene {current_scene.scene_id}"
            )

        return True